weather = input("Enter the weather today (sunny or rainy): ")
miles = float(input("Enter journey distance in miles: "))
budget_available = float(input("Enter available budget for journey in £: "))
bus_journey_cost = 0
taxi_journey_cost = 0
train_journey_cost = 0

if weather == "sunny" and miles <= 2:
    print("Walk")
elif weather == "rainy" or miles > 2:
    bus_journey_cost = miles * 3
    if bus_journey_cost < budget_available:
        print("Bus")
    elif bus_journey_cost > budget_available:
        taxi_journey_cost = miles * 2
        if taxi_journey_cost < budget_available:
            print("Taxi")
        elif taxi_journey_cost > budget_available and bus_journey_cost > budget_available:
            train_journey_cost = miles * 0.33
            if train_journey_cost < budget_available:
                print("Train")
            elif taxi_journey_cost > budget_available and bus_journey_cost > budget_available and train_journey_cost > budget_available:
                print("Walk or find other transport within budget")
else:
    print("Error please try again")