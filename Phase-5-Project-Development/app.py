print("LEGAL EASE - AI LEGAL DOCUMENT GENERATOR")

# DocumentRequest model
document_type = input("Enter document type: ")
parties = input("Enter parties involved: ")
terms = input("Enter terms and conditions: ")
date = input("Enter effective date: ")

# Generate document
document = f"""
--- GENERATED LEGAL DOCUMENT ---

Document Type:
{document_type}

Parties Involved:
{parties}

Terms and Conditions:
{terms}

Effective Date:
{date}

--- END OF DOCUMENT ---
"""

print(document)