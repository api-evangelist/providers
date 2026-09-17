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
  scored_at: '2026-09-16'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://github.com/narratorai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/narratorai
coverage:
  checked: '2026-09-14'
  detail: Narrator is listed Inactive by Y Combinator and its narrator.ai domain now 301-redirects to narratordata.com, an unrelated WordPress poetry blog; api.narrator.ai and app.narrator.ai no longer resolve in DNS and docs.narrator.ai returns Cloudflare error 1014 from a dangling ReadMe CNAME, so there is no live surface left to profile.
  evidence:
  - status: 301
    url: https://narrator.ai/
  - status: 403
    url: https://docs.narrator.ai/openapi.json
  - status: 404
    url: https://portal.narrator.ai/openapi.json
  - status: 200
    url: https://www.ycombinator.com/companies/narrator
  - status: 200
    url: https://github.com/narratorai
  reason: defunct
  state: none
created: '2026-09-14'
description: Narrator was a New York data-intelligence company (Y Combinator S2019) that built an end-to-end analytics platform on top of the Activity Schema — a single time-series modeling approach it published as an alternative to star-schema warehouse modeling — covering warehouse transformations, dataset and narrative building, customer-journey analysis and scheduled materializations. The company raised roughly $7.6M and is listed by Y Combinator as Inactive; its narrator.ai domain now 301-redirects to an unrelated WordPress site, and its API, app and documentation hosts no longer resolve or serve. The only surviving first-party surface is the narratorai GitHub organization, where the full platform source (Hasura graph, the Mavis Python service, and the Next.js portal) was published under an MIT license in February 2025.
image: https://avatars.githubusercontent.com/u/35506833?v=4
layout: provider
modified: '2026-09-14'
name: Narrator
nav: Providers
network: true
overview: Narrator is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Data, Business Intelligence, and Data Warehouse.
random_paper: 19
score:
  band: minimal
  composite: 5.7
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
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 5.3
  previous_composite: 5.7
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: ainarrator
tags:
- Company
- Analytics
- Data
- Business Intelligence
- Data Warehouse
- Activity Schema
- Open-Source
---
