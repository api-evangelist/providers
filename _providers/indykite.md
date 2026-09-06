---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 56
  human_in_the_loop: 0
  name: Indykite Agentic Access
  operation_count: 88
  slug: indykite-agentic-access
  summary_line: 88 operations · 56 acting
api_count: 2
apis:
- baseURL: https://us.api.indykite.com
  baseurl_source: declared
  description: Application Agent Credential management
  name: Indykite Application Agent Credentials API
  slug: indykite-application-agent-credentials-api
- baseURL: https://us.api.indykite.com
  baseurl_source: declared
  description: Application Agent CRUD operations
  name: Indykite Application Agents API
  slug: indykite-application-agents-api
- baseURL: https://us.api.indykite.com
  baseurl_source: declared
  description: Application and agent management
  name: Indykite Applications API
  slug: indykite-applications-api
- baseURL: https://us.api.indykite.com
  baseurl_source: declared
  description: KBAC and ContX IQ Policies CRUD operations
  name: Indykite Authorization Policies API
  slug: indykite-authorization-policies-api
- baseURL: https://us.api.indykite.com
  baseurl_source: declared
  description: Authorization API implemented according to [AuthZEN specification](https://openid.net/wg/authzen/specifications/).
  name: Indykite AuthZEN API
  slug: indykite-authzen-api
- baseURL: https://us.api.indykite.com
  baseurl_source: declared
  description: Capture REST API represents the service interface for data capture.
  name: Indykite Capture API
  slug: indykite-capture-api
- baseURL: https://us.api.indykite.com
  baseurl_source: declared
  description: ContX IQ API supports CRUD operations on IKG which cooperates with authorization engine.
  name: Indykite ContX IQ API
  slug: indykite-contx-iq-api
- baseURL: https://us.api.indykite.com
  baseurl_source: declared
  description: DataSchema enables customers to define their own data models within the Identity Knowledge Graph (IKG)
  name: Indykite DataSchema API
  slug: indykite-dataschema-api
- baseURL: https://us.api.indykite.com
  baseurl_source: declared
  description: The Deprecated API from Indykite — 2 operation(s) for deprecated.
  name: Indykite Deprecated API
  slug: indykite-deprecated-api
- baseURL: https://us.api.indykite.com
  baseurl_source: declared
  description: Entity Matching Pipeline configuration
  name: Indykite Entity Matching API
  slug: indykite-entity-matching-api
- baseURL: https://us.api.indykite.com
  baseurl_source: declared
  description: The EntityMatching API from Indykite — 3 operation(s) for entitymatching.
  name: Indykite EntityMatching API
  slug: indykite-entitymatching-api
- baseURL: https://us.api.indykite.com
  baseurl_source: declared
  description: Event Sink configuration
  name: Indykite Event Sinks API
  slug: indykite-event-sinks-api
- baseURL: https://us.api.indykite.com
  baseurl_source: declared
  description: External Data Resolver configuration
  name: Indykite External Data Resolver API
  slug: indykite-external-data-resolver-api
- baseURL: https://us.api.indykite.com
  baseurl_source: declared
  description: Knowledge Query management
  name: Indykite Knowledge Queries API
  slug: indykite-knowledge-queries-api
- baseURL: https://us.api.indykite.com
  baseurl_source: declared
  description: MCP Servers configuration
  name: Indykite MCP Servers API
  slug: indykite-mcp-servers-api
- baseURL: https://us.api.indykite.com
  baseurl_source: declared
  description: Organization operations
  name: Indykite Organizations API
  slug: indykite-organizations-api
- baseURL: https://us.api.indykite.com
  baseurl_source: declared
  description: Project CRUD operations
  name: Indykite Projects API
  slug: indykite-projects-api
- baseURL: https://us.api.indykite.com
  baseurl_source: declared
  description: Service Account Credential management
  name: Indykite Service Account Credentials API
  slug: indykite-service-account-credentials-api
- baseURL: https://us.api.indykite.com
  baseurl_source: declared
  description: Service Account CRUD operations
  name: Indykite Service Accounts API
  slug: indykite-service-accounts-api
- baseURL: https://us.api.indykite.com
  baseurl_source: declared
  description: Token introspection configuration
  name: Indykite Token Introspect API
  slug: indykite-token-introspect-api
- baseURL: https://us.api.indykite.com
  baseurl_source: declared
  description: Trust Score Profile management
  name: Indykite Trust Score API
  slug: indykite-trust-score-api
arazzos:
- description: Upsert nodes and a relationship into the Identity Knowledge Graph, then ask AuthZEN/KBAC whether a subject may act on a resource.
  name: Capture graph data then make an authorization decision
  slug: indykite-capture-and-authorize
- description: Create a project, an application and an application agent, then mint an AppAgent credential for data-plane calls.
  name: Provision an IndyKite project and AppAgent credential
  slug: indykite-provision-project-appagent
artifact_total: 52
asyncapis:
- description: ''
  name: Indykite Event Sinks Webhooks
  slug: indykite-event-sinks-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Config REST Application Agent Credentials API
  slug: open-indykite-application-agent-credentials-api
- collection_type: open
  name: Config REST Application Agent Credentials Application Agents API
  slug: open-indykite-application-agents-api
- collection_type: open
  name: Config REST Application Agent Credentials Applications API
  slug: open-indykite-applications-api
- collection_type: open
  name: Config REST Application Agent Credentials Authorization Policies API
  slug: open-indykite-authorization-policies-api
- collection_type: open
  name: Config REST Application Agent Credentials AuthZEN API
  slug: open-indykite-authzen-api
- collection_type: open
  name: Config REST Application Agent Credentials Capture API
  slug: open-indykite-capture-api
- collection_type: open
  name: Config REST Application Agent Credentials ContX IQ API
  slug: open-indykite-contx-iq-api
- collection_type: open
  name: Config REST Application Agent Credentials DataSchema API
  slug: open-indykite-dataschema-api
- collection_type: open
  name: Config REST Application Agent Credentials Deprecated API
  slug: open-indykite-deprecated-api
- collection_type: open
  name: Config REST Application Agent Credentials Entity Matching API
  slug: open-indykite-entity-matching-api
- collection_type: open
  name: Config REST Application Agent Credentials EntityMatching API
  slug: open-indykite-entitymatching-api
- collection_type: open
  name: Config REST Application Agent Credentials Event Sinks API
  slug: open-indykite-event-sinks-api
- collection_type: open
  name: Config REST Application Agent Credentials External Data Resolver API
  slug: open-indykite-external-data-resolver-api
- collection_type: open
  name: Config REST Application Agent Credentials Knowledge Queries API
  slug: open-indykite-knowledge-queries-api
- collection_type: open
  name: Config REST Application Agent Credentials MCP Servers API
  slug: open-indykite-mcp-servers-api
- collection_type: open
  name: Config REST Application Agent Credentials Organizations API
  slug: open-indykite-organizations-api
- collection_type: open
  name: Config REST Application Agent Credentials Projects API
  slug: open-indykite-projects-api
- collection_type: open
  name: Config REST Application Agent Credentials Service Account Credentials API
  slug: open-indykite-service-account-credentials-api
- collection_type: open
  name: Config REST Application Agent Credentials Service Accounts API
  slug: open-indykite-service-accounts-api
- collection_type: open
  name: Config REST Application Agent Credentials Token Introspect API
  slug: open-indykite-token-introspect-api
- collection_type: open
  name: Config REST Application Agent Credentials Trust Score API
  slug: open-indykite-trust-score-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/indykite-config-overlay.yaml
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
  name: Indykite MCP Server
  slug: indykite-mcp-server
modified: '2026-07-19'
name: Indykite
nav: Providers
network: true
overview: 'Indykite publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Application Agent Credentials API, Application Agents API, Applications API, and 18 more. Tagged areas include Company, Identity, Authorization, Access Control, and Knowledge Graph.


  The Indykite catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Indykite''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 26 more developer resources.'
random_paper: 4
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 4.5
    contract_quality: 67.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 36.8
  previous_composite: 47.0
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
