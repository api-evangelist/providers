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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Microsoft Azure Cosmos Db Agentic Access
  operation_count: 11
  slug: microsoft-azure-cosmos-db-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 3
apis:
- description: Collections operations
  name: microsoft-azure-cosmos-db Collections API
  slug: microsoft-azure-cosmos-db-collections-api
- description: Databases operations
  name: microsoft-azure-cosmos-db Databases API
  slug: microsoft-azure-cosmos-db-databases-api
- description: Documents operations
  name: microsoft-azure-cosmos-db Documents API
  slug: microsoft-azure-cosmos-db-documents-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Cosmos DB REST Collections API
  slug: open-microsoft-azure-cosmos-db-collections-api
- collection_type: open
  name: Azure Cosmos DB REST Collections Databases API
  slug: open-microsoft-azure-cosmos-db-databases-api
- collection_type: open
  name: Azure Cosmos DB REST Collections Documents API
  slug: open-microsoft-azure-cosmos-db-documents-api
- collection_type: open
  name: Azure Cosmos DB REST API
  slug: open-microsoft-azure-cosmos-db
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-cosmos-db-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-cosmos-db-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-cosmos-db-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AzureCosmosDB
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/azure-cosmos-db
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
description: 'Azure Cosmos DB is a globally distributed, multi-model database service offering guaranteed low latency, elastic scalability, and tunable consistency. This collection catalogs the REST APIs for data plane operations across NoSQL, MongoDB, Cassandra, Gremlin, and Table models alongside resource provider APIs for account and throughput management. - url: https://azure.microsoft.com/en-us/blog/azure-cosmos-db-a-competitive-advantage-for-healthcare-isvs/ type: Blog'
finops:
- name: Microsoft Azure Cosmos Db Finops
  service_category: API
  slug: microsoft-azure-cosmos-db-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-cosmos-db.png
layout: provider
modified: '2026-05-19'
name: microsoft-azure-cosmos-db
nav: Providers
network: true
overview: 'microsoft-azure-cosmos-db publishes 3 APIs on the [APIs.io](https://apis.io/) network: Collections API, Databases API, and Documents API.


  microsoft-azure-cosmos-db''s developer surface includes authentication, developer portal, pricing, documentation, support, and 6 more developer resources.'
plans:
- name: Microsoft Azure Cosmos Db Plans Pricing
  plan_count: 3
  slug: microsoft-azure-cosmos-db-plans-pricing
random_paper: 142
rate_limits:
- limit_count: 5
  name: Microsoft Azure Cosmos Db Rate Limits
  slug: microsoft-azure-cosmos-db-rate-limits
score:
  band: thin
  composite: 37.7
  delta: -0.7
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 35.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cosmos-db/refs/heads/main/screenshots/microsoft-azure-cosmos-db-2026-06-20T185408.png
security:
- kind: authentication
  name: Microsoft Azure Cosmos Db Authentication
  slug: microsoft-azure-cosmos-db-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Microsoft Azure Cosmos Db Domain Security
  slug: microsoft-azure-cosmos-db-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-cosmos-db
website: https://portal.azure.com/
---
