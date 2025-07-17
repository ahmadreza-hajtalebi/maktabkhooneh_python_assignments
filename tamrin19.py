def pick_evens(*args):
    answer = []
    for i in args:
        if i % 2 == 0:
            answer.append(i)
        else:
            pass
    return answer