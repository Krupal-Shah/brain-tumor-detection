# brain-tumor-detection
A machine learning model to detect brain tumors

### To build the mode
1. Run the `brain-tumor.ipynb` script

### To run the docker image locally:
1. Build docker image:
    $ docker build —t image_name .

2. Run docker container:
    $ docker run --name container_name -p 8000:8000 image_name

3. Output will contain
    INFO: Uvicorn running on http://0.0.0.0:8000
        - use this url in chrome to see the model frontend
        - use for testing the model

4. Query Model

    4.1 Via Web Interface (Chrome):
        http://0.0.0.0:8000/docs -> test model

    4.2 Via API (Postman):
        POST http://0.0.0.0:8000/predict
    
    4.3 Via API (Python):
        client.py

    4.4 Via curl request
        curl -X 'POST' "http://0.0.0.0:8000/predict" -H "accept/application/json" -H "Content-Type: application/json" -d '{"image_path":"path_to_image"}'
