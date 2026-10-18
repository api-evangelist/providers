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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for CarChain platform enabling vehicle ownership and ride‑hailing operations. Documentation is limited to a prototype page without machine‑readable specs.
  name: CarChain API
  slug: carchain-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carchain93c1/refs/heads/main/hosts/carchain93c1-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carchain93c1-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/carchainnet
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carchain93c1/refs/heads/main/security/carchain93c1-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carchain93c1-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carchainnet.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.carchainnet.com/prototype.html
- group: company
  title: ''
  type: Blog
  url: https://blog.carchainnet.ir
coverage:
  checked: '2026-10-07'
  detail: Prototype documentation page is a JavaScript‑rendered SPA with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://www.carchainnet.com/prototype.html
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Carchain93c1 is a blockchain-based platform that aims to facilitate the buying, selling, and sharing of cars. It proposes a decentralized ride‑hailing ecosystem where transactions are recorded on a distributed ledger, offering transparency, smart‑contract‑driven agreements, and scalable server infrastructure. The service targets both individual users and fleet operators, promising collaborative benefits and secure, immutable records of vehicle ownership and usage.
layout: provider
modified: '2026-10-07'
name: Carchain93c1
nav: Providers
network: true
overview: 'Carchain93c1 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Ride‑hailing, Blockchain, Tokens, ICO, and Payments.


  Carchain93c1''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 5.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carchain93C1 Domain Security
  slug: carchain93c1-domain-security
  summary_line: TLSv1.3
slug: carchain93c1
tags:
- Ride‑hailing
- Blockchain
- Tokens
- ICO
- Payments
- Decentralized
website: https://www.carchainnet.com
---
