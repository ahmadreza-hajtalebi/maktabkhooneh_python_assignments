def skiline(*args):
    answer = 0
    for i in args:
        if i > answer:
            answer = i
        else:
            pass
    return answer