import gym
import gym_deepracer
import time


env = gym.make('deepracer-v0')   # starts as 1000x600
env.update_random_settings({'car_rand_loc':False})
env.resize(128,128) # resize to 128x128 for learning

state = env.reset()

for _ in range(20):
    throttle = 5  # accelerate at 2 m/s^2
    turn = 15     # turn wheels 15 degrees
    action = (throttle, turn)
    state, reward, done, _ = env.step(action)
    time.sleep(1/10) # run at 10fps
env.quit()