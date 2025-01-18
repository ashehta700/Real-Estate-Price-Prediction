# Real Estate Price Prediction Application

## Overview
This project aims to build an AI-driven application to predict real estate prices in Egypt based on data collected from websites like aqarmap , bayut ,smsarko , propertyfinder ,   and aqaryamasr . The application will provide users with the predicted price of an apartment and display distances from essential utilities like roads, ATMs, hospitals, and more. The project involves data scraping, GIS analysis, AI model training, and application deployment.

## Project Steps

### Step 1: Data Collection (Web Scraping)
**Goal:** Extract apartment data such as price, location, area, and number of rooms from the Aqar website.

#### Technologies:
- Python
- Libraries: `requests`, `BeautifulSoup`, `Selenium`
- Database: PostgreSQL

#### Implementation Plan:
1. Inspect the website structure to identify data elements.
2. Develop a Python script to scrape:
   - Apartment price
   - Area (in square meters)
   - Number of rooms
   - Location (address or coordinates if available)
3. Save the scraped data into a database for further processing.


### Step 2: Geospatial Data Processing (GIS Layers)
**Goal:** Calculate the distance of apartments from utilities like roads, ATMs, and hospitals.

#### Technologies:
- Database: PostgreSQL with PostGIS extension
- Geocoding: Geopy (if location data is in text form)
- GIS Data: Obtain layers from public datasets or government sources

#### Implementation Plan:
1. Import GIS layers into PostGIS.
2. Geocode apartment addresses using Geopy to obtain latitude and longitude.
3. Use PostGIS functions like `ST_Distance()` to calculate distances from utilities.



### Step 3: AI Model Development
**Goal:** Train a machine learning model to predict apartment prices based on features like area, rooms, and distances to utilities.

#### Technologies:
- Python
- Libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`

#### Implementation Plan:
1. Preprocess the collected data (handle missing values, normalize distances, etc.).
2. Split data into training and testing sets.
3. Train a regression model (e.g., Linear Regression, Random Forest, or Neural Network).
4. Evaluate the model using metrics like Mean Absolute Error (MAE) and R-squared.



### Step 4: Application Deployment
**Goal:** Build a user-friendly app for predictions and visualizations.

#### Technologies:
- Frontend: Streamlit
- Backend: Flask 
- Mapping: Leaflet.js
- Database: PostgreSQL with PostGIS



## Expected Deliverables
1. **Web Scraper:** Script to extract apartment data.
2. **Database:** Structured storage for apartment and utility data.
3. **AI Model:** Trained model for price prediction.
4. **Application:** Deployed app with user-friendly UI and GIS-based visualizations.




#### Instalation Plan:
1. I use a streamlit technology to Run the scrapping page from sites like (Aqar - aqaryamasr - smsarko ,etc .. )
2. To use this app for scrap and collect the data just go to the "directory realstate pricing detection" and run the app with command "streamlit run app.py"
3. Enjoy with the smoothy userinterface that can collect the data with specific website you choice and then extract the data > > 
4. Then this data is loaded from a model and training on it and then get the location for this data and get the distance with GIS layers like (ATM's - Hospitals - Roads , etc .. )
5. Use Leaflet.js to visualize apartment locations and distances to utilities.
6. run the smoothy app with userfirendly that can predict the price of new house from user that the user can enter the location of his appartment 
7. The app can get him the distance away the main layers 
8. the app get the price fro rent and sale the appartment depend on the training 
9.To Run this app just go to the directory "house pricing app" and then run the command "streamlit run app.py" and Enjoy 




All @ Copy Rights Save to "Ahmed Shehta Ahmed"
https://ahmed-shehta.netlify.app


