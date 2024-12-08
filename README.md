# 2024Fall_projects

# Title
Predictive Model for Weight Loss Using Monte Carlo Simulations

# Team Members
Ishan Joshi (ishan2505), Shruti Gosain (shrutigosain), Nishtha Joshi (nj10-15)

## Objective:
Weight loss is a common goal for many individuals, yet achieving it effectively remains a challenge due to individual variability in responses to diet and exercise. Traditional fitness plans often assume a one-size-fits-all approach, leading to inconsistent results. This project aims to design a Monte Carlo simulation model that incorporates key factors like workout type, intensity, duration, metabolic rate, and caloric intake to predict weight loss outcomes and identify optimal workout strategies. 

## Hypothese and the Varibles Used:
## Hypotheses 1: Predicted weight loss over a fixed duration increases as the number of workout days in a week and daily activity level increase. However, individuals with higher initial weight experience greater variability in weight loss due to differences in calorie deficits influenced by resting metabolic rate (RMR) and workout intensity.

## Fixed Variables (Input from the user):
1. Initial Weight (lbs): Initial body weight of an individual
2. Age, Gender, Height: These variables influence the basal metabolic rate (RMR).
3. Workout Duration (hours): Number of hours a person does the workout in a day.
4. Calorie Intake (kcal): The number of calories that a person is consuming.
5. Activity Type and Activity Intensity: These are based on a numerical number called MET value which is different for each activity type and the intensity.

## Random Variables:
1. Number of workout days in a week (days): Total number of workout days in a week.
2. Daily Activity Level (kcal/day): The number of calories a person burn per day from daily activities like walking etc.

## Other Derived Variables:
1. Resting Metabolic Rate (RMR): Calculated based on Age, Gender, Height and Initial Weight.
2. Workout calories (kcal): Calculated based on workout intensity and its type (MET value).
3. Total Calories Burned (kcal): Calculated based on the sum of Workout calories, Daily Activity Level and RMR.
4. Calorie Deficit(kcal): Calculated based on Total Calories Burned(kcal) and Calorie intake(kcal)
5. Predicted Weight Loss(lbs): Calculated by converting the calories into weight factor.

## Formulae used:
Resting Metabolic Rate (RMR): The Mifflin-St Jeor equation is widely recognized for estimating RMR:
  Men: RMR (kcal/day) = 10 × weight (kg) + 6.25 × height (cm) - 5 × age (years) + 5
  Women: RMR (kcal/day) = 10 × weight (kg) + 6.25 × height (cm) - 5 × age (years) - 161

Reference:
1. https://en.wikipedia.org/wiki/Basal_metabolic_rate - For getting the formula for RMR/BMR using the The Mifflin St Jeor equation from this link.
2. https://www.bannerhealth.com/staying-well/health-and-wellness/fitness-nutrition/ideal-weight
- For setting the range for age and height.

Workout Calories (kcal): This is calculated using MET values(varying according to activity type and intensity), initial weight and workout duration (fixed)

Workout Calories (kcal): MET value × initial weight (lbs) × workout duration (hours)
Reference: https://pacompendium.com/adult-compendium/ - For getting the MET values based on activity type and intensity

Total Calories Burned (kcal): Workout Calories + Daily Activity Level + RMR

Calories Deficit (kcal) = Total Calories Burned - Calorie Intake (kcal)

