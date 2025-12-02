
import pandas as pd
import matplotlib.pyplot as plt

CSV_PATH = "harmful_content_dataset.csv"

df = pd.read_csv(CSV_PATH)

print("Head:")
print(df.head())
print("\nCategory value counts:")
print(df['category'].value_counts())

plt.figure()
df['category'].value_counts().plot(kind='bar')
plt.title("Content Category Distribution")
plt.xlabel("Category")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("category_distribution.png")
plt.close()

severity_map = {
    "safe": 0,
    "spam": 1,
    "misinformation": 2,
    "harassment": 2,
    "hate_speech": 3,
    "violent_speech": 3,
}
df['severity_score'] = df['category'].map(severity_map)

print("\nAverage severity score:", df['severity_score'].mean())

user_stats = (
    df.groupby('user_id')
      .agg(
          total_comments=('comment_id', 'count'),
          harmful_comments=('severity_score', lambda x: (x > 0).sum()),
          avg_severity=('severity_score', 'mean')
      )
      .reset_index()
)
user_stats['harmful_ratio'] = user_stats['harmful_comments'] / user_stats['total_comments']

print("\nTop 10 high-risk users by harmful_ratio:")
print(user_stats.sort_values('harmful_ratio', ascending=False).head(10))

user_stats.to_csv("user_level_stats.csv", index=False)

print("\nUser-level stats saved to user_level_stats.csv")
print("Category distribution chart saved to category_distribution.png")
