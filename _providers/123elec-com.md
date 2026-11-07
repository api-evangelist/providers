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
- group: agent
  href: https://artifacts.apis.io/123elec-com/llms/123elec-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/123elec-com-llms.txt
- group: other
  href: https://artifacts.apis.io/123elec-com/hosts/123elec-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/123elec-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/123elec-com/vendors/123elec-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/123elec-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/123elec-com/security/123elec-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/123elec-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://123elec.com/
- group: company
  title: ''
  type: Blog
  url: https://www.blog.123elec.com/
- group: operate
  title: ''
  type: Support
  url: https://www.123elec.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.123elec.com/cgv
coverage:
  checked: '2026-10-31'
  detail: 123elec.com is a retail e‑commerce site selling electrical hardware and does not provide a public API.
  evidence:
  - status: 200
    url: https://www.123elec.com/
  reason: not-a-software-company
  state: none
created: '2026-10-31'
description: 'Site officiel 123elec : Boutique en ligne de matériel électrique divers spécialisée dans les installations électriques domestiques et proposant des prix intéressants sur de grandes marques (Legrand, Schneider, Hager, Wago, etc.) sur l''ensemble des équipements et appareillages électriques.'
image: https://www.123elec.com/static/version1792532770/frontend/Phaseneutre/hyva/fr_FR/images/favicon/favicon-32x32.png?frz-v=2121
layout: provider
modified: '2026-10-31'
name: 123elec
nav: Providers
network: true
overview: '123elec is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Electrical, Hardware, Retail, and France.


  123elec''s developer surface includes engineering blog, support, and 6 more developer resources.'
plans:
- name: 123Elec Com Plans Pricing
  plan_count: 0
  slug: 123elec-com-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: 123Elec Com Rate Limits
  slug: 123elec-com-rate-limits
scopes:
- name: 123Elec Com Scopes
  scope_count: 0
  slug: 123elec-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.0
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 9.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 123Elec Com Authentication
  slug: 123elec-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: 123Elec Com Domain Security
  slug: 123elec-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 123elec-com
tags:
- E-Commerce
- Electrical
- Hardware
- Retail
- France
website: https://123elec.com/
---
