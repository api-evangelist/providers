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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Agent-driven commerce over the Universal Commerce Protocol (UCP) on the Nara Organics Shopify storefront — catalog search, cart, and buyer-approved checkout via a published MCP endpoint, plus an unaut
  name: Nara Organics Commerce (UCP)
  slug: nara-organics-commerce-ucp
artifact_total: 5
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nara-organics-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nara-organics-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nara-organics-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nara-organics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nara-organics-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nara-organics-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nara-organics-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nara-organics-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nara-organics-lifecycle.yml
- group: docs
  title: ''
  type: Documentation
  url: https://nara.com/agents.md
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nara.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nara.com/policies/terms-of-service
- group: company
  title: ''
  type: Website
  url: https://nara.com/
created: '2026-07-17'
description: 'Nara Organics is a direct-to-consumer organic infant-formula brand, surfaced as a portfolio company of Initialized Capital and profiled in the API Evangelist network. It is not a traditional API provider, but its Shopify storefront at nara.com exposes a modern agent-native commerce surface: a published Universal Commerce Protocol (UCP) MCP endpoint for agent-driven catalog search, cart, and buyer-approved checkout; a Shopify Customer Account OIDC provider; and /llms.txt + /agents.md agent instructions covering the read-only product surface and the Shop Pay flow. The company is currently managing a voluntary infant-formula recall communicated through its storefront.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nara-organics.png
layout: provider
mcp_servers:
- description: ''
  name: nara-organics-mcp.yml
  slug: nara-organics-mcpyml
modified: '2026-07-20'
name: Nara Organics
nav: Providers
network: true
overview: 'Nara Organics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Commerce, Retail, and Shopify.


  Nara Organics'' developer surface includes authentication, documentation, and 12 more developer resources.'
random_paper: 53
scopes:
- name: Nara Organics Scopes
  scope_count: 4
  slug: nara-organics-scopes
  summary_line: 4 scopes
score:
  band: emerging
  composite: 20.3
  delta: -0.1
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 20.4
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Nara Organics Authentication
  slug: nara-organics-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Nara Organics Domain Security
  slug: nara-organics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nara-organics
tags:
- Company
- Consumer
- Commerce
- Retail
- Shopify
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Infant Formula
website: https://nara.com/
---
