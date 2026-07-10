def round_robin_schedule(problem_instance):
    tasks, vms = problem_instance
    return [i % len(vms) for i in range(len(tasks))]