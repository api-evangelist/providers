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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Pdfendpoint Agentic Access
  operation_count: 5
  slug: pdfendpoint-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 3
apis:
- description: The Account API from PDFEndpoint — 2 operation(s) for account.
  name: PDFEndpoint Account API
  slug: pdfendpoint-account-api
- description: The Convert API from PDFEndpoint — 1 operation(s) for convert.
  name: PDFEndpoint Convert API
  slug: pdfendpoint-convert-api
- description: The Renders API from PDFEndpoint — 2 operation(s) for renders.
  name: PDFEndpoint Renders API
  slug: pdfendpoint-renders-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PDFEndpoint Account API
  slug: open-pdfendpoint-account-api
- collection_type: open
  name: PDFEndpoint Account Convert API
  slug: open-pdfendpoint-convert-api
- collection_type: open
  name: PDFEndpoint Account Renders API
  slug: open-pdfendpoint-renders-api
- collection_type: open
  name: PDFEndpoint API
  slug: open-pdfendpoint
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pdfendpoint-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pdfendpoint-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pdfendpoint-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://pdfendpoint.com
- group: docs
  title: ''
  type: Documentation
  url: https://pdfendpoint.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/pdfendpoint-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pdfendpoint-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pdfendpoint-finops.yml
created: '2026-06-25'
description: PDFEndpoint is a lightweight HTML and URL to PDF conversion API. A single REST endpoint renders raw HTML or a publicly accessible HTTPS URL into a PDF using a headless browser, with extensive options for page size, margins, orientation, headers and footers, encryption, and multiple delivery modes (JSON URL, base64, inline, webhook, S3, GCP). A sandbox mode watermarks output without consuming the monthly quota.
finops:
- name: Pdfendpoint Finops
  service_category: Document Generation
  slug: pdfendpoint-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pdfendpoint.png
layout: provider
modified: '2026-06-25'
name: PDFEndpoint
nav: Providers
network: true
overview: 'PDFEndpoint publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, Convert API, and Renders API. Tagged areas include PDF, HTML to PDF, URL to PDF, Document Generation, and Conversion.


  PDFEndpoint''s developer surface includes authentication, documentation, and 6 more developer resources.'
plans:
- name: Pdfendpoint Plans Pricing
  plan_count: 2
  slug: pdfendpoint-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Pdfendpoint Rate Limits
  slug: pdfendpoint-rate-limits
score:
  band: thin
  composite: 36.5
  delta: 1.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 55.8
    developer_ergonomics: 26.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pdfendpoint/refs/heads/main/screenshots/pdfendpoint-2026-08-07T191717.png
security:
- kind: authentication
  name: Pdfendpoint Authentication
  slug: pdfendpoint-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pdfendpoint Domain Security
  slug: pdfendpoint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pdfendpoint
tags:
- PDF
- HTML to PDF
- URL to PDF
- Document Generation
- Conversion
website: https://pdfendpoint.com
---
