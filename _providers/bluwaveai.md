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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bluwaveai/refs/heads/main/hosts/bluwaveai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bluwaveai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bluwaveai/refs/heads/main/vendors/bluwaveai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bluwaveai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bluwave-ai.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://help.bluwave-ai.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.bluwave-ai.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.bluwave-ai.com/team
- group: company
  title: ''
  type: Blog
  url: https://www.bluwave-ai.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.bluwave-ai.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bluwaveai/refs/heads/main/security/bluwaveai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bluwaveai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bluwave-ai.com
coverage:
  checked: '2026-09-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on the API or docs hosts.
  evidence:
  - status: 404
    url: https://help.bluwave-ai.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-29'
description: BluWave-ai, founded in Ottawa, Canada in 2017, provides artificial intelligence SaaS platforms that help utilities, data centers, independent power producers, enterprises and fleet operators optimize renewable energy, storage and electric transportation assets, accelerating the global energy transition and reducing emissions.
image: https://img.pagecloud.com/ohHXppVgpSV4xIYSQVNEB_AJHj8=/1300x0/filters:no_upscale()/bluwave-ai/Wind_turbines_California_Photo_by_Cameron_Venti_on_Unsplash_med-q178f.jpg
layout: provider
modified: '2026-09-29'
name: Bluwaveai
nav: Providers
network: true
overview: 'Bluwaveai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Clean Energy, Smart Grid, Energy Storage, and Data Center.


  Bluwaveai''s developer surface includes engineering blog, documentation, and 8 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 10.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bluwaveai Domain Security
  slug: bluwaveai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bluwaveai
tags:
- Artificial Intelligence
- Clean Energy
- Smart Grid
- Energy Storage
- Data Center
- Electric Vehicles
- Utilities
website: https://www.bluwave-ai.com
---
