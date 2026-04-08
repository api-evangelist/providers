---
aid: acord
url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/apis.yml
apis:
- aid: acord:acord-xml-standards-api
  name: ACORD XML Standards API
  tags:
  - ACORD
  - Claims
  - Insurance
  - Policy
  - Property Casualty
  - SOAP
  - XML
  image: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/image.png
  humanURL: https://www.acord.org/standards-architecture/acord-data-standards
  baseURL: https://claims.insurer-internal.example.com/acord
  properties:
  - url: https://www.acord.org/standards-architecture/acord-data-standards
    type: Documentation
  - url: https://www.acord.org/standards-architecture/acord-data-standards
    type: Reference
  description: ACORD XML Standards define data exchange formats for property & casualty, life, annuity, and reinsurance using SOAP/XML protocols. APIs enable claims inquiry, policy administration, and regulatory reporting across insurers, reinsurers, and intermediaries.
- aid: acord:acord-ngds-api
  name: ACORD Next-Generation Digital Standards (NGDS) API
  tags:
  - ACORD
  - Digital Standards
  - Insurance
  - IoT
  - JSON
  - Microservices
  - REST
  image: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/image.png
  humanURL: https://www.acord.org/standards-architecture/acord-data-standards/next-generation-digital-standards
  baseURL: https://api.insurer-internal.example.com/ngds
  properties:
  - url: https://www.acord.org/standards-architecture/acord-data-standards/next-generation-digital-standards
    type: Documentation
  - url: https://www.acord.org/standards-architecture/acord-data-standards/next-generation-digital-standards
    type: Reference
  - url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/openapi/acord-ngds-openapi.yml
    type: OpenAPI
  description: The ACORD Next-Generation Digital Standards (NGDS) Object Model provides granular, transaction-centric standards for APIs, microservices, IoT, and RESTful architectures. Based on JSON and YAML data-interchange formats, NGDS enables modern insurance data exchange for underwriting, policy management, and claims administration.
- aid: acord:acord-reinsurance-standards-api
  name: ACORD Reinsurance & Large Commercial Data Standards API
  tags:
  - Data Standards
  - Insurance
  - Large Commercial
  - Reinsurance
  - XML
  image: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/image.png
  humanURL: https://www.acord.org/standards-architecture/acord-data-standards/Global_Reinsurance_Data_Standards
  baseURL: https://reinsurance.insurer-internal.example.com/acord
  properties:
  - url: https://www.acord.org/standards-architecture/acord-data-standards/Global_Reinsurance_Data_Standards
    type: Documentation
  description: ACORD Global Reinsurance & Large Commercial Data Standards define XML data exchange formats for reinsurance and large commercial lines. APIs support facultative and treaty reinsurance transactions, placement, and settlement between cedants, reinsurers, and brokers.
name: Acord
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: ACORD is a global standards-setting body for the insurance industry, providing data standards, reference architecture, and digital tools that enable insurers, brokers, and software providers to exchange information.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

