---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.4
  scored_at: '2026-11-06'
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
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tensorlake.ai/pricing
- group: agent
  href: https://artifacts.apis.io/tensorlake/agentic-access/tensorlake-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tensorlake-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/tensorlake/security/tensorlake-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tensorlake-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/tensorlake/authentication/tensorlake-authentication.yml
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
  href: https://artifacts.apis.io/tensorlake/plans/tensorlake-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tensorlake-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/tensorlake/rate-limits/tensorlake-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tensorlake-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tensorlake/finops/tensorlake-finops.yml
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
- has_sources: true
  method: generated
  name: Tensorlake Finops
  primary_unit: ''
  service_category: AI and Machine Learning
  slug: tensorlake-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tensorlake.png
layout: provider
modified: '2026-07-12'
name: Tensorlake
nav: Providers
network: true
overview: 'Tensorlake publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Datasets API, Files API, Parse API, and 2 more. Tagged areas include Document Extraction, Data Extraction, Document Ingestion, Document Parsing, and OCR.


  The Tensorlake catalog on APIs.io includes 1 Spectral governance ruleset.


  Tensorlake''s developer surface includes pricing, authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Tensorlake Plans Pricing
  plan_count: 14
  slug: tensorlake-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Tensorlake Rate Limits
  slug: tensorlake-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Tensorlake API Rules
  rule_count: 59
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 4
  slug: tensorlake-rules
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 36.8
    contract_governance: 13.6
    contract_quality: 55.5
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 2.6
  previous_composite: 36.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/tensorlake/tensorlake-2026-09-02T163114.png
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
