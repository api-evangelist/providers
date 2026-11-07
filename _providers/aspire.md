---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Aspire''s public REST API for business finance automation: payout/transfer operations across 30+ currencies (local and SWIFT), FX quotes, virtual card issuance and controls, and bank-feed/transaction r'
  name: Aspire API
  slug: aspire-api
artifact_total: 9
asyncapis:
- description: ''
  name: Aspire Webhooks
  slug: aspire-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/aspire/plans/aspire-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aspire-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/aspire/mcp/aspire-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aspire-mcp.yml
- group: auth
  href: https://artifacts.apis.io/aspire/security/aspire-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aspire-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/aspire/llms/aspire-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aspire-llms.txt
- group: company
  title: ''
  type: Website
  url: https://aspireapp.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.api.aspireapp.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.aspireapp.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.api.aspireapp.com/authentication
- group: company
  title: ''
  type: Blog
  url: https://aspireapp.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.aspireapp.com/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://aspireapp.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.aspireapp.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aspireapp.com/tnc/master-service-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aspireapp.com/tnc/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://aspireapp.com/security-and-compliance
- group: auth
  title: ''
  type: Security
  url: https://aspireapp.com/security-and-compliance
- group: build
  title: ''
  type: Postman
  url: https://aspireapi.postman.co/network/import?collection=28742427-8779dc4f-4c34-42e5-b43e-9ad318f7c026-2s9YXccQHr
created: '2026-07-17'
description: Aspire is a Singapore-headquartered fintech offering an all-in-one finance platform for growing businesses operating globally. Its products include multi-currency business accounts, corporate cards, global payments and FX, expense and budget management, bill pay, bulk payments, invoice and accounts-receivable management, yield on idle balances, and global payroll. Aspire also exposes a developer API (api.aspireapp.com/public/v1) covering payouts/transfers, card issuance, and bank-feed/transaction reporting, secured with OAuth 2.0 bearer tokens (client-credentials and authorization-code + PKCE flows), idempotency keys, and webhooks. The company serves 50,000+ businesses, is backed by Lightspeed Venture Partners, and is PCI DSS v4.0.1, ISO/IEC 27001:2022, and SOC 2 Type 2 certified.
finops:
- has_sources: true
  method: derived
  name: Aspire Finops
  primary_unit: account
  service_category: ''
  slug: aspire-finops
  template: false
image: https://aspireapp.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Aspire MCP Server
  slug: aspire
modified: '2026-07-18'
name: Aspire
nav: Providers
network: true
overview: 'Aspire is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Business Banking, Payments, and Payouts.


  The Aspire catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Aspire''s developer surface includes documentation, getting-started guide, engineering blog, support, pricing, signup flow, and 11 more developer resources.'
plans:
- name: Aspire Plans Pricing
  plan_count: 3
  slug: aspire-plans-pricing
- name: Aspire Price Estimates
  plan_count: 0
  slug: aspire-price-estimates
random_paper: 20
scopes:
- name: Aspire Scopes
  scope_count: 2
  slug: aspire-scopes
  summary_line: 2 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 52.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 61.9
    discoverability: 71.7
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - singapore
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 52.1
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 35.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/aspire/aspire-2026-07-25T201432.png
security:
- kind: authentication
  name: Aspire Authentication
  slug: aspire-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Aspire Domain Security
  slug: aspire-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aspire
tags:
- Company
- Fintech
- Business Banking
- Payments
- Payouts
- Card Issuance
- Foreign Exchange
- Expense Management
- Financial Services
- Singapore
website: https://aspireapp.com
---
