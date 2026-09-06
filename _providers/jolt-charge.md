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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
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
random_paper: 12
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 16.6
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 25.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jolt-charge/refs/heads/main/screenshots/jolt-charge-2026-08-07T171029.png
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
