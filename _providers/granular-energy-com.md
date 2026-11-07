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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/granular-energy-com/vendors/granular-energy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/granular-energy-com-vendors.yml
- group: other
  href: https://artifacts.apis.io/granular-energy-com/hosts/granular-energy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/granular-energy-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.granular-energy.com/legal-notice
- group: operate
  title: ''
  type: Support
  url: https://support.granular-energy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.granular-energy.com/
- group: auth
  href: https://artifacts.apis.io/granular-energy-com/security/granular-energy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/granular-energy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://granular-energy.com
coverage:
  checked: '2026-10-23'
  detail: Home page returns minimal HTML and blocks access to API spec URLs.
  evidence:
  - status: 200
    url: https://granular.energy
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Granular Energy provides software tools that enable utilities, energy traders and buyers to manage and trade clean energy certificates such as RECs, I‑RECs, GOs and REGOs. The platform offers unified compliance and voluntary EAC management, supports development of location‑based and hourly‑matched renewable products, and automates third‑party verified reporting. It is aimed at energy industry professionals seeking scalable, transparent solutions for clean‑power strategy and procurement.
image: https://images.prismic.io/granular-marketing-website/a3763a08-8041-45e4-b714-b8fcf4ff739f_lichtblick_granular_energy.jpg?auto=compress,format&rect=0,225,3183,1671&w=2400&h=1260
layout: provider
modified: '2026-10-23'
name: Granular
nav: Providers
network: true
overview: 'Granular is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Clean Energy Software, Energy Attribute Certificates, Renewable Energy Management, and Carbon Transparency.


  Granular''s developer surface includes support, documentation, and 5 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 39.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 6.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/granular-energy-com/granular-energy-com-2026-11-03T133015.png
security:
- kind: domain-security
  name: Granular Energy Com Domain Security
  slug: granular-energy-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: granular-energy-com
tags:
- Clean Energy Software
- Energy Attribute Certificates
- Renewable Energy Management
- Carbon Transparency
website: http://granular-energy.com
---
