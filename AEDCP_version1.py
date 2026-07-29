total_exercise_day = 0
yes_exercise_day = 1
no_exercise_day = 0

print("---------------------------")
print("Do you exercise on Monday?")
monday_exercise_answer = input("Yes or No :")
if monday_exercise_answer == "Yes":
    total_exercise_day = total_exercise_day + yes_exercise_day
elif monday_exercise_answer == "No":
    total_exercise_day = total_exercise_day + no_exercise_day
print("---------------------------")

print("Do you exercise on Tuesday?")
tuesday_exercise_answer = input("Yes or No :")
if tuesday_exercise_answer == "Yes":
    total_exercise_day = total_exercise_day + yes_exercise_day
elif tuesday_exercise_answer == "No":
    total_exercise_day = total_exercise_day + no_exercise_day
print("---------------------------")

print("Do you exercise on Wendsday?")
wendsday_exercise_answer = input("Yes or No :")
if wendsday_exercise_answer == "Yes":
    total_exercise_day = total_exercise_day + yes_exercise_day
elif wendsday_exercise_answer == "No":
    total_exercise_day = total_exercise_day + no_exercise_day
print("---------------------------")

print("Do you exercise on Thursday?")
thursday_exercise_answer = input("Yes or No :")
if thursday_exercise_answer == "Yes":
    total_exercise_day = total_exercise_day + yes_exercise_day
elif thursday_exercise_answer == "No":
    total_exercise_day = total_exercise_day + no_exercise_day
print("---------------------------")

print("Do you exercise on Friday?")
friday_exercise_answer = input("Yes or No :")
if friday_exercise_answer == "Yes":
    total_exercise_day = total_exercise_day + yes_exercise_day
elif friday_exercise_answer == "No":
    total_exercise_day = total_exercise_day + no_exercise_day
print("---------------------------")

print("Do you exercise on Saturday?")
saturday_exercise_answer = input("Yes or No :")
if saturday_exercise_answer == "Yes":
    total_exercise_day = total_exercise_day + yes_exercise_day
elif saturday_exercise_answer == "No":
    total_exercise_day = total_exercise_day + no_exercise_day
print("---------------------------")

print("Do you exercise on Sunday?")
sunday_exercise_answer = input("Yes or No :")
if sunday_exercise_answer == "Yes":
    total_exercise_day = total_exercise_day + yes_exercise_day
elif sunday_exercise_answer == "No":
    total_exercise_day = total_exercise_day + no_exercise_day
print("---------------------------")

print("Result")
if total_exercise_day == 0:
    print("You did not exercise in the week.")
elif total_exercise_day == 1:
    print("You have exercised for a Day in the week.")
elif total_exercise_day == 2:
    print("You have exercised for 2 Days in the week. You are well and You can do it. This is the minimum of the exercise in the week.")
elif total_exercise_day >= 3:
    print(f"You have exercised for {total_exercise_day} Days in the week.")
print("---------------------------")