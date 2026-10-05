---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Thecoinanalysis Agentic Access
  operation_count: 4
  slug: thecoinanalysis-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: Public API for live crypto token prices.
  name: Public Price API
  slug: public-price-api
- baseURL: https://www.thecoinanalysis.com
  baseurl_source: spec
  description: The Public API API from The Coin Analysis — 4 operation(s) for public api.
  name: The Coin Analysis Public API
  slug: thecoinanalysis-public-api-api
artifact_total: 6
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thecoinanalysis/refs/heads/main/agentic-access/thecoinanalysis-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/thecoinanalysis-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thecoinanalysis/refs/heads/main/rules/thecoinanalysis-rules.yml
  title: ''
  type: Spectral
  url: rules/thecoinanalysis-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thecoinanalysis/refs/heads/main/errors/thecoinanalysis-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/thecoinanalysis-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thecoinanalysis/refs/heads/main/conformance/thecoinanalysis-conformance.yml
  title: ''
  type: Conformance
  url: conformance/thecoinanalysis-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thecoinanalysis/refs/heads/main/hosts/thecoinanalysis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thecoinanalysis-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thecoinanalysis.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thecoinanalysis.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.thecoinanalysis.com/prices
- group: company
  title: ''
  type: Newsroom
  url: https://www.thecoinanalysis.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thecoinanalysis/refs/heads/main/authentication/thecoinanalysis-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thecoinanalysis-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thecoinanalysis/refs/heads/main/security/thecoinanalysis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thecoinanalysis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.thecoinanalysis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.thecoinanalysis.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.thecoinanalysis.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.thecoinanalysis.com/developers
created: '2026-09-28'
description: The Coin Analysis provides real-time cryptocurrency news, market analysis, and price data through a REST API. It offers endpoints for current crypto prices, historical data, and news articles, secured with an API key. The service targets developers building financial, trading, or analytics applications.
image: https://www.thecoinanalysis.com/logo.png
layout: provider
modified: '2026-09-28'
name: The Coin Analysis
nav: Providers
network: true
overview: 'The Coin Analysis publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Public API, and 1 more. Tagged areas include Company, Crypto, News, and Data.


  The The Coin Analysis catalog on APIs.io includes 1 Spectral governance ruleset.


  The Coin Analysis'' developer surface includes pricing, authentication, documentation, API reference, getting-started guide, and 10 more developer resources.'
random_paper: 8
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: The Coin Analysis API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: thecoinanalysis-rules
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 31.5
    catalog_earned_first_party: 0.0
    catalog_gap: 83.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 44.1
    developer_ergonomics: 40.5
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Thecoinanalysis Authentication
  slug: thecoinanalysis-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Thecoinanalysis Domain Security
  slug: thecoinanalysis-domain-security
  summary_line: TLSv1.3 · DMARC
slug: thecoinanalysis
tags:
- Company
- Crypto
- News
- Data
website: https://www.thecoinanalysis.com/
---
