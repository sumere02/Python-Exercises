from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.handlers.sha2_crypt import sha256_crypt
from functools import wraps

#User login decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash(message="Login first",category="danger")
            return redirect(url_for("login"))
    return decorated_function

#ArticleForm
class ArticleForm(Form):
    title = StringField(label="Title",validators=[validators.Length(min = 5,max = 25)])
    content = TextAreaField(label = "Content",validators=[validators.Length(min = 10)])

#RegisterForm
class RegisterForm(Form):
    name = StringField(label ="Name Surname",validators=[validators.Length(min = 4,max = 25)])
    username = StringField(label="ID",validators=[validators.Length(min = 4,max = 25),validators.DataRequired()])
    email = StringField(label = "Email",validators = [validators.Email(message = "Wrong email address"),validators.DataRequired()])
    password = PasswordField(label = "Password",validators = [validators.DataRequired(),validators.EqualTo(fieldname = "confirm",message = "Password does not match")])
    confirm = PasswordField(label = "Validate Password",validators=[validators.DataRequired()])

#LoginForm
class LoginForm(Form):
    username = StringField("ID",validators=[validators.DataRequired()])
    password = PasswordField("Password",validators=[validators.DataRequired()])

app = Flask(__name__)
app.secret_key = "SumerBlog"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "SumerBlog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

#Main Page
@app.route("/")
def index():
    return render_template("index.html")

#Register Page
@app.route("/register",methods = ["GET","POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users(name,email,username,password) VALUES(%s,%s,%s,%s)",(name,email,username,password))
        mysql.connection.commit()
        cursor.close()
        flash(message = "Registered succesfully",category="success")
        return redirect(url_for("login"))
    else:
        return render_template("register.html",form = form)

#Login Page
@app.route("/login",methods = ["GET","POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        username = form.username.data
        password = form.password.data
        cursor = mysql.connection.cursor()
        result = cursor.execute("SELECT * FROM users WHERE username = %s",(username,))
        data = cursor.fetchone()
        cursor.close()
        if result:
            if sha256_crypt.verify(password,data["Password"]):
                flash(message = "Welcome",category="success")
                session["logged_in"] = True
                session["username"] = username
                return redirect(url_for("index"))
            else:
                flash(message = "Incorrect password",category = "danger")
                return redirect(url_for("login")) 
        else:
            flash(message = "Incorrect ID",category = "danger")
            return redirect(url_for("login"))    
    else:
        return render_template("login.html",form = form)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))
#About Us Page

@app.route("/dashboard")
@login_required
def dashboard():
    cursor = mysql.connection.cursor()
    result = cursor.execute("SELECT * FROM articles WHERE Author = %s",(session["username"],))
    if result:
        articles = cursor.fetchall()
        cursor.close()
        return render_template("dashboard.html",articles = articles)
    else:
        return render_template("dashboard.html")

@app.route("/addarticle",methods = ["GET","POST"])
@login_required
def addarticle():
    form = ArticleForm(request.form)
    if request.method == "POST" and form.validate():
        title = form.title.data
        author = session["username"]
        content = form.content.data
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO articles(Title,Author,Content) VALUES (%s,%s,%s)",(title,author,content))
        mysql.connection.commit()
        cursor.close()
        flash(message = "Article added",category ="success")
        return redirect("dashboard")
    else:
        return render_template("addarticle.html",form = form)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/articles")
def articles():
    cursor = mysql.connection.cursor()
    result = cursor.execute("SELECT * FROM articles")
    if result:
        articles = cursor.fetchall()
        cursor.close()
        return render_template("articles.html",articles = articles)
    else:
        cursor.close()
        return render_template("articles.html")

#Article Page
@app.route("/article/<string:id>")
def detail(id):
    cursor = mysql.connection.cursor()
    result = cursor.execute("SELECT * FROM articles WHERE id = %s",(id,))
    if result:
        article = cursor.fetchone()
        cursor.close()
        return render_template("article.html",article = article)
    else:
        cursor.close()
        return render_template("article.html")

#Delete Article
@app.route("/delete/<string:id>")
@login_required
def delete(id):
    cursor = mysql.connection.cursor()
    result = cursor.execute("SELECT * FROM articles where id = %s",(id,))
    if result:
        content = cursor.fetchone()
        if content["Author"] == session["username"]:
            result = cursor.execute("DELETE FROM articles where id = %s",(id,))
            mysql.connection.commit()    
            cursor.close()
            flash(message="Article Deleted",category="info")
            return redirect(url_for("dashboard"))
        else:
            flash(message="Restricted File",category="info")
    else:
        flash(message="Article not exists",category="info")
    cursor.close()
    return redirect(url_for("index"))
#Update Article
@app.route("/update/<string:id>",methods = ["GET","POST"])
@login_required
def update(id):
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        result = cursor.execute("SELECT * FROM articles where id = %s",(id,))
        if result:
            article = cursor.fetchone()
            if article["Author"] == session["username"]:
                form = ArticleForm()
                form.title.data = article["Title"]
                form.content.data = article["Content"]
                cursor.close()
                return render_template("update.html",form = form)
            else:
                flash(message = "Restricted File",category = "info")          
        else:
            flash("Article not exists",category = "info")
        cursor.close()
        return redirect(url_for("index"))
    else:
        form = ArticleForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE articles SET Title = %s,Content = %s where id = %s",(title,content,id))
            mysql.connection.commit()
            cursor.close()
            flash("Article Updated",category = "info")
            return redirect(url_for("dashboard"))

#Search URL
@app.route("/search",methods = ["GET","POST"])
def search():
    if request.method == "GET":
        return redirect(url_for("index"))
    else:
        keyword = request.form.get("keyword")
        cursor = mysql.connection.cursor()
        result = cursor.execute("SELECT * FROM articles WHERE Title LIKE '%" + keyword + "%'")
        if result:
            articles = cursor.fetchall()
            cursor.close()
            return render_template("articles.html",articles = articles)
        else:
            flash(message = "Not Found",category="info")
            return redirect(url_for("articles"))
if __name__ == "__main__":
    app.run(debug = True)
