
# Model 1 - Multi-Variable Linear Regression on GIS Data

**inputs**: GIS data 
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
    - characteristics of subsection
        - race
            - column for each main race (or arbitrary groupings)
            - proportion of total  
        - mean income
        - mean education level
        - mean age

**output**: number of crimes / time legth of data set
            (aka crime frequency)


## Development Process

1. Create subsections
    - function that takes:
        - number subsections 
            - type: int
            - width/height        
        - returns list of:
            -`bbox` (bounding box)
                - type: `tuple[Float]`
                - (lat_lower, lat_upper, long_lower, long_upper)

2. Accumulating data from each appropriate dataset such that it's like:
    
    | num sidewalks | .... | characteristics | ... | total number of crimes |

3. Data cleaning

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

7. (hyperparamater tuning ?)

8. Evaluate model, reflect, make changes (repeat at step 5)
    - Choose some ...
        - arbitrary metric
        - significance level
        - baseline model
        - real model developed in actual scientific literature that does same thing
            - theres also a section of the report "Related Works" for this

# Model 2 - ...

want to:

- use other concepts from class like
    - qualitative outputs (logistic regression)
    - support vectors
    - ...

## Development Process

in general, similar to model 1 development process 
