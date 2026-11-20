# Health in Nature and People in London Boroughs

How does a healthy natural environment (through the amount of green space) relate to or effect human health in London Boroughs. Is it a primary factor, a minor contributing factor or just a correlating factor

- **Student ID:** 24000117484
- **Repository:** M6006-ds2026-24000117484

This project lives in `project/`. The repository is the whole course folder:
`requirements.txt` and `.gitignore` are at the repository root, and the
week folders hold the lab notebooks.

## Research question:

$$\boxed{\text{What Effect does Green Space have on the Health of London Borough Residents, How strong is that effect and are there any other factors involved}}$$

## The real-world problem and who it affects

$$\boxed{\text{Inequality is prevelant in London, not only in economic terms but also environmental inequality (e.g. access to green space) and health inequality (e.g. health outcomes and access to good healthcare). These inequalities are often present in tandem with each other, meaning that those who exist or live in an unequal environment will face barriers at multiple levels meaning the most vulnerable groups and demographics will have compounding inequality}}$$

## Data

Where the data comes from, how to get it, and what licence it is under.
Put data files in `data/`: that folder is not committed to GitHub, so explain
here how someone else can get the data

## Cleaning and preprocessing

As the data is sourced from the Office for National Statistics (ONS), the data requires minial preprocessing. Three different datasets were sourced and merged, with columns irrelevant to the research question being dropped and Null values being checked for. A function for eliminating whitespace and capitalisation was run on the column names to avoid uneccesary complications later in the statistical analsysis. 

## Descriptive statistics and visualisation

A pairplot was generated showing the relation between the two chosen independent variables (wealth and green space) and the dependent variable (health). A regression line was fitted to indicate relationships between the independent and dependent variables and a comparison was made between including and excluding the City of London in the dataset (as it is much smaller, more built and more wealthy when compared against other boroughs, due to its nature as the financial district and the unique administrative policies). 

A regression analysis was run (with the same variables), excluding the city of London, to identify statistical significance of the relationships and to identify how much variance in the dependent variable the independent variables can explain.

## Analysis plan

For the predictive analysis, a regression model was identified as the strongest option. This is due to the nature of the data and the purpose for the model implementation: To find a) whether green space (as an indicator for environmental health) has an effect on human health; and b) to attempt to quantify the effect observed (if the model has inaccurate predictions it indicates a non causal relation).

The model will be tested using the 'leave one out' method due to the small number of data points (32 including the City of London). The model will predict the health of each borough from the data on the other boroughs.

Alternative models were considered but found incompatible with either the data or the research question. The primary alternative modelling method considered was a Classifier, however, the data is continious and a Classifier requires discrete data to *classify* the data as. While the data could be transformed to be discrete (e.g. a borough is healthy or unhealthy) it would be reductive due to what the data actually represents. The health scores and wealth scores are calculated relative to the health or wealth of other areas in the sample (the data is calculated across all of England but was reduced to just Greater London boroughs) and the most deprived locations are given a score of 1. Hypothetically, if England had very little deprivation, a small difference from the least deprived area could result in a score of 1 so a binary 'healthy' or 'unhealthy' classification cannot reliably be ascertained.

## How to run this

From the repository root: create and activate a virtual environment, then
`pip install -r requirements.txt`, then open the notebook in `project/`.

## Use of AI (required)

The provided 'Tutor' AI was the only AI model used in the creation of this piece of work. Modifications to the instructions for the 'Tutor' Model have been made, the only modification was unrelated to the restrictions of the model and no edits to existing rules were made. The modifications consist only of an instruction to make the model say 'YABBA-DABBA-DOO' after each statements.

AI was used for basic debugging and syntax guidance.

- **Tool:** Tutor agent (VS Code)
- **Model:** the maker, family and version shown in the chat's model picker
- **Used for:** understanding how imputation changes variance; checking my
  interpretation of odds ratios; fixing a package that would not install in my
  `.venv`
- **Not used for:** writing the analysis code or the text of this README
