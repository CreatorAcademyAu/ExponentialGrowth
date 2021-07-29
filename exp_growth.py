stack_height = 0.0001
folds = 0
print("How many times do we need to fold a 0.1mm piece of paper to reach a particular height?")
target_height = input("What is your target height in metres?")

while stack_height < float(target_height):
    stack_height*=2
    folds+=1
    print('folds:',folds,'height:',stack_height)

print('the number of folds required is',folds)
