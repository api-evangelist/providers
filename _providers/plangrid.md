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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'REST API for the PlanGrid construction productivity platform. Manage projects, annotations, comments, documents, photos, sheets and versions, snapshots, RFIs, submittal packages, field reports, tasks '
  name: PlanGrid API
  slug: plangrid-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://construction.autodesk.com/products/plangrid/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.plangrid.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.plangrid.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.plangrid.com/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.plangrid.com/reference/getting-started-1
- group: operate
  title: ''
  type: Support
  url: https://help.plangrid.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/plangrid
- group: auth
  title: ''
  type: Authentication
  url: authentication/plangrid-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/plangrid-scopes.yml
- group: build
  title: ''
  type: SDKs
  url: packages/plangrid-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/plangrid-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plangrid-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/plangrid-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/plangrid-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/plangrid-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/plangrid-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.plangrid.com/reference/api-versioning
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/plangrid-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/plangrid-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/plangrid-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plangrid-domain-security.yml
created: '2026-07-17'
description: PlanGrid is a construction productivity platform (now part of Autodesk Construction Cloud) that gives field and office teams access to construction drawings, sheets, documents, photos, RFIs, submittals, field reports, tasks, and punch lists on web and mobile. The PlanGrid API is a REST API served from io.plangrid.com that lets developers programmatically manage projects, annotations, comments, documents, photos, sheets and versions, snapshots, RFIs, submittal packages, field reports, tasks and task lists, roles, and project team users. It supports OAuth 2.0 (authorization code and implicit grants) as well as HTTP Basic API-key authentication, media-type versioning via the Accept header, cursor-based pagination, batch requests, and multi-step file upload workflows for PDFs, photos, and documents.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plangrid.png
layout: provider
mcp_servers:
- description: ''
  name: plangrid-mcp.yml
  slug: plangrid-mcpyml
modified: '2026-07-20'
name: PlanGrid
nav: Providers
network: true
overview: 'PlanGrid publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Construction, Construction Technology, and Project Management.


  PlanGrid''s developer surface includes documentation, API reference, getting-started guide, support, authentication, changelog, and 15 more developer resources.'
random_paper: 2
scopes:
- name: Plangrid Scopes
  scope_count: 2
  slug: plangrid-scopes
  summary_line: 2 scopes · authorizationCode/implicit
score:
  band: emerging
  composite: 23.5
  delta: -2.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 28.9
  previous_composite: 26.0
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Plangrid Authentication
  slug: plangrid-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Plangrid Domain Security
  slug: plangrid-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: plangrid
tags:
- Company
- Enterprise
- Construction
- Construction Technology
- Project Management
- Field Reports
- Documents
- RFIs
- REST API
- Autodesk
website: https://construction.autodesk.com/products/plangrid/
---
