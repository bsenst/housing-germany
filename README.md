# housing-germany
Machine learning project for the [Data Talks Club Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) 2023.

# Problem Description
The real estate market in Germany is dynamic and influenced by various factors such as location, property type, size, amenities, and economic conditions. Accurately predicting rental prices is crucial for both property owners and potential tenants to make informed decisions. In this context, developing a reliable machine learning model to predict housing rent prices in Germany becomes paramount.

The objective of this project is to build a predictive model that can estimate the monthly rent for residential properties in Germany based on selected features.
# Instructions

```
pip install -r requirements.txt
```

## Dataset
> CorrieBar. (2019, October). Apartment rental offers in Germany, Version 6. Retrieved October 28, 2023 from https://www.kaggle.com/datasets/corrieaar/apartment-rental-offers-in-germany

To download the dataset follow the instructions on https://www.kaggle.com/docs/api

```
kaggle datasets download -d corrieaar/apartment-rental-offers-in-germany
unzip apartment-rental-offers-in-germany.zip
```

## Explore Data with Notebook

Open the `housing-eda.ipynb` notebook.

## Run Model Training Script

```
python scripts/train.py
```

## Test Model Prediction Script

```
python scripts/predict.py
```

## Run App

```
python flask app/flask_app.py
```

```
streamlit run app/streamlit_app.py
```

## Run App with Docker

```
docker build -t model_server .
docker run -p 5000:5000 -p 8501:8501 model_server
```

Visit the live app at [housing-germany.streamlit.app](https://www.streamlit.io)
