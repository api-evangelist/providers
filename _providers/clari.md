---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
- acting_count: 7
  human_in_the_loop: 1
  name: Clari Agentic Access
  operation_count: 15
  slug: clari-agentic-access
  summary_line: 15 operations · 7 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: The Clari Copilot API provides access to conversation intelligence features including call recordings, AI-generated summaries, coaching insights, deal intelligence, and competitor tracking signals cap
  name: Clari Copilot API
  slug: clari-copilot-api
- description: The Activity API API from Clari — 1 operation(s) for activity api.
  name: Clari Activity API API
  slug: clari-activity-api-api
- description: The Administrative API API from Clari — 1 operation(s) for administrative api.
  name: Clari Administrative API API
  slug: clari-administrative-api-api
- description: The Audit API API from Clari — 2 operation(s) for audit api.
  name: Clari Audit API API
  slug: clari-audit-api-api
- description: The Bulk Export Framework API from Clari — 3 operation(s) for bulk export framework.
  name: Clari Bulk Export Framework API
  slug: clari-bulk-export-framework-api
- description: The Bulk Ingest Job Status API API from Clari — 1 operation(s) for bulk ingest job status api.
  name: Clari Bulk Ingest Job Status API API
  slug: clari-bulk-ingest-job-status-api-api
- description: The Export API from Clari — 1 operation(s) for export.
  name: Clari Export API
  slug: clari-export-api
- description: The Forecast API API from Clari — 1 operation(s) for forecast api.
  name: Clari Forecast API API
  slug: clari-forecast-api-api
- description: The Ingestion API API from Clari — 3 operation(s) for ingestion api.
  name: Clari Ingestion API API
  slug: clari-ingestion-api-api
- description: The Opportunity API API from Clari — 1 operation(s) for opportunity api.
  name: Clari Opportunity API API
  slug: clari-opportunity-api-api
artifact_total: 26
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clari-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/clari-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clari-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clari-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.clari.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.clari.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/clari
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clari
- group: company
  title: ''
  type: Blog
  url: https://www.clari.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clari.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://clari.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://x.com/clarihq
- group: commercial
  title: ''
  type: Plans
  url: plans/clari-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clari-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/clari-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/clari-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/clari-context.jsonld
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
created: '2026-06-13'
description: Clari is a revenue operations platform that provides a REST API for accessing pipeline data, forecasts, opportunity signals, activity intelligence, and CRM-enriched deal insights. The API enables revenue teams to programmatically export forecast submissions, query activity data (meetings, emails, attachments), and ingest custom entity data into the Clari platform. Clari also offers a Copilot API for accessing conversation intelligence data including call recordings, AI summaries, and coaching insights. The platform serves enterprise B2B organizations with tools to improve forecast accuracy, accelerate pipeline execution, and unify revenue operations across sales, marketing, and customer success teams.
examples:
- key_count: 3
  name: Clari Activity Export Example
  slug: clari-activity-export-example
- key_count: 3
  name: Clari Forecast Export Example
  slug: clari-forecast-export-example
- key_count: 3
  name: Clari Job Status Example
  slug: clari-job-status-example
finops:
- name: Clari Finops
  service_category: ''
  slug: clari-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Clari revenue operations platform. Clari provides programmatic access to pipeline data, forecasts, opportunity signals, activity intelligenc
  name: Clari GraphQL Schema
  slug: clari-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clari.png
json_schemas:
- name: ClariExportJob
  property_count: 7
  slug: clari-export-job
- name: ClariForecastExportRequest
  property_count: 6
  slug: clari-forecast-export-request
- name: ClariIngestionRequest
  property_count: 1
  slug: clari-ingestion-request
jsonld:
- class_count: 28
  name: Clari Context
  property_count: 6
  slug: clari-context
layout: provider
modified: '2026-06-13'
name: Clari
nav: Providers
network: true
overview: 'Clari publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Activity API API, Administrative API API, Audit API API, and 6 more. Tagged areas include Revenue Operations, Forecasting, Pipeline Management, Sales Intelligence, and Activity Intelligence.


  The Clari catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clari''s developer surface includes authentication, documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Clari Plans Pricing
  plan_count: 3
  slug: clari-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 0
  name: Clari Rate Limits
  slug: clari-rate-limits
rules:
- name: Clari API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: clari-jsonschema-spectral-rules
score:
  band: developing
  composite: 57.7
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 74.6
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 21.1
  previous_composite: 57.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clari/refs/heads/main/screenshots/clari-2026-06-20T174439.png
security:
- kind: authentication
  name: Clari Authentication
  slug: clari-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Clari Domain Security
  slug: clari-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Clari Trust Center
  slug: clari-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: clari
tags:
- Revenue Operations
- Forecasting
- Pipeline Management
- Sales Intelligence
- Activity Intelligence
- Deal Insights
- CRM
- Conversation Intelligence
- B2B
- Enterprise
website: https://www.clari.com/
---
