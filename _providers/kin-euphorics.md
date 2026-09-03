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
    agentic_access: true
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
  score: 27.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The Kin Euphorics Shopify storefront agent-commerce surface. Its UCP discovery document (/.well-known/ucp) advertises a Universal Commerce Protocol shopping service over MCP transport, supporting cata
  name: Kin Euphorics Storefront (UCP / MCP)
  slug: kin-euphorics-storefront
artifact_total: 5
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.kineuphorics.com
- group: start
  title: ''
  type: Portal
  url: https://www.kineuphorics.com
- group: start
  title: ''
  type: Login
  url: https://account.kineuphorics.com
- group: start
  title: ''
  type: SignUp
  url: https://account.kineuphorics.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kineuphorics.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kineuphorics.com/policies/privacy-policy
- group: agent
  title: ''
  type: AgenticAccess
  url: https://www.kineuphorics.com/agents.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kin-euphorics-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kin-euphorics-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/kin-euphorics-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/kin-euphorics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kin-euphorics-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kin-euphorics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kin-euphorics-llms.txt
created: '2026-07-17'
description: 'Kin Euphorics is a non-alcoholic functional beverage company that makes "euphorics" — botanical drinks blending adaptogens, nootropics, and botanics formulated to lift mood, ease stress, and offer a social alternative to alcohol. Co-founded by Jen Batchelor and Bella Hadid, the brand sells ready-to-drink and mixable products such as Kin Spritz, Dream Light, Lightwave, and High Rhode direct to consumers through a Shopify storefront. That storefront exposes a modern agent-commerce surface: a UCP (Universal Commerce Protocol) discovery document advertising an MCP shopping endpoint for catalog search, cart, and checkout, alongside Shopify customer-account OpenID Connect for authentication and Google Pay / Shop Pay payment handlers.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kin-euphorics.png
layout: provider
mcp_servers:
- description: ''
  name: UCP / MCP Shopping Server
  slug: ucp-mcp-shopping-server
modified: '2026-07-19'
name: Kin Euphorics
nav: Providers
network: true
overview: 'Kin Euphorics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Beverages, Non-Alcoholic, Functional Beverage, and Adaptogens.


  Kin Euphorics'' developer surface includes developer portal, signup flow, authentication, and 11 more developer resources.'
random_paper: 1
scopes:
- name: Kin Euphorics Scopes
  scope_count: 4
  slug: kin-euphorics-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.6
  provenance:
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kin-euphorics/refs/heads/main/screenshots/kin-euphorics-2026-08-07T171224.png
security:
- kind: authentication
  name: Kin Euphorics Authentication
  slug: kin-euphorics-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Kin Euphorics Domain Security
  slug: kin-euphorics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kin-euphorics
tags:
- Company
- Beverages
- Non-Alcoholic
- Functional Beverage
- Adaptogens
- Nootropics
- Consumer Packaged Goods
- E-Commerce
- Shopify
- Direct to Consumer
- Agentic Commerce
- UCP
- MCP
website: https://www.kineuphorics.com
---
