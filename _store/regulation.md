---
aid: regulation
name: Regulation
description: Regulation encompasses the rules, laws, and standards established by governments, agencies, and standards bodies that govern how businesses and individuals must operate. In the context of APIs and digital technology, regulation drives compliance requirements for data privacy (GDPR, CCPA), financial services (PSD2, Dodd-Frank), healthcare (HIPAA), and many other sectors. A rich ecosystem of APIs exists to access regulatory data, track regulatory changes, and automate compliance workflows.
type: Index
url: https://raw.githubusercontent.com/api-evangelist/regulation/refs/heads/main/apis.yml
tags:
  - Compliance
  - Governance
  - Government
  - Legal
  - Policy
  - Regulation
  - Regulatory Change
  - Risk Management
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: regulation:regulations-gov
    name: Regulations.gov API
    description: The Regulations.gov API provides access to federal regulatory dockets, documents, and public comments. Enables programmatic access to the full regulatory comment process and rulemaking lifecycle across US federal agencies.
    humanURL: https://open.gsa.gov/api/regulationsgov/
    baseURL: https://api.regulations.gov/v4
    tags:
      - Federal Regulations
      - Government
      - Public Comments
      - Rulemaking
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/regulationsgov/
      - type: OpenAPI
        url: https://api.regulations.gov/v4/api-docs
  - aid: regulation:federal-register
    name: Federal Register API
    description: The Federal Register API provides programmatic access to documents published in the Federal Register since 1994, including proposed rules, final rules, notices, and presidential documents. Supports advanced search and full-text retrieval.
    humanURL: https://www.federalregister.gov/developers/documentation/api/v1
    baseURL: https://www.federalregister.gov/api/v1
    tags:
      - Federal Register
      - Government
      - Regulatory Documents
      - Rules
    properties:
      - type: Documentation
        url: https://www.federalregister.gov/developers/documentation/api/v1
      - type: Documentation
        url: https://www.federalregister.gov/reader-aids/developer-resources/rest-api
  - aid: regulation:compliance-ai
    name: Compliance.ai Regulatory Change Management API
    description: Compliance.ai provides an API for regulatory change management that automatically aggregates data from federal and state agencies, enforcement actions, regulatory publications, white papers, and millions of new and existing rules. Enables financial institutions and businesses to stay current with regulatory developments.
    humanURL: https://www.compliance.ai/api/
    baseURL: https://api.compliance.ai
    tags:
      - Compliance
      - Financial Services
      - Regulatory Change
      - RegTech
    properties:
      - type: Documentation
        url: https://www.compliance.ai/api/
common:
  - type: Website
    url: https://open.gsa.gov/api/regulationsgov/
    name: Regulations.gov API - GSA Open Technology
  - type: Website
    url: https://www.federalregister.gov/developers/documentation/api/v1
    name: Federal Register API Documentation
  - type: Website
    url: https://catalog.data.gov/dataset/regulations-gov-api
    name: Regulations.gov API - Data.gov Catalog
  - type: Website
    url: https://www.compliance.ai/api/
    name: Compliance.ai Developer Program
  - type: Website
    url: https://developer.finra.org/
    name: FINRA Developer Center
  - type: Documentation
    url: https://en.wikipedia.org/wiki/Regulation
    name: Regulation - Wikipedia
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/regulation/refs/heads/main/json-schema/regulation-document-schema.json
    name: Regulatory Document JSON Schema
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/regulation/refs/heads/main/json-schema/regulation-comment-schema.json
    name: Public Comment JSON Schema
  - type: JSONStructure
    url: https://raw.githubusercontent.com/api-evangelist/regulation/refs/heads/main/json-structure/regulation-document-structure.json
    name: Regulatory Document JSON Structure
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/regulation/refs/heads/main/json-ld/regulation-context.jsonld
    name: Regulation JSON-LD Context
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/regulation/refs/heads/main/vocabulary/regulation-vocabulary.yml
    name: Regulation Vocabulary
  - type: Examples
    url: https://raw.githubusercontent.com/api-evangelist/regulation/refs/heads/main/examples/regulation-document-federal-register-example.json
    name: Federal Register Document Example
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
