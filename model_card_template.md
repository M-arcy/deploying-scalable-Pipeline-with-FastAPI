# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf


## Model Details
The model is a Random Forest Classifier trained to predict whether a person's income is above or below $50,000 based on demographic data from the US Census dataset included in the data folder. The model uses work class, education level, marital status, occupation, relationship type, race, sex and country of origin. 
Frameworks used included Scikit-learn, Python, Pandas, NumPy. Categorical features were one-hot encoded, and labels were binarized.

## Intended Use
The model is designed to assist in understanding demographic income patterns for research, analysis, or downstream tasks such as public policy evaluations. Specifically, it can be used by data analysts to explore income distributions across different demographic groups, by researchers studying socio-economic trends or as an educational example in machine learning and data science courses.
This model should not be used for decision-making affecting individuals (such as hiring decisions) as it may reflect biases present in the original dataset.

## Training Data
The training data comes from a [1994 U.S. Census dataset](https://archive.ics.uci.edu/dataset/20/census+income), which includes 32,561 samples of demographic and income information. The data was split into 80% training and 20% testing sets. 

## Evaluation Data
The evaluation data is the held-out 20% test set from the original census dataset. This consists of approximately 6,513 rows of data. The same preprocessing steps applied to the training set were used on the evaluation data to ensure consistency.

## Metrics
The following metrics were used to evaluate the model’s performance:

* Precision: 0.7419 <br>
>Precision measures the proportion of positive identifications that were actually correct.

* Recall: 0.6384<br>
> Recall measures the proportion of actual positives that were correctly identified.

* F1-Score: 0.6863<br>
> F1-score represents the harmonic mean of precision and recall, providing a balanced view of performance when 
classes are imbalanced.

__Slice-Based Performance:__
Performance metrics were also calculated on specific data slices, such as:

* Workclass: Self-emp-inc — Precision: 0.7807 | Recall: 0.7542 | F1: 0.7672
* Education: Bachelors — Precision: 0.7523 | Recall: 0.7289 | F1: 0.7404<br>
The full set of slice-based metrics is saved in the `slice_output.txt` file.

## Ethical Considerations
It is important to acknowledge that the U.S. Census dataset may reflect societal patterns and disparities in economic outcomes across demographic groups. These patterns can be influenced by a range of factors, including historical inequalities, structural barriers, and data limitations. As a result, the model may exhibit differences in performance for specific groups. Examples include:

Some occupations may have differing income distributions due to historical economic trends and systemic factors.
Groups with fewer data points (e.g., categories such as "Without-pay" under workclass) may yield less reliable predictions.
Additionally, income levels are shaped by broader socio-economic factors not captured by the dataset, such as inflation rates, educational opportunities, and regional variations in the cost of living.

Reference: For further reading on fairness and bias in machine learning, see Mitchell et al. (2019), Fairness and Abstraction in Sociotechnical Systems. [Link to paper can be found here.](https://arxiv.org/pdf/1811.07867)

## Caveats and Recommendations
__Use Cases:__ This model is intended for research and educational purposes and should not be used for high-stakes decision-making.<br>
__Data Limitations:__ The census data is from a specific time period and may not reflect current socio-economic conditions.<br>
__Bias Mitigation:__ It is recommended to apply fairness-enhancing tools, such as Aequitas or FairLearn, to analyze and mitigate potential biases.