---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jolt-charge-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jolt-charge-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jolt-charge-llms.txt
- group: company
  title: ''
  type: Website
  url: https://joltcharge.com/au/
- group: company
  title: ''
  type: Blog
  url: https://joltcharge.com/au/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://joltcharge.com/au/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jolt-charge
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jolt-charge
- group: operate
  title: ''
  type: Support
  url: https://joltcharge.com/au/contact/
- group: operate
  title: ''
  type: ContactForm
  url: https://joltcharge.com/au/contact/
- group: start
  title: ''
  type: SignUp
  url: https://joltcharge.com/au/start/
- group: commercial
  title: ''
  type: Pricing
  url: https://joltcharge.com/au/jolt-plus/
- group: company
  title: ''
  type: Careers
  url: https://joltcharge.com/au/careers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://joltcharge.com/au/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://joltcharge.com/au/privacy/
- group: other
  title: ''
  type: FairUsePolicy
  url: https://joltcharge.com/au/fair-use-policy/
created: '2026-07-27'
description: 'JOLT is a Sydney-headquartered electric vehicle charging network operator that builds and runs free-to-start kerbside DC fast chargers across Australia, and has since extended the same model into New Zealand, Canada, the United Kingdom and the United States. Its charge points deliver the first 7kWh of each day''s charging at no cost — around 45km of range in roughly 15 minutes over CCS2 or CHAdeMO — funded not by the driver but by the digital out-of-home advertising screens mounted on the charger itself, which makes JOLT simultaneously a charge point operator and a media network selling audience reach to advertisers. It sits in the energy value chain as a downstream infrastructure and demand-side player: it buys electricity (claiming 100% GreenPower green-certified wind and solar), owns and operates the charging assets on public and retail land in partnership with governments and hosts such as Transport for NSW, Ausgrid and major grocery retailers, and monetises the dwell time
  rather than the kilowatt-hour. Its API posture is honestly closed. JOLT publishes no developer programme, no API documentation, no OpenAPI or other machine-readable contract, and no open data feed; the only public HTTP surfaces on its domains are a marketing WordPress install (whose custom jolt/v1 REST namespace exposes a single VAT form endpoint) and an api.joltcharge.com host that serves a static redirect to the mobile app rather than any API. It is not a designated data holder under the Australian Consumer Data Right for energy — it does not appear in the CDR Register''s energy data holder brands — so the CDR energy mandate that compels Australian electricity retailers to expose standardised usage and tariff data does not reach it, and no OCPP, OCPI, ISO 15118 or Green Button/ESPI conformance is published. All customer charging data, session history and audience analytics are reachable only through the JOLT consumer app or a sales conversation.'
image: https://joltcharge.com/au/wp-content/uploads/sites/10/2023/05/jolt-logo.svg
layout: provider
modified: '2026-07-27'
name: JOLT
nav: Providers
network: true
overview: 'JOLT is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Australia, EV Charging, Electricity, and Utilities.


  JOLT''s developer surface includes engineering blog, support, signup flow, pricing, and 12 more developer resources.'
random_paper: 87
score:
  band: emerging
  composite: 19.3
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 19.3
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 25.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: domain-security
  name: Jolt Charge Domain Security
  slug: jolt-charge-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jolt-charge
tags:
- Energy
- Australia
- EV Charging
- Electricity
- Utilities
- Renewables
- Advertising
- Mobility
- Carbon
- Infrastructure
website: https://joltcharge.com/au/
---
