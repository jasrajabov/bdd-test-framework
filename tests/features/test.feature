Feature: XML is parsed

  Scenario Outline: Test xml is parsed
    Given following paths
      | input_path | output_path |
      |    Desktop/test_files   |  Desktop/test_output_files |

    When test xml <input_file> is created
    And App is launched
    Then xml parser parses the file and generates <output_file>
    Examples: input vs output
    |input_file| output_file |
    | 111.xml  | reportFile_111.csv |
    | 222.xml  | reportFile_222.csv |
    | 333.xml  | reportFile_333.csv |


