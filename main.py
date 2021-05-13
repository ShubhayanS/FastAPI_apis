from secrets import choice
import fastapi
import random
import string
from itertools import permutations

app = fastapi.FastAPI()


@app.get("/")
def calculate():
    return {
        "message":"Hello World",
        "status":"OK 404"
    }

@app.get("/math1/{nterms}")
def calculate(nterms:int):
    # first two terms
    n1, n2 = 0, 1
    count = 0
    list=[]
    status=""
    # check if the number of terms is valid
    if nterms <= 0:
        status="Error, Negative not allowed"
    elif nterms == 1:
        status="OK"
        list.append(n1)
    else:
        status="OK"
        while count < nterms:
            list.append(n1)
            nth = n1 + n2
            # update values
            n1 = n2 
            n2 = nth
            count += 1
    return {
        "status":status,
        "febonacci":list
    }


@app.get("/math2/{nterms}")
def calculate(nterms):
    nterms= int(nterms)
    # first two terms
    p = 1
    status=""
    # check if the number of terms is valid
    if nterms < 0:
        status="Error, Negative not allowed"
    else:
        status="OK"
        while(nterms!=0):
            p=nterms*p #multiply all factors of a number
            nterms=nterms-1
    return {
        "status":status,
        "factorial":p
    }



@app.get("/string1/{word}")
def calculate(word):
    return {
        "status":"OK",
        "length":len(word) #prints length of a string 
    }


@app.get("/string2/{letters}/{stringer}")
def calculate(letters:int,stringer:str):
    li=list(stringer) #converts input character to string
    newstr=""
    for i in range(letters):
        newstr+=str(random.choices(li)[0])#select characters of a input string till required length
    permutation = [''.join(p) for p in permutations(newstr)] #to find pnc of the generated string
    return {
        "status":"OK",
        "length":permutation
    }


