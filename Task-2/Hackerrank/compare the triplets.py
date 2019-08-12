
# Complete the compareTriplets function below.
def compareTriplets(a, b):

     Alice = 0
     Bob = 0
     for i in range(0, len(a)):
         if a[i]>b[i]:
             Alice += 1
         if a[i]<b[i]:
             Bob += 1
     return [Alice, Bob]


    
