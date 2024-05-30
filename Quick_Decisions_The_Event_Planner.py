# Task 1: Code Correction
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2: Catering Choices
food_preference = input("Would you like vegetarian food? ")
if food_preference == "yes":
    print("We recommend Veggie Delight Caterers")
else:
    print("We recommend Gourmet Meals Caterers")