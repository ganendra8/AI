import random

def status_location(st1, loc):
    if loc == 'A':
        if st1 == 'dirty':
            print(f"location: {loc}, status: {st1}")
            print("Cleaning location A...")
            print("Move to location: B")
        else:
            print(f"location: {loc}, status: {st1}")
            print("A location is already clean")
            print("Move to location: B")

    elif loc == 'B':
        if st1 == 'dirty':
            print(f"location: {loc}, status: {st1}")
            print("Cleaning location B...")
            print("Move to location: A")
        else:
            print(f"location: {loc}, status: {st1}")
            print("B location is already clean")
            print("Move to location: A")

# Randomly choose initial status and location
status = random.choice(['dirty', 'clean'])
location = random.choice(['A', 'B'])

print(f"Initial location: {location}")
print(f"Initial status: {status}")

# Simulate the cleaning process
if location == 'A':
    status_location(status, location)
    new_status = random.choice(['dirty', 'clean'])
    status_location(new_status, 'B')
elif location == 'B':
    status_location(status, location)
    new_status = random.choice(['dirty', 'clean'])
    status_location(new_status, 'A')
