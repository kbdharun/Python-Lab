# Q3


'''
HRA=25%,DA=12% and PF=8%. 3. Create a class called DISATNCE with feet and inch as the private property. Include
the following methods in DISTANCE class. a) Using operator overloading
i. Add two DISTANCE objects
ii. ADD one Distance objects with total feet value(inplace addition)
iii. ADD one int value to DISATNCE object. b). using property( ) object set the values and display the values for DISTANCE
object.
'''


class DISTANCE:
    def __init__(self, feet=0, inch=0):
        self.feet = feet
        self.inch = inch


    def __str__(self):
        return f"{self.feet} feet {self.inch} inches"


    def __add__(self, other):
        if isinstance(other, int):
            feet = self.feet + other
            inch = self.inch
        else:
            feet = self.feet + other.feet
            inch = self.inch + other.inch
        if inch >= 12:
            feet += inch // 12
            inch = inch % 12
        return DISTANCE(feet, inch)


    def __iadd__(self, other):
        self.feet += other.feet
        self.inch += other.inch
        if self.inch >= 12:
            self.feet += self.inch // 12
            self.inch = self.inch % 12
        return self


    @property
    def distance(self):
        return f"{self.feet} feet {self.inch} inches"


    @distance.setter
    def distance(self, val):
        vals = val.split()
        if len(vals) == 2:
            self.feet = int(vals[0])
            self.inch = int(vals[1])
        elif len(vals) == 1:
            if 'feet' in vals[0]:
                self.feet = int(vals[0].replace('feet', '').strip())
            elif 'inch' in vals[0]:
                self.inch = int(vals[0].replace('inch', '').strip())
            else:
                raise ValueError("Invalid input format")
        else:
            raise ValueError("Invalid input format")


# Testing the class
d1 = DISTANCE(5, 8)
d2 = DISTANCE(3, 10)
d3 = d1 + d2
print(d3) # Output: 9 feet 6 inches


d1 += DISTANCE(1, 6)
print(d1) # Output: 7 feet 2 inches


d4 = d1 + 4
print(d4) # Output: 11 feet 2 inches