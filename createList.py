file_path = "mail9.txt"
with open(file_path, "w") as file:
    for i in range(10):  
        mails = str(i).zfill(1)  
        file.write(mails + "\n")

print("Done")