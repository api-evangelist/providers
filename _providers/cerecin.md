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
api_count: 1
apis:
- description: API documentation not publicly machine-readable
  name: Cerecin API
  slug: cerecin-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/cerecin/hosts/cerecin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cerecin-hosts.yml
- group: auth
  href: https://artifacts.apis.io/cerecin/security/cerecin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cerecin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cerecin.com
- group: docs
  title: ''
  type: Documentation
  url: https://cerecin.com/science
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cerecin.com/privacy-policy
coverage:
  checked: '2026-10-08'
  detail: No OpenAPI or other machine-readable contract found on discovered hosts.
  evidence:
  - status: 0
    url: https://api.cerecin.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Cerecin is a neuroscience-focused healthcare company headquartered in Broomfield, Colorado, with additional offices in Singapore and Australia. It leverages the physiological ketone system to develop metabolic therapies for brain disorders, including rare pediatric epilepsy and Alzheimer’s disease. The firm has a diversified pipeline of products, strategic partnerships, and a scientific advisory board, aiming to address unmet medical needs in neurology through innovative drug delivery and formulation technologies.
layout: provider
modified: '2026-10-07'
name: Cerecin
nav: Providers
network: true
overview: 'Cerecin is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Neuroscience, Healthcare, Metabolism, and Neurology.


  Cerecin''s developer surface includes documentation and 4 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 53.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 8.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 6.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cerecin/cerecin-2026-11-03T123713.png
security:
- kind: domain-security
  name: Cerecin Domain Security
  slug: cerecin-domain-security
  summary_line: no transport/DNS hardening detected
slug: cerecin
tags:
- Company
- Neuroscience
- Healthcare
- Metabolism
- Neurology
website: https://cerecin.com
---
