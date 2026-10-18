---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.5
  scored_at: '2026-10-17'
api_count: 9
apis:
- baseURL: https://api.equibles.com
  baseurl_source: declared
  description: The Equibles API API from Equibles — 1 operation(s) for equibles api.
  name: Equibles Equibles API
  slug: equibles-equibles-api-api
- baseURL: https://api.equibles.com
  baseurl_source: declared
  description: The Etfs API from Equibles — 2 operation(s) for etfs.
  name: Equibles Etfs API
  slug: equibles-etfs-api
- baseURL: https://api.equibles.com
  baseurl_source: declared
  description: The Fda API from Equibles — 1 operation(s) for fda.
  name: Equibles Fda API
  slug: equibles-fda-api
- baseURL: https://api.equibles.com
  baseurl_source: declared
  description: The Funds API from Equibles — 1 operation(s) for funds.
  name: Equibles Funds API
  slug: equibles-funds-api
- baseURL: https://api.equibles.com
  baseurl_source: declared
  description: The Investment Advisers API from Equibles — 1 operation(s) for investment advisers.
  name: Equibles Investment Advisers API
  slug: equibles-investment-advisers-api
- baseURL: https://api.equibles.com
  baseurl_source: declared
  description: The Ipos API from Equibles — 1 operation(s) for ipos.
  name: Equibles Ipos API
  slug: equibles-ipos-api
- baseURL: https://api.equibles.com
  baseurl_source: declared
  description: The Short Interest API from Equibles — 1 operation(s) for short interest.
  name: Equibles Short Interest API
  slug: equibles-short-interest-api
- baseURL: https://api.equibles.com
  baseurl_source: declared
  description: The Short Volume API from Equibles — 1 operation(s) for short volume.
  name: Equibles Short Volume API
  slug: equibles-short-volume-api
- baseURL: https://api.equibles.com
  baseurl_source: declared
  description: The Stocks API from Equibles — 3 operation(s) for stocks.
  name: Equibles Stocks API
  slug: equibles-stocks-api
artifact_total: 21
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/equibles/refs/heads/main/rate-limits/equibles-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/equibles-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/equibles/refs/heads/main/plans/equibles-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/equibles-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/equibles/refs/heads/main/rules/equibles-rules.yml
  title: ''
  type: Spectral
  url: rules/equibles-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/equibles/refs/heads/main/json-ld/equibles-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/equibles-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/equibles/refs/heads/main/vocabulary/equibles-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/equibles-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/equibles/refs/heads/main/data-model/equibles-data-model.yml
  title: ''
  type: DataModel
  url: data-model/equibles-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/equibles/refs/heads/main/changelog/equibles-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/equibles-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/equibles/refs/heads/main/conventions/equibles-conventions.yml
  title: ''
  type: Conventions
  url: conventions/equibles-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/equibles/refs/heads/main/authentication/equibles-authentication.yml
  title: ''
  type: Authentication
  url: authentication/equibles-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/equibles/refs/heads/main/conformance/equibles-conformance.yml
  title: ''
  type: Conformance
  url: conformance/equibles-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/equibles/refs/heads/main/llms/equibles-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/equibles-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/equibles/refs/heads/main/mcp/equibles-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/equibles-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/equibles/refs/heads/main/well-known/equibles-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/equibles-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/equibles/refs/heads/main/hosts/equibles-hosts.yml
  title: ''
  type: Hosts
  url: hosts/equibles-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/equibles/refs/heads/main/vendors/equibles-vendors.yml
  title: ''
  type: Vendors
  url: vendors/equibles-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://equibles.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://equibles.com/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://equibles.com/auth/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://equibles.com/docs/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://equibles.com/docs/api
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/equibles/refs/heads/main/security/equibles-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/equibles-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equibles.com
- group: docs
  title: ''
  type: Documentation
  url: https://equibles.com/docs
- group: company
  title: ''
  type: Blog
  url: https://equibles.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://equibles.com/pricing
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://equibles.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-05'
description: Equibles provides a platform for researching US stocks, offering access to SEC filings, earnings call transcripts, 13F holdings, insider and congressional trades, and AI-driven analysis via ALVIS. Users can query financial data through a REST API and integrate with AI assistants like ChatGPT, Claude, or Cursor. The service includes free starter access and comprehensive documentation for developers.
image: https://equibles.com/images/og-default.png
json_schemas:
- name: GetV1EtfsSpyHoldingsResponse
  property_count: 2
  slug: equibles-get-v1-etfs-spy-holdings-response
- name: GetV1EtfsSpyResponse
  property_count: 1
  slug: equibles-get-v1-etfs-spy-response
- name: GetV1IposIpoidResponse
  property_count: 16
  slug: equibles-get-v1-ipos-ipoid-response
- name: GetV1StocksAaplPricesResponse
  property_count: 2
  slug: equibles-get-v1-stocks-aapl-prices-response
- name: GetV1V1IdResponse
  property_count: 1
  slug: equibles-get-v1-v1-id-response
jsonld:
- class_count: 5
  name: Equibles Context
  property_count: 22
  slug: equibles-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.equibles.com.
  name: Equibles MCP Server
  slug: equibles-mcp-yml
modified: '2026-10-05'
name: Equibles
nav: Providers
network: true
overview: 'Equibles is listed with 9 APIs on the [APIs.io](https://apis.io/) network, including Equibles API, Etfs API, Fda API, and 6 more. Tagged areas include Company, Finance, Data, and Stocks.


  The Equibles catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Equibles'' developer surface includes changelog, authentication, API reference, documentation, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Equibles Plans Pricing
  plan_count: 2
  slug: equibles-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Equibles Rate Limits
  slug: equibles-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Equibles API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: equibles-rules
score:
  band: developing
  composite: 41.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 76.0
    catalog_earned_first_party: 16.0
    catalog_gap: 39.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 19.7
    contract_quality: 25.8
    developer_ergonomics: 31.0
    discoverability: 71.7
    operational_transparency: 36.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Equibles Authentication
  slug: equibles-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Equibles Domain Security
  slug: equibles-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: equibles
tags:
- Company
- Finance
- Data
- Stocks
website: https://equibles.com
---
