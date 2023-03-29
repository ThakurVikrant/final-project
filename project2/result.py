#Average score python program

print("Enter Marks Obtained in 3 test: ")

test1=int(input("enter a total number in test1::"))
test2=int(input("enter a total number in test2::"))
test3=int(input("enter a total number in test3::"))

total = test1+test2+test3
average_score = total/3

if average_score >= 90:
    letter_grade = 'A'
elif 80 <= average_score < 90:
    letter_grade = 'B'
elif 70 <= average_score < 80:
    letter_grade = 'C'
elif 60 <= average_score < 70:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print("Average score: {:.2f}".format(average_score))
print("Letter grade: {}".format(letter_grade))    