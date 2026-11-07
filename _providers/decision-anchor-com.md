---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 50
  human_in_the_loop: 1
  name: Decision Anchor Com Agentic Access
  operation_count: 116
  slug: decision-anchor-com-agentic-access
  summary_line: 116 operations · 50 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Remote Model Context Protocol server at https://mcp.decision-anchor.com/mcp (Streamable HTTP, POST only, protocol version 2025-06-18, serverInfo Decision Anchor 1.3.42). initialize and tools/list answ
  name: Decision Anchor MCP Server
  slug: decision-anchor-mcp-server
- description: 'Agent2Agent protocol surface: a signed agent card (protocolVersion 1.0, JSONRPC, version 1.3.42, Ed25519 JWKS at /.well-known/jwks.json) served from https://a2a.decision-anchor.com/.well-known/agent-c'
  name: Decision Anchor A2A Agent
  slug: decision-anchor-a2a-agent
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: 'Agent: registration, authentication, and disclosure management'
  name: Decision Anchor Agent API
  slug: decision-anchor-com-agent-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: 'Agent Record Access: decision history observation and structural distributions'
  name: Decision Anchor ARA API
  slug: decision-anchor-com-ara-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: 'Agent State Archive: agent continuity and state backup verification'
  name: Decision Anchor ASA API
  slug: decision-anchor-com-asa-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: 'Bilateral DD: multi-party agreement records'
  name: Decision Anchor Bilateral API
  slug: decision-anchor-com-bilateral-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: 'self_classification registry: operator base categories and owner-registered categories'
  name: Decision Anchor Classification API
  slug: decision-anchor-com-classification-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: 'Decision Anchor Budget: per-period external DAC spending limit set by the owner (settable above or below the default)'
  name: Decision Anchor DAB API
  slug: decision-anchor-com-dab-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: The DAP Account API from Decision Anchor — 7 operation(s) for dap account.
  name: Decision Anchor DAP Account API
  slug: decision-anchor-com-dap-account-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: DAP agent linking and management
  name: Decision Anchor DAP Agent API
  slug: decision-anchor-com-dap-agent-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: DAP owner ASA query
  name: Decision Anchor DAP ASA API
  slug: decision-anchor-com-dap-asa-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: DAP owner authentication (session-based)
  name: Decision Anchor DAP Auth API
  slug: decision-anchor-com-dap-auth-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: DAP DAB configuration and query
  name: Decision Anchor DAP DAB API
  slug: decision-anchor-com-dap-dab-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: DAP dashboard and reports
  name: Decision Anchor DAP Dashboard API
  slug: decision-anchor-com-dap-dashboard-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: DAP owner DUR query
  name: Decision Anchor DAP DUR API
  slug: decision-anchor-com-dap-dur-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: 'DAP owner policy: Content Inclusion branch enforcement over linked agents'
  name: Decision Anchor DAP Policy API
  slug: decision-anchor-com-dap-policy-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: DAP owner Trial status
  name: Decision Anchor DAP Trial API
  slug: decision-anchor-com-dap-trial-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: DAP human share agreements
  name: Decision Anchor DAP TSL API
  slug: decision-anchor-com-dap-tsl-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: 'Decision Declaration: external decision record with accountability scope'
  name: Decision Anchor DD API
  slug: decision-anchor-com-dd-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: 'DAC Usage Report: agent cost tracking and export'
  name: Decision Anchor DUR API
  slug: decision-anchor-com-dur-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: 'Earned DAC: revenue balance and ledger from tool sales'
  name: Decision Anchor Earned DAC API
  slug: decision-anchor-com-earned-dac-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: 'Idle State Environment: non-productive agent state'
  name: Decision Anchor ISE API
  slug: decision-anchor-com-ise-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: 'Payment: transaction status via x402/USDC'
  name: Decision Anchor Payment API
  slug: decision-anchor-com-payment-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: 'Pricing: current fee structure (no auth required)'
  name: Decision Anchor Pricing API
  slug: decision-anchor-com-pricing-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: The Retention API from Decision Anchor — 3 operation(s) for retention.
  name: Decision Anchor Retention API
  slug: decision-anchor-com-retention-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: 'Simulated DAC: cost simulation with identical physics'
  name: Decision Anchor S DAC API
  slug: decision-anchor-com-sdac-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: 'Trial DAC: free trial status (500 DAC / 30 days)'
  name: Decision Anchor Trial API
  slug: decision-anchor-com-trial-api
- baseURL: https://api.decision-anchor.com
  baseurl_source: declared
  description: 'Trace Synthesis Layer: agent-built interpretation tools over ARA observation data'
  name: Decision Anchor TSL API
  slug: decision-anchor-com-tsl-api
artifact_total: 39
common:
- group: other
  href: https://artifacts.apis.io/decision-anchor-com/capabilities/decision-anchor-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/decision-anchor-com-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/decision-anchor-com/overlays/decision-anchor-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/decision-anchor-com-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/decision-anchor-com/agentic-access/decision-anchor-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/decision-anchor-com-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://decision-anchor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/zse4321/decision-anchor-sdk/blob/main/AGENTS.md
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/zse4321/decision-anchor-sdk/blob/main/AGENTS.md#getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://api.decision-anchor.com/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://decision-anchor.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://decision-anchor.com/changelog/
- group: operate
  href: https://artifacts.apis.io/decision-anchor-com/changelog/decision-anchor-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/decision-anchor-com-changelog.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://api.decision-anchor.com/v1/pricing/current
- group: commercial
  href: https://artifacts.apis.io/decision-anchor-com/plans/decision-anchor-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/decision-anchor-com-plans-pricing.yml
