---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Mercoa Agentic Access
  operation_count: 48
  slug: mercoa-agentic-access
  summary_line: 48 operations · 31 acting
api_count: 1
apis:
- description: 'REST API and SDK suite for embedding accounts payable and accounts receivable into vertical SaaS platforms. Exposes resources for entities, users, invoices, bills, vendors, approval policies, payment '
  name: Mercoa API
  slug: mercoa-api
- baseURL: https://api.mercoa.com
  baseurl_source: declared
  description: The Entities API from Mercoa — 7 operation(s) for entities.
  name: Mercoa Entities API
  slug: mercoa-entities-api
- baseURL: https://api.mercoa.com
  baseurl_source: declared
  description: The Entity Groups API from Mercoa — 5 operation(s) for entity groups.
  name: Mercoa Entity Groups API
  slug: mercoa-entity-groups-api
- baseURL: https://api.mercoa.com
  baseurl_source: declared
  description: The Invoice Templates API from Mercoa — 3 operation(s) for invoice templates.
  name: Mercoa Invoice Templates API
  slug: mercoa-invoice-templates-api
- baseURL: https://api.mercoa.com
  baseurl_source: declared
  description: The Invoices API from Mercoa — 8 operation(s) for invoices.
  name: Mercoa Invoices API
  slug: mercoa-invoices-api
- baseURL: https://api.mercoa.com
  baseurl_source: declared
  description: The OCR API from Mercoa — 3 operation(s) for ocr.
  name: Mercoa OCR API
  slug: mercoa-ocr-api
- baseURL: https://api.mercoa.com
  baseurl_source: declared
  description: The Organization API from Mercoa — 1 operation(s) for organization.
  name: Mercoa Organization API
  slug: mercoa-organization-api
- baseURL: https://api.mercoa.com
  baseurl_source: declared
  description: The Payment Gateway API from Mercoa — 2 operation(s) for payment gateway.
  name: Mercoa Payment Gateway API
  slug: mercoa-payment-gateway-api
- baseURL: https://api.mercoa.com
  baseurl_source: declared
  description: The Payment Methods API from Mercoa — 3 operation(s) for payment methods.
  name: Mercoa Payment Methods API
  slug: mercoa-payment-methods-api
- baseURL: https://api.mercoa.com
  baseurl_source: declared
  description: The Transactions API from Mercoa — 2 operation(s) for transactions.
  name: Mercoa Transactions API
  slug: mercoa-transactions-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mercoa Entities API
  slug: open-mercoa-entities-api
- collection_type: open
  name: Mercoa Entities Entity Groups API
  slug: open-mercoa-entity-groups-api
- collection_type: open
  name: Mercoa Entities Invoice Templates API
  slug: open-mercoa-invoice-templates-api
- collection_type: open
  name: Mercoa Entities Invoices API
  slug: open-mercoa-invoices-api
- collection_type: open
  name: Mercoa Entities OCR API
  slug: open-mercoa-ocr-api
- collection_type: open
  name: Mercoa Entities Organization API
  slug: open-mercoa-organization-api
- collection_type: open
  name: Mercoa Entities Payment Gateway API
  slug: open-mercoa-payment-gateway-api
- collection_type: open
  name: Mercoa Entities Payment Methods API
  slug: open-mercoa-payment-methods-api
- collection_type: open
  name: Mercoa Entities Transactions API
  slug: open-mercoa-transactions-api
- collection_type: open
  name: Mercoa API
  slug: open-mercoa
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mercoa-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mercoa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mercoa-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://mercoa.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mercoa.com/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/mercoa-finance
- group: start
  title: ''
  type: Signup
  url: https://mercoa.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.mercoa.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://mercoa.com/blog
created: '2026-05-23'
description: Mercoa is an embedded AP and AR platform that vertical SaaS companies use to launch AI-powered BillPay and invoicing inside their own products. The platform handles bill ingestion via intelligent email inboxes, vendor onboarding, approval workflows, payment scheduling, branded invoicing, AI-driven collection reminders, and disbursement across ACH, check, virtual card, and BNPL. Builders can choose React components, a hosted iFrame, or pure REST APIs and SDKs depending on how much UI control they need. Mercoa publishes official SDKs for TypeScript, Python, and Java and is backed by Y Combinator. Customers monetize Mercoa through per-user pricing, transaction fees, and premium payment option margins.
finops:
- name: Mercoa Finops
  service_category: API
  slug: mercoa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mercoa.png
layout: provider
modified: '2026-05-23'
name: Mercoa
nav: Providers
network: true
overview: 'Mercoa publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Entities API, Entity Groups API, Invoice Templates API, and 6 more. Tagged areas include Mercoa, Embedded Finance, Accounts Payable, Accounts Receivable, and Bill Pay.


  Mercoa''s developer surface includes authentication, documentation, signup flow, engineering blog, and 5 more developer resources.'
plans:
- name: Mercoa Plans Pricing
  plan_count: 1
  slug: mercoa-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Mercoa Rate Limits
  slug: mercoa-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/mercoa/refs/heads/main/screenshots/mercoa-2026-06-20T185210.png
security:
- kind: authentication
  name: Mercoa Authentication
  slug: mercoa-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mercoa Domain Security
  slug: mercoa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mercoa
tags:
- Mercoa
- Embedded Finance
- Accounts Payable
- Accounts Receivable
- Bill Pay
- Invoicing
- Payments
- Vertical SaaS
- Vendors
- Approvals
- Disbursements
- Virtual Cards
website: https://mercoa.com/
---
