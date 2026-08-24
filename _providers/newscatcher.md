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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-24'
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
artifact_total: 46
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Local News AggregationCount API
  slug: open-newscatcher-aggregationcount-api
- collection_type: open
  name: Local News AggregationCount Authors API
  slug: open-newscatcher-authors-api
- collection_type: open
  name: Local News AggregationCount BreakingNews API
  slug: open-newscatcher-breakingnews-api
- collection_type: open
  name: Local News AggregationCount Datasets API
  slug: open-newscatcher-datasets-api
- collection_type: open
  name: Local News AggregationCount Entities API
  slug: open-newscatcher-entities-api
- collection_type: open
  name: Local News AggregationCount Jobs API
  slug: open-newscatcher-jobs-api
- collection_type: open
  name: Local News AggregationCount LatestHeadlines API
  slug: open-newscatcher-latestheadlines-api
- collection_type: open
  name: Local News AggregationCount Meta API
  slug: open-newscatcher-meta-api
- collection_type: open
  name: Local News AggregationCount Monitors API
  slug: open-newscatcher-monitors-api
- collection_type: open
  name: Local News AggregationCount Projects API
  slug: open-newscatcher-projects-api
- collection_type: open
  name: Local News AggregationCount Search API
  slug: open-newscatcher-search-api
- collection_type: open
  name: Local News AggregationCount SearchBy API
  slug: open-newscatcher-searchby-api
- collection_type: open
  name: Local News AggregationCount SearchByLink API
  slug: open-newscatcher-searchbylink-api
- collection_type: open
  name: Local News AggregationCount Sources API
  slug: open-newscatcher-sources-api
- collection_type: open
  name: Local News AggregationCount Subscription API
  slug: open-newscatcher-subscription-api
- collection_type: open
  name: Local News AggregationCount Webhooks API
  slug: open-newscatcher-webhooks-api
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
random_paper: 20
rate_limits:
- limit_count: 11
  name: Newscatcher Rate Limits
  slug: newscatcher-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Newscatcher API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: newscatcher-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.2
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 72.6
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 52.6
  previous_composite: 50.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.12.1
  scored_at: '2026-08-24'
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
- Artificial Intelligence
- Enterprise
website: https://www.newscatcherapi.com
---
