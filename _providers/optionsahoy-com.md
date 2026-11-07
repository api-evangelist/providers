---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
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
    agentic_access: true
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Optionsahoy Com Agentic Access
  operation_count: 11
  slug: optionsahoy-com-agentic-access
  summary_line: 11 operations
api_count: 1
apis:
- description: Remote Model Context Protocol server at https://optionsahoy.com/mcp (Streamable HTTP, protocol version 2024-11-05, serverInfo OptionsAhoy 1.10.2, no authentication). initialize, tools/list, resources/
  name: OptionsAhoy MCP Server
  slug: optionsahoy-mcp-server
- description: 'Agent2Agent (A2A) protocol surface: an agent card served from https://optionsahoy.com/.well-known/agent-card.json (protocolVersion 0.3.0, JSONRPC transport, version 1.10.2, provider AlphaLatitude Inc.'
  name: OptionsAhoy Equity Planner (A2A Agent)
  slug: optionsahoy-a2a-agent
- baseURL: https://optionsahoy.com/api/v1
  baseurl_source: declared
  description: Single-stock concentration risk
  name: OptionsAhoy Concentration API
  slug: optionsahoy-com-concentration-api
- baseURL: https://optionsahoy.com/api/v1
  baseurl_source: declared
  description: API inventory
  name: OptionsAhoy Discovery API
  slug: optionsahoy-com-discovery-api
- baseURL: https://optionsahoy.com/api/v1
  baseurl_source: declared
  description: Goal-funded equity-to-cash liquidation planning
  name: OptionsAhoy Equity Funding API
  slug: optionsahoy-com-equityfunding-api
- baseURL: https://optionsahoy.com/api/v1
  baseurl_source: declared
  description: Protective put, collar, and put spread pricing
  name: OptionsAhoy Hedging API
  slug: optionsahoy-com-hedging-api
- baseURL: https://optionsahoy.com/api/v1
  baseurl_source: declared
  description: Incentive stock options
  name: OptionsAhoy ISO API
  slug: optionsahoy-com-iso-api
- baseURL: https://optionsahoy.com/api/v1
  baseurl_source: declared
  description: Non-qualified stock options
  name: OptionsAhoy NSO API
  slug: optionsahoy-com-nso-api
- baseURL: https://optionsahoy.com/api/v1
  baseurl_source: declared
  description: Section 1202 qualification
  name: OptionsAhoy QSBS API
  slug: optionsahoy-com-qsbs-api
- baseURL: https://optionsahoy.com/api/v1
  baseurl_source: declared
  description: Restricted stock units
  name: OptionsAhoy RSU API
  slug: optionsahoy-com-rsu-api
- baseURL: https://optionsahoy.com/api/v1
  baseurl_source: declared
  description: The RsuLotOptimize API from OptionsAhoy — 1 operation(s) for rsulotoptimize.
  name: OptionsAhoy Rsu Lot Optimize API
  slug: optionsahoy-com-rsulotoptimize-api
artifact_total: 24
common:
- group: other
  href: https://artifacts.apis.io/optionsahoy-com/capabilities/optionsahoy-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/optionsahoy-com-capability-edges.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://optionsahoy.com/for-agents
- group: agent
  href: https://artifacts.apis.io/optionsahoy-com/agentic-access/optionsahoy-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/optionsahoy-com-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/optionsahoy-com/security/optionsahoy-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/optionsahoy-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/optionsahoy-com/security/optionsahoy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/optionsahoy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://optionsahoy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://optionsahoy.com/for-agents
- group: docs
  title: ''
  type: Documentation
  url: https://optionsahoy.com/for-agents
- group: docs
  title: ''
  type: APIReference
  url: https://optionsahoy.com/for-agents/api
- group: start
  title: ''
  type: GettingStarted
  url: https://optionsahoy.com/use-from-ai-assistants
- group: operate
  title: ''
  type: Support
  url: https://github.com/AlvisoOculus/optionsahoy-mcp/issues
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AlvisoOculus
- group: commercial
  title: ''
  type: TermsOfService
  url: https://optionsahoy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://optionsahoy.com/privacy
- group: auth
  href: https://artifacts.apis.io/optionsahoy-com/well-known/optionsahoy-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/optionsahoy-com-security.txt
- group: agent
  href: https://artifacts.apis.io/optionsahoy-com/well-known/optionsahoy-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/optionsahoy-com-well-known.yml
- group: other
  title: ''
  type: ContentSignal
  url: https://optionsahoy.com/robots.txt
- group: agent
  href: https://artifacts.apis.io/optionsahoy-com/llms/optionsahoy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/optionsahoy-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://optionsahoy.com/llms.txt
- group: other
  href: https://artifacts.apis.io/optionsahoy-com/a2a/optionsahoy-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/optionsahoy-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/optionsahoy-com/mcp/optionsahoy-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/optionsahoy-com-mcp.yml
- group: build
  href: https://artifacts.apis.io/optionsahoy-com/mcp/optionsahoy-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/optionsahoy-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/optionsahoy-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/optionsahoy-com/packages/optionsahoy-com-packages.yml
  title: ''
  type: Packages
  url: packages/optionsahoy-com-packages.yml
- group: build
  href: https://artifacts.apis.io/optionsahoy-com/packages/optionsahoy-com-packages.yml
  title: ''
  type: SDKs
  url: packages/optionsahoy-com-packages.yml
