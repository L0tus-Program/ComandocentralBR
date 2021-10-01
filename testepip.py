import os

result = None

def ipconfig():
    a = os.popen("systeminfo").read()  # os.popen(...).read()  
    return a

result = ipconfig()
os.system('cls')



print (result)
