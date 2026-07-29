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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Azure Cosmos Db Agentic Access
  operation_count: 21
  slug: azure-cosmos-db-agentic-access
  summary_line: 21 operations · 9 acting
api_count: 11
apis:
- description: REST API for creating, querying, and managing databases, containers, items, stored procedures, triggers, user-defined functions, users, and permissions. Authentication uses master keys, resource token
  name: Azure Cosmos DB Data Plane REST API
  slug: data-plane-api
- description: Azure Resource Manager REST API for managing Cosmos DB accounts, databases, containers, throughput, backups, and role-based access at the control-plane level. Authentication uses Microsoft Entra ID OA
  name: Azure Cosmos DB Resource Provider API
  slug: resource-provider-api
- description: Document collections (containers)
  name: Azure Cosmos DB Collections API
  slug: azure-cosmos-db-collections-api
- description: Database resources
  name: Azure Cosmos DB Databases API
  slug: azure-cosmos-db-databases-api
- description: Document items
  name: Azure Cosmos DB Documents API
  slug: azure-cosmos-db-documents-api
- description: Throughput offers
  name: Azure Cosmos DB Offers API
  slug: azure-cosmos-db-offers-api
- description: Permissions
  name: Azure Cosmos DB Permissions API
  slug: azure-cosmos-db-permissions-api
- description: Stored procedures
  name: Azure Cosmos DB Stored Procedures API
  slug: azure-cosmos-db-stored-procedures-api
- description: Triggers
  name: Azure Cosmos DB Triggers API
  slug: azure-cosmos-db-triggers-api
- description: UDFs
  name: Azure Cosmos DB User Defined Functions API
  slug: azure-cosmos-db-user-defined-functions-api
- description: Users
  name: Azure Cosmos DB Users API
  slug: azure-cosmos-db-users-api
artifact_total: 17
collections:
- collection_type: open
  name: Azure Cosmos DB Data Plane REST API
  slug: open-azure-cosmos-db
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-cosmos-db-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/azure-cosmos-db-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-cosmos-db-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azure-cosmos-db-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/azure-cosmos-db-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AzureCosmosDB
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/azure-cosmos-db
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/cosmos-db/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/cosmos-db/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/cosmos-db/
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/cosmos-db/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/feed/atom/
created: '2026-05-11'
description: Azure Cosmos DB is a fully managed, globally distributed, multi-model NoSQL and relational database service from Microsoft Azure that supports document, key-value, graph, column-family, and vector data models with turnkey global distribution, elastic scale, and SLA-backed latency, throughput, consistency, and availability. The Cosmos DB REST API exposes CRUD and query operations on databases, containers, items, stored procedures, triggers, and user-defined functions using master-key or resource-token authentication, alongside the Cosmos DB Resource Provider (Azure Resource Manager) using Microsoft Entra ID OAuth 2.0.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-cosmos-db.png
layout: provider
modified: '2026-05-11'
name: Azure Cosmos DB
nav: Providers
network: true
overview: 'Azure Cosmos DB publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Collections API, Databases API, Documents API, and 6 more. Tagged areas include Database, NoSQL, Document Database, Vector Database, and Globally Distributed.


  Azure Cosmos DB''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 7 more developer resources.'
random_paper: 77
scopes:
- name: Azure Cosmos Db Scopes
  scope_count: 1
  slug: azure-cosmos-db-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: emerging
  composite: 27.9
  delta: -2.1
  facets:
    commercial_clarity: 10.5
    contract_quality: 53.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 30.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-cosmos-db/refs/heads/main/screenshots/azure-cosmos-db-2026-06-20T172847.png
security:
- kind: authentication
  name: Azure Cosmos Db Authentication
  slug: azure-cosmos-db-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Azure Cosmos Db Domain Security
  slug: azure-cosmos-db-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Azure Cosmos Db Vulnerability Disclosure
  slug: azure-cosmos-db-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: azure-cosmos-db
tags:
- Database
- NoSQL
- Document Database
- Vector Database
- Globally Distributed
- Cloud
- Azure
website: https://azure.microsoft.com/en-us/products/cosmos-db/
---
