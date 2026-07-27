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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Docsumo Agentic Access
  operation_count: 10
  slug: docsumo-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 5
apis:
- description: Account-configured webhook callbacks that POST a JSON payload to your endpoint when a document changes processing status (uploaded, processed, reviewed), carrying document identifiers and status for d
  name: Docsumo Webhooks API
  slug: docsumo-webhooks-api
- description: Enabled document types and account detail.
  name: Docsumo Document Types API
  slug: docsumo-document-types-api
- description: Upload, list, summarize, and delete documents.
  name: Docsumo Documents API
  slug: docsumo-documents-api
- description: Retrieve AI-extracted data for a processed document.
  name: Docsumo Extraction API
  slug: docsumo-extraction-api
- description: Human-in-the-loop review URLs and review status.
  name: Docsumo Review API
  slug: docsumo-review-api
artifact_total: 12
collections:
- collection_type: open
  name: Docsumo API
  slug: open-docsumo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/docsumo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/docsumo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/docsumo-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/docsumo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/docsumo
- group: company
  title: ''
  type: Website
  url: https://www.docsumo.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.docsumo.com/reference/getting-started-with-your-api
- group: commercial
  title: ''
  type: Plans
  url: plans/docsumo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/docsumo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/docsumo-finops.yml
created: '2026-06-21'
description: Docsumo is an intelligent document processing (IDP) platform that uses OCR, computer vision, and machine learning to convert unstructured documents - invoices, bank statements, pay stubs, receipts, tax forms - into structured, validated data. The REST API at https://app.docsumo.com/api/v1 uploads documents, retrieves AI-extracted data, supports human-in-the-loop review, and emits webhooks as documents finish processing.
finops:
- name: Docsumo Finops
  service_category: AI and Machine Learning
  slug: docsumo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/docsumo.png
layout: provider
modified: '2026-06-21'
name: Docsumo
nav: Providers
network: true
overview: 'Docsumo publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Document Types API, Documents API, Extraction API, and 1 more. Tagged areas include Document Processing, IDP, OCR, Data Extraction, and AI.


  Docsumo''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Docsumo Plans Pricing
  plan_count: 3
  slug: docsumo-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Docsumo Rate Limits
  slug: docsumo-rate-limits
score:
  band: thin
  composite: 42.1
  delta: 3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.9
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/docsumo/refs/heads/main/screenshots/docsumo-2026-07-25T212211.png
security:
- kind: authentication
  name: Docsumo Authentication
  slug: docsumo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Docsumo Domain Security
  slug: docsumo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: docsumo
tags:
- Document Processing
- IDP
- OCR
- Data Extraction
- AI
website: https://www.docsumo.com
---
