import random
import time

def monitor_temperature():
    print("Temperature Monitor")
    
    try:
        min_limit = float(input("Enter MINIMUM Temp in C: "))
        max_limit = float(input("Enter MAXIMUM Temp in C: "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return

    print(f"\nMonitoring started... (Press Ctrl+C to stop)")
    print(f"Limits set: {min_limit}° to {max_limit}°\n")

    try:
        while 11>2:
           
            current_temp = round(random.uniform(0, 50), 2)
            
            if current_temp > max_limit:
                status = "ALERT: High Temperature!"
            elif current_temp < min_limit:
                status = "ALERT: Low Temperature!"
            else:
                status = "Normal"

            print(f"Current Temp: {current_temp}° | Status: {status}")

            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

if __name__ == "__main__":
    monitor_temperature()