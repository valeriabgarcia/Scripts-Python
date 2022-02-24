#exec(open("script1.py").read())
import script1

result2 = 8

if __name__ == '__main__':
    if(script1.func1() == result2):
        print("Result is true")
    else:
        print("Result is false")

script1.func1()