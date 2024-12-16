# 2024Fall_projects

# Title
Predictive Model for Weight Loss Using Monte Carlo Simulations

# Team Members
Ishan Joshi (ishan2505), Shruti Gosain (shrutigosain), Nishtha Joshi (nj10-15)

## Objective:
Weight loss is a common goal for many individuals, yet achieving it effectively remains a challenge due to individual variability in responses to sleep and exercise. Traditional fitness plans often assume a one-routine-fits-all approach, leading to inconsistent results. This project aims to design a Monte Carlo simulation model that incorporates key factors like workout type, intensity, duration, metabolic rate, sleep duration and caloric intake to predict weight loss outcomes. 

## 3 Stages of Monte Carlo Simulation:

**Stage 1 - Design**

Variables that affect the system and their distribution:​

Input Variables:​
      - User Attributes: age, height, weight, calorie intake, gender.​
      - Activity MET Values and Duration​
      - Additional Factors: workout days, additional calories burned from non-workout activities, sleep duration.​

Defined Distributions for Random Variables:​
      - Workout Days per Week: Uniform distribution between 2 and 7.​
      - Additional Calories Burned: Uniform distribution between 200 and 700 kcal.​
      - Calorie Intake Variation: Uniform random variation of ±500 kcal around the user's base calorie intake.​
      - Sleep Duration Variation: Uniform random variation of ±2 hours around the user’s average sleep duration.​

The relationship between these inputs and the output (weight change):​
      - Resting Metabolic Rate (RMR): Calculated using the weight, height, age, gender.​
      - Calories Burned from Activities: Using MET values and activity durations.​
      - Weight Change: Derived from calorie deficits or surpluses.​

**Stage 2 - Validation**

We validated one scenario with user inputs to check the trajectory of the graph. ​

Summary of Activities:
Activity                                                                                  MET Value  Duration (hours)  Duration (minutes)
Resistance (weight) training, multiple exercises, 8-15 reps at varied resistance          3.5                 2                   0
Jog/walk combination (jogging component of less than 10 minutes) (Taylor Code 180)        6.0                 0                   5
Total duration of all activities: 2 hours and 5 minutes.

User Details:
Age (years)  Height (inch)  Weight (lbs) Calorie Intake Gender
26             77           190          3000            male

​<img width="1038" alt="image" src="https://github.com/user-attachments/assets/dd426c71-f274-4890-8a4c-67e7c0059a47" />
For each simulation run, a new set of random values is generated for the random variables.​
The random sampling is repeated for the number of simulations, with each simulation spanning weeks (7 days).​

**Stage 3 - Experiment and Predictions**​

- Ran the simulation for many iterations.​
- Introduced more random variables to experiment the simulation.​
- Made variations to the fixed variables from the initial hypothesis.​
- Compared the initial hypothesis with the newer ones and made conclusions​.

<img width="1053" alt="image" src="https://github.com/user-attachments/assets/9c06e959-7ead-4f7f-9bb3-d398dcd65e12" />

## Assumptions:
1) Additional calories is the non-exercise calories that an individual might burn apart from working out and RMR​
2) We have assumed that all the calculations we have used referenced from the paper are correct ​
3) We have assumed that total calories burned is only the sum of RMR + Workout Calories + Additional Calories ​
4) We have assumed that weight loss can be derived using Calorie Deficit which is the difference of Total Calories burned and Calorie Intake


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

**Monte Carlo Simulation Graph for Hypotheses 3**
<img width="1048" alt="Hypotheses 3" src="https://github.com/user-attachments/assets/4c16582b-ff87-415c-bc3a-3008af13a1cd">
