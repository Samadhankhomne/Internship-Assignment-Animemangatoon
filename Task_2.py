from textblob import TextBlob
import pandas as pd

#  Sample user comments for "The Difference Between Manga and Manhwa"
comments = [
    "I love both manga and manhwa! They have their own unique styles.",
    "Manhwa art is so much better, but manga has better stories.",
    "This article is boring and didn’t provide any new information.",
    "I think manhwa is just a copy of manga, nothing original.",
    "Both manga and manhwa are great, but I prefer manga because of the deeper storylines.",
    "Great article! It really helped me understand the difference.",
    "I didn't like the way they explained it. Felt too biased.",
    "Manga will always be superior to manhwa in terms of storytelling.",
    "Thanks for this article! I always wondered what made them different.",
    "This article was confusing and didn't make any sense."
]

#  Function to classify sentiment
def analyze_sentiment(comment):
    blob = TextBlob(comment)
    return "positive" if blob.sentiment.polarity > 0 else "negative"

# Step 3: Create DataFrame and apply sentiment analysis
df = pd.DataFrame(comments, columns=['comment'])
df['sentiment'] = df['comment'].apply(analyze_sentiment)

#  Display results
print(df)

# Calculate percentage of positive and negative comments
positive_comments = len(df[df['sentiment'] == 'positive'])
negative_comments = len(df[df['sentiment'] == 'negative'])
total_comments = len(df)

positive_percentage = (positive_comments / total_comments) * 100
negative_percentage = (negative_comments / total_comments) * 100

print(f"Positive comments: {positive_percentage:.2f}%")
print(f"Negative comments: {negative_percentage:.2f}%")

