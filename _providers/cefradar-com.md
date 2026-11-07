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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cefradar Com Agentic Access
  operation_count: 14
  slug: cefradar-com-agentic-access
  summary_line: 14 operations
api_count: 1
apis:
- baseURL: https://cefradar.com
  baseurl_source: declared
  description: Your own key's plan and budget (the only call that needs a key).
  name: CEF Radar Account API
  slug: cefradar-com-account-api
- baseURL: https://cefradar.com
  baseurl_source: declared
  description: Dated announcements a holder may need to act on, with the date to act by.
  name: CEF Radar Events API
  slug: cefradar-com-events-api
- baseURL: https://cefradar.com
  baseurl_source: declared
  description: 'U.S. closed-end funds: the list, one fund, its facts, holdings and announcements.'
  name: CEF Radar Funds API
  slug: cefradar-com-funds-api
- baseURL: https://cefradar.com
  baseurl_source: declared
  description: The large investors who file notices about owning 5% or more of a fund, and those notices.
  name: CEF Radar Investors API
  slug: cefradar-com-investors-api
- baseURL: https://cefradar.com
  baseurl_source: declared
  description: Search-box suggestions and 'which funds hold X'.
  name: CEF Radar Search API
  slug: cefradar-com-search-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/cefradar-com/agentic-access/cefradar-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cefradar-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/cefradar-com/rules/cefradar-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cefradar-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cefradar-com/json-ld/cefradar-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cefradar-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cefradar-com/vocabulary/cefradar-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cefradar-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cefradar-com/data-model/cefradar-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cefradar-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/cefradar-com/errors/cefradar-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cefradar-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cefradar-com/conformance/cefradar-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cefradar-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cefradar-com/llms/cefradar-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cefradar-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cefradar-com/mcp/cefradar-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cefradar-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cefradar-com/well-known/cefradar-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cefradar-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cefradar-com/hosts/cefradar-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cefradar-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cefradar-com/vendors/cefradar-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cefradar-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cefradar.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cefradar.com/privacy
- group: auth
  href: https://artifacts.apis.io/cefradar-com/security/cefradar-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cefradar-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cefradar.com/
created: '2026-11-04'
description: CEF Radar provides plain‑words analysis of closed‑end fund activity. Users can enter a fund ticker or name to see if large investors are pushing for changes, whether the fund has announced buy‑backs, votes, or closures, and get explanations of filings. The service offers guides on tender offers, proxy votes, activist investors, return of capital, expense ratios, leverage, liquidations, mergers, and term funds, all illustrated with live SEC filing examples.
image: https://cefradar.com/static/og/default.png?v=1789691814
jsonld:
- class_count: 2
  name: Cefradar Com Context
  property_count: 6
  slug: cefradar-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at cefradar.com.
  name: CEF Radar MCP Server
  slug: cefradar-com-mcp-yml
modified: '2026-11-04'
name: CEF Radar
nav: Providers
network: true
overview: 'CEF Radar publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Events API, Funds API, and 2 more. Tagged areas include Closed‑end funds, SEC Filings, Investor alerts, Fund activity, and Buybacks.


  The CEF Radar catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: CEF Radar API Rules
  rule_count: 55
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 2
  slug: cefradar-com-rules
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 47.9
    developer_ergonomics: 0.0
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
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
  name: Cefradar Com Domain Security
  slug: cefradar-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cefradar-com
tags:
- Closed‑end funds
- SEC Filings
- Investor alerts
- Fund activity
- Buybacks
website: https://cefradar.com/
---
