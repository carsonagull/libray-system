bookID = input("Enter Book ID: ")
dueDate = int(input("Enter Due Date: "))
returnDate = int(input("Enter Return Date: "))

daysOverdue = returnDate - dueDate

if daysOverdue <= 0:
    fineRate = 0
elif daysOverdue <= 7:
    fineRate = 20
elif daysOverdue <= 14:
    fineRate = 50
else:
    fineRate = 100

fineAmount = daysOverdue * fineRate if daysOverdue > 0 else 0

print("\nLibrary Fine Details")
print(f"Book ID: {bookID}")
print(f"Return Date: {returnDate}")
print(f"Days Overdue: {daysOverdue}")
print(f"Fine Rate: Ksh. {fineRate} per day")
print(f"Total Fine Amount: Ksh. {fineAmount}")