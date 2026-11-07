---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Dune Analytics Agentic Access
  operation_count: 5
  slug: dune-analytics-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- description: REST endpoints for executing pre-saved Dune SQL queries, polling execution status, and paginating results. Powers programmatic access to community and team-built analytics. Authentication via X-Dune-A
  name: Dune Query API
  slug: query-api
- description: Curated, fixed endpoints over Dune's most popular trend datasets without writing SQL.
  name: Dune Trends API
  slug: trends-api
- description: Real-time multichain wallet, token, and transaction data across EVM and SVM chains via Sim by Dune.
  name: Dune Echo (Sim) Multichain API
  slug: echo-api
- baseURL: https://api.dune.com/api/v1
  baseurl_source: declared
  description: The Execution API from Dune Analytics — 3 operation(s) for execution.
  name: Dune Analytics Execution API
  slug: dune-analytics-execution-api
- baseURL: https://api.dune.com/api/v1
  baseurl_source: declared
  description: The Query API from Dune Analytics — 2 operation(s) for query.
  name: Dune Analytics Query API
  slug: dune-analytics-query-api
- baseURL: https://api.dune.com/api/v1
  baseurl_source: declared
  description: The Contracts API from Dune Analytics — 2 operation(s) for contracts.
  name: Dune Analytics Contracts API
  slug: dune-analytics-contracts-api
- baseURL: https://api.dune.com/api/v1
  baseurl_source: declared
  description: The Dashboards API from Dune Analytics — 4 operation(s) for dashboards.
  name: Dune Analytics Dashboards API
  slug: dune-analytics-dashboards-api
- baseURL: https://api.dune.com/api/v1
  baseurl_source: declared
  description: The Datasets API from Dune Analytics — 4 operation(s) for datasets.
  name: Dune Analytics Datasets API
  slug: dune-analytics-datasets-api
- baseURL: https://api.dune.com/api/v1
  baseurl_source: declared
  description: The Endpoints API from Dune Analytics — 1 operation(s) for endpoints.
  name: Dune Analytics Endpoints API
  slug: dune-analytics-endpoints-api
- baseURL: https://api.dune.com/api/v1
  baseurl_source: declared
  description: The Materialized Views API from Dune Analytics — 3 operation(s) for materialized views.
  name: Dune Analytics Materialized Views API
  slug: dune-analytics-materialized-views-api
- baseURL: https://api.dune.com/api/v1
  baseurl_source: declared
  description: The Pipelines API from Dune Analytics — 2 operation(s) for pipelines.
  name: Dune Analytics Pipelines API
  slug: dune-analytics-pipelines-api
- baseURL: https://api.dune.com/api/v1
  baseurl_source: declared
  description: The Queries API from Dune Analytics — 2 operation(s) for queries.
  name: Dune Analytics Queries API
  slug: dune-analytics-queries-api
- baseURL: https://api.dune.com/api/v1
  baseurl_source: declared
  description: The Sql API from Dune Analytics — 1 operation(s) for sql.
  name: Dune Analytics Sql API
  slug: dune-analytics-sql-api
- baseURL: https://api.dune.com/api/v1
  baseurl_source: declared
  description: The Uploads API from Dune Analytics — 5 operation(s) for uploads.
  name: Dune Analytics Uploads API
  slug: dune-analytics-uploads-api
- baseURL: https://api.dune.com/api/v1
  baseurl_source: declared
  description: The Usage API from Dune Analytics — 1 operation(s) for usage.
  name: Dune Analytics Usage API
  slug: dune-analytics-usage-api
- baseURL: https://api.dune.com/api/v1
  baseurl_source: declared
  description: The Visualizations API from Dune Analytics — 1 operation(s) for visualizations.
  name: Dune Analytics Visualizations API
  slug: dune-analytics-visualizations-api
artifact_total: 28
collections:
- collection_type: open
  name: Dune Analytics Query Execution API
  slug: open-dune-analytics-execution-api
- collection_type: open
  name: Dune Analytics Execution Query API
  slug: open-dune-analytics-query-api
- collection_type: open
  name: Dune Analytics Query API
  slug: open-dune-analytics
common:
- group: other
  href: https://artifacts.apis.io/dune-analytics/capabilities/dune-analytics-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/dune-analytics-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.dune.com/
- group: agent
  href: https://artifacts.apis.io/dune-analytics/agentic-access/dune-analytics-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dune-analytics-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/dune-analytics/security/dune-analytics-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dune-analytics-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/dune-analytics/security/dune-analytics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dune-analytics-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/dune-analytics/authentication/dune-analytics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dune-analytics-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dune-analytics
- group: start
  title: ''
  type: Portal
  url: https://dune.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dune.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://dune.com/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/duneanalytics
- group: commercial
  href: https://artifacts.apis.io/dune-analytics/plans/dune-analytics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dune-analytics-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/dune-analytics/rate-limits/dune-analytics-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dune-analytics-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dune-analytics/finops/dune-analytics-finops.yml
  title: ''
  type: FinOps
  url: finops/dune-analytics-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.dune.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://dune.com/blog/feed
created: '2026-05-08'
description: 'Dune is a SQL-based crowdsourced blockchain analytics platform. The Dune API exposes Query Execution endpoints (run/poll/results), pre-built Trends endpoints, EVM Transactions API, Echo (real-time multichain wallet data via Sim), a Trino warehouse connector, and dbt integration. Pricing is credit-based: query executions, data exports, and writes consume credits against a plan-tier monthly allowance.'
finops:
- has_sources: true
  method: generated
  name: Dune Analytics Finops
  primary_unit: ''
  service_category: Crypto Analytics
  slug: dune-analytics-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dune-analytics.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.dune.com over HTTP.
  name: Dune Analytics MCP Server
  slug: dune-analytics
modified: '2026-05-08'
name: Dune Analytics
nav: Providers
network: true
overview: 'Dune Analytics publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Execution API, Query API, Contracts API, and 13 more. Tagged areas include Web3, Analytics, SQL, Dashboards, and Blockchain.


  The Dune Analytics catalog on APIs.io includes 1 Spectral governance ruleset.


  Dune Analytics'' developer surface includes authentication, developer portal, documentation, pricing, GitHub presence, engineering blog, and 10 more developer resources.'
plans:
- name: Dune Analytics Plans Pricing
  plan_count: 4
  slug: dune-analytics-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Dune Analytics Rate Limits
  slug: dune-analytics-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Dune Analytics API Rules
  rule_count: 50
  severity_counts:
    error: 40
    hint: 0
    info: 4
    warn: 6
  slug: dune-analytics-rules
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 50.1
    developer_ergonomics: 33.3
    discoverability: 75.0
    operational_transparency: 13.2
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 81.3
      total: 16
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/dune-analytics/dune-analytics-2026-06-20T180421.png
security:
- kind: authentication
  name: Dune Analytics Authentication
  slug: dune-analytics-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dune Analytics Domain Security
  slug: dune-analytics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Dune Analytics Trust Center
  slug: dune-analytics-trust-center
  summary_line: trust center published
slug: dune-analytics
tags:
- Web3
- Analytics
- SQL
- Dashboards
- Blockchain
- Onchain
- Multi-Chain
- Ethereum
website: https://www.dune.com/
---
