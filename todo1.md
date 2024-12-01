


# TODO


- **Issue** need to ensure that any dataset used for features fully encompasses/spans all the subsections chosen
- **Consider** selecting between `geometry.within`, `geometry.intersects` or `geometry.overlaps` depending on the nature of the data set (choose case-by-case)
- **Consider** how to use speed limit data -- e.g., use mean speed limit for each subsection to create singular value per data item (row) -- would require considering the length of road as well so it's difficult



## Model 1 - Multi-Variable Linear Regression on GIS Data

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


### Development Process

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
   - z-score normalize (e.g., use `sklearn.preprocessing.StandardScaler`)
   - remove outliers
   - remove missing data
   - remove duplicates 

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

## Model 2 - ...

want to:

- use other concepts from class like
    - qualitative outputs (logistic regression)
    - support vectors
    - ...

### Development Process

in general, similar to model 1 development process
- [ ] Use a more efficient method of joining data by geographic distance. E.g., connecting arrest incidents with nearest sidewalk. Current method could take hours with 50k arrests dataset.
- [ ] When making Folium maps (geographic maps with popup markers on them), use a plotting technique more appropriate to the data (refer to lecture slides). E.g., a heat map, contour plot, hexagon scatter plot.
- [ ] In the [datasets](https://github.com/christian-byrne/tucson-crime-models/tree/main/data), go to `infrastructure` folder, choose other infrastructure datasets (e.g., `streetlights`), and explore correlations in the same way it's been done for sidewalks in [Analzing correlation between distance to sidewalks and arrest frequency](https://colab.research.google.com/github/christian-byrne/tucson-crime-models/blob/main/main.ipynb#scrollTo=q-fOMfTsP1vG&line=1&uniqifier=1)
- ...Explore other trends in the data with other approaches. See these [suggestions given by LLM](https://github.com/christian-byrne/tucson-crime-models/blob/main/doc/correlation-discovery.md)
