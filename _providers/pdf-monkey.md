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
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Pdf Monkey Agentic Access
  operation_count: 13
  slug: pdf-monkey-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 3
apis:
- description: Endpoints for verifying API credentials and retrieving account information
  name: PDF Monkey Authentication API
  slug: pdf-monkey-authentication-api
- description: Create, retrieve, update, delete, and list PDF documents
  name: PDF Monkey Documents API
  slug: pdf-monkey-documents-api
- description: Manage document templates for PDF generation
  name: PDF Monkey Templates API
  slug: pdf-monkey-templates-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PDF Monkey Authentication API
  slug: open-pdf-monkey-authentication-api
- collection_type: open
  name: PDFMonkey Document Cards API
  slug: open-pdf-monkey-document-cards-api
- collection_type: open
  name: PDF Monkey Authentication Documents API
  slug: open-pdf-monkey-documents-api
- collection_type: open
  name: PDF Monkey Authentication Templates API
  slug: open-pdf-monkey-templates-api
- collection_type: open
  name: PDFMonkey API
  slug: open-pdfmonkey
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pdf-monkey-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pdf-monkey-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pdf-monkey-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.pdfmonkey.io
- group: docs
  title: ''
  type: Documentation
  url: https://pdfmonkey.io/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/pdfmonkey
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pdfmonkey/
- group: company
  title: ''
  type: Blog
  url: https://www.pdfmonkey.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pdfmonkey.io/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pdfmonkey.io/
- group: other
  title: ''
  type: X
  url: https://twitter.com/pdfmonkey
- group: commercial
  title: ''
  type: Plans
  url: plans/pdf-monkey-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pdf-monkey-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pdf-monkey-finops.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pdfmonkey
created: 2026-06-13
description: PDF Monkey is a PDF generation REST API that uses Handlebars templates to produce high-quality PDFs from JSON data. Developers build templates in a visual dashboard, call the API with dynamic JSON payloads, and retrieve generated documents via signed download URLs or webhooks. The service supports document management, asynchronous and synchronous generation, webhook notifications powered by Svix, fillable PDF forms, password protection, and integrations with Zapier, Make, and n8n.
examples:
- key_count: 4
  name: Create Document Sync
  slug: create-document-sync
- key_count: 4
  name: Create Document
  slug: create-document
- key_count: 4
  name: List Documents
  slug: list-documents
finops:
- name: Pdf Monkey Finops
  service_category: ''
  slug: pdf-monkey-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pdf-monkey.png
json_schemas:
- name: DocumentTemplate
  property_count: 20
  slug: document-template
- name: Document
  property_count: 16
  slug: document
jsonld:
- class_count: 0
  name: Pdf Monkey Context
  property_count: 0
  slug: pdf-monkey
layout: provider
modified: '2026-08-08'
name: PDF Monkey
nav: Providers
network: true
overview: 'PDF Monkey publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Documents API, and Templates API. Tagged areas include PDF, Document Generation, Templates, Handlebars, and REST API.


  The PDF Monkey catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PDF Monkey''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Pdf Monkey Plans Pricing
  plan_count: 5
  slug: pdf-monkey-plans-pricing
random_paper: 124
rate_limits:
- limit_count: 0
  name: Pdf Monkey Rate Limits
  slug: pdf-monkey-rate-limits
rules:
- name: PDF Monkey API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: pdf-monkey-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 70.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pdf-monkey/refs/heads/main/screenshots/pdf-monkey-2026-08-07T191719.png
security:
- kind: authentication
  name: Pdf Monkey Authentication
  slug: pdf-monkey-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pdf Monkey Domain Security
  slug: pdf-monkey-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pdf-monkey
tags:
- PDF
- Document Generation
- Templates
- Handlebars
- REST API
- Webhooks
website: https://www.pdfmonkey.io
---
