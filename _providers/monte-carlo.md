---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: unknown
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 58.6
  scored_at: '2026-11-06'
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
  phrasing_intents:
  - id: graphql
    intent: Run a GraphQL query or mutation against Monte Carlo
    question: How do I pull my data incidents and monitors out of Monte Carlo programmatically?
  phrasing_ops: 1
  slug: monte-carlo-graph-ql-api
artifact_total: 37
collections:
- collection_type: open
  name: Monte Carlo Graphql API
  slug: open-monte-carlo-graphql-api
- collection_type: open
  name: Monte Carlo GraphQL API
  slug: open-monte-carlo
common:
- group: other
  href: https://artifacts.apis.io/monte-carlo/overlays/monte-carlo-graph-ql-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/monte-carlo-graph-ql-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/monte-carlo/agentic-access/monte-carlo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/monte-carlo-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/monte-carlo/security/monte-carlo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/monte-carlo-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/monte-carlo/security/monte-carlo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/monte-carlo-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/monte-carlo/authentication/monte-carlo-authentication.yml
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
  href: https://artifacts.apis.io/monte-carlo/well-known/monte-carlo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/monte-carlo-well-known.yml
- group: auth
  href: https://artifacts.apis.io/monte-carlo/well-known/monte-carlo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/monte-carlo-security.txt
- group: other
  href: https://artifacts.apis.io/monte-carlo/well-known/monte-carlo-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/monte-carlo-api-catalog.json
- group: auth
  href: https://artifacts.apis.io/monte-carlo/security/monte-carlo-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/monte-carlo-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/monte-carlo/security/monte-carlo-trust-center.yml
  title: ''
  type: Compliance
  url: security/monte-carlo-trust-center.yml
- group: build
  href: https://artifacts.apis.io/monte-carlo/packages/monte-carlo-packages.yml
  title: ''
  type: Packages
  url: packages/monte-carlo-packages.yml
- group: build
  href: https://artifacts.apis.io/monte-carlo/packages/monte-carlo-packages.yml
  title: ''
  type: SDKs
  url: packages/monte-carlo-packages.yml
- group: build
  href: https://artifacts.apis.io/monte-carlo/cli/monte-carlo-cli.yml
  title: ''
  type: CLI
  url: cli/monte-carlo-cli.yml
- group: operate
  href: https://artifacts.apis.io/monte-carlo/changelog/monte-carlo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/monte-carlo-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.getmontecarlo.com/changelog
- group: commercial
  href: https://artifacts.apis.io/monte-carlo/plans/monte-carlo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/monte-carlo-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/monte-carlo/rate-limits/monte-carlo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/monte-carlo-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/monte-carlo/lifecycle/monte-carlo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/monte-carlo-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getmontecarlo.com/
- group: operate
  href: https://artifacts.apis.io/monte-carlo/lifecycle/monte-carlo-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/monte-carlo-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/monte-carlo/conventions/monte-carlo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/monte-carlo-conventions.yml
- group: design
  href: https://artifacts.apis.io/monte-carlo/conformance/monte-carlo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/monte-carlo-conformance.yml
- group: design
  href: https://artifacts.apis.io/monte-carlo/webhooks/monte-carlo-webhooks.yml
  title: ''
  type: Webhooks
  url: webhooks/monte-carlo-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/monte-carlo/llms/monte-carlo-llms.txt
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
- group: company
  title: ''
  type: Blog
  url: https://montecarlo.ai/blog
created: '2026-05-11'
description: Monte Carlo is a data and AI observability platform that monitors data warehouses, lakes, and pipelines for freshness, volume, schema, and quality anomalies, helping data teams detect, resolve, and prevent data downtime across Snowflake, Databricks, BigQuery, Redshift, and other modern data stack tools. Monte Carlo exposes a GraphQL API at https://api.getmontecarlo.com/graphql used for programmatic access to monitors, incidents, lineage, assets, alerts, custom rules, and lake/metastore integrations, with a supporting Python SDK and CLI (pycarlo / montecarlo). Authentication uses an API Key ID and Token pair sent via headers.
finops:
- has_sources: true
  method: derived
  name: Monte Carlo Finops
  primary_unit: ''
  service_category: ''
  slug: monte-carlo-finops
  template: true
