---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
  score: 20.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Google News Agentic Access
  operation_count: 4
  slug: google-news-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://news.google.com/rss
  baseurl_source: declared
  description: Retrieve top news headlines
  name: Google News RSS Headlines API
  slug: google-news-headlines-api
- baseURL: https://news.google.com/rss
  baseurl_source: declared
  description: Search for news articles
  name: Google News RSS Search API
  slug: google-news-search-api
- baseURL: https://news.google.com/rss
  baseurl_source: declared
  description: Retrieve news by topic
  name: Google News RSS Topics API
  slug: google-news-topics-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google News RSS Headlines API
  slug: open-google-news-headlines-api
- collection_type: open
  name: Google News RSS Headlines Search API
  slug: open-google-news-search-api
- collection_type: open
  name: Google News RSS Headlines Topics API
  slug: open-google-news-topics-api
- collection_type: open
  name: Google News RSS API
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-news-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-news-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-news-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/google-news-initiative
- group: start
  title: ''
  type: Portal
  url: https://news.google.com
- group: start
  title: ''
  type: GettingStarted
  url: https://news.google.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://support.google.com/news
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/google-news/refs/heads/main/json-ld/google-news.jsonld
- group: company
  title: ''
  type: Blog
  url: https://blog.google/outreach-initiatives/google-news-initiative/rss/
created: '2026-03-13'
description: Google News provides RSS feeds that deliver news headlines organized by topic, location, and search query. The feeds expose structured XML data that can be consumed programmatically to retrieve top stories, topic-based headlines (World, Business, Technology, Sports, etc.), location-specific news, and keyword search results across multiple languages and regions.
finops:
- name: Google News Finops
  service_category: API
  slug: google-news-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-news.png
json_schemas:
- name: Google News RSS Feed Schema
  property_count: 0
  slug: google-news
jsonld:
- class_count: 0
  name: Google News Context
  property_count: 8
  slug: google-news
layout: provider
modified: '2026-05-19'
name: Google News RSS
nav: Providers
network: true
overview: 'Google News RSS publishes 3 APIs on the [APIs.io](https://apis.io/) network: Headlines API, Search API, and Topics API. Tagged areas include Aggregation, Google News, Headlines, Media, and News.


  The Google News RSS catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google News RSS''s developer surface includes developer portal, getting-started guide, support, engineering blog, and 7 more developer resources.'
plans:
- name: Google News Plans Pricing
  plan_count: 3
  slug: google-news-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Google News Rate Limits
  slug: google-news-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google News RSS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-news-jsonschema-spectral-rules
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: Google News RSS API Rules
  rule_count: 15
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 4
  slug: google-news-spectral-rules
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 12
    catalog_gap: 44.5
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 13.6
    contract_quality: 57.1
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-news/refs/heads/main/screenshots/google-news-2026-06-20T182219.png
security:
- kind: domain-security
  name: Google News Domain Security
  slug: google-news-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google News Vulnerability Disclosure
  slug: google-news-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-news
tags:
- Aggregation
- Google News
- Headlines
- Media
- News
- RSS
website: https://news.google.com
---
