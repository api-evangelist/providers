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
    agent_skills: false
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
  score: 20.3
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The agent-driven commerce surface exposed on the aventon.com Shopify storefront via the Universal Commerce Protocol (ucp.dev). An MCP endpoint offers catalog search, cart, checkout, discount, fulfillm
  name: Aventon Agent Commerce (UCP / MCP)
  slug: aventon-agent-commerce-ucp-mcp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://aventon.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aventon.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aventon.com/policies/terms-of-service
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aventon-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aventon-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aventon-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aventon-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aventon-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aventon-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aventon-domain-security.yml
created: '2026-07-17'
description: 'Aventon is a consumer electric bicycle (e-bike) manufacturer headquartered in Brea, California. Founded in 2012 and originally known for fixed-gear and track bikes, the company pivoted to electric bikes and is now one of the larger direct-to-consumer e-bike brands in the United States, with a lineup that spans commuter, fat-tire, lightweight, folding, cargo, and mountain e-bikes sold online and through a dealer network. Aventon operates no traditional public developer API of its own, but its Shopify-powered storefront at aventon.com natively exposes agent-facing commerce surfaces: a published /llms.txt, Shopify Customer Account OpenID Connect discovery, and a live Universal Commerce Protocol (UCP) MCP endpoint for agent-driven catalog search, cart, and checkout.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aventon.png
layout: provider
mcp_servers:
- description: ''
  name: Aventon MCP Server
  slug: aventon-mcp-server
modified: '2026-07-18'
name: Aventon
nav: Providers
network: true
overview: 'Aventon publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Electric Bikes, E-Commerce, and Retail.


  Aventon''s developer surface includes authentication and 9 more developer resources.'
random_paper: 7
scopes:
- name: Aventon Scopes
  scope_count: 4
  slug: aventon-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 16.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aventon/refs/heads/main/screenshots/aventon-2026-08-07T162023.png
security:
- kind: authentication
  name: Aventon Authentication
  slug: aventon-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Aventon Domain Security
  slug: aventon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aventon
tags:
- Company
- Consumer
- Electric Bikes
- E-Commerce
- Retail
- Agent Commerce
- Shopify
- Universal Commerce Protocol
website: https://aventon.com
---
