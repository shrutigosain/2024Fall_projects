# 2024Fall_projects

# Title
Predictive Model for Weight Loss Using Monte Carlo Simulations

# Team Members
Ishan Joshi (ishan2505), Shruti Gosain (shrutigosain), Nishtha Joshi (nj10-15)

## Objective:
Weight loss is a common goal for many individuals, yet achieving it effectively remains a challenge due to individual variability in responses to sleep and exercise. Traditional fitness plans often assume a one-routine-fits-all approach, leading to inconsistent results. This project aims to design a Monte Carlo simulation model that incorporates key factors like workout type, intensity, duration, metabolic rate, sleep duration and caloric intake to predict weight loss outcomes. 

## Hypothese and the Varibles Used:
**Hypotheses 1:** Predicted weight loss over a fixed duration increases as the number of workout days in a week and additional calories burned (daily activity level) increase.

**Hypotheses 2:** Predicted weight loss over a fixed duration is influenced by calorie intake, sleep duration, number of workout days per week, and additional calories burned through daily activity. Increased variability in these factors leads to wider range in weight loss trajectories due to fluctuations in energy balance and resting metabolic rate (RMR).

**Hypotheses 3:** Predicted weight loss over a fixed duration differs among individuals with identical user details but varying initial weight offsets (+40 lbs, 0 lbs, and -40 lbs). Individuals with a positive weight offset (+40 lbs) are expected to have a flatter slope of weight loss compared to those with a negative weight offset (-40 lbs), using the individual with 0 lbs offset as the reference point.

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

      a. https://en.wikipedia.org/wiki/Basal_metabolic_rate - Took the formula for RMR/BMR using the The Mifflin St Jeor equation from this link.

      b. https://www.bannerhealth.com/staying-well/health-and-wellness/fitness-nutrition/ideal-weight - Took the range for setting the age and height inputs

      c. https://www.researchgate.net/publication/6498022_Impact_of_Sleep_and_Sleep_Loss_on_Neuroendocrine_and_Metabolic_Function - Took the formula for adjusted RMR when sleep factor is introduced. There is a reduced RMR by approximately 5% for every hour below the recommended 7-8 hours of sleep.

2. Workout Calories (kcal): This is calculated using MET values(varying according to activity type and intensity), initial weight and workout duration (fixed)

   Workout Calories (kcal): MET value × initial weight (lbs) × workout duration (hours)

   Reference: https://pacompendium.com/adult-compendium/ - For getting the MET values based on activity type and intensity

3. Total Calories Burned (kcal): Workout Calories + RMR + Additional Calories Burned

4. Calories Deficit (kcal): Total Calories Burned - Calorie Intake (kcal)

## Conclusion

**Hypotheses 1:**
The Monte Carlo Simulation graph shows the effective realtionship between the additional calories burnt from non-exercise activites, number of workout days and predicted weight loss over a fixed duration.

The simulation partially supports our hypotheses as it confirms that weight loss increases with an increase in the number of workout days and additional calories burnt, considering that the calorie intake is ideal for the given weight. The wide range of trajectories depict the variability due to different RMR, routine and initial conditions (like initial weight, calorie intake etc.). Calorie intake plays a very significant role in determining the weight loss of a person. Keeping it constant does not make sense in an ideal scenario.

**Monte Carlo Simulation Graph for Hypotheses 1**
<img width="1121" alt="Hypotheses 1" src="https://github.com/user-attachments/assets/04c2f419-1ab7-4e1f-9937-14bb0cf6f546">

**Hypotheses 2:**
The Monte Carlo simulation graph for Hypothesis 2 reveals a stronger co-relation between the random variables. 

Greater variability in the factors like workout days, sleep duration or calorie intake shows a wider spread of weight loss trajectories. These randomization cause slower and less predictable progress, as seen in the dispersion of lines in the graph. This variability also aligns with the hypothesis that inconsistency in key factors disrupts energy balance and impacts metabolic efficiency, leading to a less reliable weight loss outcome.

Overall, the simulation supports our hypothesis while variability introduces uncertainty and slower progress.

**Monte Carlo Simulation Graph for Hypotheses 2**
<img width="1074" alt="Hypotheses 2" src="https://github.com/user-attachments/assets/111378a4-d0f3-481f-8982-0e4a569ac68b">

**Hypotheses 3:**
The Monte Carlo Simulation supports our hypotheses and the graph clearly shows that an individual's starting weight significantly impacts the predictability of weight loss. People with higher initial weights tend to lose weight faster and more consistently because of higher energy expenditure and a greater resting metabolic rate (RMR). In contrast, individuals with lower initial weights experience slower and more gradual weight loss, with greater variability in their outcomes.

Overall, the results confirm that while factors such as consistent calorie intake, sleep, and workout days play a role but initial weight is the primary determinant of the predictability of weight loss. The graph provides clear evidence that heavier individuals experience a more pronounced and predictable decreasing trend in weight loss over time.

**Monte Carlo Simulation Graph for Hypotheses 3**
<img width="1048" alt="Hypotheses 3" src="https://github.com/user-attachments/assets/4c16582b-ff87-415c-bc3a-3008af13a1cd">
