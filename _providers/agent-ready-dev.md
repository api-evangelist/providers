---
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
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 72.9
  scored_at: '2026-09-20'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Agent Ready Dev Agentic Access
  operation_count: 8
  slug: agent-ready-dev-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 1
apis:
- baseURL: https://agent-ready.dev
  baseurl_source: declared
  description: REST API for agent-ready.dev scans, published as OpenAPI 3.1.0 at https://agent-ready.dev/api/v1/openapi.json (servers[] https://agent-ready.dev, info.contact support@agent-ready.dev). Eight operation
  name: Agent Ready API
  slug: agent-ready-api
- description: Hosted Model Context Protocol server at https://agent-ready.dev/api/v1/mcp (Streamable HTTP, POST only, protocol version 2025-06-18, serverInfo agent-ready 1.0.0). initialize, tools/list, resources/li
  name: Agent Ready MCP Server
  slug: agent-ready-mcp-server
- description: 'Agent2Agent (A2A) surface: a signed agent card served from https://agent-ready.dev/.well-known/agent-card.json (protocolVersion 1.0, JSONRPC, version 1.0.0, ES256 JWS signature with keys at /.well-kno'
  name: Agent Ready A2A Agent
  slug: agent-ready-a2a-agent
artifact_total: 12
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/agentic-access/agent-ready-dev-agentic-access.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/openapi/agent-ready-dev-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/agent-ready-dev-openapi.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/a2a/agent-ready-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agent-ready-dev-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/mcp/agent-ready-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agent-ready-dev-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/mcp/agent-ready-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agent-ready-dev-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/well-known/agent-ready-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agent-ready-dev-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/well-known/agent-ready-dev-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/agent-ready-dev-api-catalog.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/well-known/agent-ready-dev-http-message-signatures-directory.json
  title: ''
  type: HTTPMessageSignatures
  url: well-known/agent-ready-dev-http-message-signatures-directory.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/well-known/agent-ready-dev-robots.txt
  title: ''
  type: ContentSignal
  url: well-known/agent-ready-dev-robots.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/llms/agent-ready-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agent-ready-dev-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/packages/agent-ready-dev-packages.yml
  title: ''
  type: Packages
  url: packages/agent-ready-dev-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/packages/agent-ready-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/agent-ready-dev-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/cli/agent-ready-dev-cli.yml
  title: ''
  type: CLI
  url: cli/agent-ready-dev-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/components/agent-ready-dev-components.yml
  title: ''
  type: Components
  url: components/agent-ready-dev-components.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/authentication/agent-ready-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agent-ready-dev-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/scopes/agent-ready-dev-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/agent-ready-dev-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/conventions/agent-ready-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agent-ready-dev-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/conventions/agent-ready-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agent-ready-dev-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/errors/agent-ready-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agent-ready-dev-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/data-model/agent-ready-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agent-ready-dev-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/rate-limits/agent-ready-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agent-ready-dev-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/plans/agent-ready-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agent-ready-dev-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/conformance/agent-ready-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agent-ready-dev-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/lifecycle/agent-ready-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agent-ready-dev-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://agent-ready.dev/docs/api#versioning-and-deprecation-policy
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/changelog/agent-ready-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/agent-ready-dev-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/security/agent-ready-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agent-ready-dev-domain-security.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/agent-ready-dev/refs/heads/main/sandbox/agent-ready-dev-sandbox.yml
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
image: https://agent-ready.dev/icon-512.png
layout: provider
mcp_servers:
- description: ''
  name: Agent Ready MCP Server
  slug: agent-ready-mcp-server
- description: ''
  name: Agent Ready MCP endpoint (Streamable HTTP, Bearer)
  slug: agent-ready-mcp-endpoint-streamable-http-bearer
- description: ''
  name: Agent Ready MCP Apps endpoint (no auth)
  slug: agent-ready-mcp-apps-endpoint-no-auth
modified: '2026-09-19'
name: Agent Ready
nav: Providers
network: true
overview: 'Agent Ready publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agents, Agent Readiness, Website Scanning, Developer Tools, and MCP.


  Agent Ready''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, CLI, and 37 more developer resources.'
plans:
- name: Agent Ready Dev Plans Pricing
  plan_count: 3
  slug: agent-ready-dev-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Agent Ready Dev Rate Limits
  slug: agent-ready-dev-rate-limits
scopes:
- name: Agent Ready Dev Scopes
  scope_count: 4
  slug: agent-ready-dev-scopes
  summary_line: 4 scopes
score:
  band: strong
  composite: 61.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 59.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 60.2
    developer_ergonomics: 83.3
    discoverability: 75.9
    operational_transparency: 44.7
  previous_composite: 2.8
  provenance:
    agentic_access: derived
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
  trend: rising
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Agent Ready Dev Authentication
  slug: agent-ready-dev-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Agent Ready Dev Domain Security
  slug: agent-ready-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: agent-ready-dev
tags:
- Agents
- Agent Readiness
- Website Scanning
- Developer Tools
- MCP
- A2A
- llms-txt
- x402
- NLWeb
- Accessibility
- agent-native
- Australia
website: https://agent-ready.dev/
---
