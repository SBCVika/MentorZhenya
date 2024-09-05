*** Settings ***
Library    ../src/Keywords.py
Library    Collections
Test Setup    Initialization
Test Teardown    Cleanup

*** Variables ***
${CHANNEL} =   1
${BUS}     =   CAN
${MESSAGE} =   msg_OperationTime
${SIGNAL} =    Seconds

*** Keywords ***
Initialization
    Start Ecu Canoe

Cleanup
    Stop Ecu Canoe



*** Test Cases ***
Test Seconds
    ${value1}=  Read Signal Value From ECU   CAN    1    msg_OperationTime    Seconds
    Log    First signal value: ${value1}
    Sleep    3
    ${value2}=  Read Signal Value From ECU   CAN    1    msg_OperationTime    Seconds
    Log    First signal value: ${value2}
    Should Not Be Equal    ${value1}    ${value2}