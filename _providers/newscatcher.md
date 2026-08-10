---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 48
  human_in_the_loop: 1
  name: Newscatcher Agentic Access
  operation_count: 79
  slug: newscatcher-agentic-access
  summary_line: 79 operations · 48 acting · 1 human-in-the-loop
api_count: 16
apis:
- description: Operations to aggregate news counts.
  name: Newscatcher AggregationCount API
  slug: newscatcher-aggregationcount-api
- description: Operations to search by author.
  name: Newscatcher Authors API
  slug: newscatcher-authors-api
- description: Operations to retrieve breaking news articles.
  name: Newscatcher BreakingNews API
  slug: newscatcher-breakingnews-api
- description: Operations to create and manage datasets of entities. A dataset is a named collection of entities — think of it as a watchlist or portfolio. Connect a dataset to a job via `connected_dataset_ids` to a
  name: Newscatcher Datasets API
  slug: newscatcher-datasets-api
- description: Operations to create, update, and delete company entities. Entities are the building blocks of Company Watchlist. Each entity represents a company (or person) you want to track. Add identifying inform
  name: Newscatcher Entities API
  slug: newscatcher-entities-api
- description: Operations to create, monitor, and retrieve job results.
  name: Newscatcher Jobs API
  slug: newscatcher-jobs-api
- description: Operations to retrieve local news latest headlines. Includes both standard location filtering and advanced GeoNames filtering.
  name: Newscatcher LatestHeadlines API
  slug: newscatcher-latestheadlines-api
- description: Operations to check API health and version.
  name: Newscatcher Meta API
  slug: newscatcher-meta-api
- description: Operations to create, operate and retrieve monitor results.
  name: Newscatcher Monitors API
  slug: newscatcher-monitors-api
- description: Operations to create, organize, and manage projects. A project is a named container for jobs, monitors, and datasets. Group related resources by use case, team, or client, and share them with teammate
  name: Newscatcher Projects API
  slug: newscatcher-projects-api
- description: Operations to search for local news articles. Includes both standard location filtering and advanced GeoNames filtering.
  name: Newscatcher Search API
  slug: newscatcher-search-api
- description: Operations to search local news by link, ID or RSS GUID.
  name: Newscatcher SearchBy API
  slug: newscatcher-searchby-api
- description: Operations to search by link or ID.
  name: Newscatcher SearchByLink API
  slug: newscatcher-searchbylink-api
- description: Operations to retrieve local news sources.
  name: Newscatcher Sources API
  slug: newscatcher-sources-api
- description: Operations to get subscription info.
  name: Newscatcher Subscription API
  slug: newscatcher-subscription-api
- description: Operations to create and manage reusable webhook endpoints. A webhook is a named HTTP endpoint that receives a POST notification when a job or monitor completes. Create webhooks once at the organizati
  name: Newscatcher Webhooks API
  slug: newscatcher-webhooks-api
artifact_total: 29
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/newscatcher-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/newscatcher-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/newscatcher-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.newscatcherapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.newscatcherapi.com/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Newscatcher
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/newscatcherapi
- group: company
  title: ''
  type: Blog
  url: https://www.newscatcherapi.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.newscatcherapi.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.newscatcherapi.com
- group: other
  title: ''
  type: X
  url: https://x.com/newscatcherapi
- group: commercial
  title: ''
  type: Plans
  url: plans/newscatcher-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/newscatcher-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/newscatcher-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/newscatcher-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchemaCollection
  url: json-schema/newscatcher-article-schema.json
- group: docs
  title: ''
  type: JSONSchemaCollection
  url: json-schema/newscatcher-search-response-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/newscatcher-context.jsonld
created: '2026-06-12'
description: Newscatcher is a news search and aggregation API platform that provides access to over 120,000 news sources worldwide with full-text search, NLP enrichment, entity extraction, sentiment analysis, and automated clustering. The platform offers three core products — a News API for structured article retrieval, a Web Search (CatchAll) API for recall-first AI-grade web search, and a Local News API for hyper-local geographic news coverage. All APIs return clean, enriched, and deduplication-ready data designed for enterprise risk teams, financial services, AI platforms, and media intelligence workflows. The company is backed by Y Combinator (S22) and holds ISO certifications and SOC2 Type II compliance.
examples:
- key_count: 2
  name: Newscatcher Catchall Submit Example
  slug: newscatcher-catchall-submit-example
- key_count: 12
  name: Newscatcher Search Request Example
  slug: newscatcher-search-request-example
- key_count: 9
  name: Newscatcher Search Response Example
  slug: newscatcher-search-response-example
finops:
- name: Newscatcher Finops
  service_category: ''
  slug: newscatcher-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/newscatcher.png
json_schemas:
- name: Newscatcher Article
  property_count: 31
  slug: newscatcher-article
- name: Newscatcher Search Response
  property_count: 9
  slug: newscatcher-search-response
jsonld:
- class_count: 34
  name: Newscatcher Context
  property_count: 36
  slug: newscatcher-context
layout: provider
modified: '2026-06-12'
name: Newscatcher
nav: Providers
network: true
overview: 'Newscatcher publishes 16 APIs on the [APIs.io](https://apis.io/) network, including AggregationCount API, Authors API, BreakingNews API, and 13 more. Tagged areas include News, Search, NLP, Sentiment Analysis, and Entity Extraction.


  The Newscatcher catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Newscatcher''s developer surface includes authentication, documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Newscatcher Plans Pricing
  plan_count: 7
  slug: newscatcher-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 11
  name: Newscatcher Rate Limits
  slug: newscatcher-rate-limits
rules:
- name: Newscatcher API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: newscatcher-jsonschema-spectral-rules
score:
  band: developing
  composite: 55.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 72.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 55.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/newscatcher/refs/heads/main/screenshots/newscatcher-2026-06-20T190251.png
security:
- kind: authentication
  name: Newscatcher Authentication
  slug: newscatcher-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Newscatcher Domain Security
  slug: newscatcher-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: newscatcher
tags:
- News
- Search
- NLP
- Sentiment Analysis
- Entity Extraction
- Clustering
- Media Intelligence
- Financial Intelligence
- AI
- Enterprise
website: https://www.newscatcherapi.com
---
