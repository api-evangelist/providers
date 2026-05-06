---
aid: vtex
url: https://raw.githubusercontent.com/api-evangelist/vtex/refs/heads/main/apis.yml
name: VTEX
description: VTEX is a global enterprise digital commerce platform that provides end-to-end solutions for businesses to create, manage, and scale their online stores. Founded in Brazil, VTEX serves thousands of merchants across 38 countries with capabilities spanning catalog management, checkout, payments, logistics, marketplace, promotions, search, and customer identity. The platform offers an extensive API ecosystem enabling headless commerce, composable architectures, and deep integrations with third-party tools and marketplaces.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Commerce
  - E-Commerce
  - Retail
  - Marketplace
  - Payments
created: '2024-06-07'
modified: '2026-05-04'
specificationVersion: '0.19'
type: Contract
access: 3rd-Party
position: Consuming
apis:
  - aid: vtex:vtex-anti-fraud-provider-api
    name: VTEX Anti-Fraud Provider API
    description: The VTEX Anti-Fraud Provider API defines the integration protocol between VTEX and anti-fraud providers. It enables third-party anti-fraud services to connect with the VTEX payment ecosystem, receive transaction data, assess fraud risk, and return risk scores and recommendations in real time.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/how-the-integration-protocol-between-vtex-and-antifraud-companies-works
    baseURL: https://{providerApiEndpoint}
    tags:
      - Anti-Fraud
      - Fraud Prevention
      - Payments
      - Security
    properties:
      - url: openapi/vtex-anti-fraud-provider-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/how-the-integration-protocol-between-vtex-and-antifraud-companies-works
        type: Documentation
  - aid: vtex:vtex-buyer-organization-api
    name: VTEX Buyer Organization API
    description: The VTEX Buyer Organization API enables B2B commerce capabilities by allowing businesses to manage buyer organizations, their members, roles, and cost centers. It supports bulk import of buyer organizations and manages permissions for B2B purchasing workflows.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/bulk-import-buyer-organizations-spreadsheet
    baseURL: https://{accountName}.{environment}.com.br
    tags:
      - B2B
      - Commerce
      - Organizations
      - Purchasing
    properties:
      - url: openapi/vtex-buyer-organization-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/bulk-import-buyer-organizations-spreadsheet
        type: Documentation
  - aid: vtex:vtex-catalog-api-seller-portal
    name: VTEX Catalog API - Seller Portal
    description: The VTEX Catalog API for Seller Portal provides endpoints for sellers to manage their product catalog within the VTEX seller portal experience. It enables product creation, category mapping, attribute management, and SKU synchronization between seller catalogs and marketplace catalogs.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/catalog-api-seller-portal-overview
    baseURL: https://{accountName}.{environment}.com.br
    tags:
      - Catalog
      - Commerce
      - Marketplace
      - Seller
    properties:
      - url: openapi/vtex-catalog-api-seller-portal-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/catalog-api-seller-portal-overview
        type: Documentation
  - aid: vtex:vtex-catalog-api
    name: VTEX Catalog API
    description: The VTEX Catalog API provides comprehensive product catalog management for VTEX stores. It covers categories, brands, products, SKUs, product specifications, product images, product attachments, and collection management. This is the primary API for building and maintaining product catalogs in VTEX.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/catalog-overview
    baseURL: https://{accountName}.{environment}.com.br
    tags:
      - Catalog
      - Commerce
      - Products
      - SKU
    properties:
      - url: openapi/vtex-catalog-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/catalog-overview
        type: Documentation
  - aid: vtex:vtex-checkout-api
    name: VTEX Checkout API
    description: The VTEX Checkout API manages the complete checkout lifecycle for VTEX stores. It handles cart management, order simulation, address validation, payment selection, order placement, and cart attachment operations. This API is central to the purchase flow in any VTEX storefront.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/checkout-overview
    baseURL: https://{accountName}.{environment}.com.br
    tags:
      - Cart
      - Checkout
      - Commerce
      - Orders
    properties:
      - url: openapi/vtex-checkout-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/checkout-overview
        type: Documentation
  - aid: vtex:vtex-customer-credit-api
    name: VTEX Customer Credit API
    description: The VTEX Customer Credit API manages credit lines for B2B and B2C customers. It enables merchants to create credit accounts, set credit limits, track outstanding balances, open and close invoices, and manage credit terms. Useful for businesses that extend net-terms or credit facilities to their buyers.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://help.vtex.com/en/tutorial/customer-credit-overview--1uIqTjWxIIIEW0COMg4uE0
    baseURL: https://{accountName}.{environment}.com.br
    tags:
      - B2B
      - Commerce
      - Credit
      - Finance
    properties:
      - url: openapi/vtex-customer-credit-openapi-original.yml
        type: OpenAPI
      - url: https://help.vtex.com/en/tutorial/customer-credit-overview--1uIqTjWxIIIEW0COMg4uE0
        type: Documentation
  - aid: vtex:vtex-data-subject-rights-api
    name: VTEX Data Subject Rights API
    description: The VTEX Data Subject Rights API enables GDPR and LGPD compliance by allowing organizations to process data subject requests. It supports the right to access, rectify, erase, and restrict processing of personal data stored in VTEX systems.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://help.vtex.com/en/tutorial/data-subject-rights--6imchxTx09icupKMbzHVIM
    baseURL: https://api.vtex.com
    tags:
      - Compliance
      - Data Privacy
      - GDPR
      - Privacy
    properties:
      - url: openapi/vtex-data-subject-rights-openapi-original.yml
        type: OpenAPI
      - url: https://help.vtex.com/en/tutorial/data-subject-rights--6imchxTx09icupKMbzHVIM
        type: Documentation
  - aid: vtex:vtex-do-api
    name: VTEX DO API
    description: The VTEX DO API provides task and note management capabilities for VTEX store operators. It allows creating, updating, listing, and deleting tasks and notes associated with orders and other store objects, enabling internal operational workflows.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/api-reference/do-api
    baseURL: https://{accountName}.{environment}.com.br/api/do
    tags:
      - Commerce
      - Operations
      - Tasks
      - Workflow
    properties:
      - url: openapi/vtex-do-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/api-reference/do-api
        type: Documentation
  - aid: vtex:vtex-gift-card-hub-api
    name: VTEX Gift Card Hub API
    description: The VTEX Gift Card Hub API provides a central integration point for managing gift card providers on the VTEX platform. It enables merchants to list, activate, and deactivate gift card providers, and process gift card transactions through a unified interface.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/managing-vtex-gift-cards
    baseURL: https://{accountName}.{environment}.com.br
    tags:
      - Commerce
      - Gift Cards
      - Payments
      - Promotions
    properties:
      - url: openapi/vtex-gift-card-hub-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/managing-vtex-gift-cards
        type: Documentation
  - aid: vtex:vtex-gift-card-api
    name: VTEX Gift Card API
    description: The VTEX Gift Card API manages the lifecycle of gift cards within the VTEX native gift card provider. It supports creating, redeeming, crediting, debiting, and canceling gift card transactions, as well as listing and retrieving gift card information.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/managing-vtex-gift-cards
    baseURL: https://{accountName}.{environment}.com.br/api/
    tags:
      - Commerce
      - Gift Cards
      - Payments
      - Promotions
    properties:
      - url: openapi/vtex-gift-card-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/managing-vtex-gift-cards
        type: Documentation
  - aid: vtex:vtex-gift-card-provider-protocol-api
    name: VTEX Gift Card Provider Protocol API
    description: The VTEX Gift Card Provider Protocol defines the interface for integrating external gift card providers with VTEX. It specifies the endpoints external providers must implement to handle gift card transactions, balance checks, and redemption flows within VTEX checkout.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/gift-card-integration-guide
    baseURL: https://{providerApiEndpoint}
    tags:
      - Commerce
      - Gift Cards
      - Integration
      - Payments
    properties:
      - url: openapi/vtex-gift-card-provider-protocol-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/gift-card-integration-guide
        type: Documentation
  - aid: vtex:vtex-headless-cms-api
    name: VTEX Headless CMS API
    description: The VTEX Headless CMS API provides content management capabilities for FastStore and headless VTEX storefronts. It enables managing CMS pages, sections, content types, and building blocks that compose headless commerce experiences.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/faststore/headless-cms-overview
    baseURL: https://{accountName}.myvtex.com
    tags:
      - CMS
      - Commerce
      - Content Management
      - Headless
    properties:
      - url: openapi/vtex-headless-cms-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/faststore/headless-cms-overview
        type: Documentation
  - aid: vtex:vtex-id-api
    name: VTEX ID API
    description: The VTEX ID API provides authentication and identity management for VTEX stores. It handles user login, token generation, authentication renewal, and password management for customers, store operators, and API integrations.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/api-reference/vtex-id-api
    baseURL: https://{accountName}.{environment}.com.br
    tags:
      - Authentication
      - Commerce
      - Identity
      - Security
    properties:
      - url: openapi/vtex-id-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/api-reference/vtex-id-api
        type: Documentation
  - aid: vtex:vtex-intelligent-search-events-api
    name: VTEX Intelligent Search Events API
    description: The VTEX Intelligent Search Events API captures behavioral signals from shoppers to improve search relevance. It collects events such as search queries, product clicks, and purchase completions to feed the machine learning models powering VTEX Intelligent Search.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG
    baseURL: https://sp.vtex.com/event-api/v1/{accountName}
    tags:
      - Analytics
      - Commerce
      - Events
      - Search
    properties:
      - url: openapi/vtex-intelligent-search-events-openapi-original.yml
        type: OpenAPI
      - url: https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG
        type: Documentation
  - aid: vtex:vtex-intelligent-search-api
    name: VTEX Intelligent Search API
    description: The VTEX Intelligent Search API delivers AI-powered search and product discovery features for VTEX storefronts. It provides product search with faceted filtering, autocomplete suggestions, banners, product recommendations, and spelling correction powered by machine learning.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/apps/vtex.search@1.0.8
    baseURL: https://{accountName}.{environment}.com.br/api/io/_v/api/intelligent-search
    tags:
      - AI
      - Commerce
      - Product Discovery
      - Search
    properties:
      - url: openapi/vtex-intelligent-search-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/apps/vtex.search@1.0.8
        type: Documentation
  - aid: vtex:vtex-legacy-cms-portal-api
    name: VTEX Legacy CMS Portal API
    description: The VTEX Legacy CMS Portal API provides access to the classic VTEX CMS system used in traditional VTEX stores. It enables managing HTML templates, site structure, shelves, and custom pages within the legacy CMS portal.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/1oN446gRGcR2s70RvBCAmj
    baseURL: https://{accountName}.{environment}.com.br
    tags:
      - CMS
      - Commerce
      - Content Management
      - Legacy
    properties:
      - url: openapi/vtex-legacy-cms-portal-openapi-original.yml
        type: OpenAPI
      - url: https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/1oN446gRGcR2s70RvBCAmj
        type: Documentation
  - aid: vtex:vtex-legacy-search-api
    name: VTEX Legacy Search API
    description: The VTEX Legacy Search API supports product search and discovery for traditional VTEX storefronts not yet migrated to Intelligent Search. It provides catalog browsing, text search, faceted filtering, category navigation, and product listing page capabilities.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/search-overview
    baseURL: https://{accountName}.{environment}.com.br
    tags:
      - Catalog
      - Commerce
      - Legacy
      - Search
    properties:
      - url: openapi/vtex-legacy-search-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/search-overview
        type: Documentation
  - aid: vtex:vtex-license-manager-api
    name: VTEX License Manager API
    description: The VTEX License Manager API manages access control and permissions within the VTEX platform. It handles user accounts, roles, resources, app permissions, and account access tokens, serving as the primary authorization layer for VTEX administrative operations.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3
    baseURL: https://{accountName}.{environment}.com.br
    tags:
      - Access Control
      - Authorization
      - Commerce
      - Permissions
    properties:
      - url: openapi/vtex-license-manager-openapi-original.yml
        type: OpenAPI
      - url: https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3
        type: Documentation
  - aid: vtex:vtex-logistics-api
    name: VTEX Logistics API
    description: The VTEX Logistics API manages the complete fulfillment infrastructure for VTEX stores. It covers warehouses, inventory management, shipping carriers, freight calculations, pickup points, geolocation zones, scheduled delivery windows, and dock management to support complex omnichannel fulfillment scenarios.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/fulfillment
    baseURL: https://{accountName}.{environment}.com.br
    tags:
      - Commerce
      - Fulfillment
      - Inventory
      - Logistics
    properties:
      - url: openapi/vtex-logistics-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/fulfillment
        type: Documentation
  - aid: vtex:vtex-marketplace-api
    name: VTEX Marketplace API
    description: The VTEX Marketplace API manages the relationships and operations between VTEX marketplaces and their sellers. It supports seller onboarding, offer management, seller portal access, and the coordination of catalog and order flows between marketplace operators and their sellers.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/marketplace-overview
    baseURL: https://{accountName}.{environment}.com.br/api
    tags:
      - Commerce
      - Marketplace
      - Multi-Seller
      - Retail
    properties:
      - url: openapi/vtex-marketplace-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/marketplace-overview
        type: Documentation
  - aid: vtex:vtex-marketplace-protocol-external-mapper-api
    name: VTEX Marketplace Protocol - External Mapper API
    description: The VTEX Marketplace Protocol External Mapper API defines the catalog mapping protocol for external marketplace connectors. It enables synchronization of product categories, brands, and specifications between external marketplace catalogs and the VTEX catalog.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/updates/release-notes/marketplace-protocol-documentation-update
    baseURL: https://portal.{environment}.com.br
    tags:
      - Catalog
      - Integration
      - Marketplace
      - Protocol
    properties:
      - url: openapi/vtex-marketplace-protocol-external-mapper-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/updates/release-notes/marketplace-protocol-documentation-update
        type: Documentation
  - aid: vtex:vtex-marketplace-protocol-external-orders-api
    name: VTEX Marketplace Protocol - External Orders API
    description: The VTEX Marketplace Protocol External Orders API defines the order flow protocol for external marketplace integrations. It specifies how external marketplaces send orders to VTEX sellers, handle order status updates, and manage cancellations.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/external-marketplace-integration-guide
    baseURL: https://{accountName}.{environment}.com.br
    tags:
      - Integration
      - Marketplace
      - Orders
      - Protocol
    properties:
      - url: openapi/vtex-marketplace-protocol-external-orders-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/external-marketplace-integration-guide
        type: Documentation
  - aid: vtex:vtex-marketplace-protocol-external-seller-fulfillment-api
    name: VTEX Marketplace Protocol - External Seller Fulfillment API
    description: The VTEX Marketplace Protocol External Seller Fulfillment API defines endpoints that external sellers must implement to receive and fulfill orders from VTEX marketplaces. It covers order notification, fulfillment status updates, and delivery tracking callbacks.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/external-seller-integration-connector
    baseURL: https://{fulfillmentEndpoint}
    tags:
      - Fulfillment
      - Integration
      - Marketplace
      - Seller
    properties:
      - url: openapi/vtex-marketplace-protocol-external-seller-fulfillment-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/external-seller-integration-connector
        type: Documentation
  - aid: vtex:vtex-marketplace-protocol-external-seller-marketplace-api
    name: VTEX Marketplace Protocol - External Seller Marketplace API
    description: The VTEX Marketplace Protocol External Seller Marketplace API defines the protocol for VTEX acting as a seller on external marketplaces. It enables VTEX stores to list products, receive orders, and send fulfillment updates to external marketplace platforms.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/external-seller-integration-guide
    baseURL: https://{marketplaceServicesEndpoint}
    tags:
      - Integration
      - Marketplace
      - Protocol
      - Seller
    properties:
      - url: openapi/vtex-marketplace-protocol-external-seller-marketplace-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/external-seller-integration-guide
        type: Documentation
  - aid: vtex:vtex-master-data-api
    name: VTEX Master Data API
    description: The VTEX Master Data API is a NoSQL document store built into the VTEX platform. It provides schema-flexible data entity management with CRUD operations, full-text search, and indexing. Used for storing customer profiles, wishlists, subscriptions, and custom business data.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw
    baseURL: https://{accountName}.{environment}.com.br
    tags:
      - Commerce
      - Customer Data
      - Data Management
      - NoSQL
    properties:
      - url: openapi/vtex-master-data-openapi-original.yml
        type: OpenAPI
      - url: https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw
        type: Documentation
  - aid: vtex:vtex-message-center-api
    name: VTEX Message Center API
    description: The VTEX Message Center API manages transactional email templates and message flows for VTEX stores. It handles email template management and message triggers for order confirmations, shipping notifications, and other transactional communications.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://help.vtex.com/en/tutorial/understanding-the-message-center--tutorials_84
    baseURL: https://{accountName}.{environment}.com.br
    tags:
      - Commerce
      - Email
      - Messaging
      - Notifications
    properties:
      - url: openapi/vtex-message-center-openapi-original.yml
        type: OpenAPI
      - url: https://help.vtex.com/en/tutorial/understanding-the-message-center--tutorials_84
        type: Documentation
  - aid: vtex:vtex-orders-api
    name: VTEX Orders API
    description: The VTEX Orders API provides comprehensive order management for VTEX stores. It enables listing, retrieving, filtering, and updating orders, managing order lifecycle events, processing cancellations, handling returns, and generating order invoices. This API is the backbone of post-purchase operations.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/orders-overview
    baseURL: https://{accountName}.{environment}.com.br
    tags:
      - Commerce
      - Fulfillment
      - Order Management
      - Orders
    properties:
      - url: openapi/vtex-orders-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/orders-overview
        type: Documentation
  - aid: vtex:vtex-orders-pii-api
    name: VTEX Orders API - PII Data Architecture
    description: The VTEX Orders API PII variant supports VTEX stores using the PII data architecture where sensitive customer data is stored encrypted. It provides the same order management capabilities as the standard Orders API but with PII-compliant data handling for GDPR and LGPD requirements.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/changes-in-vtex-features-behavior-to-handle-pii-data
    baseURL: https://{accountName}.{environment}.com.br
    tags:
      - Commerce
      - Data Privacy
      - Orders
      - PII
    properties:
      - url: openapi/vtex-orders-pii-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/changes-in-vtex-features-behavior-to-handle-pii-data
        type: Documentation
  - aid: vtex:vtex-payment-provider-protocol-api
    name: VTEX Payment Provider Protocol API
    description: The VTEX Payment Provider Protocol API defines the interface that payment providers must implement to integrate with VTEX checkout. It covers authorization, settlement, refund, and void operations, as well as payment method discovery and 3DS authentication flows.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://help.vtex.com/en/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m
    baseURL: https://{providerApiEndpoint}
    tags:
      - Commerce
      - Fintech
      - Payments
      - Protocol
    properties:
      - url: openapi/vtex-payment-provider-protocol-openapi-original.yml
        type: OpenAPI
      - url: https://help.vtex.com/en/tutorial/payment-provider-protocol--RdsT2spdq80MMwwOeEq0m
        type: Documentation
  - aid: vtex:vtex-payments-gateway-api
    name: VTEX Payments Gateway API
    description: The VTEX Payments Gateway API provides access to the VTEX payment processing infrastructure. It handles payment transaction management, refunds, chargebacks, payment conditions, and anti-fraud integration for payments processed through VTEX stores.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/payments-integration-guide
    baseURL: https://{accountName}.vtexpayments.com.br
    tags:
      - Commerce
      - Fintech
      - Payments
      - Transactions
    properties:
      - url: openapi/vtex-payments-gateway-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/payments-integration-guide
        type: Documentation
  - aid: vtex:vtex-pick-pack-last-mile-protocol-api
    name: VTEX Pick and Pack Last Mile Protocol API
    description: The VTEX Pick and Pack Last Mile Protocol API defines the integration interface for last-mile delivery partners. It enables delivery providers to receive delivery requests, update status, report issues, and manage delivery tracking for the VTEX Pick and Pack fulfillment solution.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://help.vtex.com/en/tutorial/vtex-pick-and-pack-last-mile--HN7WKV0xoq2ssVjsJlfzr
    baseURL: https://auth.pickingnpacking.com/{environment}
    tags:
      - Commerce
      - Delivery
      - Logistics
      - Last Mile
    properties:
      - url: openapi/vtex-pick-pack-last-mile-protocol-openapi-original.yml
        type: OpenAPI
      - url: https://help.vtex.com/en/tutorial/vtex-pick-and-pack-last-mile--HN7WKV0xoq2ssVjsJlfzr
        type: Documentation
  - aid: vtex:vtex-policies-system-api
    name: VTEX Policies System API
    description: The VTEX Policies System API manages reusable policy rules that can be applied across the VTEX platform. Policies define conditional logic for promotions, pricing, catalog visibility, and checkout behaviors, enabling merchants to create flexible rule-based configurations.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/vtex-io-documentation-policies
    baseURL: https://{accountName}.{environment}.com.br
    tags:
      - Commerce
      - Configuration
      - Policies
      - Rules
    properties:
      - url: openapi/vtex-policies-system-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/vtex-io-documentation-policies
        type: Documentation
  - aid: vtex:vtex-pricing-hub-api
    name: VTEX Pricing Hub API
    description: The VTEX Pricing Hub API allows merchants to integrate external pricing engines with VTEX checkout. It defines the protocol for external price providers to receive pricing requests and return custom prices during the checkout simulation process.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/pricing-hub
    baseURL: https://prchub.{environment}.com.br
    tags:
      - Commerce
      - Integration
      - Pricing
      - Protocol
    properties:
      - url: openapi/vtex-pricing-hub-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/pricing-hub
        type: Documentation
  - aid: vtex:vtex-pricing-api
    name: VTEX Pricing API
    description: The VTEX Pricing API manages product pricing configurations for VTEX stores. It handles fixed prices, price tables, trade policies, cost prices, and price rule inheritance, enabling merchants to configure complex pricing scenarios across different customer segments and trade policies.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/pricing-overview
    baseURL: https://api.vtex.com/{accountName}
    tags:
      - Commerce
      - Pricing
      - Retail
      - Trade Policy
    properties:
      - url: openapi/vtex-pricing-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/pricing-overview
        type: Documentation
  - aid: vtex:vtex-profile-system-api
    name: VTEX Profile System API - PII Data Architecture
    description: The VTEX Profile System API manages customer profiles in VTEX stores using the PII data architecture. It provides CRUD operations for shopper profiles, addresses, and payment tokens with privacy-first design that stores sensitive data encrypted and separate from other store data.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/profile-system
    baseURL: https://{accountName}.{environment}.com.br
    tags:
      - Commerce
      - Customer Profiles
      - Data Privacy
      - PII
    properties:
      - url: openapi/vtex-profile-system-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/profile-system
        type: Documentation
  - aid: vtex:vtex-promotions-taxes-api
    name: VTEX Promotions and Taxes API
    description: The VTEX Promotions and Taxes API manages discount campaigns, coupons, gift promotions, and tax configurations for VTEX stores. It supports creating and managing complex promotional rules including cart-level discounts, product-level promotions, and progressive discounts.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/promotions-overview
    baseURL: https://{accountName}.{environment}.com.br
    tags:
      - Commerce
      - Discounts
      - Promotions
      - Taxes
    properties:
      - url: openapi/vtex-promotions-taxes-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/promotions-overview
        type: Documentation
  - aid: vtex:vtex-reviews-ratings-api
    name: VTEX Reviews and Ratings API
    description: The VTEX Reviews and Ratings API manages customer product reviews and star ratings for VTEX stores. It provides endpoints for submitting, retrieving, approving, and moderating reviews, enabling social proof features within VTEX storefronts.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/apps/vtex.reviews-and-ratings
    baseURL: https://{accountName}.myvtex.com
    tags:
      - Commerce
      - Customer Feedback
      - Ratings
      - Reviews
    properties:
      - url: openapi/vtex-reviews-ratings-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/apps/vtex.reviews-and-ratings
        type: Documentation
  - aid: vtex:vtex-sent-offers-api
    name: VTEX Sent Offers API
    description: The VTEX Sent Offers API manages product offers that VTEX sellers send to external marketplaces. It provides visibility into offer synchronization status, error tracking, feed management, and the history of offer interactions between VTEX and connected marketplace channels.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/sent-offers-integration-guide-connectors
    baseURL: https://portal.{environment}.com.br
    tags:
      - Commerce
      - Marketplace
      - Offers
      - Seller
    properties:
      - url: openapi/vtex-sent-offers-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/sent-offers-integration-guide-connectors
        type: Documentation
  - aid: vtex:vtex-sessions-api
    name: VTEX Session Manager API
    description: The VTEX Session Manager API maintains shopping session state across VTEX storefront interactions. Sessions store contextual information such as trade policy, region, campaign audiences, and price table selections that affect catalog visibility, pricing, and promotional eligibility during a shopper's visit.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/sessions-system-overview
    baseURL: https://{accountName}.{environment}.com.br
    tags:
      - Commerce
      - Context
      - Sessions
      - Storefront
    properties:
      - url: openapi/vtex-sessions-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/sessions-system-overview
        type: Documentation
  - aid: vtex:vtex-shipping-network-api
    name: VTEX Shipping Network API
    description: The VTEX Shipping Network API provides access to VTEX's carrier partnership network for shipping label generation and tracking. It enables merchants to create shipments, generate labels through VTEX's contracted carrier network, and track package delivery status.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/vtex-shipping-network
    baseURL: https://app.io.vtex.com
    tags:
      - Commerce
      - Logistics
      - Shipping
      - Tracking
    properties:
      - url: openapi/vtex-shipping-network-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/vtex-shipping-network
        type: Documentation
  - aid: vtex:vtex-sku-bindings-api
    name: VTEX SKU Bindings API
    description: The VTEX SKU Bindings API manages the relationships between SKUs in a marketplace and their corresponding seller SKUs. It provides binding, unbinding, and querying operations for marketplace-seller SKU associations, ensuring accurate product matching across the marketplace ecosystem.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://help.vtex.com/en/tutorial/sku-bindings--1SmrVgNwjJX17hdqwLa0TX
    baseURL: https://{accountName}.{environment}.com.br/api
    tags:
      - Catalog
      - Commerce
      - Marketplace
      - SKU
    properties:
      - url: openapi/vtex-sku-bindings-openapi-original.yml
        type: OpenAPI
      - url: https://help.vtex.com/en/tutorial/sku-bindings--1SmrVgNwjJX17hdqwLa0TX
        type: Documentation
  - aid: vtex:vtex-subscriptions-api
    name: VTEX Subscriptions API
    description: The VTEX Subscriptions API (v3) manages recurring purchase subscriptions for VTEX stores. It provides lifecycle management for subscription plans, subscriber management, subscription order scheduling, frequency configuration, and subscription address and payment updates.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/subscriptions
    baseURL: https://{accountName}.{environment}.com.br
    tags:
      - Commerce
      - Recurring
      - Retail
      - Subscriptions
    properties:
      - url: openapi/vtex-subscriptions-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/subscriptions
        type: Documentation
  - aid: vtex:vtex-suggestions-api
    name: VTEX Suggestions API
    description: The VTEX Suggestions API manages product suggestions from sellers to marketplace operators. It handles the proposal and approval workflow for sellers suggesting new products or modifications to existing marketplace catalog items, streamlining catalog expansion in multi-seller environments.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/apps/vtex.search/suggestions
    baseURL: https://api.vtex.com/{accountName}
    tags:
      - Catalog
      - Commerce
      - Marketplace
      - Seller
    properties:
      - url: openapi/vtex-suggestions-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/apps/vtex.search/suggestions
        type: Documentation
  - aid: vtex:vtex-tracking-api
    name: VTEX Tracking API
    description: The VTEX Tracking API provides real-time package tracking capabilities for VTEX deliveries. It enables shipment registration, delivery status updates, carrier event ingestion, and last-mile tracking data retrieval for the VTEX tracking service.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.vtex.com/docs/guides/vtex-tracking
    baseURL: https://api.vtextracking.com/receiver
    tags:
      - Commerce
      - Logistics
      - Shipping
      - Tracking
    properties:
      - url: openapi/vtex-tracking-openapi-original.yml
        type: OpenAPI
      - url: https://developers.vtex.com/docs/guides/vtex-tracking
        type: Documentation
