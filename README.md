# COMPOUND NOUNS CHALLENGE
The basic idea for my solution is to split the compound nouns into syllables, create a training set containing all permutations from the syllables together with their labels.
This training set is used to fine-tune a dilibert word model for German language that is used in the encoder and also in the decoder.
The last layer in the decoder is replaced by a linear layer that ouptuts logits with the shape of the labels (7 in our case).
To check the classification probability one can pass the logits to a softmax function.

## Inspect the development
It is recommended to use a virtual environment that comprises jupyter-lab or jupyter-notebook.
In the virtual environment you can install all necessary libraries by:
```bash
pip install -r requirements
```
All development steps are sequentially noted in Classify_ICD.ipynb.

## Run Unit Tests and API
In order to run the unit tests and the API you need a machine with docker and docker-compose installed.
The command to run the modules is:
```bash
docker-compose up --build
```
Now you can grab a cup of coffee and wait for the build to finish.
When everything is up and runnig your screen should show:
```bash
Attaching to mia_challenge-api-1, mia_challenge-test-1
mia_challenge-test-1  | ============================= test session starts ==============================
mia_challenge-test-1  | platform linux -- Python 3.10.4, pytest-7.1.2, pluggy-1.0.0 -- /usr/local/bin/python
mia_challenge-test-1  | cachedir: .pytest_cache
mia_challenge-test-1  | rootdir: /app
mia_challenge-test-1  | plugins: anyio-3.5.0
mia_challenge-test-1  | collecting ... collected 3 items
mia_challenge-test-1  | 
mia_challenge-test-1  | test_ap.py::test_version PASSED                                          [ 33%]
mia_challenge-test-1  | test_ap.py::test_known_item PASSED                                       [ 66%]
mia_challenge-test-1  | test_ap.py::test_unknown_item PASSED                                     [100%]
mia_challenge-test-1  | 
mia_challenge-test-1  | ============================== 3 passed in 24.57s ==============================
mia_challenge-test-1 exited with code 0
mia_challenge-api-1   | INFO:     Started server process [1]
mia_challenge-api-1   | INFO:     Waiting for application startup.
mia_challenge-api-1   | INFO:     Application startup complete.
mia_challenge-api-1   | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```
Now, you should be able to access the API via browser on http://localhost:8000/docs. If your docker is running on a remote machine, please replace localhost by that machines ip address.
