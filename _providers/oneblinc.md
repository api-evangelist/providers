---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.oneblinc.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.oneblinc.com/sign-up
- group: operate
  title: ''
  type: Support
  url: https://oneblinc.zendesk.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OneBlinc
- group: auth
  title: ''
  type: Compliance
  url: https://www.oneblinc.com/compliance
- group: operate
  title: ''
  type: StatusPage
  url: https://status.oneblinc.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/oneblinc-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/oneblinc-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oneblinc-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/oneblinc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/oneblinc-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oneblinc-llms.txt
coverage:
  checked: '2026-08-26'
  detail: OneBlinc ships only end-user mobile and web apps — its Next.js route manifest lists no /developers, /api or /docs route, its GitHub org has zero public repositories, and its one business product (BlincFy income verification) is sold behind a "Schedule a Demo" form; api.oneblinc.com is a real origin but returns a 0-byte HTTP 404 on every discovery path, so it is a private app backend, not a published API.
  evidence:
  - status: 404
    url: https://api.oneblinc.com/openapi.json
  - status: 404
    url: https://api.oneblinc.com/graphql
  - status: 200
    url: https://api.github.com/orgs/OneBlinc/repos
  - status: 200
    url: https://www.oneblinc.com/products/blinc-fy
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: OneBlinc is a US consumer fintech that provides cash advances, credit-building and financial-wellness products to public-sector, healthcare and other essential workers who are underserved by traditional banks. Its consumer products are delivered through the OneBlinc / BlincAdvance mobile apps — BlincAdvance (paycheck advances from $50 up to $250 on an $8.99/month subscription, with an optional paid instant-deposit tier), BlincBoost (a credit-building subscription), BlincShield and BlincEarn — and a legacy installment-loan product originated by BlincLoans, Inc. that is not currently accepting new applications. Its one business-facing product, BlincFy, sells customer-permissioned income and employment verification data and analytics, but is sold through a "Schedule a Demo" sales motion with no public developer documentation. OneBlinc publishes no public API, developer portal, SDK or machine-readable specification; api.oneblinc.com is a private backend for its own mobile clients.
image: https://www.oneblinc.com/images/meta-logo.png
layout: provider
modified: '2026-08-26'
name: OneBlinc
nav: Providers
network: true
overview: 'OneBlinc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Fintech, Consumer Lending, and Cash Advance.


  OneBlinc''s developer surface includes signup flow, support, and 10 more developer resources.'
plans:
- name: Oneblinc Plans Pricing
  plan_count: 3
  slug: oneblinc-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Oneblinc Rate Limits
  slug: oneblinc-rate-limits
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 17.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 20.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oneblinc/refs/heads/main/screenshots/oneblinc-2026-09-02T150845.png
security:
- kind: domain-security
  name: Oneblinc Domain Security
  slug: oneblinc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oneblinc
tags:
- Company
- Financial-Services
- Fintech
- Consumer Lending
- Cash Advance
- Earned Wage Access
- Credit Building
- Income Verification
- Mobile Banking
- United States
website: https://www.oneblinc.com/
---
