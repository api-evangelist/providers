---
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API returning Shariah-compliance screening for stocks and ETFs — a compliance status and 0-5 ranking per ticker, a full screening report with revenue breakdown and interest-bearing securities/deb
  name: Musaffa B2B Shariah Compliance API
  slug: musaffa-b2b-shariah-compliance-api
artifact_total: 6
asyncapis:
- description: ''
  name: Musaffa Screening Webhooks
  slug: musaffa-screening-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/musaffa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://musaffa.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://musaffa.com/for-business/
- group: docs
  title: ''
  type: Documentation
  url: https://api.musaffa.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.musaffa.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://musaffa.com/for-business/
- group: start
  title: ''
  type: SignUp
  url: https://musaffa.com/authentication/register/
- group: start
  title: ''
  type: Login
  url: https://musaffa.com/authentication/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://musaffa.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://musaffa.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://musaffa.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://musaffa.com/news/
- group: auth
  title: ''
  type: Authentication
  url: authentication/musaffa-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/musaffa-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/musaffa-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/musaffa-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/musaffa-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/musaffa-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/musaffa-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/musaffa-screening-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/musaffa-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/musaffa-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/musaffa-llms.txt
created: '2026-08-26'
description: 'Musaffa is a New York-headquartered Islamic fintech that operates a halal investing platform and sells its underlying Shariah-compliance dataset to other businesses as the Musaffa B2B API. The company screens 120,000+ stocks and ETFs across 70+ global exchanges against an AAOIFI-based methodology and exposes the results — compliance status, a 0-5 compliance ranking, revenue breakdown, interest-bearing securities and debt ratios, dividend purification amounts and related securities — through a versioned REST API at platform.musaffa.com, plus an outbound webhook that pushes compliance-status changes to a subscriber URL. The B2B API is documented publicly at api.musaffa.com (v1, v2 and the current v3) but the API itself is sold through a demo/sales process: credentials are a client ID plus a shared secret issued per client, and there is no self-service signup for the API.'
image: https://musaffa.com/assets/images/header/musaffa-logo-black.webp
layout: provider
modified: '2026-08-26'
name: Musaffa
nav: Providers
network: true
overview: 'Musaffa publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Islamic Finance, Shariah Compliance, Halal Investing, Stock Screening, and Financial Data.


  The Musaffa catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Musaffa''s developer surface includes documentation, API reference, pricing, signup flow, support, engineering blog, authentication, and 16 more developer resources.'
plans:
- name: Musaffa Plans Pricing
  plan_count: 4
  slug: musaffa-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Musaffa Rate Limits
  slug: musaffa-rate-limits
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 15
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 47.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Musaffa Authentication
  slug: musaffa-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Musaffa Domain Security
  slug: musaffa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: musaffa
tags:
- Islamic Finance
- Shariah Compliance
- Halal Investing
- Stock Screening
- Financial Data
- ETFs
- Market Data
- Fintech
- Investing
- Compliance
- Zakat
- Company
website: https://musaffa.com/
---
