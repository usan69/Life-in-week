age= input("what is your current age ?")


age_as_int= int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining *12


message= f"You have {days_remaining} days or {weeks_remaining} weeks or5 {months_remaining} months left."

print(message)