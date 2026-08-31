---
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.2
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: A live, remotely hosted Model Context Protocol server operated by SellerX at mcp.sellerx.com. The endpoint requires an OAuth 2.1 bearer token, so the tool manifest is auth-gated, but the server publis
  name: SellerX MCP Server
  slug: mcp
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sellerx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sellerx.com/
- group: company
  title: ''
  type: About
  url: https://www.sellerx.com/about/
- group: other
  title: ''
  type: Products
  url: https://www.sellerx.com/brands/
- group: company
  title: ''
  type: Careers
  url: https://www.sellerx.com/work-with-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sellerx.com/privacy-policy
- group: commercial
  title: ''
  type: Legal
  url: https://www.sellerx.com/imprint
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kwcommerce
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/seller-x
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sellerx-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sellerx-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sellerx-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sellerx-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sellerx-conformance.yml
created: '2026-08-05'
description: SellerX is a Berlin-based consumer-brand builder, founded in 2020, that acquires, operates and scales everyday consumer products into omnichannel global brands. Originally one of Europe's largest Amazon FBA aggregators, it merged with KW Commerce in 2021 and with the US aggregator Elevate Brands in 2023, and has since repositioned itself from an aggregator into a brand builder. The group operates 20+ brands and 25k+ products across 10+ countries from hubs in Berlin, London, Manila and Dongguan, and has raised more than $750M in equity and debt from Sofina, L Catterton, Cherry Ventures, Felix Capital, 83North, an ADIA subsidiary, BlackRock and Victory Park Capital. SellerX sells consumer goods to consumers through marketplaces and its own channels; it publishes no public API, developer portal, SDK or machine-readable specification of its own.
image: https://www.sellerx.com/logo.png
layout: provider
mcp_servers:
- description: ''
  name: SellerX MCP Server
  slug: sellerx-mcp-server
modified: '2026-08-05'
name: SellerX
nav: Providers
network: true
overview: 'SellerX publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Consumer Brands, Retail, and Amazon Aggregator.


  SellerX''s developer surface includes legal docs, authentication, and 12 more developer resources.'
random_paper: 11
scopes:
- name: Sellerx Scopes
  scope_count: 1
  slug: sellerx-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 13.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Sellerx Authentication
  slug: sellerx-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Sellerx Domain Security
  slug: sellerx-domain-security
  summary_line: TLSv1.2 · DMARC
slug: sellerx
tags:
- Company
- E-Commerce
- Consumer Brands
- Retail
- Amazon Aggregator
- Marketplace Seller
- Consumer Packaged Goods
- Germany
website: https://www.sellerx.com/
---
