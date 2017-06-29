"""
2-input XOR example -- this is most likely the simplest possible example.
"""

from __future__ import print_function

import datetime
import math
import os

import neat

from database import Database
from predictor import visualize

# 2-input XOR inputs and expected outputs.
xor_inputs =  [(0.0, 0.0), (0.0, 1.0), (1.0, 0.0), (1.0, 1.0)]
xor_outputs = [(0.0 ,0.0), (1.0, 0.0), (1.0 ,0.0), (0.0, 1.0)]

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)


db = Database()
data = db.load_values()


def my_eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        genome.fitness = 0.0
        net = neat.nn.FeedForwardNetwork.create(genome, config)

        trials = 0
        for day in daterange(data['min_date'], data['max_date']):
            point = data['values'][day]
            input_vector = (point['day_of_week'], point['day'], point['month'], point['year'], 1)
            next_point = data['values'][day + datetime.timedelta(days=1)]
            expected_vector = (next_point['day_of_week'], next_point['day'], next_point['month'], next_point['year'])
            avergage_vector = (data['avg']['day_of_week'], data['avg']['day'], data['avg']['month'], data['avg']['year'])
            output_vector = net.activate(input_vector)
            fitness = 0.0
            fitness += ((output_vector[0] - expected_vector[0]) / avergage_vector[0]) ** 2
            fitness += ((output_vector[1] - expected_vector[1]) / avergage_vector[1]) ** 2
            fitness += ((output_vector[2] - expected_vector[2]) / avergage_vector[2]) ** 2
            fitness += ((output_vector[3] - expected_vector[3]) / avergage_vector[3]) ** 2
            genome.fitness += math.sqrt(fitness)

            trials += 1
        genome.fitness = trials / genome.fitness



def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        genome.fitness = 8.0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        for xi, xo in zip(xor_inputs, xor_outputs):
            output = net.activate(xi)
            genome.fitness -= (output[0] - xo[0]) ** 2 + (output[1] - xo[1]) ** 2


def run(config_file):
    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                 neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                 config_file)


    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))

    # Run for up to 300 generations.
    winner = p.run(my_eval_genomes, 100)

    # Display the winning genome.
    print('\nBest genome:\n{!s}'.format(winner))

    # Show output of the most fit genome against training data.
    print('\nOutput:')
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)

    for day in daterange(data['min_date'], data['max_date']):
        point = data['values'][day]
        input_vector = (point['day_of_week'], point['day'], point['month'], point['year'], 1)
        next_point = data['values'][day + datetime.timedelta(days=1)]
        expected_vector = (next_point['day_of_week'], next_point['day'], next_point['month'], next_point['year'])
        output_vector = winner_net.activate(input_vector)
        print("input {!r}, expected output {!r}, got {!r}".format(input_vector, expected_vector, output_vector))

    node_names = {-1:'day_of_week', -2: 'day', -3: 'month', -4: 'year', -5:'one', 0:'day_of_week_o', 1: 'day_o', 2: 'month_o', 3: 'year_o'}
    visualize.draw_net(config, winner, True, node_names=node_names)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)

    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-4')
    p.run(my_eval_genomes, 10)


if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config_neat')
    run(config_path)