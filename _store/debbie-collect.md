---
aid: debbie-collect
name: Debbie Collect
url: https://raw.githubusercontent.com/api-evangelist/debbie-collect/refs/heads/main/apis.yml
type: Contract
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Accounts Receivable
  - Collections
  - Debt Collection
  - FinTech
  - Payments
  - SaaS
created: '2025-02-24'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: company
description: Debbie (Debbie Collect, operated by Intellitech Systems A/S) is an AI-driven SaaS platform that automates debt collection and accounts receivable management. Companies, collection agencies, and law firms use Debbie to run digital reminder flows, debtor dialogue, payment plans, and case management. Debbie publishes two RESTful APIs - a Platform API for collectors integrating Debbie into existing systems, and a Client API for creditors creating cases and exchanging payment data.
apis:
  - aid: debbie-collect:debbie-platform-api
    name: Debbie Platform API
    description: The Debbie Platform API exposes resources for cases, creditors, customers, vouchers, files, updates, billing, and webhooks. It is used by collection agencies and other operators integrating Debbie into their core systems.
    humanURL: https://documentation.debbiecollect.com
    baseURL: https://api.debbie.dk
    tags:
      - Cases
      - Collections
      - Creditors
      - Customers
      - Webhooks
    properties:
      - type: Documentation
        url: https://documentation.debbiecollect.com
      - type: OpenAPI
        url: openapi/debbie-platform-api-openapi.yml
      - type: JSONSchema
        url: json-schema/debbie-case.json
      - type: JSONSchema
        url: json-schema/debbie-customer.json
      - type: Rules
        url: rules/debbie-platform-api-rules.yml
      - type: Capabilities
        url: capabilities/debbie-platform-api-capabilities.yml
  - aid: debbie-collect:debbie-client-api
    name: Debbie Client API
    description: The Debbie Client API allows creditors to create collection cases, exchange payment data, and receive case status updates. It is the primary integration surface for ERP/billing systems pushing overdue invoices into Debbie.
    humanURL: https://creditor-docs.debbie.dk
    baseURL: https://creditor.debbie.dk/api
    tags:
      - Cases
      - Creditor
      - Payments
    properties:
      - type: Documentation
        url: https://creditor-docs.debbie.dk
      - type: OpenAPI
        url: openapi/debbie-client-api-openapi.yml
common:
  - type: Website
    url: https://debbiecollect.com/
  - type: API Documentation
    url: https://debbiecollect.com/api-documentation
  - type: Status
    url: https://debbie.freshstatus.io
  - type: Security & Compliance
    url: https://debbiecollect.com/security-compliance-2
  - type: Blog
    url: https://debbiecollect.com/blog
  - type: Support
    url: mailto:api-support@debbie.dk
  - type: JSON-LD
    url: json-ld/debbie-context.jsonld
  - type: Vocabulary
    url: vocabulary/debbie-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
