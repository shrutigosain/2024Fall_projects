# 2024Fall_projects

# Title
Predictive Model for Weight Loss Using Monte Carlo Simulations

# Team Members
Ishan Joshi (ishan2505), Shruti Gosain (shrutigosain), Nishtha Joshi (nj10-15)

## Objective:
Weight loss is a common goal for many individuals, yet achieving it effectively remains a challenge due to individual variability in responses to sleep and exercise. Traditional fitness plans often assume a one-routine-fits-all approach, leading to inconsistent results. This project aims to design a Monte Carlo simulation model that incorporates key factors like workout type, intensity, duration, metabolic rate, sleep duration and caloric intake to predict weight loss outcomes. 

## Hypothese and the Varibles Used:
**Hypotheses 1:** Predicted weight loss over a fixed duration increases as the number of workout days in a week and additional calories burned (daily activity level) increase.

**Hypotheses 2:** Consistent calorie intake, adequate sleep duration and regular workout days experience faster and more predictable weight loss, while greater variability in these factors demonstrate slower and less consistent weight loss trajectories due to fluctuations in energy balance and resting metabolic rate (RMR).

**Hypotheses 3:** Individuals with consistent calorie intake, adequate sleep duration (≥8 hours), and regular workout days experience faster and more predictable weight loss, while those with greater variability in these factors demonstrate slower and less consistent weight loss trajectories.

## Fixed Variables (Input from the user):
1. Initial Weight (lbs): Initial body weight of an individual
2. Age, Gender, Height: These variables influence the basal metabolic rate (RMR).
3. Workout Duration (hours): Number of hours a person does the workout in a day.
4. Activity Type and Activity Intensity (MET value): These are based on a numerical number called MET value which is different for each activity type and the intensity.

## Random Variables:
1. Number of workout days in a week (days): Total number of workout days in a week.
2. Additional Calories Burned (kcal/day): The number of additional calories burned per day from daily non-exercise activities.
3. Calorie Intake (kcal): The number of calories that a person is consuming everyday.
4. Sleep Duration (hours): The number of hours the person is sleeping everyday.

## Other Derived Variables:
1. Resting Metabolic Rate (RMR): Calculated based on Age, Gender, Height, Initial Weight and sleep adjustment factor (in 2nd hypothese)
2. Workout calories (kcal): Calculated based on MET value, workout duration and initial weight.
3. Total Calories Burned (kcal): Calculated based on the sum of Workout Calories, Additional Calories Burned and RMR.
4. Calorie Deficit(kcal): Calculated based on Total Calories Burned(kcal) and Calorie intake(kcal)
5. Predicted Weight Loss(lbs): Calculated by converting the calories into weight factor.

## Formulae used:
1. Resting Metabolic Rate (RMR): The Mifflin-St Jeor equation is widely recognized for estimating RMR:
   Men: RMR (kcal/day) = 10 × 0.453592 x weight (lbs) + 6.25 x 2.54 × height (inch) - 5 × age (years) + 5
   Women: RMR (kcal/day) = 10 × 0.453592 x weight (lbs) + 6.25 × 2.54 × height (inch) - 5 × age (years) - 161

Reference:
a. https://en.wikipedia.org/wiki/Basal_metabolic_rate - For getting the formula for RMR/BMR using the The Mifflin St Jeor equation from this link.
b. https://www.bannerhealth.com/staying-well/health-and-wellness/fitness-nutrition/ideal-weight - For setting the range for age and height.
c. https://www.researchgate.net/publication/6498022_Impact_of_Sleep_and_Sleep_Loss_on_Neuroendocrine_and_Metabolic_Function - Reduced RMR by approximately 5% for every hour below the recommended 7-8 hours of sleep.

2. Workout Calories (kcal): This is calculated using MET values(varying according to activity type and intensity), initial weight and workout duration (fixed)

3. Workout Calories (kcal): MET value × initial weight (lbs) × workout duration (hours)
Reference: https://pacompendium.com/adult-compendium/ - For getting the MET values based on activity type and intensity

4. Total Calories Burned (kcal): Workout Calories + RMR + Additional Calories Burned

5. Calories Deficit (kcal) = Total Calories Burned - Calorie Intake (kcal)

## Conclusion

**Hypotheses 1**
The Monte Carlo Simulation graph shows the effective realtionship between the additional calories burned from non-exercise activites, number of workout days and predicted weight loss over a fixed duration. The graph shows a decreasing trend in weight reflecting the consistent weight loss over time.

The simulation supports our Hypotheses as it confirms that as the number of workout days in a week and additional calories burned increases, there is greater weight loss. The wide range of trajectories depicts the variability due to different RMR, routine and initial conditions (like initial weight, calorie intake etc.). Despite the varibality, the downward pattern confirms that high levels of workout days and additional calories burned contribute significantly to higher weight loss outcomes.

**Monte Carlo Simulation Graph for Hypotheses 1**
<img width="1121" alt="Hypotheses 1" src="https://github.com/user-attachments/assets/04c2f419-1ab7-4e1f-9937-14bb0cf6f546">

**Hypotheses 2**


**Hypotheses 3**

