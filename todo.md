- [TODO](#todo)
  - [General](#general)
  - [Data Validation](#data-validation)
  - [Data Collection](#data-collection)
- [Model 1—Subsection-Level Crime Frequency Prediction Using Infrastructure and Socioeconomic Features](#model-1subsection-level-crime-frequency-prediction-using-infrastructure-and-socioeconomic-features)
  - [Data](#data)
    - [Items](#items)
    - [Inputs/Features](#inputsfeatures)
    - [Output/Target](#outputtarget)
  - [Development Process](#development-process)
- [Model 2 (TBD)—Some Classification-Based Model Using SVM, Decision Trees, and/or Logistic Regression](#model-2-tbdsome-classification-based-model-using-svm-decision-trees-andor-logistic-regression)
  - [Data](#data-1)
    - [Items](#items-1)
    - [Inputs/Features](#inputsfeatures-1)
    - [Output/Target](#outputtarget-1)
  - [Development Process](#development-process-1)

# TODO

## General

- [ ] Fix `create_subsections` function not creating sections over entire outer bounds
- [ ] Create indicator of what the outer bounds are on the visualizations
- [ ] Change `visualize_objects_in_subsection` function to be more efficient (probably don't need to to filter by objects in subsection and can just plot all objects)
- [ ] Combine the density-feature distributions plots into a single plot/figure
- [ ] Determine why the `business_license` dataset is not being working
- [ ] Create a heatmap variant of the crime frequency visualization
- [x] ~~Are subsections actually too long (longitudinally)?~~ NO: the long subsections occur because the outer bounds (Tucson city bounds) create a long rectangle so naturally the subsections mirror that shape
- [ ] Take all abritrary values (or numbers used in functions that can be thought of as arbitrary and parametrized) → put into the global config object → treat as hyperparameters → tune them
- [ ] If and how to remove outliers
- [ ] Decide how to use speed limit data -- e.g., use mean speed limit for each subsection to create singular value per data item (row) -- would require considering the length of road as well so it's difficult
- [ ] (most likely no longer relevant) ~~Use a more efficient method of joining data by geographic distance. E.g., connecting arrest incidents with nearest sidewalk. Current method could take hours with 50k arrests dataset.~~
- [ ] When making Folium maps (geographic maps with popup markers on them), use a plotting technique more appropriate to the data (refer to lecture slides). E.g., a heat map, contour plot, hexagon scatter plot.
- [x] In the [datasets](https://github.com/christian-byrne/tucson-crime-models/tree/main/data), go to `infrastructure` folder, choose other infrastructure datasets (e.g., `streetlights`), and explore correlations in the same way it's been done for sidewalks in [Analzing correlation between distance to sidewalks and arrest frequency](https://colab.research.google.com/github/christian-byrne/tucson-crime-models/blob/main/main.ipynb#scrollTo=q-fOMfTsP1vG&line=1&uniqifier=1)
- [x] ...Explore other trends in the data with other approaches. See these [suggestions given by LLM](https://github.com/christian-byrne/tucson-crime-models/blob/main/doc/correlation-discovery.md)

## Data Validation

- [ ] function to ensure that any dataset used for features **fully encompasses/spans** all the subsections chosen
  - function to check geographical domain of datasets then create intersection $\rightarrow$ give to function that creates subsections

## Data Collection

- [ ] (optional) selecting between `geometry.within`, `geometry.intersects` or `geometry.overlaps` depending on the nature of the data set (choose case-by-case)

# Model 1—Subsection-Level Crime Frequency Prediction Using Infrastructure and Socioeconomic Features

## Data

### Items

- [ ] subsections of Tucson

### Inputs/Features

- [ ] number of ... included in subsection
  - [ ] sidewalk
  - [ ] bicycle boulevards
  - [ ] landfill
  - [ ] fire station
  - [ ] bridge
  - [ ] crosswalk
  - [ ] streetcar route
  - [ ] streetcar stop
  - [ ] scenic route
  - [ ] streetlight
  - [ ] suntran bus stop
- [ ] characteristics of subsection
  - [ ] race
    - [ ] column for each main race (or arbitrary groupings)
    - [ ] proportion of total
  - [ ] mean income
  - [ ] mean education level
  - [ ] mean age
  - [ ] mean speed limit

### Output/Target

- [ ] number of crimes per time legth of data set (a.k.a. crime frequency)

## Development Process

1. [x] Create subsections

   - function that takes:
     - number subsections
       - type: int
       - width/height
     - returns list of: -`bbox` (bounding box) - type: `tuple[Float]` - (lat_lower, lat_upper, long_lower, long_upper)

2. [x] Collecting and organizing data into format:

   | num sidewalks | .... | characteristics | ... | total number of crimes |
   | ------------- | ---- | --------------- | --- | ---------------------- |
   | $x_1$         | .... | $c_1$           | ... | $y_1$                  |
   | $x_2$         | .... | $c_2$           | ... | $y_2$                  |
   | ...           | .... | ...             | ... | ...                    |

3. [ ] Data cleaning

   - [x] z-score normalize (e.g., use `sklearn.preprocessing.StandardScaler`)
   - [ ] remove outliers
   - [x] remove missing data
   - [ ] remove duplicates
   - [ ] validate geographical area of interest matches with function that creates subsection

4. [x] Split data into training and testing sets

5. [x] Determining best regression type:

   - For each regression type, hyperpamater tuning (determine optimal params)
     - Best subsets
       - particular subset of features
     - Lasso reg
       - best lambda/alpha (LARS)
     - Ridge reg
       - best lambda/alpha
   - Choose best regression type

6. [x] Use given regression type to fit model

7. [ ] (hyperparamater tuning ?) afterwards

8. [ ] Evaluate model, reflect, make changes (repeat at step 5)
   - Choose some ...
     - arbitrary metric
     - significance level
     - baseline model
     - real model developed in actual scientific literature that does same thing
       - theres also a section of the report "Related Works" for this

# Model 2 (TBD)—Some Classification-Based Model Using SVM, Decision Trees, and/or Logistic Regression

want to:

- use other concepts from class like
  - qualitative outputs (logistic regression)
  - support vectors
  - decision trees

## Data

### Items

...tbd

### Inputs/Features

...tbd

### Output/Target

...tbd

## Development Process

...tbd
