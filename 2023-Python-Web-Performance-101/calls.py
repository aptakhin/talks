def cpu_intensive_call(*, num_iterations: int) -> None:
    x = 1
    for _ in range(num_iterations):
        x*x
