# Movie Theater Simulation

# Goal: Average wait of 10 mins or less

# arrive at theater
# get in line to buy ticket
# buy a ticket
# wait in line to have their ticket checked
# have their ticket checked
# decide to buy concessions or not
# buy concessions or go directly to seat

import simpy
import random
import statistics

wait_times = []

class Theater(object):
    def __init__(self, env, num_cashiers, num_ushers, num_servers):
        self.env = env
        self.cashier = simpy.Resource(env, num_cashiers)
        self.usher = simpy.Resource(env, num_ushers)
        self.server = simpy.Resource(env, num_servers)

    def purchase_ticket(self, moviegoer):
        yield self.env.timeout(random.randint(1,2))

    def check_ticket(self, moviegoer):
        yield self.env.timeout(0.5)

    def sell_food(self, moviegoer):
        yield self.env.timeout(random.randint(1,6))
