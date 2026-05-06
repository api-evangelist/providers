---
aid: carvana
name: Carvana
description: Carvana is an e-commerce platform for buying, selling, and financing used cars online, featuring home delivery or pickup at its distinctive car vending machines. Its primary developer-facing integration surface is the Carvana Partner REST API (published on Azure API Management at api-developer.carvana.com) which enables authorized rental companies, wholesalers, and fleet partners to post, update, and manage inventory in Carvana's catalog. A Carvana Collective API (api.collective.carvana.com) supports partner-collective workflows, and Carvana also distributes inventory data via AWS Data Exchange.
type: Index
position: Provider
access: Partner
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automotive
  - E-Commerce
  - Used Cars
  - Inventory
  - Partner API
  - Fortune 500
created: '2026-03-21'
modified: '2026-04-23'
url: https://raw.githubusercontent.com/api-evangelist/carvana/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: carvana:partner-api
    name: Carvana Partner API
    description: REST API that enables deep integration between Carvana and authorized partners (car rental companies, wholesalers, and fleet operators) for posting, updating, and managing used-vehicle inventory. Requires Carvana LLC authorization; the developer portal runs on Microsoft Azure API Management.
    humanURL: https://api-developer.carvana.com/
    baseURL: https://api-developer.carvana.com
    tags:
      - Partner
      - Inventory
      - Authorized Access
    properties:
      - type: Portal
        url: https://api-developer.carvana.com/
      - type: Login
        url: https://api-developer.carvana.com/signin
      - type: Documentation
        url: https://api-developer.carvana.com/
      - type: TermsOfService
        name: Carvana Property & Unauthorized Access Notice
        url: https://api-developer.carvana.com/
  - aid: carvana:collective-api
    name: Carvana Collective API
    description: API surface supporting Carvana Collective partner-collaborative workflows; access is restricted to authorized Carvana partners.
    humanURL: https://api.collective.carvana.com/
    baseURL: https://api.collective.carvana.com
    tags:
      - Partner
      - Collective
    properties:
      - type: Documentation
        url: https://api.collective.carvana.com/
  - aid: carvana:aws-data-exchange
    name: Carvana Car Sales Data (AWS Data Exchange)
    description: Carvana's used-car inventory and sales data product published on AWS Data Exchange for direct subscription and data-warehouse delivery to analytics, pricing, and market-research consumers.
    humanURL: https://aws.amazon.com/marketplace/pp/prodview-y77x3t6zisn4w
    tags:
      - Data Product
      - AWS Data Exchange
      - Inventory
    properties:
      - type: Listing
        url: https://aws.amazon.com/marketplace/pp/prodview-y77x3t6zisn4w
  - aid: carvana:partner-inventory-help
    name: Carvana Partner Inventory Help Center
    description: Consumer-facing explainer describing how Carvana sources partner inventory (rental fleets and other partners) into the buyer catalog.
    humanURL: https://www.carvana.com/help/carvana-inventory/where-is-partner-inventory
    tags:
      - Partner
      - Inventory
      - Consumer
    properties:
      - type: Documentation
        url: https://www.carvana.com/help/carvana-inventory/where-is-partner-inventory
common:
  - type: Website
    url: https://www.carvana.com
  - type: Portal
    name: Carvana Developer Portal
    url: https://api-developer.carvana.com/
  - type: Login
    url: https://api-developer.carvana.com/signin
  - type: Help
    url: https://www.carvana.com/help
  - type: Sell
    url: https://www.carvana.com/sell-car
  - type: Finance
    url: https://www.carvana.com/finance
  - type: VendingMachines
    url: https://www.carvana.com/vending-machine-locations
  - type: About
    url: https://www.carvana.com/company/about_us
  - type: InvestorRelations
    url: https://investors.carvana.com
  - type: Careers
    url: https://www.carvana.com/careers
  - type: Contact
    url: https://www.carvana.com/help/contact-us
  - type: TermsOfService
    url: https://www.carvana.com/terms-of-use
  - type: PrivacyPolicy
    url: https://www.carvana.com/privacy-policy
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
