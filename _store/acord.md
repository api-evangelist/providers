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
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/json-schema/ngds-policy-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/json-schema/ngds-claim-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/json-schema/ngds-party-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/json-schema/ngds-coverage-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/json-schema/ngds-underwriting-submission-schema.json
      - type: NaftikoCapability
        url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/capabilities/shared/acord-ngds.yaml
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
common:
  - url: https://www.acord.org
    type: Website
  - url: https://www.acord.org/standards-architecture/acord-data-standards
    type: Portal
  - url: https://www.acord.org/standards-architecture/acord-data-standards
    type: Documentation
  - url: https://www.acord.org/standards-architecture/acord-data-standards/next-generation-digital-standards
    type: GettingStarted
  - url: https://www.acord.org/standards-architecture/reference-architecture
    type: Documentation
  - url: https://www.acord.org/standards-architecture/get-involved/standards-project-advisory-groups
    type: Support
  - url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/openapi/acord-ngds-openapi.yml
    type: OpenAPI
  - url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/json-schema/acord-policy-schema.json
    type: JSONSchema
  - url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/json-schema/acord-claim-schema.json
    type: JSONSchema
  - url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/json-ld/acord-context.jsonld
    type: JSONLDContext
  - type: GitHubOrganization
    url: https://github.com/api-evangelist/acord
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/rules/acord-spectral-rules.yml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/capabilities/insurance-data-exchange.yaml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/vocabulary/acord-vocabulary.yaml
  - type: Features
    data:
      - name: XML Data Standards
        description: ACORD XML standards for property & casualty, life, annuity, and reinsurance SOAP/XML data exchange.
      - name: Next-Generation Digital Standards
        description: JSON/YAML-based NGDS for RESTful APIs, microservices, and IoT insurance data exchange.
      - name: Reinsurance Standards
        description: Global reinsurance and large commercial data standards for facultative and treaty transactions.
      - name: Life and Annuity Standards
        description: Electronic data standards for life insurance and annuity products covering underwriting and policy management.
      - name: Reference Architecture
        description: ACORD reference architecture providing structural frameworks for insurance technology implementations.
  - type: UseCases
    data:
      - name: Claims Data Exchange
        description: Standardized ACORD XML or NGDS JSON claims transaction exchange between carriers, adjusters, and reinsurers.
      - name: Policy Administration
        description: Automated policy issuance, endorsement, and renewal using ACORD NGDS microservices architecture.
      - name: Underwriting Automation
        description: Straight-through processing of insurance applications using ACORD standardized data elements.
      - name: Reinsurance Settlement
        description: Facultative and treaty reinsurance data exchange using ACORD Global Reinsurance Data Standards.
      - name: Regulatory Reporting
        description: Compliance reporting using ACORD-standardized data formats for regulatory submissions.
  - type: Integrations
    data:
      - name: Insurance Core Systems
        description: Integration with policy administration systems (PAS) and claims management systems (CMS).
      - name: Reinsurance Platforms
        description: Integration with reinsurance management platforms supporting ACORD AL3 and RIBO formats.
      - name: Insurtech Solutions
        description: Modern insurtech API platforms consuming ACORD NGDS JSON standards.
      - name: Regulatory Systems
        description: Integration with state and national insurance regulatory reporting systems.
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
modified: '2026-04-19'
description: ACORD is a global standards-setting body for the insurance industry, providing data standards, reference architecture, and digital tools that enable insurers, brokers, and software providers to exchange information.
name: ACORD
type: Index
specificationVersion: '0.19'
tags:
  - Claims
  - Insurance
  - Policy
  - Standards
  - Underwriting
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
---
