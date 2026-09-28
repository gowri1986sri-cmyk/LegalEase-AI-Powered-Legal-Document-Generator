# PHASE 6 – PROJECT TESTING

## Project Title

LegalEaseAI – AI-Powered Legal Document Generator

## 1. Introduction

Testing is an important phase of the LegalEaseAI project.

The main purpose of testing is to verify that the application works correctly and produces the expected output.

## 2. Testing Objectives

1. Verify that the application starts correctly.
2. Verify that the home page loads properly.
3. Verify that user inputs are accepted.
4. Verify that required fields are validated.
5. Verify that the Generate button works correctly.
6. Verify that the legal document is generated.
7. Verify that the result page displays correctly.
8. Verify that the document can be downloaded.
9. Verify that invalid inputs are handled properly.
10. Verify that API keys are protected.

## 3. Test Cases

| Test Case | Test Description | Expected Result | Status |
|---|---|---|---|
| TC01 | Start application | Application starts successfully | Pass |
| TC02 | Open home page | Home page is displayed | Pass |
| TC03 | Select document type | Document type is accepted | Pass |
| TC04 | Enter party details | Details are accepted | Pass |
| TC05 | Enter terms and conditions | Terms are accepted | Pass |
| TC06 | Enter effective date | Date is accepted | Pass |
| TC07 | Submit empty fields | Validation is displayed | Pass |
| TC08 | Click Generate | Document generation starts | Pass |
| TC09 | Display generated document | Document is displayed | Pass |
| TC10 | Download document | Document is downloaded | Pass |
| TC11 | Create another document | Home page opens | Pass |
| TC12 | API key unavailable | Demo document is generated | Pass |

## 4. Functional Testing

The following features were tested:

- Home page
- Document type selection
- User input
- Input validation
- AI document generation
- Result display
- Document download
- Create another document

## 5. Input Validation

The application checks whether required fields are completed before generating the document.

If a required field is empty, the form cannot be submitted.

## 6. AI Integration Testing

The system prepares an AI prompt using:

- Document type
- Parties involved
- Terms and conditions
- Effective date

The generated response is displayed on the result page.

If the AI API is unavailable, the application generates a demo document.

## 7. User Interface Testing

The following were tested:

- Page loading
- Input fields
- Buttons
- Result page
- Download option
- Navigation

## 8. Security Testing

The AI API key is stored using an environment variable.

The `.env` file should not be uploaded to GitHub.

## 9. Test Result

The major functionalities of LegalEaseAI were tested successfully.

The application can:

1. Accept user requirements.
2. Process the information.
3. Generate a legal document draft.
4. Display the generated document.
5. Download the generated document.

## 10. Conclusion

Testing confirms that the major components of the LegalEaseAI application work as expected.

The application is ready for the documentation and demonstration phases.

## 11. Legal Disclaimer

LegalEaseAI generates documents for educational and informational purposes.

The generated documents should be reviewed by a qualified legal professional before official use.