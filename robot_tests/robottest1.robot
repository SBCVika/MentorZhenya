*** Settings ***
Library    ../src/Keywords.py
Library    Collections
Test Setup    Initialization
Test Teardown    Cleanup

*** Variables ***
${GLOBAL_VAR} =    ${0}

*** Keywords ***
Initialization
    Start ECU

Cleanup
    Stop ECU

*** Test Cases ***
Test Data Not Available
    [Tags]    Performance    OneECU
    ${data}=  read data from ecu
    should be empty    ${data}

Test ECU Data Availability
    [Tags]    OneECU
    Sleep    3
    ${data}=  read data from ecu
    ${x}=  Get From List    ${data}    ${0}
    Should Be Equal    ${13}    ${x}

