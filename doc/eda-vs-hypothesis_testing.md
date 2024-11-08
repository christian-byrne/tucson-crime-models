1. **Hypothesis Generation from Data**:
 
    In data science, especially when aiming to model and predict outcomes, we often start with data exploration to generate potential hypotheses rather than defining them strictly before seeing the data. This is more exploratory and does not violate scientific rigor, as our goal isn't to confirm hypotheses with statistical significance but to find patterns that generalize well in unseen data.

2. **p-Hacking and Traditional Hypothesis Testing**:
 
    In scientific research, hypotheses are ideally pre-defined to prevent p-hacking, where researchers could "cherry-pick" significant results that appear due to random variation. The strict p-value threshold (e.g., 0.05) is meant to filter out false positives, but it can be misleading if researchers look for significance after seeing the data.

    Data science generally isn’t bound by p-values in the same way, so exploring data to form hypotheses is acceptable because we aren’t trying to validate them with p-values.

3. **Predictive/Inference Models and Performance Testing**:

    Data scientists focus on creating models that perform well on unseen data, not merely fitting hypotheses to known data. After generating hypotheses from patterns observed in the data, you then test their predictive power by training models and evaluating them on validation or test sets.
    
    If a hypothesis (or feature in the model) only "works" by chance, it will likely fail in the test phase, where the model's performance will reveal any random or spurious correlations.

4. **Model Evaluation in Data Science as a Guard Against Random Hypotheses**:

    Instead of relying on p-values, data science uses metrics like accuracy, precision, recall, and others (depending on the task) on validation and test datasets. These metrics assess how well the model’s inferences generalize, inherently weeding out weak or chance-based hypotheses.

    In short, because data science is focused on predictive accuracy rather than confirmatory hypothesis testing, it's natural and acceptable to derive hypotheses from the data, as long as they're tested for generalizability. This makes hypothesis generation from data a valid approach in data science, free from the risks of p-hacking seen in traditional hypothesis testing.