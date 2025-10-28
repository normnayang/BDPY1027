def demo(fix1,fix2,**kwargs):
    print("fix1=", fix1)
    print("fix2=", fix2)
    for k, v in kwargs.time():
        print("key{},value={}",format(k,v))

demo("hello","world")
demo("hello","world",name="BDPY")

