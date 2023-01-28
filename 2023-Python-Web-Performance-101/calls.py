def cpu_intensive_call(*, num_iterations):
    x = 1
    for _ in range(num_iterations):
        x*x
        # time.sleep(0)
