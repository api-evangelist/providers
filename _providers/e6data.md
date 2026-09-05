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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.e6data.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.e6data.com/product-documentation
- group: docs
  title: ''
  type: Documentation
  url: https://docs.e6data.com/product-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://docs.e6data.com/product-documentation/connectors-and-drivers/jdbc-driver/api-support
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.e6data.com/product-documentation/get-started
- group: company
  title: ''
  type: Blog
  url: https://www.e6data.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.e6data.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://docs.e6data.com/product-documentation/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.e6data.com/product-documentation/terms-and-condition
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.e6data.com/product-documentation/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.e6data.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/e6x-labs
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/e6data-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/e6data-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/e6data-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/e6data-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/e6data-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/e6data-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/e6data-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/e6data-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/e6data-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.e6data.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/e6data-domain-security.yml
created: '2026-07-17'
description: e6data is a lakehouse compute engine built to run high-concurrency, complex SQL analytics and AI workloads directly on open table formats (Apache Iceberg, Delta Lake, Apache Hudi, Hive) with zero data movement, claiming 10x faster queries at 60% lower cost through a decentralized, Kubernetes-native "atomic" architecture that scales compute incrementally. It deploys serverless or in a customer VPC across AWS, GCP and Azure, and interoperates with Databricks, Snowflake, Redshift and Microsoft Fabric. Developers connect over SQL via a JDBC type-4 driver, an official Python connector, and common BI/SQL tools (DBeaver, Superset, Tableau, Power BI, Metabase, Zeppelin, Jupyter), plus a narrow REST surface for query-history reporting. Access is authenticated with Personal Access Tokens and Service Accounts and governed by RBAC with row/column-level controls and SSO. Backed by Accel.
image: https://cdn.prod.website-files.com/6772770a5e5d008a7b3c6a6d/6821f8656a89dc1efd5b7bf4_Open%20Graph%20Image.png
layout: provider
modified: '2026-07-18'
name: e6data
nav: Providers
network: true
overview: 'e6data is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, B2B, Data, Analytics, and Lakehouse.


  e6data''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 16 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 33.7
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/e6data/refs/heads/main/screenshots/e6data-2026-07-25T212626.png
security:
- kind: authentication
  name: E6Data Authentication
  slug: e6data-authentication
  summary_line: http/oauth2 · 4 schemes
- kind: domain-security
  name: E6Data Domain Security
  slug: e6data-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: e6data
tags:
- Company
- B2B
- Data
- Analytics
- Lakehouse
- SQL
- Query Engine
- Data Infrastructure
- Big Data
website: https://www.e6data.com/
---
