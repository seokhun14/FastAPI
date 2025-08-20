my_var = [1, 2, 3]

my_int: int = "123"

my_str: str = "abc"

my_list: list[str] = ["abc", "def"]

my_tuple: tuple[str, str] = ("str", "str")
my_tuple2: tuple[str, ...] = ("str", "str", "str", "str")

my_dict: dict[str, int] = {"a": 1, "b": 2, "c": 3}


or_type_list: list[str | int] = ["a", 1, "b", 2, "c", False, 123]


