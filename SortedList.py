class SortedList(list):
  def __init__(self, values):
    super().__init__(values)
    self = values
    self.sort()

# add sortedlists, return sorted
  def __add__(self, other):
    self += other
    self.sort()
    return self

#append element, return sorted
  def append(self, value):
    super().append(value)
    self.sort()
    
#add a list to existing and sort
  def extend(self, other):
    super().extend(other)
    self.sort()

#test
lst = SortedList([4, 1, 5])
print(lst)
lst.append(8)
print(lst)
lst2 = SortedList([9, 3, 10])
lst2.extend([11, 7, 14])
print(lst2)
new = lst + lst2
print(new)