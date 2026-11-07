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
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Backpow Com Agentic Access
  operation_count: 6
  slug: backpow-com-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL: https://mcp.backpow.com
  baseurl_source: declared
  description: The Coin Oracle API from BackPoW — 1 operation(s) for coin oracle.
  name: BackPoW Coin Oracle API
  slug: backpow-com-coin-oracle-api
- baseURL: https://mcp.backpow.com
  baseurl_source: declared
  description: The Coins API from BackPoW — 1 operation(s) for coins.
  name: BackPoW Coins API
  slug: backpow-com-coins-api
- baseURL: https://mcp.backpow.com
  baseurl_source: declared
  description: The Cost Of Production API from BackPoW — 1 operation(s) for cost of production.
  name: BackPoW Cost Of Production API
  slug: backpow-com-cost-of-production-api
- baseURL: https://mcp.backpow.com
  baseurl_source: declared
  description: The Hardware API from BackPoW — 1 operation(s) for hardware.
  name: BackPoW Hardware API
  slug: backpow-com-hardware-api
- baseURL: https://mcp.backpow.com
  baseurl_source: declared
  description: The News API from BackPoW — 1 operation(s) for news.
  name: BackPoW News API
  slug: backpow-com-news-api
- baseURL: https://mcp.backpow.com
  baseurl_source: declared
  description: The Solo Mining Odds API from BackPoW — 1 operation(s) for solo mining odds.
  name: BackPoW Solo Mining Odds API
  slug: backpow-com-solo-mining-odds-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/backpow-com/agentic-access/backpow-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/backpow-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/backpow-com/rules/backpow-com-rules.yml
  title: ''
  type: Spectral
  url: rules/backpow-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/backpow-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/backpow-com/conventions/backpow-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/backpow-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/backpow-com/errors/backpow-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/backpow-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/backpow-com/conformance/backpow-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/backpow-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/backpow-com/llms/backpow-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/backpow-com-llms.txt
- group: other
  href: https://artifacts.apis.io/backpow-com/a2a/backpow-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/backpow-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/backpow-com/mcp/backpow-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/backpow-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/backpow-com/mcp/backpow-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/backpow-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/backpow-com/hosts/backpow-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/backpow-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/backpow-com/vendors/backpow-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/backpow-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/backpow-com/packages/backpow-com-packages.yml
  title: ''
  type: SDKs
  url: packages/backpow-com-packages.yml
- group: build
  href: https://artifacts.apis.io/backpow-com/packages/backpow-com-packages.yml
  title: ''
  type: Packages
  url: packages/backpow-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/backpow-com/security/backpow-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/backpow-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://backpow.com/
- group: docs
  title: ''
  type: APIReference
  url: https://backpow.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://backpow.com/about
- group: operate
  title: ''
  type: Support
  url: https://backpow.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://backpow.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://backpow.com/privacy
created: '2026-11-02'
description: BackPoW is a free, independent data site for Proof‑of‑Work mining. It tracks over 117 networks and 856 mining devices, providing real‑time cost‑of‑production, solo mining odds, hardware profitability, and solo pool information. All data is available via a public JSON API and an MCP server for AI assistants. Figures are refreshed daily and derived from live network difficulty and hardware benchmarks. The service is run by a single individual and offers no financial advice.
image: https://backpow.com/og/home.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.backpow.com.
  name: BackPoW MCP Server
  slug: backpow-com-mcp-yml
modified: '2026-11-02'
name: BackPoW
nav: Providers
network: true
overview: 'BackPoW publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Coin Oracle API, Coins API, Cost Of Production API, and 3 more. Tagged areas include Cryptocurrency, Mining, Proof of Work, and Data.


  The BackPoW catalog on APIs.io includes 1 Spectral governance ruleset.


  BackPoW''s developer surface includes API reference, getting-started guide, support, and 18 more developer resources.'
plans:
- name: Backpow Com Plans Pricing
  plan_count: 0
  slug: backpow-com-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Backpow Com Rate Limits
  slug: backpow-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: BackPoW API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: backpow-com-rules
scopes:
- name: Backpow Com Scopes
  scope_count: 0
  slug: backpow-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 46.3
    developer_ergonomics: 25.5
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 34.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Backpow Com Authentication
  slug: backpow-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Backpow Com Domain Security
  slug: backpow-com-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: backpow-com-mcp
  slug: backpow-com-mcp
slug: backpow-com
tags:
- Cryptocurrency
- Mining
- Proof of Work
- Data
website: https://backpow.com/
---
