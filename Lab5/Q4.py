# Q4.
'''
Distance value is represented in terms of feet and inch. Create a nested dictionary to store
distance value (feet and inch) for 5 distances. Outer dictionary key value as 1,2,3,..... Get the
input from the user. Include the following user defined functions:
a. Average () - find the average of 5 distance
b. Add_distance() - add any two distances among 5 distances (based on the outer
dictionary key value)
c. Maximum() - find the maximum among 5 distances. 
'''
print('''
Distance Calculation Program
============================
''')

# Objective: To create a nested disctionary function to store distance values

def get_distance():
    feet = int(input("Enter distance (in feet): "))
    inch = int(input("Enter distance (in inch): "))
    return {'feet': feet, 'inch': inch}

def add_distance(dist1, dist2):
    total_inches = (dist1['feet'] + dist2['feet']) * 12 + dist1['inch'] + dist2['inch']
    feet = total_inches // 12
    inch = total_inches % 12
    return {'feet': feet, 'inch': inch}

def average_distance(distances):
    total_feet = 0
    total_inches = 0
    for distance in distances.values():
        total_feet += distance['feet']
        total_inches += distance['inch']
    total_inches += total_feet * 12
    avg_inches = total_inches // 5
    avg_feet = avg_inches // 12
    avg_inches = avg_inches % 12
    return {'feet': avg_feet, 'inch': avg_inches}

def maximum_distance(distances):
    max_distance = None
    for distance in distances.values():
        if max_distance is None or distance['feet'] > max_distance['feet'] or (distance['feet'] == max_distance['feet'] and distance['inch'] > max_distance['inch']):
            max_distance = distance
    return max_distance

# Create the dictionary to store the input distances
distances = {}
for i in range(1, 6):
    print(f"Enter distance {i}")
    distances[i] = get_distance()

# Calculating the average distance
avg_distance = average_distance(distances)

# Adding any 2 distance, first and last in this case
sum_distance = add_distance(distances[1], distances[5])

# Finding the maximum distance
max_distance = maximum_distance(distances)

# Computed output
print("Distances:", distances)
print("Average distance:", avg_distance)
print("Sum of distances 1 and 5:", sum_distance)
print("Maximum distance:", max_distance)