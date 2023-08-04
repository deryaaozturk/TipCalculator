print("welcome to tip calculator")
bill=float(input("how much is the bill"))
tip=int(input("What percentage would you like to tip?"))
person=int(input("how many people"))
new_tip=(tip/100)*bill
new_bill=(bill+new_tip)/person
print(round(new_bill,2))