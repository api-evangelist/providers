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
    well_known_catalog: false
  schema_version: 0.2
  score: 55.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 56
  human_in_the_loop: 0
  name: Indykite Agentic Access
  operation_count: 88
  slug: indykite-agentic-access
  summary_line: 88 operations · 56 acting
api_count: 21
apis:
- description: Application Agent Credential management
  name: Indykite Application Agent Credentials API
  slug: indykite-application-agent-credentials-api
- description: Application Agent CRUD operations
  name: Indykite Application Agents API
  slug: indykite-application-agents-api
- description: Application and agent management
  name: Indykite Applications API
  slug: indykite-applications-api
- description: KBAC and ContX IQ Policies CRUD operations
  name: Indykite Authorization Policies API
  slug: indykite-authorization-policies-api
- description: Authorization API implemented according to [AuthZEN specification](https://openid.net/wg/authzen/specifications/).
  name: Indykite AuthZEN API
  slug: indykite-authzen-api
- description: Capture REST API represents the service interface for data capture.
  name: Indykite Capture API
  slug: indykite-capture-api
- description: ContX IQ API supports CRUD operations on IKG which cooperates with authorization engine.
  name: Indykite ContX IQ API
  slug: indykite-contx-iq-api
- description: DataSchema enables customers to define their own data models within the Identity Knowledge Graph (IKG)
  name: Indykite DataSchema API
  slug: indykite-dataschema-api
- description: The Deprecated API from Indykite — 2 operation(s) for deprecated.
  name: Indykite Deprecated API
  slug: indykite-deprecated-api
- description: Entity Matching Pipeline configuration
  name: Indykite Entity Matching API
  slug: indykite-entity-matching-api
- description: The EntityMatching API from Indykite — 3 operation(s) for entitymatching.
  name: Indykite EntityMatching API
  slug: indykite-entitymatching-api
- description: Event Sink configuration
  name: Indykite Event Sinks API
  slug: indykite-event-sinks-api
- description: External Data Resolver configuration
  name: Indykite External Data Resolver API
  slug: indykite-external-data-resolver-api
- description: Knowledge Query management
  name: Indykite Knowledge Queries API
  slug: indykite-knowledge-queries-api
- description: MCP Servers configuration
  name: Indykite MCP Servers API
  slug: indykite-mcp-servers-api
- description: Organization operations
  name: Indykite Organizations API
  slug: indykite-organizations-api
- description: Project CRUD operations
  name: Indykite Projects API
  slug: indykite-projects-api
- description: Service Account Credential management
  name: Indykite Service Account Credentials API
  slug: indykite-service-account-credentials-api
- description: Service Account CRUD operations
  name: Indykite Service Accounts API
  slug: indykite-service-accounts-api
- description: Token introspection configuration
  name: Indykite Token Introspect API
  slug: indykite-token-introspect-api
- description: Trust Score Profile management
  name: Indykite Trust Score API
  slug: indykite-trust-score-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Upsert nodes and a relationship into the Identity Knowledge Graph, then ask AuthZEN/KBAC whether a subject may act on a resource.
  name: Capture graph data then make an authorization decision
  slug: indykite-capture-and-authorize
- description: Create a project, an application and an application agent, then mint an AppAgent credential for data-plane calls.
  name: Provision an IndyKite project and AppAgent credential
  slug: indykite-provision-project-appagent
artifact_total: 31
asyncapis:
- description: ''
  name: Indykite Event Sinks Webhooks
  slug: indykite-event-sinks-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/indykite-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/indykite-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/indykite-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.indykite.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.indykite.com/
- group: docs
  title: ''
  type: APIReference
  url: https://openapi.indykite.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.indykite.com/docs/get-started
- group: operate
  title: ''
  type: Support
  url: https://forum.indykite.com/
- group: company
  title: ''
  type: Blog
  url: https://www.indykite.ai/blog/all
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/indykite
- group: start
  title: ''
  type: SignUp
  url: https://us.hub.indykite.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.indykite.ai/subscription-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.indykite.ai/privacy
- group: start
  title: ''
  type: Sandbox
  url: https://us.hub.indykite.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/indykite-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/indykite-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/indykite-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/indykite-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/indykite-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/indykite-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/indykite-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.indykite.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/indykite-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/indykite-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.indykite.ai/responsible-disclosure-policy
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/indykite-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/indykite-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/indykite-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/indykite-event-sinks-webhooks.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/indykite-provision-project-appagent.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/indykite-capture-and-authorize.yml
created: '2026-07-17'
description: IndyKite is the runtime control layer for agentic AI. Its enterprise platform applies trust, context, and runtime control across organizational data so autonomous AI agents can act securely, continuously injecting live signals — identity, provenance, freshness, sensitivity, and compliance status — into AI actions and access decisions at the moment they occur. The platform is built on an Identity Knowledge Graph (IKG) and delivers Knowledge-Based Access Control (KBAC), AuthZEN-based authorization, ContX IQ contextual queries, entity matching, and a hosted regional Model Context Protocol (MCP) server. IndyKite exposes a REST API (Capture, DataSchema, ContX IQ, AuthZEN, Entity Matching) and a Config API for managing organizations, projects, applications, app agents, service accounts, authorization policies, knowledge queries, event sinks, and MCP servers, plus a Go SDK and a Terraform provider. Added to the API Evangelist network via the speedinvest portfolio and enriched from
  the provider's public OpenAPI and documentation.
image: https://docs.indykite.com/img/indykite.svg
layout: provider
mcp_servers:
- description: ''
  name: indykite-mcp.yml
  slug: indykite-mcpyml
modified: '2026-07-19'
name: Indykite
nav: Providers
network: true
overview: 'Indykite publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Application Agent Credentials API, Application Agents API, Applications API, and 18 more. Tagged areas include Company, Identity, Authorization, Access Control, and Knowledge Graph.


  The Indykite catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Indykite''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 25 more developer resources.'
random_paper: 55
score:
  band: strong
  composite: 58.0
  delta: 0.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 64.4
    developer_ergonomics: 80.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 39.5
  previous_composite: 57.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/indykite/refs/heads/main/screenshots/indykite-2026-07-25T222343.png
security:
- kind: authentication
  name: Indykite Authentication
  slug: indykite-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Indykite Domain Security
  slug: indykite-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Indykite Vulnerability Disclosure
  slug: indykite-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Indykite Trust Center
  slug: indykite-trust-center
  summary_line: SOC 2 Type I, SOC 2 Type II, ISO 27001, HIPAA, GDPR, EU-U.S. Data Privacy Framework
slug: indykite
tags:
- Company
- Identity
- Authorization
- Access Control
- Knowledge Graph
- Agentic AI
- MCP
- Security
- AuthZEN
website: https://developer.indykite.com/
---
