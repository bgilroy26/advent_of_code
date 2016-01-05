def get_dims(in_string):
    dim_ints = [int(dim) for dim in in_string.split('x')]
    return tuple(dim_ints)
