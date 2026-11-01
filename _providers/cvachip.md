---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Chinese semiconductor company providing AI scaler chips, microcontrollers, and smart sensor solutions.
  name: Cvachip API
  slug: cvachip-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/cvachip/hosts/cvachip-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cvachip-hosts.yml
- group: auth
  href: https://artifacts.apis.io/cvachip/security/cvachip-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cvachip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cvachip.com
coverage:
  checked: '2026-10-12'
  detail: The provider's website does not expose any machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.cvachip.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Cvachip (曦华科技) is a Chinese semiconductor company specializing in AI scaler chips, microcontrollers, and smart sensor solutions for automotive and IoT applications. Their products include AI Scaler ASICs, TMCU-CVM series MCUs, and smart display and touch chips, targeting high‑performance, low‑power edge AI deployments. The company emphasizes safety‑critical standards such as ISO26262 and offers comprehensive hardware and software integration services.
layout: provider
modified: '2026-10-12'
name: Cvachip
nav: Providers
network: true
overview: Cvachip is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Artificial Intelligence, Automotive, and IoT.
random_paper: 14
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 3.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cvachip Domain Security
  slug: cvachip-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cvachip
tags:
- Company
- Semiconductors
- Artificial Intelligence
- Automotive
- IoT
website: https://www.cvachip.com
---
