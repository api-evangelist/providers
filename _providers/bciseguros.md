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
- description: API endpoint for BCI Seguros services (no public documentation or OpenAPI spec found).
  name: BCI Seguros API
  slug: bci-seguros-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/bciseguros/hosts/bciseguros-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bciseguros-hosts.yml
- group: other
  href: https://artifacts.apis.io/bciseguros/vendors/bciseguros-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bciseguros-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bciseguros/security/bciseguros-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bciseguros-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bciseguros.cl
coverage:
  checked: '2026-11-02'
  detail: No public OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract is available on the provider’s hosts.
  evidence:
  - status: 0
    url: https://api.bciseguros.cl/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BCI Seguros is a Chilean insurance provider offering a wide range of products including auto, home, health, life, and travel insurance. The website presents detailed information about their services, claim assistance, and corporate innovations. It emphasizes customer support with contact numbers and online claim filing, reflecting a focus on comprehensive coverage and digital assistance for individuals and businesses.
image: https://www.bciseguros.cl/wp-content/uploads/2019/01/screenshot-1.png
layout: provider
modified: '2026-11-02'
name: BCI Seguros
nav: Providers
network: true
overview: BCI Seguros is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Chile, Auto, Homes, and Health.
random_paper: 22
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - chile
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 5.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bciseguros Domain Security
  slug: bciseguros-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bciseguros
tags:
- Insurance
- Chile
- Auto
- Homes
- Health
website: https://www.bciseguros.cl
---
