# PNB Stock Data (pnb1y.csv)

## Overview

This repository contains historical stock data for Punjab National Bank (PNB) for a duration of one year. The data is stored in a CSV file named `pnb1y.csv`. This README provides essential information about the dataset to help users understand and utilize the data effectively.

## File Description

- **pnb1y.csv**: This CSV file contains the PNB stock data for the past year. Each row in the file represents a specific time point, and columns include relevant information such as date, opening price, closing price, high, low, volume, etc.

## Data Columns

- **Date**: The date of the stock data.
- **Open**: The opening price of PNB stock on a given date.
- **High**: The highest price of PNB stock on a given date.
- **Low**: The lowest price of PNB stock on a given date.
- **Close**: The closing price of PNB stock on a given date.
- **Volume**: The trading volume of PNB stock on a given date.

## Usage

Researchers, analysts, and developers can use this dataset for various purposes, including:

- Analyzing historical stock performance.
- Building predictive models for stock price forecasting.
- Conducting technical analysis on PNB stock.

## Example Usage (Python)

Here's a simple example of how to load and display the first few rows of the dataset using Python and Pandas:

```python
import pandas as pd

# Load the dataset
df = pd.read_csv('pnb1y.csv')

# Display the first few rows
print(df.head())
