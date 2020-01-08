import functools

class Pipeable():
    """Class that enables `>>` to function as a piping operator.
    """

    def __init__(self, base_object, *args, unpack_input=False, use_first_arg_only=False, **kwargs):
        self.base_object = base_object
        self.args = args
        self.kwargs = kwargs
        self.unpack_input = unpack_input
        self.use_first_arg_only = use_first_arg_only

    def __rshift__(self, other):
        return other.base_object(self.base_object, *other.args, **other.kwargs)

    def __rrshift__(self, other):
        if self.unpack_input:
            return self.base_object(*other, *self.args, **self.kwargs)
        elif self.use_first_arg_only:
            return self.base_object(other[0], *self.args, **self.kwargs)
        else:
            return self.base_object(other, *self.args, **self.kwargs)

    def __getattr__(self, attribute):
        return getattr(self.base_object, attribute)

    def __call__(self, *args, **kwargs):
        return Pipeable(self.base_object, *args, unpack_input=self.unpack_input, use_first_arg_only=self.use_first_arg_only, **kwargs)


def unpack_input(pipeable):
    """Decorator to place before Pipeable to cause inputs to be unpacked into the Pipeable-decorated function.

    I.e. if you want (a, b) >> func() to correspond to func(a, b), then place this above Pipeable, as follows::

        @unpack_input
        @Pipeable
        def func(a, b):
            pass

    """
    pipeable.unpack_input = True
    return pipeable


def use_first_arg_only(pipeable):
    """Decorator to place before Pipeable to cause only first input to be used.

    """
    pipeable.use_first_arg_only = True
    return pipeable

