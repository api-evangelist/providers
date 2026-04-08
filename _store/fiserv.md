---
aid: fiserv
url: https://raw.githubusercontent.com/api-evangelist/fiserv/refs/heads/main/apis.yml
apis:
- aid: fiserv:commercehub
  name: Fiserv CommerceHub API
  tags:
  - 3-D Secure
  - Commerce
  - Payments
  - Tokenization
  humanURL: https://developer.fiserv.com/product/CommerceHub
  properties:
  - url: https://developer.fiserv.com/product/CommerceHub/docs/?path=docs/Resources/API-Documents/Use-Our-APIs.md
    type: Documentation
  - url: openapi/fiserv-commercehub-openapi.yml
    type: OpenAPI
  description: The Fiserv CommerceHub API provides a unified RESTful interface for processing payments, managing tokens, verifying payment sources, and handling 3-D Secure authentication. CommerceHub enables merchants to accept payments through multiple channels including online, mobile, and in-app, with support for charges, pre-authorizations, captures, refunds, cancellations, and tokenization of payment credentials.
- aid: fiserv:cardpointe-gateway
  name: Fiserv CardPointe Gateway API
  tags:
  - Gateway
  - Payments
  - Point of Sale
  - Tokenization
  humanURL: https://developer.fiserv.com/product/CardPointe
  properties:
  - url: https://developer.fiserv.com/product/CardPointe/docs/?path=docs%2FAPIs%2FCardPointeGatewayAPI.md
    type: Documentation
  - url: openapi/fiserv-cardpointe-gateway-openapi.yml
    type: OpenAPI
  description: The CardPointe Gateway API provides a RESTful interface for integrating secure tokenization, payment processing, and reporting features into applications and websites. The API supports authorization, capture, void, refund, and inquiry operations, as well as customer profile management for storing payment credentials securely.
- aid: fiserv:bankinghub
  name: Fiserv BankingHub API
  tags:
  - Accounts
  - Banking
  - Payments
  - Transfers
  humanURL: https://developer.fiserv.com/product/BankingHub
  properties:
  - url: https://developer.fiserv.com/product/BankingHub/docs/?path=docs/get-started.md
    type: Documentation
  - url: openapi/fiserv-bankinghub-openapi.yml
    type: OpenAPI
  description: The Fiserv BankingHub API provides RESTful access to core banking operations including account management, transactions, transfers, payments, and party (customer) management. BankingHub enables financial institutions and fintech partners to integrate account opening, fund transfers, payment processing, and customer data management into their applications.
- aid: fiserv:carddeveloper
  name: Fiserv CardDeveloper API
  tags:
  - Accounts
  - Authorizations
  - Cards
  - Statements
  humanURL: https://developer.fiserv.com/product/CardDeveloper
  properties:
  - url: https://developer.fiserv.com/product/CardDeveloper/docs/?path=docs/gettingstarted/getting-started.md
    type: Documentation
  - url: openapi/fiserv-carddeveloper-openapi.yml
    type: OpenAPI
  description: The Fiserv CardDeveloper API enables financial institutions and cardholders to manage card and account information through various touchpoints. The API supports account creation, card management, authorization management, transaction inquiry, limit management, and statement retrieval for credit and debit card programs.
- aid: fiserv:payment-events
  name: Fiserv Payment Events
  tags:
  - Disputes
  - Events
  - Payments
  - Webhooks
  humanURL: https://docs.fiserv.dev/public/docs/webhooks-and-status-updates-checkout
  properties:
  - url: https://docs.fiserv.dev/public/docs/webhooks-and-status-updates-checkout
    type: Documentation
  - url: asyncapi/fiserv-payment-events-asyncapi.yml
    type: AsyncAPI
  description: Fiserv provides webhook-based event notifications across the payments lifecycle. Merchants can subscribe to webhooks to receive real-time notifications for key events including transaction status changes, settlement updates, dispute notifications, and checkout completions.
name: Fiserv
tags:
- Banking
- Financial
- Payments
- Wealth Management
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-17'
modified: '2026-04-07'
position: Consumer
description: Fiserv is a global provider of financial services technology solutions, offering a wide range of products and services to help clients in the banking, payments, and wealth management industries.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

