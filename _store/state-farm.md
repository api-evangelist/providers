---
aid: state-farm
url: https://raw.githubusercontent.com/api-evangelist/state-farm/refs/heads/main/apis.yml
modified: '2026-05-02'
name: State Farm
description: State Farm is the largest property and casualty insurance provider in the United States, headquartered in Bloomington, Illinois. Founded in 1922, the company offers a comprehensive range of insurance products including auto, home, renters, life, health, business, and farm/ranch insurance, as well as banking and financial services. State Farm operates through a network of approximately 19,000 agents across the US and Canada. The company has invested heavily in its digital transformation, operating a Partner Gateway developer portal at developer.statefarm.com that exposes APIs enabling partners, agents, and third-party platforms to integrate with State Farm's insurance products and services. State Farm is a mutual company owned by its policyholders, consistently ranked among the Fortune 50.
apis:
  - aid: state-farm:renters-insurance-api
    name: Renters Insurance API
    description: The State Farm Renters Insurance API enables partner platforms, real estate applications, and property management systems to offer embedded renters insurance quotes and policies to tenants. Partners can request quotes, initiate policy applications, and retrieve policy status using this API. State Farm is the industry leader in renters insurance, providing coverage for personal belongings, liability protection, and additional living expenses. Available in all US states except California, Massachusetts, and Rhode Island.
    humanURL: https://developer.statefarm.com/api/renters
    baseURL: https://api.statefarm.com/v1
    tags:
      - Insurance
      - Renters Insurance
      - Property
      - Embedded Insurance
      - Partner
    properties:
      - type: Documentation
        url: https://developer.statefarm.com/api/renters
      - type: OpenAPI
        url: openapi/state-farm-renters-insurance-openapi.yml
  - aid: state-farm:auto-insurance-api
    name: Auto Insurance API
    description: The State Farm Auto Insurance API supports partner integrations for automobile insurance quoting, policy management, and claims inquiry. This API enables auto dealers, telematics platforms, and financial institutions to embed State Farm auto insurance products within their own applications. State Farm is the largest auto insurer in the US. The API supports retrieving quotes, checking policy status, and accessing coverage information.
    humanURL: https://developer.statefarm.com/
    baseURL: https://api.statefarm.com/v1
    tags:
      - Insurance
      - Auto Insurance
      - Vehicles
      - Partner
      - Embedded Insurance
    properties:
      - type: Documentation
        url: https://developer.statefarm.com/
  - aid: state-farm:b2b-insurance-inquiry-api
    name: B2B Insurance Inquiry API
    description: The State Farm B2B Insurance Inquiry API is designed for lenders, mortgage servicers, and financial institutions that need to verify homeowner and auto insurance policy status for collateral protection purposes. This API supports home and auto lenders in verifying that borrowers maintain the required insurance coverage on financed assets. Accessible through the State Farm B2B portal.
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
  - type: Twitter
    url: https://twitter.com/StateFarm
  - type: Privacy Policy
    url: https://www.statefarm.com/customer-care/privacy-security/privacy/privacy-policy
  - type: Terms of Service
    url: https://www.statefarm.com/customer-care/legal-disclaimer
  - type: FAQ
    url: https://developer.statefarm.com/faq
  - type: OpenAPI
    url: openapi/state-farm-renters-insurance-openapi.yml
  - type: JSONSchema
    url: json-schema/state-farm-renters-policy-schema.json
  - type: JSONStructure
    url: json-structure/state-farm-renters-policy-structure.json
  - type: JSONLD
    url: json-ld/state-farm-context.jsonld
  - type: Vocabulary
    url: vocabulary/state-farm-vocabulary.yml
  - type: SpectralRules
    url: rules/state-farm-rules.yml
  - type: NaftikoCapabilities
    url: capabilities/embedded-insurance.yaml
---
