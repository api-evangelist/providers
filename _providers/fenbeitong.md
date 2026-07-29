---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Token- and signature-authenticated REST API for enterprises to integrate Fenbeitong organization structure, orders (flights, car, train, hotel, dining, takeout, procurement), approvals, budgets and bi
  name: Fenbeitong Open Platform
  slug: fenbeitong-open-platform
artifact_total: 5
asyncapis:
- description: ''
  name: Fenbeitong Webhooks
  slug: fenbeitong-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.fenbeitong.com
- group: start
  title: ''
  type: DeveloperPortal
  url: http://docs.open.fenbeitong.com/open-api/1.fenbeitong-introduction.html
- group: docs
  title: ''
  type: Documentation
  url: http://docs.open.fenbeitong.com/open-api/1.fenbeitong-introduction.html
- group: docs
  title: ''
  type: APIReference
  url: http://docs.open.fenbeitong.com/open-api/2apijie-ru.html
- group: start
  title: ''
  type: GettingStarted
  url: http://docs.open.fenbeitong.com/open-api/1.fenbeitong-introduction/11join-introduction.html
- group: operate
  title: ''
  type: Support
  url: https://www.fenbeitong.com/service.php
- group: start
  title: ''
  type: SignUp
  url: https://www.fenbeitong.com/apply.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://static.fenbeitong.com/agreement.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fenbeitong.com/level-agreement-6c73c91144ec5aa632b25bedb4e657c4.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/fenbeitong-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fenbeitong-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fenbeitong-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fenbeitong-error-codes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fenbeitong-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fenbeitong-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fenbeitong-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fenbeitong-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/fenbeitong-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fenbeitong-llms.txt
created: '2026-07-17'
description: Fenbeitong (分贝通) is a Beijing-based enterprise expenditure and spend management platform that unifies corporate travel (flights, rail, hotel, ride-hailing), dining, takeout, procurement, budgeting, reimbursement and payment into a single SaaS-plus-payment system for over 4,000 companies. Its Open Platform (开放平台) exposes a token- and signature-authenticated REST API that lets partnered enterprises integrate organization structure, orders, approvals, budgets and billing, and receive real-time order events via webhooks. Founded in 2016 and backed by Ribbit Capital and DST Global, the company operates production and sandbox API environments.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fenbeitong.png
layout: provider
modified: '2026-07-19'
name: Fenbeitong
nav: Providers
network: true
overview: 'Fenbeitong publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Spend Management, Expense Management, and Corporate Travel.


  The Fenbeitong catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fenbeitong''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, sandbox, and 12 more developer resources.'
random_paper: 30
score:
  band: developing
  composite: 42.3
  delta: 2.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.6
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 39.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fenbeitong/refs/heads/main/screenshots/fenbeitong-2026-07-25T214442.png
security:
- kind: authentication
  name: Fenbeitong Authentication
  slug: fenbeitong-authentication
  summary_line: token/signature · 2 schemes
- kind: domain-security
  name: Fenbeitong Domain Security
  slug: fenbeitong-domain-security
  summary_line: TLSv1.3
- kind: trust-center
  name: Fenbeitong Trust Center
  slug: fenbeitong-trust-center
  summary_line: CSA STAR Level 2
slug: fenbeitong
tags:
- Company
- Fintech
- Spend Management
- Expense Management
- Corporate Travel
- Payments
- Procurement
- China
website: https://www.fenbeitong.com
---
