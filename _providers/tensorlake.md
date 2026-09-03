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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Tensorlake Agentic Access
  operation_count: 27
  slug: tensorlake-agentic-access
  summary_line: 27 operations · 18 acting
api_count: 1
apis:
- baseURL: https://api.tensorlake.ai
  baseurl_source: declared
  description: Group documents under a shared parse/extraction configuration.
  name: Tensorlake Datasets API
  slug: tensorlake-datasets-api
- baseURL: https://api.tensorlake.ai
  baseurl_source: declared
  description: Upload and manage files referenced by parse and extraction jobs.
  name: Tensorlake Files API
  slug: tensorlake-files-api
- baseURL: https://api.tensorlake.ai
  baseurl_source: declared
  description: Asynchronous document parsing jobs.
  name: Tensorlake Parse API
  slug: tensorlake-parse-api
- baseURL: https://api.tensorlake.ai
  baseurl_source: declared
  description: MicroVM sandboxes for serverless workflows and agent code.
  name: Tensorlake Sandboxes API
  slug: tensorlake-sandboxes-api
- baseURL: https://api.tensorlake.ai
  baseurl_source: declared
  description: Schema-guided extraction, classification, read/OCR, and edit.
  name: Tensorlake Structured Extraction API
  slug: tensorlake-structured-extraction-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tensorlake Datasets API
  slug: open-tensorlake-datasets-api
- collection_type: open
  name: Tensorlake Datasets Files API
  slug: open-tensorlake-files-api
- collection_type: open
  name: Tensorlake Datasets Parse API
  slug: open-tensorlake-parse-api
- collection_type: open
  name: Tensorlake Datasets Sandboxes API
  slug: open-tensorlake-sandboxes-api
- collection_type: open
  name: Tensorlake Datasets Structured Extraction API
  slug: open-tensorlake-structured-extraction-api
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
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 61.3
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 41.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tensorlake/refs/heads/main/screenshots/tensorlake-2026-09-02T163114.png
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
- Artificial Intelligence
- Unstructured Data
- Document AI
- RAG
website: https://www.tensorlake.ai
---
