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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/amore-cloud/hosts/amore-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amore-cloud-hosts.yml
- group: auth
  href: https://artifacts.apis.io/amore-cloud/security/amore-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amore-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amore.cloud/
coverage:
  checked: '2026-11-01'
  detail: The company provides consulting services and does not expose a public API.
  evidence:
  - status: 200
    url: https://amore.cloud/
  reason: not-a-software-company
  state: none
created: '2026-11-01'
description: Starberg & More Solutions AB is a Swedish IT consultancy specializing in AI services, system integrations, custom software development, and IT infrastructure. With over 20 years of experience, they help businesses automate processes, connect ERP, CRM and e‑commerce platforms, and build tailored web services and applications.
image: https://amore.cloud/img/logo.png
layout: provider
modified: '2026-11-01'
name: Starberg & More Solutions AB
nav: Providers
network: true
overview: Starberg & More Solutions AB is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include IT Consulting, Artificial Intelligence, Integration, Software Development, and Sweden.
random_paper: 8
scopes:
- name: Amore Cloud Scopes
  scope_count: 0
  slug: amore-cloud-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 4.7
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Amore Cloud Authentication
  slug: amore-cloud-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Amore Cloud Domain Security
  slug: amore-cloud-domain-security
  summary_line: TLSv1.3 · DMARC
slug: amore-cloud
tags:
- IT Consulting
- Artificial Intelligence
- Integration
- Software Development
- Sweden
website: https://amore.cloud/
---
