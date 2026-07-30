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
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 43.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Unito Agentic Access
  operation_count: 6
  slug: unito-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 3
apis:
- description: The Reports API from Unito — 1 operation(s) for reports.
  name: Unito Reports API
  slug: unito-reports-api
- description: The Server API from Unito — 2 operation(s) for server.
  name: Unito Server API
  slug: unito-server-api
- description: The Workspaces API from Unito — 2 operation(s) for workspaces.
  name: Unito Workspaces API
  slug: unito-workspaces-api
artifact_total: 9
asyncapis:
- description: ''
  name: Unito Connector Webhooks
  slug: unito-connector-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unito-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/unito-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unito-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unito-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://unito.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.unito.io/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.unito.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.unito.io/embeds/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.unito.io/docs/intro/
- group: operate
  title: ''
  type: Support
  url: https://guide.unito.io/en/
- group: company
  title: ''
  type: Blog
  url: https://unito.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unitoio
- group: commercial
  title: ''
  type: Pricing
  url: https://unito.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.unito.io/#/signup
- group: start
  title: ''
  type: Login
  url: https://app.unito.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unito.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unito.io/privacy/
- group: operate
  title: ''
  type: Contact
  url: https://unito.io/contact/
- group: operate
  title: ''
  type: StatusPage
  url: https://unitoio.statuspage.io/
- group: build
  title: ''
  type: Packages
  url: packages/unito-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/unito-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/unito-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/unito-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unito-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/unito-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://unito.io/security/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/unito-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unito-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/unito-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/unito-conventions.yml
- group: build
  title: ''
  type: CLI
  url: cli/unito-cli.yml
- group: design
  title: ''
  type: Components
  url: components/unito-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/unito-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/unito-connector-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Unito is a two-way sync and integration platform that keeps work items in sync across 60+ SaaS tools such as Asana, Jira, Trello, GitHub, Azure DevOps, ServiceNow, Salesforce, and Smartsheet, with no-code field mappings and rules. For developers Unito offers a Connector Developer Platform (TypeScript SDK + CLI for building two-way sync connectors), an embeddable Sync Embed iframe, and the Unito Embed API - a REST API for embedding partners to manage workspaces and pull flow and workspace usage reports. Unito is SOC 2 Type 2 certified and based in Montreal, Canada.
image: https://avatars.githubusercontent.com/u/13460182
layout: provider
mcp_servers:
- description: ''
  name: unito-mcp.yml
  slug: unito-mcpyml
modified: '2026-07-21'
name: Unito
nav: Providers
network: true
overview: 'Unito publishes 3 APIs on the [APIs.io](https://apis.io/) network: Reports API, Server API, and Workspaces API. Tagged areas include Integration, Two-Way Sync, Workflow Automation, Project Management, and Collaboration.


  The Unito catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Unito''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 28 more developer resources.'
random_paper: 67
score:
  band: strong
  composite: 57.3
  delta: -0.6
  facets:
    commercial_clarity: 60.5
    contract_quality: 58.2
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 28.9
  previous_composite: 57.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Unito Authentication
  slug: unito-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Unito Domain Security
  slug: unito-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Unito Trust Center
  slug: unito-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: unito
tags:
- Integration
- Two-Way Sync
- Workflow Automation
- Project Management
- Collaboration
- Embedded Integrations
- SaaS
website: https://unito.io
---
