---
aid: columbia-sportswear
url: https://raw.githubusercontent.com/api-evangelist/columbia-sportswear/refs/heads/main/apis.yml
name: Columbia Sportswear
tags:
  - Apparel
  - B2B
  - Consumer Management
  - Cognitive
  - Footwear
  - Order Management
  - Outdoor
  - Product Lifecycle
  - Retail
type: Index
x-type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-03-23'
modified: '2026-04-28'
position: Consumer
description: 'Columbia Sportswear is a global designer, marketer, and distributor of outdoor, active, and everyday lifestyle apparel, footwear, accessories, and equipment under the Columbia, Mountain Hardwear, SOREL, and prAna brands. Columbia Sportswear Digital operates a partner-focused developer portal on Microsoft Azure API Management at columbia.portal.azure-api.net, exposing APIs for Order Management, Consumer Management, Product Lifecycle Management, Cognitive, Weather, and Translation. The developer portal is gated: registered partners create an account, browse products and APIs, request subscription keys, and integrate against the published endpoints. The company also exchanges traditional EDI documents (POs, ASNs, invoices) with retail trading partners through providers like TrueCommerce and eZCom.'
apis:
  - aid: columbia-sportswear:digital-developer-portal
    name: Columbia Sportswear Digital Developer Portal
    tags:
      - Cognitive
      - Consumer Management
      - Order Management
      - Partner APIs
      - Product Lifecycle
      - Translation
      - Weather
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://columbia.portal.azure-api.net/
    properties:
      - url: https://columbia.portal.azure-api.net/
        type: Developer Portal
      - url: https://columbia-dev.portal.azure-api.net/
        type: Developer Portal (Dev)
    description: Columbia Sportswear's partner-facing API platform hosted on Microsoft Azure API Management. The portal organizes APIs across Order Management (B2B and DTC orders), Consumer Management (loyalty, profiles), Product Lifecycle Management (catalog, content, classification), Cognitive (search and recommendations), Weather, and Translation. Subscription keys are required and granted on a per-partner basis. The portal exposes try-it consoles, request examples, and documentation per API product.
    x-features:
      - Hosted on Microsoft Azure API Management
      - Subscription-key based authentication
      - Multi-product API catalog (Order, Consumer, PLM, Cognitive, Weather, Translation)
      - Self-service partner onboarding and key request
      - Try-it consoles per API operation
      - Dev and production portal environments
    x-use-cases:
      - Power retail partner order fulfillment workflows
      - Sync product catalog data with marketplaces
      - Personalize consumer experiences via consumer-management APIs
      - Drive store and fulfillment decisions with weather data
      - Enable translation and localization for global commerce
common:
  - type: Website
    url: https://www.columbia.com/
  - type: Corporate
    url: https://www.columbiasportswear.com/
  - type: Developer Portal
    url: https://columbia.portal.azure-api.net/
  - type: Developer Portal (Dev)
    url: https://columbia-dev.portal.azure-api.net/
  - type: Investor Relations
    url: https://investor.columbia.com/
  - type: Mountain Hardwear
    url: https://www.mountainhardwear.com/
  - type: SOREL
    url: https://www.sorel.com/
  - type: prAna
    url: https://www.prana.com/
  - type: B2B Support (Europe)
    url: https://europe-customers.columbia.com/hc/en-us
  - type: Privacy Policy
    url: https://www.columbia.com/privacy.html
  - type: Terms of Use
    url: https://www.columbia.com/terms-and-conditions.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
