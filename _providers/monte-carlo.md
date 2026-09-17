---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.1
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Monte Carlo Agentic Access
  operation_count: 1
  slug: monte-carlo-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: GraphQL API for the Monte Carlo data observability platform. Provides programmatic access to monitors, incidents, assets, lineage, custom rules, warehouses, lakes, metastores, and alerts. Authenticati
  name: Monte Carlo GraphQL API
  slug: graphql-api
- description: A REST write API for pushing observability data into Monte Carlo from sources its pull-based collectors cannot reach. Three endpoints — POST /ingest/v1/metadata (table and view schema, columns, row an
  name: Monte Carlo Push Ingest API
  slug: push-ingest-api
- description: A first-party, fully hosted Model Context Protocol server that gives AI agents direct access to Monte Carlo — investigating alerts, exploring assets and lineage, creating and tuning monitors, and eval
  name: Monte Carlo MCP Server
  slug: mcp-server
- baseURL: https://api.getmontecarlo.com/graphql
  baseurl_source: declared
  description: The Graph QL API from Monte Carlo — 1 operation(s) for graph ql.
  name: Monte Carlo Graph QL API
  slug: monte-carlo-graph-ql-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Monte Carlo Graphql API
  slug: open-monte-carlo-graphql-api
- collection_type: open
  name: Monte Carlo GraphQL API
  slug: open-monte-carlo
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/agentic-access/monte-carlo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/monte-carlo-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/security/monte-carlo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/monte-carlo-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/security/monte-carlo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/monte-carlo-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/authentication/monte-carlo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/monte-carlo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/monte-carlo-ai
- group: company
  title: ''
  type: Website
  url: https://montecarlo.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getmontecarlo.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/monte-carlo-data
- group: commercial
  title: ''
  type: Pricing
  url: https://montecarlo.ai/request-for-pricing/
- group: start
  title: ''
  type: Signup
  url: https://montecarlo.ai/request-a-demo
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.getmontecarlo.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://montecarlo.ai/blog/feed
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.getmontecarlo.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/well-known/monte-carlo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/monte-carlo-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/well-known/monte-carlo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/monte-carlo-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/well-known/monte-carlo-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/monte-carlo-api-catalog.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/security/monte-carlo-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/monte-carlo-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/security/monte-carlo-trust-center.yml
  title: ''
  type: Compliance
  url: security/monte-carlo-trust-center.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/packages/monte-carlo-packages.yml
  title: ''
  type: Packages
  url: packages/monte-carlo-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/packages/monte-carlo-packages.yml
  title: ''
  type: SDKs
  url: packages/monte-carlo-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/cli/monte-carlo-cli.yml
  title: ''
  type: CLI
  url: cli/monte-carlo-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/changelog/monte-carlo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/monte-carlo-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.getmontecarlo.com/changelog
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/plans/monte-carlo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/monte-carlo-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/rate-limits/monte-carlo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/monte-carlo-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/lifecycle/monte-carlo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/monte-carlo-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getmontecarlo.com/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/lifecycle/monte-carlo-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/monte-carlo-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/conventions/monte-carlo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/monte-carlo-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/conformance/monte-carlo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/monte-carlo-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/webhooks/monte-carlo-webhooks.yml
  title: ''
  type: Webhooks
  url: webhooks/monte-carlo-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/llms/monte-carlo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/monte-carlo-llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getmontecarlo.com/docs/welcome
- group: commercial
  title: ''
  type: TermsOfService
  url: https://montecarlo.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://montecarlo.ai/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://getmontecarlo.com/signin/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.getmontecarlo.com/docs/developer-resources
created: '2026-05-11'
description: Monte Carlo is a data and AI observability platform that monitors data warehouses, lakes, and pipelines for freshness, volume, schema, and quality anomalies, helping data teams detect, resolve, and prevent data downtime across Snowflake, Databricks, BigQuery, Redshift, and other modern data stack tools. Monte Carlo exposes a GraphQL API at https://api.getmontecarlo.com/graphql used for programmatic access to monitors, incidents, lineage, assets, alerts, custom rules, and lake/metastore integrations, with a supporting Python SDK and CLI (pycarlo / montecarlo). Authentication uses an API Key ID and Token pair sent via headers.
graphqls:
- description: GraphQL API for the Monte Carlo data observability platform. Provides programmatic access to monitors, incidents, assets, lineage, custom rules, warehouses, lakes, metastores, and alerts. Authenticati
  name: Monte Carlo GraphQL API
  slug: monte-carlo-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/monte-carlo.png
layout: provider
mcp_servers:
- description: First-party, fully hosted Model Context Protocol server for the Monte Carlo data + AI observability platform. Lets an agent investigate alerts, explore assets and lineage, create and tune monitors, an
  name: Monte Carlo MCP Server
  slug: monte-carlo-mcp-server
modified: '2026-09-16'
name: Monte Carlo
nav: Providers
network: true
overview: 'Monte Carlo publishes 1 API on the [APIs.io](https://apis.io/) network: Graph QL API. Tagged areas include Data Observability, Data Quality, Data Reliability, Data Lake, and Data Warehouse.


  Monte Carlo''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, API reference, CLI, and 30 more developer resources.'
plans:
- name: Monte Carlo Plans Pricing
  plan_count: 4
  slug: monte-carlo-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Monte Carlo Rate Limits
  slug: monte-carlo-rate-limits
scopes:
- name: Monte Carlo Scopes
  scope_count: 6
  slug: monte-carlo-scopes
  summary_line: 6 scopes
score:
  band: exemplar
  composite: 67.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 32.9
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 59.1
    developer_ergonomics: 66.7
    discoverability: 75.9
    operational_transparency: 92.1
  previous_composite: 34.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/screenshots/monte-carlo-2026-06-20T185743.png
security:
- kind: authentication
  name: Monte Carlo Authentication
  slug: monte-carlo-authentication
  summary_line: apiKey/oauth2 · 5 schemes
- kind: domain-security
  name: Monte Carlo Domain Security
  slug: monte-carlo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Monte Carlo Vulnerability Disclosure
  slug: monte-carlo-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Monte Carlo Trust Center
  slug: monte-carlo-trust-center
  summary_line: SOC 2, ISO 27001
slug: monte-carlo
tags:
- Data Observability
- Data Quality
- Data Reliability
- Data Lake
- Data Warehouse
- Lineage
- Monitoring
- AI Observability
website: https://montecarlo.ai/
---
