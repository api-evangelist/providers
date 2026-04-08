---
aid: tallyman
url: https://raw.githubusercontent.com/api-evangelist/tallyman/refs/heads/main/apis.yml
apis:
- name: Tallyman Collections API
  description: Core API for managing debt collections, customer accounts, and payment arrangements.
  image: https://www.tallyman.co.uk/api-logo.png
  humanURL: https://www.tallyman.co.uk/collections
  baseURL: https://api.tallyman.co.uk/v1
  tags:
  - Accounts
  - Arrangements
  - Collections
  - Payments
  properties:
  - type: Documentation
    url: https://docs.tallyman.co.uk/api/collections
  - type: OpenAPI
    url: https://api.tallyman.co.uk/v1/openapi.json
  - type: Authentication
    url: https://docs.tallyman.co.uk/api/authentication
  - type: Swagger
    url: https://api.tallyman.co.uk/swagger
  - type: Postman Collection
    url: https://www.postman.com/tallyman/collections
  - type: Rate Limits
    url: https://docs.tallyman.co.uk/api/rate-limits
  - type: Status
    url: https://status.tallyman.co.uk
  contact:
  - type: Support
    url: https://support.tallyman.co.uk
  - type: Email
    url: mailto:api-support@tallyman.co.uk
  - type: Twitter
    url: https://twitter.com/tallymantech
- name: Tallyman Customer API
  description: API for managing customer information, communication preferences, and profile data.
  humanURL: https://www.tallyman.co.uk/customer-api
  baseURL: https://api.tallyman.co.uk/v1/customers
  tags:
  - Communications
  - Customers
  - Preferences
  - Profiles
  properties:
  - type: Documentation
    url: https://docs.tallyman.co.uk/api/customers
  - type: OpenAPI
    url: https://api.tallyman.co.uk/v1/customers/openapi.json
- name: Tallyman Payment API
  description: API for processing payments, refunds, and payment plan management.
  humanURL: https://www.tallyman.co.uk/payment-api
  baseURL: https://api.tallyman.co.uk/v1/payments
  tags:
  - Payment Plans
  - Payments
  - Refunds
  - Transactions
  properties:
  - type: Documentation
    url: https://docs.tallyman.co.uk/api/payments
  - type: OpenAPI
    url: https://api.tallyman.co.uk/v1/payments/openapi.json
  - type: Security
    url: https://docs.tallyman.co.uk/api/payment-security
- name: Tallyman Reporting API
  description: API for generating reports, analytics, and business intelligence data.
  humanURL: https://www.tallyman.co.uk/reporting-api
  baseURL: https://api.tallyman.co.uk/v1/reports
  tags:
  - Analytics
  - Business Intelligence
  - Metrics
  - Reporting
  properties:
  - type: Documentation
    url: https://docs.tallyman.co.uk/api/reporting
  - type: OpenAPI
    url: https://api.tallyman.co.uk/v1/reports/openapi.json
- name: Tallyman Webhooks API
  description: Event-driven webhooks for real-time notifications on collection activities.
  humanURL: https://www.tallyman.co.uk/webhooks
  baseURL: https://api.tallyman.co.uk/v1/webhooks
  tags:
  - Events
  - Notifications
  - Real-Time
  - Webhooks
  properties:
  - type: Documentation
    url: https://docs.tallyman.co.uk/api/webhooks
  - type: Event Catalog
    url: https://docs.tallyman.co.uk/api/webhook-events
name: Tallyman
tags:
- Collections
- Credit Management
- CRM
- Debt Recovery
- Financial Services
type: Contract
image: https://www.tallyman.co.uk/logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection management and debt recovery platform APIs.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

