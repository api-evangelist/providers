---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 59.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 37
  human_in_the_loop: 5
  name: Lightrun Agentic Access
  operation_count: 67
  slug: lightrun-agentic-access
  summary_line: 67 operations · 37 acting · 5 human-in-the-loop
api_count: 20
apis:
- description: Actions API.
  name: Lightrun Actions API
  slug: lightrun-actions-api
- description: Agent Pools API.
  name: Lightrun Agent Pools API
  slug: lightrun-agent-pools-api
- description: Agents API.
  name: Lightrun Agents API
  slug: lightrun-agents-api
- description: Custom sources API.
  name: Lightrun Custom sources API
  slug: lightrun-custom-sources-api
- description: Debug Cases API.
  name: Lightrun Debug Cases API
  slug: lightrun-debug-cases-api
- description: The Debug Runbook methods API from Lightrun — 1 operation(s) for debug runbook methods.
  name: Lightrun Debug Runbook methods API
  slug: lightrun-debug-runbook-methods-api
- description: Debug Runbooks API.
  name: Lightrun Debug Runbooks API
  slug: lightrun-debug-runbooks-api
- description: Debug Runbooks Configuration API.
  name: Lightrun Debug Runbooks Configuration API
  slug: lightrun-debug-runbooks-configuration-api
- description: Dynamic SBOM API.
  name: Lightrun Dynamic SBOM API
  slug: lightrun-dynamic-sbom-api
- description: Identity Management (IdM) configuration API
  name: Lightrun Identity Management (IdM) configuration API
  slug: lightrun-identity-management-idm-configuration-api
- description: Just-In-Time Access API.
  name: Lightrun Just-In-Time Access API
  slug: lightrun-just-in-time-access-api
- description: Company License API.
  name: Lightrun License API
  slug: lightrun-license-api
- description: Lightrun feature flags status API.
  name: Lightrun Lightrun feature flags status API
  slug: lightrun-lightrun-feature-flags-status-api
- description: Loaded packages API.
  name: Lightrun Loaded packages API
  slug: lightrun-loaded-packages-api
- description: SMTP connectivity configuration API
  name: Lightrun SMTP connectivity configuration API
  slug: lightrun-smtp-connectivity-configuration-api
- description: System access API key management API.
  name: Lightrun System access API key API
  slug: lightrun-system-access-api-key-api
- description: Tags API.
  name: Lightrun Tags API
  slug: lightrun-tags-api
- description: User Groups API.
  name: Lightrun User Groups API
  slug: lightrun-user-groups-api
- description: Users API.
  name: Lightrun Users API
  slug: lightrun-users-api
- description: Watched packages API.
  name: Lightrun Watched packages API
  slug: lightrun-watched-packages-api
artifact_total: 27
asyncapis:
- description: ''
  name: Lightrun Webhooks
  slug: lightrun-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://lightrun.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lightrun.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lightrun.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lightrun.com/public-api/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lightrun.com/get-started/
- group: company
  title: ''
  type: Blog
  url: https://lightrun.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lightrun-platform
- group: commercial
  title: ''
  type: Pricing
  url: https://lightrun.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.lightrun.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lightrun.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lightrun.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.lightrun.com/release_notes/functionality-changes-deprecations/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lightrun-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.lightrun.com/release_notes/lightrun-release-notes/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lightrun-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lightrun-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lightrun-agentic-access.yml
- group: build
  title: ''
  type: CLI
  url: cli/lightrun-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/lightrun-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lightrun-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lightrun-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lightrun-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lightrun-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lightrun-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lightrun-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lightrun-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lightrun-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.lightrun.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/lightrun-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightrun-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lightrun-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/lightrun-openid-configuration.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lightrun-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/lightrun-public-api-overlay.yaml
created: '2026-07-17'
description: Lightrun is a developer-native observability and live-debugging platform. Language agents embedded in a running JVM, Python, Node.js or .NET process accept dynamic actions — logs, snapshots, counters, tic-toc timings and custom metrics — placed on a file and line while the application keeps serving traffic, so engineers can inspect production behavior without redeploying, restarting or attaching a traditional debugger. The platform is driven from JetBrains, VS Code and Visual Studio plugins, a Java CLI, a bearer-authenticated Public REST API, and a published MCP server that gives AI coding assistants live runtime context. Around that core it adds agent-pool RBAC, PII redaction, SSO and SCIM provisioning, and a Dynamic SBOM surface that reports which third-party packages are actually reachable at runtime.
image: https://lightrun.com/
layout: provider
mcp_servers:
- description: ''
  name: lightrun-mcp.yml
  slug: lightrun-mcpyml
modified: '2026-07-19'
name: Lightrun
nav: Providers
network: true
overview: 'Lightrun publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Agent Pools API, Agents API, and 17 more. Tagged areas include Company, Developer Tools, Observability, Debugging, and Monitoring.


  The Lightrun catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lightrun''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 28 more developer resources.'
random_paper: 30
scopes:
- name: Lightrun Scopes
  scope_count: 0
  slug: lightrun-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 58.9
  delta: 0.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.3
    developer_ergonomics: 76.1
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 52.6
  previous_composite: 58.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lightrun/refs/heads/main/screenshots/lightrun-2026-07-25T225125.png
security:
- kind: authentication
  name: Lightrun Authentication
  slug: lightrun-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lightrun Domain Security
  slug: lightrun-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Lightrun Trust Center
  slug: lightrun-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: lightrun
tags:
- Company
- Developer Tools
- Observability
- Debugging
- Monitoring
- Logging
- Application Performance
- Agent Skills
- Model Context Protocol
- DevOps
website: https://lightrun.com/
---
