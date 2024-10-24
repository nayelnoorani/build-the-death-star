Consider possible feature engineering

Next, we'll need to decide on our modeling approach, considering the class imbalance. We could try:

Random Forest with class weights
XGBoost with scale_pos_weight
LightGBM with is_unbalanced=True