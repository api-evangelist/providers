---
aid: aetna
url: https://raw.githubusercontent.com/api-evangelist/aetna/refs/heads/main/apis.yml
modified: '2026-04-19'
name: Aetna
description: Aetna, a CVS Health company, offers health insurance, dental, vision, and other plans for individuals, families, employers, health care providers, and insurance agents and brokers. As a major U.S. health insurer, Aetna provides federally mandated FHIR R4 APIs for patient access, provider directory, and drug formulary data under CMS Interoperability and Patient Access Final Rule (CMS-9115-F). Provider connectivity is supported through the Availity portal for EDI transactions.
tags:
  - Health Insurance
  - Healthcare
  - FHIR
  - Patient Access
  - Provider Directory
apis:
  - aid: aetna-patient-access-fhir-api
    name: Aetna Patient Access FHIR API
    description: FHIR R4 compliant Patient Access API providing members secure access to their health data including claims, clinical data, and coverage information. Required under CMS Interoperability and Patient Access Final Rule (CMS-9115-F). Supports SMART on FHIR authorization and provides access to ExplanationOfBenefit, Coverage, Patient, and related FHIR resources.
    tags:
      - FHIR
      - Patient Access
      - Health Data
      - Claims
      - CMS Mandate
    properties:
      - type: Documentation
        url: https://www.aetna.com/individuals-families/member-rights-resources/member-data-access.html
      - type: Authentication
        url: https://www.aetna.com/individuals-families/member-rights-resources/member-data-access.html
  - aid: aetna-provider-directory-fhir-api
    name: Aetna Provider Directory FHIR API
    description: FHIR R4 compliant Provider Directory API providing standardized access to in-network provider and facility information. Enables third-party applications to search for providers, verify network participation, and access provider details. Required under CMS Interoperability and Patient Access Final Rule for payer-to-payer data exchange.
    tags:
      - FHIR
      - Provider Directory
      - Network
      - Healthcare Providers
      - CMS Mandate
    properties:
      - type: Documentation
        url: https://www.aetna.com/health-care-professionals/working-with-aetna/provider-directory.html
  - aid: aetna-drug-formulary-fhir-api
    name: Aetna Drug Formulary FHIR API
    description: FHIR R4 compliant Drug Formulary API providing standardized access to plan formulary data including covered drugs, tiers, cost-sharing requirements, and prior authorization requirements. Implements the DaVinci PDEX Formulary Implementation Guide. Enables members and third-party applications to compare drug coverage across health plans.
    tags:
      - FHIR
      - Drug Formulary
      - Pharmacy
      - Medications
      - CMS Mandate
    properties:
      - type: Documentation
        url: https://www.aetna.com/individuals-families/member-rights-resources/member-data-access.html
  - aid: aetna-provider-edi-api
    name: Aetna Provider EDI API
    description: Electronic Data Interchange connectivity for healthcare providers enabling electronic submission of claims, eligibility verification, claim status inquiries, and remittance advice. Accessible through the Availity provider portal supporting EDI 837 (claims), 270/271 (eligibility), 276/277 (claim status), and 835 (remittance) HIPAA transactions.
    tags:
      - EDI
      - Claims
      - Eligibility
      - Provider Portal
      - HIPAA
    properties:
      - type: Documentation
        url: https://www.aetna.com/health-care-professionals/claims-payment/claims-submission.html
      - type: Portal
        url: https://www.availity.com
common:
  - type: Website
    url: https://www.aetna.com
  - type: Portal
    url: https://www.aetna.com/health-care-professionals.html
  - type: Login
    url: https://member.aetna.com
  - type: Support
    url: https://www.aetna.com/individuals-families/contact-aetna.html
  - type: PrivacyPolicy
    url: https://www.aetna.com/legal-notices/privacy.html
  - type: TermsOfService
    url: https://www.aetna.com/legal-notices/terms-of-use.html
  - type: Features
    data:
      - name: FHIR R4 Compliance
        description: All patient-facing APIs implement HL7 FHIR Release 4 standard for interoperability.
      - name: SMART on FHIR Authorization
        description: Secure OAuth 2.0 authorization framework for patient-authorized third-party app access.
      - name: CMS Interoperability Compliance
        description: Full compliance with CMS-9115-F Interoperability and Patient Access Final Rule.
      - name: EDI Transaction Support
        description: Complete HIPAA-compliant EDI transaction set for provider administrative workflows.
      - name: Payer-to-Payer Data Exchange
        description: Supports member-directed payer-to-payer data exchange for continuity of care.
      - name: DaVinci Implementation Guides
        description: Implements HL7 DaVinci Project PDEX, PDex Drug Formulary, and Plan Net guides.
  - type: UseCases
    data:
      - name: Member Health Record Access
        description: Members use SMART on FHIR apps to access their complete health records across providers.
      - name: Provider Network Verification
        description: Developers build directory search tools to help patients find in-network providers.
      - name: Drug Cost Comparison
        description: Applications use formulary API to compare medication costs across Aetna plans.
      - name: Electronic Claims Submission
        description: Healthcare providers submit claims electronically via EDI 837 transactions through Availity.
      - name: Eligibility Verification
        description: Providers verify member eligibility and benefits in real time using 270/271 EDI transactions.
      - name: Remittance Processing
        description: Providers receive and process electronic remittance advice via EDI 835 transactions.
  - type: Integrations
    data:
      - name: CVS Caremark
        description: Integrated pharmacy benefit management for prescription drug coverage and mail-order pharmacy.
      - name: Availity
        description: Primary provider portal for EDI transactions, eligibility, claims, and authorization requests.
      - name: Epic Payer Platform
        description: EHR integration enabling clinical workflows including prior authorization and care management.
      - name: Apple Health
        description: FHIR-based integration enabling Aetna members to view health data in Apple Health app.
      - name: CommonWell Health Alliance
        description: Interoperability network participation for cross-organization health data exchange.
      - name: CMS Blue Button 2.0
        description: Alignment with CMS Blue Button 2.0 FHIR API patterns for Medicare data access.
---
