---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Meilisearch Agentic Access
  operation_count: 33
  slug: meilisearch-agentic-access
  summary_line: 33 operations · 17 acting · 1 human-in-the-loop
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
- group: commercial
  href: https://artifacts.apis.io/meilisearch/plans/meilisearch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/meilisearch-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/meilisearch/rate-limits/meilisearch-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/meilisearch-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/meilisearch/finops/meilisearch-finops.yml
  title: ''
  type: FinOps
  url: finops/meilisearch-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.meilisearch.com/
- group: agent
  href: https://artifacts.apis.io/meilisearch/agentic-access/meilisearch-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/meilisearch-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/meilisearch/security/meilisearch-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/meilisearch-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/meilisearch/security/meilisearch-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/meilisearch-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/meilisearch/security/meilisearch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meilisearch-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/meilisearch/authentication/meilisearch-authentication.yml
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
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/meilisearch/meilisearch/blob/9d3365c81607e17ec9df1473f97d5dc9109bb1c4/crates/openapi-generator/.spectral.yaml
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
- has_sources: true
  method: derived
  name: Meilisearch Finops
  primary_unit: subscription
  service_category: ''
  slug: meilisearch-finops
  template: false
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
overview: 'Meilisearch publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Documents API, Health API, Indexes API, and 5 more. Tagged areas include AI Search, Full-Text Search, Hybrid Search, Open Source, and Search.


  The Meilisearch catalog on APIs.io includes 1 Spectral governance ruleset.


  Meilisearch''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, engineering blog, changelog, and 14 more developer resources.'
plans:
- name: Meilisearch Plans Pricing
  plan_count: 4
  slug: meilisearch-plans-pricing
- name: Meilisearch Price Estimates
  plan_count: 0
  slug: meilisearch-price-estimates
random_paper: 6
rate_limits:
- limit_count: 3
  name: Meilisearch Rate Limits
  slug: meilisearch-rate-limits
rules:
- authorship: provider
  effective_rule_count: 41
  extends:
  - spectral:oas
  name: Meilisearch — meilisearch rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: meilisearch-meilisearch-spectral-rules
score:
  band: developing
  composite: 52.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 55.0
    catalog_earned_first_party: 17.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 64.5
    contract_governance: 15.2
    contract_quality: 47.4
    developer_ergonomics: 61.9
    discoverability: 56.7
    operational_transparency: 36.8
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/meilisearch/meilisearch-2026-06-20T185134.png
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
