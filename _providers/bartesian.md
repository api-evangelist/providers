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
- description: The agent-facing commerce surface of the Bartesian Shopify storefront. The store publishes a Universal Commerce Protocol merchant profile at https://bartesian.com/.well-known/ucp declaring UCP version
  name: Bartesian Commerce (UCP Shopping)
  slug: commerce
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bartesian-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bartesian.com/
- group: docs
  title: ''
  type: Documentation
  url: https://bartesian.com/agents.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bartesian
- group: operate
  title: ''
  type: Support
  url: https://bartesian.com/pages/help
- group: operate
  title: ''
  type: HelpCenter
  url: https://bartesian.com/pages/faq
- group: company
  title: ''
  type: Blog
  url: https://bartesian.com/blogs/news
- group: commercial
  title: ''
  type: Pricing
  url: https://bartesian.com/collections/cocktail-machine
- group: start
  title: ''
  type: SignUp
  url: https://bartesian.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bartesian.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bartesian.com/policies/privacy-policy
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/
created: '2026-08-06'
description: 'Bartesian is a Chicago-based consumer appliance company founded in 2014 by Ryan Close, maker of a capsule-based countertop cocktail machine that mixes bar-quality drinks on demand from a pod of bitters, juices and extracts plus the user''s own base spirit. The company launched off a Kickstarter campaign, took investment from Beam Suntory in 2016, and closed a US$20 million round led by Cleveland Avenue in 2021. It runs a razor-and-blade model selling machines and cocktail capsules direct to consumers, plus commercial placements in stadiums and airport lounges. Bartesian publishes no first-party developer program or REST API, but its Shopify storefront at bartesian.com exposes a real and unusually open agent-facing commerce surface: a published llms.txt and agents.md, a dedicated agentic-discovery sitemap, a Universal Commerce Protocol merchant profile at /.well-known/ucp, and a live MCP endpoint at /api/ucp/mcp that returns all 13 UCP Shopping tools with complete JSON Schema
  inputSchemas to an anonymous caller - gating execution, not discovery - alongside OAuth 2.0 / OpenID Connect discovery for Shopify customer accounts.'
image: https://avatars.githubusercontent.com/u/220963642?v=4
layout: provider
mcp_servers:
- description: ''
  name: Bartesian MCP Server
  slug: bartesian-mcp-server
modified: '2026-08-06'
name: Bartesian
nav: Providers
network: true
overview: 'Bartesian publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Consumer Products, and Appliances.


  Bartesian''s developer surface includes documentation, support, engineering blog, pricing, signup flow, and 7 more developer resources.'
random_paper: 8
scopes:
- name: Bartesian Scopes
  scope_count: 4
  slug: bartesian-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 25.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bartesian/refs/heads/main/screenshots/bartesian-2026-08-07T162210.png
security:
- kind: authentication
  name: Bartesian Authentication
  slug: bartesian-authentication
  summary_line: oauth2/openIdConnect/custom-header · 3 schemes
- kind: domain-security
  name: Bartesian Domain Security
  slug: bartesian-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bartesian
tags:
- Company
- Retail
- E-Commerce
- Consumer Products
- Appliances
- Beverages
- Direct to Consumer
- Commerce
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Shopify
website: https://bartesian.com/
---
