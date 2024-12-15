from user import *
from activity import *

class Calculations:

    def calculate_calories_burned( user:'User', activity_manager: 'Activity') -> float:
        """
        Calculate the total calories burned during all logged activities.

        Args:
            user (User): The user object containing user details like weight.
            activity_manager (Activity): The activity manager object containing logged activities.

        Returns:
            float: Total calories burned from all activities.

            >>> user = User(30, 175, 75, 2000, 'male')
            >>> activity_manager = Activity()
            >>> activity_manager.activities = { "Running": {"met_value": 7.5, "duration_minutes": 30},"Cycling": {"met_value": 6.8, "duration_minutes": 45}}
            >>> calculate_calories_burned(user, activity_manager, 300)
            956.625
        """

        # Calculate workout calories using MET values, duration (in hours), and user's weight
        workout_calories = sum(
            activity["met_value"] * (activity["duration_minutes"] / 60) * user.weight
            for activity in activity_manager.activities.values()
        )
        return workout_calories


    def calculate_daily_rmr_change(weight: float, user: 'User') -> float:
        """
        Calculate the Resting Metabolic Rate (RMR) based on the user's weight, height, age, and gender.

        Args:
            user (User): The user object containing details like weight, height, age, and gender.

        Returns:
            float: The calculated RMR in kcal/day.

            >>> user = User(30, 175, 75, 2000, 'male')
            >>> calculate_daily_rmr_change(75, user)
            1684.7750000000003

        Raises:
        ValueError: If the gender is not 'male' or 'female'.

        """

        if user.gender == "male":
            # RMR formula for males
            rmr = (10 * 0.453592 * weight) + (6.25 * 2.54 * user.height) - (5 * user.age) + 5
        elif user.gender == "female":
            # RMR formula for females
            rmr = (10 * 0.453592 * weight) + (6.25 * 2.54 * user.height) - (5 * user.age) - 161
        else:
            # Error for invalid gender input
            raise ValueError("Invalid gender. Please enter 'male' or 'female'.")
        return rmr
