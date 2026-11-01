---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 17
  human_in_the_loop: 2
  name: Snaptrade Agentic Access
  operation_count: 42
  slug: snaptrade-agentic-access
  summary_line: 42 operations · 17 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.snaptrade.com
  baseurl_source: declared
  description: Retrieve account information, such as positions, balances, etc.
  name: SnapTrade Account Information API
  slug: snaptrade-account-information-api
- baseURL: https://api.snaptrade.com
  baseurl_source: declared
  description: Check whether the API is operational and verify timestamps.
  name: SnapTrade API Status API
  slug: snaptrade-api-status-api
- baseURL: https://api.snaptrade.com
  baseurl_source: declared
  description: Register and authenticate users with SnapTrade.
  name: SnapTrade Authentication API
  slug: snaptrade-authentication-api
- baseURL: https://api.snaptrade.com
  baseurl_source: declared
  description: Retrieve and manage user connections.
  name: SnapTrade Connections API
  slug: snaptrade-connections-api
- baseURL: https://api.snaptrade.com
  baseurl_source: declared
  description: Retrieve usage information about your SnapTrade Client ID.
  name: SnapTrade Management API
  slug: snaptrade-management-api
- baseURL: https://api.snaptrade.com
  baseurl_source: declared
  description: Retrieve basic information for API use, such as supported brokerages, exchanges, currencies, etc.
  name: SnapTrade Reference Data API
  slug: snaptrade-reference-data-api
- baseURL: https://api.snaptrade.com
  baseurl_source: declared
  description: Manage orders on user accounts.
  name: SnapTrade Trading API
  slug: snaptrade-trading-api
artifact_total: 28
asyncapis:
- description: ''
  name: Snaptrade Webhooks
  slug: snaptrade-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/snaptrade/agentic-access/snaptrade-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/snaptrade-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/snaptrade/rate-limits/snaptrade-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/snaptrade-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/snaptrade/plans/snaptrade-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/snaptrade-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/snaptrade/rules/snaptrade-rules.yml
  title: ''
  type: Spectral
  url: rules/snaptrade-rules.yml
- group: design
  href: https://artifacts.apis.io/snaptrade/json-ld/snaptrade-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/snaptrade-context.jsonld
- group: design
  href: https://artifacts.apis.io/snaptrade/vocabulary/snaptrade-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/snaptrade-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/snaptrade/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/snaptrade/asyncapi/snaptrade-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/snaptrade-webhooks.yml
- group: design
  href: https://artifacts.apis.io/snaptrade/data-model/snaptrade-data-model.yml
  title: ''
  type: DataModel
  url: data-model/snaptrade-data-model.yml
- group: build
  href: https://artifacts.apis.io/snaptrade/cli/snaptrade-cli.yml
  title: ''
  type: CLI
  url: cli/snaptrade-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.snaptrade.com/
- group: auth
  href: https://artifacts.apis.io/snaptrade/authentication/snaptrade-authentication.yml
  title: ''
  type: Authentication
  url: authentication/snaptrade-authentication.yml
- group: design
  href: https://artifacts.apis.io/snaptrade/errors/snaptrade-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/snaptrade-problem-types.yml
- group: design
  href: https://artifacts.apis.io/snaptrade/conformance/snaptrade-conformance.yml
  title: ''
  type: Conformance
  url: conformance/snaptrade-conformance.yml
- group: agent
  href: https://artifacts.apis.io/snaptrade/llms/snaptrade-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/snaptrade-llms.txt
- group: auth
  href: https://artifacts.apis.io/snaptrade/well-known/snaptrade-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/snaptrade-support-security.txt
- group: agent
  href: https://artifacts.apis.io/snaptrade/well-known/snaptrade-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/snaptrade-well-known.yml
- group: other
  href: https://artifacts.apis.io/snaptrade/hosts/snaptrade-hosts.yml
  title: ''
  type: Hosts
  url: hosts/snaptrade-hosts.yml
