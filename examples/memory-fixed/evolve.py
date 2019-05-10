"""
This example produces networks that can remember a fixed-length sequence of bits. It is
intentionally very (overly?) simplistic just to show the usage of the NEAT library. However,
if you come up with a more interesting or impressive example, please submit a pull request!

This example also demonstrates the use of a custom activation function.
"""

from __future__ import division, print_function

import math
import os
import random

import neat
import visualize


# Demonstration of how to add your own custom activation function.
# This sinc function will be available if my_sinc_function is included in the
# config file activation_options option under the DefaultGenome section.
# Note that sinc is not necessarily useful for this example, it was chosen
# arbitrarily just to demonstrate adding a custom activation function.
def sinc(x):
    return 1.0 if x == 0 else math.sin(x) / x


# N is the length of the test sequence.
N = 3
# num_tests is the number of random examples each network is tested against.
num_tests = 2 ** (N+2)



def eval_genome(genome, config):
    net = neatfast.nn.RecurrentNetwork.create(genome, config)

    error = 0.0
    for _ in range(num_tests):
        # Create a random sequence, and feed it to the network with the
        # second input set to zero.
        seq = [random.choice((0.0, 1.0)) for _ in range(N)]
        net.reset()
        for s in seq:
            inputs = [s, 0.0]
            net.activate(inputs)

        # Set the second input to one, and get the network output.
        for s in seq:
            inputs = [0.0, 1.0]
            output = net.activate(inputs)

            error += (round(output[0]) - s) ** 2

    return 4.0 - 4.0 * (error / (N * num_tests))


def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        genome.fitness = eval_genome(genome, config)


def run():
    # Determine path to configuration file.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config')
    config = neatfast.Config(neatfast.DefaultGenome, neatfast.DefaultReproduction,
                         neatfast.DefaultSpeciesSet, neatfast.DefaultStagnation,
                         config_path)

    # Demonstration of saving a configuration back to a text file.
    config.save('test_save_config.txt')

    # Demonstration of how to add your own custom activation function.
    # This sinc function will be available if my_sinc_function is included in the
    # config file activation_options option under the DefaultGenome section.
    config.genome_config.add_activation('my_sinc_function', sinc)

    pop = neatfast.Population(config)
    stats = neatfast.StatisticsReporter()
    pop.add_reporter(stats)
    pop.add_reporter(neatfast.StdOutReporter(True))

    if 1:
        pe = neatfast.ParallelEvaluator(4, eval_genome)
        winner = pop.run(pe.evaluate, 1000)
    else:
        winner = pop.run(eval_genomes, 1000)


    # Log statistics.
    stats.save()

    # Show output of the most fit genome against a random input.
    print('\nBest genome:\n{!s}'.format(winner))
    print('\nOutput:')
    winner_net = neatfast.nn.RecurrentNetwork.create(winner, config)
    num_correct = 0
    for n in range(num_tests):
        print('\nRun {0} output:'.format(n))
        seq = [random.choice((0.0, 1.0)) for _ in range(N)]
        winner_net.reset()
        for s in seq:
            inputs = [s, 0.0]
            winner_net.activate(inputs)
            print('\tseq {0}'.format(inputs))

        correct = True
        for s in seq:
            output = winner_net.activate([0, 1])
            print("\texpected {0:1.5f} got {1:1.5f}".format(s, output[0]))
            correct = correct and round(output[0]) == s
        print("OK" if correct else "FAIL")
        num_correct += 1 if correct else 0

    print("{0} of {1} correct {2:.2f}%".format(num_correct, num_tests, num_correct/num_tests))

    node_names = {-1: 'input', -2: 'gate', 0: 'output'}
    visualize.draw_net(config, winner, True, node_names=node_names)
    visualize.plot_stats(stats, ylog=False, view=True)


if __name__ == '__main__':
    run()