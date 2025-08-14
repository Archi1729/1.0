*** Settings ***
Documentation     Comprehensive web automation demo using Robot Framework
Library           SeleniumLibrary
Suite Setup       Log    Starting Web Automation Demo
Suite Teardown    Log    Completed Web Automation Demo

*** Variables ***
${GMAIL_URL}      https://gmail.com
${GOOGLE_URL}     https://google.com
${BROWSER}        chrome

*** Test Cases ***
Test Gmail Website With Selenium
    [Documentation]    Test Gmail using Selenium WebDriver
    [Tags]    selenium    gmail
    Open Browser    ${GMAIL_URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be    Gmail
    Page Should Contain    Gmail
    Wait Until Page Contains Element    id=identifierId    timeout=10s
    Close Browser

Test Google Website With Selenium
    [Documentation]    Test Google using Selenium WebDriver
    [Tags]    selenium    google
    Open Browser    ${GOOGLE_URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be    Google
    Page Should Contain Element    name=q
    Close Browser

*** Keywords ***
Navigate To Website
    [Arguments]    ${url}    ${expected_title}
    [Documentation]    Navigate to a website and verify title
    Go To    ${url}
    Title Should Be    ${expected_title}
    Log    Successfully navigated to ${url}

Verify Page Elements
    [Arguments]    ${element_selector}
    [Documentation]    Verify that specific elements are present on page
    Wait Until Page Contains Element    ${element_selector}    timeout=10s
    Page Should Contain Element    ${element_selector}
    Log    Element ${element_selector} found on page
