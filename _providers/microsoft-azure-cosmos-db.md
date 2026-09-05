---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Microsoft Azure Cosmos Db Agentic Access
  operation_count: 11
  slug: microsoft-azure-cosmos-db-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 3
apis:
- baseURL: https://{account}.documents.azure.com/
  baseurl_source: declared
  description: Collections operations
  name: microsoft-azure-cosmos-db Collections API
  slug: microsoft-azure-cosmos-db-collections-api
- baseURL: https://{account}.documents.azure.com/
  baseurl_source: declared
  description: Databases operations
  name: microsoft-azure-cosmos-db Databases API
  slug: microsoft-azure-cosmos-db-databases-api
- baseURL: https://{account}.documents.azure.com/
  baseurl_source: declared
  description: Documents operations
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
name: Azure Cosmos DB
nav: Providers
network: true
overview: 'Azure Cosmos DB publishes 3 APIs on the [APIs.io](https://apis.io/) network: microsoft-azure-cosmos-db Collections API, microsoft-azure-cosmos-db Databases API, and microsoft-azure-cosmos-db Documents API.


  Azure Cosmos DB''s developer surface includes authentication, developer portal, pricing, documentation, support, and 6 more developer resources.'
plans:
- name: Microsoft Azure Cosmos Db Plans Pricing
  plan_count: 3
  slug: microsoft-azure-cosmos-db-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Microsoft Azure Cosmos Db Rate Limits
  slug: microsoft-azure-cosmos-db-rate-limits
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 35.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
