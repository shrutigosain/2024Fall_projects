# 2024Fall_projects

## HYPOTHESIS:
1. How long will an individual take to reduce current weight to the desired weight
2. How will the different types of workouts (e.g., high-intensity interval training) affect the weight-loss goals when tailored to individual variability
3. Maybe something related to diet…

## Objective:
Weight loss is a common goal for many individuals, yet achieving it effectively remains a challenge due to individual variability in responses to diet and exercise. Traditional fitness plans often assume a one-size-fits-all approach, leading to inconsistent results. This project aims to design a Monte Carlo simulation model that incorporates key factors like workout type, intensity, duration, metabolic rate, and caloric intake to predict weight loss outcomes and identify optimal workout strategies. 

In this project, the variables can be categorized into inputs, outputs, and control parameters, as follows:

# 1. Input Variables
These variables represent the factors that influence weight loss. They are fed into the simulation to model the system.
Personal and Biological Factors
* Initial Weight (kg): The starting weight of the individual
* Resting Metabolic Rate (RMR, kcal/day): The energy expenditure at rest. (optional)
* Age (years): Influences metabolic rate and caloric burn efficiency.
* Gender: Impacts baseline metabolic rate and fat distribution.

## Exercise Variables 
* Workout Type: The category of exercise (e.g., cardio, strength training, HIIT).
* Workout Duration (minutes): Time spent in a workout session.
* Workout Intensity: Levels of effort (e.g., low, medium, high).
* Total Calories Burnt : Varies based on type and intensity of exercise.

## Other Variables
* Caloric Intake (kcal/day): Total daily calories consumed. (diet related)
* Variation in Workout Days (days/week): Random fluctuations in the number of active workout days. (adherence related)

## Random Variables (Variability)
* Daily Activity Level (kcal/day): Additional calories burned from daily activities outside planned workouts.

# 2. Output Variables
These variables represent the simulation's results and allow the evaluation of hypotheses.

* Predicted Weight Loss (kg): Change in weight over a defined time period.
* Body Fat Percentage (%): Change in body composition based on caloric deficit.
* Caloric Deficit

# 3. Control Parameters
These variables are set constants or fixed values to manage the simulation environment.

* Simulation Duration (weeks): Length of time modeled (in months).
* Number of Iterations: Number of Monte Carlo simulations 
* Conversion Factor: Caloric deficit required for 1 kg of weight loss 

## Relationships Between Variables
The simulation will model relationships like:
1. Calories Burned = RMR + Workout Burn + Daily Activity Burn
2. Caloric Deficit = Calories Burned - Caloric Intake
3. Weight Loss = Caloric Deficit ÷ 7,700 (kcal/kg)

