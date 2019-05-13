credit_score = True
total_salry = True

if credit_score and total_salry:
    print('Eligible')
else:
    print('Not eligible')

#  for and both should be true

isCitizenOfIndia = True
isAdult = False

if isCitizenOfIndia or isAdult:
    print('You can come')
else:
    print('No you are not allowed')

# any of varible is True then its true

student = False


if not student:
    print('Not allowed to vote')
else:
    print('Congaulations , You can Vote')
