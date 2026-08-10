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
  score: 27.9
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Agent-driven commerce surface for the Molekule storefront implementing the Universal Commerce Protocol over MCP. Agents discover capabilities at /.well-known/ucp, then search the catalog, build a cart
  name: Molekule Agent Commerce (UCP / MCP)
  slug: molekule-agent-commerce-ucp-mcp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://molekule.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/molekule-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/molekule-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/molekule-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/molekule-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/molekule-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/molekule-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/molekule-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/molekule-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://molekule.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://molekule.com/policies/terms-of-service
created: '2026-07-17'
description: 'Molekule is a consumer air-quality hardware company that makes FDA-cleared HEPA air purifiers for homes and businesses. It sells direct-to-consumer through molekule.com, a Shopify-hosted storefront. While Molekule does not publish a traditional developer API, its store exposes a live agent-commerce surface: a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a Model Context Protocol (MCP) endpoint at /api/ucp/mcp for AI shopping agents, OpenID Connect buyer authentication via the Shopify Customer Account API, and published agent instructions at /agents.md and /llms.txt. This profile captures that machine-readable commerce surface for the API Evangelist network.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/molekule.png
layout: provider
mcp_servers:
- description: ''
  name: molekule-mcp.yml
  slug: molekule-mcpyml
modified: '2026-07-20'
name: Molekule
nav: Providers
network: true
overview: 'Molekule publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hardware, Air Quality, Consumer IoT, and E-Commerce.


  Molekule''s developer surface includes authentication and 11 more developer resources.'
random_paper: 50
scopes:
- name: Molekule Scopes
  scope_count: 4
  slug: molekule-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 19.6
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 19.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/molekule/refs/heads/main/screenshots/molekule-2026-08-07T184120.png
security:
- kind: authentication
  name: Molekule Authentication
  slug: molekule-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Molekule Domain Security
  slug: molekule-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: molekule
tags:
- Company
- Hardware
- Air Quality
- Consumer IoT
- E-Commerce
- Agent Commerce
- MCP
- Shopify
website: https://molekule.com
---
