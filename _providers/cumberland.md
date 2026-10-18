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
- description: Electronic trading API for Cumberland institutional clients, listed as "API" on status.cumberland.io; reference documentation is behind a client login at apidocs.cumberland.io, so no contract is publi
  name: Cumberland CPE API
  slug: cumberland-cpe-api
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cumberland/refs/heads/main/well-known/cumberland-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cumberland-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cumberland/refs/heads/main/well-known/cumberland-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cumberland-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cumberland/refs/heads/main/hosts/cumberland-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cumberland-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cumberland/refs/heads/main/vendors/cumberland-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cumberland-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cumberland/refs/heads/main/security/cumberland-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cumberland-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cumberland.io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cumberland.io/
- group: company
  title: ''
  type: Newsroom
  url: https://www.cumberland.io/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cumberland.io/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cumberland.io/terms-and-conditions
- group: start
  title: ''
  type: Login
  url: https://apidocs.cumberland.io/login
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cumberland-drw/
- group: other
  title: ''
  type: X
  url: https://twitter.com/cumberlandsays
coverage:
  checked: '2026-10-14'
  detail: apidocs.cumberland.io redirects every path to a client login page (2,650-byte shell), so the CPE API reference and any contract are visible only to onboarded Cumberland counterparties.
  evidence:
  - status: 200
    url: https://apidocs.cumberland.io/
  - status: 200
    url: https://apidocs.cumberland.io/login
  - status: 200
    url: https://status.cumberland.io/
  reason: customer-only-docs
  state: gated
created: '2026-10-13'
description: Cumberland is the cryptocurrency trading and liquidity arm of DRW, providing institutional OTC spot, derivatives and options liquidity in digital assets. Clients trade through its electronic platforms, Marea and an API (named the Cumberland CPE API on its public status page); the API documentation at apidocs.cumberland.io sits behind a client login.
image: https://res.cloudinary.com/drw/image/upload/v1669155373/comm-cumberland/open-graph/cm-opengraph.png
layout: provider
modified: '2026-10-14'
name: Cumberland
nav: Providers
network: true
overview: Cumberland is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Trading, Liquidity, and OTC.
random_paper: 19
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 58.9
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 13.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cumberland Domain Security
  slug: cumberland-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cumberland
tags:
- Company
- Cryptocurrency
- Trading
- Liquidity
- OTC
- Digital Assets
- Financial Services
website: https://cumberland.io
---
