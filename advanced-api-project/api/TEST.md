Testing Strategy
The goal of our test suite is to verify the correctness, reliability, and security of the API endpoints in the advanced_api_project, especially those related to the Book model.
We focused on:

CRUD Functionality – Ensuring that Create, Read, Update, and Delete actions work as expected.
Permissions – Validating that only authenticated users can create, update, or delete books.
Data Integrity – Verifying correct serialization and validation of data.
Filtering, Searching & Ordering – Ensuring these advanced query capabilities behave as expected.
HTTP Status Codes – Confirming each endpoint returns the correct status code for each scenario.

----How to Run the Tests---
Make sure your environment is set up:
Django is installed.
The api app is added in INSTALLED_APPS.
Migrations have been applied.
Then, run the test suite with:
python manage.py test api

---This command will----
Use Django's test runner.
Create a temporary test database (your real data is unaffected).
Execute all test cases defined in /api/test_views.py.

---How to Interpret Test Results----
After running the test command, you’ll see output like this:
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..........

---

Ran 10 tests in 1.234s

OK
. → Each dot represents a passed test.
F → Indicates a failed test.
E → Indicates an error in the test setup or logic.
If any test fails, Django will output a traceback showing:
The test name that failed.
The line where the error occurred.
The expected vs. actual result.
