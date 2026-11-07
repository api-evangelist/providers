---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
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
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Delta Lake storage framework defines the on-disk transaction log and protocol that adds ACID transactions, schema enforcement, and time travel to Parquet-based data lakes. Delta Lake exposes Spark
  name: Delta Lake Storage Framework
  slug: delta-lake-storage
- description: Catalog-managed Delta tables delegate table scan planning to an external catalog using the Iceberg REST Catalog protocol, enabling interoperability with Unity Catalog and other catalog services.
  name: Delta Catalog-Managed Tables
  slug: delta-catalog
- baseURL: https://sharing.delta.io/delta-sharing/
  baseurl_source: declared
  description: Schema discovery APIs
  name: Delta Lake Schemas API
  slug: delta-lake-schemas-api
- baseURL: https://sharing.delta.io/delta-sharing/
  baseurl_source: declared
  description: Share discovery APIs
  name: Delta Lake Shares API
  slug: delta-lake-shares-api
- baseURL: https://sharing.delta.io/delta-sharing/
  baseurl_source: declared
  description: Table query and inspection APIs
  name: Delta Lake Tables API
  slug: delta-lake-tables-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/delta-lake/plans/delta-lake-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/delta-lake-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/delta-lake/rate-limits/delta-lake-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/delta-lake-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/delta-lake/finops/delta-lake-finops.yml
  title: ''
  type: FinOps
  url: finops/delta-lake-finops.yml
- group: other
  href: https://artifacts.apis.io/delta-lake/overlays/delta-lake-delta-sharing-protocol-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/delta-lake-delta-sharing-protocol-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/delta-lake/authentication/delta-lake-authentication.yml
  title: ''
  type: Authentication
  url: authentication/delta-lake-authentication.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/delta-io/delta/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/delta-io/delta/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/delta-io/delta/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/delta-io/delta/blob/master/LICENSE.txt
- group: auth
  href: https://artifacts.apis.io/delta-lake/security/delta-lake-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/delta-lake-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deltalake
- group: company
  title: ''
  type: Website
  url: https://delta.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.delta.io/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/delta-io
- group: company
  title: ''
  type: Blog
  url: https://delta.io/blog/
- group: other
  title: ''
  type: LinuxFoundation
  url: https://lfaidata.foundation/projects/delta-lake/
- group: operate
  title: ''
  type: Slack
  url: https://go.delta.io/slack
- group: design
  href: https://artifacts.apis.io/delta-lake/vocabulary/delta-lake-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/delta-lake-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/delta-lake/packages/delta-lake-packages.yml
  title: ''
  type: Packages
  url: packages/delta-lake-packages.yml
- group: build
  href: https://artifacts.apis.io/delta-lake/packages/delta-lake-packages.yml
  title: ''
  type: SDKs
  url: packages/delta-lake-packages.yml
- group: agent
  href: https://artifacts.apis.io/delta-lake/llms/delta-lake-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/delta-lake-llms.txt
- group: design
  href: https://artifacts.apis.io/delta-lake/conformance/delta-lake-conformance.yml
  title: ''
  type: Conformance
  url: conformance/delta-lake-conformance.yml
- group: design
  href: https://artifacts.apis.io/delta-lake/lifecycle/delta-lake-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/delta-lake-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/delta-lake/lifecycle/delta-lake-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/delta-lake-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/delta-lake/changelog/delta-lake-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/delta-lake-changelog.yml
- group: design
  href: https://artifacts.apis.io/delta-lake/errors/delta-lake-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/delta-lake-problem-types.yml
- group: design
  href: https://artifacts.apis.io/delta-lake/conventions/delta-lake-conventions.yml
  title: ''
  type: Conventions
  url: conventions/delta-lake-conventions.yml
- group: design
  href: https://artifacts.apis.io/delta-lake/conventions/delta-lake-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/delta-lake-conventions.yml
- group: design
  href: https://artifacts.apis.io/delta-lake/data-model/delta-lake-data-model.yml
  title: ''
  type: DataModel
  url: data-model/delta-lake-data-model.yml
- group: start
  href: https://artifacts.apis.io/delta-lake/sandbox/delta-lake-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/delta-lake-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/delta-lake/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.delta.io/delta-apidoc/
- group: start
  title: ''
  type: GettingStarted
  url: https://delta.io/learn/getting-started
- group: operate
  title: ''
  type: Support
  url: https://delta.io/resources/getting-help
- group: operate
  title: ''
  type: Roadmap
  url: https://delta.io/roadmap
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lfprojects.org/policies/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lfprojects.org/policies/privacy-policy/
created: '2026-03-16'
description: Delta Lake is a graduated project of the Linux Foundation AI & Data Foundation providing an open source storage framework for building Lakehouse architectures. Originally contributed by Databricks, it adds reliability, quality, and performance to data lakes with ACID transactions, schema enforcement, time travel, and Iceberg/Hudi interoperability via UniForm. Delta Lake projects also include Delta Sharing (an open protocol for secure data sharing) and catalog-managed tables built on the Iceberg REST Catalog protocol.
finops:
- has_sources: true
  method: derived
  name: Delta Lake Finops
  primary_unit: ''
  service_category: ''
  slug: delta-lake-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/delta-lake.png
layout: provider
modified: '2026-09-05'
name: Delta Lake
nav: Providers
network: true
overview: 'Delta Lake publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Schemas API, Shares API, Tables API, and 2 more. Tagged areas include Data, Data Lake, Lakehouse, Linux Foundation, and Open Source.


  The Delta Lake catalog on APIs.io includes 1 Spectral governance ruleset.


  Delta Lake''s developer surface includes authentication, documentation, engineering blog, changelog, sandbox, API reference, getting-started guide, and 30 more developer resources.'
plans:
- name: Delta Lake Plans Pricing
  plan_count: 0
  slug: delta-lake-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Delta Lake Rate Limits
  slug: delta-lake-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Delta Lake API Rules
  rule_count: 58
  severity_counts:
    error: 56
    hint: 0
    info: 1
    warn: 1
  slug: delta-lake-rules
score:
  band: developing
  composite: 48.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 45.5
    contract_quality: 45.5
    developer_ergonomics: 63.7
    discoverability: 64.3
    operational_transparency: 34.2
  open_source:
    applies: true
    score: 65.0
  previous_composite: 48.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
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
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/delta-lake/delta-lake-2026-06-20T175901.png
security:
- kind: authentication
  name: Delta Lake Authentication
  slug: delta-lake-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Delta Lake Domain Security
  slug: delta-lake-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 3
skills:
- name: delta-lake-discover-shared-data
  slug: delta-lake-discover-shared-data
- name: delta-lake-read-change-data-feed
  slug: delta-lake-read-change-data-feed
- name: delta-lake-read-shared-table
  slug: delta-lake-read-shared-table
slug: delta-lake
tags:
- Data
- Data Lake
- Lakehouse
- Linux Foundation
- Open Source
- Storage
- Streaming
website: https://delta.io/
---
