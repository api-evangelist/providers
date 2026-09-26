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
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://airex-energy.com/
- group: company
  title: ''
  type: Newsroom
  url: https://airex-energy.com/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airex-energy.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://airex-energy.com/terms-and-conditions/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airexenergy/refs/heads/main/security/airexenergy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airexenergy-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/airexenergy/refs/heads/main/llms/airexenergy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airexenergy-llms.txt
coverage:
  checked: '2026-09-19'
  detail: Airex Energy is an industrial biomass-torrefaction manufacturer whose entire web presence is a WordPress marketing site — /api, /docs, /api-docs, /openapi.json, /swagger.json and every /.well-known/ path return the site's 404 template, and the only HTTP 200 JSON surface, /wp-json/, exposes nothing but WordPress core and third-party plugin namespaces (Yoast, Elementor, WPML, Gravity Forms, Wordfence).
  evidence:
  - status: 200
    url: https://airex-energy.com/
  - status: 404
    url: https://airex-energy.com/openapi.json
  - status: 404
    url: https://airex-energy.com/api-docs
  - status: 404
    url: https://airex-energy.com/.well-known/agent-card.json
  - status: 200
    url: https://airex-energy.com/wp-json/
  reason: no-developer-program
  state: none
created: '2026-09-19'
description: Airex Energy (Airex Énergie) is a Laval, Québec cleantech company that converts residual biomass — forest residues, sawdust, bark and recycled wood — into biocoal, biochar and biocarbon using its patented CarbonFX torrefaction technology. Founded in 2014 as a division of Airex Industries, it operates a commercial biocoal pellet plant in Bécancour, Québec, has partnered with SUEZ to industrialize biochar production in Europe and North America, and raised a CAD $38 million Series B in 2024. It is an industrial manufacturer and does not publish a developer program or public API.
layout: provider
modified: '2026-09-19'
name: Airex Energy
nav: Providers
network: true
overview: Airex Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biochar, Biocoal, Bioenergy, and Torrefaction.
random_paper: 21
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 45.5
    operational_transparency: 0.0
  previous_composite: 8.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Airexenergy Domain Security
  slug: airexenergy-domain-security
  summary_line: DMARC
slug: airexenergy
tags:
- Company
- Biochar
- Biocoal
- Bioenergy
- Torrefaction
- Carbon Removal
- Clean Technology
- Biomass
- Manufacturing
website: https://airex-energy.com/
---
