def count_calls(cls):
    class Wrapper(cls):
        call_count = 0

        def __getattribute__(self, name):
            attr = super().__getattribute__(name)
            if callable(attr) and name != '_increment_call_count':
                def new_func(*args, **kwargs):
                    Wrapper._increment_call_count()
                    return attr(*args, **kwargs)
                return new_func
            return attr

        @classmethod
        def _increment_call_count(cls):
            cls.call_count += 1

        @classmethod
        def get_call_count(cls):
            return cls.call_count

    return Wrapper

# Example usage:
@count_calls
class MyClass:
    def hello(self):
        print("Labas")

    def sum(self, x, y):
        return x + y


obj = MyClass()
obj.hello()
obj.sum(5, 98)
obj.hello()

print(MyClass.get_call_count())  # Output: 3