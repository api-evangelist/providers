---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Savvly Agentic Access
  operation_count: 12
  slug: savvly-agentic-access
  summary_line: 12 operations
api_count: 1
apis:
- baseURL: https://api.savvly.com
  baseurl_source: spec
  description: The Comparisons API from Savvly — 2 operation(s) for comparisons.
  name: Savvly Comparisons API
  slug: savvly-comparisons-api
- baseURL: https://api.savvly.com
  baseurl_source: spec
  description: The Product API from Savvly — 6 operation(s) for product.
  name: Savvly Product API
  slug: savvly-product-api
- baseURL: https://api.savvly.com
  baseurl_source: spec
  description: The Projections API from Savvly — 4 operation(s) for projections.
  name: Savvly Projections API
  slug: savvly-projections-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Savvly Public Comparisons API
  slug: open-savvly-comparisons-api
- collection_type: open
  name: Savvly Public Comparisons Product API
  slug: open-savvly-product-api
- collection_type: open
  name: Savvly Public Comparisons Projections API
  slug: open-savvly-projections-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/savvly-compare-and-explain.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/savvly-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/savvly-openapi-overlay.yaml
- group: other
  title: ''
  type: AgentCard
  url: a2a/savvly-a2a.yml
- group: company
  title: ''
  type: Website
  url: https://savvly.com/
created: '2026-07-17'
description: Savvly is a company surfaced as a portfolio company of techstars and added to the API Evangelist network as a stub for enrichment. This profile is a lead awaiting the enrichment pipeline.
layout: provider
mcp_servers:
- description: First-party Savvly MCP server exposing the Savvly Public API (product data, projections, comparisons, eligibility, FAQ) to AI agents. No authentication; rate-limited. Also distributed as npm @savvly/m
  name: Savvly MCP Server
  slug: savvly-mcp-server
modified: '2026-07-17'
name: Savvly
nav: Providers
network: true
overview: 'Savvly publishes 3 APIs on the [APIs.io](https://apis.io/) network: Comparisons API, Product API, and Projections API. Tagged areas include Company.'
random_paper: 5
screenshot: https://raw.githubusercontent.com/api-evangelist/savvly/refs/heads/main/screenshots/savvly-2026-09-02T154449.png
security:
- kind: domain-security
  name: Savvly Domain Security
  slug: savvly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: savvly
tags:
- Company
website: https://savvly.com/
---
