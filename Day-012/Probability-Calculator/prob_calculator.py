import copy
import random

class Hat:
    def __init__(self, **kwargs):
        # Get keyworded items
        self.hat = kwargs
        # Make contents list
        self.contents = list()
        # Assign colors to contents
        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)
    # Draw function
    def draw(self, numBalls):
        balls = list()
        # If there is less ball than requested, return all contents
        if len(self.contents) <= numBalls:
            return self.contents
        # Otherwise return randomly selected balls
        for i in range(numBalls):
            ball_picked = random.choice(self.contents)
            balls.append(ball_picked)
            self.contents.pop(self.contents.index(ball_picked))
        return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_find = 0
    # Do experiment
    for i in range(num_experiments):
        # Copy given hat class
        copyHat = copy.deepcopy(hat)
        # Draw requested ball
        balls = copyHat.draw(num_balls_drawn)
        # Increase num_find
        num_find += 1
        # Check experiment is true or not
        for k, v in expected_balls.items():
            # If it is false, then decrease num_find
            if(v > len([i for i in balls if i == k])):
                num_find -= 1
                break
    # Return probability
    return num_find/num_experiments