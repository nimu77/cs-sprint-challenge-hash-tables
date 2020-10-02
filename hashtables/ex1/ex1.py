def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # the length of the array weights
    length = len(weights)

    # dictionary to store the key and values
    a = {}

    # return None if weight has only 1 elements
    if length <= 1:
        return None

    # iterate 
    for idx, weight in enumerate(weights):
        if limit - weight in a:
            return idx, a[limit - weight]

        # if not in a add idx as the value in a dict
        a[weight] = idx
