---
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 25.4
  scored_at: '2026-09-06'
api_count: 1
apis:
- description: The Universal Commerce Protocol (UCP) shopping service for the uppercase storefront, exposed as a remote Model Context Protocol server over HTTP JSON-RPC at https://uppercase.co.in/api/ucp/mcp. An ano
  name: uppercase UCP Shopping MCP
  slug: uppercase-ucp-shopping-mcp
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acefouraccessories-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://uppercase.co.in/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acefouraccessories-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/acefouraccessories-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/acefouraccessories-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/acefouraccessories-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/acefouraccessories-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/acefouraccessories-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/acefouraccessories-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acefouraccessories-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/acefouraccessories-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/acefouraccessories-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/acefouraccessories-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/acefouraccessories-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Blog
  url: https://uppercase.co.in/blogs/blogs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uppercase.co.in/pages/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uppercase.co.in/pages/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://uppercase.co.in/pages/complaint-form
- group: company
  title: ''
  type: About
  url: https://uppercase.co.in/pages/about-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acefour-accessories-pvt-ltd/
created: '2026-09-06'
description: 'Acefour Accessories Private Limited is a Mumbai-based direct-to-consumer travel goods company, founded in 2021 by Sudip Ghose, Uday Sodhi and Arnob Kumar Mondal and trading under the brand "uppercase". It designs and sells hard and soft luggage, trolley bags, backpacks, duffles, office and college bags built from recycled materials, and sells them through its own Shopify storefront at uppercase.co.in alongside Indian marketplaces and retail. It is not a software vendor and publishes no developer program, no OpenAPI and no SDK. It does, however, expose a live and anonymously callable agent-commerce surface on its own domain: a Universal Commerce Protocol (UCP) shopping MCP server at /api/ucp/mcp advertising 13 catalog, cart, checkout and order tools, declared in /.well-known/ucp.json and documented for agents in /llms.txt. That surface is provided by the Shopify platform and operated under Acefour''s domain and merchant account.'
image: https://uppercase.co.in/cdn/shop/files/JB1.png?v=1738235635
layout: provider
mcp_servers:
- description: ''
  name: Acefour Accessories MCP Server
  slug: acefour-accessories-mcp-server
modified: '2026-09-06'
name: Acefour Accessories
nav: Providers
network: true
overview: 'Acefour Accessories publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Consumer Goods, and Travel.


  Acefour Accessories'' developer surface includes authentication, engineering blog, support, and 18 more developer resources.'
plans:
- name: Acefouraccessories Plans Pricing
  plan_count: 0
  slug: acefouraccessories-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Acefouraccessories Rate Limits
  slug: acefouraccessories-rate-limits
scopes:
- name: Acefouraccessories Scopes
  scope_count: 4
  slug: acefouraccessories-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 18.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.19.0
  scored_at: '2026-09-06'
security:
- kind: authentication
  name: Acefouraccessories Authentication
  slug: acefouraccessories-authentication
  summary_line: none/openIdConnect/oauth2 · 3 schemes
- kind: domain-security
  name: Acefouraccessories Domain Security
  slug: acefouraccessories-domain-security
  summary_line: TLSv1.3 · HSTS
slug: acefouraccessories
tags:
- Company
- Retail
- E-Commerce
- Consumer Goods
- Travel
- Luggage
- Direct to Consumer
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Shopify
- India
website: https://uppercase.co.in/
---
