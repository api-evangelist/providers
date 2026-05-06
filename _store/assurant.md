---
aid: assurant
url: https://raw.githubusercontent.com/api-evangelist/assurant/refs/heads/main/apis.yml
name: Assurant
description: Assurant is a global provider of lifestyle and housing solutions that help people thrive in a connected world. The company provides protection products and services including device protection, renter's insurance, auto F&I products, and connected living services. Assurant's APEX (Assurant Product Experience Exchange) platform provides embedded insurance APIs that enable partners to integrate protection products, claims management, and diagnostics directly into their workflows and customer experiences. The APEX platform supports 99.95% uptime and covers multiple product lines across technology, real estate, auto, and retail industries.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Insurance
  - Device Protection
  - Embedded Insurance
  - Housing
  - Claims
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: assurant:apex-insurance-api
    name: Assurant APEX Embedded Insurance API
    description: The Assurant APEX (Assurant Product Experience Exchange) platform provides embedded insurance APIs that enable partners to integrate protection products, claims management, and diagnostics into their workflows. The scalable API platform supports 99.95% uptime and covers product lines including device protection, renter's insurance, auto F&I products, and connected living services across multiple industries.
    humanURL: https://www.assurant.com/partner-with-us/apex
    baseURL: https://api-prod.portal.assurant.com
    tags:
      - Claims
      - Device Protection
      - Embedded Insurance
      - Insurance
    properties:
      - type: Documentation
        url: https://www.assurant.com/partner-with-us/apex
      - type: OpenAPI
        url: openapi/assurant-apex-insurance-api-openapi.yml
  - aid: assurant:global-housing-api
    name: Assurant Global Housing API
    description: The Assurant Global Housing API provides property management companies and housing partners with programmatic access to insurance products including renter's insurance, lender-placed insurance, and property preservation services. The API enables seamless integration of housing protection solutions into partner platforms.
    humanURL: https://www.assurant.com/partner-with-us/apex/global-housing
    baseURL: https://housing-apis.developer.assurant.com
    tags:
      - Housing
      - Insurance
      - Property
      - Renters Insurance
    properties:
      - type: Documentation
        url: https://www.assurant.com/partner-with-us/apex/global-housing
common:
  - type: Portal
    url: https://www.assurant.com/
    title: Assurant Website
  - type: Portal
    url: https://www.assurant.com/partner-with-us/apex
    title: APEX Partner Platform
  - type: SignUp
    url: https://www.assurant.com/partner-with-us/apex
    title: Partner with Assurant
  - type: Features
    data:
      - name: Embedded Device Protection
        description: APIs for embedding smartphone, tablet, and consumer electronics protection programs directly into carrier, retailer, and OEM customer experiences.
      - name: Claims Management
        description: End-to-end claims management APIs supporting claim filing, status tracking, device diagnostics, and repair/replacement fulfillment.
      - name: Renter's Insurance
        description: API integration for embedding renter's insurance enrollment, policy management, and claims into property management platforms.
      - name: Auto F&I Products
        description: Finance and insurance product APIs for automotive dealers including vehicle service contracts, GAP insurance, and protection products.
      - name: Connected Living Services
        description: Smart home device protection and tech support service APIs for connected device ecosystems.
  - type: UseCases
    data:
      - name: Mobile Carrier Device Protection
        description: Mobile carriers integrate APEX APIs to offer device protection plans at point of sale and manage claims for damaged or lost devices.
      - name: Property Management Renters Insurance
        description: Property management companies integrate the Global Housing API to offer and track renter's insurance compliance among tenants.
      - name: Auto Dealer F&I Integration
        description: Auto dealers and F&I providers integrate Assurant's vehicle protection APIs into dealer management systems for protection product sales.
      - name: E-Commerce Protection Programs
        description: Retailers integrate APEX APIs to offer product protection programs at checkout for electronics, appliances, and other products.
  - type: Integrations
    data:
      - name: Carrier Billing Systems
        description: Integration with mobile carrier billing and CRM systems for device protection plan enrollment and premium collection.
      - name: Property Management Platforms
        description: Integration with property management software including Yardi, RealPage, and AppFolio for renter's insurance programs.
      - name: Dealer Management Systems
        description: Integration with automotive DMS platforms for F&I product enrollment and vehicle protection program management.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
