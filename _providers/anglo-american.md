---
access_model:
  confidence: low
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/anglo-american/hosts/anglo-american-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anglo-american-hosts.yml
- group: other
  href: https://artifacts.apis.io/anglo-american/vendors/anglo-american-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anglo-american-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.angloamerican.com/site-services/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.angloamerican.com/site-services/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.angloamerican.com/media
- group: auth
  href: https://artifacts.apis.io/anglo-american/security/anglo-american-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anglo-american-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.angloamerican.com/
coverage:
  checked: '2026-11-01'
  detail: Anglo American is a mining corporation with no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.angloamerican.com/
  reason: not-a-software-company
  state: none
created: '2026-11-01'
description: Anglo American is a leading global mining company dedicated to responsibly producing copper, premium iron ore, and crop nutrients. The company focuses on sustainable mining practices, innovation, and technology integration across its operations worldwide, aiming to improve people's lives and support a low‑carbon future.
image: https://www.angloamerican.com/~/media/Images/A/Anglo-American-Group-v9/PLC/social-media-image/angloamerican-sm-21.jpg
layout: provider
modified: '2026-11-01'
name: Anglo American
nav: Providers
network: true
overview: Anglo American is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Mining, Metals, Sustainability, Global, and Resources.
plans:
- name: Anglo American Plans Pricing
  plan_count: 0
  slug: anglo-american-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Anglo American Rate Limits
  slug: anglo-american-rate-limits
scopes:
- name: Anglo American Scopes
  scope_count: 0
  slug: anglo-american-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - global
    - north-america
  previous_composite: 10.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anglo American Authentication
  slug: anglo-american-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Anglo American Domain Security
  slug: anglo-american-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anglo-american
tags:
- Mining
- Metals
- Sustainability
- Global
- Resources
website: https://www.angloamerican.com/
---
