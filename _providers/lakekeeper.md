---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.6
  scored_at: '2026-09-05'
api_count: 3
apis:
- baseURL: '{scheme}://{host}/lakekeeper/v1'
  baseurl_source: declared
  description: Lakekeeper's data-plane API served under /lakekeeper/v1, cataloging non-Iceberg table formats — Lance, Delta, CSV, Parquet — alongside Iceberg tables in the same Warehouse and Namespace, with the same
  name: Lakekeeper Generic Table (Data) API
  slug: lakekeeper-generic-table-data-api
- baseURL: '{scheme}://{host}/management/v1'
  baseurl_source: declared
  description: The authorization API from Lakekeeper — 1 operation(s) for authorization.
  name: Lakekeeper Authorization API
  slug: lakekeeper-authorization-api
- baseURL: '{scheme}://{host}/management/v1'
  baseurl_source: declared
  description: The Catalog API API from Lakekeeper — 16 operation(s) for catalog api.
  name: Lakekeeper Catalog API
  slug: lakekeeper-catalog-api-api
- baseURL: '{scheme}://{host}/management/v1'
  baseurl_source: declared
  description: The Configuration API API from Lakekeeper — 1 operation(s) for configuration api.
  name: Lakekeeper Configuration API
  slug: lakekeeper-configuration-api-api
- baseURL: '{scheme}://{host}/management/v1'
  baseurl_source: declared
  description: The OAuth2 API API from Lakekeeper — 1 operation(s) for oauth2 api.
  name: Lakekeeper OAuth2 API
  slug: lakekeeper-oauth2-api-api
- baseURL: '{scheme}://{host}/management/v1'
  baseurl_source: declared
  description: Cedar Authorization Management. Only available if Cedar authorization is enabled.
  name: Lakekeeper Permissions Cedar API
  slug: lakekeeper-permissions-cedar-api
- baseURL: '{scheme}://{host}/management/v1'
  baseurl_source: declared
  description: Authorization and permissions management using OpenFGA
  name: Lakekeeper Permissions Openfga API
  slug: lakekeeper-permissions-openfga-api
- baseURL: '{scheme}://{host}/management/v1'
  baseurl_source: declared
  description: Manage Projects
  name: Lakekeeper Project API
  slug: lakekeeper-project-api
- baseURL: '{scheme}://{host}/management/v1'
  baseurl_source: declared
  description: Manage Roles
  name: Lakekeeper Role API
  slug: lakekeeper-role-api
- baseURL: '{scheme}://{host}/management/v1'
  baseurl_source: declared
  description: Manage Server
  name: Lakekeeper Server API
  slug: lakekeeper-server-api
- baseURL: '{scheme}://{host}/management/v1'
  baseurl_source: declared
  description: View & Manage Tasks
  name: Lakekeeper Tasks API
  slug: lakekeeper-tasks-api
- baseURL: '{scheme}://{host}/management/v1'
  baseurl_source: declared
  description: Manage Users
  name: Lakekeeper User API
  slug: lakekeeper-user-api
- baseURL: '{scheme}://{host}/management/v1'
  baseurl_source: declared
  description: Manage Warehouses
  name: Lakekeeper Warehouse API
  slug: lakekeeper-warehouse-api
artifact_total: 19
asyncapis:
- description: ''
  name: Lakekeeper Events
  slug: lakekeeper-events
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lakekeeper-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lakekeeper.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lakekeeper.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lakekeeper.io/docs/latest/api-overview/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lakekeeper.io/docs/latest/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lakekeeper.io/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://docs.lakekeeper.io/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lakekeeper
- group: company
  title: ''
  type: Blog
  url: https://vakamo.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://vakamo.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.lakekeeper.io/about/license/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.lakekeeper.io/about/release-notes/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.lakekeeper.io/llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/lakekeeper-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lakekeeper-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lakekeeper-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/lakekeeper-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lakekeeper-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lakekeeper-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lakekeeper-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lakekeeper-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/lakekeeper-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lakekeeper-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/lakekeeper-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lakekeeper-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/lakekeeper-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lakekeeper-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lakekeeper-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lakekeeper-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/lakekeeper-management-api-overlay.yaml
created: '2026-08-27'
description: Lakekeeper is an open-source Apache Iceberg REST Catalog written in Rust and maintained by Vakamo. It manages Iceberg tables, views and namespaces for query engines such as Apache Spark, Trino, StarRocks, DuckDB, Athena, Flink and PyIceberg, vending short-lived, prefix-scoped storage credentials for S3, GCS, Azure ADLS and Microsoft OneLake/Fabric instead of handing long-lived keys to engines. It exposes three distinct HTTP APIs — the standard Iceberg REST Catalog API at /catalog/v1, a Lakekeeper-specific Management API at /management/v1 for bootstrapping, projects, warehouses, users, roles, tasks and fine-grained permissions, and a Data API at /lakekeeper/v1 that catalogs non-Iceberg generic tables such as Lance, Delta and Parquet. Authorization is pluggable (OpenFGA for RBAC/ ReBAC, Open Policy Agent bridge, Cedar in the commercial Lakekeeper+ distribution), authentication is OIDC/OAuth2 or Kubernetes service accounts, and change events are published as CloudEvents to Kafka
  or NATS. Lakekeeper is self-hosted software under Apache 2.0; commercial Lakekeeper+ and Lakekeeper Cloud are sold by Vakamo.
image: https://docs.lakekeeper.io/assets/logos/LAKEKEEPER_IMAGE_TEXT_SIDE.svg
layout: provider
modified: '2026-08-27'
name: Lakekeeper
nav: Providers
network: true
overview: 'Lakekeeper publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Generic Table (Data) API, Authorization API, Catalog API, and 10 more. Tagged areas include Apache Iceberg, Data Catalog, Lakehouse, Open-Source, and Rust.


  The Lakekeeper catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lakekeeper''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 24 more developer resources.'
plans:
- name: Lakekeeper Plans Pricing
  plan_count: 3
  slug: lakekeeper-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Lakekeeper Rate Limits
  slug: lakekeeper-rate-limits
scopes:
- name: Lakekeeper Scopes
  scope_count: 1
  slug: lakekeeper-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 54.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 59.5
    developer_ergonomics: 80.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 54.2
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 7.1
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lakekeeper/refs/heads/main/screenshots/lakekeeper-2026-09-02T150205.png
security:
- kind: authentication
  name: Lakekeeper Authentication
  slug: lakekeeper-authentication
  summary_line: http/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Lakekeeper Domain Security
  slug: lakekeeper-domain-security
  summary_line: TLSv1.3 · HSTS
slug: lakekeeper
tags:
- Apache Iceberg
- Data Catalog
- Lakehouse
- Open-Source
- Rust
- Data Governance
- Access Control
- Object Storage
- Metadata
- Self-Hosted
- openfga
- Data Engineering
website: https://lakekeeper.io/
---
