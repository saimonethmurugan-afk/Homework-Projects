#  Travel Details

passenger_name ="Sai"
destination = "King's Cross Station"
ticket_price = 30
no_tickets = 1
ticket_availability = True
total_costs=0

print("Passenger's name: ", passenger_name)
print("Destination: ",destination)
print("Ticket price: ",total_costs)
print("No. Tickets: ",no_tickets)
print("Tickets are avilable: ", ticket_availability)

#Arithmetic Operators

total_costs = ticket_price * no_tickets 
ten_off = 0
ten_off = total_costs * 0.9
double_price = 0
double_price = total_costs * 2
increased_price = 0
increased_price = total_costs + 5
half_price = 0
half_price = total_costs/2

Discount = 10
Discount_applied_costs = total_costs - Discount

print("Discount: ", Discount)
print("Discount applied final costs: ",Discount_applied_costs)
Final_costs = Discount_applied_costs
print("Final Costs: ",Final_costs)
print("Double ticket price:",double_price)
print("Increased ticket price",increased_price)
print("Half ticket price: ", half_price)

#Comparison operators

print("Is Total Costs less than £50?",total_costs < 50)
print("Are there more than 2 tickets booked?",no_tickets > 2)
print("Is the destination King's Cross Station?", destination == "King's Cross Station")
print("Is final costs more than £32?",Final_costs > 32)

#String Operations

travel_message = passenger_name + " is travelling to " + destination +"."
print("Travel message:",travel_message)
print("Destination name in upper case: ",destination.upper())
print("Passenger name in lower case: ",passenger_name.lower())
print("First letter of destination name: ", destination[0])
print("Length of passenger name: ", len(passenger_name))

#Swapping Values

morning_ticket_price = 30
evening_ticket_price = 40

print("Before Swapping: ")
print("\nMorning Ticket Price: £",morning_ticket_price)
print("\nEvening Ticket Price: £ ",evening_ticket_price)


#Final Ticket Summary

print("\n==========================================================")
print("TRAVEL TICKET SUMMARY")
print("==============================================================")
print("Passenger: ",passenger_name)
print("Destination: ",destination)
print("Tickets booked:",no_tickets)
print("Final amount to pay: £",Final_costs)
print("Booking confirmed?",ticket_availability)
