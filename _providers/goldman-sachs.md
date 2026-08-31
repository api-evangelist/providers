---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-08-30'
api_count: 9
apis:
- description: Part of the Marquee developer platform, the Content Services API lets institutional clients programmatically consume client-focused Goldman Sachs content and commentary across equity, fixed income, cu
  name: Goldman Sachs Content Services API
  slug: goldman-sachs-content-services-api
- description: The Pricing & Risk Services API exposes Goldman Sachs' industry-leading derivatives pricing and risk analytics models so institutional clients can price instruments, compute risk measures and gain a d
  name: Goldman Sachs Pricing & Risk Services API
  slug: goldman-sachs-pricing-risk-services-api
- description: 'The Hedging Services API lets institutional clients tailor portfolio exposures and risks using Goldman Sachs'' hedging and optimization tools. Clients can dynamically manage objectives and constraints '
  name: Goldman Sachs Hedging Services API
  slug: goldman-sachs-hedging-services-api
- description: The Index Services API provides access to the full range of Goldman Sachs indices, systematic trading strategies and basket products, or the ability to create bespoke solutions to tailor investment st
  name: Goldman Sachs Index Services API
  slug: goldman-sachs-index-services-api
- description: The Portfolio Services API lets institutional clients programmatically manage the portfolio lifecycle from creation and update through to scheduling reports, with full control over visibility and shar
  name: Goldman Sachs Portfolio Services API
  slug: goldman-sachs-portfolio-services-api
- description: The Data Services API integrates Goldman Sachs data and insights into client tools and processes, exposing over 400 datasets spanning Equities, Fixed Income, Currencies, Commodities and Digital Assets
  name: Goldman Sachs Data Services API
  slug: goldman-sachs-data-services-api
- description: GS Quant is Goldman Sachs' open-source Python toolkit for quantitative finance, distributed on GitHub and PyPI, that wraps the Marquee pricing, risk and data APIs behind a Python client. Developers au
  name: GS Quant Python Toolkit
  slug: goldman-sachs-gs-quant-toolkit
- description: Goldman Sachs Transaction Banking (TxB) provides programmatic access for eligible partners and clients to embed treasury and banking capabilities into their own ecosystem, organized around three funct
  name: Goldman Sachs Transaction Banking (TxB) API
  slug: goldman-sachs-transaction-banking-api
- description: The Goldman Sachs Custody Solutions (GSCS) RIA Custody platform exposes REST APIs that let advisor firms and third-party integration partners build applications on top of institutional-grade custody f
  name: Goldman Sachs RIA Custody API
  slug: goldman-sachs-ria-custody-api
artifact_total: 15
asyncapis:
- description: ''
  name: Goldman Sachs Txb Webhooks
  slug: goldman-sachs-txb-webhooks
common:
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.goldmansachs.com/privacy-and-cookies
- group: start
  title: ''
  type: Login
  url: https://www.goldmansachs.com/login
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goldman-sachs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.goldmansachs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.gs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.gs.com/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goldmansachs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/goldman-sachs
- group: company
  title: ''
  type: Blog
  url: https://developer.gs.com/blog/posts
- group: commercial
  title: ''
  type: Plans
  url: plans/goldman-sachs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/goldman-sachs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/goldman-sachs-finops.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/goldman-sachs-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/goldman-sachs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/goldman-sachs-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/goldman-sachs-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/goldman-sachs-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/goldman-sachs-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/goldman-sachs-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/goldman-sachs-llms.txt
created: '2024-03-13'
description: Goldman Sachs is a leading global money-center investment bank and financial services firm. Its public developer surface is institutional and professional-client oriented, spanning the Marquee digital platform (content, pricing and risk, hedging, indices, portfolio, and market-data services plus the open-source GS Quant Python toolkit), the Transaction Banking (TxB) embedded-banking APIs for virtual accounts, payments and reporting across Fedwire/ACH/SWIFT rails, and the RIA Custody (GS Custody Solutions) REST APIs for advisor firms. Access is gated to institutional clients and approved partners; there is no self-serve consumer open-finance API.
finops:
- name: Goldman Sachs Finops
  service_category: Banking / Capital Markets
  slug: goldman-sachs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/goldman-sachs.png
layout: provider
modified: '2026-07-23'
name: Goldman Sachs
nav: Providers
network: true
overview: 'Goldman Sachs publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Financial, Investment Banking, Money Center, and Institutional.


  The Goldman Sachs catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Goldman Sachs'' developer surface includes documentation, engineering blog, authentication, and 17 more developer resources.'
plans:
- name: Goldman Sachs Plans Pricing
  plan_count: 2
  slug: goldman-sachs-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Goldman Sachs Rate Limits
  slug: goldman-sachs-rate-limits
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 13
    catalog_gap: 73.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 30.3
    commercial_clarity: 30.3
    contract_governance: 4.5
    contract_quality: 42.7
    developer_ergonomics: 40.5
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 37.2
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 34.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goldman-sachs/refs/heads/main/screenshots/goldman-sachs-2026-06-20T181950.png
security:
- kind: authentication
  name: Goldman Sachs Authentication
  slug: goldman-sachs-authentication
  summary_line: oauth2/http/mutualTLS · 4 schemes
- kind: domain-security
  name: Goldman Sachs Domain Security
  slug: goldman-sachs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: goldman-sachs
tags:
- Banking
- Financial
- Investment Banking
- Money Center
- Institutional
- Transaction Banking
- Custody
- Market Data
- United States
- Fortune 100
website: https://www.goldmansachs.com/
---
