attendees = int(input("enter number of attendees: "))
print("large hall") if attendees < 100 else print("conference room")
wants_vegetarian_food = input("Do you want vegetarian food? ")
print("Veggie delight caterers")if wants_vegetarian_food == 'yes' else print("Gourmet meals caterers")