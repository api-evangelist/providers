---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Rossum Agentic Access
  operation_count: 9
  slug: rossum-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 7
apis:
- description: REST API for managing organizations, users, workspaces, queues, schemas, documents, annotations and webhook/serverless extensions (hooks). Token authentication; access tokens valid ~162 hours by defau
  name: Rossum REST API v1
  slug: rest-v1
- description: Same REST surface served from each customer's tenant subdomain (https://<tenant>.rossum.app/api/v1/) for organisations created after November 2022 or migrated to the new platform.
  name: Rossum Tenant API (rossum.app)
  slug: tenant-app
- description: The Annotations API from Rossum — 2 operation(s) for annotations.
  name: Rossum Annotations API
  slug: rossum-annotations-api
- description: The Authentication API from Rossum — 2 operation(s) for authentication.
  name: Rossum Authentication API
  slug: rossum-authentication-api
- description: The Queues API from Rossum — 2 operation(s) for queues.
  name: Rossum Queues API
  slug: rossum-queues-api
- description: The Schemas API from Rossum — 1 operation(s) for schemas.
  name: Rossum Schemas API
  slug: rossum-schemas-api
- description: The Uploads API from Rossum — 1 operation(s) for uploads.
  name: Rossum Uploads API
  slug: rossum-uploads-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rossum REST Annotations API
  slug: open-rossum-annotations-api
- collection_type: open
  name: Rossum REST Annotations Authentication API
  slug: open-rossum-authentication-api
- collection_type: open
  name: Rossum REST Annotations Queues API
  slug: open-rossum-queues-api
- collection_type: open
  name: Rossum REST Annotations Schemas API
  slug: open-rossum-schemas-api
- collection_type: open
  name: Rossum REST Annotations Uploads API
  slug: open-rossum-uploads-api
- collection_type: open
  name: Rossum REST API
  slug: open-rossum
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rossum-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rossum-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rossum-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rossum-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://rossum.ai/blog/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rossum
- group: company
  title: ''
  type: Website
  url: https://rossum.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://elis.rossum.ai/api/docs/
- group: other
  title: ''
  type: DeveloperHub
  url: https://developers.rossum.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://rossum.ai/pricing/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/rossumai
- group: commercial
  title: ''
  type: Plans
  url: plans/rossum-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rossum-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rossum-finops.yml
created: '2026-05-08'
description: Rossum is an AI-powered document processing platform specialised in transactional documents — invoices, purchase orders, contracts — with cognitive data capture, validation workflows and integration extensions. The Rossum REST API exposes organizations, users, workspaces, queues, schemas, annotations, documents and hooks/extensions across two deployment domains (legacy elis.rossum.ai and the newer per-tenant rossum.app).
finops:
- name: Rossum Finops
  service_category: Document AI / AP Automation
  slug: rossum-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rossum.png
layout: provider
modified: '2026-05-08'
name: Rossum
nav: Providers
network: true
overview: 'Rossum publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Annotations API, Authentication API, Queues API, and 2 more. Tagged areas include Artificial Intelligence, Document AI, IDP, Invoices, and OCR.


  Rossum''s developer surface includes authentication, engineering blog, documentation, pricing, GitHub presence, and 9 more developer resources.'
plans:
- name: Rossum Plans Pricing
  plan_count: 5
  slug: rossum-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Rossum Rate Limits
  slug: rossum-rate-limits
score:
  band: thin
  composite: 31.6
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 49.8
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 31.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rossum/refs/heads/main/screenshots/rossum-2026-06-20T193224.png
security:
- kind: authentication
  name: Rossum Authentication
  slug: rossum-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rossum Domain Security
  slug: rossum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rossum Vulnerability Disclosure
  slug: rossum-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: rossum
tags:
- Artificial Intelligence
- Document AI
- IDP
- Invoices
- OCR
- Workflows
- AP Automation
website: https://rossum.ai/
---
