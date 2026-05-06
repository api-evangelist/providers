---
aid: rite-aid
name: Rite Aid
description: Rite Aid is one of the nation's leading drugstore chains, providing prescription drugs, health and beauty aids, and convenience items. Rite Aid supports vendor integrations through EDI (Electronic Data Interchange) and B2B services, and offers digital health tools including an AI health assistant, pharmacy services, vaccination record management, and preventive health screening programs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - EDI
  - Fortune 500
  - Health
  - Pharmacy
  - Prescriptions
  - Retail
url: https://raw.githubusercontent.com/api-evangelist/rite-aid/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: rite-aid:edi-integration
    name: Rite Aid EDI Integration
    description: Rite Aid supports Electronic Data Interchange (EDI) for vendor integration using ANSI/ASC X12 standards (versions 4010 and 5010). Supported transactions include purchase orders (850), invoices (810), advance ship notices (856), and other supply chain documents. Integration is managed through the OpenText Trading Grid platform.
    humanURL: https://www.riteaidediservices.com/
    tags:
      - B2B Integration
      - EDI
      - Supply Chain
      - Vendor
    properties:
      - type: Documentation
        url: https://www.riteaidediservices.com/transaction-guidelines/edi-standards-versions-transactions/
      - type: Portal
        url: https://raportal.riteaid.com/
  - aid: rite-aid:digital-health
    name: Rite Aid Digital Health Services
    description: Rite Aid's digital health platform includes an AI health assistant for informational health queries, pharmacy services with prescription transfer and records management, vaccination record access, and preventive health blood testing programs available at 2,000+ locations.
    humanURL: https://riteaid.com/
    tags:
      - AI Health Assistant
      - Digital Health
      - Pharmacy
      - Preventive Health
      - Vaccinations
    properties:
      - type: Website
        url: https://riteaid.com/
      - type: MobileApp
        url: https://riteaid.com/app
common:
  - type: Website
    url: https://www.rite-aid.com
  - type: EDIPortal
    url: https://raportal.riteaid.com/
  - type: EDIServices
    url: https://www.riteaidediservices.com/
  - type: MobileApp
    url: https://riteaid.com/app
  - type: PrivacyPolicy
    url: https://www.riteaid.com/privacy-policy
  - type: TermsOfService
    url: https://www.riteaid.com/terms-of-use
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/rite-aid/refs/heads/main/json-schema/rite-aid-edi-transaction-schema.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/rite-aid/refs/heads/main/json-ld/rite-aid-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/rite-aid/refs/heads/main/vocabulary/rite-aid-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
