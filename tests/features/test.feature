Feature: XML is parsed

  Scenario: Test xml is parsed
    Given App is launched
    When xml file is present in the input folder
    Then xml parser parses the file
