# API keys
Get your keys at https://stepik.org/oauth2/applications/
(client type = confidential, authorization grant type = client credentials)


``./examples/exteranal-reports/library/api_keys.py``

# Usage 

## Item Report
To start flask app

    cd ./examples/extrenal-reports/
    python app.py
 
Site will be available by ``*local-ip*:5000``
or ``127.0.0.1:5000``

**Note:** To change your course id:
replace *111634* in app.py with *course_id*

``contest_table = itr.ContestTable(111634)``
