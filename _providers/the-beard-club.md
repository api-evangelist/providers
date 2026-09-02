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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Native Shopify Universal Commerce Protocol (UCP 2026-04-08) shopping service, exposed as a Model Context Protocol endpoint for agent-driven commerce — catalog search, cart, checkout, fulfillment, disc
  name: The Beard Club UCP Shopping MCP
  slug: the-beard-club-ucp-shopping-mcp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://thebeardclub.com
- group: docs
  title: ''
  type: Documentation
  url: https://thebeardclub.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/the-beard-club-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/the-beard-club-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/the-beard-club-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-beard-club-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/the-beard-club-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/the-beard-club-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/the-beard-club-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-beard-club-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thebeardclub.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thebeardclub.com/policies/terms-of-service
created: '2026-07-17'
description: 'The Beard Club is a men''s grooming and beard-care brand selling beard oils, balms, washes, aftershave, grooming kits, trimmers, and subscription grooming boxes through its Shopify-powered online store at thebeardclub.com. Beyond the consumer storefront, the store is agent-commerce ready: it implements the Universal Commerce Protocol (UCP 2026-04-08) with a native Model Context Protocol (MCP) endpoint at /api/ucp/mcp, a machine-readable /llms.txt and /agents.md, UCP service discovery at /.well-known/ucp, Shopify Customer Account OpenID Connect authentication, and read-only product and collection JSON endpoints — so AI shopping assistants can search the catalog, build carts, and complete buyer-approved checkouts programmatically.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-beard-club.png
layout: provider
mcp_servers:
- description: ''
  name: The Beard Club MCP Server
  slug: the-beard-club-mcp-server
modified: '2026-07-21'
name: The Beard Club
nav: Providers
network: true
overview: 'The Beard Club publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Men''s Grooming, and Consumer Goods.


  The Beard Club''s developer surface includes documentation, authentication, and 11 more developer resources.'
random_paper: 20
scopes:
- name: The Beard Club Scopes
  scope_count: 4
  slug: the-beard-club-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 18.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: The Beard Club Authentication
  slug: the-beard-club-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: The Beard Club Domain Security
  slug: the-beard-club-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: the-beard-club
tags:
- Company
- E-Commerce
- Retail
- Men's Grooming
- Consumer Goods
- Shopify
- Agent Commerce
- UCP
- MCP
- Subscription
website: https://thebeardclub.com
---
