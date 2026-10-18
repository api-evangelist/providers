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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/path/refs/heads/main/hosts/path-hosts.yml
  title: ''
  type: Hosts
  url: hosts/path-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/path/refs/heads/main/vendors/path-vendors.yml
  title: ''
  type: Vendors
  url: vendors/path-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pathcrypto.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pathcrypto.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.pathcrypto.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/path/refs/heads/main/security/path-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/path-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pathcrypto.com
- group: other
  title: ''
  type: Image
  url: https://cdn.prod.website-files.com/62a0c3db69e9f31272bb38a0/632a5c2ad7c654f6c4be73ab_Path-256x256.jpg
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.pathcrypto.com
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Path Crypto is an SEC‑registered financial advisory firm offering crypto investing and portfolio management services. It provides managed crypto portfolios, a self‑directed wallet, and institutional solutions, guiding clients through regulated cryptocurrency investment strategies.
layout: provider
modified: '2026-10-12'
name: Path
nav: Providers
network: true
overview: 'Path is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency, Financial Services, Investment, Portfolio Management, and SEC Registered.


  Path''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Path Domain Security
  slug: path-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: path
tags:
- Cryptocurrency
- Financial Services
- Investment
- Portfolio Management
- SEC Registered
website: https://www.pathcrypto.com
---
