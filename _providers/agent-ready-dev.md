---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 74.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Agent Ready Dev Agentic Access
  operation_count: 8
  slug: agent-ready-dev-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 3
apis:
- description: Hosted Model Context Protocol server at https://agent-ready.dev/api/v1/mcp (Streamable HTTP, POST only, protocol version 2025-06-18, serverInfo agent-ready 1.0.0). initialize, tools/list, resources/li
  name: Agent Ready MCP Server
  slug: agent-ready-mcp-server
- description: 'Agent2Agent (A2A) surface: a signed agent card served from https://agent-ready.dev/.well-known/agent-card.json (protocolVersion 1.0, JSONRPC, version 1.0.0, ES256 JWS signature with keys at /.well-kno'
  name: Agent Ready A2A Agent
  slug: agent-ready-a2a-agent
- baseURL: https://agent-ready.dev/api/v1/mcp
  baseurl_source: declared
  description: The MCP API from Agent Ready — 1 operation(s) for mcp.
  name: Agent Ready MCP API
  slug: agent-ready-dev-mcp-api
- baseURL: https://agent-ready.dev/api/v1/mcp
  baseurl_source: declared
  description: The NLWeb API from Agent Ready — 1 operation(s) for nlweb.
  name: Agent Ready NL Web API
  slug: agent-ready-dev-nlweb-api
- baseURL: https://agent-ready.dev/api/v1/mcp
  baseurl_source: declared
  description: The Scans API from Agent Ready — 3 operation(s) for scans.
  name: Agent Ready Scans API
  slug: agent-ready-dev-scans-api
- baseURL: https://agent-ready.dev/api/v1/mcp
  baseurl_source: declared
  description: The X402 API from Agent Ready — 1 operation(s) for x402.
  name: Agent Ready X402 API
  slug: agent-ready-dev-x402-api
artifact_total: 21
common:
- group: other
  href: https://artifacts.apis.io/agent-ready-dev/capabilities/agent-ready-dev-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/agent-ready-dev-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/agent-ready-dev/overlays/agent-ready-dev-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agent-ready-dev-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/agent-ready-dev/agentic-access/agent-ready-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agent-ready-dev-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://agent-ready.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agent-ready.dev/docs
- group: docs
  title: ''
  type: Documentation
  url: https://agent-ready.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://agent-ready.dev/docs/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://agent-ready.dev/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://agent-ready.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://agent-ready.dev/sign-up
- group: start
  title: ''
  type: Login
  url: https://agent-ready.dev/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agent-ready.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agent-ready.dev/privacy
- group: operate
  title: ''
  type: Support
  url: https://agent-ready.dev/about
- group: operate
  title: ''
  type: StatusPage
  url: https://status.agent-ready.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mlava
- group: docs
  href: https://artifacts.apis.io/agent-ready-dev/openapi/agent-ready-dev-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/agent-ready-dev-openapi.yml
- group: other
  href: https://artifacts.apis.io/agent-ready-dev/a2a/agent-ready-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agent-ready-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agent-ready-dev/mcp/agent-ready-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agent-ready-dev-mcp.yml
- group: build
  href: https://artifacts.apis.io/agent-ready-dev/mcp/agent-ready-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agent-ready-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agent-ready-dev/well-known/agent-ready-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agent-ready-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/agent-ready-dev/well-known/agent-ready-dev-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/agent-ready-dev-api-catalog.json
- group: other
  href: https://artifacts.apis.io/agent-ready-dev/well-known/agent-ready-dev-http-message-signatures-directory.json
  title: ''
  type: HTTPMessageSignatures
  url: well-known/agent-ready-dev-http-message-signatures-directory.json
- group: other
  href: https://artifacts.apis.io/agent-ready-dev/well-known/agent-ready-dev-robots.txt
  title: ''
  type: ContentSignal
  url: well-known/agent-ready-dev-robots.txt
- group: agent
  href: https://artifacts.apis.io/agent-ready-dev/llms/agent-ready-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agent-ready-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/agent-ready-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/agent-ready-dev/packages/agent-ready-dev-packages.yml
  title: ''
  type: Packages
  url: packages/agent-ready-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/agent-ready-dev/packages/agent-ready-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/agent-ready-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/agent-ready-dev/cli/agent-ready-dev-cli.yml
  title: ''
  type: CLI
  url: cli/agent-ready-dev-cli.yml
- group: design
  href: https://artifacts.apis.io/agent-ready-dev/components/agent-ready-dev-components.yml
  title: ''
  type: Components
  url: components/agent-ready-dev-components.yml
- group: auth
  href: https://artifacts.apis.io/agent-ready-dev/authentication/agent-ready-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agent-ready-dev-authentication.yml
- group: auth
  href: https://artifacts.apis.io/agent-ready-dev/scopes/agent-ready-dev-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/agent-ready-dev-scopes.yml
- group: design
  href: https://artifacts.apis.io/agent-ready-dev/conventions/agent-ready-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agent-ready-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/agent-ready-dev/conventions/agent-ready-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agent-ready-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/agent-ready-dev/errors/agent-ready-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agent-ready-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agent-ready-dev/data-model/agent-ready-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agent-ready-dev-data-model.yml
