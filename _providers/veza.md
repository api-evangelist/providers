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
  band: agent-aware
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 39.4
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Publish identity, resource and authorization metadata from custom or unsupported applications into the Veza Entity Catalog, and run authorization assessment queries and reports.
  name: Veza Open Authorization API (OAA)
  slug: veza-open-authorization-api-oaa
artifact_total: 5
asyncapis:
- description: ''
  name: Veza Webhooks
  slug: veza-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.veza.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.veza.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.veza.com/oaa/reference/api/oaa-push-api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.veza.com/oaa/guide/getting-started.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/veza
- group: company
  title: ''
  type: Blog
  url: https://www.veza.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.veza.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.veza.com/demo/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.veza.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/veza-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/veza-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/veza-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/veza-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/veza-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/veza-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/veza-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/veza-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/veza-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/veza-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/veza-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/veza-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/veza-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.veza.com/
created: '2026-07-17'
description: Veza is an identity security platform. Its Open Authorization API (OAA) publishes identity, resource, and authorization metadata from custom or unsupported applications into the Veza Entity Catalog, making access across systems searchable and governable for least-privilege enforcement, access reviews, and rules and alerts. The REST API manages custom providers and their data sources, pushes OAA JSON payloads (users, groups, roles, resources, permissions), and runs authorization assessment queries and reports. It authenticates with a per-tenant API key presented as a bearer token, with official Python and C# SDKs and a command-line client.
image: https://veza.com/wp-content/uploads/2024/01/Veza_Stacked-1.png
layout: provider
mcp_servers:
- description: ''
  name: veza-mcp.yml
  slug: veza-mcpyml
modified: '2026-07-21'
name: Veza
nav: Providers
network: true
overview: 'Veza publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Identity Security, Authorization, and Access Management.


  The Veza catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Veza''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, authentication, CLI, and 17 more developer resources.'
random_paper: 30
score:
  band: thin
  composite: 38.6
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 22.6
    developer_ergonomics: 76.1
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 38.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Veza Authentication
  slug: veza-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Veza Domain Security
  slug: veza-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: veza
tags:
- Company
- Security
- Identity Security
- Authorization
- Access Management
- Identity Governance
- API
website: https://www.veza.com/
---
