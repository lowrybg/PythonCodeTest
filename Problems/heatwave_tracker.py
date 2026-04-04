# Problem: The Summer Heatwave Tracker
# Write a program that analyzes daily temperatures over a given period to find the longest
# "heatwave." A heatwave is defined as a consecutive sequence of days where the temperature is
# strictly 30.0°C or higher.
#
# Input Data:
# The program will read a sequence of numbers from the console:
#
# On the first line: The number of days being tracked—an integer N in the range [1 … 100].
#
# On the next N lines: The recorded temperature for each day—a floating-point number.

def track_heatwave():
    n = int(input())

    max_streak = 0
    best_peak = 0.0

    current_streak = 0
    current_peak = 0.0

    for _ in range(n):
        temp = float(input())

        if temp >= 30.0:
            current_streak += 1
            if temp > current_peak:
                current_peak = temp
        else:

            if current_streak > max_streak:
                max_streak = current_streak
                best_peak = current_peak

            current_streak = 0
            current_peak = 0.0


    if current_streak > max_streak:
        max_streak = current_streak
        best_peak = current_peak

    if max_streak > 0:
        print(f"{max_streak} days")
        print(f"{best_peak:.1f}°C")
    else:
        print("No heatwave detected.")


# Execute the program
if __name__ == "__main__":
    track_heatwave()