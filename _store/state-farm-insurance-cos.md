---
aid: state-farm-insurance-cos
url: https://raw.githubusercontent.com/api-evangelist/state-farm-insurance-cos/refs/heads/main/apis.yml
modified: '2026-05-02'
name: State Farm Insurance Companies
description: State Farm Insurance Companies is the collective name for the group of insurance subsidiaries operating under State Farm Mutual Automobile Insurance Company, the parent organization headquartered in Bloomington, Illinois. The group comprises fourteen property and casualty insurance companies and two life insurance companies including State Farm Mutual Automobile Insurance Company, State Farm Fire and Casualty Company, State Farm Indemnity Company, State Farm Life Insurance Company, State Farm General Insurance Company, State Farm Florida Insurance Company, and State Farm Lloyds, among others. This multi-entity structure allows State Farm to manage its business across different US state regulatory environments. As a group, State Farm Insurance Companies is the largest property and casualty insurer in the United States. The group shares the common digital infrastructure and developer platform operated at developer.statefarm.com.
apis:
  - aid: state-farm-insurance-cos:partner-gateway-api
    name: Partner Gateway API
    description: The State Farm Partner Gateway API serves as the unified integration layer for all State Farm Insurance Companies subsidiaries, enabling external partners to access insurance products across the State Farm family of companies through a single API entry point. The Partner Gateway supports embedded insurance workflows, lender integrations, real estate platforms, and third-party aggregators, routing requests to the appropriate State Farm subsidiary based on the product type and state jurisdiction.
    humanURL: https://developer.statefarm.com
    baseURL: https://api.statefarm.com/v1
    tags:
      - Insurance
      - Partner
      - Integration
      - API Gateway
      - Multi-line
    properties:
      - type: Documentation
        url: https://developer.statefarm.com
      - type: FAQ
        url: https://developer.statefarm.com/faq
  - aid: state-farm-insurance-cos:renters-insurance-api
    name: Renters Insurance API
    description: The Renters Insurance API from State Farm Insurance Companies enables property management platforms, multifamily housing operators, and partner aggregators to embed State Farm renters insurance into their tenant onboarding flows. State Farm is the number one writer of renters insurance in the US. Partners can request quotes, bind policies, and retrieve policy status through this API. Coverage is underwritten by the appropriate State Farm subsidiary for each state jurisdiction.
    humanURL: https://developer.statefarm.com/api/renters
    baseURL: https://api.statefarm.com/v1
    tags:
      - Insurance
      - Renters Insurance
      - Embedded Insurance
      - Partner
      - Multi-line
    properties:
      - type: Documentation
        url: https://developer.statefarm.com/api/renters
      - type: OpenAPI
        url: openapi/state-farm-insurance-cos-renters-openapi.yml
  - aid: state-farm-insurance-cos:b2b-lender-services-api
    name: B2B Lender Services API
    description: The State Farm B2B Lender Services API provides mortgage lenders and auto lenders with programmatic access to verify insurance coverage for collateral assets financed by their borrowers. Lenders can confirm active homeowners, auto, or property insurance policies written by any State Farm Insurance Companies subsidiary. This supports lender compliance, reduces force-placed insurance, and streamlines closing workflows.
    humanURL: https://b2b.statefarm.com/b2b-content/home-auto-lenders/ins-inquiry
    baseURL: https://b2b.statefarm.com/api/v1
    tags:
      - Insurance
      - B2B
      - Lenders
      - Mortgage
      - Verification
    properties:
      - type: Documentation
        url: https://b2b.statefarm.com/b2b-content/home-auto-lenders/ins-inquiry
common:
  - type: Website
    url: https://www.statefarm.com
  - type: Developer Portal
    url: https://developer.statefarm.com
  - type: GitHub
    url: https://github.com/StateFarmIns
  - type: Engineering Blog
    url: https://engineering.statefarm.com/blog
  - type: B2B Portal
    url: https://b2b.statefarm.com
  - type: LinkedIn
    url: https://www.linkedin.com/company/state-farm
  - type: Newsroom
    url: https://newsroom.statefarm.com
  - type: Privacy Policy
    url: https://www.statefarm.com/customer-care/privacy-security/privacy/privacy-policy
  - type: Terms of Service
    url: https://www.statefarm.com/customer-care/legal-disclaimer
  - type: OpenAPI
    url: openapi/state-farm-insurance-cos-renters-openapi.yml
  - type: JSONSchema
    url: json-schema/state-farm-insurance-cos-renters-policy-schema.json
  - type: JSONStructure
    url: json-structure/state-farm-insurance-cos-renters-policy-structure.json
  - type: JSONLD
    url: json-ld/state-farm-insurance-cos-context.jsonld
  - type: Vocabulary
    url: vocabulary/state-farm-insurance-cos-vocabulary.yml
  - type: SpectralRules
    url: rules/state-farm-insurance-cos-rules.yml
  - type: NaftikoCapabilities
    url: capabilities/embedded-insurance.yaml
---
