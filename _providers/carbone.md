---
access_model:
  confidence: medium
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Carbone Agentic Access
  operation_count: 7
  slug: carbone-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 1
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
- baseURL: https://api.carbone.io
  baseurl_source: declared
  description: The Render API from Carbone — 3 operation(s) for render.
  name: Carbone Render API
  slug: carbone-render-api
- baseURL: https://api.carbone.io
  baseurl_source: declared
  description: The Status API from Carbone — 1 operation(s) for status.
  name: Carbone Status API
  slug: carbone-status-api
- baseURL: https://api.carbone.io
  baseurl_source: declared
  description: The Template API from Carbone — 2 operation(s) for template.
  name: Carbone Template API
  slug: carbone-template-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Carbone Cloud HTTP Render API
  slug: open-carbone-render-api
- collection_type: open
  name: Carbone Cloud HTTP Render Status API
  slug: open-carbone-status-api
- collection_type: open
  name: Carbone Cloud HTTP Render Template API
  slug: open-carbone-template-api
- collection_type: open
  name: Carbone Cloud HTTP API
  slug: open-carbone
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/carboneio/carbone/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/carboneio/carbone/blob/master/SECURITY.md
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
overview: 'Carbone publishes 3 APIs on the [APIs.io](https://apis.io/) network: Render API, Status API, and Template API. Tagged areas include Document Generation, PDF, Templates, Open-Source, and Office.


  Carbone''s developer surface includes authentication, documentation, pricing, GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: Carbone Plans Pricing
  plan_count: 11
  slug: carbone-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Carbone Rate Limits
  slug: carbone-rate-limits
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 50.6
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 34.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Open-Source
- Office
- DOCX
- XLSX
website: https://carbone.io/
---
