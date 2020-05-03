from ultrasonic import dustbin as db

b=db() # declare an object fo dustbin type
print("intially filled % =",b.percentage_Filled()) #  fucntion to print the percent dustbin  is filled
print("intial stored depth in cm=",b.initial_Depth) # prints the initial depth being used right now for calculations(-1 represents not yet initialized)
b.update_Initial() # update the initial depth of the dustbin with the current sensor value or configuration
print("current height in cm=",b.current_Depth()) # display the current depth/sensor height
print("percentage filled now=",b.percentage_Filled()) #  fucntion to print the percent dustbin  is filled

    
