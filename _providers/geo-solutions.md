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
api_count: 1
apis:
- description: Geo Solutions provides geo‑intelligence APIs for public services, utilities, transport, and industrial sectors. Documentation is not publicly available.
  name: GEO Solutions API
  slug: geo-solutions-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/geo-solutions/well-known/geo-solutions-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/geo-solutions-well-known.yml
- group: other
  href: https://artifacts.apis.io/geo-solutions/hosts/geo-solutions-hosts.yml
  title: ''
  type: Hosts
  url: hosts/geo-solutions-hosts.yml
- group: other
  href: https://artifacts.apis.io/geo-solutions/vendors/geo-solutions-vendors.yml
  title: ''
  type: Vendors
  url: vendors/geo-solutions-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.geosolutions.be/otwg20/#/login?guestlogin=12
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://geosquare.be/nl-be/privacy-policy?hsLang=nl-be
- group: company
  title: ''
  type: Blog
  url: https://geosquare.be/blog
- group: auth
  href: https://artifacts.apis.io/geo-solutions/security/geo-solutions-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/geo-solutions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://geosquare.be
coverage:
  checked: '2026-10-26'
  detail: No public developer portal or API documentation is available on the website.
  evidence:
  - status: 200
    url: https://www.geo-solutions.com/
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: GEO Solutions, operating under the GeoSquare brand, provides flexible and scalable geo‑intelligence applications and APIs for public services, utilities, transport, and industrial sectors across the Benelux region. With over 250 employees and 350+ satisfied customers, they help organizations turn location data into measurable impact through solutions like interactive geo‑portals, mobility data, route optimization, address validation, and AI‑assisted mapping.
layout: provider
modified: '2026-10-26'
name: GEO Solutions
nav: Providers
network: true
overview: 'GEO Solutions is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geo, GIS, Location Intelligence, and Belgium.


  GEO Solutions'' developer surface includes support, engineering blog, and 6 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 44.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - belgium
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 9.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/geo-solutions/geo-solutions-2026-11-03T132603.png
security:
- kind: domain-security
  name: Geo Solutions Domain Security
  slug: geo-solutions-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: geo-solutions
tags:
- Geo
- GIS
- Location Intelligence
- Belgium
website: https://geosquare.be
---
