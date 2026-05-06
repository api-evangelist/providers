---
aid: heartland-payment-systems
name: Heartland Payment Systems
description: Heartland Payment Systems is a payment processing company offering payroll, customer engagement, point-of-sale, and other business solutions to merchants across the United States. Heartland is now a brand of Global Payments, and developer resources for Heartland integrations are published through the Global Payments developer portal. The platform supports online and in-person payments, bill pay, IoT/connected device payments, gift and loyalty, payroll, and PCI-validated point-to-point encryption.
url: https://raw.githubusercontent.com/api-evangelist/heartland-payment-systems/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Bill Pay
  - Card Present
  - Card Not Present
  - Ecommerce
  - Payment Processing
  - Payments
  - Payroll
  - Point of Sale
created: '2025'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: heartland-payment-systems:portico-api
    name: Heartland Portico Gateway API
    description: The Portico Gateway is Heartland's primary payment processing API for card-not-present and ecommerce transactions, supporting authorization, capture, refund, void, recurring billing, tokenization, and fraud prevention.
    humanURL: https://developer.globalpayments.com/heartland/getting-started/overview
    tags:
      - Card Not Present
      - Ecommerce
      - Payments
      - Tokenization
    properties:
      - type: Documentation
        url: https://developer.globalpayments.com/heartland/getting-started/overview
      - type: GettingStarted
        url: https://developer.globalpayments.com/heartland/getting-started/overview
  - aid: heartland-payment-systems:card-present-api
    name: Heartland Card Present API
    description: Heartland's Card Present APIs support both semi-integrated and fully-integrated EMV solutions for in-person payments, including terminal SDKs, P2PE, and PIN debit handling.
    humanURL: https://developer.globalpayments.com/heartland/getting-started/overview
    tags:
      - Card Present
      - EMV
      - In-Person Payments
      - Terminals
    properties:
      - type: Documentation
        url: https://developer.globalpayments.com/heartland/getting-started/overview
  - aid: heartland-payment-systems:bill-pay-api
    name: Heartland Bill Pay API
    description: The Heartland Bill Pay API enables invoice and bill payment processing for merchants accepting recurring or one-time bill payments from customers across multiple channels.
    humanURL: https://developer.globalpayments.com/heartland/getting-started/overview
    tags:
      - Bill Pay
      - Invoicing
      - Recurring Payments
    properties:
      - type: Documentation
        url: https://developer.globalpayments.com/heartland/getting-started/overview
  - aid: heartland-payment-systems:gift-loyalty-api
    name: Heartland Gift and Loyalty API
    description: The Heartland Gift and Loyalty API supports stored value cards, gift card issuance and redemption, and loyalty program integration for merchants.
    humanURL: https://developer.globalpayments.com/heartland/getting-started/overview
    tags:
      - Gift Cards
      - Loyalty
      - Stored Value
    properties:
      - type: Documentation
        url: https://developer.globalpayments.com/heartland/getting-started/overview
  - aid: heartland-payment-systems:payroll-api
    name: Heartland Payroll API
    description: Heartland's Payroll APIs support employee payroll processing, tax filings, and HR integrations for small to mid-sized businesses.
    humanURL: https://developer.globalpayments.com/heartland/getting-started/overview
    tags:
      - HR
      - Payroll
      - Tax
    properties:
      - type: Documentation
        url: https://developer.globalpayments.com/heartland/getting-started/overview
common:
  - type: Website
    url: https://www.heartland.us
  - type: ParentCompany
    url: https://www.globalpayments.com
  - type: DeveloperPortal
    url: https://developer.globalpayments.com/heartland/getting-started/overview
  - type: Documentation
    url: https://developer.globalpayments.com/heartland/getting-started/overview
  - type: Testing
    url: https://developer.globalpayments.com/heartland/Certification/Testing
  - type: Support
    url: mailto:onlinepayments@heartland.us
  - type: Contact
    url: mailto:integratormanagement@e-hps.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
