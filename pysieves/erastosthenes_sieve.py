__OFFSET = 2


def erastothenes_sieve(limit: int):
    if(limit < 0):
        raise ValueError(
            "The value of `limit` can not be negative. Given `{limit}`")
    if(limit < 2):
        return []

    candidates = [True
                  for candidate in range(2, limit + 1)]

    index = 0
    while(index < len(candidates)):
        if(candidates[index]):
            candidate = index + __OFFSET
            multiple_index = 2*index + __OFFSET
            while(multiple_index < len(candidates)):
                candidates[multiple_index] = False
                multiple_index += candidate
        index += 1
    return (candidate[0] + __OFFSET for candidate in enumerate(candidates) if candidate[1])
