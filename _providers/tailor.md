---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: 'The Tailor Platform control plane. A single tailor.v1.OperatorService with 254 RPCs covering organizations, folders, teams, access grants, IP restrictions, workspaces, applications and every platform '
  name: Tailor Platform Operator API
  slug: tailor-platform-operator-api
- description: The Tailor data plane. TailorDB generates a full GraphQL API from each application's schema — queries, mutations, filtering, sorting, Relay-style cursor pagination and aggregation — extended by custom
  name: Tailor Application GraphQL API
  slug: tailor-application-graphql-api
- description: HTTP endpoints Tailor provisions for external systems to trigger executor operations inside a workspace. Accepts application/json and application/x-www-form-urlencoded, is rate limited to 100 requests
  name: Tailor Executor Incoming Webhook API
  slug: tailor-executor-incoming-webhook-api
artifact_total: 12
asyncapis:
- description: ''
  name: Tailor Webhooks
  slug: tailor-webhooks
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/tailor-inc/proto/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.tailor.tech
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tailor.tech
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tailor.tech
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tailor.tech/reference/api/api-references
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tailor.tech/sdk/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.tailor.tech/administration/support
- group: company
  title: ''
  type: Blog
  url: https://www.tailor.tech/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tailor-platform
- group: start
  title: ''
  type: SignUp
  url: https://console.tailor.tech
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tailor.tech/privacy
- group: other
  title: ''
  type: Protobuf
  url: grpc/tailor-grpc.yml
- group: build
  title: ''
  type: Packages
  url: packages/tailor-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tailor-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tailor-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tailor-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/tailor-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tailor-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tailor-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tailor-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tailor-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tailor-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/tailor-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tailor-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tailor-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/tailor-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tailor-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tailor-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tailor-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/tailor-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tailor-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tailor-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tailor-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tailor-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: security/tailor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tailor-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tailor-domain-security.yml
created: '2026-08-29'
description: Tailor Technologies builds Tailor Platform, a headless, API-first ERP for retail, e-commerce and manufacturing operators. Its control plane is exposed as a single 254-RPC ConnectRPC service published as Protocol Buffers, and every application built on it gets an automatically generated GraphQL API over TailorDB with resolvers, pipelines, executors, workflows, an auth service and an OpenAI-compatible AI Gateway. The company ships a TypeScript SDK, a CLI, a Terraform provider, a React application framework (AppShell) and a first-party MCP server, and publishes llms.txt on both its marketing and documentation hosts. Tailor is a Y Combinator (S22) company and has raised $37M through Series A.
image: https://www.tailor.tech/og.jpg
layout: provider
mcp_servers:
- description: Tailor ships a first-party MCP server inside the tailorctl CLI. It is distributed as the npm installer @tailor-platform/tailor-mcp, which downloads the platform-appropriate tailorctl binary and runs i
  name: Tailor Platform MCP Server
  slug: tailor-platform-mcp-server
modified: '2026-08-29'
name: Tailor
nav: Providers
network: true
overview: 'Tailor publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, ERP, Headless ERP, Retail, and E-Commerce.


  The Tailor catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tailor''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, CLI, and 31 more developer resources.'
plans:
- name: Tailor Plans Pricing
  plan_count: 0
  slug: tailor-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Tailor Rate Limits
  slug: tailor-rate-limits
scopes:
- name: Tailor Scopes
  scope_count: 0
  slug: tailor-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.7
  coverage:
    artifact_dirs: 22
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 85.7
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 52.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Tailor Authentication
  slug: tailor-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Tailor Domain Security
  slug: tailor-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Tailor Vulnerability Disclosure
  slug: tailor-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Tailor Trust Center
  slug: tailor-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FedRAMP
slug: tailor
tags:
- Company
- ERP
- Headless ERP
- Retail
- E-Commerce
- Supply Chain
- Inventory Management
- GraphQL
- gRPC
- Low-Code
- Composable Commerce
- Manufacturing
website: https://www.tailor.tech
---
