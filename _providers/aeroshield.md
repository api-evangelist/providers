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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aeroshield-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aeroshield-llms.txt
- group: company
  title: ''
  type: Website
  url: https://aeroshield.tech/
- group: company
  title: ''
  type: About
  url: https://aeroshield.tech/about-us
- group: operate
  title: ''
  type: FAQ
  url: https://aeroshield.tech/faq
- group: operate
  title: ''
  type: Contact
  url: https://aeroshield.tech/contact
- group: company
  title: ''
  type: Newsroom
  url: https://aeroshield.tech/press
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aeroshield-inc/
coverage:
  checked: '2026-09-10'
  detail: AeroShield manufactures transparent silica aerogel sheets for insulated window glass and sells B2B to window and door makers; its entire web presence is a seven-page static Astro marketing site with no developer, docs, app or api subdomain resolving on aeroshield.tech.
  evidence:
  - status: 404
    url: https://aeroshield.tech/openapi.json
  - status: 404
    url: https://aeroshield.tech/.well-known/api-catalog
  - status: 404
    url: https://aeroshield.tech/llms.txt
  - status: 404
    url: https://api.github.com/orgs/aeroshield
  reason: not-a-software-company
  state: none
created: '2026-09-10'
description: AeroShield (AeroShield Materials, Inc.) is a Waltham, Massachusetts materials science company spun out of MIT in 2019 that has developed and scaled the world's most transparent silica aerogel. Its ultra-clear aerogel sheets are laminated into insulated glass units so that a standard double-pane window or door can outperform a triple pane while remaining thinner and lighter, boosting thermal efficiency by up to 65%. The company sells business-to-business to window, door and skylight manufacturers rather than to consumers, operates a pilot manufacturing facility in Waltham, and was selected for a $14.5M ARPA-E award. It publishes no developer program, no public API, and no machine-readable API artifacts; this profile records that absence.
image: https://cdn.sanity.io/images/387hr0u0/production/568fb5d28e6defec372abd46c082186ccad410a3-186x42.svg
layout: provider
modified: '2026-09-10'
name: AeroShield
nav: Providers
network: true
overview: 'AeroShield is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Materials Science, Aerogel, Building Materials, and Energy Efficiency.


  AeroShield''s developer surface includes FAQ and 7 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aeroshield Domain Security
  slug: aeroshield-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aeroshield
tags:
- Company
- Materials Science
- Aerogel
- Building Materials
- Energy Efficiency
- Windows
- Manufacturing
- Climate Tech
website: https://aeroshield.tech/
---
