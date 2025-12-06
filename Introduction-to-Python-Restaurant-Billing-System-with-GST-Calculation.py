food_type = input("Enter food type (fast, regular, luxury): ").lower()
price = float(input("Enter price of the item: "))

if food_type == "fast":
    gst_rate = 0.05
elif food_type == "regular":
    gst_rate = 0.08
elif food_type == "luxury":
    gst_rate = 0.15
else:
    print("Invalid food type entered.")
    exit()

gst_amount = price * gst_rate
final_bill = price + gst_amount

print(f"GST Rate Applied: {gst_rate * 100}%")
print(f"GST Amount: {gst_amount:.2f}")
print(f"Final Bill Amount: {final_bill:.2f}")
