---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 49
  human_in_the_loop: 2
  name: Popsink Agentic Access
  operation_count: 90
  slug: popsink-agentic-access
  summary_line: 90 operations · 49 acting · 2 human-in-the-loop
api_count: 2
apis:
- baseURL: https://app.popsink.com
  baseurl_source: declared
  description: The admin API from Popsink — 2 operation(s) for admin.
  name: Popsink Admin API
  slug: popsink-admin-api
- baseURL: https://app.popsink.com
  baseurl_source: declared
  description: The auth API from Popsink — 8 operation(s) for auth.
  name: Popsink Auth API
  slug: popsink-auth-api
- baseURL: https://app.popsink.com
  baseurl_source: declared
  description: The brokers API from Popsink — 1 operation(s) for brokers.
  name: Popsink Brokers API
  slug: popsink-brokers-api
- baseURL: https://app.popsink.com
  baseurl_source: declared
  description: The connector types API from Popsink — 3 operation(s) for connector types.
  name: Popsink connector types API
  slug: popsink-connector-types-api
- baseURL: https://app.popsink.com
  baseurl_source: declared
  description: The connectors API from Popsink — 2 operation(s) for connectors.
  name: Popsink Connectors API
  slug: popsink-connectors-api
- baseURL: https://app.popsink.com
  baseurl_source: declared
  description: The env_member API from Popsink — 2 operation(s) for env_member.
  name: Popsink Env Member API
  slug: popsink-env-member-api
- baseURL: https://app.popsink.com
  baseurl_source: declared
  description: The env_request API from Popsink — 3 operation(s) for env_request.
  name: Popsink Env Request API
  slug: popsink-env-request-api
- baseURL: https://app.popsink.com
  baseurl_source: declared
  description: The envs API from Popsink — 2 operation(s) for envs.
  name: Popsink Envs API
  slug: popsink-envs-api
- baseURL: https://app.popsink.com
  baseurl_source: declared
  description: The jobs-smt API from Popsink — 13 operation(s) for jobs-smt.
  name: Popsink Jobs Smt API
  slug: popsink-jobs-smt-api
- baseURL: https://app.popsink.com
  baseurl_source: declared
  description: The organizations API from Popsink — 2 operation(s) for organizations.
  name: Popsink Organizations API
  slug: popsink-organizations-api
- baseURL: https://app.popsink.com
  baseurl_source: declared
  description: The pipelines API from Popsink — 9 operation(s) for pipelines.
  name: Popsink Pipelines API
  slug: popsink-pipelines-api
- baseURL: https://app.popsink.com
  baseurl_source: declared
  description: The Popsink Public API API from Popsink — 1 operation(s) for popsink public api.
  name: Popsink Public API
  slug: popsink-popsink-public-api-api
- baseURL: https://app.popsink.com
  baseurl_source: declared
  description: The probes API from Popsink — 2 operation(s) for probes.
  name: Popsink Probes API
  slug: popsink-probes-api
- baseURL: https://app.popsink.com
  baseurl_source: declared
  description: The saml API from Popsink — 4 operation(s) for saml.
  name: Popsink Saml API
  slug: popsink-saml-api
- baseURL: https://app.popsink.com
  baseurl_source: declared
  description: The schemas API from Popsink — 1 operation(s) for schemas.
  name: Popsink Schemas API
  slug: popsink-schemas-api
- baseURL: https://app.popsink.com
  baseurl_source: declared
  description: The team_member API from Popsink — 3 operation(s) for team_member.
  name: Popsink Team Member API
  slug: popsink-team-member-api
- baseURL: https://app.popsink.com
  baseurl_source: declared
  description: The team_request API from Popsink — 3 operation(s) for team_request.
  name: Popsink Team Request API
  slug: popsink-team-request-api
- baseURL: https://app.popsink.com
  baseurl_source: declared
  description: The teams API from Popsink — 2 operation(s) for teams.
  name: Popsink Teams API
  slug: popsink-teams-api
- baseURL: https://app.popsink.com
  baseurl_source: declared
  description: The user-logs API from Popsink — 1 operation(s) for user-logs.
  name: Popsink User Logs API
  slug: popsink-user-logs-api
- baseURL: https://app.popsink.com
  baseurl_source: declared
  description: The users API from Popsink — 7 operation(s) for users.
  name: Popsink Users API
  slug: popsink-users-api
- baseURL: https://app.popsink.com
  baseurl_source: declared
  description: The Health Checks API from Popsink — 4 operation(s) for health checks.
  name: Popsink Health Checks API
  slug: popsink-health-checks-api
artifact_total: 50
collections:
- collection_type: open
  name: Fast admin API
  slug: open-popsink-admin-api
- collection_type: open
  name: Fast admin auth API
  slug: open-popsink-auth-api
- collection_type: open
  name: Fast admin brokers API
  slug: open-popsink-brokers-api
- collection_type: open
  name: Fast admin connector types API
  slug: open-popsink-connector-types-api
- collection_type: open
  name: Fast admin connectors API
  slug: open-popsink-connectors-api
- collection_type: open
  name: Fast admin env_member API
  slug: open-popsink-env-member-api
- collection_type: open
  name: Fast admin env_request API
  slug: open-popsink-env-request-api
- collection_type: open
  name: Fast admin envs API
  slug: open-popsink-envs-api
