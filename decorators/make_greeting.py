from debug.debug import debug


@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"


make_greeting("Benjamin")

# Decorator нь функцыг параметер болгон авч, хэрэглэгчид хэрэгтэй логик оруулж, функцыг дахин тодорхойлж болдог.