- group: operate
  href: https://artifacts.apis.io/agent-ready-dev/rate-limits/agent-ready-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agent-ready-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/agent-ready-dev/plans/agent-ready-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agent-ready-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agent-ready-dev/conformance/agent-ready-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agent-ready-dev-conformance.yml
- group: design
  href: https://artifacts.apis.io/agent-ready-dev/lifecycle/agent-ready-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agent-ready-dev-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://agent-ready.dev/docs/api#versioning-and-deprecation-policy
- group: operate
  href: https://artifacts.apis.io/agent-ready-dev/changelog/agent-ready-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/agent-ready-dev-changelog.yml
- group: auth
  href: https://artifacts.apis.io/agent-ready-dev/security/agent-ready-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agent-ready-dev-domain-security.yml
- group: start
  href: https://artifacts.apis.io/agent-ready-dev/sandbox/agent-ready-dev-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/agent-ready-dev-sandbox.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://agent-ready.dev/privacy
- group: other
  title: ''
  type: Subprocessors
  url: https://agent-ready.dev/privacy
created: '2026-09-19'
description: Agent Ready (agent-ready.dev) is an independent AI agent-readability scanner built and maintained by Mark Lavercombe. It scores any public website against the Vercel Agent Readability Spec, the llmstxt.org specification and the agent-protocol manifests (MCP server cards, A2A agent cards, agents.json, agent-permissions.json, UCP, ACP, x402, MPP, AP2, NLWeb, RFC 9727 API catalog, Web Bot Auth, Agent Skills Discovery) — 72 checks plus a separate 23-check WCAG 2.2 accessibility sub-score — and returns a 0-100 score with per-check remediation. The same scanner is exposed as an OpenAPI 3.1 REST API at https://agent-ready.dev/api/v1 (Pro API keys, Idempotency-Key on writes, RFC 8594 Sunset policy), a hosted Streamable HTTP MCP server at /api/v1/mcp plus a no-auth MCP Apps endpoint, an A2A 1.0 agent card, a stdio MCP package and CLI on npm, JavaScript and Python client SDKs, a GitHub Action, and pay-per-scan x402/MPP micropayments in USDC on Base. Free ($0) and Pro ($19/month) plans.
finops:
- has_sources: true
  method: derived
  name: Agent Ready Dev Finops
  primary_unit: scan
  service_category: ''
  slug: agent-ready-dev-finops
  template: false
image: https://agent-ready.dev/icon-512.png
layout: provider
mcp_servers:
- description: Agent Ready operates TWO hosted Streamable HTTP MCP endpoints on its apex host plus a stdio package on npm. (1) https://agent-ready.dev/api/v1/mcp — the "agent-ready" server (protocol version 2025-06-
  name: Agent Ready MCP Server
  slug: agent-ready-dev-mcp-yml
- description: ''
  name: Agent Ready MCP Apps endpoint (no auth)
  slug: agent-ready-mcp-apps-endpoint-no-auth
modified: '2026-09-19'
name: Agent Ready
nav: Providers
network: true
overview: 'Agent Ready publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including MCP API, NL Web API, Scans API, and 3 more. Tagged areas include Agents, Agent Readiness, Website Scanning, Developer Tools, and MCP.


  The Agent Ready catalog on APIs.io includes 1 Spectral governance ruleset.


  Agent Ready''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, CLI, and 39 more developer resources.'
plans:
- name: Agent Ready Dev Plans Pricing
  plan_count: 4
  slug: agent-ready-dev-plans-pricing
- name: Agent Ready Dev Price Estimates
  plan_count: 0
  slug: agent-ready-dev-price-estimates
random_paper: 5
rate_limits:
- limit_count: 0
  name: Agent Ready Dev Rate Limits
  slug: agent-ready-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Agent Ready API Rules
  rule_count: 58
  severity_counts:
    error: 48
    hint: 0
    info: 5
    warn: 5
  slug: agent-ready-dev-rules
scopes:
- name: Agent Ready Dev Scopes
  scope_count: 4
  slug: agent-ready-dev-scopes
  summary_line: 4 scopes
score:
  band: strong
  composite: 56.9
  coverage:
    artifact_dirs: 34
    catalog_earned: 59.5
    catalog_earned_first_party: 12.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.0
  facets:
    access_clarity: 61.8
    contract_governance: 31.8
    contract_quality: 54.4
    developer_ergonomics: 61.9
    discoverability: 80.0
    operational_transparency: 30.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 67.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 75.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/agent-ready-dev/agent-ready-dev-2026-10-11T093045.png
security:
- kind: authentication
  name: Agent Ready Dev Authentication
  slug: agent-ready-dev-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Agent Ready Dev Domain Security
  slug: agent-ready-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: agent-ready-api
  slug: agent-ready-dev-agent-ready-api
- name: agent-ready-cli
  slug: agent-ready-dev-agent-ready-cli
- name: agent-ready-mcp
  slug: agent-ready-dev-agent-ready-mcp
- name: scan-agent-readiness
  slug: agent-ready-dev-scan-agent-readiness
slug: agent-ready-dev
tags:
- Agents
- Agent Readiness
- Website Scanning
- Developer Tools
- MCP
- A2A
- Llms.txt
- x402
- NLWeb
- Accessibility
- Agent-Native
- Australia
website: https://agent-ready.dev/
---
