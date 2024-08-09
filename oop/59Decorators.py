
def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("thx for using my code")
    return mfx

@greet
def hello():
    print("hello guys")


hello()