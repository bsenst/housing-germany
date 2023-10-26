# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Flask app files to the container
COPY flask_app.py /app/
COPY model.pkl /app/

# Install necessary packages
RUN pip install flask scikit-learn pandas

# Expose the port the app runs on
EXPOSE 5000

# Define environment variable
ENV FLASK_APP flask_app.py

# Command to run the Flask app
CMD ["flask", "run", "--host", "0.0.0.0"]

# Install Streamlit
RUN pip install streamlit

# Copy the Streamlit app files to the container
COPY streamlit_app.py /app/

# Expose the port for Streamlit
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "streamlit_app.py"]
