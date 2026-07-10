# Definition of a simple problem instance, extracted from the original article.
# The problem instance is composed of a task list, which specifies each task length
# and the VMs list, which specifies each VM processing capacity

# Tasks and their corresponding length in Million Instructions (MI)
Tasks = [
    ("T1", 15),
    ("T2", 25),
    ("T3", 35),
    ("T4", 20),
    ("T5", 30),
    ("T6", 40)
]

# VMs and their corresponding processing capacity in Million Instructions per Second (MIPS)
VMs = [
    ("VM1", 60),
    ("VM2", 50),
    ("VM3", 40),
    ("VM4", 30),
]