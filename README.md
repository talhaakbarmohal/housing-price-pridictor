# Melbourne Housing Price Prediction

This project predicts housing prices in Melbourne using various features such as location, area, number of rooms, and more. The system is built using **Flask** as the backend server and **HTML, JavaScript, and CSS** for the frontend interface.

## Project Overview

This web-based application provides a **predictive model** to estimate housing prices in Melbourne based on user input. The user can provide the following details:

- **Region**: The neighborhood or region of the property.
- **Distance from City**: How far the property is from the city center.
- **LandSize**: The total square footage of the house.
- **Number of Rooms**: Total rooms in the house.
- **Number of Bathrooms**: Total bathrooms in the house.

The application uses a **Flask server** to handle the API calls and run the prediction model, which estimates the price based on a pre-trained model.

## Features

- **User Input Form**: The user can input details through a clean, interactive web interface.
- **Price Prediction**: Using the machine learning model, the predicted price is shown after submitting the form.
- **Flask Backend**: Flask handles the logic and serves the model predictions.
- **Responsive Design**: The frontend is styled using **CSS** to be responsive and user-friendly.

## Technologies Used

- **Frontend**:
  - **HTML**: Basic structure of the web page.
  - **CSS**: Styling for the web interface to make it visually appealing.
  - **JavaScript**: To send requests to the Flask backend and update the page with results dynamically.

- **Backend**:
  - **Flask**: Python web framework used for handling API calls and serving the model predictions.
  - **Python Libraries**: 
    - **pandas**: For data manipulation and processing.
    - **scikit-learn**: For building the predictive model.
    - **pickle**: For loading the saved model.

- **Machine Learning Model**:
  - A trained model that predicts housing prices using various input features.

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/melbourne-housing-price-prediction.git
cd melbourne-housing-price-prediction
