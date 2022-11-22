import gym
import gym_minigrid
import dreamerv2.api as dv2
from learn2learn.gym.envs import HalfCheetahForwardBackward-v1

config = dv2.defaults.update({
    'logdir': '~/logdir/minigrid',
    'log_every': 1e3,
    'train_every': 10,
    'prefill': 1e5,
    'actor_ent': 3e-3,
    'loss_scales.kl': 1.0,
    'discount': 0.99,
    'env_name': "HalfCheetahForwardBackward-v1"
}).parse_flags()


def make_env():
    env = gym.make(config['env_name'])
    # env = ch.envs.ActionSpaceScaler(env)
    return env

env = gym.make(config['env_name'])
print("env")
print(env)
print("env.sample_tasks(1)")
print(env.sample_tasks(1))
print("env.get_task()")
print(env.get_task())

action = env.action_space.sample()
obs = env.step(action)
print('obs')
print(obs)


# for task in [env.get_task(), env.sample_tasks(1)[0]]:
#     env.set_task(task)
#     env.reset()
#     action = env.action_space.sample()
#     env.step(action)
# seed = 42

# env = l2l.gym.AsyncVectorEnv([make_env for _ in range(num_workers)])
# # env = l2l.gym.AsyncVectorEnv([make_env for _ in range(num_workers)])
# env.seed(seed)
# env.set_task(env.sample_tasks(1)[0])

# env = gym.make('MiniGrid-DoorKey-6x6-v0')
# env = gym_minigrid.wrappers.RGBImgPartialObsWrapper(env)
# dv2.train(env, config)
