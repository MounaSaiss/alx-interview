def canUnlockAll(boxes):
    n = len(boxes)  # Total number of boxes
    unlocked = [False] * n  # Keep track of opened boxes
    unlocked[0] = True  # The first box is always unlocked
    keys = [0]  # Start with the keys from the first box

    while keys:
        current_box = keys.pop()  # Get the next box to unlock
        for key in boxes[current_box]:  # Iterate over keys in the current box
            if key < n and not unlocked[key]:  # If the key opens a new box
                unlocked[key] = True  # Mark the box as unlocked
                keys.append(key)  # Add the box's keys to the list to check

    # Return True if all boxes are unlocked, False otherwise
    return all(unlocked)

