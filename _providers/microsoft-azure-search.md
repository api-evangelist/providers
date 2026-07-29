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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Microsoft Azure Search Agentic Access
  operation_count: 7
  slug: microsoft-azure-search-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 3
apis:
- description: The management REST API provides operations for creating and managing Azure AI Search service instances, scaling replicas and partitions, and managing keys and shared private link resources.
  name: Azure AI Search Management REST API
  slug: management-api
- description: The Documents API from Azure AI Search — 2 operation(s) for documents.
  name: Azure AI Search Documents API
  slug: microsoft-azure-search-documents-api
- description: The Indexes API from Azure AI Search — 2 operation(s) for indexes.
  name: Azure AI Search Indexes API
  slug: microsoft-azure-search-indexes-api
artifact_total: 10
collections:
- collection_type: open
  name: Azure AI Search REST API
  slug: open-microsoft-azure-search
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-search-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-search-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-search-authentication.yml
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
  url: https://azure.microsoft.com/en-us/pricing/details/search/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/search/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/search/search-get-started-portal
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/azure/search/search-howto-dotnet-sdk
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
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
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/product/azure-cognitive-search/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-cognitive-search
created: '2026-03-13'
description: Azure AI Search (formerly Azure Cognitive Search) is a cloud search service with built-in AI capabilities for enriching content and enabling vector and semantic search over heterogeneous data. It indexes content from Azure data sources and supports full-text, faceted, geospatial, vector, and hybrid retrieval.
finops:
- name: Microsoft Azure Search Finops
  service_category: API
  slug: microsoft-azure-search-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-search.png
layout: provider
modified: '2026-05-19'
name: Azure AI Search
nav: Providers
network: true
overview: 'Azure AI Search publishes 2 APIs on the [APIs.io](https://apis.io/) network: Documents API and Indexes API. Tagged areas include AI Search, Cognitive Search, Hybrid Search, Search, and Semantic Search.


  Azure AI Search''s developer surface includes authentication, developer portal, pricing, documentation, getting-started guide, support, engineering blog, and 8 more developer resources.'
plans:
- name: Microsoft Azure Search Plans Pricing
  plan_count: 3
  slug: microsoft-azure-search-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Microsoft Azure Search Rate Limits
  slug: microsoft-azure-search-rate-limits
score:
  band: developing
  composite: 52.7
  delta: -2.1
  facets:
    commercial_clarity: 71.1
    contract_quality: 55.1
    developer_ergonomics: 52.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 54.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-search/refs/heads/main/screenshots/microsoft-azure-search-2026-06-20T185434.png
security:
- kind: authentication
  name: Microsoft Azure Search Authentication
  slug: microsoft-azure-search-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Microsoft Azure Search Domain Security
  slug: microsoft-azure-search-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-search
tags:
- AI Search
- Cognitive Search
- Hybrid Search
- Search
- Semantic Search
- Vector Search
website: https://portal.azure.com/
---
