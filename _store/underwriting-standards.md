---
aid: underwriting-standards
name: Underwriting Standards
description: A curated collection of data standards, APIs, and specifications used in insurance underwriting. This covers the landscape of industry-wide data interchange formats, protocol standards, and API ecosystems that enable carriers, MGAs, brokers, and InsurTech platforms to exchange underwriting data programmatically. Key standards include ACORD (Property & Casualty, Life, Reinsurance), LIMRA LDEx (employee benefits), and emerging OpenInsurance initiatives.
url: https://raw.githubusercontent.com/api-evangelist/underwriting-standards/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Underwriting
  - Insurance
  - Standards
  - ACORD
  - Data Exchange
  - InsurTech
created: '2025-01-01'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: underwriting-standards:acord-api
    name: ACORD Next-Generation Digital Standards API
    tags:
      - Insurance
      - ACORD
      - Standards
      - Property And Casualty
      - Life Insurance
      - Reinsurance
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://www.acord.org
    humanURL: https://www.acord.org/standards-architecture/acord-data-standards/next-generation-digital-standards
    properties:
      - url: https://www.acord.org/standards-architecture/acord-data-standards
        type: Documentation
      - url: https://www.acord.org/standards-architecture/acord-data-standards/next-generation-digital-standards
        type: Documentation
      - url: https://www.acord.org/standards-architecture/reference-architecture
        type: Reference Architecture
    description: ACORD (Association for Cooperative Operations Research and Development) provides the insurance industry's primary data standards. The Next-Generation Digital Standards (NGDS) are JSON/YAML-based transaction-centric standards for RESTful APIs and microservices, covering Policy, Claims, Party, Product, and Reinsurance entities. ACORD standards are used by over 3,000 member organizations worldwide.
  - aid: underwriting-standards:ldex
    name: LIMRA LDEx Data Exchange Standards
    tags:
      - Insurance
      - LIMRA
      - Benefits Administration
      - Standards
      - Employee Benefits
      - Life Insurance
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://www.limra.com
    humanURL: https://www.limra.com/en/solutions-and-services/data-exchange-standards/
    properties:
      - url: https://www.limra.com/en/solutions-and-services/data-exchange-standards/ldex-overview/
        type: Documentation
      - url: https://www.limra.com/en/solutions-and-services/data-exchange-standards/standards-download/
        type: Downloads
    description: The LIMRA Data Exchange (LDEx) Standards are free, collaboratively developed standards for exchanging employee workplace benefits data between carriers and benefits administration platforms. LDEx provides REST API endpoints compliant with OpenAPI 3.1 and supports JSON, XML, and YAML payloads. Use cases include enrollment, eligibility, coverage changes, terminations, and evidence of insurability.
common:
  - type: Website
    url: https://www.acord.org/
  - type: Website
    url: https://www.limra.com/
  - type: Standard
    url: https://www.acord.org/standards-architecture/acord-data-standards
  - type: Standard
    url: https://www.limra.com/en/solutions-and-services/data-exchange-standards/
  - type: JSON-LD
    url: json-ld/underwriting-standards-context.jsonld
  - type: Vocabulary
    url: vocabulary/underwriting-standards-vocabulary.yml
  - type: JSONSchema
    url: json-schema/underwriting-standards-submission-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
