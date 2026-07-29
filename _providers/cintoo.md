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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 63
  human_in_the_loop: 0
  name: Cintoo Agentic Access
  operation_count: 100
  slug: cintoo-agentic-access
  summary_line: 100 operations · 63 acting
api_count: 21
apis:
- description: The Account API from Cintoo — 4 operation(s) for account.
  name: Cintoo Account API
  slug: cintoo-account-api
- description: The Annotation API from Cintoo — 3 operation(s) for annotation.
  name: Cintoo Annotation API
  slug: cintoo-annotation-api
- description: The Autodesk API from Cintoo — 3 operation(s) for autodesk.
  name: Cintoo Autodesk API
  slug: cintoo-autodesk-api
- description: The Crop API from Cintoo — 3 operation(s) for crop.
  name: Cintoo Crop API
  slug: cintoo-crop-api
- description: The Export Scene API from Cintoo — 1 operation(s) for export scene.
  name: Cintoo Export Scene API
  slug: cintoo-export-scene-api
- description: The File API from Cintoo — 7 operation(s) for file.
  name: Cintoo File API
  slug: cintoo-file-api
- description: The Group API from Cintoo — 3 operation(s) for group.
  name: Cintoo Group API
  slug: cintoo-group-api
- description: The Integrations API from Cintoo — 3 operation(s) for integrations.
  name: Cintoo Integrations API
  slug: cintoo-integrations-api
- description: The Konekt API from Cintoo — 4 operation(s) for konekt.
  name: Cintoo Konekt API
  slug: cintoo-konekt-api
- description: The Measurement API from Cintoo — 1 operation(s) for measurement.
  name: Cintoo Measurement API
  slug: cintoo-measurement-api
- description: The Members API from Cintoo — 4 operation(s) for members.
  name: Cintoo Members API
  slug: cintoo-members-api
- description: The Permissions API from Cintoo — 1 operation(s) for permissions.
  name: Cintoo Permissions API
  slug: cintoo-permissions-api
- description: The Project API from Cintoo — 5 operation(s) for project.
  name: Cintoo Project API
  slug: cintoo-project-api
- description: The Role API from Cintoo — 2 operation(s) for role.
  name: Cintoo Role API
  slug: cintoo-role-api
- description: The Share Link API from Cintoo — 2 operation(s) for share link.
  name: Cintoo Share Link API
  slug: cintoo-share-link-api
- description: The Subscription API from Cintoo — 2 operation(s) for subscription.
  name: Cintoo Subscription API
  slug: cintoo-subscription-api
- description: The Tag API from Cintoo — 3 operation(s) for tag.
  name: Cintoo Tag API
  slug: cintoo-tag-api
- description: The Tag List API from Cintoo — 7 operation(s) for tag list.
  name: Cintoo Tag List API
  slug: cintoo-tag-list-api
- description: The Usage Report API from Cintoo — 1 operation(s) for usage report.
  name: Cintoo Usage Report API
  slug: cintoo-usage-report-api
- description: The User API from Cintoo — 3 operation(s) for user.
  name: Cintoo User API
  slug: cintoo-user-api
- description: The Workzone API from Cintoo — 3 operation(s) for workzone.
  name: Cintoo Workzone API
  slug: cintoo-workzone-api
artifact_total: 26
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aec.cintoo.com/api/2
- group: docs
  title: ''
  type: Documentation
  url: https://aec.cintoo.com/api/2
- group: operate
  title: ''
  type: Support
  url: https://help.cintoo.com/en/support/home
- group: company
  title: ''
  type: Blog
  url: https://cintoo.com/en/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cintoo.com/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cintoo.com/en/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://cintoo.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/cintoo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cintoo-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cintoo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cintoo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cintoo-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cintoo-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cintoo-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cintoo-sandbox.yml
- group: build
  title: ''
  type: CLI
  url: cli/cintoo-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cintoo-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cintoo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cintoo-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cintoo-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Cintoo is a cloud-based reality-capture and digital-twin platform that transforms 3D laser-scan point-cloud data into high-fidelity, streamable 3D meshes hosted in the cloud. Teams across AEC (architecture, engineering, construction), BIM, GIS, and asset management use Cintoo Cloud to store, visualize, classify, annotate, measure, and share reality-capture data, and to run scan-to-BIM and digital-twin workflows. The Cintoo Open API 2.0.0 (OpenAPI 3.0.3, currently beta) exposes 100 operations across accounts, subscriptions, users, groups, roles, projects, work zones, files, annotations, crops, measurements, tags, share links, and integrations (Autodesk, Konekt), secured with OAuth2 authorization-code and JWT Bearer tokens. Cintoo was surfaced as a portfolio company of Partech and enriched from its public developer surface by the API Evangelist pipeline.
image: https://cintoo.com/hubfs/Cintoo/images/cintoo-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: cintoo-mcp.yml
  slug: cintoo-mcpyml
modified: '2026-07-18'
name: Cintoo
nav: Providers
network: true
overview: 'Cintoo publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Account API, Annotation API, Autodesk API, and 18 more. Tagged areas include Company, Infrastructure SaaS, Reality Capture, Digital Twin, and Point Cloud.


  Cintoo''s developer surface includes documentation, support, engineering blog, authentication, sandbox, CLI, and 15 more developer resources.'
random_paper: 36
scopes:
- name: Cintoo Scopes
  scope_count: 0
  slug: cintoo-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.3
  delta: -3.9
  facets:
    commercial_clarity: 21.1
    contract_quality: 48.9
    developer_ergonomics: 51.6
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 40.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cintoo/refs/heads/main/screenshots/cintoo-2026-07-25T205406.png
security:
- kind: authentication
  name: Cintoo Authentication
  slug: cintoo-authentication
  summary_line: oauth2/http-bearer-jwt · 1 scheme
- kind: domain-security
  name: Cintoo Domain Security
  slug: cintoo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cintoo
tags:
- Company
- Infrastructure SaaS
- Reality Capture
- Digital Twin
- Point Cloud
- 3D
- AEC
- BIM
- Construction
- Scan-to-BIM
- GIS
website: https://cintoo.com
---
