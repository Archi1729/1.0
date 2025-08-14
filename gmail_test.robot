*** Settings ***
Documentation     Test Gmail website using Robot Framework
Library           SeleniumLibrary

*** Variables ***
${GMAIL_URL}      https://gmail.com
${BROWSER}        chrome

*** Test Cases ***
Open Gmail Website
    [Documentation]    Open Gmail website and verify it loads
    Open Browser    ${GMAIL_URL}    ${BROWSER}
    Title Should Be    Gmail
    Page Should Contain    Gmail
    Close Browser

*** Keywords ***
Verify Gmail Page Loaded
    [Documentation]    Verify that Gmail page has loaded correctly
    Wait Until Page Contains    Gmail    timeout=10s
    Page Should Contain Element    id=identifierId
