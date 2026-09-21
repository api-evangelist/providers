---
agent_readiness:
  band: agent-native
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.3
  scored_at: '2026-09-20'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Optionsahoy Com Agentic Access
  operation_count: 11
  slug: optionsahoy-com-agentic-access
  summary_line: 11 operations
api_count: 3
apis:
- baseURL: https://optionsahoy.com/api/v1
  baseurl_source: declared
  description: Keyless, CORS-open REST API wrapping the eight OptionsAhoy equity-compensation calculators — multi-year ISO/AMT exercise optimization, NSO exercise tax and sell-vs-hold, RSU sell-vs-hold, RSU lot-orde
  name: OptionsAhoy Calculator API
  slug: optionsahoy-calculator-api
- description: Remote Model Context Protocol server at https://optionsahoy.com/mcp (Streamable HTTP, protocol version 2024-11-05, serverInfo OptionsAhoy 1.10.2, no authentication). initialize, tools/list, resources/
  name: OptionsAhoy MCP Server
  slug: optionsahoy-mcp-server
- description: 'Agent2Agent (A2A) protocol surface: an agent card served from https://optionsahoy.com/.well-known/agent-card.json (protocolVersion 0.3.0, JSONRPC transport, version 1.10.2, provider AlphaLatitude Inc.'
  name: OptionsAhoy Equity Planner (A2A Agent)
  slug: optionsahoy-a2a-agent
artifact_total: 11
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/agentic-access/optionsahoy-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/optionsahoy-com-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/security/optionsahoy-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/optionsahoy-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/security/optionsahoy-com-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/well-known/optionsahoy-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/optionsahoy-com-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/well-known/optionsahoy-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/optionsahoy-com-well-known.yml
- group: other
  title: ''
  type: ContentSignal
  url: https://optionsahoy.com/robots.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/llms/optionsahoy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/optionsahoy-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://optionsahoy.com/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/a2a/optionsahoy-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/optionsahoy-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/mcp/optionsahoy-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/optionsahoy-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/mcp/optionsahoy-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/optionsahoy-com-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/packages/optionsahoy-com-packages.yml
  title: ''
  type: Packages
  url: packages/optionsahoy-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/packages/optionsahoy-com-packages.yml
  title: ''
  type: SDKs
  url: packages/optionsahoy-com-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/conventions/optionsahoy-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/optionsahoy-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/conventions/optionsahoy-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/optionsahoy-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/errors/optionsahoy-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/optionsahoy-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/data-model/optionsahoy-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/optionsahoy-com-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/overlays/optionsahoy-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optionsahoy-com-openapi-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/conformance/optionsahoy-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/optionsahoy-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/lifecycle/optionsahoy-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/optionsahoy-com-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/changelog/optionsahoy-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/optionsahoy-com-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://optionsahoy.com/for-agents
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/plans/optionsahoy-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/optionsahoy-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/rate-limits/optionsahoy-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/optionsahoy-com-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/sandbox/optionsahoy-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/optionsahoy-com-sandbox.yml
- group: other
  title: ''
  type: Playground
  url: https://optionsahoy.com/for-agents#try-it
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/components/optionsahoy-com-components.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/authentication/optionsahoy-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/optionsahoy-com-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/optionsahoy-com/refs/heads/main/security/optionsahoy-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/optionsahoy-com-vulnerability-disclosure.yml
created: '2026-09-19'
description: 'AlphaLatitude Inc. is a Sunnyvale, California C-corporation (founded March 2026) that builds OptionsAhoy, an equity-compensation optimization product for individual investors: multi-year, multi-state tax planning for incentive stock options and the alternative minimum tax, non-qualified stock options, restricted stock units, qualified small business stock, single-stock concentration, protective-put and collar hedging, and selling equity to fund a cash goal. The paid platform is an invite-only beta; the eight calculators behind it are published free and keyless as in-browser tools and as three agent surfaces on one host — an 11-operation OpenAPI 3.1.0 REST API at https://optionsahoy.com/api/v1, a remote MCP server at https://optionsahoy.com/mcp (eight annotated tools, also shipped as the optionsahoy-mcp npm stdio package and a Claude Desktop bundle), and an A2A 0.3.0 agent card at /.well-known/agent-card.json with eight skills. The engine is deterministic (no model inference)
  and the provider publishes a verification page reproducing its federal and state tax math against IRS Rev. Proc. 2025-32, PSL Tax-Calculator and OpenTaxSolver.'
image: https://optionsahoy.com/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: AlphaLatitude Inc. MCP Server
  slug: alphalatitude-inc-mcp-server
- description: ''
  name: OptionsAhoy MCP endpoint (Streamable HTTP)
  slug: optionsahoy-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: AlphaLatitude Inc.
nav: Providers
network: true
overview: 'AlphaLatitude Inc. publishes 1 API on the [APIs.io](https://apis.io/) network: OptionsAhoy Calculator API. Tagged areas include Equity Compensation, Tax, Stock Options, Financial Planning, and Personal Finance.


  AlphaLatitude Inc.''s developer surface includes documentation, API reference, getting-started guide, support, changelog, sandbox, authentication, and 34 more developer resources.'
plans:
- name: Optionsahoy Com Plans Pricing
  plan_count: 1
  slug: optionsahoy-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Optionsahoy Com Rate Limits
  slug: optionsahoy-com-rate-limits
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 56.4
    developer_ergonomics: 72.6
    discoverability: 81.5
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 50.3
  provenance:
    agentic_access: first-party
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- agent-native
- Deterministic
- United States
website: https://optionsahoy.com/
---
