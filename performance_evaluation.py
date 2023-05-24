import random
import matplotlib.pyplot as plt


def allocate_process_first_fit(memory, process_size):
    for i in range(len(memory)):
        if memory[i] >= process_size:
            memory[i] -= process_size
            return True
    return False

def allocate_process_best_fit(memory, process_size):
    best_fit_index = -1
    best_fit_size = float('inf')

    for i in range(len(memory)):
        if memory[i] >= process_size and memory[i] - process_size < best_fit_size:
            best_fit_index = i
            best_fit_size = memory[i] - process_size

    if best_fit_index != -1:
        memory[best_fit_index] -= process_size
        return True

    return False

def allocate_process_worst_fit(memory, process_size):
    worst_fit_index = -1
    worst_fit_size = -1

    for i in range(len(memory)):
        if memory[i] >= process_size and memory[i] - process_size > worst_fit_size:
            worst_fit_index = i
            worst_fit_size = memory[i] - process_size

    if worst_fit_index != -1:
        memory[worst_fit_index] -= process_size
        return True

    return False

def allocate_process_next_fit(memory, process_size, last_index):
    allocated = False

    for i in range(last_index + 1, len(memory)):
        if memory[i] >= process_size:
            allocated = True
            memory[i] -= process_size
            return allocated, i

    for i in range(last_index + 1):
        if memory[i] >= process_size:
            allocated = True
            memory[i] -= process_size
            return allocated, i

    return allocated, last_index

# Define the number of trials and processes
num_trials = 1000
num_processes = 10
memory_size = 1000

# Initialize the performance counters
first_fit_count = 0
best_fit_count = 0
worst_fit_count = 0
next_fit_count = 0

# Perform the trials
for _ in range(num_trials):
    # Generate random processes
    processes = [random.randint(50, 400) for _ in range(num_processes)]

    # Initialize memory for each trial
    memory = [memory_size] * num_processes

    # First Fit
    memory_copy = memory.copy()
    for process_size in processes:
        allocated = allocate_process_first_fit(memory_copy, process_size)
        if allocated:
            first_fit_count += 1

    # Best Fit
    memory_copy = memory.copy()
    for process_size in processes:
        allocated = allocate_process_best_fit(memory_copy, process_size)
        if allocated:
            best_fit_count += 1

    # Worst Fit
    memory_copy = memory.copy()
    for process_size in processes:
        allocated = allocate_process_worst_fit(memory_copy, process_size)
        if allocated:
            worst_fit_count += 1

    # Next Fit
    memory_copy = memory.copy()
    last_index = -1
    for process_size in processes:
        allocated, last_index = allocate_process_next_fit(memory_copy, process_size, last_index)
        if allocated:
            next_fit_count += 1

# Calculate the percentages
first_fit_percentage = (first_fit_count / (num_processes * num_trials)) * 100
best_fit_percentage = (best_fit_count / (num_processes * num_trials)) * 100
worst_fit_percentage = (worst_fit_count / (num_processes * num_trials)) * 100
next_fit_percentage = (next_fit_count / (num_processes * num_trials)) * 100

# Display the performance percentages
print("Performance Results:")
print(f"First Fit: {first_fit_percentage}%")
print(f"Best Fit: {best_fit_percentage}%")
print(f"Worst Fit: {worst_fit_percentage}%")
print(f"Next Fit: {next_fit_percentage}%")

# Create a bar graph to represent the performance
algorithms = ['First Fit', 'Best Fit', 'Worst Fit', 'Next Fit']
percentages = [first_fit_percentage, best_fit_percentage, worst_fit_percentage, next_fit_percentage]

plt.bar(algorithms, percentages)
plt.xlabel('Memory Allocation Algorithms')
plt.ylabel('Percentage of Successful Allocations')
plt.title('Memory Allocation Algorithm Performance')
plt.ylim(0, 100)

# Display the graph
plt.show()
performance_evaluation
