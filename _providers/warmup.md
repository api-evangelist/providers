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
- group: agent
  href: https://artifacts.apis.io/warmup/llms/warmup-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/warmup-llms.txt
- group: other
  href: https://artifacts.apis.io/warmup/hosts/warmup-hosts.yml
  title: ''
  type: Hosts
  url: hosts/warmup-hosts.yml
- group: other
  href: https://artifacts.apis.io/warmup/vendors/warmup-vendors.yml
  title: ''
  type: Vendors
  url: vendors/warmup-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.warmup.co.uk/support
- group: start
  title: ''
  type: SignUp
  url: https://tools.warmup.co.uk/register-warranty
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.warmup.co.uk/privacy-policy
- group: auth
  href: https://artifacts.apis.io/warmup/security/warmup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/warmup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.warmup.co.uk/
- group: company
  title: ''
  type: Blog
  url: https://www.warmup.co.uk/blog
- group: commercial
  title: ''
  type: Terms
  url: https://www.warmup.co.uk/terms-and-conditions
- group: company
  title: ''
  type: About
  url: https://www.warmup.co.uk/about
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found on any discovered host.
  evidence:
  - status: 404
    url: https://www.warmup.co.uk/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Warmup Plc is a UK‑based provider of underfloor heating solutions, offering a range of electric and water‑based heating systems, thermostats, insulation products and related services. The company serves residential and commercial customers, provides trade support, sustainability information, and a blog with heating advice. Warmup’s website showcases product catalogs, technical documentation, and contact options for installers and end‑users.
layout: provider
modified: '2026-10-28'
name: Warmup (underfloor heating)
nav: Providers
network: true
overview: 'Warmup (underfloor heating) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Underfloor Heating, United Kingdom, Home Improvement, and HVAC.


  Warmup (underfloor heating)''s developer surface includes support, signup flow, engineering blog, terms of service, and 7 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 51.8
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/warmup/warmup-2026-11-03T150006.png
security:
- kind: domain-security
  name: Warmup Domain Security
  slug: warmup-domain-security
  summary_line: TLSv1.3 · HSTS
slug: warmup
tags:
- Company
- Underfloor Heating
- United Kingdom
- Home Improvement
- HVAC
website: https://www.warmup.co.uk/
---
