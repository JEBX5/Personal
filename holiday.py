destination = ["paris" , "berlin" , "milan" , "dublin"]
flight_price = [100 , 150 , 130 , 35]
rental = 100
hotel = 120
flight_dict = {}

city_flight = input("Please enter the name for the destination you are flying too"
                    "\nParis"
                    "\nBerlin"
                    "\nMilan"
                    "\nDublin\n")
# clean input
city_flight = city_flight.strip().lower()

#some error check here

num_nights = int(input("Please enter how many nights you are staying for "))
rental_days = int(input("Please enter how many days you are renting a car for "))

#check both are numbers


def hotel_cost(x):
    y = x * hotel
    return y

def plane_cost(x):
    if x == "berlin":
        y = 150
    elif x == "paris":
        y = 100
    elif x == "milan":
        y = 120
    elif x == "dublin":
        y = 35
    else:
        y = "You did not enter one of the 4 city names correctly, please restart"
    return y

def car_rental(x):
    y = x * rental
    return y

def holiday_cost(x, y, z):
    t = x + y + z
    return t


print(plane_cost(city_flight))
print(hotel_cost(num_nights))
print(car_rental(rental_days))

# get inputs
# set variable 