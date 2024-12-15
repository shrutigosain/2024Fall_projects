
import pandas as pd

class Activity:

    def __init__(self):
        """
        Initializes an Activity instance.

        :param activities: dictionary to store activity descriptions and details.
        :param total_duration_minutes: tracks total duration of activities in minutes.

        >>> activity_manager = Activity()
        >>> activity_manager.activities
        {}
        >>> activity_manager.total_duration_minutes
        0
        """
        self.activities = {}  # Dictionary to store activities and their durations
        self.total_duration_minutes = 0  # To keep track of the total duration of all activities


    def prompt_duration(self) -> int:
        """
        Prompts the user to input the duration of an activity in hours and minutes.
        Ensures the entered duration is positive and valid.

        :returns: the duration of the activity in minutes.

        """

        while True:
            try:
                # Asking user for input duration
                print(" You will be prompted to enter your workout duration in hours and then minutes..")
                hours = int(input("Enter the duration in hours: "))
                minutes = int(input("Enter the duration in minutes: "))

                if hours < 0 or minutes < 0 or (hours == 0 and minutes == 0):
                    print("Duration must be positive and greater than 0. Please try again.")
                    continue
                duration_minutes = hours * 60 + minutes  # Convert hours to minutes
                return duration_minutes

            except ValueError:
                print("Invalid input. Please enter valid numbers for hours and minutes.")


    def add_activity(self, description: str, met_value: float) -> bool:
        """
        Adds an activity to the list after validating the total duration.

        :param description: description of the activity.
        :param met_value: MET value associated with the activity.

        :returns: true if the activity is successfully added, false otherwise.

        """

        duration_minutes = self.prompt_duration()
        if self.total_duration_minutes + duration_minutes > 180:

            # Prevents adding activities if total duration exceeds 3 hours
            print(
                "Error: Total duration of activities exceeds 3 hours. Please re-enter the activity and duration."
            )
            return False
        self.total_duration_minutes += duration_minutes

        # Stores activity description and duration in the dictionary
        self.activities[description] = {
            "met_value": met_value,
            "duration_minutes": duration_minutes
        }
        return True


    def select_bicycle(self) -> bool:
        '''
        Allows the user to select and add a bicycling activity.

        Presents a list of predefined bicycling activities with their MET values. The user selects an activity,
        and its details are added to the list of activities after validating the total duration.

        :returns: true if the activity is successfully added, false otherwise.

        '''
        print("Select a Bicycle Activity Description:")

        # Values from reference paper
        activities = {
            1: (6.8, "Bicycling, stationary, general"),
            2: (3.5, "Bicycling, stationary, 25-30 watts, very light to light effort"),
            3: (4.0, "Bicycling, stationary, 50 watts, light effort"),
            4: (5.0, "Bicycling, stationary, 60 watts, light to moderate effort"),
            5: (5.8, "Bicycling, stationary, 70-80 watts"),
            6: (6.0, "Bicycling, stationary, 90-100 watts, moderate to vigorous"),
            7: (6.8, "Bicycling, stationary, 101-125 watts"),
            8: (8.0, "Bicycling, stationary, 126-150 watts"),
            9: (10.3, "Bicycling, stationary, 151-199 watts"),
            10: (10.8, "Bicycling, stationary, 200-229 watts, vigorous"),
            11: (12.5, "Bicycling, stationary, 230-250 watts, very vigorous"),
            12: (13.8, "Bicycling, stationary, 270-305 watts, very vigorous"),
            13: (16.3, "Bicycling, stationary, >325 watts, very vigorous"),
            14: (9.0, "Bicycling, stationary, RPM/Spin bike class"),
            15: (8.8, "Bicycling, interactive virtual cycling, indoor cycle ergometer"),
            16: (8.8, "Bicycling, high intensity interval training"),
        }

        for key, value in activities.items():
            print(f"{key}. {value[1]}")
        choice = int(input("Enter the number corresponding to your choice: "))
        if choice in activities:
            return self.add_activity(activities[choice][1], activities[choice][0])
        else:
            print("Invalid choice.")
            return False


    def select_conditioning_exercise(self) -> bool:
        """
        Allows the user to select and add a conditioning exercise.

        :returns: true if the activity is successfully added, false otherwise.

        """
        print("Select a Conditioning Exercise Description:")

        # Values from reference paper
        activities = {
            1: (7.5, "Calisthenics (e.g., pushups, sit ups, pull-ups, jumping jacks, burpees, battling ropes), vigorous effort"),
            2: (3.8, "Calisthenics (e.g., pushups, sit ups, pull-ups, lunges), moderate effort"),
            3: (2.8, "Calisthenics (e.g., curl ups, abdominal crunches, plank), light effort"),
            4: (3.5, "Calisthenics, light or moderate effort, general (e.g., back exercises), going up & down from floor (Taylor Code 150)"),
            5: (6.0, "Circuit training, body weight exercises"),
            6: (3.5, "Circuit training, light effort"),
            7: (5.0, "Circuit training, moderate effort"),
            8: (7.5, "Circuit training, including kettlebells, some aerobic movement with minimal rest, general, vigorous intensity"),
            9: (5.0, "Elliptical trainer, moderate effort"),
            10: (9.0, "Elliptical trainer, vigorous effort"),
            11: (6.0, "Resistance (weight lifting – free weight, nautilus or universal-type), power lifting or body building, vigorous effort (Taylor Code 210)"),
            12: (5.0, "Resistance (weight) training, squats, deadlift, slow or explosive effort"),
            13: (3.5, "Resistance (weight) training, multiple exercises, 8-15 reps at varied resistance"),
            14: (5.8, "Resistance Training, circuit, reciprocal supersets, peripheral heart action training"),
            15: (3.0, "Body weight resistance exercises (e.g., squat, lunge, push-up, crunch), general"),
            16: (6.5, "Body weight resistance exercises (e.g., squat, lunge, push-up, crunch), high intensity"),
            17: (9.8, "Kettle bell swings"),
            18: (9.0, "Jumping rope, Digi-Jump Machine, 120 jumps/minute"),
            19: (7.3, "Rowing, stationary ergometer, general, vigorous effort"),
            20: (5.0, "Rowing, stationary ergometer, general, <100 watts, moderate effort"),
            21: (7.5, "Rowing, stationary, 100 to 149 watts, vigorous effort"),
            22: (11.0, "Rowing, stationary, 150 to 199 watts, vigorous effort"),
            23: (14.0, "Rowing, stationary, ≥ 200 watts, very vigorous effort"),
            24: (2.3, "Stretching, mild"),
            25: (1.8, "Pilates, traditional, mat"),
            26: (2.8, "Pilates, general"),
            27: (2.3, "Yoga, Hatha"),
            28: (8.0, "Yoga, high intensity"),
            29: (2.3, "Yoga, General"),
            30: (6.5, "Zumba, group class")
        }

        for key, value in activities.items():
            print(f"{key}. {value[1]}")
        choice = int(input("Enter the number corresponding to your choice: "))
        if choice in activities:
            return self.add_activity(activities[choice][1], activities[choice][0])
        else:
            print("Invalid choice.")
            return False


    def select_running(self) -> bool:
        '''
        Allows the user to select and add a running activity.

        Returns:
        bool: True if the activity is successfully added, False otherwise.
        '''

        print("Select a Running Activity Description:")

        # Values from reference paper
        activities = {
            1: (6.0, "Jog/walk combination (jogging component of less than 10 minutes) (Taylor Code 180)"),
            2: (7.5, "Jogging, general, self-selected pace"),
            3: (4.8, "Jogging, in place"),
            4: (3.3, "Jogging 2.6 to 3.7 mph"),
            5: (4.5, "Jogging on a mini-tramp"),
            6: (6.5, "Running, 4 to 4.2 mph (13 min/mile)"),
            7: (7.8, "Running 4.3 to 4.8 mph"),
            8: (8.5, "Running, 5.0 to 5.2 mph (12 min/mile)"),
            9: (9.0, "Running, 5.5 -5.8 mph"),
            10: (9.3, "Running, 6-6.3 mph (10 min/mile)"),
            11: (10.5, "Running, 6.7 mph (9 min/mile)"),
            12: (11.0, "Running, 7 mph (8.5 min/mile)"),
            13: (11.8, "Running, 7.5 mph (8 min/mile)"),
            14: (12.0, "Running, 8 mph (7.5 min/mile)"),
            15: (12.5, "Running, 8.6 mph (7 min/mile)"),
            16: (13.0, "Running, 9 mph (6.5 min/mile)"),
            17: (14.8, "Running, 9.3 to 9.6 mph"),
            18: (14.8, "Running, 10 mph (6 min/mile)"),
            19: (16.8, "Running, 11 mph (5.5 min/mile)"),
            20: (18.5, "Running, 12 mph (5.0 min/mile)"),
            21: (19.8, "Running, 13 mph (4.6 min/mile)"),
            22: (23.0, "Running, 14 mph (4.3 min/mile)")
        }
        for key, value in activities.items():
            print(f"{key}. {value[1]}")
        choice = int(input("Enter the number corresponding to your choice: "))
        if choice in activities:
            return self.add_activity(activities[choice][1], activities[choice][0])
        else:
            print("Invalid choice.")
            return False

    def get_activity_summary(self) -> pd.DataFrame:
        '''
        Returns the activity summary as a pandas DataFrame.

        Returns:
            pd.DataFrame: A DataFrame containing activity details.

        '''
        if not self.activities:
            print("No activities added.")
            return None

        # Convert activities to a DataFrame
        data = [
            {
                "Activity": description,
                "MET Value": details["met_value"],
                "Duration (hours)": details["duration_minutes"] // 60,
                "Duration (minutes)": details["duration_minutes"] % 60
            }
            for description, details in self.activities.items()
        ]
        return pd.DataFrame(data)

    def start(self):
        '''
        Starts the activity selection process. Allows the user to add multiple activities, ensuring the total duration does not exceed 3 hours.

            >>> activity_manager = Activity()
            >>> activity_manager.start()
            Select an Activity Type:
            1. Bicycle
            2. Conditioning Exercise
            3. Running
            (User selects activities and durations interactively)
        '''
        print(
            "Please select the type of activities performed and enter the duration."
        )
        print("Note: Overtraining is not healthy. Duration of all activities should be less than 3 hours.")

        # Selection of the main "TYPE OF ACTIVITY"
        while True:
            print("\nSelect an Activity Type:")
            print("1. Bicycle")
            print("2. Conditioning Exercise")
            print("3. Running")
            activity_type = int(input("Enter the number corresponding to your choice: "))

            if activity_type == 1:
                if not self.select_bicycle():
                    continue
            elif activity_type == 2:
                if not self.select_conditioning_exercise():
                    continue
            elif activity_type == 3:
                if not self.select_running():
                    continue
            else:
                print("Invalid activity type.")
                continue

            print("Activity added successfully!")
            print(f"Total duration so far: {self.total_duration_minutes // 60} hours and {self.total_duration_minutes % 60} minutes.")
            more = input("Do you want to add more activities? (Y to continue, N to exit): ").strip().upper()
            if more == 'N':
                break

        print("\n Summary of Activities:")
        activity_summary = self.get_activity_summary()
        if activity_summary is not None:
            print(activity_summary.to_string(index=False))
        print(f"Total duration of all activities: {self.total_duration_minutes // 60} hours and {self.total_duration_minutes % 60} minutes.")
