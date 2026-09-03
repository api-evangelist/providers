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
    error_semantics: documented
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
  score: 16.4
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: The agent-facing commerce surface for the UrbanStems store, implementing the Universal Commerce Protocol (dev.ucp.shopping) over MCP. Thirteen tools cover catalog search and lookup, product detail, ca
  name: UrbanStems Commerce MCP API
  slug: urbanstems-commerce-mcp-api
- description: The read-only storefront JSON endpoints UrbanStems documents for agents in its own /llms.txt and /agents.md — product JSON at /products/{handle}.json, collection product listings at /collections/{hand
  name: UrbanStems Storefront JSON API
  slug: urbanstems-storefront-json-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/urbanstems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://urbanstems.com/
- group: docs
  title: ''
  type: Documentation
  url: https://urbanstems.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://help.urbanstems.com/en-US
- group: company
  title: ''
  type: Blog
  url: https://urbanstems.com/blogs/news
- group: company
  title: ''
  type: BlogRSS
  url: https://urbanstems.com/blogs/news.atom
- group: start
  title: ''
  type: SignUp
  url: https://urbanstems.com/account/register
- group: start
  title: ''
  type: Login
  url: https://urbanstems.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://urbanstems.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://urbanstems.com/policies/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/urbanstems
- group: agent
  title: ''
  type: MCPServer
  url: mcp/urbanstems-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/urbanstems-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/urbanstems-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/urbanstems-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/urbanstems-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/urbanstems-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/urbanstems-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/urbanstems-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/urbanstems-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/urbanstems-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/urbanstems-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/urbanstems-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/urbanstems-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/urbanstems-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/urbanstems-packages.yml
created: '2026-09-02'
description: 'UrbanStems is a direct-to-consumer flower and gifting company founded on Valentine''s Day 2014 in Washington, DC, selling modern bouquets, plants, gifts and centerpieces with same-day delivery in major US cities and next-day delivery nationwide, sourced through a vertically integrated supply chain that buys direct from Rainforest Alliance Certified farms. Its storefront runs on Shopify at urbanstems.com, and the company exposes a genuine agent-facing commerce surface rather than a developer API program: a published /llms.txt and /agents.md, a /.well-known/ucp merchant profile implementing the Universal Commerce Protocol (UCP 2026-08-25), and a live unauthenticated Model Context Protocol endpoint offering thirteen catalog, cart, checkout and order tools that lets an agent search the catalog and drive a buyer-approved purchase end to end.'
image: https://urbanstems.com/cdn/shop/t/637/assets/organization-image_large.png?v=133620255960512887901788204824
layout: provider
mcp_servers:
- description: ''
  name: UrbanStems Model Context Protocol servers
  slug: urbanstems-model-context-protocol-servers
modified: '2026-09-02'
name: UrbanStems
nav: Providers
network: true
overview: 'UrbanStems publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, E-Commerce, Retail, and Flowers.


  UrbanStems'' developer surface includes documentation, support, engineering blog, signup flow, authentication, and 22 more developer resources.'
plans:
- name: Urbanstems Plans Pricing
  plan_count: 0
  slug: urbanstems-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Urbanstems Rate Limits
  slug: urbanstems-rate-limits
scopes:
- name: Urbanstems Scopes
  scope_count: 0
  slug: urbanstems-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 5.3
  previous_composite: 22.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: authentication
  name: Urbanstems Authentication
  slug: urbanstems-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Urbanstems Domain Security
  slug: urbanstems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: urbanstems
tags:
- Company
- Commerce
- E-Commerce
- Retail
- Flowers
- Gifting
- Agentic Commerce
- Universal Commerce Protocol
- Model Context Protocol
- Shopify
- Direct to Consumer
website: https://urbanstems.com/
---
