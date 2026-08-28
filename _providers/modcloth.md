---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 21.2
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: Universal Commerce Protocol shopping service exposed over MCP — search the catalog, build a cart, and run a buyer-approved checkout.
  name: Modcloth UCP Agentic Commerce (MCP)
  slug: modcloth-ucp-agentic-commerce-mcp
- description: Read-only Shopify Storefront JSON for products, collections, and search — no authentication required.
  name: Modcloth Storefront JSON (read-only)
  slug: modcloth-storefront-json-read-only
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://modcloth.com
- group: docs
  title: ''
  type: Documentation
  url: https://modcloth.com/agents.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/modcloth-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/modcloth-agentic-shopping.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/modcloth-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/modcloth-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/modcloth-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/modcloth-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/modcloth-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/modcloth-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/modcloth-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/modcloth-domain-security.yml
- group: start
  title: ''
  type: Login
  url: https://account.modcloth.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://modcloth.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://modcloth.com/policies/privacy-policy
created: '2026-07-17'
description: 'Modcloth is a vintage-inspired, indie and retro women''s fashion retailer selling dresses, apparel, footwear, and accessories through its Shopify-hosted online store at modcloth.com. Surfaced as a portfolio company of Norwest Venture Partners, the store exposes a real agent-facing commerce surface: a Universal Commerce Protocol (UCP) shopping service over an MCP endpoint, Shopify customer-account OAuth 2.0 / OpenID Connect, published /llms.txt and /agents.md agent instructions, and read-only Shopify Storefront JSON for catalog and collections. Checkout requires contemporaneous buyer approval.'
image: https://modcloth.com/cdn/shop/files/ModCloth_Logo_1200x628_15dc462f-196f-49fb-a86d-79841942351e.jpg?v=1750463087
layout: provider
mcp_servers:
- description: ''
  name: Modcloth MCP Server
  slug: modcloth-mcp-server
modified: '2026-07-20'
name: Modcloth
nav: Providers
network: true
overview: 'Modcloth publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Fashion, and Apparel.


  Modcloth''s developer surface includes documentation, authentication, and 13 more developer resources.'
random_paper: 18
scopes:
- name: Modcloth Scopes
  scope_count: 4
  slug: modcloth-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 21.0
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.2
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 21.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/modcloth/refs/heads/main/screenshots/modcloth-2026-08-07T183919.png
security:
- kind: authentication
  name: Modcloth Authentication
  slug: modcloth-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Modcloth Domain Security
  slug: modcloth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: modcloth
tags:
- Company
- Retail
- E-Commerce
- Fashion
- Apparel
- Shopify
- Agentic Commerce
- MCP
website: https://modcloth.com
---
