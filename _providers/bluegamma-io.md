---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: BlueGamma provides real-time forward curve, swap rate and market data APIs.
  name: BlueGamma API
  slug: bluegamma-api
artifact_total: 5
common:
- group: operate
  href: https://artifacts.apis.io/bluegamma-io/rate-limits/bluegamma-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bluegamma-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/bluegamma-io/plans/bluegamma-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bluegamma-io-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bluegamma-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/bluegamma-io/authentication/bluegamma-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bluegamma-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/bluegamma-io/conformance/bluegamma-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bluegamma-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bluegamma-io/llms/bluegamma-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bluegamma-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/bluegamma-io/well-known/bluegamma-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bluegamma-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/bluegamma-io/hosts/bluegamma-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bluegamma-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/bluegamma-io/vendors/bluegamma-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bluegamma-io-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://auth.bluegamma.io/sign-up
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bluegamma.io/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.bluegamma.io/session-expired?redirect=https%3A%2F%2Fauth-api.bluegamma.io%2Fuser_management%2Fauthorize%3Fclient_id%3Dclient_01HRW99ZFVP2HV3X4J3V1Z373S%26provider%3Dauthkit%26redirect_uri%3Dhttps%253A%252F%252Fdev.bluegamma.io%252Fcallback%26response_type%3Dcode%26screen_hint%3Dsign-in%26state%3D%25257B%252522referrer%252522%25253Anull%25252C%252522redirect%252522%25253A%252522https%25253A%25252F%25252Fdev.bluegamma.io%25252F%252522%25257D
- group: company
  title: ''
  type: Blog
  url: https://www.bluegamma.io/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bluegamma.io/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://dev.bluegamma.io/
- group: docs
  title: ''
  type: APIReference
  url: https://www.bluegamma.io/llms.txt
- group: auth
  href: https://artifacts.apis.io/bluegamma-io/security/bluegamma-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bluegamma-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bluegamma.io/
created: '2026-11-02'
description: BlueGamma provides live interest rate forward curves, swap pricing, and amortising swap tools instantly via Excel, API, or web. Users can access up-to-date market data without a terminal, with a free 14‑day trial. The platform targets financial professionals needing accurate curve data for pricing and risk management, offering easy integration and comprehensive documentation.
image: https://www.bluegamma.io/images/bluegamma-og.png
layout: provider
modified: '2026-11-02'
name: BlueGamma
nav: Providers
network: true
overview: 'BlueGamma is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Market Data, Interest Rates, and Company.


  BlueGamma''s developer surface includes authentication, signup flow, pricing, engineering blog, getting-started guide, documentation, API reference, and 11 more developer resources.'
plans:
- name: Bluegamma Io Plans Pricing
  plan_count: 3
  slug: bluegamma-io-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: Bluegamma Io Rate Limits
  slug: bluegamma-io-rate-limits
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 56.0
    catalog_earned_first_party: 24.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 38.6
    discoverability: 57.1
    operational_transparency: 31.6
  provenance:
    conformance: derived
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 21.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bluegamma Io Authentication
  slug: bluegamma-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bluegamma Io Domain Security
  slug: bluegamma-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bluegamma-io
tags:
- Finance
- Market Data
- Interest Rates
- Company
website: https://bluegamma.io/
---
