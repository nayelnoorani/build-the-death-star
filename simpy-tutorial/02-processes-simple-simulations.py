import simpy

# Function that simulates a process
def machine(env, name, work_time, idle_time, initial_delay):
    yield env.timeout(initial_delay)
    while True:
        print(f"{name} started working at {env.now}")
        yield env.timeout(work_time)
        print(f"{name} idling at {env.now}")
        yield env.timeout(idle_time)

# Create environment
env = simpy.Environment()

# Add two machine processes to environment
env.process(machine(env, 'Machine 1', 5, 2, 0))
env.process(machine(env, 'Machine 2', 3, 1, 2))

# Run simulation for 20 time units
env.run(until=20)