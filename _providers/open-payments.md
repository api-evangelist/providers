---
access_model:
  confidence: high
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Open Payments Agentic Access
  operation_count: 8
  slug: open-payments-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 5
apis:
- description: Structured query over a dataset distribution.
  name: CMS Open Payments Datastore Query API
  slug: open-payments-datastore-query-api
- description: SQL query over a datastore resource.
  name: CMS Open Payments Datastore SQL API
  slug: open-payments-datastore-sql-api
- description: Bulk CSV or JSON download of query results.
  name: CMS Open Payments Download API
  slug: open-payments-download-api
- description: DCAT-US dataset catalog and metadata.
  name: CMS Open Payments Metastore API
  slug: open-payments-metastore-api
- description: Full-text and faceted dataset discovery.
  name: CMS Open Payments Search API
  slug: open-payments-search-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CMS Open Payments Datastore Query API
  slug: open-open-payments-datastore-query-api
- collection_type: open
  name: CMS Open Payments Datastore Query Datastore SQL API
  slug: open-open-payments-datastore-sql-api
- collection_type: open
  name: CMS Open Payments Datastore Query Download API
  slug: open-open-payments-download-api
- collection_type: open
  name: CMS Open Payments Datastore Query Metastore API
  slug: open-open-payments-metastore-api
- collection_type: open
  name: CMS Open Payments Datastore Query Search API
  slug: open-open-payments-search-api
- collection_type: open
  name: CMS Open Payments API
  slug: open-open-payments
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/open-payments-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/open-payments-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-payments-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openpaymentsdata.cms.gov
- group: docs
  title: ''
  type: Documentation
  url: https://openpaymentsdata.cms.gov/about/api
- group: start
  title: ''
  type: SignUp
  url: https://www.cms.gov/priorities/key-initiatives/open-payments
- group: commercial
  title: ''
  type: Plans
  url: plans/open-payments-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/open-payments-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/open-payments-finops.yml
created: '2026-07-11'
description: CMS Open Payments is the U.S. federal transparency program (run by the Centers for Medicare and Medicaid Services) that publishes payments and transfers of value made by drug and medical device manufacturers and group purchasing organizations to physicians, non-physician practitioners, and teaching hospitals. The public data site at openpaymentsdata.cms.gov exposes a free, open, no-authentication REST API (a DKAN-style data catalog under /api/1) that lets developers query general payments, research payments, and ownership and investment records by program year. The API offers a structured datastore query interface (filter, select, sort, paginate), a SQL query endpoint, CSV and JSON downloads, and a metastore catalog for dataset discovery and metadata. Reads are completely free and require no API key. Program Year 2025 alone contains roughly 17 million published records totaling about 14.67 billion dollars in payments.
finops:
- name: Open Payments Finops
  service_category: Government Open Data
  slug: open-payments-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-payments.png
layout: provider
modified: '2026-07-11'
name: CMS Open Payments
nav: Providers
network: true
overview: 'CMS Open Payments publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Datastore Query API, Datastore SQL API, Download API, and 2 more. Tagged areas include Government Data, Healthcare, Open Data, Transparency, and Payments.


  CMS Open Payments'' developer surface includes authentication, documentation, signup flow, and 6 more developer resources.'
plans:
- name: Open Payments Plans Pricing
  plan_count: 1
  slug: open-payments-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Open Payments Rate Limits
  slug: open-payments-rate-limits
score:
  band: thin
  composite: 35.1
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 54.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-payments/refs/heads/main/screenshots/open-payments-2026-08-07T190513.png
security:
- kind: authentication
  name: Open Payments Authentication
  slug: open-payments-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Open Payments Domain Security
  slug: open-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: open-payments
tags:
- Government Data
- Healthcare
- Open Data
- Transparency
- Payments
- Clinical Data
- Physicians
- Open Government
- Public Sector
website: https://openpaymentsdata.cms.gov
---
