---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Xano Agentic Access
  operation_count: 37
  slug: xano-agentic-access
  summary_line: 37 operations · 21 acting
api_count: 1
apis:
- description: The REST APIs that Xano users build visually. Each API group is served at its own /api:{token} path on the instance and auto-generates its own OpenAPI/Swagger document; surface, paths, and auth are de
  name: Xano Generated User APIs
  slug: xano-generated-user-apis
- baseURL: https://{instance}.xano.io/api:meta
  baseurl_source: declared
  description: API groups, their endpoints, and generated OpenAPI.
  name: Xano API Groups API
  slug: xano-api-groups-api
- baseURL: https://{instance}.xano.io/api:meta
  baseurl_source: declared
  description: Authenticated user and accessible workspaces.
  name: Xano Auth API
  slug: xano-auth-api
- baseURL: https://{instance}.xano.io/api:meta
  baseurl_source: declared
  description: Table records (database content) CRUD and search.
  name: Xano Content API
  slug: xano-content-api
- baseURL: https://{instance}.xano.io/api:meta
  baseurl_source: declared
  description: Workspace file library.
  name: Xano Files API
  slug: xano-files-api
- baseURL: https://{instance}.xano.io/api:meta
  baseurl_source: declared
  description: Database tables, schema, and indexes.
  name: Xano Tables API
  slug: xano-tables-api
- baseURL: https://{instance}.xano.io/api:meta
  baseurl_source: declared
  description: Workspace details, branches, import/export.
  name: Xano Workspace API
  slug: xano-workspace-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Xano Metadata API Groups API
  slug: open-xano-api-groups-api
- collection_type: open
  name: Xano Metadata API Groups Auth API
  slug: open-xano-auth-api
- collection_type: open
  name: Xano Metadata API Groups Content API
  slug: open-xano-content-api
- collection_type: open
  name: Xano Metadata API Groups Files API
  slug: open-xano-files-api
- collection_type: open
  name: Xano Metadata API Groups Tables API
  slug: open-xano-tables-api
- collection_type: open
  name: Xano Metadata API Groups Workspace API
  slug: open-xano-workspace-api
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
overview: 'Xano publishes 6 APIs on the [APIs.io](https://apis.io/) network, including API Groups API, Auth API, Content API, and 3 more. Tagged areas include No-Code, Backend-as-a-Service, API Builder, Database, and Serverless.


  Xano''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Xano Plans Pricing
  plan_count: 4
  slug: xano-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 4
  name: Xano Rate Limits
  slug: xano-rate-limits
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 50.2
    developer_ergonomics: 29.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- No-Code
- Backend-as-a-Service
- API Builder
- Database
- Serverless
website: https://www.xano.com
---
