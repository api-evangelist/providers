---
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: REST API (HTTP + JSON, API-key auth via ?api_key=) returning structured data from a catalog of sites. Endpoints include Product, Search, Universal Web Scraper, and Batch (async). Base host is api.choc
  name: Chocodata Scraper API
  slug: chocodata-scraper-api
artifact_total: 1
created: '2026-07-16'
description: Web-scraping REST API that returns structured JSON from a large catalog of target sites (e-commerce, search engines, social, real estate, finance, and more), with proxies, CAPTCHA, and anti-bot handling managed server-side. Offers an npm-distributed MCP server, a live llms.txt docs manifest, and published Claude agent skills.
layout: provider
modified: '2026-07-16'
name: Chocodata
nav: Providers
network: true
overview: Chocodata publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include web-scraping, data-extraction, serp, e-commerce-data, and social-media-data.
random_paper: 30
score:
  band: minimal
  composite: 5.9
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chocodata/refs/heads/main/screenshots/chocodata-2026-07-25T205249.png
slug: chocodata
tags:
- web-scraping
- data-extraction
- serp
- e-commerce-data
- social-media-data
- proxy
- mcp
- agent-native
- structured-json
---
