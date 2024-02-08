def print_kwargs(**kwargs):
        """ Like *args, **kwargs can take however many arguments you would like to supply to it.
        However,**kwargs differs from *args in that you will need to assign keywords."""
        print(kwargs)

print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)

def print_values(**kwargs):
    """ The function greets a dictionary of names """
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))

print_values(my_name="Sammy", your_name="Casey")

def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))

print_values(
            name_1="Alex",
            name_2="Gray",
            name_3="Harper",
            name_4="Phoenix",
            name_5="Remy",
            name_6="Val"
        )

def some_kwargs(kwarg_1, kwarg_2, kwarg_3):
    """ Here we are using the **kwargs to call a function"""
    print("kwarg_1:", kwarg_1)
    print("kwarg_2:", kwarg_2)
    print("kwarg_3:", kwarg_3)

kwargs = {"kwarg_1": "Val", "kwarg_2": "Harper", "kwarg_3": "Remy"}
some_kwargs(**kwargs)