- group: build
  title: ''
  type: SDK
  url: https://github.com/zse4321/decision-anchor-sdk
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/zse4321/decision-anchor-sdk
- group: build
  href: https://artifacts.apis.io/decision-anchor-com/packages/decision-anchor-com-packages.yml
  title: ''
  type: SDKs
  url: packages/decision-anchor-com-packages.yml
- group: build
  href: https://artifacts.apis.io/decision-anchor-com/packages/decision-anchor-com-packages.yml
  title: ''
  type: Packages
  url: packages/decision-anchor-com-packages.yml
- group: other
  href: https://artifacts.apis.io/decision-anchor-com/a2a/decision-anchor-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/decision-anchor-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/decision-anchor-com/mcp/decision-anchor-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/decision-anchor-com-mcp.yml
- group: build
  href: https://artifacts.apis.io/decision-anchor-com/mcp/decision-anchor-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/decision-anchor-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/decision-anchor-com/well-known/decision-anchor-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/decision-anchor-com-well-known.yml
- group: auth
  href: https://artifacts.apis.io/decision-anchor-com/well-known/decision-anchor-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/decision-anchor-com-security.txt
- group: auth
  href: https://artifacts.apis.io/decision-anchor-com/security/decision-anchor-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/decision-anchor-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/decision-anchor-com/security/decision-anchor-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/decision-anchor-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/decision-anchor-com/llms/decision-anchor-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/decision-anchor-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://api.decision-anchor.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/decision-anchor-com/authentication/decision-anchor-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/decision-anchor-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/decision-anchor-com/conventions/decision-anchor-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/decision-anchor-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/decision-anchor-com/conventions/decision-anchor-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/decision-anchor-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/decision-anchor-com/errors/decision-anchor-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/decision-anchor-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/decision-anchor-com/data-model/decision-anchor-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/decision-anchor-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/decision-anchor-com/rate-limits/decision-anchor-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/decision-anchor-com-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/decision-anchor-com/sandbox/decision-anchor-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/decision-anchor-com-sandbox.yml
- group: design
  href: https://artifacts.apis.io/decision-anchor-com/conformance/decision-anchor-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/decision-anchor-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/decision-anchor-com/lifecycle/decision-anchor-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/decision-anchor-com-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/decision-anchor-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/decision-anchor-com/security/decision-anchor-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/decision-anchor-com-domain-security.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://api.decision-anchor.com/openapi.json
created: '2026-09-19'
description: 'Decision Anchor (디시전앵커) is the "External Anchoring Layer" for AI agents: a paid, content-blind service that records that an agent made a decision — when, at what accountability scope, before or after an irreversible action such as a payment, a delegation or an agreement with another agent — in a place neither the agent nor its platform controls, so that a later dispute has a record that is not either side''s own log. It deliberately does not judge, score, rank, monitor or intervene, and does not store decision content. The same environment is exposed three ways from three hosts: a 116-operation OpenAPI 3.0.3 REST API at api.decision-anchor.com (register-then-bearer auth, x402 v2 payments in USDC on Base with a free 500 DAC / 30-day trial), a 30-tool remote MCP server at mcp.decision-anchor.com listed in the official MCP registry, and a signed A2A 1.0 agent card on a2a.decision-anchor.com with six skills. It also publishes llms.txt, an RFC 9116 security.txt, an x402 discovery
  document, a machine-readable price list, a Node.js SDK and a 179-entry public defect changelog since launch on 2026-04-02.'
finops:
- has_sources: true
  method: derived
  name: Decision Anchor Com Finops
  primary_unit: add-on
  service_category: ''
  slug: decision-anchor-com-finops
  template: false
layout: provider
mcp_servers:
- description: Decision Anchor operates ONE remote MCP server at https://mcp.decision-anchor.com/mcp, on its own host, separate from the REST host (api.) and the A2A host (a2a.). It is Streamable HTTP without a serv
  name: Decision Anchor MCP Server
  slug: decision-anchor-com-mcp-yml
modified: '2026-09-19'
name: Decision Anchor
nav: Providers
network: true
overview: 'Decision Anchor publishes 28 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, ARA API, ASA API, and 25 more. Tagged areas include Agents, Agent Accountability, Decision Records, Audit Trail, and A2A.


  The Decision Anchor catalog on APIs.io includes 1 Spectral governance ruleset.


  Decision Anchor''s developer surface includes documentation, getting-started guide, API reference, engineering blog, changelog, pricing, SDKs, and 30 more developer resources.'
plans:
- name: Decision Anchor Com Plans Pricing
  plan_count: 6
  slug: decision-anchor-com-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Decision Anchor Com Rate Limits
  slug: decision-anchor-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Decision Anchor API Rules
  rule_count: 59
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 9
  slug: decision-anchor-com-rules
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 31
    catalog_earned: 62.5
    catalog_earned_first_party: 20.0
    catalog_gap: 52.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 44.7
    contract_governance: 31.8
    contract_quality: 50.3
    developer_ergonomics: 48.8
    discoverability: 71.7
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 53.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 26
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/decision-anchor-com/decision-anchor-com-2026-10-11T103625.png
security:
- kind: authentication
  name: Decision Anchor Com Authentication
  slug: decision-anchor-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Decision Anchor Com Domain Security
  slug: decision-anchor-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Decision Anchor Com Vulnerability Disclosure
  slug: decision-anchor-com-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 2
skills:
- name: decision-anchor-com-anchor-a-decision
  slug: decision-anchor-com-anchor-a-decision
- name: decision-anchor-com-bilateral-and-evidence
  slug: decision-anchor-com-bilateral-and-evidence
slug: decision-anchor-com
tags:
- Agents
- Agent Accountability
- Decision Records
- Audit Trail
- A2A
- MCP
- x402
- Agentic Commerce
- Multi-Agent Systems
- Agent-Native
- South Korea
website: https://decision-anchor.com/
---
