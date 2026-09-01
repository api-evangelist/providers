---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.8
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tamara-mellon-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tamara-mellon-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tamara-mellon-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tamara-mellon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shop.tamaramellon.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TamaraMellon
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/tamara-mellon_stock/
coverage:
  checked: '2026-08-29'
  detail: 'Tamara Mellon is a direct-to-consumer luxury footwear retailer with no developer program, and its web presence is currently dark: www.tamaramellon.com returns a bare HTTP 404 on every path from an unprovisioned CDN origin whose TLS certificate does not cover the domain, while the brand''s Shopify storefront at shop.tamaramellon.com 302s to a store password gate, so the only machine-readable documents on any host it controls are Shopify''s own Customer Account OIDC/OAuth metadata.'
  evidence:
  - status: 404
    url: https://www.tamaramellon.com/
  - status: 404
    url: https://www.tamaramellon.com/.well-known/api-catalog
  - status: 302
    url: https://shop.tamaramellon.com/
  - status: 401
    url: https://shop.tamaramellon.com/products.json
  - status: 404
    url: https://www.tamaramellon.com/api/ucp/mcp
  - status: 200
    url: https://shop.tamaramellon.com/.well-known/openid-configuration
  - status: 200
    url: https://github.com/TamaraMellon
  reason: not-a-software-company
  state: none
created: '2026-08-29'
description: 'Tamara Mellon Brand, Inc. is a Los Angeles based direct-to-consumer luxury footwear company founded in 2016 by designer Tamara Mellon, co-founder of Jimmy Choo, together with chief executive Jill Layfield. The brand sells Italian-made women''s shoes and accessories straight to customers online rather than through wholesale, releasing product in monthly drops instead of following the traditional fashion calendar, and it is reported to have raised roughly $87 million in venture funding after the earlier Tamara Mellon LLC filed for Chapter 11 in 2015. In August 2025 the company announced a licensing and operating partnership with footwear licensing firm Titan Industries. It is a consumer goods retailer rather than a software company: it publishes no public API, developer portal, SDK, or machine-readable specification of any kind. As probed on 2026-08-29 its canonical domain returns HTTP 404 on every path from an unprovisioned CDN origin, and its Shopify storefront at shop.tamaramellon.com
  redirects to a store password gate.'
image: https://avatars.githubusercontent.com/u/25162387?v=4
layout: provider
modified: '2026-08-29'
name: Tamara Mellon
nav: Providers
network: true
overview: Tamara Mellon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fashion, Footwear, Luxury, and Retail.
random_paper: 20
scopes:
- name: Tamara Mellon Scopes
  scope_count: 0
  slug: tamara-mellon-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 8.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Tamara Mellon Authentication
  slug: tamara-mellon-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Tamara Mellon Domain Security
  slug: tamara-mellon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tamara-mellon
tags:
- Company
- Fashion
- Footwear
- Luxury
- Retail
- Direct to Consumer
- E-Commerce
- Consumer Goods
- Apparel
website: https://shop.tamaramellon.com/
---
