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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Unstructured Agentic Access
  operation_count: 46
  slug: unstructured-agentic-access
  summary_line: 46 operations · 24 acting
api_count: 9
apis:
- description: The channels API from Unstructured — 3 operation(s) for channels.
  name: Unstructured channels API
  slug: unstructured-channels-api
- description: The destinations API from Unstructured — 3 operation(s) for destinations.
  name: Unstructured destinations API
  slug: unstructured-destinations-api
- description: The general API from Unstructured — 1 operation(s) for general.
  name: Unstructured general API
  slug: unstructured-general-api
- description: The jobs API from Unstructured — 6 operation(s) for jobs.
  name: Unstructured jobs API
  slug: unstructured-jobs-api
- description: The notifications API from Unstructured — 4 operation(s) for notifications.
  name: Unstructured notifications API
  slug: unstructured-notifications-api
- description: The sources API from Unstructured — 3 operation(s) for sources.
  name: Unstructured sources API
  slug: unstructured-sources-api
- description: The templates API from Unstructured — 2 operation(s) for templates.
  name: Unstructured templates API
  slug: unstructured-templates-api
- description: The workflow-channels API from Unstructured — 3 operation(s) for workflow-channels.
  name: Unstructured workflow-channels API
  slug: unstructured-workflow-channels-api
- description: The workflows API from Unstructured — 6 operation(s) for workflows.
  name: Unstructured workflows API
  slug: unstructured-workflows-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unstructured-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/unstructured-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unstructured-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unstructured-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://unstructured.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unstructured.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Unstructured-IO
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unstructuredio/
- group: other
  title: ''
  type: X
  url: https://twitter.com/UnstructuredIO
- group: company
  title: ''
  type: Blog
  url: https://unstructured.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://unstructured.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://unstructuredio.trust.pagerduty.com/posts/dashboard
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/Unstructured-IO/unstructured-python-client
- group: build
  title: ''
  type: JavaScriptSDK
  url: https://github.com/Unstructured-IO/unstructured-js-client
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Unstructured-IO/UNS-MCP
- group: commercial
  title: ''
  type: Plans
  url: plans/unstructured-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unstructured-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/unstructured-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/unstructured/refs/heads/main/vocabulary/unstructured-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/unstructured/refs/heads/main/json-schema/unstructured-schemas.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/unstructured/refs/heads/main/json-ld/unstructured-context.jsonld
created: '2026-06-12'
description: Unstructured is a document parsing and pre-processing platform that provides a REST API for ingesting PDFs, HTML, DOCX, images, and more than 50 other file formats, transforming them into clean structured JSON chunks ready for RAG pipelines and LLM applications. The platform offers partitioning, enrichment, chunking, and embedding capabilities via both a SaaS serverless API and self-hosted deployments. Billing is calculated on a per-page basis, with a free tier of 15,000 pages, pay-as-you-go at $0.03 per page, and custom enterprise pricing. Unstructured also ships Python and JavaScript SDKs, an MCP server for AI agent workflows, and 40+ connectors for source and destination data systems including S3, Databricks, and vector databases.
finops:
- name: Unstructured Finops
  service_category: ''
  slug: unstructured-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unstructured.png
json_schemas:
- name: Unstructured API Schemas
  property_count: 0
  slug: unstructured-schemas
jsonld:
- class_count: 4
  name: Unstructured Context
  property_count: 12
  slug: unstructured-context
layout: provider
mcp_servers:
- description: ''
  name: UNS-MCP
  slug: uns-mcp
modified: '2026-06-12'
name: Unstructured
nav: Providers
network: true
overview: 'Unstructured publishes 9 APIs on the [APIs.io](https://apis.io/) network, including channels API, destinations API, general API, and 6 more. Tagged areas include document-processing, ETL, RAG, LLM, and PDF.


  The Unstructured catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Unstructured''s developer surface includes authentication, documentation, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Unstructured Plans Pricing
  plan_count: 3
  slug: unstructured-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 2
  name: Unstructured Rate Limits
  slug: unstructured-rate-limits
rules:
- name: Unstructured API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: unstructured-jsonschema-spectral-rules
score:
  band: developing
  composite: 55.3
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 65.9
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 42.1
  previous_composite: 55.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unstructured/refs/heads/main/screenshots/unstructured-2026-06-20T200434.png
security:
- kind: authentication
  name: Unstructured Authentication
  slug: unstructured-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Unstructured Domain Security
  slug: unstructured-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Unstructured Trust Center
  slug: unstructured-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: unstructured
tags:
- document-processing
- ETL
- RAG
- LLM
- PDF
- OCR
- data-ingestion
- chunking
- embeddings
- AI
website: https://unstructured.io
---
