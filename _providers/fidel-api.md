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
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Card-linking REST API for linking Visa/Mastercard/Amex cards to programs and receiving real-time transaction events (Programs, Brands, Cards, Transactions, Locations, Offers, Webhooks, MIDs).
  name: Fidel API
  slug: fidel-api
artifact_total: 4
asyncapis:
- description: ''
  name: Fidel Api Webhooks
  slug: fidel-api-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fidel-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fidelapi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.fidel.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fidelapi.com/
- group: docs
  title: ''
  type: APIReference
  url: https://reference.fidel.uk/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fidelapi.com/docs/select
- group: operate
  title: ''
  type: Support
  url: https://community.fidel.uk/
- group: company
  title: ''
  type: Blog
  url: https://fidelapi.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Enigmatic-Smile
- group: commercial
  title: ''
  type: Pricing
  url: https://fidelapi.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.fidel.uk/sign-up
- group: start
  title: ''
  type: Login
  url: https://dashboard.fidel.uk/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fidelapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fidelapi.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fidel.uk/
- group: auth
  title: ''
  type: Authentication
  url: authentication/fidel-api-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/fidel-api-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fidel-api-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fidel-api-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fidel-api-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fidel-api-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fidel-api-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fidel-api-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fidel-api-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.fidelapi.com/docs/select
- group: design
  title: ''
  type: Components
  url: components/fidel-api-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fidel-api-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fidel-api-llms.txt
created: '2026-07-17'
description: Fidel API is a global card-linking platform that connects Visa, Mastercard and Amex payment cards to web and mobile applications through a single API. Once a cardholder links a card (via Fidel's PCI-compliant Web, iOS, Android or React Native SDKs), Fidel streams enriched, real-time transaction data - authorization, clearing and refund events - from the card networks to the developer's server via signed webhooks. Developers use it to build card-linked loyalty, rewards, cashback and offers programs without handling raw card data or PCI scope. The platform spans Programs, Brands, Locations, Cards, Transactions, Offers and Merchant IDs, operates test and live environments, and is available across the US, UK, Ireland, Canada, Sweden and the UAE (with Japan in beta). Founded in 2018 and headquartered in London, Fidel is backed by Bain Capital Ventures.
image: https://fidelapi.com/fidel_social.png
layout: provider
modified: '2026-07-19'
name: FIDEL API
nav: Providers
network: true
overview: 'FIDEL API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Card Linking, Payments, and Transactions.


  The FIDEL API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  FIDEL API''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
random_paper: 20
score:
  band: developing
  composite: 53.5
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 51.6
    developer_ergonomics: 65.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 44.7
  previous_composite: 53.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 59.4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fidel-api/refs/heads/main/screenshots/fidel-api-2026-07-25T214421.png
security:
- kind: authentication
  name: Fidel Api Authentication
  slug: fidel-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Fidel Api Domain Security
  slug: fidel-api-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fidel-api
tags:
- Company
- Fintech
- Card Linking
- Payments
- Transactions
- Webhooks
- SDK
- Card-Linked Offers
- Financial Data
website: https://fidelapi.com/
---
