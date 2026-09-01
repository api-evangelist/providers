---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST/JSON API for single-product (ASIN) extraction, search results, and async batch scraping across 20 Amazon marketplaces. API key auth via ?api_key= query parameter; only HTTP 2xx responses are bill
  name: Amazon Scraper REST API
  slug: amazon-scraper-rest-api
artifact_total: 1
created: '2026-07-16'
description: REST/JSON API for extracting structured Amazon product, search, and batch data across 20 marketplaces, with key-based authentication, official SDKs, a CLI, and a local MCP server. Operated independently under the ChocoData namespace; not affiliated with Amazon.com, Inc.
layout: provider
modified: '2026-07-16'
name: Amazon Scraper API
nav: Providers
network: true
overview: Amazon Scraper API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Web Scraping, Data Extraction, E-Commerce Data, Amazon, and marketplace data.
random_paper: 17
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 1
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 7.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-scraper-api/refs/heads/main/screenshots/amazon-scraper-api-2026-07-25T200010.png
slug: amazon-scraper-api
tags:
- Web Scraping
- Data Extraction
- E-Commerce Data
- Amazon
- marketplace data
- Product Intelligence
- Price Monitoring
- Competitor Research
- MCP
- Agent Tooling
---
