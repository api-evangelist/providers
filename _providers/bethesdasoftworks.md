---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.3
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API reference for Bethesda services as described on the Bethesda website.
  name: Bethesda API
  slug: bethesda-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bethesdasoftworks/refs/heads/main/llms/bethesdasoftworks-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bethesdasoftworks-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bethesdasoftworks/refs/heads/main/well-known/bethesdasoftworks-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bethesdasoftworks-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bethesdasoftworks/refs/heads/main/hosts/bethesdasoftworks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bethesdasoftworks-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bethesdasoftworks/refs/heads/main/vendors/bethesdasoftworks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bethesdasoftworks-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://bethesda.net/news
- group: docs
  title: ''
  type: Documentation
  url: https://help.bethesda.net/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bethesdasoftworks/refs/heads/main/security/bethesdasoftworks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bethesdasoftworks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bethesda.net
coverage:
  checked: '2026-09-28'
  detail: Bethesda provides API reference pages but no machine‑readable OpenAPI/GraphQL/AsyncAPI contract was discoverable.
  evidence:
  - status: 200
    url: https://api.bethesda.net/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Bethesda Softworks is an American video game publisher based in Rockville, Maryland, known for popular franchises such as The Elder Scrolls, Fallout, and Doom. Founded in 1986, the company develops and publishes games across multiple platforms, operating a digital storefront at bethesda.net and supporting a vibrant community of players worldwide.
layout: provider
modified: '2026-09-28'
name: Bethesdasoftworks
nav: Providers
network: true
overview: 'Bethesdasoftworks publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Video Games, Publishers, and Bethesda.


  Bethesdasoftworks'' developer surface includes documentation and 7 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bethesdasoftworks Domain Security
  slug: bethesdasoftworks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bethesdasoftworks
tags:
- Company
- Gaming
- Video Games
- Publishers
- Bethesda
website: https://bethesda.net
---
