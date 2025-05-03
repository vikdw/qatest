import subprocess


#initilizing the count variable.
count=0

#for loop 0 to 1233(1234 times).
for x in range(1234):
    #running Binary and saving o/p to variable
    output = subprocess.run(["/home/vikasdw/Downloads/qatest-linux-amd64", "run"],capture_output=True, text=True).stdout

    #checking if op is not None
    if output is not None:
        output= output.strip()
        #checking if op is fizz and incrementing the counter
        if output=="fizz":
            count=count+1

#saving o/p to file.
with open('output.txt','w') as file:
    print("saving o/p to file.")
    file.write(f"fizz appear: {count}/1234 times.")


print(f"fizz appear: {count}/1234 times.")
