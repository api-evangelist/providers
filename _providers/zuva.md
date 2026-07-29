---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Zuva Agentic Access
  operation_count: 22
  slug: zuva-agentic-access
  summary_line: 22 operations · 9 acting
api_count: 5
apis:
- description: Multi-level document classification.
  name: Zuva Classification API
  slug: zuva-classification-api
- description: Extract field values from documents.
  name: Zuva Field Extraction API
  slug: zuva-field-extraction-api
- description: Field catalog management.
  name: Zuva Fields API
  slug: zuva-fields-api
- description: Upload and manage document files.
  name: Zuva Files API
  slug: zuva-files-api
- description: Optical character recognition.
  name: Zuva OCR API
  slug: zuva-ocr-api
artifact_total: 12
collections:
- collection_type: open
  name: Zuva DocAI API
  slug: open-zuva
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zuva-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zuva-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zuva-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zuvaai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zuva-inc
- group: company
  title: ''
  type: Website
  url: https://zuva.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://zuva.ai/documentation/
- group: commercial
  title: ''
  type: Plans
  url: plans/zuva-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zuva-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zuva-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://zuva.ai/blog/
created: '2026-06-21'
description: Zuva (by Kira Systems) provides a contract and document AI REST API for extracting structured data from unstructured documents. The Zuva DocAI API offers asynchronous OCR, field extraction across 1,400+ pre-built fields, multi-level document classification across 220+ document types, language detection, and a searchable fields catalog, secured with Bearer API tokens across US and EU regions.
finops:
- name: Zuva Finops
  service_category: AI and Machine Learning
  slug: zuva-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zuva.png
layout: provider
modified: '2026-06-21'
name: Zuva
nav: Providers
network: true
overview: 'Zuva publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Classification API, Field Extraction API, Fields API, and 2 more. Tagged areas include AI, Document AI, Contract Analysis, Field Extraction, and Classification.


  Zuva''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Zuva Plans Pricing
  plan_count: 3
  slug: zuva-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 6
  name: Zuva Rate Limits
  slug: zuva-rate-limits
score:
  band: thin
  composite: 37.4
  delta: -2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Zuva Authentication
  slug: zuva-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zuva Domain Security
  slug: zuva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zuva
tags:
- AI
- Document AI
- Contract Analysis
- Field Extraction
- Classification
- OCR
website: https://zuva.ai/
---
