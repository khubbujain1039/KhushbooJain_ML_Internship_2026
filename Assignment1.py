# Netflix User Analytics - Week 2 Assignment 1
# Dataset: 750 Netflix users with demographics, viewing habits, and subscription details

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, mean_squared_error

# ─────────────────────────────────────────────────────────────────────────────
# PART A: Dataset Understanding
# ─────────────────────────────────────────────────────────────────────────────

# Q1. Load the dataset and display the first five records
df = pd.read_csv("Dataset_2.csv")
print("=" * 60)
print("Q1. First Five Records")
print("=" * 60)
print(df.head())

# Q2. Number of rows and columns
print("\n" + "=" * 60)
print("Q2. Shape of Dataset")
print("=" * 60)
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# Q3. All column names
print("\n" + "=" * 60)
print("Q3. Column Names")
print("=" * 60)
print(df.columns.tolist())

# Q4. Numerical and categorical features
print("\n" + "=" * 60)
print("Q4. Numerical and Categorical Features")
print("=" * 60)
numerical_features = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
categorical_features = df.select_dtypes(include=["object"]).columns.tolist()
print(f"Numerical Features  : {numerical_features}")
print(f"Categorical Features: {categorical_features}")

# Q5. Missing values check
print("\n" + "=" * 60)
print("Q5. Missing Values")
print("=" * 60)
print(df.isnull().sum())
if df.isnull().sum().sum() == 0:
    print("\nNo missing values found in the dataset.")
else:
    print("\nMissing values detected — consider imputation or removal.")

# ─────────────────────────────────────────────────────────────────────────────
# PART B: Exploratory Data Analysis
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("Q6. Average Age of Users")
print("=" * 60)
print(f"Average Age: {df['Age'].mean():.2f} years")

print("\n" + "=" * 60)
print("Q7. Average Watch Hours Per Week")
print("=" * 60)
print(f"Average Watch Hours/Week: {df['WatchHoursPerWeek'].mean():.2f} hours")

print("\n" + "=" * 60)
print("Q8. Average Monthly Spending")
print("=" * 60)
print(f"Average Monthly Spend: ₹{df['MonthlySpend'].mean():.2f}")

print("\n" + "=" * 60)
print("Q9. Users per Subscription Category")
print("=" * 60)
print(df['SubscriptionType'].value_counts())

print("\n" + "=" * 60)
print("Q10. Subscription Renewal Percentage")
print("=" * 60)
renewal_pct = (df['SubscriptionRenewed'].value_counts(normalize=True) * 100).round(2)
print(renewal_pct)
print(f"\n{renewal_pct.get('Yes', 0)}% of users renewed their subscriptions.")

# ─────────────────────────────────────────────────────────────────────────────
# PART C: Data Preparation
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("Q11. Encoding Categorical Features")
print("=" * 60)

df_encoded = df.copy()
le = LabelEncoder()

for col in categorical_features:
    df_encoded[col] = le.fit_transform(df_encoded[col])

print("Categorical columns encoded successfully.")
print(df_encoded.head())

# Q12. Feature set and target variable for subscription renewal prediction
print("\n" + "=" * 60)
print("Q12. Feature Set (X) and Target Variable (y)")
print("=" * 60)

# Drop UserID (not a predictor) and the target column
X = df_encoded.drop(columns=["UserID", "SubscriptionRenewed"])
y = df_encoded["SubscriptionRenewed"]

print(f"Features (X): {X.columns.tolist()}")
print(f"Target   (y): SubscriptionRenewed")

# Q13. Train-test split
print("\n" + "=" * 60)
print("Q13. Train-Test Split (80% train / 20% test)")
print("=" * 60)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Training samples : {X_train.shape[0]}")
print(f"Testing  samples : {X_test.shape[0]}")

# ─────────────────────────────────────────────────────────────────────────────
# PART D: Decision Tree Classification
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("Q14. Training Decision Tree Classifier")
print("=" * 60)

dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
print("Decision Tree model trained successfully.")

# Q15. Accuracy
print("\n" + "=" * 60)
print("Q15. Decision Tree Accuracy")
print("=" * 60)

y_pred_dt = dt_model.predict(X_test)
dt_accuracy = accuracy_score(y_test, y_pred_dt)
print(f"Decision Tree Accuracy: {dt_accuracy * 100:.2f}%")

# Q16. Confusion Matrix
print("\n" + "=" * 60)
print("Q16. Confusion Matrix — Decision Tree")
print("=" * 60)

cm_dt = confusion_matrix(y_test, y_pred_dt)
print(cm_dt)
print("\nInterpretation:")
print(f"  True Negatives  (correctly predicted 'No renewal') : {cm_dt[0][0]}")
print(f"  False Positives (predicted 'Yes' but actually 'No'): {cm_dt[0][1]}")
print(f"  False Negatives (predicted 'No' but actually 'Yes'): {cm_dt[1][0]}")
print(f"  True Positives  (correctly predicted 'Yes renewal'): {cm_dt[1][1]}")

