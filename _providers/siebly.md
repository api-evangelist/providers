---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Browse Siebly trading-system reference pages for glossary terms, execution modes, exchange state, runtime workflows, WebSocket behavior, and AI-agent guidance.
  name: Siebly Trading System API
  slug: siebly-trading-system-api
- description: 'Siebly API as documented publicly: 195 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Siebly API
  slug: siebly-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/siebly/rules/siebly-rules.yml
  title: ''
  type: Spectral
  url: rules/siebly-rules.yml
- group: design
  href: https://artifacts.apis.io/siebly/vocabulary/siebly-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/siebly-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/siebly/conformance/siebly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/siebly-conformance.yml
- group: agent
  href: https://artifacts.apis.io/siebly/llms/siebly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/siebly-llms.txt
- group: auth
  href: https://artifacts.apis.io/siebly/well-known/siebly-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/siebly-security.txt
- group: agent
  href: https://artifacts.apis.io/siebly/well-known/siebly-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/siebly-well-known.yml
- group: other
  href: https://artifacts.apis.io/siebly/hosts/siebly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/siebly-hosts.yml
- group: other
  href: https://artifacts.apis.io/siebly/vendors/siebly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/siebly-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://siebly.io/security
- group: build
  title: ''
  type: SDKs
  url: https://siebly.io/sdk
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sieblyio
- group: operate
  title: ''
  type: ChangeLog
  url: https://siebly.io/releases
- group: docs
  title: ''
  type: APIReference
  url: https://siebly.io/reference
- group: auth
  href: https://artifacts.apis.io/siebly/security/siebly-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/siebly-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/siebly/security/siebly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/siebly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://siebly.io
- group: docs
  title: ''
  type: Documentation
  url: https://siebly.io/sdk/binance/javascript
- group: operate
  title: ''
  type: Support
  url: https://siebly.io/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://siebly.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://siebly.io/privacy
- group: company
  title: ''
  type: Blog
  url: https://siebly.io/blog
coverage:
  checked: '2026-11-03'
  detail: Documentation is provided as markdown pages without a machine‑readable OpenAPI, GraphQL, or AsyncAPI spec.
  evidence:
  - status: 200
    url: https://siebly.io/reference.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Siebly provides JavaScript, Node.js, and TypeScript SDKs for major cryptocurrency exchanges such as Binance, Bybit, OKX, Gate, Bitget, KuCoin, Coinbase, Kraken, HTX, and Hyperliquid. The platform offers REST and WebSocket API integrations, comprehensive documentation, examples, and release notes, enabling developers to build trading applications quickly and securely.
image: https://siebly.io/wideLogoBannerSieblyLight2.png
layout: provider
modified: '2026-11-03'
name: Siebly
nav: Providers
network: true
overview: 'Siebly is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include SDK, Cryptocurrency, JavaScript, TypeScript, and Exchange.


  The Siebly catalog on APIs.io includes 1 Spectral governance ruleset.


  Siebly''s developer surface includes changelog, API reference, documentation, support, engineering blog, and 16 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 65
  extends:
  - spectral:oas
  name: Siebly API Rules
  rule_count: 24
  severity_counts:
    error: 19
    hint: 0
    info: 1
    warn: 4
  slug: siebly-rules
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 7.8
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 19.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Siebly Domain Security
  slug: siebly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Siebly Vulnerability Disclosure
  slug: siebly-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: siebly
tags:
- SDK
- Cryptocurrency
- JavaScript
- TypeScript
- Exchange
website: https://siebly.io
---
