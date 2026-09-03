---
access_model:
  confidence: high
  label: Self-serve freemium — Google login, free 200 req/day tier, in-browser playground
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - https://usebolsai.com/#pricing
  - https://usebolsai.com/#playground
  trial: true
  try_now: true
api_count: 2
apis:
- description: REST/JSON API for Brazilian financial-market data — equities, FIIs, fundamentals, dividends, financial statements, and macro series. Authenticated via X-API-Key header.
  name: Bolsai Financial Data API
  slug: bolsai-financial-data-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bolsai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bolsai-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/bolsai-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bolsai-well-known.yml
- group: company
  title: ''
  type: Blog
  url: https://usebolsai.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://usebolsai.com/#pricing
- group: operate
  title: ''
  type: Support
  url: mailto:vinicius.lazzari@usebolsai.com
created: '2026-07-06'
description: Brazilian financial-market data REST API serving equities, real-estate funds (FIIs), fundamentals, dividends, financial statements, and macroeconomic series sourced from official feeds (B3, CVM, BCB). Covers 350+ B3 stocks, 400+ FIIs and 40 years of price history, with an official MCP server (hosted OAuth endpoint and PyPI package) for AI agents.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bolsai.png
layout: provider
mcp_servers:
- description: Official Bolsai MCP server exposing Brazilian financial-market data (B3 stocks, FIIs, fundamentals, dividends, CVM financial statements, BCB macro series) to MCP clients. Available BOTH as a hosted re
  name: Bolsai MCP Server
  slug: bolsai-mcp-server
modified: '2026-09-03'
name: Bolsai
nav: Providers
network: true
overview: 'Bolsai publishes 1 API on the [APIs.io](https://apis.io/) network: Financial Data API. Tagged areas include Finance, Financial Data, Market Data, Stocks/equities, and Real Estate Funds.


  Bolsai''s developer surface includes authentication, engineering blog, pricing, support, and 3 more developer resources.'
plans:
- name: Bolsai Plans Pricing
  plan_count: 3
  slug: bolsai-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Bolsai Rate Limits
  slug: bolsai-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/bolsai/refs/heads/main/screenshots/bolsai-2026-07-25T203539.png
security:
- kind: authentication
  name: Bolsai Authentication
  slug: bolsai-authentication
  summary_line: apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Bolsai Domain Security
  slug: bolsai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bolsai
tags:
- Finance
- Financial Data
- Market Data
- Stocks/equities
- Real Estate Funds
- Dividends
- Fundamentals
- Macroeconomic Data
- Brazil
- Developer Tools
- MCP
- AI Agents
---
