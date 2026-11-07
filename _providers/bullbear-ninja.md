---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Financial data platform providing public filings, government documents, and research analyses for US and Korean listed companies.
  name: Bullbear Ninja API
  slug: bullbear-ninja-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/bullbear-ninja/hosts/bullbear-ninja-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bullbear-ninja-hosts.yml
- group: other
  href: https://artifacts.apis.io/bullbear-ninja/vendors/bullbear-ninja-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bullbear-ninja-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bullbear.ninja/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bullbear.ninja/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://bullbear.ninja/pricing
- group: start
  title: ''
  type: Login
  url: https://bullbear.ninja/login
- group: other
  title: ''
  type: Leadership
  url: https://bullbear.ninja/symbol/TEAM
- group: auth
  href: https://artifacts.apis.io/bullbear-ninja/security/bullbear-ninja-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bullbear-ninja-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bullbear.ninja/
coverage:
  checked: '2026-11-03'
  detail: The site provides no public API documentation or machine‑readable contracts.
  evidence:
  - status: 200
    url: https://bullbear.ninja/
  reason: no-developer-program
  state: none
created: '2026-11-03'
description: Argos (bullbear.ninja) is a Korean‑language financial data platform that aggregates public filings, government documents, and research‑firm analyses to provide investors with a timeline of fundamental changes for US and Korean listed companies. The service offers real‑time alerts, market screens, and portfolio tools, helping users make data‑driven decisions across equities, crypto, and short‑term finance.
image: https://bullbear.ninja/opengraph-image?4265f04deffc1be3
layout: provider
modified: '2026-11-03'
name: Argos
nav: Providers
network: true
overview: 'Argos is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Data, Analytics, and Korean.


  Argos'' developer surface includes pricing and 8 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bullbear Ninja Domain Security
  slug: bullbear-ninja-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bullbear-ninja
tags:
- Company
- Finance
- Data
- Analytics
- Korean
- Markets
website: https://bullbear.ninja/
---
