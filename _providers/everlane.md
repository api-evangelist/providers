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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'Agent-facing commerce surface for the Everlane storefront, hosted on Shopify: a Model Context Protocol (MCP) server for catalog search, cart, product details, and store-policy lookup, plus a Universal'
  name: Everlane Storefront (Shopify MCP / UCP)
  slug: everlane-storefront-shopify-mcp-ucp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://everlane.com
- group: operate
  title: ''
  type: Support
  url: https://support.everlane.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.everlane.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.everlane.com/policies/terms-of-service
- group: start
  title: ''
  type: SignUp
  url: https://account.everlane.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Everlane
- group: agent
  title: ''
  type: MCPServer
  url: mcp/everlane-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/everlane-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/everlane-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/everlane-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/everlane-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/everlane-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/everlane-domain-security.yml
created: '2026-07-17'
description: 'Everlane is a San Francisco-based direct-to-consumer apparel and footwear brand known for its "Radical Transparency" model — publishing factory sourcing, true costs, and markups on everyday wardrobe essentials. As an API Evangelist network entry, Everlane has no bespoke public developer program; its online store runs on Shopify and exposes an agent-facing commerce surface: a live Storefront MCP server at everlane.com/api/mcp (product search, cart, product details, and policy/FAQ lookup), a Universal Commerce Protocol (UCP) profile at /.well-known/ucp, a published /llms.txt of agent instructions, and Shopify Customer Account OIDC/OAuth2 authentication. Surfaced as a Slow Ventures portfolio company and enriched from its public agent, well-known, and authentication surfaces.'
image: https://www.everlane.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: everlane MCP Server
  slug: everlane-mcp-server
modified: '2026-07-19'
name: everlane
nav: Providers
network: true
overview: 'everlane publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Apparel, and Fashion.


  everlane''s developer surface includes support, signup flow, authentication, and 10 more developer resources.'
random_paper: 10
scopes:
- name: Everlane Scopes
  scope_count: 4
  slug: everlane-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 18.1
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/everlane/refs/heads/main/screenshots/everlane-2026-08-07T165037.png
security:
- kind: authentication
  name: Everlane Authentication
  slug: everlane-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Everlane Domain Security
  slug: everlane-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: everlane
tags:
- Company
- Retail
- E-Commerce
- Apparel
- Fashion
- Direct to Consumer
- Shopify
- Agentic Commerce
website: https://everlane.com
---
