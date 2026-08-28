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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The storefront's agent-facing commerce surface, implementing the Universal Commerce Protocol (UCP) over a hosted MCP endpoint for catalog search, cart, checkout, fulfillment and order tracking. Checko
  name: Barn & Willow Agentic Commerce (UCP)
  slug: barn-willow-agentic-commerce-ucp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://barnandwillow.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/barn-and-willow-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/barn-and-willow-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/barn-and-willow-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/barn-and-willow-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/barn-and-willow-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/barn-and-willow-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/barn-and-willow-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://barnandwillow.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://barnandwillow.com/policies/terms-of-service
created: '2026-07-17'
description: 'Barn & Willow is a direct-to-consumer home furnishings brand specializing in made-to-measure window treatments — custom drapery, curtains, roman shades and blinds in natural fabrics such as linen, cotton and velvet. The company sells online at barnandwillow.com, a Shopify-hosted storefront, offering free fabric swatches, measuring guides and design consultations. Surfaced as a portfolio company of 500 Global and added to the API Evangelist network, the storefront exposes a real agentic-commerce surface: a Universal Commerce Protocol (UCP) merchant profile and hosted MCP endpoint for agent-driven shopping, Shopify Customer Account OAuth 2.0 / OpenID Connect authentication, and an llms.txt agent-instructions document.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/barn-and-willow.png
layout: provider
mcp_servers:
- description: ''
  name: Barn & Willow MCP Server
  slug: barn-willow-mcp-server
modified: '2026-07-18'
name: Barn & Willow
nav: Providers
network: true
overview: 'Barn & Willow publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Home Furnishings, and Window Treatments.


  Barn & Willow''s developer surface includes authentication and 9 more developer resources.'
random_paper: 16
scopes:
- name: Barn And Willow Scopes
  scope_count: 4
  slug: barn-and-willow-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 17.5
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 17.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/barn-and-willow/refs/heads/main/screenshots/barn-and-willow-2026-08-07T162148.png
security:
- kind: authentication
  name: Barn And Willow Authentication
  slug: barn-and-willow-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Barn And Willow Domain Security
  slug: barn-and-willow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: barn-and-willow
tags:
- Company
- E-Commerce
- Retail
- Home Furnishings
- Window Treatments
- Agentic Commerce
- Shopify
- Direct to Consumer
website: https://barnandwillow.com
---
