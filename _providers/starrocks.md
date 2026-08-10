---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 3
apis:
- description: 'Stream Load is a synchronous HTTP-based ingestion API. Clients PUT a CSV or JSON payload to /api/{db}/{table}/_stream_load with HTTP Basic authentication and headers like `label`, `column_separator`, '
  name: StarRocks Stream Load HTTP API
  slug: starrocks-stream-load
- description: The Frontend (FE) HTTP server exposes REST endpoints for cluster administration, metrics, query profiling, and load monitoring. Most administrative operations are additionally available via the SQL `A
  name: StarRocks FE HTTP API
  slug: starrocks-fe-http
- description: StarRocks is wire-compatible with MySQL on port 9030, so any MySQL/MariaDB client or JDBC driver can connect to issue SQL queries.
  name: StarRocks Query Interface (MySQL Wire)
  slug: starrocks-mysql-protocol
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/starrocks-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/starrocks-oss
- group: company
  title: ''
  type: Website
  url: https://www.starrocks.io/
- group: start
  title: ''
  type: Portal
  url: https://docs.starrocks.io/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/StarRocks/starrocks
- group: commercial
  title: ''
  type: License
  url: https://github.com/StarRocks/starrocks/blob/main/LICENSE.txt
- group: other
  title: CelerData Cloud
  type: CommercialOffering
  url: https://www.celerdata.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/starrocks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/starrocks-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/starrocks-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.starrocks.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.starrocks.io/blog/rss.xml
created: '2026-05-08'
description: StarRocks is a high-performance, open-source (Apache 2.0) OLAP / lakehouse engine. Clients run SQL via the MySQL protocol, while the FE HTTP server exposes REST endpoints for management and Stream Load is an HTTP-based ingestion API. CelerData provides the managed cloud offering.
finops:
- name: Starrocks Finops
  service_category: API
  slug: starrocks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/starrocks.png
layout: provider
modified: '2026-05-08'
name: StarRocks
nav: Providers
network: true
overview: 'StarRocks publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include OLAP, Lakehouse, SQL, Open Source, and Real-Time Analytics.


  StarRocks'' developer surface includes developer portal, engineering blog, and 10 more developer resources.'
plans:
- name: Starrocks Plans Pricing
  plan_count: 3
  slug: starrocks-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 5
  name: Starrocks Rate Limits
  slug: starrocks-rate-limits
score:
  band: emerging
  composite: 21.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 21.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/starrocks/refs/heads/main/screenshots/starrocks-2026-06-20T194511.png
security:
- kind: domain-security
  name: Starrocks Domain Security
  slug: starrocks-domain-security
  summary_line: TLSv1.3 · HSTS
slug: starrocks
tags:
- OLAP
- Lakehouse
- SQL
- Open Source
- Real-Time Analytics
website: https://www.starrocks.io/
---
