---
aid: cbre
url: https://raw.githubusercontent.com/api-evangelist/cbre/refs/heads/main/apis.yml
name: CBRE
tags:
  - Analytics
  - Commercial Real Estate
  - Facilities Management
  - Fortune 500
  - Investment Management
  - Property Management
  - Real Estate
  - Valuation
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-21'
modified: '2026-04-23'
position: Consumer
description: 'CBRE Group, Inc. (NYSE: CBRE) is the world''s largest commercial real estate services and investment firm, with 155,000 professionals across 500+ offices in 100+ countries. CBRE provides advisory and transaction, project management, property management, valuation, investment management, and consulting services. Its technology arm publishes developer APIs through developer.cbre.com that expose property, analytics, and facilities data to partners.'
apis:
  - aid: cbre:cbre-api
    name: CBRE Developer API
    tags:
      - Analytics
      - Commercial Property
      - Facilities
      - Investment
      - Real Estate
      - Valuation
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.cbre.com
    humanURL: https://developer.cbre.com/
    properties:
      - url: https://developer.cbre.com/
        type: Documentation
      - url: openapi/cbre-cbre-api-openapi.yml
        type: OpenAPI
      - url: https://developer.cbre.com/
        type: Portal
    description: CBRE provides APIs for commercial real estate data including property listings, market analytics, facilities management, lease administration, valuation, and investment management. The platform enables partners and clients to access CBRE's real estate intelligence and integrate with internal systems.
common:
  - type: Website
    url: https://www.cbre.com
  - type: About
    url: https://www.cbre.com/about-us
  - type: Careers
    url: https://www.cbre.com/careers
  - type: InvestorRelations
    url: https://ir.cbre.com
  - type: Newsroom
    url: https://www.cbre.com/about-us/newsroom
  - type: PressReleases
    url: https://www.cbre.com/about-us/newsroom
  - type: Research
    url: https://www.cbre.com/insights
  - type: Sustainability
    url: https://www.cbre.com/services/energy-and-sustainability-solutions
  - type: Contact
    url: https://www.cbre.com/about-us/culture-and-history/contact-us
  - type: TermsOfService
    url: https://www.cbre.com/about-us/disclaimer-terms-of-use
  - type: PrivacyPolicy
    url: https://www.cbre.com/about-us/global-privacy-and-cookie-notice
  - type: Portal
    url: https://developer.cbre.com/
  - name: Features
    type: Features
    data:
      - name: Property Search
      - name: Listing Management
      - name: Lease Administration
      - name: Market Analytics
      - name: Valuation
      - name: Facilities Management
      - name: Work Order Management
      - name: Space Utilization
      - name: Investment Management
      - name: Transaction Services
      - name: Portfolio Reporting
      - name: Sustainability Metrics
  - name: UseCases
    type: UseCases
    data:
      - name: Corporate Real Estate Portfolio Management
      - name: Commercial Property Marketing
      - name: Facilities Operations
      - name: Lease Accounting (ASC 842 / IFRS 16)
      - name: Investment Fund Reporting
      - name: Workplace Occupancy Analytics
      - name: Market Research and Forecasting
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
specificationVersion: '0.19'
---
