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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://www.nordnet.se/security-disclosure
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nordnet/refs/heads/main/llms/nordnet-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nordnet-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nordnet/refs/heads/main/well-known/nordnet-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nordnet-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nordnet/refs/heads/main/well-known/nordnet-nordnet-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nordnet-nordnet-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nordnet/refs/heads/main/well-known/nordnet-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nordnet-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nordnet/refs/heads/main/hosts/nordnet-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nordnet-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/nordnet/refs/heads/main/packages/nordnet-packages.yml
  title: ''
  type: SDKs
  url: packages/nordnet-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/nordnet/refs/heads/main/packages/nordnet-packages.yml
  title: ''
  type: Packages
  url: packages/nordnet-packages.yml
- group: start
  title: ''
  type: Login
  url: https://www.nordnet.se/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nordnet/refs/heads/main/security/nordnet-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/nordnet-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nordnet/refs/heads/main/security/nordnet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nordnet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nordnet.se/
- group: other
  title: ''
  type: Image
  url: https://www.nordnet.se/favicon.ico
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://nordnet.se/
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: Nordnet is a leading digital brokerage and wealth management platform based in Sweden, offering a wide range of financial services including stock trading, mutual funds, ETFs, bonds, and private market investments. The platform provides intuitive tools for both private investors and professional traders, with features such as real‑time market data, portfolio analytics, and automated savings plans. Nordnet emphasizes low fees, transparent pricing, and a user‑friendly experience across web and mobile applications, serving millions of customers across the Nordics.
image: https://www.nordnet.se/static/images/nordnet-og-image.png
layout: provider
modified: '2026-10-14'
name: Nordnet
nav: Providers
network: true
overview: Nordnet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Brokerage, WealthManagement, Sweden, and Nordic.
random_paper: 14
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 55.4
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Nordnet Domain Security
  slug: nordnet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nordnet Vulnerability Disclosure
  slug: nordnet-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: nordnet
tags:
- Finance
- Brokerage
- WealthManagement
- Sweden
- Nordic
website: https://www.nordnet.se/
---
