import simpy
import random
from statistics import mean

class Airport:
    def __init__(self, env, num_checkers, arrival_rate, log_file):
        self.env = env
        self.checkers = [simpy.Resource(env, capacity=1) for _ in range(num_checkers)]
        self.arrival_rate = arrival_rate
        self.log_file = log_file
        self.wait_times = []

    def log_event(self, message):
        with open(self.log_file, 'a') as f:
            f.write(f"{message}\n")
    
    def log_statistics(self):
        if self.wait_times:
            avg_wait = mean(self.wait_times)
            max_wait = max(self.wait_times)
            min_wait = min(self.wait_times)
            self.log_event("\nFinal Statistics:")
            self.log_event(f"Average wait time: {avg_wait:.2f} minutes")
            self.log_event(f"Maximum wait time: {max_wait:.2f} minutes")
            self.log_event(f"Minimum wait time: {min_wait:.2f} minutes")
            self.log_event(f"Total passengers processed: {len(self.wait_times)}")
    
    def get_queue_lengths(self):
        # Get the length of each queue as a list
        return [len(checker.queue) for checker in self.checkers]
    
    def find_shortest_queue(self):
        queue_lengths = self.get_queue_lengths()
        min_length = min(queue_lengths)
        shortest_queues = [i for i, length in enumerate(queue_lengths) if length == min_length]
        return random.choice(shortest_queues)
    
    def id_check(self, passenger_id):
        checker_id = self.find_shortest_queue()
        arrival_time = self.env.now

        queue_lengths = ' '.join(map(str, self.get_queue_lengths()))
        self.log_event(f"Passenger {passenger_id} arrives at {arrival_time:.2f} with queue lengths: {queue_lengths}")

        with self.checkers[checker_id].request() as req:
            yield req

            # Log start of ID check
            check_start = self.env.now
            wait_time = check_start - arrival_time
            self.wait_times.append(wait_time)

            self.log_event(f"Passenger {passenger_id} starts ID check at {check_start:.2f}")

            check_duration = random.choice([1,2])
            yield self.env.timeout(check_duration)

            check_end = self.env.now
            self.log_event(f"Passenger {passenger_id} ends ID check at {check_end:.2f}")

    def passenger_generator(self):
        passenger_id = 0
        while True:
            yield self.env.timeout(random.expovariate(self.arrival_rate))
            passenger_id += 1
            self.env.process(self.id_check(passenger_id))

def run_simulation(sim_time=60, num_checkers=5, arrival_rate=5, log_file='airport-simulation/log-02.txt'):
    # Clear log file
    open(log_file, 'w').close()

    # Create environment and start simulation
    env = simpy.Environment()
    simulation = Airport(env, num_checkers, arrival_rate, log_file)
    env.process(simulation.passenger_generator())
    env.run(until=sim_time)

    # Log statistics
    simulation.log_statistics()

if __name__ == '__main__':
    run_simulation()