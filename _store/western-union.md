---
aid: western-union
url: https://raw.githubusercontent.com/api-evangelist/western-union/refs/heads/main/apis.yml
modified: '2026-05-03'
description: The Western Union Company is a global leader in cross-border, cross-currency money movement, providing money transfer, money order, and other financial services to consumers and businesses worldwide. Western Union's Partnership APIs enable financial institutions, fintech companies, and enterprise customers to integrate WU's global payment network for money transfers, batch payments, FX quotes, and account management across 200+ countries and territories in 130+ currencies. Authentication uses mTLS with client certificates.
apis:
  - aid: western-union:mass-payments
    name: Western Union Mass Payments API
    description: The Western Union Mass Payments API enables financial institutions and enterprise customers to send up to 10,000 international payments in a single batch across 130+ currencies. The API supports payment lifecycle management including creating batches, adding individual payments, committing batches, and tracking payment status. Authentication is via mTLS (mutual TLS) with client certificates.
    humanURL: https://developer.westernunion.com/api-money-transfer.html
    baseURL: https://api.westernunion.com
    tags:
      - Money Transfer
      - Payments
      - International
      - Batch Payments
      - Financial Services
    properties:
      - type: Documentation
        url: https://developer.westernunion.com/api-money-transfer.html
      - type: Portal
        url: https://developer.westernunion.com/getting-started.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/western-union/refs/heads/main/openapi/western-union-mass-payments-openapi.yml
      - type: GettingStarted
        url: https://developer.westernunion.com/getting-started.html
    contact:
      - FN: Western Union Partnership Program
        url: https://developer.westernunion.com/getting-started.html
        email: wuconnect@westernunion.com
  - aid: western-union:open-banking
    name: Western Union Open Banking API
    description: Western Union's PSD2-compliant Open Banking API enables Payment Service Providers to access account information (AIS) and initiate payments (PIS) in compliance with European Payment Services Directive 2 (PSD2). The API supports Strong Customer Authentication (SCA) and integrates with the WU Business Solutions global payment network.
    humanURL: https://wu-priora.saltedge.com/
    baseURL: https://wu-priora.saltedge.com
    tags:
      - Open Banking
      - PSD2
      - Account Information
      - Payment Initiation
      - Financial Services
    properties:
      - type: Portal
        url: https://wu-priora.saltedge.com/
      - type: Documentation
        url: https://wu-priora.saltedge.com/
    contact:
      - FN: Western Union Business Solutions
common:
  - type: Website
    url: https://www.westernunion.com
  - type: BusinessSolutions
    url: https://business.westernunion.com
  - type: Portal
    url: https://developer.westernunion.com
  - type: GettingStarted
    url: https://developer.westernunion.com/getting-started.html
  - type: Contact
    url: https://corporate.westernunion.com/fi-partnerships/solutions/
  - type: PrivacyPolicy
    url: https://www.westernunion.com/us/en/privacy-statement.html
  - type: TermsOfService
    url: https://www.westernunion.com/us/en/digital-service-agreement.html
  - type: LinkedIn
    url: https://www.linkedin.com/company/western-union
---
