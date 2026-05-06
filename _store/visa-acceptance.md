---
aid: visa-acceptance
name: Visa Acceptance
description: Visa Acceptance Solutions (powered by CyberSource) is the developer platform for accepting payments online, in-person, and via mobile. The platform provides REST APIs for payment authorization, capture, refund, void, reversal, invoicing, and pay-by-link. Authentication uses JWT with RSA key pairs, with support for Intelligent Commerce APIs enabling AI agent-initiated payments.
type: Index
position: Consumer
access: 3rd-Party
url: https://raw.githubusercontent.com/api-evangelist/visa-acceptance/refs/heads/main/apis.yml
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Payments
  - E-Commerce
  - Fintech
  - Credit Cards
  - Invoicing
  - Payment Links
  - Digital Wallets
created: '2025-02-17'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: visa-acceptance:visa-acceptance-payments
    name: Visa Acceptance Payments API
    description: REST API for accepting and processing payments including authorization, capture, refund, void, and reversal operations. Supports credit cards, debit cards, Apple Pay, Google Pay, and other payment methods.
    humanURL: https://developer.visaacceptance.com/
    tags:
      - Payments
      - Authorization
      - Capture
      - Refunds
      - Voids
    properties:
      - type: OpenAPI
        url: openapi/visa-acceptance-payments-openapi.yml
      - type: Documentation
        url: https://developer.visaacceptance.com/docs.html
      - type: GettingStarted
        url: https://developer.visaacceptance.com/docs/vas/en-us/platform/developer/all/rest/rest-getting-started/restgs-intro.html
      - type: Authentication
        url: https://developer.visaacceptance.com/docs/vas/en-us/platform/developer/all/rest/rest-getting-started/restgs-intro.html
      - type: Sandbox
        url: https://developer.visaacceptance.com/hello-world/sandbox.html
      - type: Testing
        url: https://developer.visaacceptance.com/hello-world/testing-guide.html
  - aid: visa-acceptance:visa-acceptance-invoicing
    name: Visa Acceptance Invoicing API
    description: Create, manage, and send invoices to customers with payment links. Supports line items, custom due dates, and real-time payment status.
    humanURL: https://developer.visaacceptance.com/
    tags:
      - Invoicing
      - Payments
      - Payment Links
    properties:
      - type: OpenAPI
        url: openapi/visa-acceptance-payments-openapi.yml
      - type: Documentation
        url: https://developer.visaacceptance.com/docs.html
  - aid: visa-acceptance:visa-acceptance-pay-by-link
    name: Visa Acceptance Pay by Link API
    description: Generate shareable payment links that redirect customers to a hosted payment page. Supports AI agent-initiated payments via the Agent Toolkit.
    humanURL: https://developer.visaacceptance.com/docs/vas/en-us/agent-toolkit/quick-start/all/na/agent-toolkit/agent-toolkit-intro.html
    tags:
      - Payment Links
      - Payments
      - AI Agents
    properties:
      - type: OpenAPI
        url: openapi/visa-acceptance-payments-openapi.yml
      - type: Documentation
        url: https://developer.visaacceptance.com/docs/vas/en-us/agent-toolkit/quick-start/all/na/agent-toolkit/agent-toolkit-intro.html
common:
  - type: Website
    url: https://developer.visaacceptance.com/
  - type: Documentation
    url: https://developer.visaacceptance.com/docs.html
  - type: Sandbox
    url: https://developer.visaacceptance.com/hello-world/sandbox.html
  - type: Support
    url: https://developer.visaacceptance.com/support/contact-us.html
  - type: ResponseCodes
    url: https://developer.visaacceptance.com/api/reference/response-codes.html
  - type: JSONSchema
    url: json-schema/visa-acceptance-payment-schema.json
  - type: JSON-LD
    url: json-ld/visa-acceptance-context.jsonld
  - type: Vocabulary
    url: vocabulary/visa-acceptance-vocabulary.yml
  - type: SpectralRules
    url: rules/visa-acceptance-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
