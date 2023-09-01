import numpy as np

# created a random vector of size 20 with float values between 1 and 20
ranvec = np.random.uniform(low=1, high=20, size=20)

# reshape the array to 4 by 5 using reshape method
mat45 = ranvec.reshape(4, 5)
print(mat45)
print("\n Replacing the maximum in each row by 0 using where method\n")
# replace the max in each row by 0 using where method
mat45 = np.where(mat45 == np.amax(mat45, axis=1, keepdims=True), 0, mat45)
print(mat45)