class MyShape:
    def __init__(color="Orange", is_filled=False):
        cvet = color
        value = is_filled
     
    def __str__(color, is_filled):
        return f"Color: {color}, Value: {is_filled}"
    
    def getArea():
        return 0

shape1 = MyShape()
print(MyShape.__str__("Orange", False))               
print(MyShape.getArea())