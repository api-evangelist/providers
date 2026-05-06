---
aid: department-of-veterans-affairs
name: Department of Veterans Affairs (VA)
description: The Department of Veterans Affairs (VA) provides health care, benefits, and memorial services to U.S. military Veterans and their families. The VA API Platform at developer.va.gov publishes a structured catalog of APIs spanning Veteran identity confirmation, benefits claims, appeals, document intake, education, loan guaranty, facilities, forms, and HL7 FHIR clinical health data.
url: https://raw.githubusercontent.com/api-evangelist/department-of-veterans-affairs/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/apis-json.png
created: '2024-01-01'
modified: '2026-04-28'
type: Index
position: Consuming
access: 3rd-Party
specificationVersion: '0.20'
tags:
  - Federal Government
  - Healthcare
  - Veterans
common:
  - url: https://developer.va.gov/
    type: Portal
  - url: https://developer.va.gov/support/faq
    type: FAQ
  - url: https://developer.va.gov/support/contact-us
    type: Support
  - url: https://developer.va.gov/onboarding
    type: Onboarding
apis:
  - aid: department-of-veterans-affairs:va-facilities-api
    name: VA Facilities API
    description: Search and retrieve VA medical facilities, benefits offices, vet centers, and cemeteries by location, service, or identifier.
    humanURL: https://developer.va.gov/explore/api/va-facilities
    baseURL: https://api.va.gov/services/va_facilities/v1
    tags:
      - Facilities
      - Health
      - Benefits
    properties:
      - type: Documentation
        url: https://developer.va.gov/explore/api/va-facilities
      - type: OpenAPI
        url: openapi/va-facilities-api-openapi.yml
      - type: JSONSchema
        url: json-schema/va-facility-schema.json
      - type: Example
        url: examples/facility-example.json
      - type: Sandbox
        url: https://developer.va.gov/explore/api/va-facilities/sandbox-access
      - type: ChangeLog
        url: https://developer.va.gov/explore/api/va-facilities/release-notes
  - aid: department-of-veterans-affairs:va-forms-api
    name: VA Forms API
    description: Programmatic catalog of official VA forms with current PDF URLs and revision metadata.
    humanURL: https://developer.va.gov/explore/api/va-forms
    baseURL: https://api.va.gov/services/va_forms/v0
    tags:
      - Forms
    properties:
      - type: Documentation
        url: https://developer.va.gov/explore/api/va-forms
      - type: OpenAPI
        url: openapi/va-forms-api-openapi.yml
      - type: JSONSchema
        url: json-schema/va-form-schema.json
      - type: Example
        url: examples/form-example.json
      - type: Sandbox
        url: https://developer.va.gov/explore/api/va-forms/sandbox-access
      - type: ChangeLog
        url: https://developer.va.gov/explore/api/va-forms/release-notes
  - aid: department-of-veterans-affairs:va-benefits-claims-api
    name: VA Benefits Claims API
    description: Submit and track VA benefits claims (Form 526), intent-to-file notices, and Power of Attorney records.
    humanURL: https://developer.va.gov/explore/api/benefits-claims
    baseURL: https://api.va.gov/services/claims/v2
    tags:
      - Benefits
      - Claims
    properties:
      - type: Documentation
        url: https://developer.va.gov/explore/api/benefits-claims
      - type: OpenAPI
        url: openapi/va-benefits-claims-api-openapi.yml
      - type: JSONSchema
        url: json-schema/va-claim-schema.json
      - type: Example
        url: examples/claim-example.json
      - type: Authentication
        url: https://developer.va.gov/explore/api/benefits-claims/authorization-code
      - type: Sandbox
        url: https://developer.va.gov/explore/api/benefits-claims/sandbox-access
      - type: ChangeLog
        url: https://developer.va.gov/explore/api/benefits-claims/release-notes
  - aid: department-of-veterans-affairs:va-benefits-intake-api
    name: VA Benefits Intake API
    description: Submit and track PDF documents for benefits applications via a guided upload workflow.
    humanURL: https://developer.va.gov/explore/api/benefits-intake
    baseURL: https://api.va.gov/services/vba_documents/v1
    tags:
      - Benefits
      - Intake
      - Documents
    properties:
      - type: Documentation
        url: https://developer.va.gov/explore/api/benefits-intake
      - type: OpenAPI
        url: openapi/va-benefits-intake-api-openapi.yml
      - type: Sandbox
        url: https://developer.va.gov/explore/api/benefits-intake/sandbox-access
      - type: ChangeLog
        url: https://developer.va.gov/explore/api/benefits-intake/release-notes
  - aid: department-of-veterans-affairs:va-appeals-status-api
    name: VA Appeals Status API
    description: Retrieve the status, events, and issues of a Veteran's appeals, supplemental claims, and higher-level reviews.
    humanURL: https://developer.va.gov/explore/api/appeals-status
    baseURL: https://api.va.gov/services/appeals/v1
    tags:
      - Appeals
      - Status
    properties:
      - type: Documentation
        url: https://developer.va.gov/explore/api/appeals-status
      - type: OpenAPI
        url: openapi/va-appeals-status-api-openapi.yml
      - type: JSONSchema
        url: json-schema/va-appeal-schema.json
      - type: ChangeLog
        url: https://developer.va.gov/explore/api/appeals-status/release-notes
  - aid: department-of-veterans-affairs:va-clinical-health-fhir-api
    name: VA Clinical Health API (FHIR)
    description: Read HL7 FHIR R4 clinical resources for a Veteran via SMART-on-FHIR authorization.
    humanURL: https://developer.va.gov/explore/api/clinical-health
    baseURL: https://api.va.gov/services/fhir/v0/r4
    tags:
      - Health
      - FHIR
      - Clinical
    properties:
      - type: Documentation
        url: https://developer.va.gov/explore/api/clinical-health
      - type: OpenAPI
        url: openapi/va-clinical-health-fhir-api-openapi.yml
      - type: ChangeLog
        url: https://developer.va.gov/explore/api/clinical-health/release-notes
  - aid: department-of-veterans-affairs:va-veteran-confirmation-api
    name: VA Veteran Confirmation API
    description: Confirm a person's Veteran status given basic identifying information.
    humanURL: https://developer.va.gov/explore/api/veteran-confirmation
    baseURL: https://api.va.gov/services/veteran_confirmation/v1
    tags:
      - Verification
      - Identity
    properties:
      - type: Documentation
        url: https://developer.va.gov/explore/api/veteran-confirmation
      - type: OpenAPI
        url: openapi/va-veteran-confirmation-api-openapi.yml
      - type: JSONSchema
        url: json-schema/va-veteran-confirmation-schema.json
      - type: Sandbox
        url: https://developer.va.gov/explore/api/veteran-confirmation/sandbox-access
      - type: ChangeLog
        url: https://developer.va.gov/explore/api/veteran-confirmation/release-notes
  - aid: department-of-veterans-affairs:va-address-validation-api
    name: VA Address Validation API
    description: Verify and standardize U.S. and international addresses for Veterans and their families.
    humanURL: https://developer.va.gov/explore/api/address-validation
    tags:
      - Address
      - Validation
    properties:
      - type: Documentation
        url: https://developer.va.gov/explore/api/address-validation
      - type: Sandbox
        url: https://developer.va.gov/explore/api/address-validation/sandbox-access
      - type: ChangeLog
        url: https://developer.va.gov/explore/api/address-validation/release-notes
  - aid: department-of-veterans-affairs:va-benefits-documents-api
    name: VA Benefits Documents API
    description: Retrieve VA-generated benefit documents (decision letters, award letters, certifications) for Veterans.
    humanURL: https://developer.va.gov/explore/api/benefits-documents
    tags:
      - Benefits
      - Documents
    properties:
      - type: Documentation
        url: https://developer.va.gov/explore/api/benefits-documents
      - type: ChangeLog
        url: https://developer.va.gov/explore/api/benefits-documents/release-notes
  - aid: department-of-veterans-affairs:va-benefits-reference-data-api
    name: VA Benefits Reference Data API
    description: Reference data lookups for benefits-claim form fields (countries, states, disabilities, treatment centers, etc.).
    humanURL: https://developer.va.gov/explore/api/benefits-reference-data
    tags:
      - Reference Data
      - Benefits
    properties:
      - type: Documentation
        url: https://developer.va.gov/explore/api/benefits-reference-data
      - type: ChangeLog
        url: https://developer.va.gov/explore/api/benefits-reference-data/release-notes
  - aid: department-of-veterans-affairs:va-community-care-eligibility-api
    name: VA Community Care Eligibility API
    description: Determine whether a Veteran is eligible for community-care services under VA referral programs.
    humanURL: https://developer.va.gov/explore/api/community-care-eligibility
    tags:
      - Health
      - Eligibility
    properties:
      - type: Documentation
        url: https://developer.va.gov/explore/api/community-care-eligibility
      - type: ChangeLog
        url: https://developer.va.gov/explore/api/community-care-eligibility/release-notes
  - aid: department-of-veterans-affairs:va-decision-reviews-api
    name: VA Decision Reviews API
    description: Submit supplemental claims, higher-level reviews, and Notices of Disagreement under appeals modernization.
    humanURL: https://developer.va.gov/explore/api/decision-reviews
    tags:
      - Appeals
      - Decision Reviews
    properties:
      - type: Documentation
        url: https://developer.va.gov/explore/api/decision-reviews
      - type: ChangeLog
        url: https://developer.va.gov/explore/api/decision-reviews/release-notes
  - aid: department-of-veterans-affairs:va-direct-deposit-management-api
    name: VA Direct Deposit Management API
    description: Read and update a Veteran's direct-deposit information for benefit payments.
    humanURL: https://developer.va.gov/explore/api/direct-deposit-management
    tags:
      - Payments
      - Direct Deposit
    properties:
      - type: Documentation
        url: https://developer.va.gov/explore/api/direct-deposit-management
      - type: ChangeLog
        url: https://developer.va.gov/explore/api/direct-deposit-management/release-notes
  - aid: department-of-veterans-affairs:va-education-benefits-api
    name: VA Education Benefits API
    description: Submit and track GI Bill and VA education benefit applications and entitlement data.
    humanURL: https://developer.va.gov/explore/api/education-benefits
    tags:
      - Education
      - Benefits
    properties:
      - type: Documentation
        url: https://developer.va.gov/explore/api/education-benefits
      - type: ChangeLog
        url: https://developer.va.gov/explore/api/education-benefits/release-notes
  - aid: department-of-veterans-affairs:va-loan-guaranty-api
    name: VA Loan Guaranty API
    description: Access VA-guaranteed home-loan eligibility, certificates of eligibility (COE), and loan data.
    humanURL: https://developer.va.gov/explore/api/loan-guaranty
    tags:
      - Loans
      - Loan Guaranty
    properties:
      - type: Documentation
        url: https://developer.va.gov/explore/api/loan-guaranty
      - type: ChangeLog
        url: https://developer.va.gov/explore/api/loan-guaranty/release-notes
  - aid: department-of-veterans-affairs:va-loan-review-api
    name: VA Loan Review API
    description: Lender-facing API for review, conditions, and modification of VA-guaranteed home loans.
    humanURL: https://developer.va.gov/explore/api/loan-review
    tags:
      - Loans
      - Review
    properties:
      - type: Documentation
        url: https://developer.va.gov/explore/api/loan-review
      - type: ChangeLog
        url: https://developer.va.gov/explore/api/loan-review/release-notes
  - aid: department-of-veterans-affairs:va-guaranty-remittance-api
    name: VA Guaranty Remittance API
    description: Submit and track guaranty remittance payments for VA-guaranteed loans.
    humanURL: https://developer.va.gov/explore/api/guaranty-remittance
    tags:
      - Loans
      - Payments
    properties:
      - type: Documentation
        url: https://developer.va.gov/explore/api/guaranty-remittance
      - type: ChangeLog
        url: https://developer.va.gov/explore/api/guaranty-remittance/release-notes
  - aid: department-of-veterans-affairs:va-letter-generator-api
    name: VA Letter Generator API
    description: Generate official VA letters (e.g. service verification, benefit summary) on demand.
    humanURL: https://developer.va.gov/explore/api/va-letter-generator
    tags:
      - Letters
    properties:
      - type: Documentation
        url: https://developer.va.gov/explore/api/va-letter-generator
      - type: ChangeLog
        url: https://developer.va.gov/explore/api/va-letter-generator/release-notes
  - aid: department-of-veterans-affairs:va-patient-health-fhir-api
    name: VA Patient Health API (FHIR)
    description: Veteran-authorized SMART-on-FHIR API exposing the patient's own health record.
    humanURL: https://developer.va.gov/explore/api/patient-health
    tags:
      - Health
      - FHIR
      - Patient
    properties:
      - type: Documentation
        url: https://developer.va.gov/explore/api/patient-health
      - type: ChangeLog
        url: https://developer.va.gov/explore/api/patient-health/release-notes
  - aid: department-of-veterans-affairs:va-veteran-service-history-and-eligibility-api
    name: VA Veteran Service History and Eligibility API
    description: Retrieve a Veteran's service history and eligibility for VA programs.
    humanURL: https://developer.va.gov/explore/api/veteran-service-history-and-eligibility
    tags:
      - Service History
      - Eligibility
    properties:
      - type: Documentation
        url: https://developer.va.gov/explore/api/veteran-service-history-and-eligibility
      - type: ChangeLog
        url: https://developer.va.gov/explore/api/veteran-service-history-and-eligibility/release-notes
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
