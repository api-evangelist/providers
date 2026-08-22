---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.6
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gravity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/gravity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gravity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gravitytechnologies.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gravitytechnologies.com/terms-conditions
- group: operate
  title: ''
  type: Support
  url: https://gravitytechnologies.com/forms/contact
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/gravity-well-known.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gravity-well-known.yml
created: '2026-07-17'
description: Gravity (Gravity Technologies) builds and deploys ultra-fast DC electric-vehicle charging infrastructure for dense urban environments. Its Distributed Energy Access Points (DEAPs) deliver up to five-minute charges from compact, modular hardware that requires minimal real estate and no dedicated utility upgrade, letting operators place high-power charging in garages, curbside, and fleet depots. The company was surfaced as a portfolio company of GV and Redpoint Ventures and added to the API Evangelist network for enrichment; it publishes no public developer portal, API, or SDKs at this time, so this profile captures company identity and the domain security surface rather than API artifacts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gravity.png
layout: provider
modified: '2026-07-19'
name: Gravity
nav: Providers
network: true
overview: 'Gravity is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Frontier Tech, Electric Vehicles, EV Charging, and Energy.


  Gravity''s developer surface includes support and 7 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 9.8
  delta: -1.4
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 21.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gravity/refs/heads/main/screenshots/gravity-2026-07-25T220252.png
security:
- kind: domain-security
  name: Gravity Domain Security
  slug: gravity-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gravity Vulnerability Disclosure
  slug: gravity-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: gravity
tags:
- Company
- Frontier Tech
- Electric Vehicles
- EV Charging
- Energy
- Charging Infrastructure
- Mobility
- Clean Energy
website: https://gravitytechnologies.com
---
