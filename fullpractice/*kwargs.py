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