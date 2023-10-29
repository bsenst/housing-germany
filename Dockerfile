# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Flask app files to the container
COPY app/flask_app.py /app/
COPY assets/model.pkl /app/assets/

# Install necessary packages
RUN pip install flask scikit-learn==1.2.2 pandas

# Expose the port the app runs on
EXPOSE 5000

# Define environment variable
ENV FLASK_APP flask_app.py

# Install Streamlit
RUN pip install streamlit

# Copy the Streamlit app files to the container
COPY app/streamlit_app.py /app/

# Expose the port for Streamlit
EXPOSE 8501

CMD ["bash", "-c", "streamlit run streamlit_app.py & flask run --host=0.0.0.0 --port=5000"]
