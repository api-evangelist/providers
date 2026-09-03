---
access_model:
  confidence: high
  label: Freemium · Self-serve signup · 14-day evaluation before choosing a plan
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Metaplane Agentic Access
  operation_count: 22
  slug: metaplane-agentic-access
  summary_line: 22 operations · 16 acting
api_count: 1
apis:
- baseURL: https://dev.api.metaplane.dev
  baseurl_source: declared
  description: The Metaplane REST API — 23 operations over connections, monitors, monitor evaluations, datapoint ingestion and tags. Bearer-token authenticated, versioned by path prefix (/v1 with /v2 for two monitor
  name: Metaplane API
  slug: metaplane
- baseURL: https://dev.api.metaplane.dev
  baseurl_source: declared
  description: The Connections API from Metaplane — 4 operations for listing warehouse, BI and dbt connections, reading sync status, triggering a re-sync and rotating a connection private key.
  name: Metaplane Connections API
  slug: metaplane-connections-api
- baseURL: https://dev.api.metaplane.dev
  baseurl_source: declared
  description: The Monitors API from Metaplane — 12 operations for creating, updating, running and reading data quality monitors, their evaluation history and their status, plus historic-data import and datapoint in
  name: Metaplane Monitors API
  slug: metaplane-monitors-api
- baseURL: https://dev.api.metaplane.dev
  baseurl_source: declared
  description: 'The Tags API from Metaplane — 7 operations for bulk-labelling tables and monitors, removing tags, fetching tag definitions and reading tagged objects and monitors back. Tags are the routing dimension '
  name: Metaplane Tags API
  slug: metaplane-tags-api
artifact_total: 19
asyncapis:
- description: ''
  name: Metaplane Webhooks
  slug: metaplane-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Metaplane Connections API
  slug: open-metaplane-connections-api
- collection_type: open
  name: Metaplane Connections Datapoints API
  slug: open-metaplane-datapoints-api
- collection_type: open
  name: Metaplane Connections Monitors API
  slug: open-metaplane-monitors-api
- collection_type: open
  name: Metaplane Connections Tags API
  slug: open-metaplane-tags-api
- collection_type: open
  name: Metaplane API
  slug: open-metaplane
common:
- group: company
  title: ''
  type: Website
  url: https://www.metaplane.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metaplane.dev
- group: docs
  title: ''
  type: APIReference
  url: https://docs.metaplane.dev/reference/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.metaplane.dev/docs/setting-up-metaplane-for-the-first-time
- group: commercial
  title: ''
  type: Pricing
  url: https://www.metaplane.dev/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/metaplane-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/metaplane-rate-limits.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.metaplane.dev/signup
- group: start
  title: ''
  type: Login
  url: https://www.metaplane.dev/login
- group: operate
  title: ''
  type: Support
  url: https://www.metaplane.dev/book-a-demo
- group: company
  title: ''
  type: Blog
  url: https://www.metaplane.dev/blog/rss.xml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.metaplane.dev/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/metaplane-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.metaplane.dev
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/metaplane-lifecycle.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.metaplane.dev/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.metaplane.dev/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/metaplane
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/metaplane
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.metaplane.dev/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/metaplane-llms.txt
- group: build
  title: ''
  type: CLI
  url: cli/metaplane-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/metaplane-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/metaplane-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/metaplane-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/metaplane-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/metaplane-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/metaplane-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/metaplane-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/metaplane-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metaplane-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/metaplane-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/metaplane-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/metaplane-agentic-access.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/metaplane-finops.yml
created: '2026-03-27'
description: Metaplane is a data observability platform for data teams — automated anomaly detection, data quality monitoring, column-level lineage, schema-change alerting and data CI/CD across Snowflake, BigQuery, Redshift, Databricks, ClickHouse, Postgres, MySQL, SQL Server, S3, dbt, Airflow and the major BI tools. Metaplane learns the normal behaviour of every monitored table with an ML model and raises grouped incidents when volume, freshness, nullness, uniqueness, cardinality or a custom SQL metric drifts out of bounds. It exposes a REST API of 23 operations over connections, monitors, monitor evaluations, datapoint ingestion and tags, documented on a ReadMe developer portal, plus outbound incident webhooks and a free local CLI for visualising dbt runs. Metaplane was acquired by Datadog in April 2025 and continues to operate as a standalone product surface.
finops:
- name: Metaplane Finops
  service_category: API
  slug: metaplane-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/metaplane.png
layout: provider
mcp_servers:
- description: ''
  name: Metaplane MCP Server
  slug: metaplane-mcp-server
modified: '2026-08-29'
name: Metaplane
nav: Providers
network: true
overview: 'Metaplane publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Connections API, Monitors API, and 2 more. Tagged areas include AIOps, Data Observability, Data Quality, Anomaly Detection, and Data Lineage.


  The Metaplane catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Metaplane''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, engineering blog, and 29 more developer resources.'
plans:
- name: Metaplane Plans Pricing
  plan_count: 3
  slug: metaplane-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Metaplane Rate Limits
  slug: metaplane-rate-limits
score:
  band: strong
  composite: 60.1
  coverage:
    artifact_dirs: 24
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 61.7
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 60.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/metaplane/refs/heads/main/screenshots/metaplane-2026-06-20T185251.png
security:
- kind: authentication
  name: Metaplane Authentication
  slug: metaplane-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Metaplane Domain Security
  slug: metaplane-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Metaplane Trust Center
  slug: metaplane-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: metaplane
tags:
- AIOps
- Data Observability
- Data Quality
- Anomaly Detection
- Data Lineage
- Monitoring
- Analytics
- Data Engineering
- dbt
- Snowflake
website: https://www.metaplane.dev
---
