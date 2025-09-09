import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("apt-get install python")
    os.system("apt-get install python2")
    os.system("apt-get install python3")
    os.system("pip install requests")
    os.system("pip install fade")
elif c == "1":
    os.system("apt-get install python")
    os.system("apt-get install python2")
    os.system("apt-get install python3")
    os.system("pip3 install requests")
    os.system("pip3 install fade")
print("Done.")