common:
  - url: https://developers.vtex.com/
    type: Portal
  - url: https://developers.vtex.com/docs/guides
    type: Guides
  - url: https://developers.vtex.com/updates/release-notes
    type: ChangeLog
  - url: https://help.vtex.com/
    type: Support
  - url: https://status.vtex.com/
    type: Status
  - url: https://community.vtex.com/s/
    type: Community
  - url: https://github.com/vtex-apps
    type: GitHubOrg
  - url: https://developers.vtex.com/docs/apps
    type: SDK
  - url: https://vtex.com/en-us/partners/
    type: Partners
  - url: https://vtex.com/en-us/blog/
    type: Blog
  - url: https://help.vtex.com/en/support
    type: Support Plan
  - url: rules/vtex-rules.yml
    type: SpectralRules
  - url: vocabulary/vtex-vocabulary.yml
    type: Vocabulary
  - url: json-ld/vtex-context.jsonld
    type: JSONLDContext
  - url: capabilities/store-operations.yaml
    type: NaftikoCapability
  - url: capabilities/catalog-management.yaml
    type: NaftikoCapability
  - url: capabilities/payment-processing.yaml
    type: NaftikoCapability
  - type: Features
    data:
      - 'Starter subscription: $250-$500/mo minimum + GMV fees'
      - 'Enterprise: outcome-based GMV pricing, avg $134K/year'
      - B2C and B2B Composable Commerce platform
      - REST API at {accountname}.vtexcommercestable.com.br
      - 'Default rate limit: 5,000 req/min (endpoint-specific lower)'
      - Catalog/Search/Order Management with own rate limits
      - OMS (Order Management System) built in
      - PIM (Product Information Management)
      - Marketplace as Operator (1P + 3P sellers)
      - Marketplace as Seller
      - Headless storefronts (FastStore for React/Next.js)
      - Live Shopping
      - Subscription/recurring orders
      - Social Commerce (Instagram, WhatsApp, TikTok)
      - Data residency in multiple regions
      - AppKey/AppToken auth
    sources:
      - https://www.vtex.com/pricing/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
