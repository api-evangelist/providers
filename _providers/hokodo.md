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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Hokodo's B2B Buy Now, Pay Later REST API. Create companies and customers, request credit offers, place orders, and manage deferred payment plans and trade accounts. Versioned at /v1/; authenticated wi
  name: Hokodo BNPL API
  slug: hokodo-bnpl-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hokodo-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.hokodo.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hokodo.co/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hokodo.co/
- group: start
  title: ''
  type: SignUp
  url: https://sandbox.hokodo.co/
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.hokodo.co/
- group: operate
  title: ''
  type: Support
  url: https://hokodo.freshdesk.com/en/support/home
- group: company
  title: ''
  type: Blog
  url: https://hokodo.co/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hokodo-tech
- group: commercial
  title: ''
  type: TermsOfService
  url: https://static.hokodo.co/shared/hokodotermsandconditions.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://static.hokodo.co/shared/hokodoprivacypolicy.pdf
- group: company
  title: ''
  type: Website
  url: https://www.hokodo.co/
- group: build
  title: ''
  type: Packages
  url: packages/hokodo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hokodo-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hokodo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hokodo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hokodo-problem-types.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hokodo-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hokodo-llms.txt
created: '2026-07-17'
description: Hokodo is a London-based B2B payments and embedded trade-credit fintech that lets merchants and B2B marketplaces offer digital trade accounts and Buy Now, Pay Later at checkout. Buyers get instant credit decisions and flexible terms (30/60/90-day payment terms, instalments, and consolidated trade accounts) while Hokodo underwrites the credit risk, finances the invoice, and protects the merchant against non-payment. The platform is delivered through a versioned REST API (https://api.hokodo.co/v1/) covering companies, customers, credit offers, orders and payment plans, plus prebuilt Magento modules and a JavaScript SDK. Hokodo is backed by Anthemis and other investors and operates across the UK and Europe.
image: https://cdn.prod.website-files.com/5c80a8f7065a7b1940eb8538/684bf894db503831d2c72284_Home.png
layout: provider
modified: '2026-07-19'
name: Hokodo
nav: Providers
network: true
overview: 'Hokodo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, B2B Payments, Buy Now Pay Later, and Trade Credit.


  Hokodo''s developer surface includes documentation, API reference, signup flow, sandbox, support, engineering blog, authentication, and 12 more developer resources.'
random_paper: 44
score:
  band: emerging
  composite: 26.8
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 26.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hokodo/refs/heads/main/screenshots/hokodo-2026-07-25T221321.png
security:
- kind: authentication
  name: Hokodo Authentication
  slug: hokodo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hokodo Domain Security
  slug: hokodo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hokodo
tags:
- Company
- Fintech
- B2B Payments
- Buy Now Pay Later
- Trade Credit
- Embedded Finance
- Invoice Financing
- Payments API
website: https://www.hokodo.co/
---
