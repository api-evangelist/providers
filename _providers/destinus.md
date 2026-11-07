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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/destinus/hosts/destinus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/destinus-hosts.yml
- group: other
  href: https://artifacts.apis.io/destinus/vendors/destinus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/destinus-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.destinus.com/press/news
- group: auth
  href: https://artifacts.apis.io/destinus/security/destinus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/destinus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.destinus.com/
coverage:
  checked: '2026-10-23'
  detail: No API documentation or machine‑readable contract was found for Destinus.
  evidence:
  - status: 200
    url: https://tc-test.destinus.com/docs/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Destinus is a European defence manufacturer focused on scalable strike and air‑defence systems for European and allied armed forces. It delivers autonomous, AI‑driven weapon subsystems such as Kryla, Hornet, Ruta and Vorexon, emphasizing industrial‑scale production, rapid iteration, and strategic autonomy for Europe. The company’s mission is to strengthen Europe’s security through advanced, affordable, cost‑asymmetric systems, with a vertically integrated OEM approach and a unified autonomy stack.
image: https://cdn.prod.website-files.com/696aa687f423696991481f4a/69d15fb972ae6e8cace05ef3_177b3ae27549c6ec3b26507aed998e14_open-graph-basic-title.png
layout: provider
modified: '2026-10-22'
name: Destinus
nav: Providers
network: true
overview: Destinus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defence, Aerospace, Weapons, and Europe.
random_paper: 15
score:
  band: minimal
  composite: 3.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 3.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/destinus/destinus-2026-11-03T130546.png
security:
- kind: domain-security
  name: Destinus Domain Security
  slug: destinus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: destinus
tags:
- Company
- Defence
- Aerospace
- Weapons
- Europe
website: https://www.destinus.com/
---
