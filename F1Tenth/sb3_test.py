
import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv, SubprocVecEnv
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.callbacks import CheckpointCallback
import f110_gym
import tdqm.rich as tqdm

# Define the F1Tenth Gym environment
env_id = 'f110_gym:f110-v0'
env = gym.make(env_id, render_mode='human_fast')

# debug: env action and observation space
print(env.action_space)
print(env.observation_space)

# Create a vectorized environment
# n_envs = 4
# env = make_vec_env(env_id, n_envs=n_envs, seed=0)

# Define the MLP policy
policy = 'MultiInputPolicy'

# Create the PPO agent
model = PPO(policy, env, verbose=1)

# enable gui??
env.reset()
env.render()

# test, but add trainloop
# for _ in range(1000):
#     env.step(env.action_space.sample())
#     env.render()
# env.close()

# set up model in learning mode with goal number of timesteps to complete
model.learn(total_timesteps=10000)
print("got here")
obs = env.reset()
for i in tqdm.tqdm(range(10000)):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    try:
        env.render()
    except Exception as e:
        print(e)
        print("failure in render, continuing...")
    if done:
        obs = env.reset()
    if i % 100 == 0:
        print("saving...")
        model.save("sb3_mlp_policy_f110")


# Evaluate the agent
mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=10)

# Save the agent
model.save("sb3_mlp_policy_f110")