disp = ConfusionMatrixDisplay(confusion_matrix=cm_dt, display_labels=["No", "Yes"])
disp.plot(cmap="Blues")
plt.title("Confusion Matrix — Decision Tree")
plt.tight_layout()
plt.savefig("confusion_matrix_dt.png", dpi=150)
plt.show()
print("Plot saved as confusion_matrix_dt.png")

# ─────────────────────────────────────────────────────────────────────────────
# PART E: K-Nearest Neighbors (KNN)
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("Q17. Training KNN Classifier (K = 5)")
print("=" * 60)

knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)
print("KNN model trained successfully.")

# Q18. Compare KNN vs Decision Tree accuracy
print("\n" + "=" * 60)
print("Q18. KNN vs Decision Tree — Accuracy Comparison")
print("=" * 60)

y_pred_knn = knn_model.predict(X_test)
knn_accuracy = accuracy_score(y_test, y_pred_knn)

print(f"Decision Tree Accuracy : {dt_accuracy * 100:.2f}%")
print(f"KNN Accuracy (K=5)     : {knn_accuracy * 100:.2f}%")

if dt_accuracy > knn_accuracy:
    print("\nConclusion: Decision Tree performed better for subscription renewal prediction.")
elif knn_accuracy > dt_accuracy:
    print("\nConclusion: KNN performed better for subscription renewal prediction.")
else:
    print("\nConclusion: Both models achieved the same accuracy.")

# ─────────────────────────────────────────────────────────────────────────────
# PART F: Linear Regression
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("Q19. Training Linear Regression to Predict Monthly Spending")
print("=" * 60)

# Use all features except UserID and MonthlySpend as predictors
X_reg = df_encoded.drop(columns=["UserID", "MonthlySpend"])
y_reg = df_encoded["MonthlySpend"]

X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)

lr_model = LinearRegression()
lr_model.fit(X_train_reg, y_train_reg)

y_pred_reg = lr_model.predict(X_test_reg)
rmse = np.sqrt(mean_squared_error(y_test_reg, y_pred_reg))

print(f"Linear Regression trained successfully.")
print(f"RMSE on test set: ₹{rmse:.2f}")

# Q20. Predict monthly spending for a new user
print("\n" + "=" * 60)
print("Q20. Predicting Monthly Spending for a New User")
print("=" * 60)

# New user profile (values must match encoding used above):
# Age=30, Gender=Male(1), SubscriptionType=Premium(1), WatchHoursPerWeek=15,
# DevicesUsed=2, FavoriteGenre=Action(0), AdClicks=20, SubscriptionRenewed=Yes(1)
new_user = pd.DataFrame([{
    "Age": 30,
    "Gender": 1,                  # 1 = Male (after LabelEncoder)
    "SubscriptionType": 1,        # 1 = Premium
    "WatchHoursPerWeek": 15,
    "DevicesUsed": 2,
    "FavoriteGenre": 0,           # 0 = Action
    "AdClicks": 20,
    "SubscriptionRenewed": 1      # 1 = Yes
}])

predicted_spend = lr_model.predict(new_user)[0]
print(f"Predicted Monthly Spending: ₹{predicted_spend:.2f}")
print("\nInterpretation:")
print(f"  Based on the user's profile (Age 30, Premium subscriber, 15 hrs/week,")
print(f"  2 devices, 20 ad clicks), the model predicts a monthly spend of ₹{predicted_spend:.2f}.")
print(f"  Netflix can use this to anticipate revenue and tailor upsell offers.")

# ─────────────────────────────────────────────────────────────────────────────
# Business Reflection Questions
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("BUSINESS REFLECTION QUESTIONS")
print("=" * 60)

print("""
1. Which factors appear to influence subscription renewal the most?
   WatchHoursPerWeek, MonthlySpend, SubscriptionType, and DevicesUsed
   tend to be the most influential features, as highly engaged users
   who spend more are more likely to renew.

2. Why is subscription renewal a classification problem?
   Because the target variable (SubscriptionRenewed) has discrete
   categories — 'Yes' or 'No'. Classification algorithms predict
   which class a new observation belongs to.

3. Why is monthly spending a regression problem?
   Because MonthlySpend is a continuous numerical variable. Regression
   models predict a real-valued output rather than a discrete category.

4. Which algorithm performed better for renewal prediction?
   See Q18 output above for the exact comparison. In general, Decision
   Trees handle mixed feature types well and are easier to interpret,
   while KNN can outperform when the data has local patterns.

5. How could the platform use these predictions to improve customer retention?
   - Identify users likely NOT to renew and proactively offer discounts
     or personalised content recommendations.
   - Use spending predictions to design targeted upsell campaigns.
   - Segment users by genre and subscription type for tailored marketing.
   - Trigger early retention interventions for low watch-hour users.
""")