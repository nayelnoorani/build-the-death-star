import simpy
import random
import numpy as np

# Set seeds for reproducibility
RANDOM_SEED = 42  # The answer to the Ultimate Question of Life, the Universe, and Everything
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

SIM_TIME = 8 * 60  # in minutes
PASSENGER_ARRIVAL_RATE = 50  # passengers per minute
MEAN_ID_CHECK_TIME = 0.75  # minutes
MIN_PERSONAL_CHECK_TIME = 0.5  # minutes
MAX_PERSONAL_CHECK_TIME = 1.0  # minutes
NUM_SIMULATIONS = 10  # Number of simulations to run
MAX_WAITING_TIME = 15  # in minutes

def generate_passenger_arrivals(env):
    while True:
        yield env.timeout(random.expovariate(PASSENGER_ARRIVAL_RATE))
        env.process(passenger_process(env))

def passenger_process(env):
    arrival_time = env.now
    
    with id_checkers.request() as req:
        yield req
        id_check_start = env.now
        id_check_duration = random.expovariate(1/MEAN_ID_CHECK_TIME)
        yield env.timeout(id_check_duration)
        id_check_end = env.now
    
    shortest_queue = min(personal_checkers, key=lambda x: len(x.queue))
    with shortest_queue.request() as req:
        yield req
        personal_check_start = env.now
        personal_check_duration = random.uniform(MIN_PERSONAL_CHECK_TIME, MAX_PERSONAL_CHECK_TIME)
        yield env.timeout(personal_check_duration)
        personal_check_end = env.now
    
    total_time = env.now - arrival_time
    service_time = (id_check_end - id_check_start) + (personal_check_end - personal_check_start)
    wait_time = total_time - service_time
    
    waiting_times.append(wait_time)

def run_simulation(num_id_checkers, num_personal_checkers):
    global id_checkers, personal_checkers, waiting_times
    
    env = simpy.Environment()
    id_checkers = simpy.Resource(env, capacity=num_id_checkers)
    personal_checkers = [simpy.Resource(env, capacity=1) for _ in range(num_personal_checkers)]
    waiting_times = []
        
    env.process(generate_passenger_arrivals(env))
    env.run(until=SIM_TIME)
    
    return np.mean(waiting_times) if waiting_times else 0

def run_multiple_simulations(num_id_checkers, num_personal_checkers):
    random.seed(RANDOM_SEED)
    np.random.seed(RANDOM_SEED)
    total_wait_time = sum(run_simulation(num_id_checkers, num_personal_checkers) for _ in range(NUM_SIMULATIONS))
    return total_wait_time / NUM_SIMULATIONS

def reduce_resources(num_id_checkers, num_personal_checkers):
    if num_id_checkers > 0 and num_personal_checkers > 0:
        if num_id_checkers == num_personal_checkers:
            num_id_checkers -= 1
        elif num_id_checkers < num_personal_checkers:
            num_personal_checkers -= 1
    return (num_id_checkers, num_personal_checkers)

def increase_resources(num_id_checkers, num_personal_checkers):
    if num_id_checkers == num_personal_checkers:
        num_id_checkers += 1
    elif num_id_checkers > num_personal_checkers:
        num_personal_checkers += 1
    return (num_id_checkers, num_personal_checkers)

def print_current_parameters(num_id_checkers, num_personal_checkers, average_wait_time):
    print(f"Number of ID checkers: {num_id_checkers}")
    print(f"Number of personal checkers: {num_personal_checkers}")
    print(f"Average wait time: {average_wait_time:.2f} minutes")

def main():
    num_id_checkers = PASSENGER_ARRIVAL_RATE // 2
    num_personal_checkers = PASSENGER_ARRIVAL_RATE // 2
    decision_delta = 5 # minutes
    max_iterations = 100  # maximum number of iterations
    stabilization_count = 0  # counter for stabilization period
    stabilization_threshold = 5  # number of iterations to consider the system stable
    
    print("Welcome to the Airport Wait Times Simulation!\nInitial parameters:\n")
    print(f"Passenger arrival rate: {PASSENGER_ARRIVAL_RATE} passengers per minute")
    print(f"Target wait time: {MAX_WAITING_TIME} minutes")
    
    average_wait_time = run_multiple_simulations(num_id_checkers, num_personal_checkers)
    print_current_parameters(num_id_checkers, num_personal_checkers, average_wait_time)

    for iteration in range(max_iterations):
        if abs(MAX_WAITING_TIME - average_wait_time) < decision_delta:
            stabilization_count += 1
            if stabilization_count >= stabilization_threshold:
                print(f"Solution stabilized after {iteration + 1} iterations.")
                break
        else:
            stabilization_count = 0  # Reset stabilization count if we're not within the delta

        if average_wait_time > MAX_WAITING_TIME:
            num_id_checkers, num_personal_checkers = increase_resources(num_id_checkers, num_personal_checkers)
        else:
            num_id_checkers, num_personal_checkers = reduce_resources(num_id_checkers, num_personal_checkers)

        average_wait_time = run_multiple_simulations(num_id_checkers, num_personal_checkers)
        print_current_parameters(num_id_checkers, num_personal_checkers, average_wait_time)

        if iteration == max_iterations - 1:
            print("Maximum number of iterations reached. No solution found.\nPrinting latest parameters:")

    print_current_parameters(num_id_checkers, num_personal_checkers, average_wait_time)
    print("Thank you for using the Airport Wait Times Simulation!")

if __name__ == "__main__":
    main()