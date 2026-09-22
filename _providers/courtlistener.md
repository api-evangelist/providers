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
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-09-21'
api_count: 1
apis:
- description: API for CourtListener legal data access
  name: CourtListener API
  slug: courtlistener-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/courtlistener/refs/heads/main/well-known/courtlistener-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/courtlistener-well-known.yml
- group: operate
  title: ''
  type: Support
  url: https://www.courtlistener.com/help/
- group: start
  title: ''
  type: Login
  url: https://www.courtlistener.com/sign-in/?next=/?
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/courtlistener/refs/heads/main/security/courtlistener-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/courtlistener-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.courtlistener.com/
coverage:
  checked: 2026-09-21
  detail: Documentation pages return HTML shells and no machine‑readable OpenAPI spec is available.
  evidence:
  - status: 0
    url: https://api.courtlistener.com/openapi.json
  - status: 403
    url: https://www.courtlistener.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-21'
description: Free Law Project is a nonprofit organization that provides free access to legal information and tools. It operates CourtListener, a comprehensive searchable database of United States court opinions, oral arguments, and other legal documents, along with related services such as RECAP and Bots.law. The platform aims to make the legal ecosystem more equitable and competitive by leveraging technology and open data.
image: https://storage.courtlistener.com/static/png/og-image-1200x630.7f25387a570b.png
layout: provider
modified: '2026-09-21'
name: CourtListener
nav: Providers
network: true
overview: 'CourtListener publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Legal, Non-Profit, Open Data, CourtListener, and FreeLaw.


  CourtListener''s developer surface includes support and 4 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 3
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 59.3
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Courtlistener Domain Security
  slug: courtlistener-domain-security
  summary_line: TLSv1.3 · DMARC
slug: courtlistener
tags:
- Legal
- Non-Profit
- Open Data
- CourtListener
- FreeLaw
website: https://www.courtlistener.com/
---
