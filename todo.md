- [Narrative](#narrative)
- [TODO](#todo)
  - [General](#general)
  - [Data Cleaning/Collection](#data-cleaningcollection)
  - [Data Exploration](#data-exploration)
  - [Feature Engineering](#feature-engineering)
  - [Data Visualization](#data-visualization)
  - [Hyperparameter Tuning](#hyperparameter-tuning)
  - [Evaluation](#evaluation)
  - [Discussion/Reflection](#discussionreflection)
- [Model 1—Subsection-Level Crime Frequency Prediction Using Infrastructure and Socioeconomic Features](#model-1subsection-level-crime-frequency-prediction-using-infrastructure-and-socioeconomic-features)
  - [Data](#data)
    - [Items](#items)
    - [Inputs/Features](#inputsfeatures)
    - [Output/Target](#outputtarget)
  - [Development Process](#development-process)
- [Model 2 Sociodemographic Prediction Using Crime Density Features](#model-2-sociodemographic-prediction-using-crime-density-features)
  - [Data](#data-1)
    - [Items](#items-1)
    - [Inputs/Features](#inputsfeatures-1)
    - [Output/Target](#outputtarget-1)
  - [Development Process](#development-process-1)

# Narrative


> Which is a better predictor of crime?
>
> - Socioeconomic features about people living somewhere
> - Infrastructure/geological features about the area
>
> Note: not trying to determine causal relationship, just determining which is a better predictor (in the nature of data science)

**Model 1:**

| Items       | Inputs/Features         | Output/Target   | Model Type                    |
| ----------- | ----------------------- | --------------- | ----------------------------- |
| Subsections | Infrastructure features | Crime Frequency | Ridge/Lasso Linear Regression |

**Model 2:**

| Items       | Inputs/Features                                                | Output/Target          | Model Type            |
| ----------- | -------------------------------------------------------------- | ---------------------- | --------------------- |
| Subsections | Crime Density, Possibly crime density at different zoom levels | Socioeconomic features | SVM or Decision Trees |

# TODO

## General

- [ ] ~~(optional - If have time) Combine arrests datasets from diff years into one dataset in beginning of notebook~~ no time
- [ ] edit written sections of notebook
- [ ] add inline comments where necessary
- [x] Use processes from previous HW
  - [x] data scale transform

## Data Cleaning/Collection


- [x] Use github link to load dependencies instead of requiring local file
- [x] ~~function to ensure that any dataset used for features **fully encompasses/spans** all the subsections chosen~~ We already span the entire region (verified visually) by just using the sidewalks dataset as the reference area
- [x] function to check geographical domain of datasets then create intersection $\rightarrow$ give to function that creates subsections
- [x] Best way to test for feature multicollinearity?
  - [x] e.g.,
    - [x] ~~use VIF (Variance Inflation Factor) to test for multicollinearity~~ correlation matrix with a threshold seems adequate
    - [x] plot correlation matrix, etc.
  - [x] Resolution strategy: if scales are different → drop the feature that has lower correlation with target variable; else if scales are same → use PCA to combine into single feature
- [x] Move feature engineering stuff into data processing, especially because we need the results of that code earlier on (e.g., for data viz)
- [x] ~~Determine why the `business_license` dataset is not being working~~ It has addresses but no geometry data, so it cannot be used
- [x] Define what an outlier would be → If and how to remove?


## Data Exploration

- [x] ~~Decide how to use speed limit data -- e.g., use mean speed limit for each subsection to create singular value per data item (row) -- would require considering the length of road as well so it's difficult~~ (not important)
- [x] (most likely no longer relevant) ~~Use a more efficient method of joining data by geographic distance. E.g., connecting arrest incidents with nearest sidewalk. Current method could take hours with 50k arrests dataset.~~
- [x] In the [datasets](https://github.com/christian-byrne/tucson-crime-models/tree/main/data), go to `infrastructure` folder, choose other infrastructure datasets (e.g., `streetlights`), and explore correlations in the same way it's been done for sidewalks in [Analzing correlation between distance to sidewalks and arrest frequency](https://colab.research.google.com/github/christian-byrne/tucson-crime-models/blob/main/main.ipynb#scrollTo=q-fOMfTsP1vG&line=1&uniqifier=1)
- [x] ...Explore other trends in the data with other approaches. See these [suggestions given by LLM](https://github.com/christian-byrne/tucson-crime-models/blob/main/doc/correlation-discovery.md)

## Feature Engineering

- [ ] (Optional) Can test with completely random subsections similar to how bagging and random forest work -- i.e., we don't attempt to span the entire area of interest, we just randomly generate subsections within bounds (with replacement).
  - [x] ~~Can also randomize the allowed area, which would naturally be random if x and y are randomly generated~~ redundant
  - [ ] This approach can also be used to essentially create unlimited test data for more extensive evaluation
- [x] ~~Are subsections actually too long (longitudinally)?~~ NO: the long subsections occur because the outer bounds (Tucson city bounds) create a long rectangle so naturally the subsections mirror that shape
  - [x] Solution: do not create $n \times n$ subsections but rather $n \times m$ subsections where $m < n$ - calculate $m$ based on the aspect ratio of the outer bounds
- [x] (optional) selecting between `geometry.within`, `geometry.intersects` or `geometry.overlaps` depending on the nature of the data set (choose case-by-case)
- [x] Fix `create_subsections` function not creating sections over entire outer bounds
- [x] Determine outer bounds using ~~some better approach~~ (for now: sidewalks feature dataset, since arrests has a ton of geographically dispersed data/outliers way outside bounds of the other datasets)
- [ ] Setup feature processing for socioeconomic features
- [x] Implement the separation of _distance_to_ and _density_ infrastructure features

## Data Visualization

- [ ] Refer EDA slides
- [x] Visualize grouped box plots of all the features similar to HW7
- [x] ~~Create indicator of what the outer bounds are on the visualizations~~ The visualization of the subsections already demonstrates this implicitly
- [x] Change `visualize_objects_in_subsection` function to be more efficient (probably don't need to to filter by objects in subsection and can just plot all objects)
- [x] Combine the density-feature distributions plots into a single plot/figure
- [x] Heatmaps over scatterplot for infrastructure on real map
  - [x] When making Folium maps (geographic maps with popup markers on them), use a plotting technique more appropriate to the data (refer to lecture slides). E.g., a heat map, contour plot, hexagon scatter plot.
  - [x] Create a heatmap variant of the crime frequency visualization

## Hyperparameter Tuning

- [ ] Take all abritrary values (or numbers used in functions that can be thought of as arbitrary and parametrized)
  - [x] → put into the global config object
  - [x] → treat as hyperparameters
  - [ ] → tune them

## Evaluation

- [ ] On top of using the test data from initial split, also can make more subsections by changing the params of the `create_subsections` function to use different sizes, diffferent type of randomness, etc.
- [x] For both models, need more ways to evaluate
  - [x] compare vs baseline model
  - [x] ~~compare vs real model in scientific literature or similar algorithm~~ too hard to find
- [x] (from rubric) For both models, need more visualizations in the evaluation stage to demonstrate the model's performance and interpret how it works (or our best guess at how it works)

## Discussion/Reflection

- [x] Can include in discussion: development process (todo, github history, process of recognizing sparse features and changing to `distance_to`, etc.)
- [x] Optional ideas
  - [x] ~~Model chain: infra -> predicted density -> predicted socioeconomic feature~~
  - [x] ~~Abstract to paths for interesting utility/inference~~ not enough time

# Model 1—Subsection-Level Crime Frequency Prediction Using Infrastructure and Socioeconomic Features

## Data

### Items

- subsections of Tucson

### Inputs/Features

- number of ... included in subsection
  - sidewalk
  - bicycle boulevards
  - landfill
  - fire station
  - bridge
  - crosswalk
  - streetcar route
  - streetcar stop
  - scenic route
  - streetlight
  - suntran bus stop

### Output/Target

- number of crimes per time legth of data set (a.k.a. crime frequency)

## Development Process

1. Create subsections

   - function that takes:
     - number subsections
       - type: int
       - width/height
     - returns list of: -`bbox` (bounding box) - type: `tuple[Float]` - (lat_lower, lat_upper, long_lower, long_upper)

2. Collecting and organizing data into format:

   | num sidewalks | .... | characteristics | ... | total number of crimes |
   | ------------- | ---- | --------------- | --- | ---------------------- |
   | $x_1$         | .... | $c_1$           | ... | $y_1$                  |
   | $x_2$         | .... | $c_2$           | ... | $y_2$                  |
   | ...           | .... | ...             | ... | ...                    |

3. [ ] Data cleaning

   - z-score normalize (e.g., use `sklearn.preprocessing.StandardScaler`)
   - remove outliers
   - remove missing data
   - remove duplicates
   - validate geographical area of interest matches with function that creates subsection

4. Split data into training and testing sets

5. Determining best regression type:

   - For each regression type, hyperpamater tuning (determine optimal params)
     - Best subsets
       - particular subset of features
     - Lasso reg
       - best lambda/alpha (LARS)
     - Ridge reg
       - best lambda/alpha
   - Choose best regression type

6. Use given regression type to fit model

7. (hyperparamater tuning ?) afterwards

8. Evaluate model, reflect, make changes (repeat at step 5)
   - Choose some ...
     - arbitrary metric
     - significance level
     - baseline model
     - real model developed in actual scientific literature that does same thing
       - theres also a section of the report "Related Works" for this

# Model 2 Sociodemographic Prediction Using Crime Density Features

## Data

### Items

- subsections of Tucson

### Inputs/Features

- crime density
  - crime density at different zoom levels

### Output/Target

- characteristics of subsection
  - race
    - column for each main race (or arbitrary groupings)
    - proportion of total
  - mean income
  - mean education level
  - mean age
  - ~~mean speed limit~~ Not worth taking time to figure out how to preprocess this data

## Development Process
