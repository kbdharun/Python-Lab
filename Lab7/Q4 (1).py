# Q4

'''
Distance value is represented in terms of feet and inch. Create a nested dictionary to store
distance value (feet and inch) for 5 distances. Create a class called DISTANCE with nested
distance dictionary as the data member.

Include a member function to get input for five distance
values. Create another class called OPERATION with DISTANCE class object and with result 
_feet result_inch as the datamember. Include the following methods in OPEARTION class. 

a. Average () – find the average of 5 distance and store it in result_feet and
result_inch.
b. Add_distance() – add any two distances among 5 distances and store it in
result_feet and result_inch.
c. Maximum() – find the maximum among 5 distances.
'''

class DISTANCE:
    def __init__(self):
        self.distance = {
            "distance1": {"feet": 0, "inch": 0},
            "distance2": {"feet": 0, "inch": 0},
            "distance3": {"feet": 0, "inch": 0},
            "distance4": {"feet": 0, "inch": 0},
            "distance5": {"feet": 0, "inch": 0},
        }

    def get_input(self):
        for key in self.distance:
            print(f"Enter distance value {key}:")
            self.distance[key]["feet"] = int(input("Enter Feet: "))
            self.distance[key]["inch"] = int(input("Enter Inch: "))


class OPERATION:
    def __init__(self, distance_obj):
        self.distance_obj = distance_obj
        self.result_feet = 0
        self.result_inch = 0

    def average(self):
        total_feet = 0
        total_inch = 0
        for key in self.distance_obj.distance:
            total_feet += self.distance_obj.distance[key]["feet"]
            total_inch += self.distance_obj.distance[key]["inch"]
        total_inches = total_feet * 12 + total_inch
        average_inches = total_inches / 5
        self.result_feet = (average_inches // 12)
        self.result_inch = (average_inches % 12)

    def add_distance(self, key1, key2):
        feet1 = self.distance_obj.distance[key1]["feet"]
        inch1 = self.distance_obj.distance[key1]["inch"]
        feet2 = self.distance_obj.distance[key2]["feet"]
        inch2 = self.distance_obj.distance[key2]["inch"]
        total_inches = (feet1 + feet2) * 12 + inch1 + inch2
        self.result_feet = int(total_inches // 12)
        self.result_inch = int(total_inches % 12)

    def maximum(self):
        max_distance = max(self.distance_obj.distance.values(), key=lambda x: x["feet"] * 12 + x["inch"])
        self.result_feet = max_distance["feet"]
        self.result_inch = max_distance["inch"]

distance_obj = DISTANCE()
distance_obj.get_input()

operation_obj = OPERATION(distance_obj)
operation_obj.average()
print("\nAverage distance:", operation_obj.result_feet, "feet", operation_obj.result_inch, "inches")

operation_obj.add_distance("distance1", "distance3")
print("Added distance:", operation_obj.result_feet, "feet", operation_obj.result_inch, "inches")

operation_obj.maximum()
print("Maximum distance:", operation_obj.result_feet, "feet", operation_obj.result_inch, "inches")