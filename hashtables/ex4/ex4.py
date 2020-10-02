def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    result = []

    d = {}

    for i in a:
        if -i in d:
            result.append(abs(i))
            
        d[i] = True

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
