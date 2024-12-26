bmi = 84 / 1.65 ** 2
print(bmi)

print(int(bmi))   #flooring it to the lowest whole number

# we'll use round function: 0.5= it rounds up to the next whole number and when its below that it rounds upto the lower whole number

print(round(bmi))

#round func takes 2 inputs: one is the number you wanna round, second is the number of digits you want to round it to
print(round(bmi, 2))





#assaigning operators

score = 0

#user scores a point
#score = score + 1
score += 1
print(score)



#f string
score = 0 
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning} ")
