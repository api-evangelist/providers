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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: 'Agent-facing commerce API for the Beekeeper''s Naturals storefront, exposed over the Model Context Protocol as the Universal Commerce Protocol (UCP) Shopping service. The endpoint is advertised by the '
  name: Beekeeper's Naturals UCP Shopping MCP API
  slug: beekeepers-naturals-ucp-shopping-mcp
- description: 'Read-only JSON representations of the Beekeeper''s Naturals storefront catalog, documented by the store''s own agent instructions: product detail at /products/{handle}.json and collection listings at /c'
  name: Beekeeper's Naturals Storefront Product JSON
  slug: beekeepers-naturals-storefront-json
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.beekeepersnaturals.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.beekeepersnaturals.com/agents.md
- group: docs
  title: ''
  type: Documentation
  url: https://www.beekeepersnaturals.com/agents.md
- group: docs
  title: ''
  type: APIReference
  url: https://ucp.dev/2026-04-08/services/shopping/mcp.openrpc.json
- group: start
  title: ''
  type: GettingStarted
  url: https://www.beekeepersnaturals.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://help.beekeepersnaturals.com/en-US
- group: company
  title: ''
  type: Blog
  url: https://www.beekeepersnaturals.com/blogs/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.beekeepersnaturals.com/collections/all
- group: start
  title: ''
  type: SignUp
  url: https://www.beekeepersnaturals.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beekeepersnaturals.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beekeepersnaturals.com/policies/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/beekeepers-naturals-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/beekeepers-naturals-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/beekeepers-naturals-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/beekeepers-naturals-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/beekeepers-naturals-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/beekeepers-naturals-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/beekeepers-naturals-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/beekeepers-naturals-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/beekeepers-naturals-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beekeepers-naturals-domain-security.yml
created: '2026-08-02'
description: 'Beekeeper''s Naturals is a direct-to-consumer bee-derived wellness and supplement brand founded in 2017 by Carly Stein Kremer, selling propolis throat sprays, B.LXR royal-jelly brain fuel, superfood honey, bee pollen and kids'' immunity products through beekeepersnaturals.com and retail partners. The company has no traditional developer program, but its Shopify-hosted storefront publishes a genuine machine-readable agent surface: a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a live MCP endpoint at /api/ucp/mcp implementing the UCP Shopping service (catalog search, cart, checkout, order), an agent instruction document at /agents.md mirrored to /llms.txt, an agentic-discovery sitemap, OIDC/OAuth discovery for Shopify customer accounts, and read-only storefront product/collection JSON endpoints.'
image: https://www.beekeepersnaturals.com/cdn/shop/files/BestSeller-1200x630.webp?v=1776441784
layout: provider
mcp_servers:
- description: ''
  name: beekeepers-naturals-mcp.yml
  slug: beekeepers-naturals-mcpyml
modified: '2026-08-02'
name: Beekeeper's Naturals
nav: Providers
network: true
overview: 'Beekeeper''s Naturals publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Consumer Packaged Goods, and Health and Wellness.


  Beekeeper''s Naturals'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 15 more developer resources.'
random_paper: 114
scopes:
- name: Beekeepers Naturals Scopes
  scope_count: 4
  slug: beekeepers-naturals-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 30.9
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 30.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beekeepers-naturals/refs/heads/main/screenshots/beekeepers-naturals-2026-08-07T162251.png
security:
- kind: authentication
  name: Beekeepers Naturals Authentication
  slug: beekeepers-naturals-authentication
  summary_line: openIdConnect/oauth2/none · 3 schemes
- kind: domain-security
  name: Beekeepers Naturals Domain Security
  slug: beekeepers-naturals-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beekeepers-naturals
tags:
- Company
- Retail
- E-Commerce
- Consumer Packaged Goods
- Health and Wellness
- Supplements
- Shopify
- Agentic Commerce
- Universal Commerce Protocol
- Model Context Protocol
website: https://www.beekeepersnaturals.com/
---
