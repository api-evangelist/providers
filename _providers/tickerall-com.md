---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 25
  human_in_the_loop: 7
  name: Tickerall Com Agentic Access
  operation_count: 44
  slug: tickerall-com-agentic-access
  summary_line: 44 operations · 25 acting · 7 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.tickerall.com
  baseurl_source: declared
  description: The Accounts API from tickerall-com — 8 operation(s) for accounts.
  name: tickerall-com Accounts API
  slug: tickerall-com-accounts-api
- baseURL: https://api.tickerall.com
  baseurl_source: declared
  description: The Bulk API from tickerall-com — 6 operation(s) for bulk.
  name: tickerall-com Bulk API
  slug: tickerall-com-bulk-api
- baseURL: https://api.tickerall.com
  baseurl_source: declared
  description: The Candles & History API from tickerall-com — 2 operation(s) for candles & history.
  name: tickerall-com Candles & History API
  slug: tickerall-com-candles-history-api
- baseURL: https://api.tickerall.com
  baseurl_source: declared
  description: The Copy Trading API from tickerall-com — 6 operation(s) for copy trading.
  name: tickerall-com Copy Trading API
  slug: tickerall-com-copy-trading-api
- baseURL: https://api.tickerall.com
  baseurl_source: declared
  description: The Orders API from tickerall-com — 5 operation(s) for orders.
  name: tickerall-com Orders API
  slug: tickerall-com-orders-api
- baseURL: https://api.tickerall.com
  baseurl_source: declared
  description: The Sessions API from tickerall-com — 2 operation(s) for sessions.
  name: tickerall-com Sessions API
  slug: tickerall-com-sessions-api
- baseURL: https://api.tickerall.com
  baseurl_source: declared
  description: The Symbols API from tickerall-com — 2 operation(s) for symbols.
  name: tickerall-com Symbols API
  slug: tickerall-com-symbols-api
- baseURL: https://api.tickerall.com
  baseurl_source: declared
  description: The Trade History API from tickerall-com — 4 operation(s) for trade history.
  name: tickerall-com Trade History API
  slug: tickerall-com-trade-history-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/tickerall-com/agentic-access/tickerall-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tickerall-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/tickerall-com/rules/tickerall-com-rules.yml
  title: ''
  type: Spectral
  url: rules/tickerall-com-rules.yml
- group: design
  href: https://artifacts.apis.io/tickerall-com/json-ld/tickerall-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tickerall-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/tickerall-com/vocabulary/tickerall-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tickerall-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/tickerall-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/tickerall-com/data-model/tickerall-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tickerall-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/tickerall-com/errors/tickerall-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tickerall-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tickerall-com/conformance/tickerall-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tickerall-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tickerall-com/llms/tickerall-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tickerall-com-llms.txt
- group: other
  href: https://artifacts.apis.io/tickerall-com/hosts/tickerall-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tickerall-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/tickerall-com/vendors/tickerall-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tickerall-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/tickerall-com/packages/tickerall-com-packages.yml
  title: ''
  type: Packages
  url: packages/tickerall-com-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://tickerall.com/status
- group: auth
  title: ''
  type: Security
  url: https://tickerall.com/security
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@tickerall/sdk
- group: start
  title: ''
  type: Login
  url: https://tickerall.com/sign-in
- group: auth
  href: https://artifacts.apis.io/tickerall-com/security/tickerall-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tickerall-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tickerall-com/security/tickerall-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tickerall-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tickerall.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tickerall.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://tickerall.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://tickerall.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://tickerall.com/download
- group: operate
  title: ''
  type: Support
  url: https://tickerall.com/contact
- group: company
  title: ''
  type: Blog
  url: https://tickerall.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tickerall
- group: commercial
  title: ''
  type: Pricing
  url: https://tickerall.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tickerall.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tickerall.com/privacy
created: '2026-10-31'
description: Ticker All! provides a hosted MT5 & MT4 broker API that enables developers to integrate trading functionality via REST and WebSocket. It offers real‑time market data, order placement, account management, and copy‑trading capabilities without requiring an EA bridge. The service includes free demo access, tiered pricing, comprehensive documentation, and SDKs for multiple languages, making algorithmic trading implementation straightforward and scalable.
image: https://tickerall.com/og-card.png
jsonld:
- class_count: 1
  name: Tickerall Com Context
  property_count: 1
  slug: tickerall-com-context
layout: provider
modified: '2026-10-31'
name: tickerall-com
nav: Providers
network: true
overview: 'tickerall-com publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Bulk API, Candles & History API, and 5 more. Tagged areas include Finance, Trading, Foreign Exchange, MT5, and MT4.


  The tickerall-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  tickerall-com''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 23 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: tickerall-com API Rules
  rule_count: 18
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 2
  slug: tickerall-com-rules
scopes:
- name: Tickerall Com Scopes
  scope_count: 0
  slug: tickerall-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.7
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 55.8
    developer_ergonomics: 31.5
    discoverability: 66.1
    operational_transparency: 15.8
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tickerall-com/tickerall-com-2026-11-03T144719.png
security:
- kind: authentication
  name: Tickerall Com Authentication
  slug: tickerall-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Tickerall Com Domain Security
  slug: tickerall-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tickerall Com Vulnerability Disclosure
  slug: tickerall-com-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 4
skills:
- name: connect-broker
  slug: tickerall-com-connect-broker
- name: copy-trading
  slug: tickerall-com-copy-trading
- name: manage-accounts
  slug: tickerall-com-manage-accounts
- name: place-order
  slug: tickerall-com-place-order
slug: tickerall-com
tags:
- Finance
- Trading
- Foreign Exchange
- MT5
- MT4
website: https://tickerall.com/
---
