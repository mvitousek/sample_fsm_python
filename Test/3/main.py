import os, sys
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '..'))
from benchmark_tools.Timer import Timer
from Population import Population
from Utilities import relative_average
from Other import build_random_population
from retic import List, Void, Tuple

def run() ->Void:
    simulation_to_lines(evolve(build_random_population(100), 10, 2, 1))
    return

def evolve(p: Population, c: int, s: int, r: int) ->List(float):
    """
    Computes the list of average payoffs over the evolution of population
    p for c cycles of match_ups with r rounds per match and at birth/death
    rate of s
    :param p: Population
    :param c: Natural
    :param s: Natural
    :param r: Natural
    :return: [float]
    """
    payoffs = []
    for i in range(c):
        p2 = p.match_up(r)
        pp = p2.payoffs()
        p3 = p2.regenerate(s)
        payoffs = payoffs + [relative_average(pp, r)]
        p = p3
    return payoffs

def simulation_to_lines(data: List(float)) ->List(Tuple(int, float)):
    """
    Turn average payoffs into a list of Cartesian points
    :param data: [Payoffs]
    :return: None
    """
    result = []
    counter = 0
    for payoff in data:
        result = result + [(counter, payoff)]
        counter += 1
    return result
t = Timer()
with t:
    run()

