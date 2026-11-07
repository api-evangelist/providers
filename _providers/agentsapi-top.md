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
  band: agent-ready
  dimensions:
    agent_card: conformant
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
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Agentsapi Top Agentic Access
  operation_count: 23
  slug: agentsapi-top-agentic-access
  summary_line: 23 operations · 8 acting
api_count: 1
apis:
- baseURL: https://agentsapi.top
  baseurl_source: declared
  description: On-chain alerts
  name: agentsapi-top Alerts API
  slug: agentsapi-top-alerts-api
- baseURL: https://agentsapi.top
  baseurl_source: declared
  description: CCTP cross-chain USDC tracking
  name: agentsapi-top Cctp API
  slug: agentsapi-top-cctp-api
- baseURL: https://agentsapi.top
  baseurl_source: declared
  description: Entity clustering / sybil detection
  name: agentsapi-top Cluster API
  slug: agentsapi-top-cluster-api
- baseURL: https://agentsapi.top
  baseurl_source: declared
  description: Transaction explanation
  name: agentsapi-top Explain API
  slug: agentsapi-top-explain-api
- baseURL: https://agentsapi.top
  baseurl_source: declared
  description: SEC 8-K material-event filings
  name: agentsapi-top Filings API
  slug: agentsapi-top-filings-api
- baseURL: https://agentsapi.top
  baseurl_source: declared
  description: The Healthz API from agentsapi-top — 1 operation(s) for healthz.
  name: agentsapi-top Healthz API
  slug: agentsapi-top-healthz-api
- baseURL: https://agentsapi.top
  baseurl_source: declared
  description: Address identity labels
  name: agentsapi-top Label API
  slug: agentsapi-top-label-api
- baseURL: https://agentsapi.top
  baseurl_source: declared
  description: Model Context Protocol (JSON-RPC 2.0 over HTTP) endpoint — 7 paid tools with an anonymous free tier
  name: agentsapi-top MCP API
  slug: agentsapi-top-mcp-api
- baseURL: https://agentsapi.top
  baseurl_source: declared
  description: The Me API from agentsapi-top — 1 operation(s) for me.
  name: agentsapi-top Me API
  slug: agentsapi-top-me-api
- baseURL: https://agentsapi.top
  baseurl_source: declared
  description: The Statusz API from agentsapi-top — 1 operation(s) for statusz.
  name: agentsapi-top Statusz API
  slug: agentsapi-top-statusz-api
- baseURL: https://agentsapi.top
  baseurl_source: declared
  description: Alert subscriptions
  name: agentsapi-top Subscription API
  slug: agentsapi-top-subscription-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/agentsapi-top/agentic-access/agentsapi-top-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentsapi-top-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentsapi-top/rules/agentsapi-top-rules.yml
  title: ''
  type: Spectral
  url: rules/agentsapi-top-rules.yml
- group: design
  href: https://artifacts.apis.io/agentsapi-top/vocabulary/agentsapi-top-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentsapi-top-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentsapi-top/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/agentsapi-top/security/agentsapi-top-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/agentsapi-top-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/agentsapi-top/errors/agentsapi-top-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentsapi-top-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentsapi-top/conformance/agentsapi-top-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentsapi-top-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentsapi-top/llms/agentsapi-top-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentsapi-top-llms.txt
- group: other
  href: https://artifacts.apis.io/agentsapi-top/a2a/agentsapi-top-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentsapi-top-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentsapi-top/mcp/agentsapi-top-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentsapi-top-mcp.yml
- group: auth
  href: https://artifacts.apis.io/agentsapi-top/well-known/agentsapi-top-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentsapi-top-security.txt
- group: agent
  href: https://artifacts.apis.io/agentsapi-top/well-known/agentsapi-top-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentsapi-top-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentsapi-top/hosts/agentsapi-top-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentsapi-top-hosts.yml
- group: auth
  href: https://artifacts.apis.io/agentsapi-top/authentication/agentsapi-top-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentsapi-top-authentication.yml
- group: auth
  href: https://artifacts.apis.io/agentsapi-top/security/agentsapi-top-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentsapi-top-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentsapi-top/security/agentsapi-top-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentsapi-top-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentsapi.top/
created: '2026-10-30'
description: BridgeWatch provides on‑chain risk intelligence APIs for crypto developers, traders, and protocol teams. It offers address labeling, transaction explanations, funding‑cluster analysis, alert tracking, and SEC filing feeds on the Base blockchain, with transparent credit‑based pricing and webhook support.
layout: provider
mcp_servers:
- description: Remote MCP server at agentsapi.top.
  name: agentsapi-top MCP Server
  slug: agentsapi-top-mcp-yml
modified: '2026-10-30'
name: agentsapi-top
nav: Providers
network: true
overview: 'agentsapi-top publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alerts API, Cctp API, Cluster API, and 8 more. Tagged areas include Blockchain, Risk Intelligence, Cryptocurrency, and On-Chain Data.


  The agentsapi-top catalog on APIs.io includes 1 Spectral governance ruleset.


  agentsapi-top''s developer surface includes authentication and 16 more developer resources.'
plans:
- name: Agentsapi Top Plans Pricing
  plan_count: 0
  slug: agentsapi-top-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Agentsapi Top Rate Limits
  slug: agentsapi-top-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: agentsapi-top API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 1
  slug: agentsapi-top-rules
scopes:
- name: Agentsapi Top Scopes
  scope_count: 0
  slug: agentsapi-top-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 28
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 50.1
    developer_ergonomics: 13.7
    discoverability: 63.3
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 28.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/agentsapi-top/agentsapi-top-2026-11-03T120407.png
security:
- kind: authentication
  name: Agentsapi Top Authentication
  slug: agentsapi-top-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Agentsapi Top Domain Security
  slug: agentsapi-top-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Agentsapi Top Vulnerability Disclosure
  slug: agentsapi-top-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: agentsapi-top-get-api-key-balance
  slug: agentsapi-top-get-api-key-balance
- name: get-label
  slug: agentsapi-top-get-label
- name: agentsapi-top-mcp-invoke
  slug: agentsapi-top-mcp-invoke
slug: agentsapi-top
tags:
- Blockchain
- Risk Intelligence
- Cryptocurrency
- On-Chain Data
website: https://agentsapi.top/
---
