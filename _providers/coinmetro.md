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
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coinmetro/refs/heads/main/well-known/coinmetro-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coinmetro-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coinmetro/refs/heads/main/well-known/coinmetro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coinmetro-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coinmetro/refs/heads/main/hosts/coinmetro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coinmetro-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coinmetro/refs/heads/main/vendors/coinmetro-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coinmetro-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/coinmetro/refs/heads/main/packages/coinmetro-packages.yml
  title: ''
  type: SDKs
  url: packages/coinmetro-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/coinmetro/refs/heads/main/packages/coinmetro-packages.yml
  title: ''
  type: Packages
  url: packages/coinmetro-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coinmetro.com/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coinmetro.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coinmetro.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://coinmetro.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CoinMetro
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coinmetro/refs/heads/main/security/coinmetro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinmetro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coinmetro.com
coverage:
  checked: '2026-10-09'
  detail: All attempts to fetch OpenAPI specs at api.coinmetro.com returned 404.
  evidence:
  - status: 404
    url: https://api.coinmetro.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: Coinmetro is a regulated cryptocurrency exchange platform that offers secure buying, selling, and trading of digital assets. It provides a user-friendly interface, advanced trading tools, loyalty programs, and 24/7 support, aiming to make crypto accessible and trustworthy for both beginners and experienced traders.
image: https://images.prismic.io/coinmetro-website/426163f6-9a64-46d7-ac5e-42abd05e1e2a_default.png?auto=format,compress
layout: provider
modified: '2026-10-09'
name: Coinmetro
nav: Providers
network: true
overview: 'Coinmetro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Spot Trading, Margin Trading, Staking, and Auto Invest.


  Coinmetro''s developer surface includes engineering blog and 12 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 39.3
    operational_transparency: 21.1
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
  name: Coinmetro Domain Security
  slug: coinmetro-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: coinmetro
tags:
- Spot Trading
- Margin Trading
- Staking
- Auto Invest
website: https://www.coinmetro.com
---
