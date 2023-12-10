import time

def calculateTime(func):
    def wrapper(nums):
         start=time.time()
         resultat= func(nums)
         end = time.time()
         print(func.__name__ + " runs in "+ str(end-start)+ " seconds.")
    return wrapper

@calculateTime
def carre (nums):
    resultat = list()
    for i in nums:
        resultat.append(i**2)
    return resultat


@calculateTime
def cube (nums):
    resultat = list()
    for i in nums:
        resultat.append(i**3)
    return resultat

cube(range(100000))
carre(range(100000))
