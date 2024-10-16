import simpy

def machine(env, name, processing_time, previous_machine=None):
    if previous_machine:
        yield previous_machine  # Wait until the previous machine is done
    print(f'{name} started at {env.now}')
    yield env.timeout(processing_time)  # Processing time
    print(f'{name} finished at {env.now}')
    done_event = env.event()  # Create an event to signal completion
    done_event.succeed()
    return done_event

# Create environment
env = simpy.Environment()

# Create the processes, linking them sequentially
machine_a_done = env.process(machine(env, 'Machine A', 3)).value
machine_b_done = env.process(machine(env, 'Machine B', 4, previous_machine=machine_a_done)).value
env.process(machine(env, 'Machine C', 2, previous_machine=machine_b_done))

# Run the simulation
env.run()