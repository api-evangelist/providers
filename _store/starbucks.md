---
aid: starbucks
url: https://raw.githubusercontent.com/api-evangelist/starbucks/refs/heads/main/apis.yml
name: Starbucks
tags:
  - Coffee
  - Food Service
  - Loyalty
  - Ordering
  - Retail
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2024-01-01'
modified: '2026-05-02'
description: Starbucks provides partner APIs for ordering, loyalty program integration, store locations, and menu data through their developer portal. These APIs enable authorized partners to integrate Starbucks ordering, rewards, and store discovery into their applications.
apis:
  - aid: starbucks:starbucks-api
    name: Starbucks API
    tags:
      - Food Service
      - Coffee
      - Ordering
      - Loyalty
      - Store Locator
      - Menu
    properties:
      - url: https://developer.starbucks.com/
        type: Portal
      - url: https://portal.starbucks.com/
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/starbucks/refs/heads/main/openapi/starbucks-starbucks-api-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/starbucks/refs/heads/main/rules/starbucks-rules.yml
        type: SpectralRules
      - url: https://raw.githubusercontent.com/api-evangelist/starbucks/refs/heads/main/capabilities/food-service.yaml
        type: NaftikoCapabilities
    description: The Starbucks API provides partner access to ordering workflows, loyalty program management, store location discovery, and menu data. Authorized partners use OAuth2 bearer token authentication to integrate Starbucks experiences into their applications and services.
common:
  - url: https://www.starbucks.com/
    type: Website
  - url: https://developer.starbucks.com/
    type: Portal
  - url: https://portal.starbucks.com/
    type: Documentation
  - url: https://www.starbucks.com/about-us/company-information/starbucks-company-timeline
    type: About
  - url: https://www.starbucks.com/careers/
    type: Careers
  - url: https://www.starbucks.com/responsibility/privacy-policy
    type: PrivacyPolicy
  - url: https://www.starbucks.com/about-us/company-information/online-policies/terms-of-use
    type: TermsOfService
  - url: https://x.com/Starbucks
    type: X
  - url: https://www.linkedin.com/company/starbucks
    type: LinkedIn
  - url: https://www.facebook.com/Starbucks
    type: Facebook
  - url: https://www.instagram.com/starbucks
    type: Instagram
---
