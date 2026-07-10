# Genetic Algorithm for Resource Allocation and Makespan Optimization in Cloud Computing 

This code was developed as the final project of the class Analysis of Algorithms. The objective was to implement an optimization algorithm presented by an article and compare it with a baseline method studied during the classes. The chosen baseline was a simple Round Robin algorithm, and the selected article was: 
- Dehury, J.P., Kumar, D. & Kumar, S. Joint optimization of resource utilization and makespan in cloud computing using genetic algorithm. Discov Computing 29, 315 (2026).

This article proposes a genetic algorithm to minimize makespan and resource wastage, simultaneously, in a cloud computing context. This code implements the proposed genetic algorithm, with a few modifications:
1. Since this is a multi-objective problem, our implementation used the weighted sum method to create the fitness function, just like it's specified in the article. But since most genetic operators are based on maximum fitness value, the fitness function was adapted to match this requirement. In this case, higher values indicate greater minimization of wastage and makespan.
2. The experiments used a simple array of tasks and virtual machines (extracted from the article), instead of real datasets. This way, we can easily validate the execution of the GA and compare it with the baseline.

## Steps to run the code

The code can be executed using the notebook or in a local environment. To run it in your machine, please follow the steps below:

- Pre-requisites: have python 3 installed in your machine

1. Open a terminal in the root folder of this project and run the following command to create a virtual environment where your libraries will be installed:
`python -m venv .venv`
2. Run the following command to activate your environment:
    - If you are using a windows terminal or powershell, run `.venv\Scripts\activate`
    - If you are using git bash or wsl, run `source .venv/Scripts/activate`
    - If you are using mac, run `source .venv/bin/activate`

    - To deactivate the environment, run `deactivate`

3. With the environment activated, run this command to install the necessary libraries:
`pip install -r requirements.txt`
4. After installing the libraries, run the following command to execute the genetic algorithm:
`cd src && python main.py`
