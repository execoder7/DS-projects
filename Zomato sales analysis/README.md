# Zomato Analysis README

## Overview

This project analyzes data from Zomato, a popular restaurant aggregator and food delivery service, to provide insights into customer preferences and restaurant performance. The analysis includes visualizations that address key questions about restaurant types, customer voting patterns, ratings, spending habits, and order modes.

## Questions Addressed

1. **What type of restaurants do the majority of customers order from?**
   - This analysis identifies the most popular restaurant categories based on customer orders.

2. **How many votes has each type of restaurant received from the customers?**
   - We quantify customer engagement by counting the votes for each restaurant type.

3. **What are the ratings that the majority of restaurants have received?**
   - This section explores the distribution of restaurant ratings to find the most common ratings.

4. **Zomato has observed that most couples order most of their food online. What is their average spending on each other?**
   - We calculate the average spending of couples on food orders to understand their dining habits.

5. **Which mode (online or offline) has received the most ratings?**
   - This analysis compares the ratings received by online and offline orders to determine customer preferences.

6. **Which type of restaurants received more offline orders, so that Zomato can provide customers with some good offers?**
   - We identify the restaurant types with higher offline orders to suggest potential promotional offers.

## Data Visualization

Visualizations are created using Python's pandas and matplotlib libraries to effectively communicate the findings. The following types of plots are utilized:

- **Bar Plots**: To show the number of orders and votes for each restaurant type.
- **Box Plots**: To represent the distribution of ratings for online and offline orders.
- **Heat map**: To illustrate trends in online and offline orders for different type of restaurants.

## Getting Started

### Prerequisites

Ensure you have the following libraries installed:

```bash
pip install pandas matplotlib seaborn
```

### Running the Analysis

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Load the dataset and run the analysis script:

   ```python
   import pandas as pd
   import matplotlib.pyplot as plt
   import seaborn as sns

   # Load your dataset
   df = pd.read_csv('zomato_data.csv')

   # Perform analysis and create visualizations
   # (Include the code for each analysis and plotting)
   ```

3. View the generated plots and insights.

## Conclusion

This analysis provides valuable insights into Zomato's customer behavior and restaurant performance. By understanding customer preferences and engagement, Zomato can enhance its offerings and improve customer satisfaction.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Citations:
[1] https://en.wikipedia.org/wiki/Zomato
[2] https://www.elluminatiinc.com/how-zomato-works-business-model-revenue-insights/
[3] https://blog.zomato.com/introducing-zomato-food-trends-data
[4] https://www.westgateresorts.com/blog/buffets-branson/
[5] https://www.zomato.com/fine-dining-near-me
[6] https://www.zomato.com/american-restaurants-near-me
[7] https://www.zomato.com/fast-food-restaurants-near-me
[8] https://mandarinrestaurant.com/our-story/
