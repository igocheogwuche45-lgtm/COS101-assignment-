# COS 101 ASSIGNMENT
# Five Basic Physics Formulas

# 1. Speed = Distance / Time
def speed(distance, time):
    return distance / time


# 2. Force = Mass × Acceleration
def force(mass, acceleration):
    return mass * acceleration


# 3. Weight = Mass × Gravity
def weight(mass, gravity=9.8):
    return mass * gravity


# 4. Kinetic Energy = 1/2 × Mass × Velocity²
def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2


# 5. Potential Energy = Mass × Gravity × Height
def potential_energy(mass, gravity, height):
    return mass * gravity * height


# Display results
print("PHYSICS FORMULAS")

print("Speed:", speed(100, 20), "m/s")
print("Force:", force(10, 5), "N")
print("Weight:", weight(20), "N")
print("Kinetic Energy:", kinetic_energy(10, 5), "J")
print("Potential Energy:", potential_energy(10, 9.8, 5), "J")
