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
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: The agent-facing commerce surface of the Bombas Shopify storefront. The store publishes a Universal Commerce Protocol merchant profile at https://shop.bombas.com/.well-known/ucp declaring UCP versions
  name: Bombas Commerce (UCP Shopping)
  slug: commerce
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bombas-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bombas.com/
- group: docs
  title: ''
  type: Documentation
  url: https://shop.bombas.com/agents.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bombas
- group: operate
  title: ''
  type: Support
  url: https://shop.bombas.com/pages/help
- group: start
  title: ''
  type: SignUp
  url: https://shop.bombas.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shop.bombas.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shop.bombas.com/policies/privacy-policy
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/bombas_stock/
created: '2026-07-31'
description: 'Bombas is a New York City based direct-to-consumer comfort apparel brand founded in 2013 by David Heath and Randy Goldberg, selling socks, underwear, t-shirts and slippers on a one-purchased-equals-one-donated model that has powered more than 200 million donated items through a network of over 4,000 giving partners serving people experiencing homelessness. The company is privately held, was funded on Shark Tank in 2014, and runs its ecommerce on Shopify Plus. Bombas does not publish a first-party developer program or REST API, but its storefront at shop.bombas.com exposes a real agent-facing commerce surface: a published llms.txt / agents.md, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, and a live MCP endpoint at /api/ucp/mcp implementing the UCP Shopping Service, alongside OAuth 2.0 / OpenID Connect discovery for Shopify customer accounts.'
image: https://avatars.githubusercontent.com/u/30065139?v=4
layout: provider
mcp_servers:
- description: ''
  name: bombas-mcp.yml
  slug: bombas-mcpyml
modified: '2026-07-31'
name: Bombas
nav: Providers
network: true
overview: 'Bombas publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Ecommerce, Apparel, and Direct to Consumer.


  Bombas'' developer surface includes documentation, support, signup flow, and 6 more developer resources.'
random_paper: 28
scopes:
- name: Bombas Scopes
  scope_count: 4
  slug: bombas-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 20.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 20.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bombas/refs/heads/main/screenshots/bombas-2026-08-07T162716.png
security:
- kind: authentication
  name: Bombas Authentication
  slug: bombas-authentication
  summary_line: oauth2/openIdConnect/custom-header · 3 schemes
- kind: domain-security
  name: Bombas Domain Security
  slug: bombas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bombas
tags:
- Company
- Retail
- Ecommerce
- Apparel
- Direct to Consumer
- Commerce
- Agentic Commerce
- Universal Commerce Protocol
- Model Context Protocol
- Shopify
website: https://bombas.com/
---
