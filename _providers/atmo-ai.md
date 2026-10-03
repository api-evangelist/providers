---
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atmo-ai/refs/heads/main/hosts/atmo-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atmo-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atmo-ai/refs/heads/main/vendors/atmo-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atmo-ai-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.atmo.ai/log-in
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atmo-ai/refs/heads/main/security/atmo-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atmo-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.atmo.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.atmo.ai/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atmo.ai/terms
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Atmo AI provides ultra‑precise AI‑driven weather forecasting for micro‑climates, leveraging real‑time satellite, radar, buoy and ground‑station data. Its deep‑learning models deliver forecasts up to 40,000× faster than traditional methods, achieving up to 50% higher accuracy across nowcasting to 14‑day horizons. Trusted by governments, militaries and industries worldwide, Atmo AI serves sectors such as aerospace, defense, agriculture and disaster response.
image: https://cdn.prod.website-files.com/663b054598a372edb070cf86/6645260eb57b16d6d6c4adac_Atmo%20Frame.webp
layout: provider
modified: '2026-09-26'
name: Atmo AI
nav: Providers
network: true
overview: 'Atmo AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Weather, Artificial Intelligence, Forecasting, and Climate.


  Atmo AI''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atmo Ai Domain Security
  slug: atmo-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: atmo-ai
tags:
- Company
- Weather
- Artificial Intelligence
- Forecasting
- Climate
website: https://www.atmo.ai/
---
