---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
artifact_total: 5
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bluevine.com/help-center/getting-started
- group: company
  title: ''
  type: Website
  url: https://www.bluevine.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bluevine.com/guides/
- group: operate
  title: ''
  type: Support
  url: https://support.bluevine.com/
- group: company
  title: ''
  type: Blog
  url: https://www.bluevine.com/blog/
- group: company
  title: ''
  type: Newsroom
  url: https://www.bluevine.com/newsroom
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bluevine.com/business-checking/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bluevine.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.bluevine.com/contracts/registrationterms
- group: start
  title: ''
  type: Signup
  url: https://app.bluevine.com/signup/checking
- group: start
  title: ''
  type: Login
  url: https://app.bluevine.com/login
- group: agent
  title: ''
  type: LLMsTxt
  url: https://raw.githubusercontent.com/api-evangelist/bluevine/refs/heads/main/llms/bluevine-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bluevine
- group: other
  title: ''
  type: X
  url: https://x.com/bluevine
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bluevine-dev
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bluevine-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/bluevine/refs/heads/main/plans/bluevine-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/bluevine/refs/heads/main/rate-limits/bluevine-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/bluevine/refs/heads/main/finops/bluevine-finops.yml
- group: other
  title: ''
  type: ProductPage
  url: https://www.bluevine.com/line-of-credit/
- group: other
  title: ''
  type: ProductPage
  url: https://www.bluevine.com/help-center/sending-payments/connecting-financial-apps
created: '2026-06-13'
description: Bluevine is a small business banking and lending platform offering business checking accounts, lines of credit, bill pay, invoicing, and cash flow management tools for United States small and medium businesses. Bluevine does not publish a first-party public developer API or developer portal; external programmatic connectivity is delivered through the Plaid open-banking aggregator (with Finicity/Mastercard coverage also reported) and through native app integrations to QuickBooks Online, Xero, Wave, Expensify, Stripe, Square, Gusto, Cash App, and Venmo. Deposits are FDIC-insured up to $3 million through a sweep network, with revolving credit up to $250,000 issued by Celtic Bank.
finops:
- name: Bluevine Finops
  service_category: ''
  slug: bluevine-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bluevine.png
jsonld:
- class_count: 0
  name: Bluevine Context
  property_count: 0
  slug: bluevine
layout: provider
modified: '2026-07-25'
name: Bluevine
nav: Providers
network: true
overview: 'Bluevine is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Business Banking, Small Business, Fintech, Line of Credit, and Bill Pay.


  The Bluevine catalog on APIs.io includes 1 JSON-LD context.


  Bluevine''s developer surface includes getting-started guide, documentation, support, engineering blog, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Bluevine Plans Pricing
  plan_count: 3
  slug: bluevine-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Bluevine Rate Limits
  slug: bluevine-rate-limits
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 68.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 28.6
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 25.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 19.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bluevine/refs/heads/main/screenshots/bluevine-2026-06-20T173536.png
security:
- kind: domain-security
  name: Bluevine Domain Security
  slug: bluevine-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bluevine
tags:
- Business Banking
- Small Business
- Fintech
- Line of Credit
- Bill Pay
- Invoicing
- Cash Flow
- Business Checking
- Open Banking
- Lending
- United States
- Aggregator Access
website: https://www.bluevine.com/
---
