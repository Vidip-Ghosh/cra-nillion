from nada_dsl import * 
def fibonacci(): 
    n=10
    a=0
    b=1
    c=b
    count=0
    while count<n: 
        print(a)
        c=a+b
        a=b
        b=c
        count=count+1
    
if __name__=='__main__': 
    fibonacci()