---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: API for OneWeb satellite broadband services.
  name: OneWeb API
  slug: oneweb-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/oneweb/refs/heads/main/llms/oneweb-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/oneweb-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/oneweb/refs/heads/main/well-known/oneweb-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/oneweb-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/oneweb/refs/heads/main/hosts/oneweb-hosts.yml
  title: ''
  type: Hosts
  url: hosts/oneweb-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/oneweb/refs/heads/main/vendors/oneweb-vendors.yml
  title: ''
  type: Vendors
  url: vendors/oneweb-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.eutelsat.com/satellite-services/government/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eutelsat.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.eutelsat.com/media-press/media-centre/news/a1-group-renews-cee-dth-capacity-eutelsat-16deg-east
- group: docs
  title: ''
  type: Documentation
  url: https://developer.oneweb.net/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/oneweb/refs/heads/main/security/oneweb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oneweb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oneweb.net/
coverage:
  checked: 2026-09-23
  detail: Developer portal at https://eu1.anypoint.mulesoft.com/exchange/portals/oneweb/ renders JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 401
    url: https://api.oneweb.net/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-23'
description: OneWeb, now part of Eutelsat, is a global communications company operating a low Earth orbit satellite constellation to provide broadband internet services worldwide. Founded in 2012, it aims to deliver high‑speed connectivity to underserved regions, enterprises, and maritime and aviation sectors.
image: https://www.eutelsat.com/sites/default/files/2026-08/Composite-Images-20260803-124639.png
layout: provider
modified: '2026-09-23'
name: OneWeb
nav: Providers
network: true
overview: 'OneWeb publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Satellite, Broadband, LEO, and Telecommunications.


  OneWeb''s developer surface includes documentation and 9 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 66.7
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 22.2
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Oneweb Domain Security
  slug: oneweb-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: oneweb
tags:
- Company
- Satellite
- Broadband
- LEO
- Telecommunications
website: https://oneweb.net/
---
