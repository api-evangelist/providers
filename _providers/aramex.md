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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: Create shipments, print labels, create/cancel/validate pickups, schedule delivery, hold shipments, print commercial invoices and reserve shipment number ranges.
  name: Aramex Shipping Services API
  slug: aramex-shipping
- description: Track shipments and pickups and check whether a shipment has been delivered.
  name: Aramex Shipments Tracking API
  slug: aramex-tracking
- description: Fetch countries, states, cities, offices and drop-off locations; validate addresses and check whether an address is serviced.
  name: Aramex Location Services API
  slug: aramex-location
- description: Calculate shipping rates for single and multiple shipments.
  name: Aramex Rate Calculator API
  slug: aramex-ratecalculator
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/aramex/hosts/aramex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aramex-hosts.yml
- group: other
  href: https://artifacts.apis.io/aramex/vendors/aramex-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aramex-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aramex/security/aramex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aramex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aramex.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.aramex.com/developers/aramex-apis
created: '2026-10-13'
description: Aramex is a Dubai-headquartered global logistics and express transportation company. It publishes SOAP web services (Shipping, Shipments Tracking, Location and Rate Calculator) at ws.aramex.net/ShippingAPI.V2, with WSDLs published for public download; API credentials are issued through an Aramex account.
layout: provider
modified: '2026-10-13'
name: Aramex
nav: Providers
network: true
overview: 'Aramex is listed with 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Shipping, Tracking, and SOAP.


  Aramex''s developer surface includes documentation and 4 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 24.0
    developer_ergonomics: 4.8
    discoverability: 67.9
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-arab-emirates
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  previous_composite: 13.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aramex Domain Security
  slug: aramex-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aramex
tags:
- Company
- Logistics
- Shipping
- Tracking
- SOAP
website: https://www.aramex.com
---
