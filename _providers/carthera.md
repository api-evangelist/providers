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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
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
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/carthera/well-known/carthera-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carthera-well-known.yml
- group: other
  href: https://artifacts.apis.io/carthera/hosts/carthera-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carthera-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carthera.eu/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/carthera/security/carthera-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carthera-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carthera.eu
coverage:
  checked: '2026-10-07'
  detail: The OpenAPI endpoint returns an HTML page instead of a machine‑readable spec.
  evidence:
  - status: 200
    url: https://carthera.eu/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Carthera® is a clinical‑stage med‑tech company focused on developing innovative ultrasound‑based medical devices to treat severe brain disorders such as glioblastoma, brain metastases, Alzheimer’s disease and spinal‑level amyotrophic lateral sclerosis. Founded in 2010 as a spin‑off from AP‑HP, it operates in France and the USA, with a team of scientists, clinicians and industry experts aiming to revolutionize brain disease treatment.
image: https://carthera.eu/wp-content/uploads/2024/07/240701-Carthera-Forfait-Innovation-EN.pdf
layout: provider
modified: '2026-10-07'
name: Carthera
nav: Providers
network: true
overview: Carthera is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Technology, Ultrasound, Brain Disorders, Clinical Stage, and France.
random_paper: 2
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
    - north-america
  previous_composite: 7.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/carthera/carthera-2026-11-03T123428.png
security:
- kind: domain-security
  name: Carthera Domain Security
  slug: carthera-domain-security
  summary_line: TLSv1.3
slug: carthera
tags:
- Medical Technology
- Ultrasound
- Brain Disorders
- Clinical Stage
- France
- USA
website: https://carthera.eu
---
