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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Docraptor Agentic Access
  operation_count: 4
  slug: docraptor-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 3
apis:
- description: REST API for generating PDF, XLS, XLSX from HTML/CSS or URL. HTTP Basic auth using API key as username. Sync POST /docs and async POST /async_docs with status polling. Test documents are unlimited and
  name: DocRaptor REST API
  slug: rest
- description: The Async Documents API from DocRaptor — 2 operation(s) for async documents.
  name: DocRaptor Async Documents API
  slug: docraptor-async-documents-api
- description: The Documents API from DocRaptor — 2 operation(s) for documents.
  name: DocRaptor Documents API
  slug: docraptor-documents-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DocRaptor Async Documents API
  slug: open-docraptor-async-documents-api
- collection_type: open
  name: DocRaptor Async Documents API
  slug: open-docraptor-documents-api
- collection_type: open
  name: DocRaptor API
  slug: open-docraptor
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/docraptor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/docraptor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/docraptor-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/docraptor
- group: company
  title: ''
  type: Website
  url: https://docraptor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docraptor.com/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://docraptor.com/plans
- group: build
  title: ''
  type: GitHub
  url: https://github.com/DocRaptor
- group: commercial
  title: ''
  type: Plans
  url: plans/docraptor-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/docraptor-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/docraptor-finops.yml
created: '2026-05-08'
description: DocRaptor is an HTML-to-PDF / HTML-to-Excel document generation API powered by Prince XML. Strong CSS-paged-media support including headers/footers, page breaks, watermarks, accessibility tags. Synchronous and asynchronous document creation; status polling; document hosting.
finops:
- name: Docraptor Finops
  service_category: Document Generation
  slug: docraptor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/docraptor.png
layout: provider
modified: '2026-05-08'
name: DocRaptor
nav: Providers
network: true
overview: 'DocRaptor publishes 2 APIs on the [APIs.io](https://apis.io/) network: Async Documents API and Documents API. Tagged areas include Document Generation, PDF, HTML, Excel, and API.


  DocRaptor''s developer surface includes authentication, documentation, pricing, GitHub presence, and 7 more developer resources.'
plans:
- name: Docraptor Plans Pricing
  plan_count: 9
  slug: docraptor-plans-pricing
random_paper: 80
rate_limits:
- limit_count: 3
  name: Docraptor Rate Limits
  slug: docraptor-rate-limits
score:
  band: thin
  composite: 30.9
  delta: -0.5
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/docraptor/refs/heads/main/screenshots/docraptor-2026-06-20T180113.png
security:
- kind: authentication
  name: Docraptor Authentication
  slug: docraptor-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Docraptor Domain Security
  slug: docraptor-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: docraptor
tags:
- Document Generation
- PDF
- HTML
- Excel
- API
- Prince
website: https://docraptor.com/
---
