# Linear Actuator Control System

This repository contains my completed task for the Accio Robotics Controls Intern evaluation.  
It includes the circuit design and controller logic required to drive a two-wire linear actuator using relay control, RS-485 position feedback, and software-based safety interlocks.

---

## 📁 Contents

| File | Purpose |
|------|---------|
| `Actuator_Circuit_Schematic.pdf` | Complete electrical schematic showing relay logic and transistor interfacing |
| `ControlLogic_Pseudocode.txt` | Programming logic for automatic actuator motion using limit switching |
| `Final_Report_Actuator_Control.docx` | Documentation explaining system design, wiring, logic flow, and safety |
| `PositionControl_Readme.txt` (optional) | Additional notes and test observations |

---

## 🛠 System Overview

- Actuator control based on polarity reversal using SPDT relays.
- Controlled via two digital outputs (`OUT_0.0` UP, `OUT_0.1` DOWN).
- Position feedback received through **RS-485**.
- Only one movement direction active at a time (safety logic enforced).

---

## 🎯 Features Implemented

✔ Automatic up/down movement  
✔ Safety interlock (prevents both signals ON)  
✔ Limit logic based on position feedback  
✔ Fault handling and stop condition  
✔ Cycle counting for movement logs  
✔ Startup behavior logic  

---

## 🧰 Tools Used

- **KiCad 9.0**
- Text-based pseudocode / PLC-style logic
- MS Office for documentation

---

## 👤 Author

**Mahesh Prabhu**  
Embedded Systems & Controls Engineering Enthusiast  
📍 Bangalore, India  

---

