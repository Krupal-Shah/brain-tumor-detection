FROM python:3.10.11

# Set the working directory
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copy the current directory contents into the container at /code
COPY ./app /code/app
COPY ./model /code/model
COPY ./utils /code/utils

# Expose port
EXPOSE 8000

# Run the application
CMD [ "uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000" ]