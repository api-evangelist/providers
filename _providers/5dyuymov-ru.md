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
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/5dyuymov-ru/llms/5dyuymov-ru-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/5dyuymov-ru-llms.txt
- group: agent
  href: https://artifacts.apis.io/5dyuymov-ru/well-known/5dyuymov-ru-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/5dyuymov-ru-well-known.yml
- group: other
  href: https://artifacts.apis.io/5dyuymov-ru/hosts/5dyuymov-ru-hosts.yml
  title: ''
  type: Hosts
  url: hosts/5dyuymov-ru-hosts.yml
- group: auth
  href: https://artifacts.apis.io/5dyuymov-ru/security/5dyuymov-ru-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/5dyuymov-ru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://5dyuymov.ru/
- group: docs
  title: ''
  type: Documentation
  url: https://5dyuymov.ru/spec
- group: docs
  title: ''
  type: APIReference
  url: https://5dyuymov.ru/spec
- group: commercial
  title: ''
  type: TermsOfService
  url: https://5dyuymov.ru/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://5dyuymov.ru/privacy
- group: operate
  title: ''
  type: Support
  url: https://5dyuymov.ru/contact
- group: start
  title: ''
  type: DeveloperPortal
  url: https://5dyuymov.ru/b2b
coverage:
  checked: '2026-10-31'
  detail: Developer portal provides HTML docs but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://5dyuymov.ru/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: 5 дюймов (5dyuymov.ru) is a Russian supplier of pipeline fittings, pumps, and heating equipment for boiler plants and industrial production. The company offers a catalog of valves, pumps, and related accessories, providing specifications, pricing, and delivery across Russia. Customers can request detailed specifications via email or upload files, and the site includes business terms, shipping information, and contact details for sales support.
image: https://5dyuymov.ru/og/home.png
layout: provider
modified: '2026-10-31'
name: 5 дюймов
nav: Providers
network: true
overview: '5 дюймов is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pipelines, Valves, Pumps, and Heating.


  5 дюймов''s developer surface includes documentation, API reference, support, and 8 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - russia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 15.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 5Dyuymov Ru Domain Security
  slug: 5dyuymov-ru-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: 5dyuymov-ru
tags:
- Company
- Pipelines
- Valves
- Pumps
- Heating
website: https://5dyuymov.ru/
---
