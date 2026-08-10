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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 32.4
  scored_at: '2026-08-10'
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
  name: chill-mcp.yml
  slug: chill-mcpyml
modified: '2026-07-18'
name: Chill
nav: Providers
network: true
overview: 'Chill is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wellness, Supplements, E-commerce, and Marketplace.


  Chill''s developer surface includes documentation, authentication, engineering blog, support, and 12 more developer resources.'
random_paper: 60
scopes:
- name: Chill Scopes
  scope_count: 4
  slug: chill-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 26.7
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 26.7
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
  schema_version: 0.9.1
  scored_at: '2026-08-10'
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
- E-commerce
- Marketplace
- Health
- Agentic Commerce
- Shopify
- Retail
- MCP
website: https://chill.com
---
