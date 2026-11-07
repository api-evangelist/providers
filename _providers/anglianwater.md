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
api_count: 1
apis:
- description: Public API referenced on Anglian Water website, but no machine-readable contract was found.
  name: Anglian Water API
  slug: anglian-water-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/anglianwater/hosts/anglianwater-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anglianwater-hosts.yml
- group: other
  href: https://artifacts.apis.io/anglianwater/vendors/anglianwater-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anglianwater-vendors.yml
- group: auth
  href: https://artifacts.apis.io/anglianwater/security/anglianwater-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anglianwater-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.anglianwater.co.uk
coverage:
  checked: '2026-11-01'
  detail: No machine-readable API contract (OpenAPI, AsyncAPI, GraphQL, gRPC, WSDL) was found despite probing known spec endpoints.
  evidence:
  - status: 200
    url: https://api.co.uk/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Anglian Water Services Limited is a water company that operates in the East of England. It was formed in 1989 under the partial privatisation of the water industry. It provides water supply, sewerage and sewage treatment to the area formerly the responsibility of the Anglian Water Authority. The remaining functions of the authority were transferred to the Environment Agency. Anglian Water is regulated under the United Kingdom Water Industry Act 1991.
image: https://thumb.wikimedia.org/wikipedia/en/thumb/6/67/Anglian_water.png/330px-Anglian_water.png
layout: provider
modified: '2026-11-01'
name: Anglian Water
nav: Providers
network: true
overview: Anglian Water is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Water, Utilities, United Kingdom, Infrastructure, and Public Service.
random_paper: 5
score:
  band: minimal
  composite: 4.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 4.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anglianwater Domain Security
  slug: anglianwater-domain-security
  summary_line: TLSv1.3 · DMARC
slug: anglianwater
tags:
- Water
- Utilities
- United Kingdom
- Infrastructure
- Public Service
website: https://www.anglianwater.co.uk
---
