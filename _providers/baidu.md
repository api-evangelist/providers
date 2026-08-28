---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: OpenAI-compatible LLM / Model-as-a-Service API hosting the ERNIE family and select open models (DeepSeek, GLM, etc.) via chat completions and embeddings.
  name: Baidu AI Cloud Qianfan
  slug: baidu-ai-cloud-qianfan
- description: 'LBS web-service API: geocoding, reverse geocoding, place/POI search, route planning, weather, IP location, and real-time traffic. Ships an official MCP server.'
  name: Baidu Maps Open Platform
  slug: baidu-maps-open-platform
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.baidu.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ai.baidu.com/
- group: docs
  title: ''
  type: Documentation
  url: https://intl.cloud.baidu.com/doc/qianfan/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://lbsyun.baidu.com/faq/api?title=webapi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/baidubce
- group: start
  title: ''
  type: SignUp
  url: https://console.bce.baidu.com/
- group: build
  title: ''
  type: Packages
  url: packages/baidu-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/baidu-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/baidu-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/baidu-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/baidu-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/baidu-llms.txt
created: '2026-07-17'
description: Baidu is a leading Chinese internet and artificial-intelligence company whose developer surface spans three main product lines. Baidu AI Cloud "Qianfan" is a Model-as-a-Service platform hosting the ERNIE model family behind an OpenAI-compatible REST API for chat, embeddings, and agent building (AppBuilder). The Baidu AI Open Platform exposes OCR, NLP, speech, face, image, and knowledge-graph APIs. The Baidu Maps Open Platform (LBS) provides geocoding, place search, route planning, weather, and real-time traffic to millions of registered developers, and ships an official Model Context Protocol (MCP) server with a hosted remote endpoint. This profile was surfaced as a portfolio company and enriched with real, first-party developer artifacts.
image: https://www.baidu.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Baidu MCP Server
  slug: baidu-mcp-server
modified: '2026-07-18'
name: Baidu
nav: Providers
network: true
overview: 'Baidu publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Artificial Intelligence, Machine-Learning, and LLM.


  Baidu''s developer surface includes documentation, API reference, signup flow, authentication, and 8 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 19.6
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 19.6
  provenance:
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/baidu/refs/heads/main/screenshots/baidu-2026-07-25T202358.png
security:
- kind: authentication
  name: Baidu Authentication
  slug: baidu-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Baidu Domain Security
  slug: baidu-domain-security
  summary_line: TLSv1.2 · DMARC
slug: baidu
tags:
- Company
- Technology
- Artificial Intelligence
- Machine-Learning
- LLM
- Maps
- Geolocation
- Cloud
- China
website: https://www.baidu.com
---
