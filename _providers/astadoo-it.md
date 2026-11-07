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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AI‑powered search and monitoring of Italian judicial auction listings.
  name: AstaDoo API
  slug: astadoo-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/astadoo-it/llms/astadoo-it-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/astadoo-it-llms.txt
- group: agent
  href: https://artifacts.apis.io/astadoo-it/well-known/astadoo-it-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/astadoo-it-well-known.yml
- group: other
  href: https://artifacts.apis.io/astadoo-it/hosts/astadoo-it-hosts.yml
  title: ''
  type: Hosts
  url: hosts/astadoo-it-hosts.yml
- group: other
  href: https://artifacts.apis.io/astadoo-it/vendors/astadoo-it-vendors.yml
  title: ''
  type: Vendors
  url: vendors/astadoo-it-vendors.yml
- group: auth
  href: https://artifacts.apis.io/astadoo-it/security/astadoo-it-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astadoo-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://astadoo.it/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://astadoo.it/privacy
coverage:
  checked: '2026-11-02'
  detail: API reference page https://astadoo.it/api returns 404 and no machine‑readable specification was found.
  evidence:
  - status: 404
    url: https://astadoo.it/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: 'AstaDoo trova, analizza e monitora le aste immobiliari dei tribunali italiani: ricerca in linguaggio naturale, lettura del fascicolo con citazione dei documenti, avvisi via email. Strumento con intelligenza artificiale per le aste immobiliari giudiziarie italiane: ricerca in linguaggio naturale, lettura del fascicolo con citazione dei documenti, storico dei ribassi e avvisi via email sulle ricerche salvate.'
image: https://astadoo.it/og.png
layout: provider
modified: '2026-11-01'
name: AstaDoo
nav: Providers
network: true
overview: AstaDoo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Auctions, Artificial Intelligence, Italy, and Legal Tech.
random_paper: 5
scopes:
- name: Astadoo It Scopes
  scope_count: 0
  slug: astadoo-it-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - italy
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - italy-southern-europe
  previous_composite: 9.1
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Astadoo It Authentication
  slug: astadoo-it-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Astadoo It Domain Security
  slug: astadoo-it-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: astadoo-it
tags:
- Real Estate
- Auctions
- Artificial Intelligence
- Italy
- Legal Tech
website: https://astadoo.it/
---
