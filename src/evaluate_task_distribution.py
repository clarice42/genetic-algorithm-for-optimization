class EvaluateTaskDistribution:
    # Store the problem instance during initialization
    def __init__(self, problem_instance, weight):
        self.problem_instance = problem_instance
        self.weight = weight

    # Calculate task completion time
    def __task_completion_time(self, task, vm):
        return task[1] / vm[1]

    # Calculate total completion time of all tasks across all vms
    def __total_completion_time(self, tasks, vms, solution):
        total_sum = 0

        for index, value in enumerate(solution):
            total_sum = total_sum + self.__task_completion_time(tasks[index], vms[value])

        return total_sum

    # Calculate makespan
    def __makespan(self, solution):
        tasks = self.problem_instance[0]
        vms = self.problem_instance[1]
        vms_times = {}

        for index, value in enumerate(solution):
            vm = vms[value]
            vm_key = vms[value][0]
            task = tasks[index]

            # Calculates the sum of task completion time per vm and store them in a dictionary
            if(vm_key in vms_times):
                sum = vms_times[vm_key] + self.__task_completion_time(task, vm)
                vms_times[vm_key] = sum
            else:
                vms_times[vm_key] = self.__task_completion_time(task, vm)

        # Returns the task time execution of the virtual machine that finishes last
        return max(vms_times.values())

    # Calculate Rate of Utilization
    def __rate_of_utilization(self, solution):
        tasks = self.problem_instance[0]
        vms = self.problem_instance[1]

        total_completion_time = self.__total_completion_time(tasks, vms, solution)
        makespan = self.__makespan(solution)
        rate_of_utilization = (total_completion_time / (makespan * len(vms)))

        return rate_of_utilization

    # Calculate Resource Wastage
    def __resource_wastage(self, solution):
        rate_of_utilization = self.__rate_of_utilization(solution)
        return 1 - rate_of_utilization

    # Compute the fitness value of the received solution
    def __call__(self, solution, should_print_values=False):
        makespan = self.__makespan(solution)
        resource_wastage = self.__resource_wastage(solution)

        if(should_print_values):
            print("Makespan: ", makespan)
            print("Resource wastage: ", resource_wastage)

        solution = (self.weight * makespan) + ((1 - self.weight) * resource_wastage)

        # Returns the inverse value of the fitness, in order to work with the other GA
        # operators, which work with max values of fitness
        return round(1 - solution, 3)