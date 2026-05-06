---
aid: fraud-net
name: Fraud.net
description: Fraud.net provides AI-driven fraud prevention and risk management APIs. The Public API offers pre-authorization Cart Check, Transaction Check, post-event Update, and supporting device, identity, and email risk signals powered by the Collective Intelligence Network.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-13'
modified: '2026-04-28'
position: Consumer
tags:
  - Fraud
  - Risk
  - Commerce
  - Payments
  - Security
url: https://raw.githubusercontent.com/api-evangelist/fraud-net/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: fraud-net:public-api
    name: Fraud.net Public API
    description: Public API for evaluating cart and transaction risk pre-authorization and submitting post-event signals for model improvement, plus device, identity, and email risk endpoints.
    humanURL: https://api-docs.fraud.net/docs/public-apis/b2edb775739e6-api-documentation
    tags:
      - Fraud
      - Risk
      - Cart
      - Transaction
    properties:
      - type: Documentation
        url: https://api-docs.fraud.net/docs/public-apis/b2edb775739e6-api-documentation
      - type: Capabilities
        url: https://raw.githubusercontent.com/api-evangelist/fraud-net/refs/heads/main/capabilities/fraud-net-capabilities.yml
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/fraud-net/refs/heads/main/rules/fraud-net-rules.yml
common:
  - type: Website
    url: https://fraud.net/
  - type: Documentation
    url: https://api-docs.fraud.net/
  - type: SignUp
    url: https://fraud.net/contact/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
