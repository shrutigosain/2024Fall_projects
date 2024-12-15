import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from calculations import *
import random as random


def ideal_scenario(user: 'User', activity_manager: 'Activity', additional_calories: float, weeks: int=12) -> list:
    """
    Perform a simulation to predict weight changes over time based on user data and activities.

    :param user: the user object containing user details such as weight, calorie intake, etc.
    :param activity_manager: the activity manager object containing logged activities and their details.
    :param additional_calories: base additional calories burned from non-workout activities.
    :param weeks: number of weeks for the simulation (default is 12 weeks).

    :returns: array of weight changes over the simulation duration.
    """
    # Simulation parameters
    simulation_duration = weeks * 7  # Duration in days for the number of weeks
    initial_weight = user.weight  # User's initial weight
    weight = initial_weight  # Start with the initial weight
    daily_weights = [weight]  # List to track daily weight changes

    # Take user inputs for required parameters
    workout_days = int(input("Enter the number of workout days per week: "))
    additional_calories = int(input("Enter the additional calories burned daily (non-workout activities): "))
    sleep_duration = int(input("Enter your average sleep duration in hours: "))

    sleep_duration_range = np.random.randint((sleep_duration - 2),(sleep_duration + 2))

    additional_calories_range = np.random.randint((additional_calories - 200 ),(additional_calories + 200))

    # Loop through each day of the simulation
    for day in range(simulation_duration):
        is_workout_day = (day % 7) < workout_days  # Check if the day is a workout day
        workout_calories = 0

        if is_workout_day:
            workout_calories = Calculations.calculate_calories_burned(user, activity_manager)

        # Adjust RMR based on sleep duration
        rmr = Calculations.calculate_daily_rmr_change(daily_weights[-1], user)  # Adjust RMR based on current weight
        rmr_updated = calculate_daily_rmr_change_updated(rmr, sleep_duration_range)

        # Calculate total calories burned
        total_calories_burned = rmr_updated + workout_calories + additional_calories_range

        calorie_intake_range = np.random.randint((user.calorie_intake - 500),(user.calorie_intake + 500))

        # Calculate calorie deficit
        calorie_deficit = total_calories_burned - calorie_intake_range

        # Convert calorie deficit to weight change
        weight -= calorie_deficit / 3500  # 1 lb per 3500 calories
        daily_weights.append(weight)

    return daily_weights, simulation_duration

def visualize_simulation_ideal(weights_over_time: list, simulation_duration: int) -> None:
    """
    Visualizes the results of a weight loss simulation over time.

    :param weights_over_time: a list where each element represents weight at a given day of the simulation.
    :param simulation_duration: total duration of the simulation in days.

    :returns: None
    """

    # Plot the weight trajectory
    plt.figure(figsize=(12, 6))
    plt.plot(range(simulation_duration + 1), weights_over_time, color='blue', label="Weight Trajectory")

    # Add labels and title
    plt.title("Weight Loss Simulation Over Time")
    plt.xlabel("Days")
    plt.ylabel("Weight (lbs)")
    plt.legend()
    plt.grid(True)
    plt.show()


#HYPOTHESIS 1

def monte_carlo_simulation_hypothesis_1(user: 'User', activity_manager: 'Activity', additional_calories: float, weeks: int=12, num_simulations: int=1000):

    """
    Perform a Monte Carlo simulation to predict weight changes over time based on user data and activities.

    :param user: the user object containing user details such as weight, calorie intake, etc.
    :param activity_manager: the activity manager object containing logged activities and their details.
    :param additional_calories: base additional calories burned from non-workout activities.
    :param weeks: number of weeks for the simulation (default is 12 weeks).
    :param num_simulations: number of Monte Carlo iterations to run (default is 1000).

    :returns: a 2D NumPy array where each row represents weight over time for one simulation.
    """

    weights_over_time = []
    simulation_duration = weeks * 7  # Duration in days for the number of weeks
    initial_weight = user.weight  # User's initial weight

    for iteration in range(num_simulations):  # Looping for each simulation
        weight = initial_weight
        daily_weights = [weight]

        for day in range(simulation_duration):  # Simulating for each day

            # Randomizing workout days per week
            workout_days = np.random.randint(2, 7)  # Assuming between 2 and 7 workout days per week
            additional_calories = np.random.randint(200, 700)  # Randomizing additional calories burnt
            is_workout_day = random.random() < (workout_days / 7)  # Probability of working out today

            # Calculating daily workout calories burnt
            workout_calories = 0
            if is_workout_day:
                workout_calories = Calculations.calculate_calories_burned(user, activity_manager)

            rmr = Calculations.calculate_daily_rmr_change(daily_weights[day], user)  # Adjusting RMR based on current weight

            total_calories_burned = rmr + workout_calories + additional_calories

            calorie_deficit = total_calories_burned - user.calorie_intake

            # Converting calorie deficit to weight change
            weight -= calorie_deficit / 3500  # 1 lb per 3500 calories
            daily_weights.append(weight)

        weights_over_time.append(daily_weights)

    # Converting to Numpy Array
    weights_over_time = np.array(weights_over_time)
    return weights_over_time, simulation_duration

