from string_apps.string_operation import StringOperations
from structure_conversion.tuple_dictionary import sort_tuple


def run_apps():
    print("welcome to Lab1")
    string_op = StringOperations()
    string_op.longest_substring('ababcdxa')
    sort_tuple()


if __name__ == "__main__":
    run_apps()
