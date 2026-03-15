# Naive-Bayers-Prediction-model-

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Matplotlib](https://img.shields.io/badge/Render-Matplotlib-orange)

# Student Absence Predictor

This project demonstrates a Naive-Bayers prediction model on student absence based on the underlying factors:

*  Weather : Rainy, Stormy, Sunny
*  Health : Healthy, Injured, Sick
*  Academic Load : Assignment Due, Normal Day, Major Exam
*  Motivation : Unmotivated, Burned Out, Motivated
*  Location : Walking Distance, Commute
  
> **Note:** The accuracy of the model heavily relies on the amount of dataset it is given. Fortunately, the factors present a deterministic combination
by multiplying the sub-factors together. So in total there should be 162 combinations in a simulated data set. Which totally makes surveys obsolete, but for formalities sake, we have included one.
> > **Additional Note:** For the simulated result of the 162 combinations, we made a mini script point system that gives scores for each sub-factor that determines whether the student is present, or absent. For example sunny gains 1 point, rainy -1 point, and stormy -2 points. Basically apply this point system to all the sub-factors then add them all up, if the total score is 0 or higher, the student is marked as present, and if it is below 0, then the student is marked absent. But of course this is another concept and is irrelevant to the project.


## Clone the Files First
```cmd
git clone https://github.com/Aucco1/Naive-Bayers-Prediction-model-.git
```

## Install dependencies

### 1. Pandas
```cmd
pip install panda
```
### 2. Sklearn
```cmd
pip install scikit-learn
```
### 3. Streamlit
```cmd
pip install streamlit
```


## How to run instructions:

### 1. Run this in terminal
```cmd
python -m streamlit run naivebaayesaccuraccy.py
```

## Survey Phase.


### DATA TABLE

<figure>
  <img width="1214" height="688" alt="Image" src="https://github.com/user-attachments/assets/0ea45610-0c1b-4f8d-9ea4-b652452250a6" />
  <figcaption align="center"><b>Figure 1:</b> The data is first laid out on a table format system. </figcaption>
</figure>

### DATA SET TABLE


<figure>
  <img width="1086" height="465" alt="Image" src="https://github.com/user-attachments/assets/0f637e1a-4afe-4b63-9f65-cf6bf1fa06a6" />
  <figcaption align="center"><b>Figure 2:</b> The dataset divides the factors and counts how many times the sub-factors appeared in each outcomes.</figcaption>
</figure>

### HISTOGRAM


<figure>
  <img width="796" height="773" alt="Image" src="https://github.com/user-attachments/assets/5d0b4b79-cb1b-42a4-b993-ba79c3a2c858" />
  <figcaption align="center"><b>Figure 3:</b> A histrogram of the survey to serve as data representation. </figcaption>
</figure>


### HOW THE MODEL WORKS.

## Looking at the conversion.
  There are two csv files used.


### The survey dataset
```bash
    NoneCompleteCombination.csv
 ```
### The simulated dataset 
```bash
    CompleteCombinationFactors.csv
 ```

The amount of data used to train the model only proves that the more data there is to learn from, the more it predicts accurately.

## Phase 1:
 The Model looks at the spreadsheet and counts.

First it calculates the Base Probability:
	Out of the amount of rows, how many total days
	was the student Present vs Absent?
Second it builds a cheat sheet of probabilities:
	The frequency that the student was present in the 	sub-factors,
	The frequency that the student was absent in the 
	sub-factors.
Basically, calculating individual frequencies for every single option and saves them to memory. And that is the entire learning process, just memorizing historical odds.

## Phase 2:
 How the model predicts.

1.
	Revisits the cheat sheet it made and grabs the odds of specific things happening together on the days the student was known to be present and multiplies them together

(Overall % Present) × (% of Present days that were Stormy) × (% of Present days that were Healthy) × (% of Present days with a Major Exam) ... = Final Present Score

2. 	
	Same math as the first step, but for the absent score

3.
	Compares the two final numbers, determines which one is bigger then output a final answer.


## Snapshot of the program used as an interactive prediction machine.

<img width="942" height="853" alt="Image" src="https://github.com/user-attachments/assets/06845220-6621-44e5-9a24-cae56b847432" />
<img width="914" height="623" alt="Image" src="https://github.com/user-attachments/assets/b4a12ff1-ed41-47a5-bc42-507641e14afa" />
<img width="922" height="642" alt="Image" src="https://github.com/user-attachments/assets/906cd003-be7f-427a-970c-beb1ff002782" />


## Snapshot of the sidebar which contains descriptions of model Training accuracy

<img width="358" height="309" alt="Image" src="https://github.com/user-attachments/assets/bcaf6a29-df5f-4000-b137-c565e51bc9ed" />

The most accurate model by using the 162 combinations.

<img width="369" height="306" alt="Image" src="https://github.com/user-attachments/assets/5df85948-be7f-49cb-83af-ea958d8a67d0" />

The inferior version of the model by using the survey (smaller dataset).

# Conclusion
  So in conclusion, its more or less about writing code, but more on providing good data. Its not bad ai, but just a confused machine, much like how a 30 dataset survey provided a 60% accuracy (strict) compared to the full combination 162 possibilities which propelled the accuracy to 90%.

## Observation

  Naive assumption only combines factors, not understand the relation of both, it deals with odds in an independent manner and calculates blindly. Not really a great tool for complex human psychology. However it does a good job in specific tasks that involve probabilistic contexts that disregards contexts.

# Why our model is much more accurate than other models presented.

  We realized that asking people hypothetical questions resulted in really messy, inaccurate data. So instead, we used a heuristic approach. We designed a logical point system for the 5 factors (Weather, Health, etc.) and generated all the possible combinations. Our Naive Bayes model learned our logical system, which is why the accuracy is so high.

  But yeah there is a flaw, our system is accurate because it plays by our rules (the point system), it assumes every human is a walking rational calculator, perfectly logical beings. Which isnt true because humand are complex beings that have contradicting opinions.

  And because of that contradicting nature and a sparse data problem(small dataset and small respondents), we're practically creating a very inaccurate model, it would be more viable if we had thousands of people to work with in order to see more patterns, but that is exactly what we were lacking which is why we had to be creative and made a rule based data-set to properly showcase what an accurate naive bayes model would look like.

 

  



## Group 8: Pacheco, Lucero, Peralta


## License

This project is open-source and available under the [MIT License](LICENSE).
