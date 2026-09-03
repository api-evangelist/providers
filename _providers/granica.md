---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The Granica REST API (v1) lets you programmatically manage all aspects of the Granica platform, including table onboarding, compaction scheduling, catalog connections, query optimization (Optimus), va
  name: Granica APIs V1
  slug: granica-apis-v1
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/granica-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.granica.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.granica.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.granica.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.granica.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.granica.ai/getting-started/get-started
- group: company
  title: ''
  type: Blog
  url: https://www.granica.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/granica-ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.granica.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.granica.ai/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/granica-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/granica-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/granica-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/granica-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/granica-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/granica-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/granica-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/granica-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/granica-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/granica-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/granica-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/granica-trust-center.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/granica-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/granica-rate-limits.yml
created: '2026-08-22'
description: Granica Computing, Inc. builds an efficiency and data-readiness layer for enterprise AI. Its flagship product, Granica Crunch, is a continuous, policy-driven data lakehouse optimization platform that handles compaction, compression, sorting, clustering, deduplication, vacuuming, partition lifecycle management and query acceleration for Delta Lake, Apache Iceberg and Hive tables sitting in Amazon S3, Google Cloud Storage and Azure. The platform is delivered as a customer-deployed control plane plus data plane (Granica Hosted, On-Premises and Hybrid deployment models on EKS or GKE inside the customer cloud account), so table data never has to leave the customer environment. Granica publishes a public REST API reference — the Granica APIs V1 surface at base path /api/v1 — covering tables, schedules, onboarding, crunch, vacuum, partition expiration, pending deletions, catalog connections, feature flags, Optimus query optimization and object maintenance, authenticated with long-lived
  bearer API keys carrying explicit read/write scopes. The company was formerly known as Project N (the Bolt product line), and still maintains the legacy Bolt SDKs under the project-n-oss GitHub organization.
image: https://www.granica.ai/favicon-granica.svg
layout: provider
modified: '2026-08-22'
name: Granica
nav: Providers
network: true
overview: 'Granica publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Storage, Analytics, and Artificial Intelligence.


  Granica''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, and 19 more developer resources.'
plans:
- name: Granica Plans Pricing
  plan_count: 0
  slug: granica-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Granica Rate Limits
  slug: granica-rate-limits
scopes:
- name: Granica Scopes
  scope_count: 0
  slug: granica-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 29.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/granica/refs/heads/main/screenshots/granica-2026-09-02T145631.png
security:
- kind: authentication
  name: Granica Authentication
  slug: granica-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Granica Domain Security
  slug: granica-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Granica Trust Center
  slug: granica-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2, ISO/IEC 27001
slug: granica
tags:
- Company
- Data
- Storage
- Analytics
- Artificial Intelligence
- Machine-Learning
- Data Lakehouse
- Cloud Cost Optimization
- Compression
- Data Infrastructure
website: https://www.granica.ai/
---
