def demo(name,duration,instructor):
    print("course name={}".format(name))
    print("course duration={}".format(duration))
    print("course instructor={}".format(instructor))

demo("bdpy",35,"Mark Ho")
demo(name="poop",duration=35,instructor="MengHang Ho")
demo(instructor="MengHang Ho",duration=35,name="poop")
d1={"name":'pykt','duration':35,'instructor':'Ho'}
demo(**d1)