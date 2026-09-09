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
  scored_at: '2026-09-08'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ace-green-recycling-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.acegreenrecycling.com/
- group: company
  title: ''
  type: Blog
  url: https://www.acegreenrecycling.com/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.acegreenrecycling.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ace-recycling-pte-ltd
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.acegreenrecycling.com/#investors
coverage:
  checked: '2026-09-06'
  detail: ACE Green Recycling is an industrial battery-recycling process company that builds plants and licenses GREENLEAD and LithiumFirst metallurgical technology; its entire web presence is a single WordPress marketing page plus a newsroom, with no developer, docs, or API section in the navigation and every contract-discovery path returning the site's 404 template.
  evidence:
  - status: 200
    url: https://www.acegreenrecycling.com/
  - status: 404
    url: https://acegreenrecycling.com/openapi.json
  - status: 404
    url: https://acegreenrecycling.com/.well-known/api-catalog
  - status: 404
    url: https://acegreenrecycling.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/acegreenrecycling
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: ACE Green Recycling, Inc. is a US-headquartered battery recycling technology company that develops and licenses electrified, hydrometallurgical processes for recovering critical materials from end-of-life lead-acid and lithium-ion batteries. Its proprietary GREENLEAD process produces battery-grade lead, and its LithiumFirst process recovers lithium carbonate, graphite, NMC and MHP precursors, cobalt, nickel and copper salts from LFP, NMC and LTO chemistries, all at zero Scope 1 emissions. ACE operates commercial lead and lithium plants in India and Taiwan, licenses its technology to existing recyclers internationally, and is building its own advanced recycling operations in the United States. The company announced a NASDAQ listing and $32M in PIPE funding in 2026. ACE is an industrial process and materials technology company; it publishes no public API, developer portal, SDK or machine-readable specification.
image: https://www.acegreenrecycling.com/wp-content/uploads/2022/10/cropped-acelogo.png
layout: provider
modified: '2026-09-06'
name: ACE Green Recycling
nav: Providers
network: true
overview: 'ACE Green Recycling is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Battery Recycling, Recycling, Circular Economy, and Critical Minerals.


  ACE Green Recycling''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ace Green Recycling Domain Security
  slug: ace-green-recycling-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: ace-green-recycling
tags:
- Company
- Battery Recycling
- Recycling
- Circular Economy
- Critical Minerals
- Lithium-Ion Batteries
- Lead-Acid Batteries
- Clean Technology
- Energy Storage
- Sustainability
website: https://www.acegreenrecycling.com/
---
