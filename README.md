# pytest-ui-bdd
pytest-ui-bdd

# Prepare environment
1. set-up python3

2. set-up pipenv with ***pip install pipenv***

3. set-up Pipfile dependencies on new environment with ***pipenv install Pipfile***

4. Activate envi with following command ***pipenv shell***
 

    
# Run Tests  

***Hint***: To run tests in headless mode disable '--headless' in run_tests.py file

1.To run all test cases  ***Ex: python run_tests.py --browser chrome --tag all***

2.To run all positive test cases  ***Ex: python run_tests.py --browser chrome --tag positive***

3.To run all negative test cases  ***Ex: python run_tests.py --browser chrome --tag negative***

# Reports Location

Reports will be available at '/html_reports/' folder
Sample Report is here:
![img_1.png](img_1.png)