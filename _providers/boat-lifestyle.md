---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.9
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Universal Commerce Protocol (UCP) shopping service boAt Lifestyle serves from its own storefront host over MCP. An anonymous JSON-RPC tools/list returns 13 tools covering catalog search and lookup
  name: boAt Lifestyle UCP Commerce MCP
  slug: boat-lifestyle-ucp-mcp
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boat-lifestyle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.boat-lifestyle.com/
- group: company
  title: ''
  type: Blog
  url: https://www.boat-lifestyle.com/blogs/blog
- group: operate
  title: ''
  type: Support
  url: https://www.boat-lifestyle.com/pages/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.boat-lifestyle.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boat-lifestyle.com/policies/privacy-policy
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/boat-lifestyle-stock
- group: agent
  title: ''
  type: WellKnown
  url: well-known/boat-lifestyle-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/boat-lifestyle-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/boat-lifestyle-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/boat-lifestyle-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/boat-lifestyle-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/boat-lifestyle-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/boat-lifestyle-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/boat-lifestyle-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/boat-lifestyle-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/boat-lifestyle-data-model.yml
created: '2026-08-08'
description: 'boAt (legal entity Imagine Marketing Limited) is an India-based consumer electronics brand founded in 2016 by Aman Gupta and Sameer Mehta, selling wireless earbuds, headphones, smartwatches, home audio and mobile accessories. Its direct-to-consumer storefront at boat-lifestyle.com runs on Shopify and exposes a real, anonymous agent commerce surface: a Universal Commerce Protocol (UCP 2026-04-08) merchant profile at /.well-known/ucp, a live MCP endpoint at /api/ucp/mcp serving 13 catalog, cart, checkout and order tools over JSON-RPC, published agent instructions at /agents.md and /llms.txt, and Shopify Customer Accounts OpenID Connect discovery. There is no first-party developer program, no OpenAPI, and no partner API portal — the machine-readable contract is the MCP tools/list manifest, which is platform-provided by Shopify rather than authored by boAt.'
image: https://www.boat-lifestyle.com/cdn/shop/files/profile-1_2e1d2124-ba4c-43f0-bb83-0e6ee038ff30.png?v=1681111976
layout: provider
mcp_servers:
- description: ''
  name: Boat Lifestyle MCP Server
  slug: boat-lifestyle-mcp-server
modified: '2026-08-08'
name: Boat Lifestyle
nav: Providers
network: true
overview: 'Boat Lifestyle publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Electronics, E-Commerce, Retail, and Audio.


  Boat Lifestyle''s developer surface includes engineering blog, support, authentication, and 15 more developer resources.'
random_paper: 16
scopes:
- name: Boat Lifestyle Scopes
  scope_count: 4
  slug: boat-lifestyle-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 19.5
  delta: 1.9
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 17.6
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Boat Lifestyle Authentication
  slug: boat-lifestyle-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Boat Lifestyle Domain Security
  slug: boat-lifestyle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boat-lifestyle
tags:
- Company
- Consumer Electronics
- E-Commerce
- Retail
- Audio
- Wearables
- Agent Commerce
- MCP
- Shopify
- India
website: https://www.boat-lifestyle.com/
---
