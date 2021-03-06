"""Parameters for reading and validating Excel data.

`excel_config` is used to find and read Excel data in a workbook.
`valid_header` is a schema to validate the imported Excel data.

`output_header` are the headers for the exported Excel data.
"""

excel_config = {
    ".xlsb": {
        "engine": "pyxlsb",
        "header": [2, 3],
        "sheet_name": 1,
    },
    ".xlsx": {
        "engine": None,
        "header": [2, 3],
        "sheet_name": 0,
    }
}

valid_header = [("Unnamed: 0_level_0", "ID HAZOP Case"),
                ("Deviation", "HAZOPNode"),
                ("Deviation", "Parameter"),
                ("Deviation", "Guideword"),
                ("Deviation", "Description"),
                ("Cause", "HAZOPNode"),
                ("Cause", "Parameter"),
                ("Cause", "Guideword"),
                ("Cause", "Description"),
                ("Consequence", "HAZOPNode"),
                ("Consequence", "Parameter"),
                ("Consequence", "Guideword"),
                ("Consequence", "Description"),
                ("Risk Graph", "Severity"),
                ("VDI/VDE 2180-1:2019", "Frequency of Presence "),
                ("VDI/VDE 2180-1:2019", "Possibility of avoiding"),
                ("VDI/VDE 2180-1:2019", "Probability"),
                ("Safeguard", "HAZOPNode"),
                ("Safeguard", "Description"),
                ("Safeguard", "Recommendation"),
                ("Safeguard", "Recommendation.1"),
                ("Risk Graph", "Severity.1"),
                ("Risk Graph", "Frequency of Presence "),
                ("Risk Graph", "Possibility of avoiding"),
                ("Risk Graph", "Probability")]

output_header = [("", "HAZOP Case ID"),
                 ("Deviation", "HAZOPNode"),
                 ("Deviation", "Parameter"),
                 ("Deviation", "Guideword"),
                 ("Deviation", "Description"),
                 ("Cause", "HAZOPNode"),
                 ("Cause", "Parameter"),
                 ("Cause", "Guideword"),
                 ("Cause", "Description"),
                 ("Consequence", "HAZOPNode"),
                 ("Consequence", "Parameter"),
                 ("Consequence", "Guideword"),
                 ("Consequence", "Description"),
                 ("Risk Graph", "Severity"),
                 ("Risk Graph", "Frequency of presence"),
                 ("Risk Graph", "Possibility of avoiding"),
                 ("Risk Graph", "Probability"),
                 ("Safeguard", "HAZOPNode"),
                 ("Safeguard", "Description"),
                 ("Safeguard", "Recommendation"),
                 ("Safeguard", "Other info"),
                 ("Risk Graph", "Severity"),
                 ("Risk Graph", "Frequency of presence"),
                 ("Risk Graph", "Possibility of avoiding"),
                 ("Risk Graph", "Probability")]
