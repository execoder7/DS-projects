# Data Science Project: Sales Analysis

## Overview

This project analyzes a sales dataset to answer key business questions that can help improve sales strategies and marketing efforts. The analysis focuses on identifying trends in sales performance, customer behavior, and product relationships.

## Table of Contents

- [Questions Addressed](#questions-addressed)
- [Dataset](#dataset)
- [Installation](#installation)
- [Results](#results)
- [Conclusion](#conclusion)
- [License](#license)

## Questions Addressed

1. **What was the best month for sales? How much was earned that month?**
   - This analysis identifies the month with the highest sales and the total revenue generated during that month.

2. **Which city had the highest sales?**
   - We investigate sales by city to determine the location with the most significant revenue.

3. **What time should we display advertisements to maximize the likelihood of customers buying the product?**
   - The analysis explores sales data by hour to identify peak purchasing times.

4. **What products are often bought together?**
   - We analyze product combinations to find items that are frequently purchased together, providing insights for cross-selling opportunities.

5. **What products are sold the most? Why do you think they are sold the most?**
   - This section examines the top-selling products and discusses potential reasons for their popularity.

## Dataset

- **Description**: The dataset contains the following columns:
  - `Order ID`: Unique identifier for each order
  - `Product`: Name of the product sold
  - `Quantity Ordered`: Number of units sold
  - `Price Each`: Price per unit
  - `Order Date`: Date and time of the order
  - `Purchase Address`: Customer's address
  - `Month`: Month of the order
  - `Total Sales`: Total revenue from the order
  - `City`: City where the order was placed
  - `Hour`: Hour of the order

## Installation

To run this project, you need to have Python and the following libraries:

- os
- matplotlib
- collections
- itertools

## Results


- Best Month for Sales: 

![d3e0f92b-1eef-46ce-be53-3d386d7f6754](https://github.com/user-attachments/assets/0b35d77a-eac3-4488-9ee9-0d7dfe942ed4)

- City with Highest Sales: 

![c27f17cd-63df-4961-9b69-e40784c15536](https://github.com/user-attachments/assets/2718387c-337c-44be-b51a-b1156fb71732)

- Optimal Advertisement Timing: 
![61fd19af-2b33-4a40-8d07-dedceff552de](https://github.com/user-attachments/assets/799ebc57-e915-4ddd-88e7-21405883382a)
![ed8e4d7c-9831-4891-bd5a-018326a3b027](https://github.com/user-attachments/assets/7a17f287-7ca8-4b20-8221-d512f49eb582)

- Frequently Bought Together Products:

| Products                                                                                 | Count |
|-------------------------------------------------------------------------------------------|--------|
| (Lightning Charging Cable, iPhone)                                                       | 1015   |
| (Google Phone, USB-C Charging Cable)                                                     | 999    |
| (Wired Headphones, iPhone)                                                               | 462    |
| (Google Phone, Wired Headphones)                                                         | 423    |
| (Apple Airpods Headphones, iPhone)                                                       | 373    |
| (USB-C Charging Cable, Vareebadd Phone)                                                  | 368    |
| (Bose SoundSport Headphones, Google Phone)                                               | 228    |
| (USB-C Charging Cable, Wired Headphones)                                                 | 205    |
| (Vareebadd Phone, Wired Headphones)                                                      | 149    |
| (Lightning Charging Cable, Wired Headphones)                                             | 129    |


- Top-Selling Products: 
![1d2abfe8-8e42-41d0-8902-a3ec659b618d](https://github.com/user-attachments/assets/868c995e-c30f-4423-b649-3728e4fe5ecb)



