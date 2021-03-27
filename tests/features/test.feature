Feature: XML is parsed

  Scenario Outline: Test xml is parsed
    Given following paths
      | input_path | output_path |
      |    Desktop/test_files   |  Desktop/test_output_files |
    When App is launched
    Then xml parser parses the file and generates <output_file>
    Examples: input vs output
    |input_file| output_file |
    | test_file.xml  | reportFile_test_file.csv |


