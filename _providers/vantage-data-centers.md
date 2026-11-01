---
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/vantage-data-centers/well-known/vantage-data-centers-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vantage-data-centers-well-known.yml
- group: other
  href: https://artifacts.apis.io/vantage-data-centers/hosts/vantage-data-centers-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vantage-data-centers-hosts.yml
- group: other
  href: https://artifacts.apis.io/vantage-data-centers/vendors/vantage-data-centers-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vantage-data-centers-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vantage-dc.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vantage-dc.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://vantage-dc.com/news/vantage-supports-colorado-river-basin-water-resilience-initiative/
- group: start
  title: ''
  type: Login
  url: https://vantage-dc.com/Login
- group: other
  title: ''
  type: Leadership
  url: https://vantage-dc.com/Leadership
- group: company
  title: ''
  type: Blog
  url: https://blog.vantage-dc.com/
- group: auth
  href: https://artifacts.apis.io/vantage-data-centers/security/vantage-data-centers-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vantage-data-centers-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vantage-dc.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://vantage-dc.com/mcp
  - status: 403
    url: https://go.vantage-dc.com/mcp
  - status: 200
    url: https://vantage-dc.com/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Vantage Data Centers provides innovative, scalable wholesale data center campuses to hyperscalers, cloud providers and large enterprises across North America and Europe. They offer secure, high‑performance facilities with robust power, cooling and connectivity, supporting critical digital infrastructure and enabling rapid growth for technology‑driven businesses.
image: https://vantage-dc.com/wp-content/uploads/2020/12/Vantage-Default-Social-Share-Image.jpg
layout: provider
modified: '2026-10-22'
name: Vantage Data Centers
nav: Providers
network: true
overview: 'Vantage Data Centers is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Data Centers, Build-to-Suit, Cloud Infrastructure, Sustainability, and Power.


  Vantage Data Centers'' developer surface includes engineering blog and 10 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 51.8
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Vantage Data Centers Domain Security
  slug: vantage-data-centers-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vantage-data-centers
tags:
- Data Centers
- Build-to-Suit
- Cloud Infrastructure
- Sustainability
- Power
- Cooling
- Security
website: https://vantage-dc.com/
---
