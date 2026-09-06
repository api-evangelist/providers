---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
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
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-postgresql-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-postgresql-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-postgresql-authentication.yml
- group: auth
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
- name: Microsoft Azure Postgresql Finops
  service_category: API
  slug: microsoft-azure-postgresql-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-postgresql.png
layout: provider
modified: '2026-05-19'
name: Azure Database for PostgreSQL
nav: Providers
network: true
overview: 'Azure Database for PostgreSQL publishes 2 APIs on the [APIs.io](https://apis.io/) network: Operations API and Servers API. Tagged areas include Database, Managed Database, Open-Source, PostgreSQL, and Relational.


  Azure Database for PostgreSQL''s developer surface includes authentication, developer portal, pricing, documentation, signup flow, support, and 9 more developer resources.'
plans:
- name: Microsoft Azure Postgresql Plans Pricing
  plan_count: 3
  slug: microsoft-azure-postgresql-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Microsoft Azure Postgresql Rate Limits
  slug: microsoft-azure-postgresql-rate-limits
scopes:
- name: Microsoft Azure Postgresql Scopes
  scope_count: 1
  slug: microsoft-azure-postgresql-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-postgresql/refs/heads/main/screenshots/microsoft-azure-postgresql-2026-06-20T185432.png
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
- Open-Source
- PostgreSQL
- Relational
website: https://azure.microsoft.com/en-us/products/postgresql
---
