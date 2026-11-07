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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.5
  scored_at: '2026-11-06'
api_count: 4
apis:
- baseURL: https://api.tiledb.com/v1
  baseurl_source: declared
  description: The array API from TileDB — 29 operation(s) for array.
  name: TileDB Array API
  slug: tiledb-array-api
- baseURL: https://api.tiledb.com/v1
  baseurl_source: declared
  description: The array_tasks API from TileDB — 1 operation(s) for array_tasks.
  name: TileDB Array Tasks API
  slug: tiledb-array-tasks-api
- baseURL: https://api.tiledb.com/v1
  baseurl_source: declared
  description: The assets API from TileDB — 3 operation(s) for assets.
  name: TileDB Assets API
  slug: tiledb-assets-api
- baseURL: https://api.tiledb.com/v1
  baseurl_source: declared
  description: The favorites API from TileDB — 12 operation(s) for favorites.
  name: TileDB Favorites API
  slug: tiledb-favorites-api
- baseURL: https://api.tiledb.com/v1
  baseurl_source: declared
  description: The files API from TileDB — 4 operation(s) for files.
  name: TileDB Files API
  slug: tiledb-files-api
- baseURL: https://api.tiledb.com/v1
  baseurl_source: declared
  description: The groups API from TileDB — 17 operation(s) for groups.
  name: TileDB Groups API
  slug: tiledb-groups-api
- baseURL: https://api.tiledb.com/v1
  baseurl_source: declared
  description: The invitation API from TileDB — 10 operation(s) for invitation.
  name: TileDB Invitation API
  slug: tiledb-invitation-api
- baseURL: https://api.tiledb.com/v1
  baseurl_source: declared
  description: The notebook API from TileDB — 5 operation(s) for notebook.
  name: TileDB Notebook API
  slug: tiledb-notebook-api
- baseURL: https://api.tiledb.com/v1
  baseurl_source: declared
  description: The notebooks API from TileDB — 3 operation(s) for notebooks.
  name: TileDB Notebooks API
  slug: tiledb-notebooks-api
- baseURL: https://api.tiledb.com/v1
  baseurl_source: declared
  description: The organization API from TileDB — 13 operation(s) for organization.
  name: TileDB Organization API
  slug: tiledb-organization-api
- baseURL: https://api.tiledb.com/v1
  baseurl_source: declared
  description: The query API from TileDB — 5 operation(s) for query.
  name: TileDB Query API
  slug: tiledb-query-api
- baseURL: https://api.tiledb.com/v1
  baseurl_source: declared
  description: The registered_task_graphs API from TileDB — 2 operation(s) for registered_task_graphs.
  name: TileDB Registered Task Graphs API
  slug: tiledb-registered-task-graphs-api
- baseURL: https://api.tiledb.com/v1
  baseurl_source: declared
  description: The sql API from TileDB — 1 operation(s) for sql.
  name: TileDB Sql API
  slug: tiledb-sql-api
- baseURL: https://api.tiledb.com/v1
  baseurl_source: declared
  description: The stats API from TileDB — 1 operation(s) for stats.
  name: TileDB Stats API
  slug: tiledb-stats-api
- baseURL: https://api.tiledb.com/v1
  baseurl_source: declared
  description: The task_graph_logs API from TileDB — 8 operation(s) for task_graph_logs.
  name: TileDB Task Graph Logs API
  slug: tiledb-task-graph-logs-api
- baseURL: https://api.tiledb.com/v1
  baseurl_source: declared
  description: The task_graphs API from TileDB — 3 operation(s) for task_graphs.
  name: TileDB Task Graphs API
  slug: tiledb-task-graphs-api
- baseURL: https://api.tiledb.com/v1
  baseurl_source: declared
  description: The tasks API from TileDB — 4 operation(s) for tasks.
  name: TileDB Tasks API
  slug: tiledb-tasks-api
- baseURL: https://api.tiledb.com/v1
  baseurl_source: declared
  description: The udf API from TileDB — 7 operation(s) for udf.
  name: TileDB Udf API
  slug: tiledb-udf-api
- baseURL: https://api.tiledb.com/v1
  baseurl_source: declared
  description: The user API from TileDB — 16 operation(s) for user.
  name: TileDB User API
  slug: tiledb-user-api
artifact_total: 30
common:
- group: other
  href: https://artifacts.apis.io/tiledb/capabilities/tiledb-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/tiledb-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/tiledb/overlays/tiledb-cloud-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tiledb-cloud-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/tiledb/overlays/tiledb-cloud-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tiledb-cloud-v2-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/tiledb/security/tiledb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tiledb-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/tiledb/scopes/tiledb-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/tiledb-scopes.yml
- group: auth
  href: https://artifacts.apis.io/tiledb/authentication/tiledb-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tiledb-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.tiledb.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documentation.cloud.tiledb.com/academy/home/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.cloud.tiledb.com/academy/home/
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.cloud.tiledb.com/academy/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.cloud.tiledb.com/academy/get-started/
- group: operate
  title: ''
  type: Support
  url: https://forum.tiledb.com/