#HYPOTHESIS 2

##Updating the RMR calculation based on Sleep Duartion (Randomly chosen between 3 and 10)
def calculate_daily_rmr_change_updated(base_rmr: float, sleep_duration: int) -> float:
    """
    Calculate the adjusted RMR based on sleep duration.
    :param base_rmr: Base Resting Metabolic Rate (RMR)
    :param sleep_duration: Optional parameter, if None a random value between 3-10 is assigned.
    :return: Adjusted RMR

    >>> calculate_daily_rmr_change_updated(2000, 8)
    2000
    >>> calculate_daily_rmr_change_updated(2000, 6)
    1800.0
    """
    if sleep_duration >= 8:
        adjusted_rmr = base_rmr  # No reduction if the duration is greater than 8 hours
    else:
        reduction_factor = 0.05 * (8 - sleep_duration)  # 5% reduction per hour below 8
        adjusted_rmr = base_rmr * (1 - reduction_factor)

    return adjusted_rmr

def monte_carlo_simulation_hypothesis_2(user: 'User', activity_manager: 'Activity', additional_calories: float, weeks: int=12, num_simulations: int=1000):

    """
    Perform a Monte Carlo simulation to predict weight changes over time based on user data and activities.

    :param user: the user object containing user details such as weight, calorie intake, etc.
    :param activity_manager: the activity manager object containing logged activities and their details.
    :param additional_calories: base additional calories burned from non-workout activities.
    :param weeks: number of weeks for the simulation (default is 12 weeks).
    :param num_simulations: number of Monte Carlo iterations to run (default is 1000).

    :returns: a 2D NumPy array where each row represents weight over time for one simulation.
    """

    weights_over_time = []
    simulation_duration = weeks * 7  # Duration in days for the number of weeks
    initial_weight = user.weight  # User's initial weight

    for iteration in range(num_simulations):  # Looping for each simulation
        weight = initial_weight
        daily_weights = [weight]

        for day in range(simulation_duration):  # Simulating for each day

            # Randomizing workout days per week
            workout_days = np.random.randint(2, 7)  # Assuming between 2 and 7 workout days per week
            additional_calories = np.random.randint(200, 700)  # Randomizing additional calories burnt
            is_workout_day = random.random() < (workout_days / 7)  # Probability of working out today

            # Calculating daily workout calories burnt
            workout_calories = 0
            if is_workout_day:
                workout_calories = Calculations.calculate_calories_burned(user, activity_manager)

            sleep_duration = np.random.randint(3, 10)

            rmr = Calculations.calculate_daily_rmr_change(daily_weights[day], user)  # Adjusting RMR based on current weight
            rmr_updated = calculate_daily_rmr_change_updated(rmr, sleep_duration)

            total_calories_burned = rmr_updated + workout_calories + additional_calories

            calorie_intake_range = np.random.randint((user.calorie_intake - user.calorie_intake/2),(user.calorie_intake + user.calorie_intake/2))
            calorie_deficit = total_calories_burned - calorie_intake_range

            # Converting calorie deficit to weight change
            weight -= calorie_deficit / 3500  # 1 lb per 3500 calories
            daily_weights.append(weight)

        weights_over_time.append(daily_weights)

    # Converting to Numpy Array
    weights_over_time = np.array(weights_over_time)
    return weights_over_time, simulation_duration

#vizualization for hypothesis1 and 2
def visualize_simulation(weights_over_time: np.ndarray, simulation_duration: int, num_simulations: int) -> None:
    """
    Visualizes the results of the Monte Carlo weight loss simulation.

    :param weights_over_time: a 2D array where each row represents weight trajectory for one simulation.
    :param simulation_duration: total duration of the simulation in days.
    :param num_simulations: number of Monte Carlo iterations.

    :returns: None
    """
    plt.figure(figsize=(12, 6))
    for i in range(num_simulations):
        plt.plot(range(simulation_duration + 1), weights_over_time[i], alpha=0.05, color='blue')

    # plot the mean trajectory
    mean_weights = weights_over_time.mean(axis=0)
    plt.plot(range(simulation_duration + 1), mean_weights, color='black', linewidth=2, label='Mean Weight')

    plt.title("Monte Carlo Simulation of Weight Loss Over 12 Weeks")
    plt.xlabel("Days")
    plt.ylabel("Weight (lbs)")
    plt.grid(True)

    plt.legend()
    plt.show()

#hypothesis 3

