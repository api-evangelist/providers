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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 59.6
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Meilisearch Agentic Access
  operation_count: 33
  slug: meilisearch-agentic-access
  summary_line: 33 operations · 19 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: The Meilisearch RESTful API provides endpoints for creating and managing indexes, adding and searching documents, configuring search settings, managing API keys, and monitoring tasks and health status
  name: Meilisearch API
  slug: meilisearch-api
- description: The Documents API from Meilisearch — 3 operation(s) for documents.
  name: Meilisearch Documents API
  slug: meilisearch-documents-api
- description: The Health API from Meilisearch — 3 operation(s) for health.
  name: Meilisearch Health API
  slug: meilisearch-health-api
- description: The Indexes API from Meilisearch — 4 operation(s) for indexes.
  name: Meilisearch Indexes API
  slug: meilisearch-indexes-api
- description: The Keys API from Meilisearch — 2 operation(s) for keys.
  name: Meilisearch Keys API
  slug: meilisearch-keys-api
- description: The Search API from Meilisearch — 3 operation(s) for search.
  name: Meilisearch Search API
  slug: meilisearch-search-api
- description: The Settings API from Meilisearch — 1 operation(s) for settings.
  name: Meilisearch Settings API
  slug: meilisearch-settings-api
- description: The Tasks API from Meilisearch — 4 operation(s) for tasks.
  name: Meilisearch Tasks API
  slug: meilisearch-tasks-api
artifact_total: 35
collections:
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
overview: 'Meilisearch publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Health API, Indexes API, and 4 more. Tagged areas include AI Search, Full-Text Search, Hybrid Search, Open Source, and Search.


  Meilisearch''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, engineering blog, changelog, and 9 more developer resources.'
plans:
- name: Meilisearch Plans Pricing
  plan_count: 4
  slug: meilisearch-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Meilisearch Rate Limits
  slug: meilisearch-rate-limits
score:
  band: developing
  composite: 50.0
  delta: 2.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 45.9
    developer_ergonomics: 43.5
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 48.0
  schema_version: 0.5
  scored_at: '2026-07-27'
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
- Open Source
- Search
website: https://www.meilisearch.com/
---
