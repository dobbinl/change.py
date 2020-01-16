print("Please enter an amount in cents less than a dollar.")

num_in = int(input())  # how many quarters go go in to 87?
num_r = num_in % 25
num_Q = int((num_in-num_r)/25)

num_in = num_r
num_r = num_in % 10
num_D = int((num_in-num_r)/10)

num_in = num_r
num_r = num_in % 5
num_N = int((num_in-num_r)/5)

num_in = num_r
num_r = num_in % 1
num_P = int((num_in-num_r)/1)

print("Your change will be:")
print("Q:",num_Q)
print("D:",num_D)
print("N:",num_N)
print("P:",num_P)