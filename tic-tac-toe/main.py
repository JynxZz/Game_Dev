import numpy as np
from tictactoeia import TicTacToeAI
from agent import Agent


# Constants
NB_EPISODES = 1000


# Training
def train():
    # Variables
    rewards = []
    mean_rewards = []
    record = 0

    # Initialize the environment
    env = TicTacToeAI()
    agent = Agent()

    # Training
    while True:
        # Get state
        state_old = agent.get_state(env)

        # Get action
        action = agent.get_action(state_old)

        # Apply action if player is X
        player = env.order[0]
        if player == "X":
            action, reward, done = env.play_step(player, action)
        else:
            action, reward, done = env.play_step(player)

        # Get new state
        state_new = agent.get_state(env)

        # Store experience
        # Short term memory
        agent.train_short_memory(state_old, action, reward, state_new, done)

        # Remember
        agent.remember(state_old, action, reward, state_new, done)

        if done:
            # Train long term memory
            env.reset()
            agent.n_games += 1
            agent.train_long_memory()

            # Save record
            if reward > record:
                record = reward
                agent.model.save()

            print(
                f"Game {agent.n_games} - Winner: {done} - Reward: {reward} - Record: {record}"
            )

            # Plotting
            rewards.append(reward)
            mean_rewards.append(np.mean(rewards))

            # Check if training is done
            if agent.n_games == NB_EPISODES:
                break
