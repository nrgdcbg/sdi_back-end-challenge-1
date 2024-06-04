import math

def calculate_cost(seats, cars):
    cheapest_cost = None
    optimal_solution = {
        "size": None,
        "num_cars": 0,
    }

    for car in cars:
        seat_capacity = car["seat_capacity"]
        price = car["price"]

        num_cars = math.ceil(seats / seat_capacity)
        
        total_cost = num_cars * price

        if cheapest_cost is None or total_cost < cheapest_cost:
            cheapest_cost = total_cost

            optimal_solution["size"] = car["size"]
            optimal_solution["num_cars"] = num_cars

    return optimal_solution, cheapest_cost

def main():
    cars = [
        {
            "size": "S",
            "seat_capacity": 5,
            "price": 5000,
        },
        {
            "size": "M",
            "seat_capacity": 10,
            "price": 8000,
        },
        {
            "size": "L",
            "seat_capacity": 15,
            "price": 12000,
        },
    ]

    seats = int(input("Please input number (seat): "))

    optimal_solution, total_cost = calculate_cost(seats, cars)

    print("{} x {}".format(optimal_solution["size"], optimal_solution["num_cars"]))
    print("Total = PHP {}".format(total_cost))

main()