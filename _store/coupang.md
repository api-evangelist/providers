---
aid: coupang
name: Coupang
x-type: company
description: Coupang is a South Korean e-commerce company offering rapid delivery of a wide range of products including groceries, electronics, fashion, and household goods through its mobile app and website. Coupang exposes an Open API platform for marketplace sellers (vendors) to integrate product catalog, order, return, cancellation, settlement, and inquiry workflows.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/coupang/refs/heads/main/apis.yml
type: Index
access: 3rd-Party
position: Consuming
created: '2024-01-01'
modified: '2026-04-28'
tags:
  - Cancellations
  - E-commerce
  - Korea
  - Marketplace
  - Open API
  - Orders
  - Products
  - Returns
  - Sellers
  - Settlement
  - Vendors
apis:
  - name: Coupang Open API
    description: The Coupang Open API is a RESTful seller (vendor) API for managing the full marketplace lifecycle including product catalog creation, order processing, return and cancellation handling, settlement queries, and customer inquiries. Authentication uses HMAC-signed Authorization headers with an X-Requested-By header issued from the WING seller portal.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.coupangcorp.com/
    baseURL: https://api-gateway.coupang.com
    tags:
      - HMAC
      - Marketplace
      - Open API
      - Orders
      - Products
      - REST
      - Sellers
      - Vendors
    properties:
      - type: Documentation
        url: https://developers.coupangcorp.com/
      - type: GettingStarted
        url: https://developers.coupangcorp.com/hc/en-us/articles/360033917473-Coupang-OPEN-API
      - type: TestGuide
        url: https://developers.coupangcorp.com/hc/en-us/articles/360033988873-OPEN-API-Test-Guide
      - type: ProductAPI
        url: https://developers.coupangcorp.com/hc/en-us/sections/360004260614-Product-API
      - type: ReturnAPI
        url: https://developers.coupangcorp.com/hc/en-us/sections/360004302273-Return-API
      - type: SettlementAPI
        url: https://developers.coupangcorp.com/hc/en-us/articles/360034152213-Settlement-Detail-Query
      - type: ProductListingGuide
        url: https://developers.coupangcorp.com/hc/en-us/articles/360034889893-OPEN-API-Product-Listing-Guide
      - type: FAQ
        url: https://developers.coupangcorp.com/hc/en-us/categories/360001818893-FAQs
    features:
      - name: HMAC Authentication
        description: Requests are signed using HMAC-SHA256 with the Open API key issued from WING.
      - name: Vendor-Scoped Endpoints
        description: All operations are scoped to a vendor ID issued by Coupang.
      - name: Full Marketplace Lifecycle
        description: Product catalog, order processing, returns, cancellations, settlements, and inquiries.
    useCases:
      - name: Seller Inventory Sync
        description: Synchronize SKUs and inventory between an external commerce platform and Coupang.
      - name: Order Fulfillment Automation
        description: Pull new orders, push shipping confirmations, and manage cancellations and returns.
      - name: Settlement Reconciliation
        description: Pull settlement histories for finance and accounting reconciliation.
    contact:
      - type: Support
        url: https://developers.coupangcorp.com/hc/en-us
common:
  - type: Website
    url: https://www.coupang.com
  - type: DeveloperPortal
    url: https://developers.coupangcorp.com/
  - type: SellerPortal
    url: https://wing.coupang.com/
  - type: About
    url: https://www.aboutcoupang.com/
  - type: TermsOfService
    url: https://www.coupang.com/np/policies/terms
  - type: PrivacyPolicy
    url: https://www.coupang.com/np/policies/privacy
  - type: LinkedIn
    url: https://www.linkedin.com/company/coupang
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
