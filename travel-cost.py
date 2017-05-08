def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost = cost - 50
    elif days >= 3:
        cost = cost - 20
    return cost

city = str(raw_input('Where to? Choose between Charlotte, Tampa, Pittsburgh, or Los Angeles:'))
days = int(raw_input('How many days?:'))
nights = int(raw_input('How many nights?:'))
spending_money = int(raw_input('How much cash in USD$ do you want to bring?:'))

def trip_cost(city, days, nights, spending_money):
    return rental_car_cost(days) + hotel_cost(nights) + plane_ride_cost(city) + spending_money

print(trip_cost(city, days, nights,spending_money))
