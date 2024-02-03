####################################################

#Feature Selection using a Univariate Testing

####################################################


import pandas as pd

my_df = pd.read_csv("feature_selection_sample_data.csv")

from sklearn.feature_selection import SelectKBest ,f_regression

X = my_df.drop(["output"],axis =1)

y = my_df["output"]

feature_selector = SelectKBest(f_regression, k="all")

fit = feature_selector.fit(X,y)

fit.pvalues_
fit.scores_

p_values = pd.DataFrame(fit.pvalues_)
scores = pd.DataFrame(fit.scores_)
input_variable_names = pd.DataFrame(X.columns)

summary_stats = pd.concat([input_variable_names,p_values,scores], axis= 1)
summary_stats.columns = ["input_variable","p_value","f_score"]
summary_stats.sort_values(by = "p_value", inplace =True)

p_value_threshold = 0.05 
score_threshold = 5

selected_variables = summary_stats.loc[(summary_stats["f_score"]>= score_threshold) & (summary_stats["p_value"]<= p_value_threshold)]

selected_variables = selected_variables["input_variable"].tolist()

X_new = X[selected_variables]



feature_selector = SelectKBest(f_regression, k=2)

fit = feature_selector.fit(X,y)

X_new1 = feature_selector.transform(X)

feature_selector.get_support()

X_new1 = X.loc[:,feature_selector.get_support()]


# Regression Template

import pandas as pd

my_df = pd.read_csv("feature_selection_sample_data.csv")

from sklearn.feature_selection import SelectKBest ,f_regression

X = my_df.drop(["output"],axis =1)

y = my_df["output"]

feature_selector = SelectKBest(f_regression, k="all")

fit = feature_selector.fit(X,y)



p_values = pd.DataFrame(fit.pvalues_)
scores = pd.DataFrame(fit.scores_)
input_variable_names = pd.DataFrame(X.columns)

summary_stats = pd.concat([input_variable_names,p_values,scores], axis= 1)
summary_stats.columns = ["input_variable","p_value","f_score"]
summary_stats.sort_values(by = "p_value", inplace =True)

p_value_threshold = 0.05 
score_threshold = 5

selected_variables = summary_stats.loc[(summary_stats["f_score"]>= score_threshold) & (summary_stats["p_value"]<= p_value_threshold)]

selected_variables = selected_variables["input_variable"].tolist()

X_new = X[selected_variables]


# Classification Template

import pandas as pd

my_df = pd.read_csv("feature_selection_sample_data.csv")

from sklearn.feature_selection import SelectKBest ,chi2

X = my_df.drop(["output"],axis =1)

y = my_df["output"]

feature_selector = SelectKBest(chi2, k="all")

fit = feature_selector.fit(X,y)



p_values = pd.DataFrame(fit.pvalues_)
scores = pd.DataFrame(fit.scores_)
input_variable_names = pd.DataFrame(X.columns)

summary_stats = pd.concat([input_variable_names,p_values,scores], axis= 1)
summary_stats.columns = ["input_variable","p_value","chi2_score"]
summary_stats.sort_values(by = "p_value", inplace =True)

p_value_threshold = 0.05 
score_threshold = 5

selected_variables = summary_stats.loc[(summary_stats["chi2_score"]>= score_threshold) & (summary_stats["p_value"]<= p_value_threshold)]

selected_variables = selected_variables["input_variable"].tolist()

X_new = X[selected_variables]