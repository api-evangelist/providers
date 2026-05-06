---
aid: tango
name: Tango
description: Tango (formerly Tango Card) is a rewards-as-a-service platform that provides APIs for automating digital reward and incentive delivery. The Tango RaaS API enables companies to integrate a global catalog of 3,100+ digital gift cards, prepaid cards, and charitable donations directly into their products and workflows. Tango serves loyalty programs, research panels, employee recognition platforms, and consumer incentive applications worldwide.
type: Index
image: https://www.tangocard.com/wp-content/uploads/2021/06/tango-logo.png
tags:
  - Catalog Management
  - Digital Rewards
  - Gift Cards
  - Incentives
  - Loyalty
  - Rewards As A Service
url: https://raw.githubusercontent.com/api-evangelist/tango/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: tango:raas-api
    name: Tango RaaS API
    description: The Tango Rewards-as-a-Service (RaaS) API v2 is a RESTful interface for automating digital reward and incentive delivery. It enables customers to manage accounts and funding, browse a global reward catalog, place and manage orders, configure digital email templates, and receive webhook notifications. The API supports both sandbox and production environments.
    humanURL: https://developers.tangocard.com/
    baseURL: https://api.tangocard.com/raas/v2
    tags:
      - Accounts
      - Catalog
      - Gift Cards
      - Orders
      - Rewards
      - Webhooks
    properties:
      - type: Documentation
        url: https://developers.tangocard.com/docs/user-guide-tango-api-v2
      - type: Reference
        url: https://developers.tangocard.com/reference
      - type: OpenAPI
        url: openapi/tango-raas-api-openapi.yml
      - type: GettingStarted
        url: https://developers.tangocard.com/docs/getting-started
      - type: Authentication
        url: https://developers.tangocard.com/docs/authentication
      - type: Sandbox
        url: https://portal.sandbox.tangocard.com
      - type: Portal
        url: https://portal.tangocard.com
      - type: ChangeLog
        url: https://developers.tangocard.com/changelog
    contact:
      - type: Support
        url: https://developers.tangocard.com/
      - type: Email
        url: mailto:devsupport@tangocard.com
common:
  - type: Website
    url: https://www.tangocard.com/
  - type: Portal
    url: https://developers.tangocard.com/
  - type: GettingStarted
    url: https://developers.tangocard.com/docs/getting-started
  - type: Authentication
    url: https://developers.tangocard.com/docs/authentication
  - type: Sandbox
    url: https://portal.sandbox.tangocard.com
  - type: ChangeLog
    url: https://developers.tangocard.com/changelog
  - type: TermsOfService
    url: https://www.tangocard.com/terms-of-service/
  - type: PrivacyPolicy
    url: https://www.tangocard.com/privacy-policy/
  - type: Contact
    url: https://www.tangocard.com/contact/
  - type: Login
    url: https://portal.tangocard.com
  - type: OpenAPI
    url: openapi/tango-raas-api-openapi.yml
  - type: JSONSchema
    url: json-schema/tango-order-schema.json
  - type: JSONSchema
    url: json-schema/tango-account-schema.json
  - type: JSONSchema
    url: json-schema/tango-catalog-item-schema.json
  - type: JSONStructure
    url: json-structure/tango-order-structure.json
  - type: JSONLD
    url: json-ld/tango-context.jsonld
  - type: SpectralRules
    url: rules/tango-rules.yml
  - type: NaftikoCapabilities
    url: capabilities/reward-automation.yaml
  - type: Vocabulary
    url: vocabulary/tango-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
