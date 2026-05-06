---
aid: csg
url: https://raw.githubusercontent.com/api-evangelist/csg/refs/heads/main/apis.yml
x-type: company
name: CSG Systems
description: CSG is a global provider of customer engagement, revenue management, and payments solutions enabling communications, media, and entertainment companies to monetize and digitally enable customer experiences. CSG's developer surface includes the CSG Forte payments REST API, Forte.js client-side tokenization library, the Forte React Native SDK, and the Singleview convergent billing platform.
image: https://raw.githubusercontent.com/api-evangelist/csg/refs/heads/main/image.png
tags:
  - Billing
  - Customer Engagement
  - Payments
  - Revenue Management
  - Telecom
type: Index
access: 3rd-Party
specificationVersion: '0.19'
created: '2026-03-18'
modified: '2026-04-28'
apis:
  - aid: csg:csg-forte-rest-api
    name: CSG Forte REST API
    description: CSG Forte provides full-stack REST APIs for payment processing within a PCI-compliant architecture. The API enables merchants and partners to create and update credit card, echeck, and scheduled transactions, securely manage customer and payment data, and query settlement information. Authentication uses HTTP Basic with organization ID, location ID, and API key.
    image: https://raw.githubusercontent.com/api-evangelist/csg/refs/heads/main/image.png
    humanURL: https://developers.forte.net/
    baseURL: https://api.forte.net/v3
    tags:
      - ACH
      - Billing
      - Credit Card
      - Payments
      - PCI
      - REST
    properties:
      - url: https://developers.forte.net/introduction-rest-api/
        type: Documentation
      - url: https://restdocs.forte.net/
        type: Reference
      - url: https://developers.forte.net/getting-started/
        type: GettingStarted
      - url: https://www.forte.net/test-account-setup/
        type: Sandbox
      - url: https://releases.forte.net/
        type: ChangeLog
      - url: https://status.forte.net/
        type: Status
      - url: https://support.forte.net/
        type: Support
      - url: https://training.forte.net/
        type: Training
      - url: openapi/csg-forte-rest-openapi.yml
        type: OpenAPI
      - url: json-schema/csg-forte-transaction-schema.json
        type: JSONSchema
      - url: json-ld/csg-context.jsonld
        type: JSONLDContext
  - aid: csg:csg-forte-js
    name: CSG Forte.js
    description: Forte.js is a JavaScript library for secure browser-based payment tokenization. It enables web applications to collect and tokenize payment card data client-side before submitting to Forte's payment API, reducing PCI scope.
    image: https://raw.githubusercontent.com/api-evangelist/csg/refs/heads/main/image.png
    humanURL: https://developers.forte.net/forte-js/
    baseURL: https://api.forte.net
    tags:
      - JavaScript
      - Payments
      - SDK
      - Web
    properties:
      - url: https://developers.forte.net/forte-js/
        type: Documentation
  - aid: csg:csg-forte-react-native-sdk
    name: CSG Forte React Native SDK
    description: The Forte React Native SDK enables mobile application developers to integrate payment processing capabilities into iOS and Android apps built with React Native.
    image: https://raw.githubusercontent.com/api-evangelist/csg/refs/heads/main/image.png
    humanURL: https://developers.forte.net/forte-react-native/
    baseURL: https://api.forte.net
    tags:
      - Mobile
      - Payments
      - React Native
      - SDK
    properties:
      - url: https://developers.forte.net/forte-react-native/
        type: Documentation
      - url: https://developers.forte.net/forte-react-native/
        type: SDKs
  - aid: csg:csg-singleview-api
    name: CSG Singleview Billing API
    description: CSG Singleview is a comprehensive convergent billing and revenue management platform designed for communication service providers. APIs enable subscriber billing, usage rating, invoice generation, and payment processing across converged 5G and IoT services.
    image: https://raw.githubusercontent.com/api-evangelist/csg/refs/heads/main/image.png
    humanURL: https://www.csgi.com/
    baseURL: https://api.csgi.com
    tags:
      - Billing
      - BSS
      - Revenue Management
      - SOAP
      - Telecom
    properties:
      - url: https://www.csgi.com/
        type: Documentation
features:
  - name: PCI-Scoped Payment Processing
    description: REST endpoints for credit card, echeck, and scheduled transactions inside a PCI-compliant architecture.
  - name: Customer and Payment Method Management
    description: Tokenize and store customer payment methods for repeat billing.
  - name: Settlement and Reconciliation
    description: Query settlement records to reconcile funded transactions.
  - name: Browser Tokenization
    description: Forte.js client-side tokenization to keep payment data out of merchant servers.
  - name: Mobile SDKs
    description: React Native SDK for integrating payments into iOS and Android apps.
  - name: Convergent Billing
    description: CSG Singleview supports subscriber billing, rating, and invoicing across 5G and IoT services.
  - name: Sandbox Environment
    description: Forte sandbox at sandbox.forte.net/api/v3 for development and integration testing.
useCases:
  - name: Merchant Payments
    description: B2B and SaaS merchants accept credit card and ACH payments via Forte.
  - name: Recurring Billing
    description: Schedule recurring transactions for subscription billing.
  - name: Mobile Checkout
    description: Mobile apps tokenize cards using the React Native SDK and charge through Forte.
  - name: Telecom Billing
    description: Communication service providers run subscriber billing on Singleview across 5G and IoT.
  - name: Marketplace Payouts
    description: Platforms reconcile and settle funds across many merchant locations.
common:
  - url: https://www.csgi.com/
    type: Website
  - url: openapi/csg-forte-rest-openapi.yml
    type: OpenAPI
  - url: json-schema/csg-forte-transaction-schema.json
    type: JSONSchema
  - url: json-ld/csg-context.jsonld
    type: JSONLDContext
  - url: rules/csg-forte-rules.yml
    type: SpectralRules
  - url: vocabulary/csg-forte-vocabulary.yml
    type: Vocabulary
  - url: https://www.forte.net/developers/
    type: Portal
  - url: https://developers.forte.net/
    type: Documentation
  - url: https://restdocs.forte.net/
    type: Reference
  - url: https://support.forte.net/
    type: Support
  - url: https://status.forte.net/
    type: Status
  - url: https://releases.forte.net/
    type: ChangeLog
  - url: https://www.forte.net/test-account-setup/
    type: GettingStarted
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
