def countValids(objects):
    count = 0
    for o in objects:
        if o.isValid():
            count += 1
    return count



