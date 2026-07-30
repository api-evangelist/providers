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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.4
  scored_at: '2026-07-28'
api_count: 16
apis:
- description: The accessManagement API from Atomicwork — 8 operation(s) for accessmanagement.
  name: Atomicwork accessManagement API
  slug: atomicwork-accessmanagement-api
- description: The agentGroups API from Atomicwork — 3 operation(s) for agentgroups.
  name: Atomicwork agentGroups API
  slug: atomicwork-agentgroups-api
- description: The assets API from Atomicwork — 7 operation(s) for assets.
  name: Atomicwork assets API
  slug: atomicwork-assets-api
- description: The auditLogs API from Atomicwork — 3 operation(s) for auditlogs.
  name: Atomicwork auditLogs API
  slug: atomicwork-auditlogs-api
- description: The businessHourConfig API from Atomicwork — 2 operation(s) for businesshourconfig.
  name: Atomicwork businessHourConfig API
  slug: atomicwork-businesshourconfig-api
- description: The changeManagement API from Atomicwork — 7 operation(s) for changemanagement.
  name: Atomicwork changeManagement API
  slug: atomicwork-changemanagement-api
- description: The customObjects API from Atomicwork — 7 operation(s) for customobjects.
  name: Atomicwork customObjects API
  slug: atomicwork-customobjects-api
- description: The entities API from Atomicwork — 1 operation(s) for entities.
  name: Atomicwork entities API
  slug: atomicwork-entities-api
- description: The forms API from Atomicwork — 5 operation(s) for forms.
  name: Atomicwork forms API
  slug: atomicwork-forms-api
- description: The problems API from Atomicwork — 4 operation(s) for problems.
  name: Atomicwork problems API
  slug: atomicwork-problems-api
- description: The requests API from Atomicwork — 19 operation(s) for requests.
  name: Atomicwork requests API
  slug: atomicwork-requests-api
- description: The serviceCatalog API from Atomicwork — 7 operation(s) for servicecatalog.
  name: Atomicwork serviceCatalog API
  slug: atomicwork-servicecatalog-api
- description: The tags API from Atomicwork — 2 operation(s) for tags.
  name: Atomicwork tags API
  slug: atomicwork-tags-api
- description: The users API from Atomicwork — 10 operation(s) for users.
  name: Atomicwork users API
  slug: atomicwork-users-api
- description: The workflows API from Atomicwork — 14 operation(s) for workflows.
  name: Atomicwork workflows API
  slug: atomicwork-workflows-api
- description: The workspaces API from Atomicwork — 3 operation(s) for workspaces.
  name: Atomicwork workspaces API
  slug: atomicwork-workspaces-api
artifact_total: 21
common:
- group: company
  title: ''
  type: Website
  url: https://www.atomicwork.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.atomicwork.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.atomicwork.com
- group: docs
  title: ''
  type: APIReference
  url: https://developers.atomicwork.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.atomicwork.com/api-reference/introduction
- group: company
  title: ''
  type: Blog
  url: https://www.atomicwork.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.atomicwork.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.atomicwork.com
- group: start
  title: ''
  type: Login
  url: https://app.atomicwork.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atomicwork.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atomicwork.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.atomicwork.com
- group: auth
  title: ''
  type: Security
  url: https://www.atomicwork.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://trust.atomicwork.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/atomicwork-public-api-openapi.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/atomicwork-public-api-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://developers.atomicwork.com/_mcp/server
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/atomicwork-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.atomicwork.com/llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/atomicwork-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/atomicwork-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/atomicwork-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/atomicwork-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/atomicwork-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/atomicwork-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/atomicwork-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atomicwork-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/atomicwork-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/atomicwork-trust-center.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Atomicwork is an agentic service management (ITSM/ESM) platform that pairs an AI "coworker" (Atom) with a modern service desk for IT, HR, and other enterprise teams. The Atomicwork Public API gives programmatic, workspace-scoped access to the core platform — requests and tickets (incidents, service requests, problems, changes, major incidents), assets and a CMDB, users and workspaces, service catalog, automation workflows, custom objects, audit logs, and identity governance (IGA) grants and entitlements. Authentication is via a workspace-scoped API key (X-Api-Key) with an X-Workspace-Id scoping header. Atomicwork also ships an official hosted MCP server so AI clients (Claude, Cursor, Copilot, Codex) can drive the same operations as tools. The API is documented as OpenAPI 3.1 with 102 paths across 16 tags, offset and cursor pagination, and a structured filter model.
image: https://cdn.prod.website-files.com/64f08da4e7effe6dcb06d456/6a101caaa06c458154ef693c_Logomark.png
layout: provider
mcp_servers:
- description: ''
  name: server
  slug: server
modified: '2026-07-18'
name: Atomicwork
nav: Providers
network: true
overview: 'Atomicwork publishes 16 APIs on the [APIs.io](https://apis.io/) network, including accessManagement API, agentGroups API, assets API, and 13 more. Tagged areas include Company, Service Management, ITSM, ESM, and IT Service Desk.


  Atomicwork''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 23 more developer resources.'
random_paper: 22
score:
  band: developing
  composite: 50.7
  delta: 1.4
  facets:
    commercial_clarity: 60.5
    contract_quality: 47.2
    developer_ergonomics: 58.2
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 26.3
  previous_composite: 49.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/atomicwork/refs/heads/main/screenshots/atomicwork-2026-07-25T201615.png
security:
- kind: authentication
  name: Atomicwork Authentication
  slug: atomicwork-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Atomicwork Domain Security
  slug: atomicwork-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Atomicwork Vulnerability Disclosure
  slug: atomicwork-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Atomicwork Trust Center
  slug: atomicwork-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2, ISO 27001, ISO 27017, ISO 27018, ISO 27701, ISO 42001, HIPAA, GDPR, CCPA, CSA STAR Level 1, Microsoft 365 Certification, CASA Tier 3
slug: atomicwork
tags:
- Company
- Service Management
- ITSM
- ESM
- IT Service Desk
- Identity Governance
- Asset Management
- AI Agents
- MCP
- Enterprise
website: https://www.atomicwork.com
---
