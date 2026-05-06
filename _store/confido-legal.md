---
aid: confido-legal
name: Confido Legal
description: Confido Legal is a payment processing and disbursements platform purpose-built for the legal industry. It enables law firms and legal technology vendors to accept client payments with automated trust-account routing, send real-time digital disbursements for settlements, and embed compliant payment workflows through a unified GraphQL API. Confido integrates with leading legal practice management tools and accounting systems including Lawmatics, Litify, LeanLaw, Smart Advocate, QuickBooks, Salesforce, and Zapier.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/confido-legal/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-04-28'
specificationVersion: '0.19'
x-type: company
tags:
  - Compliance
  - Disbursements
  - GraphQL
  - IOLTA
  - Law
  - LawTech
  - Legal
  - Legal Technology
  - Payments
  - Trust Accounting
apis:
  - aid: confido-legal:graphql-api
    name: Confido Legal GraphQL API
    description: The Confido Legal GraphQL API is the unified developer interface for the Confido payments platform. Partners and law-firm developers use it to tokenize payment methods, accept ACH and card payments with automated routing to operating or trust (IOLTA) accounts, issue real-time disbursements, manage payors and payees, and reconcile transactions. The API enforces legal-industry compliance rules (PCI, IOLTA segregation, surcharge rules) at the platform layer so partners do not have to replicate them.
    humanURL: https://docs.confidolegal.com/
    baseURL: https://api.gravity-legal.com/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - GraphQL
      - IOLTA
      - Payments
      - Trust Accounting
    properties:
      - type: Documentation
        url: https://docs.confidolegal.com/
      - type: GraphQL Endpoint
        url: https://api.gravity-legal.com/
      - type: Sandbox
        url: https://api.sandbox.gravity-legal.com/
      - type: API Playground
        url: https://studio.apollographql.com/
      - type: LLMs
        url: https://docs.confidolegal.com/llms.txt
    contact:
      - FN: Confido Legal Support
        email: support@confidolegal.com
        url: https://confidolegal.com/contact
    x-features:
      - Tokenized Payment Methods
      - ACH and Card Payments
      - Trust Account (IOLTA) Routing
      - Real-Time Disbursements
      - Payor and Payee Management
      - Webhook Notifications
      - Hosted UI Components
      - Sandbox Environment
      - Built-In PCI Compliance
      - Surcharge and Convenience Fee Support
    x-use-cases:
      - Embed compliant payments in legal practice management software
      - Route client funds between trust and operating accounts
      - Disburse settlement funds to claimants in real time
      - Tokenize payment methods for repeat retainer billing
      - Reconcile transactions with QuickBooks or Salesforce
common:
  - type: Website
    url: https://confidolegal.com/
  - type: Documentation
    url: https://docs.confidolegal.com/
  - type: Developer Portal
    url: https://docs.confidolegal.com/
  - type: Sandbox
    url: https://api.sandbox.gravity-legal.com/
  - type: Production
    url: https://api.gravity-legal.com/
  - type: Integrations
    url: https://confidolegal.com/integrations
  - type: Pricing
    url: https://confidolegal.com/pricing
  - type: Blog
    url: https://confidolegal.com/blog
  - type: Contact
    url: https://confidolegal.com/contact
  - type: Support
    email: support@confidolegal.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
