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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Shopify-hosted Universal Commerce Protocol shopping service exposed over MCP for agent-driven catalog search, cart, and buyer-approved checkout on the Pair Eyewear storefront.
  name: Pair Eyewear Agent Commerce (UCP/MCP)
  slug: pair-eyewear-agent-commerce-ucpmcp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://paireyewear.com
- group: docs
  title: ''
  type: Documentation
  url: https://paireyewear.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://paireyewear.com/pages/help-center
- group: company
  title: ''
  type: Blog
  url: https://paireyewear.com/blogs/news
- group: start
  title: ''
  type: SignUp
  url: https://paireyewear.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paireyewear.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paireyewear.com/policies/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pair-eyewear-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pair-eyewear-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pair-eyewear-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pair-eyewear-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pair-eyewear-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pair-eyewear-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pair-eyewear-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pair-eyewear-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Pair Eyewear is a direct-to-consumer eyewear brand known for its modular, magnetic Top Frames system: customers pick a base optical or sunglasses frame and swap interchangeable magnetic top frames in hundreds of patterns and licensed collaborations (Disney, Marvel, MLB, and more). Prescription and blue-light lenses are made and hand-assembled in California, with frames starting around $80, free shipping and 30-day returns, and a Pair+ membership. The paireyewear.com storefront runs on Shopify and exposes an agent-native commerce surface — a published agents.md and llms.txt, Shopify Customer Accounts OpenID Connect, and a live Universal Commerce Protocol (UCP) MCP endpoint for agent-driven catalog search, cart, and buyer-approved checkout.'
image: https://paireyewear.com/cdn/shop/files/PAIR_SEO-Image.jpg
layout: provider
mcp_servers:
- description: ''
  name: Pair Eyewear MCP Server
  slug: pair-eyewear-mcp-server
modified: '2026-07-20'
name: Pair Eyewear
nav: Providers
network: true
overview: 'Pair Eyewear publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Eyewear, E-Commerce, and Retail.


  Pair Eyewear''s developer surface includes documentation, support, engineering blog, signup flow, authentication, and 11 more developer resources.'
random_paper: 9
scopes:
- name: Pair Eyewear Scopes
  scope_count: 4
  slug: pair-eyewear-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 23.8
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
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 23.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pair-eyewear/refs/heads/main/screenshots/pair-eyewear-2026-08-07T191314.png
security:
- kind: authentication
  name: Pair Eyewear Authentication
  slug: pair-eyewear-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Pair Eyewear Domain Security
  slug: pair-eyewear-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pair-eyewear
tags:
- Company
- Consumer
- Eyewear
- E-Commerce
- Retail
- Shopify
- Direct to Consumer
- Agent Commerce
- MCP
- UCP
website: https://paireyewear.com
---
