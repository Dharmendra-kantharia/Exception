# Always write suspicuous code in try block and handling it with Exception block.
# Code which are really need to excecute whether it is fail in Try or in Exception handling those code write in Finally.

try:
    a = 10
    print(a/0)
except Exception as e :
    print(e)
    print("This is my final code after handling an exception")

try :
    f = open("Dharmendra.txt","r")
except Exception as e:
    print(e)

try :
    f = open("Dharmendra.txt","r")
    f.write("This is my suspicuous code")
except Exception as e:
    print(e)
    print("This is not my suspicious set of the code")
finally:
    print("This block will be executed any time")


# Writing a Example code for understanding.

def askint():
    try:
        val = int(input("Please enter Integer value"))
    except:
        print("You have not enter Integer value Please try again")
        try:
            val = int(input("Please enter Integer value"))
        except:
            print("Yes we are able to identityfy your mistak")
    finally:
        print("Finaly will be executed anyhow")

    

    