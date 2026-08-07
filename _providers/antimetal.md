---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Antimetal Agentic Access
  operation_count: 9
  slug: antimetal-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 3
apis:
- description: Public-facing REST API for external integrations with Antimetal. Provides programmatic access to issue creation and lifecycle management, asynchronous investigation results including root-cause and re
  name: Antimetal External API
  slug: antimetal-external-api
- description: Remote Model Context Protocol server exposing Antimetal's investigation, root-cause analysis and remediation capabilities to MCP-compatible clients such as Claude Code, Cursor, VS Code, Windsurf and C
  name: Antimetal MCP Server
  slug: antimetal-mcp-server
- description: Public protobuf/Connect definitions for the Antimetal system agent — the component that connects customer infrastructure to the Antimetal platform. Covers agent config and instance, hardware and Linux
  name: Antimetal Agent APIs (Protobuf)
  slug: antimetal-agent-apis
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/antimetal-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/antimetal-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/antimetal-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.antimetal.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.antimetal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.antimetal.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.antimetal.com/api-reference/issues/fetch-issues-for-an-organization
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.antimetal.com/quick-start
- group: start
  title: ''
  type: SignUp
  url: https://overlook.antimetal.com/
- group: operate
  title: ''
  type: Support
  url: mailto:support@antimetal.com
- group: company
  title: ''
  type: Blog
  url: https://antimetal.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/antimetal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://antimetal.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://antimetal.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.antimetal.com/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.antimetal.com/admin/security
- group: auth
  title: ''
  type: Security
  url: https://docs.antimetal.com/admin/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/antimetal-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/antimetal-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/antimetal-api-catalog.json
- group: other
  title: ''
  type: AgentCard
  url: a2a/antimetal-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/antimetal-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/antimetal-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/antimetal-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/antimetal-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/antimetal-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/antimetal-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/antimetal-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/antimetal-data-model.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/antimetal-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/antimetal-trust-center.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/antimetal-scopes.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/antimetal-service-agent-v1-service.proto
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/antimetal
created: '2026-08-06'
description: Antimetal is a New York based software company building an autonomous production-management platform for engineering teams — "everything that happens after you deploy". It maintains a continuously updated world model of a customer's production stack and runs specialized AI agents that patrol for risk and drift, triage noisy signals into structured issues, investigate incidents down to a root cause, and generate production-ready fixes tied back to the underlying evidence. It connects to more than ninety cloud, observability, CI/CD, incident and code tools — AWS, Google Cloud, Azure, Kubernetes, Datadog, Grafana, Prometheus, Sentry, Splunk, New Relic, Honeycomb, PagerDuty, incident.io, GitHub, Vercel and Slack among them. Antimetal publishes a public REST API (the Antimetal External API, at bff.antimetal.com/api/v2) covering issues, investigation results, evidential artifacts and a natural-language query endpoint, a remote MCP server at mcp.antimetal.com with OAuth 2.1 and API-key
  auth, an official TypeScript SDK, published Agent Skills for Claude Code and Cursor, open protobuf definitions for its infrastructure agent, and a Terraform provider and Helm charts.
image: https://avatars.githubusercontent.com/antimetal
layout: provider
mcp_servers:
- description: ''
  name: antimetal-mcp.yml
  slug: antimetal-mcpyml
modified: '2026-08-06'
name: Antimetal
nav: Providers
network: true
overview: 'Antimetal publishes 1 API on the [APIs.io](https://apis.io/) network: External API. Tagged areas include Company, Observability, Incident Management, Site Reliability Engineering, and Artificial Intelligence.


  Antimetal''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 28 more developer resources.'
random_paper: 55
scopes:
- name: Antimetal Scopes
  scope_count: 4
  slug: antimetal-scopes
  summary_line: 4 scopes · authorizationCode/deviceCode/refreshToken
score:
  band: developing
  composite: 55.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 56.6
    developer_ergonomics: 65.2
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 47.4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: Antimetal Authentication
  slug: antimetal-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Antimetal Domain Security
  slug: antimetal-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Antimetal Vulnerability Disclosure
  slug: antimetal-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Antimetal Trust Center
  slug: antimetal-trust-center
  summary_line: SOC 2 Type II, HIPAA
slug: antimetal
tags:
- Company
- Observability
- Incident Management
- Site Reliability Engineering
- Artificial Intelligence
- Agents
- DevOps
- Cloud Infrastructure
- Kubernetes
- Root Cause Analysis
- MCP
website: https://www.antimetal.com/
---
