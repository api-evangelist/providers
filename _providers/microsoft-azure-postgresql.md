---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Postgresql Agentic Access
  operation_count: 7
  slug: microsoft-azure-postgresql-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Operations operations
  name: Azure Database for PostgreSQL Operations API
  slug: microsoft-azure-postgresql-operations-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Servers operations
  name: Azure Database for PostgreSQL Servers API
  slug: microsoft-azure-postgresql-servers-api
artifact_total: 13
collections:
- collection_type: open
  name: Azure Database for PostgreSQL REST Operations API
  slug: open-microsoft-azure-postgresql-operations-api
- collection_type: open
  name: Azure Database for PostgreSQL REST Operations Servers API
  slug: open-microsoft-azure-postgresql-servers-api
- collection_type: open
  name: Azure Database for PostgreSQL REST API
  slug: open-microsoft-azure-postgresql
common:
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-postgresql/plans/microsoft-azure-postgresql-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-postgresql-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-postgresql/rate-limits/microsoft-azure-postgresql-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-postgresql-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-postgresql/finops/microsoft-azure-postgresql-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-postgresql-finops.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-postgresql/capabilities/microsoft-azure-postgresql-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-azure-postgresql-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-postgresql/agentic-access/microsoft-azure-postgresql-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-postgresql-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-postgresql/security/microsoft-azure-postgresql-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-postgresql-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-postgresql/authentication/microsoft-azure-postgresql-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-postgresql-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-postgresql/scopes/microsoft-azure-postgresql-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-postgresql-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/postgresql/flexible-server/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/postgresql/
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/postgresql
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/
- group: start
  title: ''
  type: Login
  url: https://portal.azure.com/
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-13'
description: Azure Database for PostgreSQL is a fully managed relational database service based on the open-source PostgreSQL engine. It provides Flexible Server and Cosmos DB for PostgreSQL deployment options with built-in high availability, automated backups, scaling, and security.
finops:
- has_sources: true
  method: derived
  name: Microsoft Azure Postgresql Finops
  primary_unit: ''
  service_category: ''
  slug: microsoft-azure-postgresql-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-postgresql.png
layout: provider
modified: '2026-05-19'
name: Azure Database for PostgreSQL
nav: Providers
network: true
overview: 'Azure Database for PostgreSQL is listed with 2 APIs on the [APIs.io](https://apis.io/) network: Operations API and Servers API. Tagged areas include Database, Managed Database, Open Source, PostgreSQL, and Relational.


  The Azure Database for PostgreSQL catalog on APIs.io includes 1 Spectral governance ruleset.


  Azure Database for PostgreSQL''s developer surface includes authentication, developer portal, pricing, documentation, signup flow, support, and 13 more developer resources.'
plans:
- name: Microsoft Azure Postgresql Plans Pricing
  plan_count: 0
  slug: microsoft-azure-postgresql-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Microsoft Azure Postgresql Rate Limits
  slug: microsoft-azure-postgresql-rate-limits
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Azure Database for PostgreSQL API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: microsoft-azure-postgresql-rules
scopes:
- name: Microsoft Azure Postgresql Scopes
  scope_count: 1
  slug: microsoft-azure-postgresql-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 13.6
    contract_quality: 44.1
    developer_ergonomics: 47.6
    discoverability: 80.4
    operational_transparency: 10.5
  previous_composite: 44.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/microsoft-azure-postgresql/microsoft-azure-postgresql-2026-06-20T185432.png
security:
- kind: authentication
  name: Microsoft Azure Postgresql Authentication
  slug: microsoft-azure-postgresql-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Postgresql Domain Security
  slug: microsoft-azure-postgresql-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-postgresql
tags:
- Database
- Managed Database
- Open Source
- PostgreSQL
- Relational
website: https://azure.microsoft.com/en-us/products/postgresql
---
