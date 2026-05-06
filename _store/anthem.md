---
name: Anthem
description: Anthem, Inc. (now operating as Elevance Health) is one of the largest health benefits companies in the United States, serving members through affiliated Blue Cross and Blue Shield health plans across multiple states including California, New York, Virginia, Georgia, and others. Anthem provides health insurance, pharmacy benefits, and behavioral health services to over 40 million members. Under CMS interoperability rules (CMS-9115-F), Anthem offers FHIR- based Patient Access and Provider Directory APIs.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/anthem/refs/heads/main/apis.yml
created: '2026-03-23'
modified: '2026-04-19'
specificationVersion: '0.16'
tags:
  - Blue Cross Blue Shield
  - FHIR
  - Health Benefits
  - Health Insurance
  - Healthcare
  - Interoperability
apis:
  - name: Anthem Patient Access API
    description: The Anthem Patient Access API provides members access to their personal health data via HL7 FHIR R4, as required by the CMS Interoperability and Patient Access Final Rule (CMS-9115-F). Members can authorize third-party apps to access their claims, clinical information, formulary data, and coverage details. Implements SMART on FHIR for authorization.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.anthem.com/developer/
    baseURL: https://fhir.anthem.com/r4/
    tags:
      - FHIR
      - Health Insurance
      - Healthcare
      - Interoperability
      - Patient Access
      - SMART on FHIR
    properties:
      - type: Documentation
        url: https://www.anthem.com/developer/
      - type: Authentication
        url: https://www.anthem.com/developer/authentication/
    contact:
      - FN: Anthem Developer Support
        url: https://www.anthem.com/developer/
  - name: Anthem Provider Directory API
    description: The Anthem Provider Directory API provides public access to provider directory information via HL7 FHIR R4, as required by CMS interoperability rules. Supports searching for in-network providers, facilities, and insurance plans. No authentication required for public directory access.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.anthem.com/developer/
    baseURL: https://fhir.anthem.com/r4/
    tags:
      - FHIR
      - Healthcare
      - Interoperability
      - Provider Directory
    properties:
      - type: Documentation
        url: https://www.anthem.com/developer/
    contact:
      - FN: Anthem Developer Support
        url: https://www.anthem.com/developer/
  - name: Anthem Drug Formulary API
    description: The Anthem Drug Formulary API provides access to prescription drug formulary data via HL7 FHIR R4, including covered medications, cost tiers, prior authorization requirements, and quantity limits for Anthem health plan formularies.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.anthem.com/developer/
    baseURL: https://fhir.anthem.com/r4/
    tags:
      - Drug Formulary
      - FHIR
      - Healthcare
      - Pharmacy
    properties:
      - type: Documentation
        url: https://www.anthem.com/developer/
    contact:
      - FN: Anthem Developer Support
        url: https://www.anthem.com/developer/
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
    X: apievangelist
    url: https://apievangelist.com
common:
  - type: Portal
    url: https://www.anthem.com
  - type: SignUp
    url: https://www.anthem.com/developer/register/
  - type: TermsOfService
    url: https://www.anthem.com/legal/terms-and-conditions/
  - type: PrivacyPolicy
    url: https://www.anthem.com/legal/privacy-policy/
  - type: Features
    data:
      - name: FHIR R4 Compliance
        description: All Anthem interoperability APIs implement HL7 FHIR Release 4 standards with USCDI-conformant resource profiles.
      - name: SMART on FHIR Authorization
        description: Patient Access APIs use SMART on FHIR for secure OAuth2-based authorization allowing members to grant third-party app access.
      - name: Claims and Clinical Data
        description: Members can access their claims history, clinical notes, lab results, immunizations, and medication history through the Patient Access API.
      - name: Provider Directory Search
        description: Search for in-network providers by specialty, location, name, and plan type through the public Provider Directory API.
  - type: UseCases
    data:
      - name: Member Health Apps
        description: Enable member-authorized third-party health apps to aggregate claims, clinical, and formulary data from Anthem plans.
      - name: Care Coordination
        description: Allow care coordinators and providers to access member health history with member authorization for improved care transitions.
      - name: Provider Lookup
        description: Enable applications to search Anthem's provider directory for in-network physicians, hospitals, and specialists.
  - type: Integrations
    data:
      - name: CommonWell Health Alliance
        description: Anthem participates in the CommonWell Health Alliance for cross-organizational clinical data exchange.
      - name: Carequality Framework
        description: Anthem participates in the Carequality interoperability framework for health data exchange between networks.
---
