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
    agent_card: false
    agent_skills: derived
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://app.coordinatehq.com/api/v1
  baseurl_source: declared
  description: Discussion entries on projects, tasks, and goals.
  name: Coordinate Comments API
  slug: coordinate-comments-api
- baseURL: https://app.coordinatehq.com/api/v1
  baseurl_source: declared
  description: Cross-entity bulk export firehose.
  name: Coordinate Entity API
  slug: coordinate-entity-api
- baseURL: https://app.coordinatehq.com/api/v1
  baseurl_source: declared
  description: Project goals / milestones with target dates.
  name: Coordinate Goals API
  slug: coordinate-goals-api
- baseURL: https://app.coordinatehq.com/api/v1
  baseurl_source: declared
  description: Task groups (internally "Milestone").
  name: Coordinate Groups API
  slug: coordinate-groups-api
- baseURL: https://app.coordinatehq.com/api/v1
  baseurl_source: declared
  description: Customer organizations linking projects and stakeholders.
  name: Coordinate Organizations API
  slug: coordinate-organizations-api
- baseURL: https://app.coordinatehq.com/api/v1
  baseurl_source: declared
  description: Read-only progress reports on a project.
  name: Coordinate Progress Reports API
  slug: coordinate-progress-reports-api
- baseURL: https://app.coordinatehq.com/api/v1
  baseurl_source: declared
  description: Rich-text pages attached to a project.
  name: Coordinate Project Pages API
  slug: coordinate-project-pages-api
- baseURL: https://app.coordinatehq.com/api/v1
  baseurl_source: declared
  description: Client projects (internally "Customer").
  name: Coordinate Projects API
  slug: coordinate-projects-api
- baseURL: https://app.coordinatehq.com/api/v1
  baseurl_source: declared
  description: Client-side collaborators on a project.
  name: Coordinate Stakeholders API
  slug: coordinate-stakeholders-api
- baseURL: https://app.coordinatehq.com/api/v1
  baseurl_source: declared
  description: Per-vendor JSON scratch storage.
  name: Coordinate Storage API
  slug: coordinate-storage-api
- baseURL: https://app.coordinatehq.com/api/v1
  baseurl_source: declared
  description: Tasks within a project.
  name: Coordinate Tasks API
  slug: coordinate-tasks-api
- baseURL: https://app.coordinatehq.com/api/v1
  baseurl_source: declared
  description: Vendor users.
  name: Coordinate Users API
  slug: coordinate-users-api
- baseURL: https://app.coordinatehq.com/api/v1
  baseurl_source: declared
  description: Webhook subscription management.
  name: Coordinate Webhooks API
  slug: coordinate-webhooks-api
- baseURL: https://app.coordinatehq.com/api/v1
  baseurl_source: declared
  description: The Coordinate REST API API from Coordinate — 0 operation(s) for coordinate rest api.
  name: Coordinate Coordinate REST API
  slug: coordinate-coordinate-rest-api-api
artifact_total: 32
asyncapis:
- description: ''
  name: Coordinate Webhooks
  slug: coordinate-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Coordinate REST Comments API
  slug: open-coordinate-comments-api
- collection_type: open
  name: Coordinate REST Comments Entity API
  slug: open-coordinate-entity-api
- collection_type: open
  name: Coordinate REST Comments Goals API
  slug: open-coordinate-goals-api
- collection_type: open
  name: Coordinate REST Comments Groups API
  slug: open-coordinate-groups-api
- collection_type: open
  name: Coordinate REST Comments Organizations API
  slug: open-coordinate-organizations-api
- collection_type: open
  name: Coordinate REST Comments Progress Reports API
  slug: open-coordinate-progress-reports-api
- collection_type: open
  name: Coordinate REST Comments Project Pages API
  slug: open-coordinate-project-pages-api
- collection_type: open
  name: Coordinate REST Comments Projects API
  slug: open-coordinate-projects-api
- collection_type: open
  name: Coordinate REST Comments Stakeholders API
  slug: open-coordinate-stakeholders-api
- collection_type: open
  name: Coordinate REST Comments Storage API
  slug: open-coordinate-storage-api
- collection_type: open
  name: Coordinate REST Comments Tasks API
  slug: open-coordinate-tasks-api
- collection_type: open
  name: Coordinate REST Comments Users API
  slug: open-coordinate-users-api
- collection_type: open
  name: Coordinate REST Comments Webhooks API
  slug: open-coordinate-webhooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/coordinate-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://coordinatehq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.coordinatehq.com/static/API_Documentation.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.coordinatehq.com/library/integrating-with-coordinate
- group: docs
  title: ''
  type: APIReference
  url: https://app.coordinatehq.com/static/API_Documentation.html
- group: operate
  title: ''
  type: Support
  url: https://coordinatehqhelp.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.coordinatehq.com/library
- group: commercial
  title: ''
  type: Pricing
  url: https://coordinatehq.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.coordinatehq.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.coordinatehq.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coordinatehq.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coordinatehq.com/legal/privacy-policy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/coordinate-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coordinate-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coordinate-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/coordinate-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coordinate-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/coordinate-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coordinate-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/coordinate-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/coordinate-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coordinate-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/coordinate-openapi-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/coordinate-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coordinate-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Coordinate (CoordinateHQ) is a client project-execution platform and branded client portal for client-facing businesses — agencies, professional services, and B2B onboarding teams. It turns repeatable workflows into automated, interactive projects with tasks, task groups, goals, progress reports, forms, eSignatures, time tracking, and in-project chat, while giving each client a simple password-free portal. Coordinate exposes a REST API (base https://app.coordinatehq.com/api/v1) for creating and syncing projects, tasks, groups, stakeholders, goals, comments, and organizations, an /entity export firehose for bulk sync, and a webhook API for real-time create/update events, alongside bi-directional Zapier integrations. This profile was enriched by the API Evangelist pipeline from Coordinate's published API reference.
image: https://cdn.prod.website-files.com/639cbe2ae16424db11366965/68c4925a9be35099761c7e7a_coordinatehq-opengraph-sept-2025.jpg
layout: provider
mcp_servers:
- description: ''
  name: Coordinate MCP Server
  slug: coordinate-mcp-server
modified: '2026-07-18'
name: Coordinate
nav: Providers
network: true
overview: 'Coordinate publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Entity API, Goals API, and 11 more. Tagged areas include Company, Enterprise Saas, Project Management, Client Portal, and Client Onboarding.


  The Coordinate catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Coordinate''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 19 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 60.1
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 42.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coordinate/refs/heads/main/screenshots/coordinate-2026-07-25T210404.png
security:
- kind: authentication
  name: Coordinate Authentication
  slug: coordinate-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Coordinate Domain Security
  slug: coordinate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coordinate
tags:
- Company
- Enterprise Saas
- Project Management
- Client Portal
- Client Onboarding
- Professional Services
- Workflow-Automation
- Collaboration
- Webhook
website: https://coordinatehq.com/
---
