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
    agent_skills: true
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
  score: 23.9
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: 'Agent-driven commerce surface for the Away storefront implementing the Universal Commerce Protocol (dev.ucp.shopping) over an MCP endpoint, with catalog search, cart, checkout, fulfillment, discount, '
  name: Away Agent Commerce (UCP / MCP)
  slug: away-agent-commerce-ucp-mcp
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/away-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.awaytravel.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/away-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/away-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/away-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/away-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/away-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/away-conformance.yml
- group: start
  title: ''
  type: Login
  url: https://accounts.awaytravel.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.awaytravel.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.awaytravel.com/policies/terms-of-service
- group: other
  title: ''
  type: RefundPolicy
  url: https://www.awaytravel.com/policies/refund-policy
created: '2026-07-17'
description: 'Away (Away: Built for modern travel) is a direct-to-consumer travel and lifestyle brand that designs and sells thoughtfully engineered suitcases, bags, and travel accessories built for modern travel. Its storefront at awaytravel.com runs on Shopify and is agent-commerce ready: it publishes an /llms.txt and /agents.md with agent instructions, implements the Universal Commerce Protocol (UCP, ucp.dev) service dev.ucp.shopping over a Model Context Protocol (MCP) endpoint for buyer-approved catalog search, cart, and checkout, and exposes Shopify Customer Account OpenID Connect authentication. Surfaced in the API Evangelist network as a portfolio company of Accel, Battery Ventures, and Forerunner Ventures; enriched from its live public discovery surfaces.'
image: http://www.awaytravel.com/cdn/shop/files/12EVER25_Ecomm-HPH-Desktop-1_9936be52-b9e2-4e19-985f-78aa1d091f3a.jpg?v=1771448528
layout: provider
mcp_servers:
- description: Away's storefront exposes an agent-commerce MCP endpoint implementing the Universal Commerce Protocol (UCP, ucp.dev) service dev.ucp.shopping. Agents discover it via /.well-known/ucp and /llms.txt. Ch
  name: Away MCP Server
  slug: away-mcp-server
modified: '2026-07-18'
name: Away
nav: Providers
network: true
overview: 'Away publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Travel, Retail, and E-Commerce.


  Away''s developer surface includes authentication and 12 more developer resources.'
random_paper: 14
scopes:
- name: Away Scopes
  scope_count: 4
  slug: away-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 19.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/away/refs/heads/main/screenshots/away-2026-08-07T162033.png
security:
- kind: authentication
  name: Away Authentication
  slug: away-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Away Domain Security
  slug: away-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: away
tags:
- Company
- Consumer
- Travel
- Retail
- E-Commerce
- Luggage
- Agent Commerce
- Shopify
- MCP
website: http://www.awaytravel.com
---
