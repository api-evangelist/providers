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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 69.2
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Newforma Agentic Access
  operation_count: 39
  slug: newforma-agentic-access
  summary_line: 39 operations · 19 acting
api_count: 4
apis:
- description: buildingSMART BIM Collaboration Format (BCF) REST API for exchanging coordination issues and topics between Newforma Konekt and third-party BIM authoring/coordination tools, plus a BCF Server.
  name: Newforma Konekt BCF REST API
  slug: newforma-konekt-bcf-rest-api
- description: The Hub API from Newforma — 7 operation(s) for hub.
  name: Newforma Hub API
  slug: newforma-hub-api
- description: The Issue API from Newforma — 17 operation(s) for issue.
  name: Newforma Issue API
  slug: newforma-issue-api
- description: The Project API from Newforma — 4 operation(s) for project.
  name: Newforma Project API
  slug: newforma-project-api
artifact_total: 9
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bimtrackapis.readme.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://konekt.help.newforma.com/4408494681869-integrations-api/
- group: docs
  title: ''
  type: APIReference
  url: https://bimtrackapis.readme.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://konekt.help.newforma.com/4408494681869-integrations-api/360008491831-api/
- group: operate
  title: ''
  type: Support
  url: https://help.newforma.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.newforma.com/newforma-api/
- group: company
  title: ''
  type: Website
  url: https://www.newforma.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bimtrack.co/
- group: operate
  title: ''
  type: ChangeLog
  url: https://bimtrackapis.readme.io/changelog
- group: operate
  title: ''
  type: Deprecation
  url: https://konekt.help.newforma.com/4408494681869-integrations-api/360008491831-api/360041452712-newforma-konekt-rest-api/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/newforma-konekt-openapi-original.json
- group: auth
  title: ''
  type: DomainSecurity
  url: security/newforma-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/newforma-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/newforma-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/newforma-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/newforma-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/newforma-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/newforma-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/newforma-konekt-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/newforma-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/newforma-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/newforma-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/newforma-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/newforma-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/newforma-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Newforma builds project information management software for the architecture, engineering, and construction (AEC) industry. Its cloud platform Newforma Konekt (formerly BIM Track by BIM One) exposes a REST API and a buildingSMART BCF REST API for BIM coordination — managing hubs, projects, and issues along with their viewpoints, attachments, comments, history, sheets, models, and users. Integrations authenticate with OAuth 2.0 / OpenID Connect (PKCE) or a Hub-owner API access token. Newforma also ships the on-premises Project Center and the cloud ConstructEx products.
image: https://www.newforma.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: newforma-mcp.yml
  slug: newforma-mcpyml
modified: '2026-07-20'
name: Newforma
nav: Providers
network: true
overview: 'Newforma publishes 3 APIs on the [APIs.io](https://apis.io/) network: Hub API, Issue API, and Project API. Tagged areas include Company, AEC, Construction, Architecture, and Engineering.


  Newforma''s developer surface includes documentation, API reference, getting-started guide, support, changelog, authentication, sandbox, and 19 more developer resources.'
random_paper: 47
scopes:
- name: Newforma Scopes
  scope_count: 14
  slug: newforma-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 40.8
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 36.7
    developer_ergonomics: 71.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 40.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Newforma Authentication
  slug: newforma-authentication
  summary_line: oauth2/openIdConnect/apiKey · 3 schemes
- kind: domain-security
  name: Newforma Domain Security
  slug: newforma-domain-security
  summary_line: TLSv1.3 · DMARC
slug: newforma
tags:
- Company
- AEC
- Construction
- Architecture
- Engineering
- BIM
- Building Information Modeling
- Project Management
- Issue Tracking
- Collaboration
website: https://www.newforma.com/
---
