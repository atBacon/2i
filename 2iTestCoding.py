#In a language of your choice, using all best practice principles you’re aware of,
#could you please provide code that iterates in multiples of A until X,
#then in multiples of A + 1 until 2X,
#then multiples of A + 2 until 3X.

#initialise variables and get A and X
MultiplierA=0
LimitX=0
MultiplierA=int(input("Enter the mulitiplier, A.>"))
LimitX=int(input("Enter the Limit, X.>"))
NewLimit=LimitX
#Newlimit is created so that it can be looped and always add original limit
#(because doubling twice is 4X rather than 3X)

#setting expectations
if 2*(LimitX)>(MultiplierA):
    print("limit is too high. Expect underwhelming results")

#Outputs are printed to better keep track
for i in range(3):
    print("New Sequence, A is",(MultiplierA),"X is",(NewLimit))
    OutputNumber=int(0)
    #output is reset each time X and A change

    while (OutputNumber)<=(NewLimit):
        print(OutputNumber)
        OutputNumber = OutputNumber+MultiplierA
        #<= used since limit can include itself

    MultiplierA=MultiplierA+1
    NewLimit=NewLimit+LimitX
    #iterating variables
