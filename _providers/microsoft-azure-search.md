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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Search Agentic Access
  operation_count: 7
  slug: microsoft-azure-search-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 3
apis:
- description: The management REST API provides operations for creating and managing Azure AI Search service instances, scaling replicas and partitions, and managing keys and shared private link resources.
  name: Azure AI Search Management REST API
  slug: management-api
- baseURL: https://{search-service}.search.windows.net/
  baseurl_source: declared
  description: The Documents API from Azure AI Search — 2 operation(s) for documents.
  name: Azure AI Search Documents API
  slug: microsoft-azure-search-documents-api
- baseURL: https://{search-service}.search.windows.net/
  baseurl_source: declared
  description: The Indexes API from Azure AI Search — 2 operation(s) for indexes.
  name: Azure AI Search Indexes API
  slug: microsoft-azure-search-indexes-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure AI Search REST Documents API
  slug: open-microsoft-azure-search-documents-api
- collection_type: open
  name: Azure AI Search REST Documents Indexes API
  slug: open-microsoft-azure-search-indexes-api
- collection_type: open
  name: Azure AI Search REST API
  slug: open-microsoft-azure-search
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-search/refs/heads/main/plans/microsoft-azure-search-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-search-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-search/refs/heads/main/rate-limits/microsoft-azure-search-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-search-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-search/refs/heads/main/finops/microsoft-azure-search-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-search-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-search/refs/heads/main/agentic-access/microsoft-azure-search-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-search-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-search/refs/heads/main/security/microsoft-azure-search-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-search-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-search/refs/heads/main/authentication/microsoft-azure-search-authentication.yml
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
- has_sources: false
  method: generated
  name: Microsoft Azure Search Finops
  primary_unit: ''
  service_category: API
  slug: microsoft-azure-search-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-search.png
layout: provider
modified: '2026-05-19'
name: Azure AI Search
nav: Providers
network: true
overview: 'Azure AI Search is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Indexes API, and 1 more. Tagged areas include AI Search, Cognitive Search, Hybrid Search, Search, and Semantic Search.


  Azure AI Search''s developer surface includes authentication, developer portal, pricing, documentation, getting-started guide, support, engineering blog, and 12 more developer resources.'
plans:
- name: Microsoft Azure Search Plans Pricing
  plan_count: 3
  slug: microsoft-azure-search-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Microsoft Azure Search Rate Limits
  slug: microsoft-azure-search-rate-limits
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 46.5
    developer_ergonomics: 54.8
    discoverability: 78.6
    operational_transparency: 42.1
  previous_composite: 47.5
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
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 22.2
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
website: https://www.microsoft.com/
---