def monte_carlo_simulation_hypothesis_3(user, activity_manager, additional_calories, weeks=12, num_simulations=1000, weight_offsets=[0, 40, -40]):
    """
    Perform Monte Carlo simulation for three weight scenarios: initial weight, +40 lbs, and -40 lbs.

    Args:
        user (User): The user object containing user details such as weight, calorie intake, etc.
        activity_manager (Activity): The activity manager object containing logged activities and their details.
        additional_calories (float): Base additional calories burned from non-workout activities.
        weeks (int): Number of weeks for the simulation (default is 12 weeks).
        num_simulations (int): Number of Monte Carlo iterations to run (default is 1000).
        weight_offsets (list): List of weight offsets to simulate (default is [0, +40, -40]).

    Returns:
        dict: A dictionary containing weights over time for each weight scenario.
    """

    results = {}  # To store results for each weight offset

    for offset in weight_offsets:
        initial_weight = user.weight + offset
        weights_over_time = []
        simulation_duration = weeks * 7  # Duration in days

        for iteration in range(num_simulations):
            weight = initial_weight
            daily_weights = [weight]

            for day in range(simulation_duration):
                # Randomizing workout days per week
                workout_days = np.random.randint(2, 7)
                additional_calories = np.random.randint(200, 700)
                is_workout_day = random.random() < (workout_days / 7)

                # Calculating daily workout calories burned
                workout_calories = 0
                if is_workout_day:
                    workout_calories = Calculations.calculate_calories_burned(user, activity_manager)

                sleep_duration = np.random.randint(3, 10)

                # Adjusting RMR based on current weight
                rmr = Calculations.calculate_daily_rmr_change(daily_weights[day], user)
                rmr_updated = calculate_daily_rmr_change_updated(rmr, sleep_duration)

                total_calories_burned = rmr_updated + workout_calories + additional_calories

                calorie_intake_range = np.random.randint(
                    (user.calorie_intake - user.calorie_intake / 2),
                    (user.calorie_intake + user.calorie_intake / 2)
                )
                calorie_deficit = total_calories_burned - calorie_intake_range

                # Converting calorie deficit to weight change
                weight -= calorie_deficit / 3500
                daily_weights.append(weight)

            weights_over_time.append(daily_weights)

        # Store results for the current offset
        results[offset] = np.array(weights_over_time)

    return results, simulation_duration

def visualize_simulation_by_weight_3(results, simulation_duration, num_simulations):
    """
    Visualizes the results of Monte Carlo weight loss simulation for multiple weight scenarios.

    Args:
        results (dict): A dictionary where keys are weight offsets and values are 2D arrays of weight trajectories.
        simulation_duration (int): Total duration of the simulation in days.
        num_simulations (int): Number of Monte Carlo iterations.

    Returns:
        None
    """
    plt.figure(figsize=(12, 6))

    # Define colors for each weight scenario
    colors = {
        0: 'blue',       # Initial weight
        40: 'green',     # +40 lbs
        -40: 'red'       # -40 lbs
    }

    for weight_offset, weights_over_time in results.items():
        for i in range(num_simulations):
            plt.plot(range(simulation_duration + 1), weights_over_time[i], alpha=0.05, color=colors[weight_offset])

        # Add a label for the first line of each weight offset
        plt.plot([], [], color=colors[weight_offset], label=f"Initial Weight Offset: {weight_offset} lbs")

        mean_weights = weights_over_time.mean(axis=0)
        plt.plot(range(simulation_duration + 1), mean_weights, color="black", linewidth=1,
                 label=f"Mean Weight Offset: {weight_offset} lbs")

    # Add title, labels, legend, and grid
    plt.title("Monte Carlo Simulation of Weight Loss for Different Weight Scenarios")
    plt.xlabel("Days")
    plt.ylabel("Weight (lbs)")

    plt.legend(loc="upper left", bbox_to_anchor=(1.05, 1), borderaxespad=0.)
    plt.grid(True)
    plt.tight_layout(rect=[0, 0, 0.85, 1])

    # Show the plot
    plt.show()


def visualize_simulation_by_weight_separate(results, simulation_duration, num_simulations):
    """
    Visualizes the results of Monte Carlo weight loss simulation for multiple weight scenarios.

    Args:
        results (dict): A dictionary where keys are weight offsets and values are 2D arrays of weight trajectories.
        simulation_duration (int): Total duration of the simulation in days.
        num_simulations (int): Number of Monte Carlo iterations.

    Returns:
        None
    """

    for weight_offset, weights_over_time in results.items():
        plt.figure(figsize=(12, 6))
        for i in range(num_simulations):
            plt.plot(range(simulation_duration + 1), weights_over_time[i], alpha=0.05, color='blue')

        mean_weights = weights_over_time.mean(axis=0)
        plt.plot(range(simulation_duration + 1), mean_weights, color="black", linewidth=1,
                 label=f"Mean Weight Offset: {weight_offset} lbs")

        plt.title(f"Monte Carlo Simulation of Weight Loss (Initial Weight Offset: {weight_offset} lbs)")
        plt.xlabel("Days")
        plt.ylabel("Weight (lbs)")
        plt.grid(True)
        plt.show()
