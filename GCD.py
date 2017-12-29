def main():
 print(gcd(125,100))
 for n in range(1,100000000000):
      if gcd(n**5-5,(n+1)**5-5)!=1:
          print("The GCD is:" ,gcd(n**5-5,(n+1)**5-5))
          print("N is:", n)
def gcd(a, b):

    if(b == 0):
        return a
    else:
        return gcd(b,a % b)

main()
