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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.7
  scored_at: '2026-09-03'
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
- description: Official hosted/remote MCP server for Connect The Dots. Lets any MCP-compatible AI client (Claude, Cursor) query your relationship graph — find warm paths to a person or company, identify decision-mak
  name: Connect The Dots
  slug: connect-the-dots
modified: '2026-07-18'
name: Connect The Dots
nav: Providers
network: true
overview: 'Connect The Dots publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Relationship Intelligence, Sales, Warm Introductions, and Network Graph.


  Connect The Dots'' developer surface includes authentication, API reference, documentation, pricing, engineering blog, support, signup flow, and 16 more developer resources.'
random_paper: 0
scopes:
- name: Ctd Scopes
  scope_count: 0
  slug: ctd-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 27.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
