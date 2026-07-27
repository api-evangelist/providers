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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Postgresql Agentic Access
  operation_count: 7
  slug: microsoft-azure-postgresql-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- description: Operations operations
  name: Azure Database for PostgreSQL Operations API
  slug: microsoft-azure-postgresql-operations-api
- description: Servers operations
  name: Azure Database for PostgreSQL Servers API
  slug: microsoft-azure-postgresql-servers-api
artifact_total: 10
collections:
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
overview: 'Azure Database for PostgreSQL publishes 2 APIs on the [APIs.io](https://apis.io/) network: Operations API and Servers API. Tagged areas include Database, Managed Database, Open Source, PostgreSQL, and Relational.


  Azure Database for PostgreSQL''s developer surface includes authentication, developer portal, pricing, documentation, signup flow, support, and 9 more developer resources.'
plans:
- name: Microsoft Azure Postgresql Plans Pricing
  plan_count: 3
  slug: microsoft-azure-postgresql-plans-pricing
random_paper: 11
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
  composite: 50.7
  delta: 3.3
  facets:
    commercial_clarity: 84.2
    contract_quality: 53.1
    developer_ergonomics: 32.6
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 47.4
  schema_version: 0.5
  scored_at: '2026-07-27'
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
- Open Source
- PostgreSQL
- Relational
website: https://azure.microsoft.com/en-us/products/postgresql
---
