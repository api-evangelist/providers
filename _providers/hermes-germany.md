---
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/hermes-germany/hosts/hermes-germany-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hermes-germany-hosts.yml
- group: auth
  href: https://artifacts.apis.io/hermes-germany/security/hermes-germany-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hermes-germany-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://myhermes.de/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://myhermes.de/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Hermes Germany operates the myHermes online portal, offering parcel and freight shipping services across Germany. The platform provides customers with tools to create shipping labels, calculate costs, track parcels, and manage returns. It serves both private and business customers, featuring a network of over 17,000 Hermes PaketShops nationwide. The service integrates with e‑commerce platforms and offers APIs for shipment creation, price calculation, and tracking, enabling automated logistics workflows.
layout: provider
modified: '2026-10-28'
name: Hermes Germany
nav: Providers
network: true
overview: Hermes Germany is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Shipping, Parcel, E‑commerce, and Germany.
plans:
- name: Hermes Germany Plans Pricing
  plan_count: 0
  slug: hermes-germany-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Hermes Germany Rate Limits
  slug: hermes-germany-rate-limits
scopes:
- name: Hermes Germany Scopes
  scope_count: 0
  slug: hermes-germany-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hermes Germany Authentication
  slug: hermes-germany-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Hermes Germany Domain Security
  slug: hermes-germany-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hermes-germany
tags:
- Logistics
- Shipping
- Parcel
- E‑commerce
- Germany
website: https://myhermes.de/
---