graphqls:
- description: GraphQL API for the Monte Carlo data observability platform. Provides programmatic access to monitors, incidents, assets, lineage, custom rules, warehouses, lakes, metastores, and alerts. Authenticati
  name: Monte Carlo GraphQL API
  slug: monte-carlo-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/monte-carlo.png
layout: provider
mcp_servers:
- description: First-party, fully hosted Model Context Protocol server for the Monte Carlo data + AI observability platform. Lets an agent investigate alerts, explore assets and lineage, create and tune monitors, an
  name: Monte Carlo MCP Server
  slug: monte-carlo
modified: '2026-09-16'
name: Monte Carlo
nav: Providers
network: true
overview: 'Monte Carlo publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Graph QL API, and 3 more. Tagged areas include Data Observability, Data Quality, Data Reliability, Data Lake, and Data Warehouse.


  The Monte Carlo catalog on APIs.io includes 1 Spectral governance ruleset.


  Monte Carlo''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, API reference, CLI, and 32 more developer resources.'
plans:
- name: Monte Carlo Plans Pricing
  plan_count: 4
  slug: monte-carlo-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Monte Carlo Rate Limits
  slug: monte-carlo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Monte Carlo API Rules
  rule_count: 48
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 1
  slug: monte-carlo-rules
scopes:
- name: Monte Carlo Scopes
  scope_count: 6
  slug: monte-carlo-scopes
  summary_line: 6 scopes
score:
  band: exemplar
  composite: 71.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 65.5
    catalog_earned_first_party: 24.0
    catalog_gap: 49.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.2
  facets:
    access_clarity: 85.5
    contract_governance: 31.8
    contract_quality: 53.2
    developer_ergonomics: 73.8
    discoverability: 75.0
    operational_transparency: 92.1
  previous_composite: 69.2
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/monte-carlo/monte-carlo-2026-06-20T185743.png
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
skill_count: 19
skills:
- name: monte-carlo-analyze-root-cause
  slug: monte-carlo-analyze-root-cause
- name: monte-carlo-asset-health
  slug: monte-carlo-asset-health
- name: automated-triage
  slug: monte-carlo-automated-triage
- name: connection-auth-rules
  slug: monte-carlo-connection-auth-rules
- name: monte-carlo-context-detection
  slug: monte-carlo-context-detection
- name: generate-validation-notebook
  slug: monte-carlo-generate-validation-notebook
- name: monte-carlo-incident-response
  slug: monte-carlo-incident-response
- name: monte-carlo-instrument-agent
  slug: monte-carlo-instrument-agent
- name: monte-carlo-manage-mac
  slug: monte-carlo-manage-mac
- name: monte-carlo-monitoring-advisor
  slug: monte-carlo-monitoring-advisor
- name: monte-carlo-performance-diagnosis
  slug: monte-carlo-performance-diagnosis
- name: monte-carlo-prevent
  slug: monte-carlo-prevent
- name: monte-carlo-proactive-monitoring
  slug: monte-carlo-proactive-monitoring
- name: push-ingestion
  slug: monte-carlo-push-ingestion
- name: monte-carlo-reinforce-agent
  slug: monte-carlo-reinforce-agent
- name: monte-carlo-remediation
  slug: monte-carlo-remediation
- name: monte-carlo-storage-cost-analysis
  slug: monte-carlo-storage-cost-analysis
- name: monte-carlo-troubleshoot-agent-traces
  slug: monte-carlo-troubleshoot-agent-traces
- name: tune-monitor
  slug: monte-carlo-tune-monitor
slug: monte-carlo
tags:
- Data Observability
- Data Quality
- Data Reliability
- Data Lake
- Data Warehouse
- Data Lineage
- Monitoring
- AI Observability
- Data Monitoring
- GraphQL
website: https://montecarlo.ai/
---
