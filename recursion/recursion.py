#Recursion function
def countdown(n):
    print(n)
    if n<=1:
        return
    else:
      countdown(n-1)

countdown(5)