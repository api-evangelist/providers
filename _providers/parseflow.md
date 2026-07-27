---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 13
  human_in_the_loop: 0
  name: Parseflow Agentic Access
  operation_count: 22
  slug: parseflow-agentic-access
  summary_line: 22 operations · 13 acting
api_count: 14
apis:
- description: The Admin API from Parseflow — 2 operation(s) for admin.
  name: Parseflow Admin API
  slug: parseflow-admin-api
- description: The Analyze API from Parseflow — 1 operation(s) for analyze.
  name: Parseflow Analyze API
  slug: parseflow-analyze-api
- description: The Batch API from Parseflow — 1 operation(s) for batch.
  name: Parseflow Batch API
  slug: parseflow-batch-api
- description: The Billing API from Parseflow — 1 operation(s) for billing.
  name: Parseflow Billing API
  slug: parseflow-billing-api
- description: The Health API from Parseflow — 2 operation(s) for health.
  name: Parseflow Health API
  slug: parseflow-health-api
- description: The Index API from Parseflow — 1 operation(s) for index.
  name: Parseflow Index API
  slug: parseflow-index-api
- description: The Jobs API from Parseflow — 3 operation(s) for jobs.
  name: Parseflow Jobs API
  slug: parseflow-jobs-api
- description: The Me API from Parseflow — 1 operation(s) for me.
  name: Parseflow Me API
  slug: parseflow-me-api
- description: The Pack API from Parseflow — 1 operation(s) for pack.
  name: Parseflow Pack API
  slug: parseflow-pack-api
- description: The Process API from Parseflow — 2 operation(s) for process.
  name: Parseflow Process API
  slug: parseflow-process-api
- description: The Search API from Parseflow — 3 operation(s) for search.
  name: Parseflow Search API
  slug: parseflow-search-api
- description: The Stats API from Parseflow — 1 operation(s) for stats.
  name: Parseflow Stats API
  slug: parseflow-stats-api
- description: The Usage API from Parseflow — 1 operation(s) for usage.
  name: Parseflow Usage API
  slug: parseflow-usage-api
- description: The Webhooks API from Parseflow — 1 operation(s) for webhooks.
  name: Parseflow Webhooks API
  slug: parseflow-webhooks-api
artifact_total: 35
collections:
- collection_type: open
  name: parseflow
  slug: open-parseflow
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/parseflow-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parseflow-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/parseflow-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://docs.parseflow.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.parseflow.tech/docs/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.parseflow.tech/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.parseflow.tech/docs/api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.parseflow.tech/docs/pricing
- group: commercial
  title: ''
  type: Billing
  url: https://docs.parseflow.tech/docs/billing
- group: operate
  title: ''
  type: FAQ
  url: https://docs.parseflow.tech/docs/faq
- group: other
  title: ''
  type: Limits
  url: https://docs.parseflow.tech/docs/limits
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/54564964/2sBXwmPsb9
- group: operate
  title: ''
  type: Contact
  url: https://docs.parseflow.tech/contact
created: '2026-05-27'
description: Document parsing, extraction, and search API. Parse PDFs, DOCX, TXT, and raw text into structured chunks, extraction fields, and search-ready data. Public REST API with multipart file upload, BYOK support, async jobs with webhook callbacks, batch processing, and a built-in keyword search index. Public Postman demo available.
examples:
- key_count: 3
  name: Parseflow Async Job Example
  slug: parseflow-async-job-example
- key_count: 2
  name: Parseflow Batch Example
  slug: parseflow-batch-example
- key_count: 2
  name: Parseflow Process Example
  slug: parseflow-process-example
- key_count: 2
  name: Parseflow Search Example
  slug: parseflow-search-example
finops:
- name: Parseflow Finops
  service_category: ''
  slug: parseflow-finops
image: https://docs.parseflow.tech/img/logo.svg
json_schemas:
- name: Parseflow Batch Request
  property_count: 7
  slug: parseflow-batch-request
- name: Parseflow Indexed Document
  property_count: 8
  slug: parseflow-indexed-document
- name: Parseflow Job Status
  property_count: 9
  slug: parseflow-job-status
- name: Parseflow Process Request
  property_count: 12
  slug: parseflow-process-request
- name: Parseflow Process Response
  property_count: 8
  slug: parseflow-process-response
- name: Parseflow Search Response
  property_count: 4
  slug: parseflow-search-response
- name: Parseflow Usage and Quota
  property_count: 8
  slug: parseflow-usage
jsonld:
- class_count: 19
  name: Parseflow Context
  property_count: 26
  slug: parseflow-context
layout: provider
modified: '2026-05-27'
name: Parseflow
nav: Providers
network: true
overview: 'Parseflow publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Analyze API, Batch API, and 11 more. Tagged areas include Document Parsing, PDF, OCR, Text Extraction, and Document AI.


  The Parseflow catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Parseflow''s developer surface includes authentication, documentation, getting-started guide, API reference, pricing, FAQ, and 7 more developer resources.'
plans:
- name: Parseflow Plans Pricing
  plan_count: 3
  slug: parseflow-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 0
  name: Parseflow Rate Limits
  slug: parseflow-rate-limits
rules:
- name: Parseflow API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: parseflow-jsonschema-spectral-rules
- name: Parseflow API Rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 3
  slug: parseflow-rules
score:
  band: developing
  composite: 52.0
  delta: 3.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 59.5
    developer_ergonomics: 41.3
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 0.0
  previous_composite: 48.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parseflow/refs/heads/main/screenshots/parseflow-2026-06-20T191419.png
security:
- kind: authentication
  name: Parseflow Authentication
  slug: parseflow-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Parseflow Domain Security
  slug: parseflow-domain-security
  summary_line: TLSv1.3
slug: parseflow
tags:
- Document Parsing
- PDF
- OCR
- Text Extraction
- Document AI
- Search
- BYOK
- Async Jobs
- Webhooks
- REST
website: https://docs.parseflow.tech/
---
