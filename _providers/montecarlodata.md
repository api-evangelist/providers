---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
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
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: GraphQL API powering the full Monte Carlo platform, enabling programmatic access to data monitors, incidents, field health, lineage, table and warehouse asset management, and the Push Ingest API for c
  name: Monte Carlo GraphQL API
  slug: monte-carlo-graphql-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/montecarlodata-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/montecarlodata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://montecarlo.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getmontecarlo.com/docs/developer-resources
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/monte-carlo-data
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/monte-carlo-data
- group: company
  title: ''
  type: Blog
  url: https://montecarlo.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://info.montecarlodata.com/solutions/data-observability-platform-pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getmontecarlo.com
- group: other
  title: ''
  type: X
  url: https://x.com/montecarlodata
- group: commercial
  title: ''
  type: Plans
  url: plans/montecarlodata-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/montecarlodata-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/montecarlodata-finops.yml
created: '2026-06-13'
description: Monte Carlo is a data and AI observability platform that helps enterprise organizations find and fix bad data fast. The platform exposes a GraphQL API that powers all the same capabilities as the Monte Carlo web application, enabling programmatic management of data monitors, incidents, field health, and lineage across data warehouses, lakes, ETL, and BI. Developers can automate custom monitoring configurations, augment lineage with external resources, manage bulk operations, and push metadata from sources unreachable via standard collection through the Push Ingest API. Additional developer tools include a Python SDK (Pycarlo), a CLI for onboarding and integration operations, webhooks for routing incident data to custom platforms, and an Airflow provider for pipeline quality gates.
finops:
- name: Montecarlodata Finops
  service_category: ''
  slug: montecarlodata-finops
graphqls:
- description: Monte Carlo Data exposes a comprehensive GraphQL API that powers the full Monte Carlo data observability platform. The API provides programmatic access to all platform capabilities — including data mo
  name: Monte Carlo Data GraphQL API
  slug: montecarlodata-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/montecarlodata.png
jsonld:
- class_count: 11
  name: Montecarlodata Context
  property_count: 11
  slug: montecarlodata-context
layout: provider
modified: '2026-06-13'
name: Monte Carlo
nav: Providers
network: true
overview: 'Monte Carlo publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Data Observability, Data Quality, Data Monitoring, Data Lineage, and GraphQL.


  The Monte Carlo catalog on APIs.io includes 1 JSON-LD context.


  Monte Carlo''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Montecarlodata Plans Pricing
  plan_count: 3
  slug: montecarlodata-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 3
  name: Montecarlodata Rate Limits
  slug: montecarlodata-rate-limits
score:
  band: thin
  composite: 41.6
  delta: -2.9
  facets:
    commercial_clarity: 57.9
    contract_quality: 56.8
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 44.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/montecarlodata/refs/heads/main/screenshots/montecarlodata-2026-06-20T185743.png
security:
- kind: domain-security
  name: Montecarlodata Domain Security
  slug: montecarlodata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Montecarlodata Trust Center
  slug: montecarlodata-trust-center
  summary_line: SOC 2, ISO 27001
slug: montecarlodata
tags:
- Data Observability
- Data Quality
- Data Monitoring
- Data Lineage
- GraphQL
- AI Observability
- Data Reliability
website: https://montecarlo.ai
---
