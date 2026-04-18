import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file
df = pd.read_csv("log.csv")

# Create time axis
time = range(len(df))

# ===== MAIN CONTROL GRAPH =====
plt.figure()
plt.plot(time, df["Setpoint"], label="Setpoint")
plt.plot(time, df["Encoder"], label="Encoder")
plt.plot(time, df["Speed"], label="Speed")

plt.xlabel("Time (samples)")
plt.ylabel("Value")
plt.title("Closed Loop Control (PID Response)")
plt.legend()
plt.grid()

# ===== DIRECTION GRAPH =====
plt.figure()
plt.plot(time, df["Direction"], label="Direction")
plt.xlabel("Time")
plt.ylabel("Direction")
plt.title("Motor Direction")
plt.legend()
plt.grid()

# ===== LED STATUS GRAPH =====
plt.figure()
plt.plot(time, df["Green"], label="Green")
plt.plot(time, df["Red"], label="Red")
plt.plot(time, df["Blue"], label="Blue")
plt.plot(time, df["Yellow"], label="Yellow")
plt.plot(time, df["White"], label="White")

plt.xlabel("Time")
plt.ylabel("LED State")
plt.title("LED Status")
plt.legend()
plt.grid()

plt.show()
