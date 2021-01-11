f=input("Input your file: ")
fn=f.split(".")
file_ext=fn[-1]
if(file_ext=='py'):
    print("The extension is python")
elif(file_ext=='txt'):
    print("The extension is text")
else:
    print("The extension is",file_ext)
    
    
    
    
    OUTPUT:
    Input your file: abc.py
    The extension is python
