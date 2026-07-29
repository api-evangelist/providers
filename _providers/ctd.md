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
  score: 23.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Simple REST API exposing the full Connect The Dots relationship graph — reachable people and companies, warm paths to a target (including natural-language and stage-filtered path search), recent job c
  name: CTD Paths API
  slug: ctd-paths-api
artifact_total: 7
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ctd-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ctd-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ctd-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ctd-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ctd-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ctd-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ctd-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/ctd-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ctd-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ctd-data-model.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ctd-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ctd-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/ctd-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ctd-domain-security.yml
- group: docs
  title: ''
  type: APIReference
  url: https://ctd.ai/integrations-api
- group: docs
  title: ''
  type: Documentation
  url: https://ctd.ai/integrations-api
- group: commercial
  title: ''
  type: Pricing
  url: https://ctd.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://ctd.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://ctd.ai/faqs
- group: start
  title: ''
  type: SignUp
  url: https://app.ctd.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ctd.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ctd.ai/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://ctd.ai
created: '2026-07-17'
description: Connect The Dots (CTD) is a relationship intelligence platform that scores every relationship across a team's network — from real two-way email and LinkedIn activity — to surface the warmest introduction path to any person or company. It merges everyone's contacts into one deduplicated "Supergraph," routes intros through the best-connected colleague (including "ghost emails" sent on their behalf), tracks job changes, and activates the network for sales, recruiting, and VC/PE deal sourcing. Everything in the app is exposed through a simple two-header REST API and a hosted MCP server for AI clients like Claude and Cursor. Backed by Norwest Venture Partners.
image: https://ctd.ai/assets/images/og-default.png
layout: provider
mcp_servers:
- description: ''
  name: ctd-mcp.yml
  slug: ctd-mcpyml
modified: '2026-07-18'
name: Connect The Dots
nav: Providers
network: true
overview: 'Connect The Dots publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Relationship Intelligence, Sales, Warm Introductions, and Network Graph.


  Connect The Dots'' developer surface includes authentication, API reference, documentation, pricing, engineering blog, support, signup flow, and 16 more developer resources.'
random_paper: 78
scopes:
- name: Ctd Scopes
  scope_count: 0
  slug: ctd-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.9
  delta: 0.9
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 10.5
  previous_composite: 31.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ctd/refs/heads/main/screenshots/ctd-2026-07-25T210842.png
security:
- kind: authentication
  name: Ctd Authentication
  slug: ctd-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Ctd Domain Security
  slug: ctd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ctd Vulnerability Disclosure
  slug: ctd-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Ctd Trust Center
  slug: ctd-trust-center
  summary_line: SOC 2 Type II, GDPR, CCPA
slug: ctd
tags:
- Company
- Relationship Intelligence
- Sales
- Warm Introductions
- Network Graph
- CRM
- MCP
- Venture Capital
website: https://ctd.ai
---
