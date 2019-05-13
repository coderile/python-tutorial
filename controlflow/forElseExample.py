successful = False

for num in range(3):
    print("Attempted")
    if successful:
        print('Successful')
        break
else:
    print('Attempted 3 times and faled')
