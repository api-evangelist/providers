---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Pdfgeneratorapi Agentic Access
  operation_count: 26
  slug: pdfgeneratorapi-agentic-access
  summary_line: 26 operations · 15 acting
api_count: 3
apis:
- description: Generate, store, and retrieve documents.
  name: PDF Generator API Documents API
  slug: pdfgeneratorapi-documents-api
- description: Manage reusable document templates and the template editor.
  name: PDF Generator API Templates API
  slug: pdfgeneratorapi-templates-api
- description: Manage multi-tenant workspaces within the organization.
  name: PDF Generator API Workspaces API
  slug: pdfgeneratorapi-workspaces-api
artifact_total: 10
collections:
- collection_type: open
  name: PDF Generator API
  slug: open-pdfgeneratorapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pdfgeneratorapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pdfgeneratorapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pdfgeneratorapi-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pdfgeneratorapi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pdf-generator-api
- group: company
  title: ''
  type: Website
  url: https://pdfgeneratorapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pdfgeneratorapi.com/v4/
- group: commercial
  title: ''
  type: Plans
  url: plans/pdfgeneratorapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pdfgeneratorapi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pdfgeneratorapi-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://pdfgeneratorapi.com/blog
created: '2026-06-25'
description: PDF Generator API is a template-based document and PDF generation service. A drag-and-drop browser template editor plus a REST API let developers merge JSON data with reusable templates to produce PDFs, HTML, and other documents synchronously, asynchronously, or in batches, organized across multi-tenant workspaces.
finops:
- name: Pdfgeneratorapi Finops
  service_category: Developer Tools and Document Automation
  slug: pdfgeneratorapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pdfgeneratorapi.png
layout: provider
modified: '2026-06-25'
name: PDF Generator API
nav: Providers
network: true
overview: 'PDF Generator API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Documents API, Templates API, and Workspaces API. Tagged areas include PDF, Document Generation, Templates, Reporting, and Workspaces.


  PDF Generator API''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Pdfgeneratorapi Plans Pricing
  plan_count: 7
  slug: pdfgeneratorapi-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Pdfgeneratorapi Rate Limits
  slug: pdfgeneratorapi-rate-limits
score:
  band: thin
  composite: 39.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Pdfgeneratorapi Authentication
  slug: pdfgeneratorapi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pdfgeneratorapi Domain Security
  slug: pdfgeneratorapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pdfgeneratorapi
tags:
- PDF
- Document Generation
- Templates
- Reporting
- Workspaces
website: https://pdfgeneratorapi.com
---
