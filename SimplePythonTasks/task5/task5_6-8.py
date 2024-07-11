objects = ["duck", "pumpkin", "pomeranian"]

for object in objects:
    object = object.capitalize()
    print("%sy Mc%sface" % (object, object))
    print(f"{object}y Mc{object}face")
    print("{name}y Mc{name}face\n".format(name = object))
