import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

df = pd.read_csv("personality_synthetic_dataset.csv")

df['social_score'] = df[
    [
        'social_energy',
        'talkativeness',
        'group_comfort',
        'party_liking',
        'public_speaking_comfort',
        'friendliness'
    ]
].mean(axis=1)

features = [
    'social_energy',
    'alone_time_preference',
    'talkativeness',
    'group_comfort',
    'party_liking',
    'public_speaking_comfort',
    'friendliness'
]

X = df[features]
y = df['social_score']

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LinearRegression())
])

pipe.fit(X, y)

def predict_personality(user_input_df):
    """
    Takes a DataFrame with feature values
    Returns: (score, personality_label)
    """

    score = pipe.predict(user_input_df)[0]

    if score >= 3.8:
        personality = "Extrovert 😄"
    elif score <= 2.5:
        personality = "Introvert 🤫"
    else:
        personality = "Ambivert 🙂"

    return round(score, 2), personality
