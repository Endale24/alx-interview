ckAll(boxes):
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = boxes[0]
    for key in keys:
        if key < n:
            unlocked[key] = True
            keys += boxes[key]
    return all(unlocked)
