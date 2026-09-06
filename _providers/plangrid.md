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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'REST API for the PlanGrid construction productivity platform. Manage projects, annotations, comments, documents, photos, sheets and versions, snapshots, RFIs, submittal packages, field reports, tasks '
  name: PlanGrid API
  slug: plangrid-api
artifact_total: 4
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
  type: X-MCPServerCandidate
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
modified: '2026-07-20'
name: PlanGrid
nav: Providers
network: true
overview: 'PlanGrid publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Construction, Construction Technology, and Project Management.


  PlanGrid''s developer surface includes documentation, API reference, getting-started guide, support, authentication, changelog, and 15 more developer resources.'
random_paper: 9
scopes:
- name: Plangrid Scopes
  scope_count: 2
  slug: plangrid-scopes
  summary_line: 2 scopes · authorizationCode/implicit
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 22.4
  previous_composite: 19.6
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plangrid/refs/heads/main/screenshots/plangrid-2026-09-02T151414.png
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
