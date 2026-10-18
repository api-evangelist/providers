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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ctristack/refs/heads/main/llms/ctristack-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ctristack-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ctristack/refs/heads/main/well-known/ctristack-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ctristack-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ctristack/refs/heads/main/hosts/ctristack-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ctristack-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ctristack/refs/heads/main/vendors/ctristack-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ctristack-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://augment.market/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://augment.market/privacy
- group: other
  title: ''
  type: Leadership
  url: https://augment.market/team
- group: docs
  title: ''
  type: Documentation
  url: https://dev.augment.market/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ctristack/refs/heads/main/security/ctristack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ctristack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://augment.market/c/ctristack
coverage:
  checked: '2026-10-11'
  detail: Login page at docs.augment.market renders JavaScript and provides no machine‑readable spec.
  evidence:
  - status: 200
    url: https://docs.augment.market/login?redirect=%2F
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-11'
description: Ctristack is a private liquidity network platform that facilitates the buying and selling of private company shares. It aggregates market activity, trade sizes, and provides tools for investors to gain exposure to private companies without direct ownership. The service offers detailed company rankings, pulse updates on market trends, and integrates with various financial data sources to deliver actionable insights for both institutional and accredited investors.
layout: provider
modified: '2026-10-11'
name: Ctristack
nav: Providers
network: true
overview: 'Ctristack is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, PrivateLiquidity, Market Data, Investor, and TradingPlatform.


  Ctristack''s developer surface includes documentation and 9 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 11.2
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
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 18.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ctristack Domain Security
  slug: ctristack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ctristack
tags:
- Company
- PrivateLiquidity
- Market Data
- Investor
- TradingPlatform
website: https://augment.market/c/ctristack
---
