
# 1. Loading the Dataset
import pandas as pd

# Load the dataset
df = pd.read_csv('traffic.csv')

# Display the first few rows to understand its structure
print(df.head())
# 2. Total Pageview Events & Pageviews Per Day
# We’ll filter out the pageview events and count their occurrences overall and per day.


# Assuming 'event' column contains types of events ('pageview', 'click', etc.)
# Assuming 'timestamp' contains the date information

# Total pageview events
total_pageviews = df[df['event'] == 'pageview'].shape[0]

# Convert timestamp to datetime if not already
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Pageviews per day
pageviews_per_day = df[df['event'] == 'pageview'].groupby(df['timestamp'].dt.date).size()

# Display results
total_pageviews, pageviews_per_day
# 3. Other Recorded Events
# Here, you want to group by event type to get counts for other types of events aside from pageviews.


# Group by event type to get the count of all events
event_counts = df.groupby('event').size()

# Display event counts
event_counts
# 4. Countries of Pageviews
# Find out which countries the pageviews came from by filtering on pageview events and grouping by country.


# Assuming there's a 'country' column and 'event' column
pageviews_by_country = df[df['event'] == 'pageview'].groupby('country').size()

# Display countries with pageviews
pageviews_by_country
# 5. Overall Click Rate (clicks/pageviews)
# To compute the click rate, divide the number of click events by the number of pageview events.


# Total click events
total_clicks = df[df['event'] == 'click'].shape[0]

# Click rate (clicks/pageviews)
click_rate = total_clicks / total_pageviews if total_pageviews > 0 else 0

# Display the overall click rate

# 6. Click Rate Distribution Across Links
# Finally, compute the click rate per link by grouping by the link, and calculating the click rate for each link.


# Assuming there's a 'link' column for the page link
clicks_per_link = df[df['event'] == 'click'].groupby('link').size()
pageviews_per_link = df[df['event'] == 'pageview'].groupby('link').size()

# Click rate per link
click_rate_per_link = (clicks_per_link / pageviews_per_link).fillna(0)

# Display click rates per link
click_rate_per_link