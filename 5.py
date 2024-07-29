def get_weather_data():
    weather_data = []
    print("Enter weather data for New York City from 1st August 2024 to 10th July 2024.")
    while True:
        date = input("Enter date (YYYY-MM-DD) or 'done' to finish: ")
        if date.lower() == 'done':
            break
        max_temp_c = float(input(f"Enter maximum temperature (in Celsius) for {date}: "))
        min_temp_c = float(input(f"Enter minimum temperature (in Celsius) for {date}: "))
        humidity_pct = float(input(f"Enter humidity (in percentage) for {date}: "))
        weather_data.append({"date": date, "max_temp_c": max_temp_c, "min_temp_c": min_temp_c, "humidity_pct": humidity_pct})
    return weather_data

def find_highest_and_lowest_temperatures(weather_data):
    highest_temperature_day = max(weather_data, key=lambda x: x["max_temp_c"])
    lowest_temperature_day = min(weather_data, key=lambda x: x["min_temp_c"])
    return highest_temperature_day, lowest_temperature_day

def count_days_with_temp_above_30(weather_data):
    hot_days_count = sum(1 for day in weather_data if day["max_temp_c"] > 30)
    return hot_days_count

def calculate_average_humidity(weather_data):
    total_humidity = sum(day["humidity_pct"] for day in weather_data)
    average_humidity = total_humidity / len(weather_data)
    return average_humidity

def main():
    weather_data = get_weather_data()
    
    while True:
        print("\nWeather Data Analysis")
        print("1. Find Highest and Lowest Temperatures")
        print("2. Count Days with Temperatures Above 30°C")
        print("3. Calculate Average Humidity")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            highest_temp_day, lowest_temp_day = find_highest_and_lowest_temperatures(weather_data)
            print(f"Highest temperature: {highest_temp_day['max_temp_c']}°C on {highest_temp_day['date']}")
            print(f"Lowest temperature: {lowest_temp_day['min_temp_c']}°C on {lowest_temp_day['date']}")
            
        elif choice == '2':
            days_above_30_count = count_days_with_temp_above_30(weather_data)
            print(f"Number of days with temperatures above 30°C: {days_above_30_count}")
            
        elif choice == '3':
            avg_humidity = calculate_average_humidity(weather_data)
            print(f"Average humidity over the specified period: {avg_humidity:.2f}%")
            
        elif choice == '4':
            print("THANK YOU!!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
