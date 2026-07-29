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
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://seedlegals.com
- group: commercial
  title: ''
  type: Pricing
  url: https://seedlegals.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://seedlegals.com/resources/
- group: operate
  title: ''
  type: Support
  url: https://seedlegals.com/us/talk-to-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://seedlegals.com/us/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://seedlegals.com/us/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://app.seedlegals.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.seedlegals.com/login
- group: agent
  title: ''
  type: MCPServer
  url: mcp/seedlegals-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/seedlegals-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/seedlegals-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/seedlegals-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/seedlegals-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/seedlegals-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seedlegals-domain-security.yml
created: '2026-07-17'
description: SeedLegals is a legal-technology platform that helps startups, founders and investors handle their company legals end to end — from incorporation and cap table management through fundraising (SEIS/EIS, SAFEs, priced rounds, agile funding top-ups), share options and team agreements, to R&D tax credit claims and ongoing compliance. Trusted by 60,000+ startups and investors across the UK, France and the US, it replaces traditional law-firm workflows with guided, self-serve document generation plus expert support. SeedLegals does not publish a public REST/OpenAPI developer program, but it operates a hosted, OAuth-protected Model Context Protocol (MCP) server at api.seedlegals.com/mcp and a FusionAuth-based OpenID Connect identity provider, both discoverable via standard OAuth/OIDC well-known metadata.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/seedlegals.png
layout: provider
mcp_servers:
- description: ''
  name: SeedLegals MCP Server
  slug: seedlegals-mcp-server
modified: '2026-07-21'
name: SeedLegals
nav: Providers
network: true
overview: 'SeedLegals is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business Applications, Legal Tech, Startups, and Fundraising.


  SeedLegals'' developer surface includes pricing, engineering blog, support, signup flow, authentication, and 10 more developer resources.'
random_paper: 77
scopes:
- name: Seedlegals Scopes
  scope_count: 7
  slug: seedlegals-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: emerging
  composite: 22.5
  delta: 1.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 20.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Seedlegals Authentication
  slug: seedlegals-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Seedlegals Domain Security
  slug: seedlegals-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: seedlegals
tags:
- Company
- Business Applications
- Legal Tech
- Startups
- Fundraising
- Cap Table
- Equity
- Compliance
- MCP
- OpenID Connect
website: https://seedlegals.com
---
