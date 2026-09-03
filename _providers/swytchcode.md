---
access_model:
  confidence: high
  label: Freemium · self-service (free tier 1,000 execution calls/mo, no credit card; Pro $29/mo)
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://www.swytchcode.com/pricing
  trial: true
  try_now: true
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.6
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'Swytchcode''s publicly consumable surfaces: developer documentation and a published llms.txt. The primary interface is an npm-installable CLI (`swy`) plus a local MCP server (stdio/localhost, not a hos'
  name: Swytchcode Documentation & Agent Surfaces
  slug: swytchcode-documentation-agent-surfaces
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swytchcode-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/swytchcode-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/swytchcode-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/swytchcode-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/swytchcode-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/swytchcode-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/swytchcode-lifecycle.yml
- group: build
  title: ''
  type: CLI
  url: cli/swytchcode-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/swytchcode-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/swytchcode-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/swytchcode-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/swytchcode-problem-types.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/swytchcode-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/swytchcode-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/swytchcode-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/swytchcode-sandbox.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.swytchcode.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.swytchcode.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.swytchcode.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/swytchcodehq
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.swytchcode.com/quickstarts/getting-started/cli-only/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.swytchcode.com/reference/commands/
- group: operate
  title: ''
  type: Support
  url: https://docs.swytchcode.com/reference/troubleshooting/
- group: start
  title: ''
  type: Login
  url: https://app.swytchcode.com/
created: '2026-07-02'
description: Self-hosted AI agent execution layer that sits between an agent and production APIs, handling auth, retries, idempotency, policy enforcement, and audit logging across 2,000+ APIs. Consumable via a public npm-installable CLI (`swy`), an embedded local MCP server, and Runtime SDKs for JavaScript/TypeScript, Python, and Go, with a published llms.txt.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/swytchcode.png
layout: provider
mcp_servers:
- description: Local MCP server embedded in the Swytchcode CLI (npm package `swytchcode`). Runs on the developer's machine over stdio (default) or HTTP/SSE — there is no hosted/remote endpoint. Registered into edito
  name: Swytchcode MCP Server
  slug: swytchcode-mcp-server
modified: '2026-09-03'
name: Swytchcode
nav: Providers
network: true
overview: 'Swytchcode publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI / Agent Tooling, agentic middleware, API Integration, API Orchestration, and API execution layer.


  Swytchcode''s developer surface includes CLI, authentication, changelog, sandbox, pricing, getting-started guide, API reference, and 17 more developer resources.'
plans:
- name: Swytchcode Plans Pricing
  plan_count: 3
  slug: swytchcode-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Swytchcode Rate Limits
  slug: swytchcode-rate-limits
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 17
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 32.2
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 66.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 11.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/swytchcode/refs/heads/main/screenshots/swytchcode-2026-09-02T161429.png
security:
- kind: authentication
  name: Swytchcode Authentication
  slug: swytchcode-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Swytchcode Domain Security
  slug: swytchcode-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: swytchcode
tags:
- AI / Agent Tooling
- agentic middleware
- API Integration
- API Orchestration
- API execution layer
- LLM tool execution
- MCP Server
- Developer Tools
- API Documentation
- API playground
---
