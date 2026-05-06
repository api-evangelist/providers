---
aid: keycorp
name: KeyCorp
description: KeyCorp is one of the nation's largest bank-based financial services companies, providing deposit, lending, cash management, and investment services to individuals, small businesses, and middle-market companies. The KeyBank Developer Portal exposes commercial banking APIs for account information, payments, inquiry, and check services.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Banking
  - Commercial Banking
  - Financial Services
  - Fortune 500
  - Payments
url: https://raw.githubusercontent.com/api-evangelist/keycorp/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: keycorp:account-information-api
    name: KeyBank Account Information API
    description: Provides real-time account insights and transaction details for commercial KeyBank accounts.
    humanURL: https://developer.key.com/
    tags:
      - Account Information
      - Commercial Banking
    properties:
      - type: Documentation
        url: https://developer.key.com/
  - aid: keycorp:ach-origination-api
    name: KeyBank ACH Origination API
    description: Enables secure, automated ACH fund transfers from commercial KeyBank accounts.
    humanURL: https://developer.key.com/
    tags:
      - ACH
      - Payments
    properties:
      - type: Documentation
        url: https://developer.key.com/
  - aid: keycorp:wire-transfer-api
    name: KeyBank Wire Transfer API
    description: Facilitates high-value wire transfer payments through KeyBank's commercial payments platform.
    humanURL: https://developer.key.com/
    tags:
      - Payments
      - Wire Transfer
    properties:
      - type: Documentation
        url: https://developer.key.com/
  - aid: keycorp:rtp-send-payment-api
    name: KeyBank RTP Send Payment API
    description: Initiates instant payments over the Real-Time Payments network from commercial KeyBank accounts.
    humanURL: https://developer.key.com/
    tags:
      - Payments
      - Real-Time Payments
    properties:
      - type: Documentation
        url: https://developer.key.com/
  - aid: keycorp:account-validation-api
    name: KeyBank Account Validation API
    description: Verifies account details and ownership before initiating commercial payments and transfers.
    humanURL: https://developer.key.com/
    tags:
      - Account Validation
      - Payments
    properties:
      - type: Documentation
        url: https://developer.key.com/
  - aid: keycorp:ach-inquiry-api
    name: KeyBank ACH Inquiry API
    description: Checks the status of ACH transactions originated through the KeyBank Developer Portal.
    humanURL: https://developer.key.com/
    tags:
      - ACH
      - Inquiry
    properties:
      - type: Documentation
        url: https://developer.key.com/
  - aid: keycorp:wire-inquiry-api
    name: KeyBank Wire Inquiry API
    description: Tracks the status and delivery of wire transfers initiated through KeyBank.
    humanURL: https://developer.key.com/
    tags:
      - Inquiry
      - Wire Transfer
    properties:
      - type: Documentation
        url: https://developer.key.com/
  - aid: keycorp:rtp-inquiry-api
    name: KeyBank RTP Inquiry API
    description: Confirms delivery and status of Real-Time Payments sent through KeyBank.
    humanURL: https://developer.key.com/
    tags:
      - Inquiry
      - Real-Time Payments
    properties:
      - type: Documentation
        url: https://developer.key.com/
  - aid: keycorp:previous-day-api
    name: KeyBank Previous Day API
    description: Reviews prior-day financial activity and reporting for commercial KeyBank accounts.
    humanURL: https://developer.key.com/
    tags:
      - Account Information
      - Reporting
    properties:
      - type: Documentation
        url: https://developer.key.com/
  - aid: keycorp:intraday-api
    name: KeyBank Intraday API
    description: Monitors same-day transaction updates and intraday activity across commercial KeyBank accounts.
    humanURL: https://developer.key.com/
    tags:
      - Account Information
      - Reporting
    properties:
      - type: Documentation
        url: https://developer.key.com/
  - aid: keycorp:check-services-api
    name: KeyBank Check Services API
    description: Manages check stops, retrieval, and related check services for commercial KeyBank accounts.
    humanURL: https://developer.key.com/
    tags:
      - Check Services
      - Commercial Banking
    properties:
      - type: Documentation
        url: https://developer.key.com/
  - aid: keycorp:webhooks
    name: KeyBank Webhooks
    description: Delivers real-time payment event notifications to subscribed consumer applications.
    humanURL: https://developer.key.com/
    tags:
      - Events
      - Webhooks
    properties:
      - type: Documentation
        url: https://developer.key.com/
common:
  - type: Website
    url: https://www.key.com/
  - type: Developer Portal
    url: https://developer.key.com/
  - type: Corporate Website
    url: https://www.keycorp.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
