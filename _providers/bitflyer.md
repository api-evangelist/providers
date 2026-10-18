---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-10-17'
api_count: 6
apis:
- baseURL: https://api.bitflyer.com/v1
  baseurl_source: declared
  description: The Account API from bitFlyer — 1 operation(s) for account.
  name: bitFlyer Account API
  slug: bitflyer-account-api
- baseURL: https://api.bitflyer.com/v1
  baseurl_source: declared
  description: The Assets API from bitFlyer — 3 operation(s) for assets.
  name: bitFlyer Assets API
  slug: bitflyer-assets-api
- baseURL: https://api.bitflyer.com/v1
  baseurl_source: declared
  description: The Chat API from bitFlyer — 1 operation(s) for chat.
  name: bitFlyer Chat API
  slug: bitflyer-chat-api
- baseURL: https://api.bitflyer.com/v1
  baseurl_source: declared
  description: The Deposits and Withdrawals API from bitFlyer — 7 operation(s) for deposits and withdrawals.
  name: bitFlyer Deposits and Withdrawals API
  slug: bitflyer-deposits-and-withdrawals-api
- baseURL: https://api.bitflyer.com/v1
  baseurl_source: declared
  description: The Markets API from bitFlyer — 9 operation(s) for markets.
  name: bitFlyer Markets API
  slug: bitflyer-markets-api
- baseURL: https://api.bitflyer.com/v1
  baseurl_source: declared
  description: The Trading API from bitFlyer — 13 operation(s) for trading.
  name: bitFlyer Trading API
  slug: bitflyer-trading-api
artifact_total: 10
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bitflyer/refs/heads/main/rules/bitflyer-rules.yml
  title: ''
  type: Spectral
  url: rules/bitflyer-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bitflyer/refs/heads/main/errors/bitflyer-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bitflyer-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bitflyer/refs/heads/main/conformance/bitflyer-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bitflyer-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitflyer/refs/heads/main/hosts/bitflyer-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitflyer-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitflyer/refs/heads/main/vendors/bitflyer-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitflyer-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitflyer/refs/heads/main/security/bitflyer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitflyer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bitflyer.com
- group: docs
  title: ''
  type: Documentation
  url: https://lightning.bitflyer.com/docs?lang=en
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bitflyer/refs/heads/main/rate-limits/bitflyer-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bitflyer-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitflyer/refs/heads/main/authentication/bitflyer-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bitflyer-authentication.yml
created: '2026-10-13'
description: bitFlyer is a Japanese cryptocurrency exchange. Its bitFlyer Lightning trading platform exposes a public and private HTTP API at api.bitflyer.com for market data, account assets, deposits and withdrawals, and order placement.
layout: provider
modified: '2026-10-13'
name: bitFlyer
nav: Providers
network: true
overview: 'bitFlyer is listed with 6 APIs on the [APIs.io](https://apis.io/) network, including Account API, Assets API, Chat API, and 3 more. Tagged areas include Company, Cryptocurrency, Exchange, Trading, and Japan.


  The bitFlyer catalog on APIs.io includes 1 Spectral governance ruleset.


  bitFlyer''s developer surface includes documentation, authentication, and 8 more developer resources.'
random_paper: 7
rate_limits:
- limit_count: 3
  name: Bitflyer Rate Limits
  slug: bitflyer-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: bitFlyer API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: bitflyer-rules
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 54.5
    catalog_earned_first_party: 12.0
    catalog_gap: 60.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 13.4
    developer_ergonomics: 21.4
    discoverability: 67.9
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Bitflyer Authentication
  slug: bitflyer-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bitflyer Domain Security
  slug: bitflyer-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bitflyer
tags:
- Company
- Cryptocurrency
- Exchange
- Trading
- Japan
website: https://bitflyer.com
---
