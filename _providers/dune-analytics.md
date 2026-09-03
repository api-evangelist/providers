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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-03'
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
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dune-analytics-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/dune-analytics-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dune-analytics-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/dune-analytics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dune-analytics-rate-limits.yml
- group: commercial
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
- name: Dune Analytics Finops
  service_category: Crypto Analytics
  slug: dune-analytics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dune-analytics.png
layout: provider
modified: '2026-05-08'
name: Dune Analytics
nav: Providers
network: true
overview: 'Dune Analytics publishes 2 APIs on the [APIs.io](https://apis.io/) network: Execution API and Query API. Tagged areas include Web3, Analytics, SQL, Dashboards, and Blockchain.


  Dune Analytics'' developer surface includes authentication, developer portal, documentation, pricing, GitHub presence, engineering blog, and 8 more developer resources.'
plans:
- name: Dune Analytics Plans Pricing
  plan_count: 4
  slug: dune-analytics-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Dune Analytics Rate Limits
  slug: dune-analytics-rate-limits
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 11
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dune-analytics/refs/heads/main/screenshots/dune-analytics-2026-06-20T180421.png
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
website: https://dune.com/
---
