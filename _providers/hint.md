---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: The agent-facing commerce surface of the drinkhint.com storefront. Discovery is published at https://www.drinkhint.com/.well-known/ucp (Universal Commerce Protocol merchant profile, versions 2026-04-0
  name: Hint Agentic Commerce (UCP / MCP)
  slug: hint-agentic-commerce-ucp-mcp
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.drinkhint.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.drinkhint.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://www.drinkhint.com/pages/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.drinkhint.com/blogs/news
- group: start
  title: ''
  type: SignUp
  url: https://www.drinkhint.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.drinkhint.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.drinkhint.com/policies/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hint-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hint-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hint-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hint-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hint-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hint-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/hint-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hint-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hint-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hint-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hint-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hint-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hint-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-22'
description: 'Hint Inc. is a San Francisco based beverage company founded in 2005 by Kara Goldin, known for fruit-infused unsweetened water sold in still, sparkling, caffeinated and kids formats across 25+ flavors. A large share of its business is direct-to-consumer through its own storefront at drinkhint.com, which runs on Shopify. Hint publishes no traditional developer program, SDKs or OpenAPI, but the storefront does expose a live, anonymous agent surface: an agents.md / llms.txt agent instruction document, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, and a Model Context Protocol endpoint at /api/ucp/mcp that answers tools/list with 13 real catalog, cart, checkout and order tools. Checkout explicitly requires contemporaneous human approval before payment.'
image: https://www.drinkhint.com/cdn/shop/files/Logo_Hint-Wordmark-Droplet-Secondary-2_Color.png?v=1762813167
layout: provider
mcp_servers:
- description: ''
  name: Hint Storefront Agentic Commerce MCP
  slug: hint-storefront-agentic-commerce-mcp
modified: '2026-08-22'
name: Hint
nav: Providers
network: true
overview: 'Hint publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Beverages, Consumer Packaged Goods, Ecommerce, and Direct to Consumer.


  Hint''s developer surface includes documentation, support, engineering blog, signup flow, authentication, and 17 more developer resources.'
plans:
- name: Hint Plans Pricing
  plan_count: 0
  slug: hint-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Hint Rate Limits
  slug: hint-rate-limits
scopes:
- name: Hint Scopes
  scope_count: 0
  slug: hint-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.9
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 0.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: authentication
  name: Hint Authentication
  slug: hint-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Hint Domain Security
  slug: hint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hint
tags:
- Company
- Beverages
- Consumer Packaged Goods
- Ecommerce
- Direct to Consumer
- Retail
- Agentic Commerce
- Model Context Protocol
- Universal Commerce Protocol
- Shopify
website: https://www.drinkhint.com/
---
