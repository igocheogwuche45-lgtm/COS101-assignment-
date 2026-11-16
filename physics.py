# PHYSICS CALCULATOR

# Function 1: Calculate Speed
def calculate_speed():
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (s): "))
    
    if time == 0:
        print("Time cannot be zero.")
    else:
        speed = distance / time
        print("Speed =", speed, "m/s")


# Function 2: Calculate Force
def calculate_force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s²): "))
    
    force = mass * acceleration
    print("Force =", force, "N")


# Function 3: Calculate Work
def calculate_work():
    force = float(input("Enter force (N): "))
    distance = float(input("Enter distance (m): "))
    
    work = force * distance
    print("Work =", work, "J")


# Function 4: Calculate Power
def calculate_power():
    work = float(input("Enter work (J): "))
    time = float(input("Enter time (s): "))
    
    if time == 0:
        print("Time cannot be zero.")
    else:
        power = work / time
        print("Power =", power, "W")


# Function 5: Calculate Kinetic Energy
def calculate_kinetic_energy():
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))
    
    kinetic_energy = 0.5 * mass * velocity ** 2
    print("Kinetic Energy =", kinetic_energy, "J")


# MAIN PROGRAM
while True:

    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Calculate Speed")
    print("2. Calculate Force")
    print("3. Calculate Work")
    print("4. Calculate Power")
    print("5. Calculate Kinetic Energy")

    choice = input("Select an operation (1-5): ")

    if choice == "1":
        calculate_speed()

    elif choice == "2":
        calculate_force()

    elif choice == "3":
        calculate_work()

    elif choice == "4":
        calculate_power()

    elif choice == "5":
        calculate_kinetic_energy()

    else:
        print("Invalid selection!")

    # Ask user whether to continue
    again = input("\nDo you want to continue? (yes/no): ").lower()

    if again != "yes":
        print("Thank you for using the Physics Calculator!")
        break
