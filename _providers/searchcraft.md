---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 28
  human_in_the_loop: 3
  name: Searchcraft Agentic Access
  operation_count: 45
  slug: searchcraft-agentic-access
  summary_line: 45 operations · 28 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: The Authentication API from Searchcraft — 2 operation(s) for authentication.
  name: Searchcraft Authentication API
  slug: searchcraft-authentication-api
- description: The Documents API from Searchcraft — 4 operation(s) for documents.
  name: Searchcraft Documents API
  slug: searchcraft-documents-api
- description: The Federation API from Searchcraft — 3 operation(s) for federation.
  name: Searchcraft Federation API
  slug: searchcraft-federation-api
- description: The Healthcheck API from Searchcraft — 1 operation(s) for healthcheck.
  name: Searchcraft Healthcheck API
  slug: searchcraft-healthcheck-api
- description: The Indexes API from Searchcraft — 4 operation(s) for indexes.
  name: Searchcraft Indexes API
  slug: searchcraft-indexes-api
- description: The Measure API from Searchcraft — 6 operation(s) for measure.
  name: Searchcraft Measure API
  slug: searchcraft-measure-api
- description: The Search API from Searchcraft — 2 operation(s) for search.
  name: Searchcraft Search API
  slug: searchcraft-search-api
- description: The Stopwords API from Searchcraft — 2 operation(s) for stopwords.
  name: Searchcraft Stopwords API
  slug: searchcraft-stopwords-api
- description: The Synonyms API from Searchcraft — 2 operation(s) for synonyms.
  name: Searchcraft Synonyms API
  slug: searchcraft-synonyms-api
- description: The Transactions API from Searchcraft — 2 operation(s) for transactions.
  name: Searchcraft Transactions API
  slug: searchcraft-transactions-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Searchcraft Authentication API
  slug: open-searchcraft-authentication-api
- collection_type: open
  name: Searchcraft Authentication Documents API
  slug: open-searchcraft-documents-api
- collection_type: open
  name: Searchcraft Authentication Federation API
  slug: open-searchcraft-federation-api
- collection_type: open
  name: Searchcraft Authentication Healthcheck API
  slug: open-searchcraft-healthcheck-api
- collection_type: open
  name: Searchcraft Authentication Indexes API
  slug: open-searchcraft-indexes-api
- collection_type: open
  name: Searchcraft Authentication Measure API
  slug: open-searchcraft-measure-api
- collection_type: open
  name: Searchcraft Authentication Search API
  slug: open-searchcraft-search-api
- collection_type: open
  name: Searchcraft Authentication Stopwords API
  slug: open-searchcraft-stopwords-api
- collection_type: open
  name: Searchcraft Authentication Synonyms API
  slug: open-searchcraft-synonyms-api
- collection_type: open
  name: Searchcraft Authentication Transactions API
  slug: open-searchcraft-transactions-api
- collection_type: open
  name: Searchcraft API
  slug: open-searchcraft
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/searchcraft-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/searchcraft-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/searchcraft-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/searchcraft-inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/searchcraft
- group: company
  title: ''
  type: Website
  url: https://www.searchcraft.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.searchcraft.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/searchcraft-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/searchcraft-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/searchcraft-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://searchcraft.io/posts
created: '2026-06-21'
description: Searchcraft is a developer-first search engine and search-as-a-service platform. Its REST API lets teams create indexes, ingest and manage documents, run fuzzy/exact full-text search with facets and relevancy tuning, query across multiple indexes via federated search, and manage synonyms, stopwords, and usage measurement. It ships as a managed cloud service (Searchcraft Cloud) and a self-hosted engine (Searchcraft Core).
finops:
- name: Searchcraft Finops
  service_category: Analytics
  slug: searchcraft-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/searchcraft.png
layout: provider
modified: '2026-06-21'
name: Searchcraft
nav: Providers
network: true
overview: 'Searchcraft publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Documents API, Federation API, and 7 more. Tagged areas include Search, Search as a Service, Full Text Search, Indexing, and Developer Tools.


  Searchcraft''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Searchcraft Plans Pricing
  plan_count: 3
  slug: searchcraft-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Searchcraft Rate Limits
  slug: searchcraft-rate-limits
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Searchcraft Authentication
  slug: searchcraft-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Searchcraft Domain Security
  slug: searchcraft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: searchcraft
tags:
- Search
- Search as a Service
- Full Text Search
- Indexing
- Developer Tools
website: https://www.searchcraft.io/
---
