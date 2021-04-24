Feature: XML is parsed

  Background: db is up
    Given db is up and running

  Scenario Outline: Test xml is parsed
    Given following paths input_path and output_path
      | input_path | output_path |
      | Desktop/test_files   | Desktop/test_output_files |
    When test xml <input_file> is created
    And App is launched
    Then xml parser parses the file and generates <output_file>
    Examples: input vs output
      |input_file| output_file |
      | 111.xml  | reportFile_111.csv |
      | 222.xml  | reportFile_222.csv |
      | 333.xml  | reportFile_333.csv |


  Scenario Outline: test db saving
    Given following paths input_path and output_path
      | input_path | output_path |
      | Desktop/test_files   | Desktop/test_output_files |
    When test xml <input_file> is created with following details: <name>, <lastname>, <id_type>, <id_value>
    And App is launched
    Then xml parser parses the file and generates <output_file>
    And data is saved in db
    Examples: data
    | input_file|output_file|name|lastname|id_type|id_value|
    | 444.xml | reportFile_444.csv | T |  EST | test | 123 |
    | 555.xml | reportFile_555.csv | Squirtle |  Poke | test | 123 |
    | 666.xml | reportFile_666.csv | Ti |  BEST | test1 | 999 |
