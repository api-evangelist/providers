---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Carbone Agentic Access
  operation_count: 7
  slug: carbone-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 6
apis:
- description: Cloud-hosted Carbone API. Two flows — upload-once via POST /template then render with a template ID; or single-request inline-base64 render. Bearer-token auth (Authorization header). Sync and async vi
  name: Carbone Cloud HTTP API
  slug: cloud
- description: Self-hosted Carbone deployment exposing the same HTTP API. Auth disabled by default; enable via configuration. 30-day free trial of paid features.
  name: Carbone On-Premises
  slug: on-prem
- description: Open-source Node.js library that powers the rendering engine. Embed directly in your application; render templates with JSON data without hitting the cloud API.
  name: Carbone Render Engine (Open Source)
  slug: js
- description: The Render API from Carbone — 3 operation(s) for render.
  name: Carbone Render API
  slug: carbone-render-api
- description: The Status API from Carbone — 1 operation(s) for status.
  name: Carbone Status API
  slug: carbone-status-api
- description: The Template API from Carbone — 2 operation(s) for template.
  name: Carbone Template API
  slug: carbone-template-api
artifact_total: 13
collections:
- collection_type: open
  name: Carbone Cloud HTTP API
  slug: open-carbone
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/carbone-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carbone-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/carbone-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/carboneio
- group: company
  title: ''
  type: Website
  url: https://carbone.io/
- group: docs
  title: ''
  type: Documentation
  url: https://carbone.io/documentation.html
- group: commercial
  title: ''
  type: Pricing
  url: https://carbone.io/pricing.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/carboneio
- group: commercial
  title: ''
  type: Plans
  url: plans/carbone-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/carbone-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/carbone-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://carbone.io/blog/
created: '2026-05-08'
description: Carbone is a document generation engine that uses Word, Excel, PowerPoint and ODF templates with JSON data to produce PDFs or office documents. The Carbone HTTP API offers a template-then-render workflow with both cloud (api.carbone.io) and on-prem deployments. The Carbone JS rendering engine is open-source and embeddable.
finops:
- name: Carbone Finops
  service_category: Document Generation
  slug: carbone-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carbone.png
layout: provider
modified: '2026-05-08'
name: Carbone
nav: Providers
network: true
overview: 'Carbone publishes 3 APIs on the [APIs.io](https://apis.io/) network: Render API, Status API, and Template API. Tagged areas include Document Generation, PDF, Templates, Open Source, and Office.


  Carbone''s developer surface includes authentication, documentation, pricing, GitHub presence, engineering blog, and 7 more developer resources.'
plans:
- name: Carbone Plans Pricing
  plan_count: 11
  slug: carbone-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Carbone Rate Limits
  slug: carbone-rate-limits
score:
  band: thin
  composite: 40.0
  delta: -2.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 53.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carbone/refs/heads/main/screenshots/carbone-2026-06-20T173951.png
security:
- kind: authentication
  name: Carbone Authentication
  slug: carbone-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Carbone Domain Security
  slug: carbone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carbone
tags:
- Document Generation
- PDF
- Templates
- Open Source
- Office
- DOCX
- XLSX
website: https://carbone.io/
---
