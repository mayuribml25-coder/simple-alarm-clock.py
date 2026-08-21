import datetime
import time

# Ask the user to enter alarm time
alarm_time = input("Enter alarm time (HH:MM:SS): ")S

print("Alarm set for:", alarm_time)
print("Waiting for alarm...")

while True
    # Get current system time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    # Compare current time with alarm time
    if current_time == alarm_time:
        print("ALARM! Wake up!")

        # Play sound on Windows
        try:
            import winsound
            winsound.Beep(1000, 1000)
        except:
            print("Sound is not supported on this system.")

        break

    time.sleep(1)