---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 1
apis:
- description: 'Agent-commerce surface for the TTRacing Shopify store: a hosted UCP shopping MCP endpoint plus unauthenticated read-only product/collection JSON browsing.'
  name: TTRacing Storefront (UCP Agent Commerce)
  slug: ttracing-storefront-ucp-agent-commerce
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://ttracing.my
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ttracing-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ttracing-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ttracing-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ttracing-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ttracing-domain-security.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ttracing.my/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ttracing.my/policies/privacy-policy
created: '2026-07-17'
description: 'TTRacing is a Malaysian gaming chair and gaming furniture brand selling ergonomic gaming chairs, office chairs, and accessories through an online Shopify storefront at ttracing.my. The store is agent-commerce ready: it publishes an llms.txt and agents.md with explicit agent instructions, a UCP (Universal Commerce Protocol) discovery document at /.well-known/ucp, and a hosted Model Context Protocol (MCP) endpoint that lets AI shopping agents search the catalog, build carts, and run buyer-approved checkout. Human customer accounts are handled via Shopify''s OpenID Connect / OAuth 2.0 authorization server. Surfaced as a 500 Global portfolio company and enriched from live probes of its public agent-facing surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ttracing.png
layout: provider
mcp_servers:
- description: ''
  name: TTRacing UCP Shopping MCP
  slug: ttracing-ucp-shopping-mcp
modified: '2026-07-21'
name: TTRacing
nav: Providers
network: true
overview: TTRacing publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming Chairs, Gaming Furniture, E-Commerce, and Retail.
random_paper: 20
screenshot: https://raw.githubusercontent.com/api-evangelist/ttracing/refs/heads/main/screenshots/ttracing-2026-09-02T164508.png
security:
- kind: domain-security
  name: Ttracing Domain Security
  slug: ttracing-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ttracing
tags:
- Company
- Gaming Chairs
- Gaming Furniture
- E-Commerce
- Retail
- Agent Commerce
- MCP
- Shopify
- Malaysia
website: https://ttracing.my
---
