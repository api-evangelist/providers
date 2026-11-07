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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: X402Supply Com Agentic Access
  operation_count: 9
  slug: x402supply-com-agentic-access
  summary_line: 9 operations · 9 acting
api_count: 3
apis:
- baseURL: https://chess-eval.x402supply.com
  baseurl_source: declared
  description: The chess-eval API from x402supply-com — 3 operation(s) for chess-eval.
  name: x402supply-com Chess Eval API
  slug: x402supply-com-chess-eval-api
- baseURL: https://diligence.x402supply.com
  baseurl_source: declared
  description: The endpoint-diligence API from x402supply-com — 4 operation(s) for endpoint-diligence.
  name: x402supply-com Endpoint Diligence API
  slug: x402supply-com-endpoint-diligence-api
- baseURL: https://entity-resolve.x402supply.com
  baseurl_source: declared
  description: The entity-resolve API from x402supply-com — 2 operation(s) for entity-resolve.
  name: x402supply-com Entity Resolve API
  slug: x402supply-com-entity-resolve-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/x402supply-com/agentic-access/x402supply-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/x402supply-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/x402supply-com/rules/x402supply-com-rules.yml
  title: ''
  type: Spectral
  url: rules/x402supply-com-rules.yml
- group: design
  href: https://artifacts.apis.io/x402supply-com/vocabulary/x402supply-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/x402supply-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/x402supply-com/errors/x402supply-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/x402supply-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/x402supply-com/conformance/x402supply-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/x402supply-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/x402supply-com/llms/x402supply-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/x402supply-com-llms.txt
- group: build
  href: https://artifacts.apis.io/x402supply-com/mcp/x402supply-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/x402supply-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/x402supply-com/mcp/x402supply-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/x402supply-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/x402supply-com/hosts/x402supply-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/x402supply-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/x402supply-com/vendors/x402supply-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/x402supply-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/x402supply-com/security/x402supply-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/x402supply-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://x402supply.com/
- group: auth
  title: ''
  type: TrustPage
  url: https://x402supply.com/trust
- group: agent
  title: ''
  type: LLMsIndex
  url: https://x402supply.com/llms.txt
created: '2026-10-29'
description: x402 Supply provides a suite of pay-per-call API tools designed for AI agents, enabling developers to integrate specialized functionalities such as timezone conversion, token verification, and data extraction on a per-call basis. Operating on the Base blockchain with USDC payments, the platform eliminates the need for traditional API keys or accounts, offering a frictionless, usage‑based billing model. The service catalog includes tools for financial data, compliance checks, and AI‑enhanced utilities, all accessible via simple HTTP endpoints.
layout: provider
mcp_servers:
- description: Remote MCP server at chess-eval.x402supply.com.
  name: x402supply-com MCP Server
  slug: x402supply-com-mcp-yml
modified: '2026-10-29'
name: x402supply-com
nav: Providers
network: true
overview: 'x402supply-com publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Chess Eval API, Endpoint Diligence API, and Entity Resolve API. Tagged areas include Company, Artificial Intelligence, Pay-per-call, Blockchain, and Tools.


  The x402supply-com catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: x402supply-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: x402supply-com-rules
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 43.8
    catalog_earned_first_party: 0.0
    catalog_gap: 71.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 44.6
    developer_ergonomics: 0.0
    discoverability: 76.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/x402supply-com/x402supply-com-2026-11-03T150251.png
security:
- kind: domain-security
  name: X402Supply Com Domain Security
  slug: x402supply-com-domain-security
  summary_line: TLSv1.3
slug: x402supply-com
tags:
- Company
- Artificial Intelligence
- Pay-per-call
- Blockchain
- Tools
website: https://x402supply.com/
---
