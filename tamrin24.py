def func_run_time(f):
    def wrapper(k):
        import datetime
        start_time = datetime.datetime.now()
        result = f(k)
        finish_time = datetime.datetime.now()
        running_time_seconds = (finish_time-start_time).total_seconds()
        print(f"the function run time : {running_time_seconds:.6f}")
        return result
    return wrapper


@func_run_time
def list_creator(n):
    my_list = []
    counter = 1
    while len(my_list) < n:
        my_list.append(counter)
        counter += 1
    return my_list


n = int(input("please inter the n :\n"))

l = list_creator(n)
print(l)
