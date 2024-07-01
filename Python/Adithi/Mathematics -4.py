# Read input parameters from in.txt file
with open("in2.txt", "r") as file:
    l = file.readline().split(",")  # Read and split the line by comma
    a = int(l[0])
    b= int(l[1])

# Function to calculate and write mathematical tables

with open("out.txt", "w") as file:
    for i in range(a, b + 1):
            file.write(f"Table for {i}:\n")
            for j in range(1, 11):
                file.write(f"{i} x {j} = {i * j}\n")


# Write mathematical tables from start to end to out.txt
