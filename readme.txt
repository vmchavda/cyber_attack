#run to project
#download project
#run requirement.txt
pip install -r requirements.txt
# run test cases in cmd
pytest -s -v TestCases\test_validation.py --soft-asserts --html=report.html --alluredir=reports --verbose --capture sys -rF
pytest -s -v TestCases\test_validation.py --soft-asserts

#folders Pages/TestCases/pytest.ini  - you can change setting in pytest.ini file

