l = [1, 2, 3]  # Define the list outside the function (a global variable)

def func(n):
    # If you just want to loop over the list values you can do this:
    for i in n:
        print(i)

# To see results call the function and pass the list as an argument
print('Method 1: ')
func(l)


# Method 2:
print('Method 2: ')
def func2(n):
    # If you want both the index and the value use range(len(n)):
    for i in range(len(n)):
        print(f"Index: {i}, Value: {n[i]}")
        
func2(l)












