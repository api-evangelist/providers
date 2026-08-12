---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 49
  human_in_the_loop: 2
  name: Popsink Agentic Access
  operation_count: 90
  slug: popsink-agentic-access
  summary_line: 90 operations · 49 acting · 2 human-in-the-loop
api_count: 21
apis:
- description: The admin API from Popsink — 2 operation(s) for admin.
  name: Popsink admin API
  slug: popsink-admin-api
- description: The auth API from Popsink — 8 operation(s) for auth.
  name: Popsink auth API
  slug: popsink-auth-api
- description: The brokers API from Popsink — 1 operation(s) for brokers.
  name: Popsink brokers API
  slug: popsink-brokers-api
- description: The connector types API from Popsink — 3 operation(s) for connector types.
  name: Popsink connector types API
  slug: popsink-connector-types-api
- description: The connectors API from Popsink — 2 operation(s) for connectors.
  name: Popsink connectors API
  slug: popsink-connectors-api
- description: The env_member API from Popsink — 2 operation(s) for env_member.
  name: Popsink env_member API
  slug: popsink-env-member-api
- description: The env_request API from Popsink — 3 operation(s) for env_request.
  name: Popsink env_request API
  slug: popsink-env-request-api
- description: The envs API from Popsink — 2 operation(s) for envs.
  name: Popsink envs API
  slug: popsink-envs-api
- description: The healthchecks API from Popsink — 4 operation(s) for healthchecks.
  name: Popsink healthchecks API
  slug: popsink-healthchecks-api
- description: The jobs-smt API from Popsink — 13 operation(s) for jobs-smt.
  name: Popsink jobs-smt API
  slug: popsink-jobs-smt-api
- description: The organizations API from Popsink — 2 operation(s) for organizations.
  name: Popsink organizations API
  slug: popsink-organizations-api
- description: The pipelines API from Popsink — 9 operation(s) for pipelines.
  name: Popsink pipelines API
  slug: popsink-pipelines-api
- description: The Popsink Public API API from Popsink — 1 operation(s) for popsink public api.
  name: Popsink Popsink Public API API
  slug: popsink-popsink-public-api-api
- description: The probes API from Popsink — 2 operation(s) for probes.
  name: Popsink probes API
  slug: popsink-probes-api
- description: The saml API from Popsink — 4 operation(s) for saml.
  name: Popsink saml API
  slug: popsink-saml-api
- description: The schemas API from Popsink — 1 operation(s) for schemas.
  name: Popsink schemas API
  slug: popsink-schemas-api
- description: The team_member API from Popsink — 3 operation(s) for team_member.
  name: Popsink team_member API
  slug: popsink-team-member-api
- description: The team_request API from Popsink — 3 operation(s) for team_request.
  name: Popsink team_request API
  slug: popsink-team-request-api
- description: The teams API from Popsink — 2 operation(s) for teams.
  name: Popsink teams API
  slug: popsink-teams-api
- description: The user-logs API from Popsink — 1 operation(s) for user-logs.
  name: Popsink user-logs API
  slug: popsink-user-logs-api
- description: The users API from Popsink — 7 operation(s) for users.
  name: Popsink users API
  slug: popsink-users-api
artifact_total: 25
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/popsink-onprem-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://popsink.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.popsink.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.popsink.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.popsink.com/public/public-api.json
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.popsink.com/quickstart
- group: company
  title: ''
  type: Blog
  url: https://popsink.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://popsink.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.popsink.com
- group: start
  title: ''
  type: Login
  url: https://app.popsink.com
- group: operate
  title: ''
  type: Support
  url: https://popsink.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://popsink.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://popsink.com/privacy-policy
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.popsink.com/roadmap
- group: operate
  title: ''
  type: StatusPage
  url: https://status.popsink.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/popsink-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/popsink-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/popsink-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/popsink-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/popsink-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/popsink-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/popsink-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/popsink-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/popsink-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/popsink-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/popsink-domain-security.yml
created: '2026-07-17'
description: Popsink is a real-time data replication and change data capture (CDC) platform that continuously moves data out of mission-critical and legacy systems into cloud data platforms with low latency and minimal production impact. It offers a broad catalog of source and target connectors (Postgres, MySQL, Oracle, MSSQL, MongoDB, Kafka, IBM Z / IBMi (AS/400), SAP, Salesforce, HubSpot, Snowflake, BigQuery, Databricks, ClickHouse, Iceberg, and more) and flexible deployment options spanning SaaS, bring-your-own-cloud, self-hosted Kubernetes, single-VM, on-premises, and air-gapped installs. Popsink exposes a public REST API and an on-prem control-plane REST API (OAuth2 password / JWT bearer, with SAML SSO) for managing pipelines, connectors, environments, teams, schemas, and transforms. Backed by Seedcamp.
image: https://cdn.prod.website-files.com/68c803b0497f18f5503b81d9/68c84fa4ed5fa62ff869c94f_Fav%20Icon%20256x256.png
layout: provider
mcp_servers:
- description: ''
  name: popsink-mcp.yml
  slug: popsink-mcpyml
modified: '2026-07-20'
name: Popsink
nav: Providers
network: true
overview: 'Popsink publishes 21 APIs on the [APIs.io](https://apis.io/) network, including admin API, auth API, brokers API, and 18 more. Tagged areas include Company, Change Data Capture, Data Replication, CDC, and Data Integration.


  Popsink''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 20 more developer resources.'
random_paper: 76
score:
  band: developing
  composite: 47.1
  delta: -1.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 50.6
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Popsink Authentication
  slug: popsink-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Popsink Domain Security
  slug: popsink-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: popsink
tags:
- Company
- Change Data Capture
- Data Replication
- CDC
- Data Integration
- Real-Time Data
- Streaming
- ETL
- Database
- Data Platform
website: https://popsink.com
---
