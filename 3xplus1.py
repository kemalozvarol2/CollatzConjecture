import matplotlib.pyplot as plt

starting_point = input('Enter starting number : ')

step_counter = 1
number = int(starting_point)
textmap = str(starting_point)
highest = 0
print(f'Step 0 : {number}')

steps = [0]
values = [number]

while number != 1:
    if number % 2 == 0:
        number = number / 2
        print(f"Step {step_counter} : {number}")
        if number > highest:
            highest = number
        values.append(number)
        textmap = textmap + ", " + str(number)
    else:
        number = (number * 3) + 1
        print(f"Step {step_counter} : {number}")
        if number > highest:
            highest = number
        values.append(number)
        textmap = textmap + ", " + str(number)
    steps.append(step_counter)
    step_counter = step_counter + 1

plt.plot(steps, values)

plt.xlabel('Step')
plt.ylabel('Value')

plt.title(f"{starting_point} 3x+1 problem\nHighest point = {highest}\nTotal Steps = {step_counter - 1}")


plt.show()

print(f'It took {step_counter - 1} steps to reach 1.')
print(f'Highest value : {highest}')