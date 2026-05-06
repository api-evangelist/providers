---
aid: coca-cola
url: https://raw.githubusercontent.com/api-evangelist/coca-cola/refs/heads/main/apis.yml
name: The Coca-Cola Company
tags:
  - Beverages
  - Beverage Manufacturer
  - Consumer Goods
  - Distribution
  - Retail
  - Supply Chain
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
x-type: company
created: '2026-03-21'
modified: '2026-04-26'
position: Consumer
description: The Coca-Cola Company is the world's largest non-alcoholic beverage company, owning and marketing more than 200 brands across sparkling soft drinks, water, hydration, sports, coffee, tea, juice, dairy, and plant-based drinks. The company sells its products in more than 200 countries through a bottling and distribution partner network. While Coca-Cola does not currently publish a broadly available public REST API, it is a heavy enterprise API consumer running an internal API program on MuleSoft that connects ERP, manufacturing, distribution, retail, marketing, and consumer engagement systems through a Center for Enablement (C4E) model. Historical Coca-Cola Enterprises (CCE) Product and Location APIs at developer.cokecce.com are no longer maintained as a public-facing developer program.
apis:
  - aid: coca-cola:coca-cola-internal-api-platform
    name: Coca-Cola Internal API Platform
    tags:
      - API Management
      - Enterprise Integration
      - Microservices
      - MuleSoft
    humanURL: https://www.mulesoft.com/webinars/api/evaluation-to-implementation-coca-cola-company-journey
    properties:
      - url: https://www.mulesoft.com/webinars/api/how-coca-cola-accelerates
        type: CaseStudy
      - url: https://www.mulesoft.com/webinars/api/evaluation-to-implementation-coca-cola-company-journey
        type: CaseStudy
    description: Internal API platform built on MuleSoft Anypoint that exposes reusable experience, process, and system APIs across The Coca-Cola Company's bottling, marketing, ecommerce, and supply-chain operations. Governed by a central Center for Enablement (C4E) team that defines design standards, security policies, and reuse metrics. Not publicly accessible but a frequently cited reference architecture for Fortune 50 API programs.
    x-features:
      - API-led connectivity (system, process, experience APIs)
      - Center for Enablement (C4E) governance
      - Reusable assets across LOBs and bottling partners
      - OAuth 2.0 / API key based access for partners
    x-use-cases:
      - Bottler integrations
      - Retail and route-to-market data exchange
      - Consumer engagement (Freestyle, loyalty)
      - Supply-chain visibility and demand planning
  - aid: coca-cola:coca-cola-enterprises-product-api-legacy
    name: Coca-Cola Enterprises Product API (Legacy)
    tags:
      - Catalog
      - Legacy
      - Products
    humanURL: http://developer.cokecce.com/docs/Product_API
    properties:
      - url: http://developer.cokecce.com/io-docs
        type: Documentation
      - url: http://developer.cokecce.com/docs/Product_API
        type: Documentation
      - url: http://developer.cokecce.com/API_Terms_of_Use
        type: TermsOfService
    description: Historical Coca-Cola Enterprises (CCE) Product API that exposed product catalog metadata and was published through an I/O Docs portal at developer.cokecce.com. Following the 2016 reorganization that created Coca-Cola European Partners (now Coca-Cola Europacific Partners), the CCE developer portal is no longer maintained as a public developer program. Documented here for archival reference only.
    x-features:
      - Product catalog lookup
      - I/O Docs interactive documentation
      - API key authentication
    x-use-cases:
      - Retail merchandising integrations (historical)
      - Product information sharing with partners (historical)
  - aid: coca-cola:coca-cola-enterprises-location-api-legacy
    name: Coca-Cola Enterprises Location API (Legacy)
    tags:
      - Geolocation
      - Legacy
      - Locations
    humanURL: http://developer.cokecce.com/docs/Location
    properties:
      - url: http://developer.cokecce.com/docs/Location
        type: Documentation
    description: Historical Coca-Cola Enterprises (CCE) Location API that exposed Coca-Cola product availability and bottler/distribution location data. No longer maintained as a public developer program after the reorganization into Coca-Cola European Partners. Documented here for archival reference only.
    x-features:
      - Location and territory lookup
      - Bottler/distributor metadata
    x-use-cases:
      - Field merchandising apps (historical)
      - Distribution territory visualization (historical)
common:
  - type: Website
    url: https://www.coca-colacompany.com/
  - type: Brands
    url: https://www.coca-colacompany.com/brands
  - type: Innovation
    url: https://www.coca-colacompany.com/innovation
  - type: Investors
    url: https://investors.coca-colacompany.com/
  - type: Press
    url: https://www.coca-colacompany.com/media-center
  - type: Sustainability
    url: https://www.coca-colacompany.com/sustainability
  - type: Careers
    url: https://www.coca-colacompany.com/careers
  - type: PrivacyPolicy
    url: https://www.coca-colacompany.com/policies-and-practices/privacy-policy
  - type: TermsOfService
    url: https://www.coca-colacompany.com/policies-and-practices/terms-of-use
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
