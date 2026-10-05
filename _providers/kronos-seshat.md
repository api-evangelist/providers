---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 24.5
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Kronos Seshat Agentic Access
  operation_count: 32
  slug: kronos-seshat-agentic-access
  summary_line: 32 operations · 1 acting
api_count: 1
apis:
- baseURL: https://kronos.seshat.markets/api
  baseurl_source: declared
  description: The Agent API from Kronos Quant Signal API — 7 operation(s) for agent.
  name: Kronos Quant Signal API Agent API
  slug: kronos-seshat-agent-api
- baseURL: https://kronos.seshat.markets/api
  baseurl_source: declared
  description: The Agent Intelligence API from Kronos Quant Signal API — 2 operation(s) for agent intelligence.
  name: Kronos Quant Signal API Agent Intelligence API
  slug: kronos-seshat-agent-intelligence-api
- baseURL: https://kronos.seshat.markets/api
  baseurl_source: declared
  description: The Analysis API from Kronos Quant Signal API — 8 operation(s) for analysis.
  name: Kronos Quant Signal API Analysis API
  slug: kronos-seshat-analysis-api
- baseURL: https://kronos.seshat.markets/api
  baseurl_source: declared
  description: The Discovery API from Kronos Quant Signal API — 2 operation(s) for discovery.
  name: Kronos Quant Signal API Discovery API
  slug: kronos-seshat-discovery-api
- baseURL: https://kronos.seshat.markets/api
  baseurl_source: declared
  description: The Experimental API from Kronos Quant Signal API — 1 operation(s) for experimental.
  name: Kronos Quant Signal API Experimental API
  slug: kronos-seshat-experimental-api
- baseURL: https://kronos.seshat.markets/api
  baseurl_source: declared
  description: The Forecast API from Kronos Quant Signal API — 4 operation(s) for forecast.
  name: Kronos Quant Signal API Forecast API
  slug: kronos-seshat-forecast-api
- baseURL: https://kronos.seshat.markets/api
  baseurl_source: declared
  description: The Market Intelligence API from Kronos Quant Signal API — 2 operation(s) for market intelligence.
  name: Kronos Quant Signal API Market Intelligence API
  slug: kronos-seshat-market-intelligence-api
- baseURL: https://kronos.seshat.markets/api
  baseurl_source: declared
  description: The Semantic Similarity API from Kronos Quant Signal API — 2 operation(s) for semantic similarity.
  name: Kronos Quant Signal API Semantic Similarity API
  slug: kronos-seshat-semantic-similarity-api
- baseURL: https://kronos.seshat.markets/api
  baseurl_source: declared
  description: The Signal API from Kronos Quant Signal API — 1 operation(s) for signal.
  name: Kronos Quant Signal API Signal API
  slug: kronos-seshat-signal-api
- baseURL: https://kronos.seshat.markets/api
  baseurl_source: declared
  description: The Verification API from Kronos Quant Signal API — 3 operation(s) for verification.
  name: Kronos Quant Signal API Verification API
  slug: kronos-seshat-verification-api
artifact_total: 17
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kronos-seshat/refs/heads/main/agentic-access/kronos-seshat-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kronos-seshat-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kronos-seshat/refs/heads/main/rules/kronos-seshat-rules.yml
  title: ''
  type: Spectral
  url: rules/kronos-seshat-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kronos-seshat/refs/heads/main/json-ld/kronos-seshat-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kronos-seshat-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kronos-seshat/refs/heads/main/vocabulary/kronos-seshat-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kronos-seshat-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kronos-seshat/refs/heads/main/data-model/kronos-seshat-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kronos-seshat-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kronos-seshat/refs/heads/main/errors/kronos-seshat-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kronos-seshat-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kronos-seshat/refs/heads/main/conformance/kronos-seshat-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kronos-seshat-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kronos-seshat/refs/heads/main/llms/kronos-seshat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kronos-seshat-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kronos-seshat/refs/heads/main/a2a/kronos-seshat-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/kronos-seshat-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kronos-seshat/refs/heads/main/well-known/kronos-seshat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kronos-seshat-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kronos-seshat/refs/heads/main/hosts/kronos-seshat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kronos-seshat-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kronos-seshat/refs/heads/main/vendors/kronos-seshat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kronos-seshat-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://kronos.seshat.markets/security
- group: start
  title: ''
  type: Sandbox
  url: https://kronos.seshat.markets/api/playground
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kronos-seshat/refs/heads/main/authentication/kronos-seshat-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kronos-seshat-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kronos-seshat/refs/heads/main/security/kronos-seshat-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kronos-seshat-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kronos-seshat/refs/heads/main/security/kronos-seshat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kronos-seshat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kronos.seshat.markets/
- group: docs
  title: ''
  type: Documentation
  url: https://kronos.seshat.markets/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://kronos.seshat.markets/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kronos.seshat.markets/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kronos.seshat.markets/privacy.html
- group: operate
  title: ''
  type: Support
  url: https://kronos.seshat.markets/contact.html
created: '2026-09-25'
description: Kronos Quant Signal API provides crypto, commodity, and pre‑market equity financial forecast signals via a RESTful API. It delivers multi‑timeframe OHLCV‑based predictions, audited model decisions, and risk metrics. Users can access live and delayed forecasts, risk assessments, and historical accuracy data, enabling quantitative analysis and strategy development across digital and traditional assets.
image: https://kronos.seshat.markets/assets/og-kronos.webp
json_schemas:
- name: KronosForecastResponse
  property_count: 7
  slug: kronos-seshat-kronos-forecast-response
jsonld:
- class_count: 7
  name: Kronos Seshat Context
  property_count: 32
  slug: kronos-seshat-context
layout: provider
modified: '2026-09-25'
name: Kronos Quant Signal API
nav: Providers
network: true
overview: 'Kronos Quant Signal API publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Agent API, Agent Intelligence API, Analysis API, and 7 more. Tagged areas include Crypto, Financial Forecast, Market Data, Auditing, and Micropayments.


  The Kronos Quant Signal API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Kronos Quant Signal API''s developer surface includes sandbox, authentication, documentation, pricing, support, and 18 more developer resources.'
random_paper: 19
rules:
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Kronos Quant Signal API API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: kronos-seshat-rules
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 59.2
    catalog_earned_first_party: 0.0
    catalog_gap: 55.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 57.2
    developer_ergonomics: 33.3
    discoverability: 73.2
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Kronos Seshat Authentication
  slug: kronos-seshat-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Kronos Seshat Domain Security
  slug: kronos-seshat-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kronos Seshat Vulnerability Disclosure
  slug: kronos-seshat-vulnerability-disclosure
  summary_line: disclosure policy published
slug: kronos-seshat
tags:
- Crypto
- Financial Forecast
- Market Data
- Auditing
- Micropayments
website: https://kronos.seshat.markets/
---