- group: company
  title: ''
  type: Blog
  url: https://www.tiledb.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TileDB-Inc
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tiledb.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.tiledb.com/auth/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tiledb.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tiledb.com/privacy-policy
- group: build
  href: https://artifacts.apis.io/tiledb/packages/tiledb-packages.yml
  title: ''
  type: Packages
  url: packages/tiledb-packages.yml
- group: build
  href: https://artifacts.apis.io/tiledb/packages/tiledb-packages.yml
  title: ''
  type: SDKs
  url: packages/tiledb-packages.yml
- group: agent
  href: https://artifacts.apis.io/tiledb/llms/tiledb-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tiledb-llms.txt
- group: design
  href: https://artifacts.apis.io/tiledb/conformance/tiledb-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tiledb-conformance.yml
- group: design
  href: https://artifacts.apis.io/tiledb/errors/tiledb-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tiledb-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tiledb/lifecycle/tiledb-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tiledb-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/tiledb/conventions/tiledb-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tiledb-conventions.yml
- group: operate
  href: https://artifacts.apis.io/tiledb/changelog/tiledb-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tiledb-changelog.yml
- group: build
  href: https://artifacts.apis.io/tiledb/cli/tiledb-cli.yml
  title: ''
  type: CLI
  url: cli/tiledb-cli.yml
- group: design
  href: https://artifacts.apis.io/tiledb/components/tiledb-components.yml
  title: ''
  type: Components
  url: components/tiledb-components.yml
- group: design
  href: https://artifacts.apis.io/tiledb/data-model/tiledb-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tiledb-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/tiledb/plans/tiledb-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tiledb-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/tiledb/rate-limits/tiledb-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tiledb-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/tiledb/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-30'
description: TileDB, Inc. builds a multimodal database around a single universal data model — the multi-dimensional array — that stores tables, genomics (VCF), single-cell (SOMA), biomedical imaging, vector embeddings, point clouds, files and ML models in one cloud-native format on S3, Azure Blob, GCS, Lustre or MinIO. The open-source TileDB Embedded storage engine is paired with TileDB Cloud (and the Carrara product line), a hosted and self-hostable platform for cataloging, sharing, governing and querying those assets, with serverless SQL, user-defined functions, task graphs, Jupyter notebooks and dashboards. The platform is programmable through the TileDB Storage Platform REST API (v1 and v2, whose Swagger 2.0 contracts TileDB publishes openly on GitHub), plus first-party clients for Python, R, Java, Go, C, C++, C#, JavaScript and Rust. The company is focused on life sciences and precision medicine.
finops:
- has_sources: true
  method: derived
  name: Tiledb Finops
  primary_unit: seat
  service_category: ''
  slug: tiledb-finops
  template: false
image: https://images.ctfassets.net/nxe07oerbx6d/PTO0pDBxwkIxfaGzEiHPi/931e190a336eebdedc825cba1723b96b/TileDB-homepage-meta.jpg
layout: provider
modified: '2026-08-30'
name: TileDB
nav: Providers
network: true
overview: 'TileDB publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Array API, Array Tasks API, Assets API, and 16 more. Tagged areas include Company, Database, Multimodal Data, Life Sciences, and Genomics.


  The TileDB catalog on APIs.io includes 1 Spectral governance ruleset.


  TileDB''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 25 more developer resources.'
plans:
- name: Tiledb Plans Pricing
  plan_count: 3
  slug: tiledb-plans-pricing
- name: Tiledb Price Estimates
  plan_count: 0
  slug: tiledb-price-estimates
random_paper: 4
rate_limits:
- limit_count: 0
  name: Tiledb Rate Limits
  slug: tiledb-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: TileDB API Rules
  rule_count: 60
  severity_counts:
    error: 41
    hint: 0
    info: 3
    warn: 16
  slug: tiledb-rules
scopes:
- name: Tiledb Scopes
  scope_count: 3
  slug: tiledb-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 59.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 59.5
    catalog_earned_first_party: 12.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 71.1
    contract_governance: 31.8
    contract_quality: 48.2
    developer_ergonomics: 73.2
    discoverability: 71.4
    operational_transparency: 18.4
  previous_composite: 58.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 73.7
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/tiledb/tiledb-2026-09-02T163742.png
security:
- kind: authentication
  name: Tiledb Authentication
  slug: tiledb-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Tiledb Domain Security
  slug: tiledb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: tiledb-discover-and-inspect-arrays
  slug: tiledb-discover-and-inspect-arrays
- name: tiledb-query-and-compute
  slug: tiledb-query-and-compute
- name: tiledb-share-and-govern-assets
  slug: tiledb-share-and-govern-assets
slug: tiledb
tags:
- Company
- Database
- Multimodal Data
- Life Sciences
- Genomics
- Single Cell
- Biomedical Imaging
- Vector Search
- Data Management
- Cloud Storage
- Analytics
- Machine Learning
website: https://www.tiledb.com/
---
