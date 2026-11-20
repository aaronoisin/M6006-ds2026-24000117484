# Health in Nature and People in London Boroughs

How does a healthy natural environment (through the amount of green space) relate to or effect human health in London Boroughs. Is it a primary factor, a minor contributing factor or just a correlating factor

- **Student ID:** 24000117484
- **Repository:** M6006-ds2026-24000117484


## Research question:

What Effect does Green Space have on the Health of London Borough Residents, How strong is that effect and are there any other factors involved

## The real-world problem and who it affects

Inequality is prevelant in London, not only in economic terms but also environmental inequality (e.g. access to green space) and health inequality (e.g. health outcomes and access to good healthcare). These inequalities are often present in tandem with each other, meaning that those who exist or live in an unequal environment will face barriers at multiple levels meaning the most vulnerable groups and demographics will have compounding inequality.

The residents of the boroughs are not the only stakeholders, councils, green space management and health organisations are also stakeholders as they all have interest and influence over green spaces or health outcomes (or both)

## Data

**Green Cover Data:**

The data for the green cover in London Boroughs was sourced from the Greater London AUthority and is available [here (green_cover_borough file)](https://data.london.gov.uk/dataset/london-green-and-blue-cover-emqzm). The data is published under the Open Government Licence v3.0 (OGL v3) and is availble for commercial and non commercial use. 

$\boxed{\begin{gathered} 
\text{Green and blue cover data:}\\ \text{Greater London Authority London Green and Blue Cover (2019).}\\ 
\text{Contains OS data © Crown copyright and database rights 2019.}\\ 
\text{Contains Verisk Analytics GeoInformation Group UKMap data.}\\ 
\text{Licensed under the Open Government Licence v3.0.}
\end{gathered}}$

**Borough Demographics Data**

The data for the depirvation demographics was sourced from the Office for National Statistics (ONS) and is available [here (as File 10)](https://www.gov.uk/government/statistics/english-indices-of-deprivation-2025). The data is published under the Open Government License V3.0.


## Cleaning and preprocessing

As the data is sourced from the Office for National Statistics (ONS), the data requires minial preprocessing. Three different datasets were sourced and merged, with columns irrelevant to the research question being dropped and Null values being checked for. A function for eliminating whitespace and capitalisation was run on the column names to avoid uneccesary complications later in the statistical analsysis. 

.describe() and .corr() were used to describe the data (.describe() is a literal quantitative description, using means and counts and .corr() was used to identify the strength of associations). This analysis showed a high correlation between wealth and health and a moderate correlation between green space and health, other variable relationships had weaker correlations.

I also found that by removing the borough of the City of London, the strength of the correlation between green space and health and also green space and wealth. This is likely due to the smaller size of the area and it's large buildings as it's role as a financial district.

### Correlation values:
 With CoL:
  - Green space & Health: 0.477538
  - Blue space & Health: -0.255465
  - Wealth & Health:0.703287

Without CoL:
  - Green space & Health: 0.643354
  - Blue space & Health: -0.297350
  - Wealth & Health: 0.733931

Blue space has a negative correlation with health, however it is not a strong correlation so the blue space variable will be considered to have a negligible effect on health.	

## Descriptive statistics and visualisation

A pairplot was generated showing the relation between the two chosen independent variables (wealth and green space) and the dependent variable (health). A regression line was fitted to indicate relationships between the independent and dependent variables and a comparison was made between including and excluding the City of London in the dataset (as it is much smaller, more built and more wealthy when compared against other boroughs, due to its nature as the financial district and the unique administrative policies). 

A regression analysis was run (with the same variables), excluding the city of London, to identify statistical significance of the relationships and to identify how much variance in the dependent variable the independent variables can explain.

A fitted regression model was used on the data (excluding the City of London) using green spaces as a dependent variable and wealth and health as the independent variables. The $R^2$ value was 0.65, 65% of the variance in health could be explained by variations in green spaces or wealth. The P-values were both under 0.05, showing statistical significance in the relationship when the other variable is held constant.

Green space (% of borough):  $p\leq 0.0059235244601048564$

Wealth:  $p\leq 0.00016753929587310002$

## Analysis plan

For the predictive analysis, a regression model was identified as the strongest option. This is due to the nature of the data and the purpose for the model implementation: To find a) whether green space (as an indicator for environmental health) has an effect on human health; and b) to attempt to quantify the strength and direction of the association observed. 


The model will be tested using the 'leave one out' method due to the small number of data points (32 including the City of London). The model will predict the health of each borough from the data on the other boroughs.

Alternative models were considered but found incompatible with either the data or the research question. The primary alternative modelling method considered was a Classifier, however, the data is continious and a Classifier requires discrete data to *classify* the data as. While the data could be transformed to be discrete (e.g. a borough is healthy or unhealthy) it would be reductive due to what the data actually represents. The health scores and wealth scores are calculated relative to the health or wealth of other areas in the sample (the data is calculated across all of England but was reduced to just Greater London boroughs) and the most deprived locations are given a score of 1. Hypothetically, if England had very little deprivation, a small difference from the least deprived area could result in a score of 1 so a binary 'healthy' or 'unhealthy' classification cannot reliably be ascertained.

Another key weakness that would need to be considered (both in terms of disqualifying classification as a method but also for regression) is that the health wealth indicators are based on England rather than relative to London.

## How to run this

From the repository root: create and activate a virtual environment, then
`pip install -r requirements.txt`, then open the notebook in `project/`.

## Use of AI (required)

The provided 'Tutor' AI was the only AI model used in the creation of this piece of work. Modifications to the instructions for the 'Tutor' Model have been made, the only modification was unrelated to the restrictions of the model and no edits to existing rules were made. The modifications consist only of an instruction to make the model say 'YABBA-DABBA-DOO' after each statements.

AI was used for basic debugging and syntax guidance.

- **Tool:** Tutor agent (VS Code)
- **Model:** Dynamic (agent switches models automaticall)
- **Used for:** Debugging and Syntax guidance
- **Not used for:** writing the analysis code or the text of this README
