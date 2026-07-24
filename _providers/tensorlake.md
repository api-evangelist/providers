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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Tensorlake Agentic Access
  operation_count: 27
  slug: tensorlake-agentic-access
  summary_line: 27 operations · 18 acting
api_count: 5
apis:
- description: Group documents under a shared parse/extraction configuration.
  name: Tensorlake Datasets API
  slug: tensorlake-datasets-api
- description: Upload and manage files referenced by parse and extraction jobs.
  name: Tensorlake Files API
  slug: tensorlake-files-api
- description: Asynchronous document parsing jobs.
  name: Tensorlake Parse API
  slug: tensorlake-parse-api
- description: MicroVM sandboxes for serverless workflows and agent code.
  name: Tensorlake Sandboxes API
  slug: tensorlake-sandboxes-api
- description: Schema-guided extraction, classification, read/OCR, and edit.
  name: Tensorlake Structured Extraction API
  slug: tensorlake-structured-extraction-api
artifact_total: 12
collections:
- collection_type: open
  name: Tensorlake API
  slug: open-tensorlake
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tensorlake-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tensorlake-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tensorlake-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tensorlakeai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tensorlake
- group: company
  title: ''
  type: Website
  url: https://www.tensorlake.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tensorlake.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/tensorlake-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tensorlake-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tensorlake-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.tensorlake.ai/blog
created: '2026-07-12'
description: Tensorlake is a document ingestion and data extraction platform for AI applications. Its Document Ingestion API parses PDFs, images, and other documents into layout-aware Markdown and structured chunks (OCR, tables, figures, signatures), performs schema-guided structured extraction and classification, and manages reusable files and datasets. Work is submitted as asynchronous parse jobs over a REST API and retrieved by polling or webhooks. Tensorlake Cloud also runs serverless workflows and MicroVM sandboxes for agentic document pipelines.
finops:
- name: Tensorlake Finops
  service_category: AI and Machine Learning
  slug: tensorlake-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tensorlake.png
layout: provider
modified: '2026-07-12'
name: Tensorlake
nav: Providers
network: true
overview: 'Tensorlake publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Datasets API, Files API, Parse API, and 2 more. Tagged areas include Document Extraction, Data Extraction, Document Ingestion, Document Parsing, and OCR.


  Tensorlake''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Tensorlake Plans Pricing
  plan_count: 4
  slug: tensorlake-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Tensorlake Rate Limits
  slug: tensorlake-rate-limits
score:
  band: thin
  composite: 38.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Tensorlake Authentication
  slug: tensorlake-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tensorlake Domain Security
  slug: tensorlake-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tensorlake
tags:
- Document Extraction
- Data Extraction
- Document Ingestion
- Document Parsing
- OCR
- Data Ingestion
- AI
- Unstructured Data
- Document AI
- RAG
website: https://www.tensorlake.ai
---
