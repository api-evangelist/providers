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
  href: https://artifacts.apis.io/polleninfo/hosts/polleninfo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/polleninfo-hosts.yml
- group: auth
  href: https://artifacts.apis.io/polleninfo/security/polleninfo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/polleninfo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://polleninformation.eu/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/polleninfo-org
coverage:
  checked: '2026-10-29'
  detail: The provider's website does not expose any machine‑readable API specification despite public pages.
  evidence:
  - status: 200
    url: https://www.polleninformation.eu/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Polleninfo is a cooperative European community of health science providers, maintained by the Austrian Pollen Information Service. It aggregates and disseminates pollen and allergy-related data across Europe, offering open data resources for researchers, healthcare professionals, and the public. The platform aims to improve public health awareness and support scientific studies on pollen trends and allergy impacts.
image: https://www.polleninformation.eu/_assets/cf1944a641108535bb7d5a965d00f539/Images/logo_polleninfo.svg
layout: provider
modified: '2026-10-28'
name: Polleninfo
nav: Providers
network: true
overview: Polleninfo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Allergy, Data, and Europe.
random_paper: 22
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 4.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/polleninfo/polleninfo-2026-11-03T141346.png
security:
- kind: domain-security
  name: Polleninfo Domain Security
  slug: polleninfo-domain-security
  summary_line: TLSv1.2
slug: polleninfo
tags:
- Company
- Health
- Allergy
- Data
- Europe
website: https://polleninformation.eu/
---
