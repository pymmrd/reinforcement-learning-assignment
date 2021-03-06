from MyImprovedDQN import *
import os
import sys
import getopt

def reward_func_robot(env, state1, state2, done):
    if done:
        return 200
    return -1

def reward_func(env, state, state2, done):
    x, x_dot, theta, theta_dot = state
    r1 = (env.x_threshold - abs(x)) / env.x_threshold - 0.8
    r2 = (env.theta_threshold_radians - abs(theta)) / env.theta_threshold_radians - 0.5
    return r1 + r2

def reward_func_car(env, state1, state2, done):
    if done:
        return 400
    else:
        return abs(state1[0] - state2[0]) * 100

def test_cartPole():

    env_mountainCar = gym.make('CartPole-v0')
        #bounds = list(zip(env_mountainCar.observation_space.low, env_mountainCar.observation_space.high))
        #zones = (20,20)
        #tf.reset_default_graph()
    env_mountainCar = env_mountainCar.unwrapped
    with tf.Session() as sess:
        qlearning = ImprovedDQN(env_mountainCar, sess, episode=2000, max_t = 200, reward_func = reward_func, model_name = os.path.join("./savedModel", "cartpole-Idqn.ckpt"))
        #qlearning.learning(32)
        qlearning.test(100, 20000)

def test_Acrobot():
    env_mountainCar = gym.make('Acrobot-v1')
        #bounds = list(zip(env_mountainCar.observation_space.low, env_mountainCar.observation_space.high))
        #zones = (20,20)
        #tf.reset_default_graph()
    env_mountainCar = env_mountainCar.unwrapped
    with tf.Session() as sess:
        qlearning = ImprovedDQN(env_mountainCar, sess, episode=2000, max_t = 500, reward_func = reward_func_car, model_name = os.path.join("./savedModel", "acrobot-Idqn.ckpt"))
        #qlearning.learning(32)
        qlearning.test(100, 20000)

def test_MountainCar():

    env_mountainCar = gym.make('MountainCar-v0')
        #bounds = list(zip(env_mountainCar.observation_space.low, env_mountainCar.observation_space.high))
        #zones = (20,20)
        #tf.reset_default_graph()
    env_mountainCar = env_mountainCar.unwrapped
    with tf.Session() as sess:
        qlearning = ImprovedDQN(env_mountainCar, sess, episode=2000, max_t = 500, reward_func = reward_func_car, model_name = os.path.join("./savedModel", "mountaincar-Idqn.ckpt"))
        #qlearning.learning(32)
        qlearning.test(100, 2000)

def usage():
    print("---------------Usage----------------")
    print("-h or --help, get the usage message")
    print("-c or --cartpole, run the cartpole-v0 gym envirmonent")
    print("-m or --mountaincar, run the mountaincar-v0 gym environment")
    print("-a or --acrobot, run the acrobot-v1 gym environment")
    print("--------------END Usage--------------")

if __name__ == '__main__':

    if len(sys.argv) < 2:
        usage()
        sys.exit(-1)
    
    try:
        options, args = getopt.getopt(sys.argv[1:],"hcma",["help", "cartpole", "mountaincar", "acrobot"])
    except getopt.GetoptError:
        sys.exit(-2)
    
    for name, value in options:
        if name in ("-h", "-help"):
            usage()
        if name in ("-c", "--cartpole"):
            test_cartPole()
        if name in ("-m", "--mountaincar"):
            test_MountainCar()
        if name in ("-a", "--acrobot"):
            test_Acrobot()
        