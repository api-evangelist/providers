---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: 'RESTful JSON API for managing invoices (billograms), customers, items, credit invoices, payment sources, offers, billing tabs, reports, and webhooks. Authenticated with HTTP Basic Auth (API User ID + '
  name: Billogram v2 API
  slug: billogram-v2-api
artifact_total: 5
asyncapis:
- description: ''
  name: Billogram Webhooks
  slug: billogram-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://billogram.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.billogram.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.billogram.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.billogram.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.billogram.com/guides/getting-started
- group: company
  title: ''
  type: Blog
  url: https://billogram.com/blog
- group: start
  title: ''
  type: Login
  url: https://billogram.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://billogram.com/privacy
- group: build
  title: ''
  type: Packages
  url: packages/billogram-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/billogram-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/billogram-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/billogram-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/billogram-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/billogram-vulnerability-disclosure.yml
created: '2026-07-17'
description: Billogram is a Swedish (Billogram AB) Invoice-to-Cash orchestration platform that automates the full invoicing and payment lifecycle for businesses with recurring revenue - invoice creation and distribution, digital payment collection, customer communication, reminders and dunning, e-invoice registration, and financial reporting. It serves the insurance, telecom, mobility/parking, and energy sectors. The Billogram v2 API is a RESTful JSON API (HTTP Basic Auth) covering customers, billograms/invoices, items, credit invoices, payment sources, offers, billing tabs, reports, and HMAC-signed webhooks, with separate sandbox and production environments and an official Python client library.
image: https://billogram.com/static/images/billogram-og_@2X.png
layout: provider
modified: '2026-07-18'
name: Billogram
nav: Providers
network: true
overview: 'Billogram publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Applicative Saas, Invoicing, Billing, and Payments.


  The Billogram catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Billogram''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 10 more developer resources.'
random_paper: 49
score:
  band: thin
  composite: 35.0
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 51.6
    developer_ergonomics: 43.5
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 10.5
  previous_composite: 35.0
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/billogram/refs/heads/main/screenshots/billogram-2026-07-25T202950.png
security:
- kind: authentication
  name: Billogram Authentication
  slug: billogram-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Billogram Domain Security
  slug: billogram-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Billogram Vulnerability Disclosure
  slug: billogram-vulnerability-disclosure
  summary_line: Hackerone
slug: billogram
tags:
- Company
- Applicative Saas
- Invoicing
- Billing
- Payments
- Invoice-to-Cash
- E-invoicing
- Fintech
- Webhooks
website: https://billogram.com/
---
