---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public API for Ausschreibungsagenten.de providing access to procurement notices and related data.
  name: Ausschreibungsagenten API
  slug: ausschreibungsagenten-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/ausschreibungsagenten-de/plans/ausschreibungsagenten-de-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ausschreibungsagenten-de-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/ausschreibungsagenten-de/llms/ausschreibungsagenten-de-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ausschreibungsagenten-de-llms.txt
- group: other
  href: https://artifacts.apis.io/ausschreibungsagenten-de/a2a/ausschreibungsagenten-de-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ausschreibungsagenten-de-a2a.yml
- group: agent
  href: https://artifacts.apis.io/ausschreibungsagenten-de/well-known/ausschreibungsagenten-de-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ausschreibungsagenten-de-well-known.yml
- group: other
  href: https://artifacts.apis.io/ausschreibungsagenten-de/hosts/ausschreibungsagenten-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ausschreibungsagenten-de-hosts.yml
- group: other
  href: https://artifacts.apis.io/ausschreibungsagenten-de/vendors/ausschreibungsagenten-de-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ausschreibungsagenten-de-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ausschreibungsagenten.de/status/ausschreibungsagenten
- group: start
  title: ''
  type: Login
  url: https://www.ausschreibungsagenten.de/login
- group: docs
  title: ''
  type: APIReference
  url: https://api.ausschreibungsagenten.de/docs
- group: auth
  href: https://artifacts.apis.io/ausschreibungsagenten-de/security/ausschreibungsagenten-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ausschreibungsagenten-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ausschreibungsagenten.de/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ausschreibungsagenten.de/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.ausschreibungsagenten.de/entwickler
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ausschreibungsagenten.de/pricing.md
- group: company
  title: ''
  type: About
  url: https://www.ausschreibungsagenten.de/ueber-uns
coverage:
  checked: '2026-11-02'
  detail: The API documentation page renders a Swagger UI but the OpenAPI file fetched does not belong to Ausschreibungsagenten.de, indicating no usable machine‑readable spec.
  evidence:
  - status: 200
    url: https://api.ausschreibungsagenten.de/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Ausschreibungsagenten.de is a Berlin‑based platform that automates the discovery of public procurement notices across Germany, Austria and Switzerland. It aggregates data from dozens of official tender portals, enriches each notice with original sources, and presents searchable, explainable matches for companies to evaluate opportunities. The service emphasizes transparent AI‑driven matching, data provenance within the EU, and a user‑friendly interface for both end‑users and developers via its public API.
image: https://www.ausschreibungsagenten.de/og-image.png
layout: provider
modified: '2026-11-02'
name: Ausschreibungsagenten.de
nav: Providers
network: true
overview: 'Ausschreibungsagenten.de is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Procurement, Artificial Intelligence, Public Data, and Germany.


  Ausschreibungsagenten.de''s developer surface includes API reference, documentation, pricing, and 12 more developer resources.'
plans:
- name: Ausschreibungsagenten De Plans Pricing
  plan_count: 5
  slug: ausschreibungsagenten-de-plans-pricing
random_paper: 22
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 66.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 24.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ausschreibungsagenten De Domain Security
  slug: ausschreibungsagenten-de-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: ausschreibungsagenten-de
tags:
- Company
- Procurement
- Artificial Intelligence
- Public Data
- Germany
website: https://www.ausschreibungsagenten.de/
---
