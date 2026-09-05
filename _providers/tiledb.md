---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://api.tiledb.com/v1
  baseurl_source: declared
  description: The primary TileDB Cloud REST API. 168 operations across arrays, groups, assets, files, notebooks, UDFs, task graphs, SQL, queries, users, organizations, invitations, favorites and tokens. Published b
  name: TileDB Storage Platform API (v1)
  slug: tiledb-storage-platform-api-v1
- baseURL: https://api.tiledb.com/v2
  baseurl_source: declared
  description: The v2 routes of the TileDB Cloud REST API — 21 operations concentrated on groups, assets, array metadata, files, notebooks, users and organizations. Published by TileDB as a separate Swagger 2.0 cont
  name: TileDB Storage Platform API (v2)
  slug: tiledb-storage-platform-api-v2
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tiledb-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tiledb-scopes.yml
- group: auth
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
  title: ''
  type: Packages
  url: packages/tiledb-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tiledb-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tiledb-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/tiledb-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tiledb-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tiledb-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tiledb-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tiledb-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/tiledb-cli.yml
- group: design
  title: ''
  type: Components
  url: components/tiledb-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tiledb-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tiledb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tiledb-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-30'
description: TileDB, Inc. builds a multimodal database around a single universal data model — the multi-dimensional array — that stores tables, genomics (VCF), single-cell (SOMA), biomedical imaging, vector embeddings, point clouds, files and ML models in one cloud-native format on S3, Azure Blob, GCS, Lustre or MinIO. The open-source TileDB Embedded storage engine is paired with TileDB Cloud (and the Carrara product line), a hosted and self-hostable platform for cataloging, sharing, governing and querying those assets, with serverless SQL, user-defined functions, task graphs, Jupyter notebooks and dashboards. The platform is programmable through the TileDB Storage Platform REST API (v1 and v2, whose Swagger 2.0 contracts TileDB publishes openly on GitHub), plus first-party clients for Python, R, Java, Go, C, C++, C#, JavaScript and Rust. The company is focused on life sciences and precision medicine.
image: https://images.ctfassets.net/nxe07oerbx6d/PTO0pDBxwkIxfaGzEiHPi/931e190a336eebdedc825cba1723b96b/TileDB-homepage-meta.jpg
layout: provider
modified: '2026-08-30'
name: TileDB
nav: Providers
network: true
overview: 'TileDB publishes 2 APIs on the [APIs.io](https://apis.io/) network: Storage Platform API (v1) and Storage Platform API (v2). Tagged areas include Company, Database, Multimodal Data, Life Sciences, and Genomics.


  TileDB''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 22 more developer resources.'
plans:
- name: Tiledb Plans Pricing
  plan_count: 3
  slug: tiledb-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Tiledb Rate Limits
  slug: tiledb-rate-limits
scopes:
- name: Tiledb Scopes
  scope_count: 3
  slug: tiledb-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 54.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 40.9
    developer_ergonomics: 73.2
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 53.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tiledb/refs/heads/main/screenshots/tiledb-2026-09-02T163742.png
security:
- kind: authentication
  name: Tiledb Authentication
  slug: tiledb-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Tiledb Domain Security
  slug: tiledb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
- Machine-Learning
website: https://www.tiledb.com/
---
