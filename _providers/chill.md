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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Chill Agentic Access
  operation_count: 0
  slug: chill-agentic-access
  summary_line: 0 operations
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://chill.com
- group: docs
  title: ''
  type: Documentation
  url: https://chill.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chill-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/chill-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/chill-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chill-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/chill-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/chill-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/chill-conventions.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chill-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chill-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://chill.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://chill.com/pages/contact
- group: start
  title: ''
  type: Login
  url: https://chill.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chill.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chill.com/policies/privacy-policy
created: '2026-07-17'
description: 'Chill.com is a natural-supplements and wellness marketplace — a Shopify-hosted store selling premium supplements, skincare, functional beverages, and healthy alternatives aimed at helping people relax, unwind, and beat stress. The store is fully agent-native: it publishes an llms.txt agent guide and implements the Universal Commerce Protocol (UCP) over a live MCP endpoint, letting AI shopping agents search the catalog, build carts, and complete buyer-approved checkout. End-user authentication is Shopify Customer Accounts (OAuth 2.0 + OpenID Connect), and read-only catalog browsing requires no auth. Surfaced as a 500 Global portfolio company and enriched from its public agent-commerce surface.'
image: https://chill.com/cdn/shop/files/A_Marketplace_to_Help_You_Beat_Stress_and_Live_Better._Simple.png?v=1750163758
layout: provider
mcp_servers:
- description: ''
  name: Chill MCP Server
  slug: chill-mcp-server
modified: '2026-07-18'
name: Chill
nav: Providers
network: true
overview: 'Chill is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wellness, Supplements, E-Commerce, and Marketplace.


  Chill''s developer surface includes documentation, authentication, engineering blog, support, and 12 more developer resources.'
random_paper: 20
scopes:
- name: Chill Scopes
  scope_count: 4
  slug: chill-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 24.2
  provenance:
    agentic_access: first-party
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chill/refs/heads/main/screenshots/chill-2026-08-07T163311.png
security:
- kind: authentication
  name: Chill Authentication
  slug: chill-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Chill Domain Security
  slug: chill-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chill
tags:
- Company
- Wellness
- Supplements
- E-Commerce
- Marketplace
- Health
- Agentic Commerce
- Shopify
- Retail
- MCP
website: https://chill.com
---
