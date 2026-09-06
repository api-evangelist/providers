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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Meilisearch Agentic Access
  operation_count: 33
  slug: meilisearch-agentic-access
  summary_line: 33 operations · 19 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The Meilisearch RESTful API provides endpoints for creating and managing indexes, adding and searching documents, configuring search settings, managing API keys, and monitoring tasks and health status
  name: Meilisearch API
  slug: meilisearch-api
- baseURL: https://localhost:7700
  baseurl_source: declared
  description: The Documents API from Meilisearch — 3 operation(s) for documents.
  name: Meilisearch Documents API
  slug: meilisearch-documents-api
- baseURL: https://localhost:7700
  baseurl_source: declared
  description: The Health API from Meilisearch — 3 operation(s) for health.
  name: Meilisearch Health API
  slug: meilisearch-health-api
- baseURL: https://localhost:7700
  baseurl_source: declared
  description: The Indexes API from Meilisearch — 4 operation(s) for indexes.
  name: Meilisearch Indexes API
  slug: meilisearch-indexes-api
- baseURL: https://localhost:7700
  baseurl_source: declared
  description: The Keys API from Meilisearch — 2 operation(s) for keys.
  name: Meilisearch Keys API
  slug: meilisearch-keys-api
- baseURL: https://localhost:7700
  baseurl_source: declared
  description: The Search API from Meilisearch — 3 operation(s) for search.
  name: Meilisearch Search API
  slug: meilisearch-search-api
- baseURL: https://localhost:7700
  baseurl_source: declared
  description: The Settings API from Meilisearch — 1 operation(s) for settings.
  name: Meilisearch Settings API
  slug: meilisearch-settings-api
- baseURL: https://localhost:7700
  baseurl_source: declared
  description: The Tasks API from Meilisearch — 4 operation(s) for tasks.
  name: Meilisearch Tasks API
  slug: meilisearch-tasks-api
artifact_total: 43
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Meilisearch Documents API
  slug: open-meilisearch-documents-api
- collection_type: open
  name: Meilisearch Documents Health API
  slug: open-meilisearch-health-api
- collection_type: open
  name: Meilisearch Documents Indexes API
  slug: open-meilisearch-indexes-api
- collection_type: open
  name: Meilisearch Documents Keys API
  slug: open-meilisearch-keys-api
- collection_type: open
  name: Meilisearch Documents Search API
  slug: open-meilisearch-search-api
- collection_type: open
  name: Meilisearch Documents Settings API
  slug: open-meilisearch-settings-api
- collection_type: open
  name: Meilisearch Documents Tasks API
  slug: open-meilisearch-tasks-api
- collection_type: open
  name: Meilisearch API
  slug: open-meilisearch
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/meilisearch-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/meilisearch-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/meilisearch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meilisearch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/meilisearch-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/meilisearch
- group: start
  title: ''
  type: Portal
  url: https://www.meilisearch.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.meilisearch.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meilisearch
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/meilisearch
- group: start
  title: ''
  type: Signup
  url: https://cloud.meilisearch.com/register
- group: start
  title: ''
  type: Login
  url: https://cloud.meilisearch.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.meilisearch.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.meilisearch.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/meilisearch/meilisearch/releases
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/meilisearch/meilisearch-mcp
created: '2025-02-08'
description: Meilisearch is an open source, lightning-fast search engine API that brings AI-powered hybrid search to sites and applications. It provides a RESTful API for indexing, searching, and managing documents, with SDKs available for all major languages and frameworks.
features:
- 'Open Source: free self-hosted'
- 'Cloud Usage-Based from $30/mo: pay per search + documents'
- 'Cloud Resource-Based from $23/mo: pay by CPU/RAM/storage'
- 'Enterprise: custom self-hosting + premier support'
- Typo-tolerant full-text search
- Vector search for semantic + RAG use cases
- Faceted search and filtering
- Multi-tenancy via tenant tokens
- Federated search across multiple indexes
- REST API with master and tenant keys
- 'Concurrent indexing tasks: 4 default'
- Embedders integration (OpenAI, HuggingFace, etc.)
- Synonyms, stop words, ranking rules
- InstantSearch UI libraries (JS, React, Vue)
- Webhooks via task notifications
- EU + US data residency
finops:
- name: Meilisearch Finops
  service_category: Search
  slug: meilisearch-finops
graphqls:
- description: This is a conceptual GraphQL schema for the [Meilisearch](https://www.meilisearch.com/) open-source search engine API. It maps the Meilisearch REST API surface to GraphQL types, queries, and mutations
  name: Meilisearch GraphQL Schema
  slug: meilisearch-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/meilisearch.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Meilisearch
nav: Providers
network: true
overview: 'Meilisearch publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Health API, Indexes API, and 4 more. Tagged areas include AI Search, Full-Text Search, Hybrid Search, Open-Source, and Search.


  Meilisearch''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, engineering blog, changelog, and 9 more developer resources.'
plans:
- name: Meilisearch Plans Pricing
  plan_count: 4
  slug: meilisearch-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Meilisearch Rate Limits
  slug: meilisearch-rate-limits
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 40.8
    commercial_clarity: 40.8
    contract_governance: 0.0
    contract_quality: 55.3
    developer_ergonomics: 61.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/meilisearch/refs/heads/main/screenshots/meilisearch-2026-06-20T185134.png
security:
- kind: authentication
  name: Meilisearch Authentication
  slug: meilisearch-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Meilisearch Domain Security
  slug: meilisearch-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Meilisearch Vulnerability Disclosure
  slug: meilisearch-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Meilisearch Trust Center
  slug: meilisearch-trust-center
  summary_line: GDPR
slug: meilisearch
tags:
- AI Search
- Full-Text Search
- Hybrid Search
- Open-Source
- Search
website: https://www.meilisearch.com/
---
