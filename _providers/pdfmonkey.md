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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Pdfmonkey Agentic Access
  operation_count: 12
  slug: pdfmonkey-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 3
apis:
- description: Lightweight document representations for status polling and listing.
  name: PDFMonkey Document Cards API
  slug: pdfmonkey-document-cards-api
- description: Create, retrieve, update, and delete generated documents.
  name: PDFMonkey Documents API
  slug: pdfmonkey-documents-api
- description: Manage document templates (HTML + Liquid, SCSS, settings).
  name: PDFMonkey Templates API
  slug: pdfmonkey-templates-api
artifact_total: 10
collections:
- collection_type: open
  name: PDFMonkey API
  slug: open-pdfmonkey
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pdfmonkey-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pdfmonkey-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pdfmonkey-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pdfmonkey
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pdfmonkey
- group: company
  title: ''
  type: Website
  url: https://www.pdfmonkey.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pdfmonkey.io
- group: commercial
  title: ''
  type: Plans
  url: plans/pdfmonkey-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pdfmonkey-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pdfmonkey-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.pdfmonkey.io/blog
created: '2026-06-25'
description: PDFMonkey is a document generation service that turns HTML + Liquid templates and a JSON data payload into PDF (or image) documents via a REST API. Templates are designed in a dashboard editor and generated on demand, asynchronously or synchronously, with webhooks and signed download URLs for delivery.
finops:
- name: Pdfmonkey Finops
  service_category: Document Generation
  slug: pdfmonkey-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pdfmonkey.png
layout: provider
modified: '2026-06-25'
name: PDFMonkey
nav: Providers
network: true
overview: 'PDFMonkey publishes 3 APIs on the [APIs.io](https://apis.io/) network: Document Cards API, Documents API, and Templates API. Tagged areas include PDF, Document Generation, Templates, HTML to PDF, and Documents.


  PDFMonkey''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Pdfmonkey Plans Pricing
  plan_count: 7
  slug: pdfmonkey-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 2
  name: Pdfmonkey Rate Limits
  slug: pdfmonkey-rate-limits
score:
  band: thin
  composite: 39.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Pdfmonkey Authentication
  slug: pdfmonkey-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pdfmonkey Domain Security
  slug: pdfmonkey-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pdfmonkey
tags:
- PDF
- Document Generation
- Templates
- HTML to PDF
- Documents
website: https://www.pdfmonkey.io
---
