---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Confluence Pro MCP for Claude, ChatGPT, and Cursor, providing AI agent integration via an MCP endpoint.
  name: Confluence Pro MCP
  slug: confluence-pro-mcp
- description: '0DTE Confluence API as documented publicly: 51 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: 0DTE Confluence API
  slug: 0dteconfluence-com-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/0dteconfluence-com/rules/0dteconfluence-com-rules.yml
  title: ''
  type: Spectral
  url: rules/0dteconfluence-com-rules.yml
- group: design
  href: https://artifacts.apis.io/0dteconfluence-com/vocabulary/0dteconfluence-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/0dteconfluence-com-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/0dteconfluence-com/authentication/0dteconfluence-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/0dteconfluence-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/0dteconfluence-com/conformance/0dteconfluence-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/0dteconfluence-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/0dteconfluence-com/llms/0dteconfluence-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/0dteconfluence-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/0dteconfluence-com/mcp/0dteconfluence-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/0dteconfluence-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/0dteconfluence-com/hosts/0dteconfluence-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/0dteconfluence-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/0dteconfluence-com/vendors/0dteconfluence-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/0dteconfluence-com-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://0dteconfluence.com/developers/mcp
- group: auth
  href: https://artifacts.apis.io/0dteconfluence-com/security/0dteconfluence-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/0dteconfluence-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://0dteconfluence.com/
- group: docs
  title: ''
  type: Documentation
  url: https://0dteconfluence.com/learn/
- group: start
  title: ''
  type: GettingStarted
  url: https://0dteconfluence.com/how-it-works
- group: operate
  title: ''
  type: Support
  url: https://0dteconfluence.com/contact
- group: company
  title: ''
  type: Blog
  url: https://0dteconfluence.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://0dteconfluence.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://0dteconfluence.com/privacy
coverage:
  checked: '2026-10-31'
  detail: API endpoint https://api.0dteconfluence.com/openapi.json returns 401 Unauthorized, indicating the spec is behind authentication.
  evidence:
  - status: 401
    url: https://api.0dteconfluence.com/openapi.json
  reason: auth-required
  state: gated
created: '2026-10-31'
description: 0DTE Confluence provides live 0‑day‑to‑expiration (0DTE) options dealer walls, classified flow, and graded A+/B setups with invalidation for major equity indices such as SPY, QQQ, IWM, SMH, and GLD. The platform offers a Decision Desk that displays live dealer walls, expected‑move bands, and a tape of market activity, along with quantitative tools like the Confluence Tape, GEX map, and exposure metrics. Users can subscribe to Desk Bundle ($159/mo) or Pro MCP ($199/mo) for advanced alerts, quant tools, and session updates. Educational guides are available in the Learn Hub, covering what 0DTE means, how the Decision Desk works, and how to interpret graded alerts. The service is advisory‑only; customers place their own orders.
image: https://0dteconfluence.com/assets/og-1200x630.jpg?v=20260805
layout: provider
mcp_servers:
- description: Remote MCP server at api.0dteconfluence.com requiring an API key.
  name: 0DTE Confluence MCP Server
  slug: 0dteconfluence-com-mcp-yml
modified: '2026-10-31'
name: 0DTE Confluence
nav: Providers
network: true
overview: '0DTE Confluence is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Trading, Options, Market Data, Analytics, and Finance.


  The 0DTE Confluence catalog on APIs.io includes 1 Spectral governance ruleset.


  0DTE Confluence''s developer surface includes authentication, documentation, getting-started guide, support, engineering blog, and 12 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: 0DTE Confluence API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: 0dteconfluence-com-rules
scopes:
- name: 0Dteconfluence Com Scopes
  scope_count: 0
  slug: 0dteconfluence-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 10.5
    contract_governance: 19.7
    contract_quality: 10.5
    developer_ergonomics: 31.0
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 26.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
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
security:
- kind: authentication
  name: 0Dteconfluence Com Authentication
  slug: 0dteconfluence-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: 0Dteconfluence Com Domain Security
  slug: 0dteconfluence-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 0dteconfluence-com
tags:
- Trading
- Options
- Market Data
- Analytics
- Finance
- Company
website: https://0dteconfluence.com/
---
