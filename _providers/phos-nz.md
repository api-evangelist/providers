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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/phos-nz/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/phos-nz/hosts/phos-nz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/phos-nz-hosts.yml
- group: other
  href: https://artifacts.apis.io/phos-nz/vendors/phos-nz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/phos-nz-vendors.yml
- group: auth
  href: https://artifacts.apis.io/phos-nz/security/phos-nz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/phos-nz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.phos.co.nz/
coverage:
  checked: '2026-10-29'
  detail: The company provides property management services and does not expose a public API.
  evidence:
  - status: 200
    url: https://www.phos.co.nz/
  reason: not-a-software-company
  state: none
created: '2026-10-29'
description: Phos Property Partners is a Wellington-based property management company offering residential, commercial, and industrial tenancy solutions across the Wellington region. Founded in 1967, Phos manages a growing portfolio of buildings with a focus on tenant satisfaction, strong family values, and commercial sensibility. The company emphasizes integrity, empathy, and people‑first approach while providing quality accommodation and responsive service.
image: http://static1.squarespace.com/static/6147d29a918044012d5b8f63/t/619b1c20368abe5d93cfd50d/1637555232846/output-onlinepngtools.png?format=1500w
layout: provider
modified: '2026-10-29'
name: phos-nz
nav: Providers
network: true
overview: phos-nz is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Property Management, Wellington, and NZ.
plans:
- name: Phos Nz Plans Pricing
  plan_count: 0
  slug: phos-nz-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Phos Nz Rate Limits
  slug: phos-nz-rate-limits
scopes:
- name: Phos Nz Scopes
  scope_count: 0
  slug: phos-nz-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 22
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
    developer_ergonomics: 6.4
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - new-zealand
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.2
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/phos-nz/phos-nz-2026-11-03T141156.png
security:
- kind: authentication
  name: Phos Nz Authentication
  slug: phos-nz-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Phos Nz Domain Security
  slug: phos-nz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: phos-nz
tags:
- Company
- Real Estate
- Property Management
- Wellington
- NZ
website: https://www.phos.co.nz/
---
