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
agent_readiness:
  band: agent-aware
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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The Shopify-native Universal Commerce Protocol (UCP) surface for the Mophones storefront — a published UCP merchant profile plus a UCP-over-MCP shopping endpoint that agents use to search the catalog,
  name: Mophones Agentic Commerce (UCP)
  slug: mophones-agentic-commerce-ucp
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://mophones.co
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mophones-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mophones-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mophones-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mophones-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mophones.co/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mophones.co/policies/terms-of-service
created: '2026-07-17'
description: Mophones (MoPhones) is a Nairobi, Kenya based fintech and recommerce company building accessible device-financing and re-commerce infrastructure for Africa, starting with premium refurbished smartphones from brands like Apple and Samsung sold with flexible weekly-installment and pay-on-delivery plans. The consumer storefront runs on Shopify at mophones.co and does not expose a first-party developer API; its only programmatic surface is the Shopify-provided agentic-commerce layer — a published Universal Commerce Protocol (UCP) profile at /.well-known/ucp and a live UCP-over-MCP shopping endpoint at /api/ucp/mcp that lets buyer-approved AI shopping agents search the catalog, build carts, and complete Shop Pay checkouts. Mophones is backed by Speedinvest and was noted as the first African startup to secure NICE financing from STV.
image: https://mophones.co/cdn/shop/files/MO-Logo-01-White-Background-Navy_Logo.jpg?v=1692099098
layout: provider
mcp_servers:
- description: ''
  name: mophones-mcp.yml
  slug: mophones-mcpyml
modified: '2026-07-20'
name: Mophones
nav: Providers
network: true
overview: Mophones publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Commerce, Agentic Commerce, and Universal Commerce Protocol.
random_paper: 128
score:
  band: emerging
  composite: 13.6
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.6
  provenance:
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mophones/refs/heads/main/screenshots/mophones-2026-08-07T184253.png
security:
- kind: domain-security
  name: Mophones Domain Security
  slug: mophones-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mophones
tags:
- Company
- E-Commerce
- Commerce
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Shopify
- Fintech
- Recommerce
- Africa
website: https://mophones.co
---
