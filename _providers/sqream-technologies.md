---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sqream-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sqream.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sqream.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sqream.com/en/latest/reference/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sqream.com/en/latest/getting_started/index.html
- group: company
  title: ''
  type: Blog
  url: https://sqream.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SQream
- group: operate
  title: ''
  type: Support
  url: https://sqream.com/contact-us/
- group: commercial
  title: ''
  type: Pricing
  url: https://sqream.com/product/pricing-page/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sqream.com/privacy-policy/
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://sqream.com/security-policy/
- group: build
  title: ''
  type: Packages
  url: packages/sqream-technologies-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sqream-technologies-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sqream-technologies-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sqream-technologies-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sqream-technologies-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sqream-technologies-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sqream-technologies-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sqream-technologies-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sqream-technologies-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sqream-technologies-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sqream-technologies-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sqream-technologies-llms.txt
created: '2026-08-29'
description: 'SQream Technologies is an Israeli data and analytics company, founded in 2010 in Tel Aviv, that builds SQreamDB — a GPU-accelerated, SQL-compliant analytics database for petabyte-scale workloads on NVIDIA hardware — alongside AISQream for AI/ML pipelines and Panoply, the no-code cloud data warehouse it acquired in 2021. SQream''s programmatic surface is a database surface rather than an HTTP one: it is reached through first-party client drivers (Python DB-API `pysqream`, JDBC, ODBC, Node.js, .NET, SQLAlchemy dialects, Spark and Trino connectors, and an Apache Airflow provider) speaking SQream''s own wire protocol, plus a set of command-line programs. SQream publishes no public REST/HTTP API, OpenAPI, AsyncAPI or GraphQL contract; its customers are enterprises in financial services, telecommunications, retail, manufacturing, healthcare and ad-tech running self-managed or cloud-deployed clusters.'
image: https://sqream.com/wp-content/uploads/2022/09/cropped-sqream_favicon-192x192.png
layout: provider
modified: '2026-08-29'
name: SQream Technologies
nav: Providers
network: true
overview: 'SQream Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Database, Data Warehouse, Analytics, and GPU.


  SQream Technologies'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, CLI, and 16 more developer resources.'
plans:
- name: Sqream Technologies Plans Pricing
  plan_count: 0
  slug: sqream-technologies-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Sqream Technologies Rate Limits
  slug: sqream-technologies-rate-limits
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 14
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 27.5
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sqream-technologies/refs/heads/main/screenshots/sqream-technologies-2026-09-02T160648.png
security:
- kind: authentication
  name: Sqream Technologies Authentication
  slug: sqream-technologies-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Sqream Technologies Domain Security
  slug: sqream-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sqream Technologies Vulnerability Disclosure
  slug: sqream-technologies-vulnerability-disclosure
  summary_line: Hackerone
slug: sqream-technologies
tags:
- Company
- Database
- Data Warehouse
- Analytics
- GPU
- SQL
- Big Data
- Machine-Learning
- Data Ingestion
- Israel
website: https://sqream.com/
---
