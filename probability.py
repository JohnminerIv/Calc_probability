import random


def prob_calculator(prob_head, num_trials, flips_p_trial=3, desired_outcomes=[[1,1,0],[1,0,1],[0,1,1]], p_of_all=True):
    """arg1 is the probability of getting a heads
    arg2 is the number of times to try to meet the desired outcomes
    arg3 is the number of times to flip the coin per trial must match length of lists in desired_outcomes
    arg4 is a list of desired outcomes with 1 representing heads and 0 representing tails
    arg5 defines if you want the propability of all your desired outcomes True=(P(a)+P(b)+P(c))
        or the average False=((P(a)+P(b)+P(c))/len(desired_outcomes))"""
    total = 0
    for i in range(num_trials):
        if trial(prob_head, flips_p_trial) in desired_outcomes:
            total += 1
    if p_of_all is True:
        return total/num_trials
    else:
        return total/num_trials/len(desired_outcomes)


def trial(prob_head, flips):
    event = [1, 0]
    probability = [prob_head, 1 - prob_head]
    outcome = []
    for i in range(flips):
        outcome.append(random.choices(event, probability)[0])
    return outcome



if __name__ == '__main__':
    # these first two should output around 0.027 because they calculate
    # the probability of any combination with 2 heads 1 tail which is 3(0.1^2(1-0.1))
    # they actually do the exact same thing
    print(prob_calculator(0.10, 10000))
    print(prob_calculator(0.10, 10000, 3, [[1,1,0],[1,0,1],[0,1,1]], True))
    # this next one should output around 0.009 because it takes the average of all the possible
    # probabilities that include 2 heads 1 tail or 3(0.1^2(1-0.1))/3
    print(prob_calculator(0.10, 10000, 3, [[1,1,0],[1,0,1],[0,1,1]], False))
    # these next three should return around 0.009 because they calculate
    # the probability of an individaul combination of 2 heads 1 tail or (0.1^2(1-0.1))
    print(prob_calculator(0.10, 10000, 3, [[1,1,0]]))
    print(prob_calculator(0.10, 10000, 3, [[1,0,1]]))
    print(prob_calculator(0.10, 10000, 3, [[0,1,1]]))
    # this one should return 0.125 or a^2(a-1) or 0.5*0.5*0.5
    print(prob_calculator(0.50, 10000, 3, [[1,1,0]]))
    # this next one should be around 0.0256 or a^2(a-1)^2 or 0.2*0.8*0.8*0.2
    print(prob_calculator(0.2, 10000, 4, [[0,1,1,0]]))