- group: other
  href: https://artifacts.apis.io/snaptrade/vendors/snaptrade-vendors.yml
  title: ''
  type: Vendors
  url: vendors/snaptrade-vendors.yml
- group: build
  href: https://artifacts.apis.io/snaptrade/packages/snaptrade-packages.yml
  title: ''
  type: SDKs
  url: packages/snaptrade-packages.yml
- group: build
  href: https://artifacts.apis.io/snaptrade/packages/snaptrade-packages.yml
  title: ''
  type: Packages
  url: packages/snaptrade-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://snaptrade.com/terms-and-conditions
- group: auth
  title: ''
  type: Security
  url: https://snaptrade.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://snaptrade.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://snaptrade.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://snaptrade.com/press
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.snaptrade.com/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.snaptrade.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.snaptrade.com/reference/API%20Status/ApiStatus_check
- group: auth
  href: https://artifacts.apis.io/snaptrade/security/snaptrade-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/snaptrade-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/snaptrade/security/snaptrade-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/snaptrade-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/snaptrade/security/snaptrade-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/snaptrade-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://snaptrade.com/
created: '2026-10-21'
description: SnapTrade provides a unified API platform that enables developers and financial institutions to integrate brokerage services, account aggregation, and trading functionalities into their applications. The service offers real-time market data, order execution, portfolio management, and compliance tools, supporting multiple asset classes and broker integrations. SnapTrade aims to simplify the complexities of financial APIs, delivering secure, scalable, and well-documented endpoints for building fintech solutions.
image: https://snaptrade.com/brand/snaptrade-brand-og.png
json_schemas:
- name: AccountOrderRecord
  property_count: 25
  slug: snaptrade-account-order-record
- name: BrokerageAuthorization
  property_count: 11
  slug: snaptrade-brokerage-authorization
- name: ConnectedAssetPartnerStats
  property_count: 14
  slug: snaptrade-connected-asset-partner-stats
- name: encryptedResponse
  property_count: 2
  slug: snaptrade-encrypted-response
- name: PartnerStats
  property_count: 14
  slug: snaptrade-partner-stats
- name: UniversalSymbol
  property_count: 10
  slug: snaptrade-universal-symbol
jsonld:
- class_count: 120
  name: Snaptrade Context
  property_count: 266
  slug: snaptrade-context
layout: provider
modified: '2026-10-21'
name: SnapTrade
nav: Providers
network: true
overview: 'SnapTrade publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Information API, API Status API, Authentication API, and 4 more. Tagged areas include Company, Fintech, Brokerage, and Trading.


  The SnapTrade catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  SnapTrade''s developer surface includes CLI, authentication, pricing, getting-started guide, documentation, API reference, and 27 more developer resources.'
plans:
- name: Snaptrade Plans Pricing
  plan_count: 2
  slug: snaptrade-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Snaptrade Rate Limits
  slug: snaptrade-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: SnapTrade API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 2
    warn: 1
  slug: snaptrade-rules
score:
  band: strong
  composite: 58.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 73.8
    catalog_earned_first_party: 16.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 22.0
    contract_quality: 70.1
    developer_ergonomics: 56.5
    discoverability: 58.9
    operational_transparency: 39.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Snaptrade Authentication
  slug: snaptrade-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Snaptrade Domain Security
  slug: snaptrade-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Snaptrade Vulnerability Disclosure
  slug: snaptrade-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Snaptrade Trust Center
  slug: snaptrade-trust-center
  summary_line: SOC 2
skill_count: 5
skills:
- name: snaptrade-account-overview
  slug: snaptrade-account-overview
- name: snaptrade-manage-users
  slug: snaptrade-manage-users
- name: snaptrade-place-equity-order
  slug: snaptrade-place-equity-order
- name: snaptrade-reference-data-symbol-search
  slug: snaptrade-reference-data-symbol-search
- name: snaptrade-sync-connection
  slug: snaptrade-sync-connection
slug: snaptrade
tags:
- Company
- Fintech
- Brokerage
- Trading
website: https://snaptrade.com/
---
