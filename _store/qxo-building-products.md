---
aid: qxo-building-products
name: QXO Building Products
description: QXO is a publicly traded company focused on building a tech-forward leader in the building products distribution industry through acquisitions and operational improvements. QXO offers a suite of customer-facing APIs for ordering, pricing, account management, product catalog, delivery tracking, and invoicing.
type: Index
url: https://raw.githubusercontent.com/api-evangelist/qxo-building-products/refs/heads/main/apis.yml
tags:
  - Building Products
  - Distribution
  - B2B
  - Construction
  - Fortune 500
scope:
  type: Contract
  position: Consuming
  access: 3rd-Party
created: '2026-03-21'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: qxo-building-products:order-api
    name: QXO Order API
    description: Enables customers to place material orders and track order status and deliveries within their own systems.
    humanURL: https://www.qxo.com/customapi
    tags:
      - Orders
      - Ordering
      - B2B
    properties:
      - type: Documentation
        url: https://www.qxo.com/customapi
      - type: SignUp
        url: https://go.qxo.com/qxoapi
  - aid: qxo-building-products:pricing-api
    name: QXO Pricing API
    description: Provides real-time pricing information for single or multiple QXO products to simplify the process of generating estimates.
    humanURL: https://www.qxo.com/customapi
    tags:
      - Pricing
      - Estimates
      - B2B
    properties:
      - type: Documentation
        url: https://www.qxo.com/customapi
      - type: SignUp
        url: https://go.qxo.com/qxoapi
  - aid: qxo-building-products:account-api
    name: QXO Account API
    description: Provides access to customer account information including billing addresses, contacts, and other account details.
    humanURL: https://www.qxo.com/customapi
    tags:
      - Accounts
      - Customers
      - B2B
    properties:
      - type: Documentation
        url: https://www.qxo.com/customapi
      - type: SignUp
        url: https://go.qxo.com/qxoapi
  - aid: qxo-building-products:product-api
    name: QXO Product API
    description: Browse the QXO product catalog to access product details and check availability across multiple product hierarchies.
    humanURL: https://www.qxo.com/customapi
    tags:
      - Products
      - Catalog
      - Inventory
    properties:
      - type: Documentation
        url: https://www.qxo.com/customapi
      - type: SignUp
        url: https://go.qxo.com/qxoapi
  - aid: qxo-building-products:delivery-tracking-api
    name: QXO Delivery Tracking API
    description: Track material order status and receive delivery photos via email for project management.
    humanURL: https://www.qxo.com/customapi
    tags:
      - Delivery
      - Tracking
      - Logistics
    properties:
      - type: Documentation
        url: https://www.qxo.com/customapi
      - type: SignUp
        url: https://go.qxo.com/qxoapi
  - aid: qxo-building-products:invoice-api
    name: QXO Invoice API
    description: Provides access to invoices, payment status, and financial information.
    humanURL: https://www.qxo.com/customapi
    tags:
      - Invoices
      - Billing
      - Payments
    properties:
      - type: Documentation
        url: https://www.qxo.com/customapi
      - type: SignUp
        url: https://go.qxo.com/qxoapi
common:
  - type: Website
    url: https://www.qxo.com
  - type: Developer
    url: https://www.qxo.com/customapi
  - type: SignUp
    url: https://go.qxo.com/qxoapi
  - type: Integrations
    url: https://www.qxo.com/integrations
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
