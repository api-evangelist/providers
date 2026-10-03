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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bestex-research/refs/heads/main/hosts/bestex-research-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bestex-research-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bestex-research/refs/heads/main/vendors/bestex-research-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bestex-research-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.bestexresearch.com/news/introducing-bestex-research
- group: start
  title: ''
  type: Login
  url: https://www.bestexresearch.com/sign-in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bestexresearch
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bestex-research/refs/heads/main/security/bestex-research-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bestex-research-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bestexresearch.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bestexresearch.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bestexresearch.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.bestexresearch.com/contact-us
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bestexresearch.com/schedule-a-demo
coverage:
  checked: '2026-09-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found despite probing API host and docs.
  evidence:
  - status: 0
    url: https://api.bestexresearch.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: BestEx Research provides independent, research-driven execution algorithms, trading technology, and trade analytics built on rigorous market microstructure research across equities and futures. Serving asset managers, hedge funds, banks, and brokers, it offers end‑to‑end global execution platforms and AI‑powered market impact models to optimize execution costs and improve trading performance.
image: https://cdn.prod.website-files.com/63c8555b3d6b34a2c0620e39/63fe708e9a8ee16724148e17_home-featured-image.webp
layout: provider
modified: '2026-09-27'
name: BestEx Research
nav: Providers
network: true
overview: 'BestEx Research is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Trading, Algorithms, Analytics, and Research.


  BestEx Research''s developer surface includes support, getting-started guide, and 9 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 13.0
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bestex Research Domain Security
  slug: bestex-research-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bestex-research
tags:
- Finance
- Trading
- Algorithms
- Analytics
- Research
website: https://www.bestexresearch.com
---
