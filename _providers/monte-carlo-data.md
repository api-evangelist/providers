---
access_model:
  confidence: high
  label: Enterprise, sales-quoted
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - https://montecarlo.ai/request-for-pricing/
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.3
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: Monte Carlo's single GraphQL endpoint. Every piece of information the web application presents can be retrieved and mutated programmatically — alerts and incidents, monitors and monitors-as-code, asse
  name: Monte Carlo GraphQL API
  slug: monte-carlo-data
- description: A REST write API for pushing observability data into Monte Carlo from sources its pull-based collectors cannot reach. Three endpoints — POST /ingest/v1/metadata (table and view schema, columns, row an
  name: Monte Carlo Push Ingest API
  slug: push-ingest-api
- description: A first-party, fully hosted Model Context Protocol server that gives AI agents direct access to Monte Carlo — investigating alerts, exploring assets and lineage, creating and tuning monitors, and eval
  name: Monte Carlo MCP Server
  slug: mcp-server
artifact_total: 13
asyncapis:
- description: ''
  name: Monte Carlo Data Webhooks
  slug: monte-carlo-data-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.montecarlodata.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.getmontecarlo.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getmontecarlo.com
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.getmontecarlo.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getmontecarlo.com/docs/welcome
- group: company
  title: ''
  type: Blog
  url: https://montecarlodata.com/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/monte-carlo-data
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/monte-carlo-data
- group: commercial
  title: ''
  type: Pricing
  url: https://montecarlo.ai/request-for-pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://montecarlo.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://montecarlo.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getmontecarlo.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.getmontecarlo.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/monte-carlo-data-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/monte-carlo-data-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/monte-carlo-data-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/monte-carlo-data-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/monte-carlo-data-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/monte-carlo-data-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/monte-carlo-data-security.txt
- group: auth
  title: ''
  type: Security
  url: security/monte-carlo-data-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/monte-carlo-data-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/monte-carlo-data-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/monte-carlo-data-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monte-carlo-data-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/monte-carlo-data-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/monte-carlo-data-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/monte-carlo-data-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/monte-carlo-data-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/monte-carlo-data-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/monte-carlo-data-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/monte-carlo-data-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/monte-carlo-data-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/monte-carlo-data-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-03-27'
description: Monte Carlo is the data + AI observability platform that detects, resolves and prevents data quality incidents across warehouses, lakes, BI tools, ETL orchestrators and, increasingly, AI agents. Its programmatic surface is a single GraphQL API at api.getmontecarlo.com/graphql that exposes everything the web app shows — alerts, incidents, monitors, assets, table and column lineage, query history and job performance — alongside a REST Push Ingest API at integrations.getmontecarlo.com for pushing metadata, lineage and query logs from sources the pull-based collectors cannot reach. Monte Carlo also runs a first-party hosted MCP server with 56 documented tools and OAuth 2.1 dynamic client registration, publishes 19 Apache-2.0 Agent Skills for coding agents, and ships a Python SDK (pycarlo), a CLI (montecarlodata) and an OpenTelemetry SDK for agent tracing. The company rebranded its web presence to montecarlo.ai during 2026; montecarlodata.com still resolves and serves the same content.
finops:
- name: Monte Carlo Data Finops
  service_category: API
  slug: monte-carlo-data-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/monte-carlo-data.png
layout: provider
mcp_servers:
- description: A first-party, fully hosted Model Context Protocol server that exposes Monte Carlo's data + AI observability platform to agents — alerts, monitors, assets, lineage, query and job performance, and AI a
  name: Monte Carlo MCP Server
  slug: monte-carlo-mcp-server
modified: '2026-08-29'
name: Monte Carlo
nav: Providers
network: true
overview: 'Monte Carlo publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AIOps, Data Observability, Data Quality, Data Lineage, and Agent Observability.


  The Monte Carlo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Monte Carlo''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, changelog, CLI, and 28 more developer resources.'
plans:
- name: Monte Carlo Data Plans Pricing
  plan_count: 0
  slug: monte-carlo-data-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Monte Carlo Data Rate Limits
  slug: monte-carlo-data-rate-limits
scopes:
- name: Monte Carlo Data Scopes
  scope_count: 0
  slug: monte-carlo-data-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.5
  coverage:
    artifact_dirs: 20
    catalog_gap: 72.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 63.1
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 50.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/monte-carlo-data/refs/heads/main/screenshots/monte-carlo-data-2026-06-20T185743.png
security:
- kind: authentication
  name: Monte Carlo Data Authentication
  slug: monte-carlo-data-authentication
  summary_line: 6 schemes
- kind: domain-security
  name: Monte Carlo Data Domain Security
  slug: monte-carlo-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Monte Carlo Data Vulnerability Disclosure
  slug: monte-carlo-data-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Monte Carlo Data Trust Center
  slug: monte-carlo-data-trust-center
  summary_line: SOC 2, ISO 27001
slug: monte-carlo-data
tags:
- AIOps
- Data Observability
- Data Quality
- Data Lineage
- Agent Observability
- Monitoring
- GraphQL
- MCP
- OpenTelemetry
- Data Engineering
website: https://www.montecarlodata.com
---
