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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Agent-facing commerce endpoint for the Petstore.com Shopify store, implemented via the Universal Commerce Protocol (UCP) over MCP — catalog search, cart, and buyer-approved checkout.
  name: Petstore.com Commerce (UCP/MCP)
  slug: petstorecom-commerce-ucpmcp
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/petstorecom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://petstore.com
- group: docs
  title: ''
  type: Documentation
  url: https://petstore.com/agents.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/petstorecom-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/petstorecom-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/petstorecom-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/petstorecom-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/petstorecom-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/petstorecom-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/petstorecom-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/petstorecom-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/petstorecom-agentic-checkout.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://petstore.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://petstore.com/policies/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://petstore.com/pages/contact
- group: company
  title: ''
  type: Blog
  url: https://petstore.com/blogs/news
- group: start
  title: ''
  type: SignUp
  url: https://petstore.com/account/register
- group: start
  title: ''
  type: Login
  url: https://petstore.com/account/login
created: '2026-07-17'
description: Petstore.com is an online pet-supplies store built on Shopify that exposes a first-class agent commerce surface. Alongside the human storefront it implements the Universal Commerce Protocol (UCP) over the Model Context Protocol (MCP) at /api/ucp/mcp, publishes a /.well-known/ucp merchant profile and a /agents.md (mirrored as /llms.txt) describing how AI agents can search the catalog, build a cart, and drive a buyer-approved checkout. Buyer identity uses Shopify Customer Account OpenID Connect, payment is handled by Google Pay and Shopify card handlers, and every checkout requires contemporaneous human approval. Read-only storefront browsing (products, collections, search, sitemap) needs no auth. Added to the API Evangelist network as a Battery Ventures portfolio lead; enriched from the store's live agent-facing surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/petstorecom.png
layout: provider
mcp_servers:
- description: Petstore.com's agent-facing commerce endpoint, implemented via the Universal Commerce Protocol (UCP) over MCP. Lets agents search the catalog, build a cart, and drive a buyer-approved checkout on this
  name: Petstore.com MCP Server
  slug: petstorecom-mcp-server
modified: '2026-07-20'
name: Petstore.com
nav: Providers
network: true
overview: 'Petstore.com publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, E-Commerce, Retail, and Pet Supplies.


  Petstore.com''s developer surface includes documentation, authentication, support, engineering blog, signup flow, and 13 more developer resources.'
random_paper: 8
scopes:
- name: Petstorecom Scopes
  scope_count: 4
  slug: petstorecom-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 11
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
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 22.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/petstorecom/refs/heads/main/screenshots/petstorecom-2026-09-02T151120.png
security:
- kind: authentication
  name: Petstorecom Authentication
  slug: petstorecom-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Petstorecom Domain Security
  slug: petstorecom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: petstorecom
tags:
- Company
- Commerce
- E-Commerce
- Retail
- Pet Supplies
- Agentic Commerce
- UCP
- MCP
- Shopify
website: https://petstore.com
---
