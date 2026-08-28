---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Universal Commerce Protocol endpoint served from the Create Wellness storefront, exposed over the Model Context Protocol. Thirteen tools cover catalog search and lookup, cart create/read/update/ca
  name: Create Wellness UCP Commerce MCP
  slug: create-wellness-ucp-commerce-mcp
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/create-wellness-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trycreate.co
- group: docs
  title: ''
  type: Documentation
  url: https://trycreate.co/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/create-wellness-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/create-wellness-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/create-wellness-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/create-wellness-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/create-wellness-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/create-wellness-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/create-wellness-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/create-wellness-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/create-wellness-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/create-wellness-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: https://trycreate.co/pages/faq
- group: company
  title: ''
  type: BlogRSS
  url: https://trycreate.co/blogs/news.atom
- group: start
  title: ''
  type: Login
  url: https://trycreate.co/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trycreate.co/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trycreate.co/policies/privacy-policy
created: '2026-08-11'
description: 'Create Wellness is a New York based direct-to-consumer supplement brand, founded in 2022, that makes creatine monohydrate gummies and drink mixes — NSF Certified for Sport, vegan, gluten-free and non-GMO — sold through its own Shopify storefront at trycreate.co and through Amazon, Target, Walmart, GNC and The Vitamin Shoppe. It is not a software company and publishes no developer programme, but its storefront serves a live, anonymous agent-commerce surface: a Universal Commerce Protocol endpoint exposed over the Model Context Protocol at /api/ucp/mcp with thirteen catalog, cart, checkout and order tools, advertised from the store''s own robots.txt, llms.txt and agents.md, and governed by a stated human-approval-before-payment rule.'
image: https://cdn.shopify.com/s/files/1/0611/9204/4732/files/Create_Wellness_Logo.png?v=1733357143
layout: provider
mcp_servers:
- description: ''
  name: Create Wellness UCP Commerce MCP
  slug: create-wellness-ucp-commerce-mcp
modified: '2026-08-11'
name: Create Wellness
nav: Providers
network: true
overview: 'Create Wellness publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health and Wellness, Supplements, Consumer Products, and E-Commerce.


  Create Wellness'' developer surface includes documentation, authentication, support, and 16 more developer resources.'
plans:
- name: Create Wellness Plans Pricing
  plan_count: 0
  slug: create-wellness-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Create Wellness Rate Limits
  slug: create-wellness-rate-limits
scopes:
- name: Create Wellness Scopes
  scope_count: 0
  slug: create-wellness-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 26.0
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 26.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Create Wellness Authentication
  slug: create-wellness-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Create Wellness Domain Security
  slug: create-wellness-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: create-wellness
tags:
- Company
- Health and Wellness
- Supplements
- Consumer Products
- E-Commerce
- Direct to Consumer
- Agentic Commerce
- MCP
- Shopify
- Nutrition
website: https://trycreate.co
---
