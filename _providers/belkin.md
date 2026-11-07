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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/belkin/hosts/belkin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/belkin-hosts.yml
- group: other
  href: https://artifacts.apis.io/belkin/vendors/belkin-vendors.yml
  title: ''
  type: Vendors
  url: vendors/belkin-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.belkin.com/support/product-replacement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.belkin.com/legal/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.belkin.com/company/newsroom/
- group: start
  title: ''
  type: Login
  url: https://www.belkin.com/login/
- group: docs
  title: ''
  type: Documentation
  url: https://www.belkin.com/shop-by/guides/
- group: company
  title: ''
  type: Blog
  url: https://www.belkin.com/company/blog/
- group: auth
  href: https://artifacts.apis.io/belkin/security/belkin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/belkin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://belkin.com/
coverage:
  checked: '2026-10-28'
  detail: Belkin sells consumer accessories and provides no public developer API.
  evidence:
  - status: 200
    url: https://www.belkin.com
  reason: not-a-software-company
  state: none
created: '2026-10-28'
description: Belkin provides a range of consumer electronics accessories, including chargers, power banks, wireless charging stations, and cable adapters. It also offers protective accessories such as screen protectors and phone cases for devices like iPhone, Samsung, Google, and Nintendo Switch. The product lineup extends to audio devices, computer peripherals, and surge protection equipment for home and office use.
layout: provider
modified: '2026-10-28'
name: Belkin WeMo
nav: Providers
network: true
overview: 'Belkin WeMo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Chargers, Power Banks, Phone Cases, Cables, and Adapters.


  Belkin WeMo''s developer surface includes support, documentation, engineering blog, and 7 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 45.5
    operational_transparency: 0.0
  previous_composite: 12.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 6.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/belkin/belkin-2026-11-03T121643.png
security:
- kind: domain-security
  name: Belkin Domain Security
  slug: belkin-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: belkin
tags:
- Chargers
- Power Banks
- Phone Cases
- Cables
- Adapters
- Audio
- Screen Protectors
- Surge Protectors
website: https://belkin.com/
---
