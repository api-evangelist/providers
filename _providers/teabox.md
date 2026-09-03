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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'Agent-driven commerce surface for the Teabox Shopify store, implementing the Universal Commerce Protocol (UCP) over a hosted MCP endpoint. Supports catalog search/lookup, cart, checkout, fulfillment, '
  name: Teabox Agent Commerce (UCP)
  slug: teabox-agent-commerce-ucp
artifact_total: 5
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/teabox-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/teabox-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/teabox-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/teabox-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/teabox-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teabox-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.teabox.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.teabox.com/policies/terms-of-service
- group: company
  title: ''
  type: Website
  url: https://www.teabox.com
created: '2026-07-17'
description: 'Teabox is a premium loose-leaf tea brand and direct-to-consumer e-commerce company backed by Accel. It sources fresh Darjeeling, Assam, Nilgiri and other Indian teas direct from gardens and ships them globally through its online store. The storefront runs on Shopify, which exposes an agent-commerce surface built on the Universal Commerce Protocol (UCP): a hosted shopping MCP endpoint, a machine-readable llms.txt / agents.md, and OpenID Connect authentication via the Shopify Customer Account API (including a customer-account MCP scope). Buyer checkout always requires explicit human approval. This profile was surfaced as an Accel portfolio company and enriched from Teabox''s public agent-facing surfaces.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/teabox.png
layout: provider
mcp_servers:
- description: ''
  name: Teabox MCP Server
  slug: teabox-mcp-server
modified: '2026-07-21'
name: Teabox
nav: Providers
network: true
overview: 'Teabox publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Tea, Food and Beverage, and E-Commerce.


  Teabox''s developer surface includes authentication and 8 more developer resources.'
random_paper: 13
scopes:
- name: Teabox Scopes
  scope_count: 4
  slug: teabox-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.2
  provenance:
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/teabox/refs/heads/main/screenshots/teabox-2026-09-02T162641.png
security:
- kind: authentication
  name: Teabox Authentication
  slug: teabox-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Teabox Domain Security
  slug: teabox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: teabox
tags:
- Company
- Consumer
- Tea
- Food and Beverage
- E-Commerce
- Retail
- Shopify
- Agent Commerce
website: https://www.teabox.com
---
