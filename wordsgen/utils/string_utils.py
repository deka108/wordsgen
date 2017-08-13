def parse_range(range_str, min_val=0, max_val=100):
    try:
        length_range = [int(num) if num else num
                        for num in range_str.split(",")]

        if len(length_range) == 1:
            lower_bound = length_range[0]
            upper_bound = length_range[0]
        elif len(length_range) == 2:
            lower_bound = length_range[0]
            upper_bound = length_range[1]
        else:
            raise ValueError

        if not lower_bound:
            lower_bound = min_val

        if not upper_bound:
            upper_bound = max_val

        return lower_bound, upper_bound
    except ValueError:
        raise ValueError("Range must either be a number or in "
                         "the form of two numbers separated by "
                         "comma eg. or 1, 6 which indicate lower and "
                         "upper bounds")


def print_array(arr):
    for ar in arr:
        print(ar)
