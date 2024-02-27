# Bitcoin Price Prediction Web Application

This is a Flask web application that predicts future Bitcoin prices and displays the current Bitcoin price obtained from an external API. The application uses a pre-trained machine learning model for Bitcoin price prediction.

## Prerequisites

Before running the application, make sure you have the following dependencies installed:

- [Python 3.x](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [Conda (Miniconda/Anaconda)](https://docs.conda.io/en/latest/miniconda.html) (Choose the one that suits your project requirements)

1. Clone the repository using 
   ```shell
   git clone <repo_URL> 
   ```
   in the command prompt of the VS code

2. Create a conda environment using conda 
   ```shell
   conda create -n bitcoin 
   ```

3. Activate the conda environment using
   ```shell
   conda activate bitcoin 
   ```

4. You can install these dependencies using `pip`. For example:
  ```shell
  pip install -r requirements.txt
  ```

5. Navigate to the 'flask' directory and run the application using python 
  ```shell
  python app.py
  ```

## Usage

### Home Page

The home page displays the current Bitcoin price obtained from an external API. This price is updated regularly.

### Price Prediction

To predict the price of Bitcoin for a specific date, you can use the "Predict" page:

1. Enter a date in the "Date" field in the format "YYYY-MM-DD."

2. Click the "Predict" button.

The application will attempt to provide a Bitcoin price prediction for the specified date based on the pre-trained model. If the date is not found in the forecast data, it will display an error message.

### Model

The application uses the Prophet forecasting library to make Bitcoin price predictions. The model is loaded from a pre-trained pickle file named `fbcrypto.pkl`. You can replace this file with your own trained model if needed.

### External API

The application fetches the current Bitcoin price from the CoinGecko API. The API request is made in the `get_current_bitcoin_price` function.
