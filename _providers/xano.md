---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Xano Agentic Access
  operation_count: 37
  slug: xano-agentic-access
  summary_line: 37 operations · 21 acting
api_count: 7
apis:
- description: The REST APIs that Xano users build visually. Each API group is served at its own /api:{token} path on the instance and auto-generates its own OpenAPI/Swagger document; surface, paths, and auth are de
  name: Xano Generated User APIs
  slug: xano-generated-user-apis
- description: API groups, their endpoints, and generated OpenAPI.
  name: Xano API Groups API
  slug: xano-api-groups-api
- description: Authenticated user and accessible workspaces.
  name: Xano Auth API
  slug: xano-auth-api
- description: Table records (database content) CRUD and search.
  name: Xano Content API
  slug: xano-content-api
- description: Workspace file library.
  name: Xano Files API
  slug: xano-files-api
- description: Database tables, schema, and indexes.
  name: Xano Tables API
  slug: xano-tables-api
- description: Workspace details, branches, import/export.
  name: Xano Workspace API
  slug: xano-workspace-api
artifact_total: 16
collections:
- collection_type: open
  name: Xano Metadata API
  slug: open-xano
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/xano-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/xano-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/xano-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xano-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/xano-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xano-inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xano
- group: company
  title: ''
  type: Website
  url: https://www.xano.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.xano.com
- group: commercial
  title: ''
  type: Plans
  url: plans/xano-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/xano-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/xano-finops.yml
created: '2026-06-20'
description: Xano is a no-code backend / backend-as-a-service that lets users visually build production REST APIs backed by a managed PostgreSQL database and serverless functions. Each workspace auto-generates its own OpenAPI/Swagger for the user-built API groups, and a separate per-instance Metadata API lets you manage tables, schema, records, files, and branches programmatically with Bearer auth.
finops:
- name: Xano Finops
  service_category: Developer Tools and Backend Platform
  slug: xano-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/xano.png
layout: provider
modified: '2026-06-20'
name: Xano
nav: Providers
network: true
overview: 'Xano publishes 6 APIs on the [APIs.io](https://apis.io/) network, including API Groups API, Auth API, Content API, and 3 more. Tagged areas include No Code, Backend as a Service, BaaS, API Builder, and Database.


  Xano''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Xano Plans Pricing
  plan_count: 4
  slug: xano-plans-pricing
random_paper: 99
rate_limits:
- limit_count: 4
  name: Xano Rate Limits
  slug: xano-rate-limits
score:
  band: thin
  composite: 39.8
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 56.8
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xano/refs/heads/main/screenshots/xano-2026-06-20T201653.png
security:
- kind: authentication
  name: Xano Authentication
  slug: xano-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Xano Domain Security
  slug: xano-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Xano Vulnerability Disclosure
  slug: xano-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Xano Trust Center
  slug: xano-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: xano
tags:
- No Code
- Backend as a Service
- BaaS
- API Builder
- Database
- Serverless
website: https://www.xano.com
---
