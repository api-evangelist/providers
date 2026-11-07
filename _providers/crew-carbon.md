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
- description: API reference not publicly documented.
  name: CREW Carbon API
  slug: crew-carbon-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/crew-carbon/hosts/crew-carbon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crew-carbon-hosts.yml
- group: other
  href: https://artifacts.apis.io/crew-carbon/vendors/crew-carbon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crew-carbon-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crewcarbon.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://crewcarbon.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://crewcarbon.com/team/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crewcarbon
- group: auth
  href: https://artifacts.apis.io/crew-carbon/security/crew-carbon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crew-carbon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crewcarbon.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://crewcarbon.com/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: CREW Carbon supplies a calcium‑based alkalinity enhancement product for wastewater treatment facilities. The product is dosed into existing biological treatment processes to improve nutrient removal, settleability, and operational cost while permanently removing greenhouse gases. It is marketed to plant owners, operators, and affiliates seeking process intensification and carbon removal solutions.
image: https://crewcarbon.com/wp-content/uploads/2026/02/Copy-of-CREW-CARBON-X-20-1200x802.jpg
layout: provider
modified: '2026-10-11'
name: CREW Carbon
nav: Providers
network: true
overview: CREW Carbon is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Wastewater Treatment, Carbon Removal, Process Intensification, Alkalinity Enhancement, and Industrial Water.
random_paper: 3
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.9
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 2.6
  previous_composite: 8.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/crew-carbon/crew-carbon-2026-11-03T125609.png
security:
- kind: domain-security
  name: Crew Carbon Domain Security
  slug: crew-carbon-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: crew-carbon
tags:
- Wastewater Treatment
- Carbon Removal
- Process Intensification
- Alkalinity Enhancement
- Industrial Water
website: https://crewcarbon.com/
---
