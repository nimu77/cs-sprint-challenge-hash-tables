def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    result = {}
    
    result_two = []
    
    for a in arrays:
        for i in a:
            if i in result:
                if i in result_two:
                    continue
                if i not in result_two:
                    result_two.append(i)
            result[i] = a
    return result_two

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))