---
aid: sprague-resources
name: Sprague Resources
description: Sprague Resources (operating as Sprague Energy) is one of the largest independent suppliers of energy products and related services in the northeastern United States and Quebec, founded in 1870. The company distributes refined fuel products (heating oil, diesel, gasoline, kerosene, biofuels), natural gas, and electricity to commercial and industrial customers, and operates 20+ port terminal facilities for materials handling. Sprague was acquired by Hartree Partners in 2024 and continues to expand through strategic acquisitions. While Sprague does not publish a public developer API, the company operates SpraguePORT, a digital customer portal for account management, pricing, and order history, and Sprague Real-time for market pricing.
modified: '2026-05-02'
created: '2023-01-01'
specificationVersion: '0.19'
type: Index
position: Provider
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Energy
  - Petroleum
  - Natural Gas
  - Fuel Distribution
  - Materials Handling
  - Northeast
url: https://raw.githubusercontent.com/api-evangelist/sprague-resources/refs/heads/main/apis.yml
apis:
  - aid: sprague-resources:sprague-port
    name: SpraguePORT Customer Portal
    description: SpraguePORT is Sprague Energy's electronic customer portal providing one-stop access to account management, order history, invoice details, market pricing data, and energy management tools. Available to commercial and industrial customers, resellers, brokers, and channel partners. The portal covers both refined petroleum products and natural gas account management. No public REST API is documented; access requires direct partnership with Sprague Energy.
    humanURL: https://www.spragueenergy.com/
    tags:
      - Energy
      - Customer Portal
      - Fuel
      - Account Management
    properties:
      - type: Website
        url: https://www.spragueenergy.com/
      - type: Customer Portal
        url: https://mysprague.com
  - aid: sprague-resources:sprague-realtime-pricing
    name: Sprague Real-time Pricing
    description: Sprague Real-time is described as "the industry's best and simplest online pricing tool" for resellers and channel partners to access current market pricing for petroleum products. Provides market transparency for refined product pricing decisions. Access is restricted to Sprague business partners.
    humanURL: https://www.spragueenergy.com/
    tags:
      - Pricing
      - Petroleum
      - Market Data
      - Energy
    properties:
      - type: Website
        url: https://www.spragueenergy.com/
common:
  - type: Website
    url: https://www.spragueenergy.com
  - type: Customer Portal
    url: https://mysprague.com
  - type: Contact
    url: https://www.spragueenergy.com/contact-us
  - type: About
    url: https://www.spragueenergy.com/about-us
  - type: JSONSchema
    url: json-schema/sprague-fuel-order-schema.json
  - type: JSONStructure
    url: json-structure/sprague-fuel-order-structure.json
  - type: JSONLD
    url: json-ld/sprague-resources-context.jsonld
  - type: Vocabulary
    url: vocabulary/sprague-resources-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
