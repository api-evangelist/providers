---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
api_count: 1
apis:
- description: REST API (OpenAPI 3.1) covering the sourcing lifecycle — RFQs, vendors, conversations, quotes, files, and webhooks. API-key authentication with team and environment scoping; the full reference and int
  name: Purchaser API
  slug: purchaser-api
artifact_total: 5
asyncapis:
- description: ''
  name: Purchaser Webhooks
  slug: purchaser-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://purchaser.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.purchaser.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.purchaser.ai
- group: docs
  title: ''
  type: APIReference
  url: https://purchaser.ai/api-and-integrations
- group: company
  title: ''
  type: Blog
  url: https://purchaser.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://purchaser.ai/contact
- group: start
  title: ''
  type: SignUp
  url: https://app.purchaser.ai/login
- group: start
  title: ''
  type: Login
  url: https://app.purchaser.ai/login
- group: design
  title: ''
  type: Conventions
  url: conventions/purchaser-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/purchaser-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/purchaser-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/purchaser-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/purchaser-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/purchaser-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/purchaser-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/purchaser-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/purchaser-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/purchaser-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/purchaser-mcp.yml
created: '2026-07-17'
description: Purchaser is an AI-powered RFQ (Request for Quotation) intelligence platform for capital-intensive industries such as EPC, LNG, transmission & distribution, and specialty-equipment manufacturing. It ingests unstructured vendor quotes from PDFs, emails, and spreadsheets and normalizes them into structured, defensible sourcing data so procurement teams can level bids apples-to-apples, surface deviations and gaps, and produce audit-ready award traceability. Purchaser exposes a REST API (OpenAPI 3.1) covering the full sourcing lifecycle — RFQs, vendors, conversations, quotes, files, and webhooks — with API-key auth, idempotency keys, versioned /api/v1/ endpoints, sliding-window rate limiting, and connectors for SAP S/4HANA, Oracle ERP Cloud, Microsoft Dynamics 365, Infor, and more. Based in Lexington, KY and backed by Homebrew.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/purchaser.png
layout: provider
modified: '2026-07-20'
name: Purchaser
nav: Providers
network: true
overview: 'Purchaser publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Procurement, Sourcing, and RFQ.


  The Purchaser catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Purchaser''s developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, and 13 more developer resources.'
random_paper: 7
screenshot: https://raw.githubusercontent.com/api-evangelist/purchaser/refs/heads/main/screenshots/purchaser-2026-09-02T152339.png
security:
- kind: authentication
  name: Purchaser Authentication
  slug: purchaser-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Purchaser Domain Security
  slug: purchaser-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Purchaser Trust Center
  slug: purchaser-trust-center
  summary_line: SOC 2 Type II
slug: purchaser
tags:
- Company
- Artificial Intelligence
- Procurement
- Sourcing
- RFQ
- Supply Chain
- Construction
- Enterprise
website: https://purchaser.ai
---
