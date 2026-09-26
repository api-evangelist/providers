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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-09-25'
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
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/StarRocks/starrocks/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/StarRocks/starrocks/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/StarRocks/starrocks/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/StarRocks/starrocks/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/StarRocks/starrocks/blob/main/CONTRIBUTING.md
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/starrocks/refs/heads/main/security/starrocks-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/starrocks/refs/heads/main/plans/starrocks-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/starrocks-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/starrocks/refs/heads/main/rate-limits/starrocks-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/starrocks-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/starrocks/refs/heads/main/finops/starrocks-finops.yml
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


  StarRocks'' developer surface includes developer portal, engineering blog, and 15 more developer resources.'
plans:
- name: Starrocks Plans Pricing
  plan_count: 3
  slug: starrocks-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Starrocks Rate Limits
  slug: starrocks-rate-limits
score:
  band: thin
  composite: 30.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 49.0
    catalog_earned_first_party: 0.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.9
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 78.6
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 23.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