- collection_type: open
  name: Fast admin healthchecks API
  slug: open-popsink-healthchecks-api
- collection_type: open
  name: Fast admin jobs-smt API
  slug: open-popsink-jobs-smt-api
- collection_type: open
  name: Fast admin organizations API
  slug: open-popsink-organizations-api
- collection_type: open
  name: Fast admin pipelines API
  slug: open-popsink-pipelines-api
- collection_type: open
  name: Fast admin Popsink Public API API
  slug: open-popsink-popsink-public-api-api
- collection_type: open
  name: Fast admin probes API
  slug: open-popsink-probes-api
- collection_type: open
  name: Fast admin saml API
  slug: open-popsink-saml-api
- collection_type: open
  name: Fast admin schemas API
  slug: open-popsink-schemas-api
- collection_type: open
  name: Fast admin team_member API
  slug: open-popsink-team-member-api
- collection_type: open
  name: Fast admin team_request API
  slug: open-popsink-team-request-api
- collection_type: open
  name: Fast admin teams API
  slug: open-popsink-teams-api
- collection_type: open
  name: Fast admin user-logs API
  slug: open-popsink-user-logs-api
- collection_type: open
  name: Fast admin users API
  slug: open-popsink-users-api
common:
- group: commercial
  href: https://artifacts.apis.io/popsink/plans/popsink-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/popsink-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/popsink/capabilities/popsink-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/popsink-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/popsink/overlays/popsink-onprem-api-overlay.yaml
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
  href: https://artifacts.apis.io/popsink/changelog/popsink-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/popsink-changelog.yml
- group: auth
  href: https://artifacts.apis.io/popsink/authentication/popsink-authentication.yml
  title: ''
  type: Authentication
  url: authentication/popsink-authentication.yml
- group: design
  href: https://artifacts.apis.io/popsink/conventions/popsink-conventions.yml
  title: ''
  type: Conventions
  url: conventions/popsink-conventions.yml
- group: design
  href: https://artifacts.apis.io/popsink/errors/popsink-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/popsink-problem-types.yml
- group: design
  href: https://artifacts.apis.io/popsink/lifecycle/popsink-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/popsink-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/popsink/data-model/popsink-data-model.yml
  title: ''
  type: DataModel
  url: data-model/popsink-data-model.yml
- group: design
  href: https://artifacts.apis.io/popsink/conformance/popsink-conformance.yml
  title: ''
  type: Conformance
  url: conformance/popsink-conformance.yml
- group: agent
  href: https://artifacts.apis.io/popsink/mcp/popsink-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/popsink-mcp.yml
- group: agent
  href: https://artifacts.apis.io/popsink/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/popsink/agentic-access/popsink-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/popsink-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/popsink/llms/popsink-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/popsink-llms.txt
- group: auth
  href: https://artifacts.apis.io/popsink/security/popsink-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/popsink-domain-security.yml
created: '2026-07-17'
description: Popsink is a real-time data replication and change data capture (CDC) platform that continuously moves data out of mission-critical and legacy systems into cloud data platforms with low latency and minimal production impact. It offers a broad catalog of source and target connectors (Postgres, MySQL, Oracle, MSSQL, MongoDB, Kafka, IBM Z / IBMi (AS/400), SAP, Salesforce, HubSpot, Snowflake, BigQuery, Databricks, ClickHouse, Iceberg, and more) and flexible deployment options spanning SaaS, bring-your-own-cloud, self-hosted Kubernetes, single-VM, on-premises, and air-gapped installs. Popsink exposes a public REST API and an on-prem control-plane REST API (OAuth2 password / JWT bearer, with SAML SSO) for managing pipelines, connectors, environments, teams, schemas, and transforms. Backed by Seedcamp.
finops:
- has_sources: true
  method: derived
  name: Popsink Finops
  primary_unit: million monthly transactions
  service_category: ''
  slug: popsink-finops
  template: false
image: https://cdn.prod.website-files.com/68c803b0497f18f5503b81d9/68c84fa4ed5fa62ff869c94f_Fav%20Icon%20256x256.png
layout: provider
modified: '2026-09-16'
name: Popsink
nav: Providers
network: true
overview: 'Popsink publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Auth API, Brokers API, and 18 more. Tagged areas include Company, Change Data Capture, Data Replication, Data Integration, and Real-Time Data.


  The Popsink catalog on APIs.io includes 1 Spectral governance ruleset.


  Popsink''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 22 more developer resources.'
plans:
- name: Popsink Plans Pricing
  plan_count: 9
  slug: popsink-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Popsink API Rules
  rule_count: 50
  severity_counts:
    error: 36
    hint: 0
    info: 7
    warn: 7
  slug: popsink-rules
score:
  band: developing
  composite: 50.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 43.0
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 28.9
  previous_composite: 50.7
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/popsink/popsink-2026-08-17T081318.png
security:
- kind: authentication
  name: Popsink Authentication
  slug: popsink-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Popsink Domain Security
  slug: popsink-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: Create a Popsink replication pipeline
  slug: popsink-create-replication-pipeline
- name: Operate and monitor a Popsink pipeline
  slug: popsink-operate-pipeline
slug: popsink
tags:
- Company
- Change Data Capture
- Data Replication
- Data Integration
- Real-Time Data
- Streaming
- ETL
- Database
- Data Platform
website: https://popsink.com
---
