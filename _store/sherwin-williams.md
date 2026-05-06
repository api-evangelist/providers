---
aid: sherwin-williams
url: https://raw.githubusercontent.com/api-evangelist/sherwin-williams/refs/heads/main/apis.yml
apis:
  - aid: sherwin-williams:sherwin-williams-supplier-api
    name: Sherwin-Williams Supplier API
    tags:
      - B2B
      - Paint
      - Retail
      - Supply Chain
    humanURL: https://suppliers.sherwin-williams.com/
    properties:
      - url: https://suppliers.sherwin-williams.com/
        type: Documentation
      - url: json-schema/sherwin-williams-product-schema.json
        type: JSONSchema
      - url: json-schema/sherwin-williams-supplier-schema.json
        type: JSONSchema
      - url: json-ld/sherwin-williams-context.jsonld
        type: JSONLD
      - url: rules/sherwin-williams-rules.yml
        type: SpectralRules
      - url: vocabulary/sherwin-williams-vocabulary.yml
        type: Vocabulary
    description: The Sherwin-Williams Supplier API enables B2B partners to integrate supply chain workflows, manage purchase orders, submit invoices, and exchange product and inventory data with Sherwin-Williams enterprise systems. The portal supports EDI and API-based integrations for suppliers and trading partners.
  - aid: sherwin-williams:sherwin-williams-edi-integration
    name: Sherwin-Williams EDI Integration
    tags:
      - B2B
      - EDI
      - Integration
      - Supply Chain
    humanURL: https://suppliers.sherwin-williams.com/
    properties:
      - url: https://suppliers.sherwin-williams.com/
        type: Documentation
    description: Sherwin-Williams EDI integration capabilities enable trading partners to exchange electronic data interchange (EDI) documents including purchase orders, invoices, advance ship notices, and inventory feeds. Supported EDI formats include X12 and EDIFACT standards.
name: Sherwin-Williams
tags:
  - B2B
  - Construction
  - Fortune 500
  - Paints
  - Retail
  - Supply Chain
type: Contract
image: https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Sherwin-Williams_logo.svg/2560px-Sherwin-Williams_logo.svg.png
access: 3rd-Party
created: '2025-03-01'
modified: '2026-05-02'
position: Consumer
description: The Sherwin-Williams Company is a global leader in the paint and coatings industry, offering products for consumers, contractors, industrial clients, and commercial builders. Sherwin-Williams provides B2B API and EDI integration capabilities for suppliers and trading partners to connect with their enterprise supply chain and retail operations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - url: https://suppliers.sherwin-williams.com/
    type: Supplier Portal
  - url: https://www.sherwin-williams.com/home-builders/services/paint-technology-and-application
    type: Partner Program
  - url: https://www.sherwin-williams.com/legal/terms-of-use
    type: Terms of Service
  - url: https://www.sherwin-williams.com/legal/privacy-policy
    type: Privacy Policy
  - url: https://github.com/sherwin-williams-co
    type: GitHub Organization
  - url: https://www.sherwin-williams.com
    type: Website
---
