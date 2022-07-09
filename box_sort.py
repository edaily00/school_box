
#Box class that holds length, width, height
class Box:

    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height
#This method returns the volume of the box
    def volume(self):
        volume = self.get_length() * self.get_width() * self.get_height()
        return volume

#This function sorts a list of boxes by volume
def box_sort(box_list):
    for i in range(1, len(box_list)):
        j = i
        while box_list[j - 1].volume() < box_list[j].volume() and j > 0:
            temp = box_list[j-1]
            box_list[j - 1] = box_list[j]
            box_list[j] = temp
            j -= 1



"""
b1 = Box(3.4, 19.8, 2.1)
b2 = Box(1.0, 1.0, 1.0)
b3 = Box(8.2, 8.2, 4.5)

boxes = [b1, b2, b3]

length = len(boxes)
for i in range(length):
    print(boxes[i].volume())

box_sort(boxes)

for i in range(length):
    print(boxes[i].volume())

"""