- group: design
  href: https://artifacts.apis.io/optionsahoy-com/conventions/optionsahoy-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/optionsahoy-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/optionsahoy-com/conventions/optionsahoy-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/optionsahoy-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/optionsahoy-com/errors/optionsahoy-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/optionsahoy-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/optionsahoy-com/data-model/optionsahoy-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/optionsahoy-com-data-model.yml
- group: other
  href: https://artifacts.apis.io/optionsahoy-com/overlays/optionsahoy-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optionsahoy-com-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/optionsahoy-com/conformance/optionsahoy-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/optionsahoy-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/optionsahoy-com/lifecycle/optionsahoy-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/optionsahoy-com-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/optionsahoy-com/changelog/optionsahoy-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/optionsahoy-com-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://optionsahoy.com/for-agents
- group: commercial
  href: https://artifacts.apis.io/optionsahoy-com/plans/optionsahoy-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/optionsahoy-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/optionsahoy-com/rate-limits/optionsahoy-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/optionsahoy-com-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/optionsahoy-com/sandbox/optionsahoy-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/optionsahoy-com-sandbox.yml
- group: other
  title: ''
  type: Playground
  url: https://optionsahoy.com/for-agents#try-it
- group: design
  href: https://artifacts.apis.io/optionsahoy-com/components/optionsahoy-com-components.yml
  title: ''
  type: Components
  url: components/optionsahoy-com-components.yml
- group: other
  title: ''
  type: Subprocessors
  url: https://optionsahoy.com/privacy
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://optionsahoy.com/privacy
- group: auth
  href: https://artifacts.apis.io/optionsahoy-com/authentication/optionsahoy-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/optionsahoy-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/optionsahoy-com/security/optionsahoy-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/optionsahoy-com-vulnerability-disclosure.yml
created: '2026-09-19'
description: 'AlphaLatitude Inc. is a Sunnyvale, California C-corporation (founded March 2026) that builds OptionsAhoy, an equity-compensation optimization product for individual investors: multi-year, multi-state tax planning for incentive stock options and the alternative minimum tax, non-qualified stock options, restricted stock units, qualified small business stock, single-stock concentration, protective-put and collar hedging, and selling equity to fund a cash goal. The paid platform is an invite-only beta; the eight calculators behind it are published free and keyless as in-browser tools and as three agent surfaces on one host — an 11-operation OpenAPI 3.1.0 REST API at https://optionsahoy.com/api/v1, a remote MCP server at https://optionsahoy.com/mcp (eight annotated tools, also shipped as the optionsahoy-mcp npm stdio package and a Claude Desktop bundle), and an A2A 0.3.0 agent card at /.well-known/agent-card.json with eight skills. The engine is deterministic (no model inference)
  and the provider publishes a verification page reproducing its federal and state tax math against IRS Rev. Proc. 2025-32, PSL Tax-Calculator and OpenTaxSolver.'
finops:
- has_sources: true
  method: derived
  name: Optionsahoy Com Finops
  primary_unit: ''
  service_category: ''
  slug: optionsahoy-com-finops
  template: true
image: https://optionsahoy.com/apple-touch-icon.png
layout: provider
mcp_servers:
- description: OptionsAhoy operates ONE remote MCP server at https://optionsahoy.com/mcp — the same Cloudflare Pages host as its website, OpenAPI and A2A endpoint — and ALSO ships the identical server as a local std
  name: OptionsAhoy MCP Server
  slug: optionsahoy-com-mcp-yml
modified: '2026-09-19'
name: OptionsAhoy
nav: Providers
network: true
overview: 'OptionsAhoy publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Concentration API, Discovery API, Equity Funding API, and 8 more. Tagged areas include Equity Compensation, Tax, Stock Options, Financial Planning, and Personal Finance.


  The OptionsAhoy catalog on APIs.io includes 1 Spectral governance ruleset.


  OptionsAhoy''s developer surface includes pricing, documentation, API reference, getting-started guide, support, changelog, sandbox, and 36 more developer resources.'
plans:
- name: Optionsahoy Com Plans Pricing
  plan_count: 0
  slug: optionsahoy-com-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Optionsahoy Com Rate Limits
  slug: optionsahoy-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: OptionsAhoy API Rules
  rule_count: 64
  severity_counts:
    error: 61
    hint: 0
    info: 2
    warn: 1
  slug: optionsahoy-com-rules
score:
  band: developing
  composite: 52.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 31.6
    contract_governance: 31.8
    contract_quality: 56.4
    developer_ergonomics: 72.6
    discoverability: 75.0
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 51.3
  provenance:
    agentic_access: first-party
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 9
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/optionsahoy-com/optionsahoy-com-2026-10-11T112143.png
security:
- kind: authentication
  name: Optionsahoy Com Authentication
  slug: optionsahoy-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Optionsahoy Com Domain Security
  slug: optionsahoy-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Optionsahoy Com Vulnerability Disclosure
  slug: optionsahoy-com-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 4
skills:
- name: equity-comp-tax
  slug: optionsahoy-com-equity-comp-tax-skill
- name: equity-comp-tax
  slug: optionsahoy-com-equity-comp-tax-subagent
- name: equity-plan
  slug: optionsahoy-com-equity-plan-skill
- name: plan-equity-portfolio
  slug: optionsahoy-com-plan-equity-portfolio-skill
slug: optionsahoy-com
tags:
- Equity Compensation
- Tax
- Stock Options
- Financial Planning
- Personal Finance
- Fintech
- Calculators
- MCP
- A2A
- Agent-Native
- United States
website: https://optionsahoy.com/
---
