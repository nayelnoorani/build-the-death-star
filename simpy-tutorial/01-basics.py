import simpy

# Create a SimPy environment
env = simpy.Environment()

# Function that simulates a process
def task_process(env):
    print(f"Task is starting at time {env.now}")
    yield env.timeout(3) # Wait for 3 time units
    print(f"Task resumed at {env.now}")

# Add the process to the environment
env.process(task_process(env))

# Run the simulation
env.run()