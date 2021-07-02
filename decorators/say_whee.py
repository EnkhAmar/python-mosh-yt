from decorators import do_twice

@do_twice
def say_whee():
    print("Whee!")

say_whee()

print(say_whee.__name__)