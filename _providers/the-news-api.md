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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: The News Api Agentic Access
  operation_count: 6
  slug: the-news-api-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL: https://api.thenewsapi.com/v1
  baseurl_source: declared
  description: Full historical and live article database search.
  name: The News API All News API
  slug: the-news-api-all-news-api
- baseURL: https://api.thenewsapi.com/v1
  baseurl_source: declared
  description: Retrieve specific articles by UUID.
  name: The News API Articles API
  slug: the-news-api-articles-api
- baseURL: https://api.thenewsapi.com/v1
  baseurl_source: declared
  description: Latest headlines organized by category.
  name: The News API Headlines API
  slug: the-news-api-headlines-api
- baseURL: https://api.thenewsapi.com/v1
  baseurl_source: declared
  description: Articles similar to a given article.
  name: The News API Similar News API
  slug: the-news-api-similar-news-api
- baseURL: https://api.thenewsapi.com/v1
  baseurl_source: declared
  description: Available news sources and their metadata.
  name: The News API Sources API
  slug: the-news-api-sources-api
- baseURL: https://api.thenewsapi.com/v1
  baseurl_source: declared
  description: Top stories filtered by keyword, category, and date.
  name: The News API Top Stories API
  slug: the-news-api-top-stories-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: The News All News API
  slug: open-the-news-api-all-news-api
- collection_type: open
  name: The News All News Articles API
  slug: open-the-news-api-articles-api
- collection_type: open
  name: The News All News Headlines API
  slug: open-the-news-api-headlines-api
- collection_type: open
  name: The News All News Similar News API
  slug: open-the-news-api-similar-news-api
- collection_type: open
  name: The News All News Sources API
  slug: open-the-news-api-sources-api
- collection_type: open
  name: The News All News Top Stories API
  slug: open-the-news-api-top-stories-api
- collection_type: open
  name: The News API
  slug: open-the-news-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/the-news-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-news-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-news-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.thenewsapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.thenewsapi.com/documentation
- group: start
  title: ''
  type: Signup
  url: https://www.thenewsapi.com/register
- group: commercial
  title: ''
  type: Pricing
  url: https://www.thenewsapi.com/pricing
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/the-news-api-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/the-news-api-article-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/the-news-api-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/the-news-api-vocabulary.yml
created: '2025-02-09'
description: The News API provides free access to search worldwide news and top stories from over 40,000 sources in 50 countries. Access live and historical news articles with advanced filtering by keyword, category, language, country, domain, and date. The API supports boolean search operators, pagination, and returns structured article data including headlines, descriptions, images, and category classifications.
examples:
- key_count: 2
  name: The News Api Top Stories Example
  slug: the-news-api-top-stories-example
finops:
- name: The News Api Finops
  service_category: API
  slug: the-news-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-news-api.png
json_schemas:
- name: The News API Article
  property_count: 14
  slug: the-news-api-article
json_structures:
- name: The News Api Article Structure
  property_count: 0
  slug: the-news-api-article-structure
jsonld:
- class_count: 20
  name: The News Api Context
  property_count: 3
  slug: the-news-api-context
layout: provider
modified: '2026-05-19'
name: The News API
nav: Providers
network: true
overview: 'The News API publishes 6 APIs on the [APIs.io](https://apis.io/) network, including All News API, Articles API, Headlines API, and 3 more. Tagged areas include Articles, Headlines, News, Media, and Search.


  The The News API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  The News API''s developer surface includes authentication, documentation, signup flow, pricing, and 7 more developer resources.'
plans:
- name: The News Api Plans Pricing
  plan_count: 3
  slug: the-news-api-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: The News Api Rate Limits
  slug: the-news-api-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: The News API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: the-news-api-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: The News API API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 2
    info: 0
    warn: 4
  slug: the-news-api-rules
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 51.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 28.8
    contract_quality: 59.2
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/the-news-api/refs/heads/main/screenshots/the-news-api-2026-06-20T195226.png
security:
- kind: authentication
  name: The News Api Authentication
  slug: the-news-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: The News Api Domain Security
  slug: the-news-api-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: the-news-api
tags:
- Articles
- Headlines
- News
- Media
- Search
- International
website: https://www.thenewsapi.com/
---
