---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 30.9
  scored_at: '2026-09-01'
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
  name: Bombas MCP Server
  slug: bombas-mcp-server
modified: '2026-07-31'
name: Bombas
nav: Providers
network: true
overview: 'Bombas publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Apparel, and Direct to Consumer.


  Bombas'' developer surface includes documentation, support, signup flow, and 6 more developer resources.'
random_paper: 19
scopes:
- name: Bombas Scopes
  scope_count: 4
  slug: bombas-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 22.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- E-Commerce
- Apparel
- Direct to Consumer
- Commerce
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Shopify
website: https://bombas.com/
---
