#----------------------------------------------------------------------
#GCF.py
#Syjer Asuncion
#This program takes two integers and find their greatest common factor
#----------------------------------------------------------------------
def gcd(x,y):
    '''
    This function takes two integers and find their greatest common factor
    Inputs: The numbers entered by the user
            x (int)
            y (int)
    Returns:x (int) = The greatest common factor
    '''
    if y != 0: 
        r = x % y #recursive case
        x = y #recursive case
        y = r #recursive case
        x = gcd(x,y)  #recursive case
    return x# base case, if y == 0

# Takes user input
int1 = int(input("Enter the first number: "))
int2 = int(input("Enter the second number: "))
# Print output
print("The greatest common factor of " + str(int1) + " and " + str(int2)+ " is " + str(gcd(max(int1,int2),min(int1,int2))))
