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
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.realscout.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://learn.realscout.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://support.realscout.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.realscout.com/
- group: start
  title: ''
  type: Login
  url: https://www.realscout.com/agents/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.realscout.com/terms-and-policies
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.realscout.com/terms-and-policies
- group: agent
  title: ''
  type: MCPServer
  url: mcp/realscout-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/realscout-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/realscout-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/realscout-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/realscout-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/realscout-llms.txt
created: '2026-07-17'
description: RealScout is a lead-nurture and collaborative home-search platform for real estate professionals — agents, teams, and brokerages — that turns an agent's existing database and local MLS inventory into a recurring source of transactions. It is CRM-agnostic and plugs into existing stacks (Follow Up Boss, Sierra, Salesforce, HubSpot) via native integrations, Zapier/Make, and direct API access on Enterprise plans. Core products include AI Search (natural-language-to-MLS-criteria), Scout Score (0–100 contact engagement scoring), Contact Enrichment, Search Links, and Auto-Nurture alerts. RealScout publishes an OAuth 2.1-protected, standards-compliant MCP server (api://realscout-admin-mcp) for agent/AI access. Backed by DCM Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/realscout.png
layout: provider
mcp_servers:
- description: ''
  name: realscout-mcp.yml
  slug: realscout-mcpyml
modified: '2026-07-20'
name: RealScout
nav: Providers
network: true
overview: 'RealScout is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Real Estate, PropTech, and Lead Nurture.


  RealScout''s developer surface includes pricing, support, engineering blog, authentication, and 9 more developer resources.'
random_paper: 18
scopes:
- name: Realscout Scopes
  scope_count: 1
  slug: realscout-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 19.9
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.9
  provenance:
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Realscout Authentication
  slug: realscout-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Realscout Domain Security
  slug: realscout-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: realscout
tags:
- Company
- Enterprise
- Real Estate
- PropTech
- Lead Nurture
- Home Search
- MLS
- MCP
- Artificial Intelligence
website: https://www.realscout.com/
---
