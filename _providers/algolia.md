---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 11
apis:
- description: Core indexing and search API for adding, updating, and deleting records and querying them with typo-tolerant, faceted, geo-aware, and rule-driven search served from globally distributed search nodes (
  name: Algolia Search API
  slug: algolia-search-api
- description: Inbound event-ingestion API for click, conversion, view, and purchase signals that feed Personalization, Recommend, A/B Testing, and Analytics. Accepts events; does not emit them.
  name: Algolia Insights API
  slug: algolia-insights-api
- description: Returns related-products, frequently-bought-together, trending, and look-alike recommendations trained from Insights events and catalog data.
  name: Algolia Recommend API
  slug: algolia-recommend-api
- description: Reports top searches, no-result searches, click/conversion rates, and other search analytics aggregated from query and Insights data.
  name: Algolia Analytics API
  slug: algolia-analytics-api
- description: Creates and manages A/B tests across index configurations and relevance settings, scoring variants on click-through and conversion.
  name: Algolia A/B Testing API
  slug: algolia-ab-testing-api
- description: Configures and applies user-affinity profiles built from Insights events to re-rank search and browse results per user.
  name: Algolia Personalization API
  slug: algolia-personalization-api
- description: Manages Algolia's hosted web crawler that extracts content from websites and pushes it into indices on a schedule.
  name: Algolia Crawler API
  slug: algolia-crawler-api
- description: Connector-based data ingestion that pulls records from sources (databases, storage, ecommerce platforms) into Algolia indices via managed tasks.
  name: Algolia Ingestion API
  slug: algolia-ingestion-api
- description: Generates and maintains query-suggestion indices from popular searches to power as-you-type autocomplete.
  name: Algolia Query Suggestions API
  slug: algolia-query-suggestions-api
- description: Exposes server status, latency, indexing, and reachability metrics for an application's Algolia infrastructure.
  name: Algolia Monitoring API
  slug: algolia-monitoring-api
- description: Returns per-application usage metrics (operations, records, search volume) for cost and quota tracking.
  name: Algolia Usage API
  slug: algolia-usage-api
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/algolia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.algolia.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.algolia.com/doc/
- group: docs
  title: ''
  type: APIReference
  url: https://www.algolia.com/doc/api-reference/
- group: start
  title: ''
  type: Signup
  url: https://dashboard.algolia.com/users/sign_up
- group: commercial
  title: ''
  type: Pricing
  url: https://www.algolia.com/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/algolia
- group: operate
  title: ''
  type: Status
  url: https://status.algolia.com
- group: commercial
  title: ''
  type: Plans
  url: plans/algolia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/algolia-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/algolia-finops.yml
created: '2026-05-04'
description: Algolia is a hosted search and discovery platform that delivers fast, typo-tolerant search, browse, recommendations, and personalization through a suite of REST APIs and edge-distributed infrastructure. It powers search experiences for ecommerce, media, SaaS, and content sites, pairing a synchronous indexing and query control plane with event-driven Insights, Recommend, A/B Testing, and Personalization products.
finops:
- name: Algolia Finops
  service_category: Search
  slug: algolia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/algolia.png
layout: provider
modified: '2026-06-16'
name: Algolia
nav: Providers
network: true
overview: 'Algolia publishes 11 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Search, Discovery, Recommendations, Personalization, and Analytics.


  Algolia''s developer surface includes documentation, API reference, signup flow, pricing, status page, and 6 more developer resources.'
plans:
- name: Algolia Plans Pricing
  plan_count: 4
  slug: algolia-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 4
  name: Algolia Rate Limits
  slug: algolia-rate-limits
score:
  band: emerging
  composite: 25.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 25.2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/algolia/refs/heads/main/screenshots/algolia-2026-06-20T171526.png
security:
- kind: domain-security
  name: Algolia Domain Security
  slug: algolia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: algolia
tags:
- Search
- Discovery
- Recommendations
- Personalization
- Analytics
- Ecommerce
website: https://www.algolia.com
---
