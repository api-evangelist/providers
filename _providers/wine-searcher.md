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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Wine Searcher Agentic Access
  operation_count: 2
  slug: wine-searcher-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: Merchant price listings
  name: Wine-Searcher market-price API
  slug: wine-searcher-market-price-api
- description: Wine price check and data lookup
  name: Wine-Searcher wine-check API
  slug: wine-searcher-wine-check-api
artifact_total: 15
collections:
- collection_type: open
  name: Wine-Searcher API
  slug: open-wine-searcher
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wine-searcher-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wine-searcher-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wine-searcher-com
- group: company
  title: ''
  type: Website
  url: https://www.wine-searcher.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.wine-searcher.com/trade/ws-api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.wine-searcher.com/trade/developer
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wine-searcher.com/trade/api
- group: operate
  title: ''
  type: FAQ
  url: https://www.wine-searcher.com/trade/faq
- group: other
  title: ''
  type: DataFeed
  url: https://www.wine-searcher.com/trade/datafeed
- group: other
  title: ''
  type: Linking
  url: https://www.wine-searcher.com/trade/ws-link
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/wine-searcher/refs/heads/main/json-ld/wine-searcher-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/wine-searcher/refs/heads/main/vocabulary/wine-searcher-vocabulary.yml
created: '2025-02-24'
description: Wine-Searcher is the world's leading wine search engine and marketplace, providing access to prices, availability, and data on over 15 million wines from retailers worldwide. The Wine-Searcher API allows developers to integrate wine pricing data, merchant listings, critic scores, vintage availability, and wine details directly into websites and applications. Typical API consumers include wine apps, websites, blogs, market research companies, wine investment platforms, and insurance services.
examples:
- key_count: 6
  name: Wine Searcher Market Price Example
  slug: wine-searcher-market-price-example
- key_count: 6
  name: Wine Searcher Wine Check Example
  slug: wine-searcher-wine-check-example
finops:
- name: Wine Searcher Finops
  service_category: API
  slug: wine-searcher-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wine-searcher.png
json_schemas:
- name: MerchantListing
  property_count: 14
  slug: wine-searcher-merchant-listing
- name: Wine
  property_count: 13
  slug: wine-searcher-wine
jsonld:
- class_count: 15
  name: Wine Searcher Context
  property_count: 16
  slug: wine-searcher-context
layout: provider
modified: '2026-05-19'
name: Wine-Searcher
nav: Providers
network: true
overview: 'Wine-Searcher publishes 2 APIs on the [APIs.io](https://apis.io/) network: market-price API and wine-check API. Tagged areas include Data, Marketplace, Wine, Prices, and Merchants.


  The Wine-Searcher catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Wine-Searcher''s developer surface includes documentation, pricing, FAQ, and 9 more developer resources.'
plans:
- name: Wine Searcher Plans Pricing
  plan_count: 3
  slug: wine-searcher-plans-pricing
random_paper: 90
rate_limits:
- limit_count: 5
  name: Wine Searcher Rate Limits
  slug: wine-searcher-rate-limits
rules:
- name: Wine-Searcher API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: wine-searcher-jsonschema-spectral-rules
- name: Wine-Searcher API Rules
  rule_count: 9
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 2
  slug: wine-searcher-rules
score:
  band: developing
  composite: 48.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 63.6
    developer_ergonomics: 17.4
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 48.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wine-searcher/refs/heads/main/screenshots/wine-searcher-2026-06-20T201514.png
security:
- kind: domain-security
  name: Wine Searcher Domain Security
  slug: wine-searcher-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wine-searcher
tags:
- Data
- Marketplace
- Wine
- Prices
- Merchants
- Vintages
- Critics
website: https://www.wine-searcher.com
---
