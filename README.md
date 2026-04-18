# Closed Loop Motor Control System (QNX RTOS)

A real-time, multithreaded embedded C application running on QNX RTOS that implements a deterministic closed-loop control system. The system reads feedback from a Hall sensor, processes it through a PID controller, and drives a DC motor via PWM using GPIO on Raspberry Pi 4.
---
## Features
Real-time closed-loop control using feedback
PID controller (Proportional + Integral + Derivative)
Deterministic execution with 10ms fixed control loop
Multithreaded design (Sensor, Controller, Actuator)
Priority-based scheduling using SCHED_RR
Direction control (Forward / Reverse / Stop)
LED visualization for system state
CSV logging for analysis (/tmp/log.csv)
Safe shutdown with GPIO reset on termination
Mutex-based shared memory communication
 ---
## Hardware Requirements
Raspberry Pi 4
QNX Neutrino RTOS (7.x / 8.x)
L298N Motor Driver
DC Motor
LM393 Hall Effect Sensor
Small Magnet (attached to motor shaft)
LEDs (5x for status indication)
Jumper wires + Power supply
---
## GPIO Configuration
Component	GPIO Pin
PWM Output	GPIO 13
Motor IN1	GPIO 17
Motor IN2	GPIO 27
Hall Sensor	GPIO 22
Green LED	GPIO 5
Red LED	GPIO 6
Blue LED	GPIO 12
Yellow LED	GPIO 16
White LED	GPIO 20
---
## System Architecture
Control Loop Flow
Sensor → Controller → Actuator → Sensor (feedback loop)
Threads & Scheduling
Task	Priority	Role
Sensor Task	Medium (15)	Reads encoder (Hall sensor)
Controller Task	High (20)	Executes PID algorithm
Actuator Task	Medium (15)	Drives motor & LEDs

✔ Scheduling Policy: SCHED_RR
✔ Loop Period: 10ms (deterministic)
---

## Control Logic
Setpoint (SP): Target encoder count
Feedback: Hall sensor pulse count
Error: SP - Encoder
PID Equation:
Output = KP * error + KI * integral + KD * derivative
---
## LED Indication
LED	Condition
Green	Forward
Red	Reverse
Blue	Low speed
Yellow	Medium speed
White	High speed
## Logging
Data is logged to:
/tmp/log.csv
---

## Format:
Setpoint,Encoder,Speed,Direction,Green,Red,Blue,Yellow,White
---
## Build Instructions
We are Using QNX Momentics IDE
Import project
clean Project
---
## Build 
Terminal Build:
make clean
make
## Run Instructions
./closed_loop_contol_system
## Stop Program (IMPORTANT)
CTRL + C

✔ Motor stops immediately
✔ LEDs turn OFF
✔ Cleanup ensures safe shutdown

## Known Limitation
Uses Hall sensor (single channel)
Cannot detect direction inherently
Reverse control is approximated using software logic
---

![IMG 3776](https://drive.google.com/file/d/1bu9psArqC7LTX9GLWT17GY8yeirsVcNf/view?usp=drivesdk)
