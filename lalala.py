import math
from posixpath import join
import codecs
w = u"\u221a"

def calc(n, m, r):
    if n==m:
        return r
    elif m=="circumference":
        r /= (2*math.pi)
    elif m=="area":
        r = math.sqrt(r/math.pi)
    elif m=="diameter":
        r /= 2
    if n == "radius":
        return r
    elif n == "circumference":
        return 2*math.pi*r
    elif n=="area":
        return math.pi*r*r
    elif n=="diameter":
        return 2*math.pi

def expl(a, c, d):
        if a=="radius":
            print("radius =", c)
        elif a=="circumference":
            print("circumference = 2 x Pi x radius")
            print("circumference = 2 x", math.pi, "x", c)
            print("circumference =", math.pi, "x", 2*c)
            print("circumference = ", d)
        elif a=="area":
            print("area = Pi x radius x radius")
            print("area =", math.pi, c, "x", c)
            print("area =", math.pi, "x", c*c)
            print("area =", d)
        elif a=="diameter":
            print("diameter = 2 x radius")
            print("diameter = 2 x", c)
            print("diameter =", d)
        print("Thanks for using :)")
    
def derrad(i, j, k):
    if i==j:
        print(j, "=", k, "(given)")
        print(i, "=", j, "=", k)
    elif j=="circumference":
        print("circumference = 2 x Pi x radius =", k)
        print("radius = circumference", chr(247) ,"(2 x Pi) =", k, chr(247), "(2 x Pi) \n =", k, chr(247), 2*math.pi)
        k /= (2*math.pi)
        print ("=", k)
    elif j=="area":
        print("area = Pi x radius x radius =", k)
        print(join("radius = ", w,"(area ", chr(247)," Pi) = ", w, "(", str(k), " ", chr(247), " ", str(math.pi), ")").replace("/", ""))
        print(join("= ", w, "(", str(k/math.pi), ")").replace('/', ''))
        k = math.sqrt(k/math.pi)
        print("=", k)
    elif j=="diameter":
        print("diameter = 2 x radius =", k)
        print("radius = diameter", chr(247), "2 =", k, "/ 2")
        k /= 2
        print("= ", k)
    expl(i, k, calc(i, "radius", k))

def code(reply):
    if reply=="ok" or reply=="yes":
        global x
        x = str(input("What would you like to calculate? (Enter 'radius', 'circumference', 'area', diameter') "))
        y = str(input(join("What value would you like to provide? (This value will be used to calculate the ", x, " of the circle, you may enter 'radius', 'circumference', 'area', or 'diameter') ").replace('/', '')))
        z = float(input(join("Enter the ", y, " of the circle: ").replace('/', '')))
        if ((x=="radius" or x=="circumference" or x=="area" or x=="diameter") and (y=="radius" or y=="circumference" or y=="area" or y=="diameter") and (type(z)==float)):
            print(x, "=", calc(x, y, z))
            reply = str(input("Would you like to know why? (reply with 'yes' or 'no') "))
            if reply=="yes":
                derrad(x, y, z)
            elif reply=="no":
                print("alright")
            else:
                print("I see you're a rebel, but you missed out on the explaination")
            o = str(input("Calculate something else? (reply with 'yes' or 'ok' to restart the code or something else to stop) "))
            code(o)
        else:
            print("enter valid values")
    else:
        try:
            if type(x)==str:
                print("thanks for using :) \nbye bye")
        except:
            o = str(input("Enter 'ok' if you wish to proceed with the code, entering anything else will stop the running window, remember to type in lowercase: "))
            if reply=="ok":
                code(o)
            else:
                print("Why did you even bother running the code if you didn't want to use it? Either way, bye bye.")

o = str(input("Use this to calculate the radius, circumference, area, or diameter of a circle.  (type 'ok' to continue) "))
code(o)
