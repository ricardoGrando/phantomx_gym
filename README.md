# phantomx Gym env

This is a gym env to work with the phantomx gazebo simulations, allowing the use of [OpenAI Baselines](https://github.com/openai/baselines) and [Stable Baselines](https://github.com/hill-a/stable-baselines) deep reinforcement learning algorithms in the robot navigation training.

This project is a part of the development of some gazebo environments to apply deep-rl algorithms.

[Research Gazebo environments for phantomx robot](https://github.com/ricardoGrando/phantomx_deep_rl_lars)

## Installation

```
git clone https://github.com/ricardoGrando/phantomx_deep_rl_lars
git clone https://github.com/ricardoGrando/gym_phantomx
cd gym_phantomx
pip install -e .
```

This is an example using the OpenAI Baselines `DDPG` algorithm in a phantomx environment.

`.\examples\openai_baselines_ddpg.py`:

```python
import gym
import gym_phantomx
import rospy
import os

env = gym.make('phantomx_Circuit_Simple-v0', env_stage=1, observation_mode=0, continuous=True, goal_list=None)

```


To cite this repository in publications:

    @misc{gymphantomx,
      author = {Grando, Ricardo},
      title = {gym-phantomx},
      year = {2022},
      publisher = {GitHub},
      journal = {GitHub repository},
      howpublished = {\url{https://github.com/ricardoGrando/gym_phantomx}},
    }
# phantomx_gym
