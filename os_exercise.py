import os

with open ("pdf.txt","w",encoding="UTF-8") as pdf_file:
    with open ("txt.txt","w",encoding="UTF-8") as txt_file:        
        for path,directories,files in os.walk("D:\Üniversite"):
            for l in files:
                if l.endswith(".pdf"):
                    pdf_file.write(l + "\n")
                elif l.endswith(".txt"):
                    txt_file.write(l + "\n")
            

