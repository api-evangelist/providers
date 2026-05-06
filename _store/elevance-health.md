---
aid: elevance-health
name: Elevance Health
url: https://raw.githubusercontent.com/api-evangelist/elevance-health/refs/heads/main/apis.yml
modified: '2026-04-28'
created: '2026-03-21'
specificationVersion: '0.19'
type: Index
position: Consuming
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Fortune 500
  - Healthcare
  - Health Insurance
  - FHIR
  - Interoperability
description: Elevance Health (formerly Anthem) is a Fortune 500 health benefits company that serves members through Blue Cross and Blue Shield affiliated health plans across multiple states. The company offers medical, pharmacy, dental, vision, and other specialty insurance and exposes a set of CMS Interoperability and Patient Access FHIR APIs to enable members, providers, and partner payers to securely exchange coverage, clinical, claims, provider directory, and formulary data.
apis:
  - aid: elevance-health:patient-access
    name: Elevance Health Patient Access API
    description: The Patient Access API enables Anthem and Elevance Health members to securely access and exchange their medical, pharmacy, dental, and vision claims and clinical data through third-party applications. Built on the HL7 FHIR R4 specification and aligned with the CARIN Consumer Directed Payer Data Exchange Implementation Guide, the API supports up to five years of historical claims and clinical data.
    humanURL: https://www.anthem.com/developers
    baseURL: https://patient360.anthem.com/P360Member/fhir
    tags:
      - FHIR
      - Healthcare
      - Health Insurance
      - Patient Access
      - Interoperability
    properties:
      - type: Documentation
        url: https://patient360c.anthem.com/P360Member/fhir/documentation
      - type: DeveloperPortal
        url: https://www.anthem.com/developers
  - aid: elevance-health:provider-directory
    name: Elevance Health Provider Directory API
    description: The Provider Directory API exposes Elevance Health network provider information including practitioners, practitioner roles, organizations, locations, and insurance plans. The API conforms to the HL7 FHIR R4 specification and the DaVinci PDEX Plan Net Implementation Guide and does not require authentication for public directory data.
    humanURL: https://www.anthem.com/developers
    tags:
      - FHIR
      - Provider Directory
      - Healthcare
      - Interoperability
    properties:
      - type: Documentation
        url: https://www.anthem.com/developers
  - aid: elevance-health:formulary
    name: Elevance Health Formulary API
    description: The Formulary API publishes Elevance Health drug coverage information including covered drug lists, tier placement, prior authorization requirements, and step therapy rules. The API conforms to the HL7 FHIR R4 specification and the DaVinci PDEX US Drug Formulary Implementation Guide.
    humanURL: https://www.anthem.com/developers
    tags:
      - FHIR
      - Formulary
      - Pharmacy
      - Healthcare
      - Interoperability
    properties:
      - type: Documentation
        url: https://www.anthem.com/developers
  - aid: elevance-health:payer-to-payer
    name: Elevance Health Payer to Payer API
    description: The Payer to Payer API enables Elevance Health to exchange member coverage and clinical data with other health plans when members move between payers, supporting the CMS Interoperability and Prior Authorization rule. The API is built on the HL7 FHIR R4 specification.
    humanURL: https://www.anthem.com/developers
    tags:
      - FHIR
      - Payer to Payer
      - Healthcare
      - Interoperability
    properties:
      - type: Documentation
        url: https://www.anthem.com/developers
common:
  - type: Website
    url: https://www.elevancehealth.com
  - type: DeveloperPortal
    url: https://www.anthem.com/developers
  - type: Documentation
    url: https://patient360c.anthem.com/P360Member/fhir/documentation
  - type: SignUp
    url: https://www.anthem.com/developers/request-anthem-io
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
