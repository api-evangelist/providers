---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for 7bridges platform (access requires login).
  name: 7bridges API
  slug: 7bridges-api
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/7bridges/hosts/7bridges-hosts.yml
  title: ''
  type: Hosts
  url: hosts/7bridges-hosts.yml
- group: other
  href: https://artifacts.apis.io/7bridges/vendors/7bridges-vendors.yml
  title: ''
  type: Vendors
  url: vendors/7bridges-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.the7bridges.com/press
- group: auth
  href: https://artifacts.apis.io/7bridges/security/7bridges-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/7bridges-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.the7bridges.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://login.the7bridges.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.the7bridges.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.the7bridges.io/api/v2/redoc/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.the7bridges.com/on-boarding?hsLang=en
- group: operate
  title: ''
  type: Support
  url: https://help.the7bridges.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.the7bridges.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.the7bridges.com/terms-and-conditions?hsLang=en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.the7bridges.com/privacy-policy?hsLang=en
coverage:
  checked: '2026-10-29'
  detail: API reference at https://api.the7bridges.io/api/v2/redoc/ redirects to a login page, requiring authentication to view the spec.
  evidence:
  - status: 302
    url: https://api.the7bridges.io/api/v2/redoc/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: 7bridges provides a SaaS platform that uses AI to give end‑to‑end visibility and resilience for supply chains. The platform combines data integration, optimisation, simulation and automation to help enterprises monitor carrier performance, predict disruptions, and make data‑driven logistics decisions. Recognised with the 2023 SaaS Awards, the company serves global shippers and logistics providers, offering a digital twin of the supply network and a knowledge base for onboarding and API integration.
image: https://www.the7bridges.com/hubfs/7bridges_logo_white_ifs_wide.svg
layout: provider
modified: '2026-10-29'
name: 7bridges
nav: Providers
network: true
overview: '7bridges is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Supply Chain, Software-as-a-Service, Logistics, Artificial Intelligence, and Platform.


  7bridges'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 8 more developer resources.'
plans:
- name: 7Bridges Plans Pricing
  plan_count: 0
  slug: 7bridges-plans-pricing
random_paper: 23
scopes:
- name: 7Bridges Scopes
  scope_count: 0
  slug: 7bridges-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 58.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.2
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/7bridges/7bridges-2026-11-03T120126.png
security:
- kind: authentication
  name: 7Bridges Authentication
  slug: 7bridges-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: 7Bridges Domain Security
  slug: 7bridges-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 7bridges
tags:
- Supply Chain
- Software-as-a-Service
- Logistics
- Artificial Intelligence
- Platform
website: https://www.the7bridges.com/
---
