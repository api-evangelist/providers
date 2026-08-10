---
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
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: A Model Context Protocol server published on garten's own host at https://tv.garten.co/mcp, serving the garten TV wellness-video property. The endpoint is provided by the Uscreen streaming platform th
  name: garten TV MCP Server
  slug: garten-tv-mcp-server
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://garten.co/
- group: company
  title: ''
  type: About
  url: https://garten.co/about/
- group: company
  title: ''
  type: Blog
  url: https://garten.co/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://garten.co/feed/
- group: operate
  title: ''
  type: Support
  url: https://garten.co/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://solutionsdesk.zendesk.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://garten.co/get-started/
- group: start
  title: ''
  type: Login
  url: https://client.garten.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://garten.co/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://garten.co/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://garten.co/careers/
- group: company
  title: ''
  type: Press
  url: https://garten.co/press/
- group: company
  title: ''
  type: Partners
  url: https://garten.co/become-partner/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getgarten
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/getgarten
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/garten_stock/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/garten-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/garten-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/garten-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/garten-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/garten-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/garten-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/garten-llms.txt
created: '2026-08-04'
description: 'garten (styled lowercase; formerly Oh My Green) is a workplace food and wellbeing company founded in 2014 by Michael Heinrich and backed by Y Combinator, headquartered in the San Francisco Bay Area. It runs turn-key office micro-kitchens and pantries (garten Kitchen), self-serve micro-markets with cashless checkout kiosks (garten Market), corporate catering and cafe management (garten Catering), and virtual and on-site wellbeing programming (garten Wellbeing, plus the garten TV streaming property), serving employers including Google, Nike, Ford and Autodesk across roughly twenty US metros. garten was acquired by the chef-driven catering platform HUNGRY in 2025. garten publishes no public developer portal, API reference, SDK or machine-readable REST contract: its client ordering surface at client.garten.co / api.garten.co is a credentialed Spree/Solidus commerce application whose API rejects anonymous calls with "You must specify an API key." The one genuinely public, machine-readable
  agent surface sits on its Uscreen-powered streaming property garten TV (tv.garten.co), which serves a Model Context Protocol server at /mcp guarded by a full OAuth 2.1 stack: RFC 9728 protected-resource metadata, RFC 8414 authorization-server metadata, PKCE S256, RFC 7591 dynamic client registration, RFC 8707 resource indicators, and seven named read/write scopes.'
image: https://garten.co/wp-content/uploads/2020/04/Garten-Logo-Navy-Tight.svg
layout: provider
mcp_servers:
- description: ''
  name: garten-mcp.yml
  slug: garten-mcpyml
modified: '2026-08-04'
name: Garten
nav: Providers
network: true
overview: 'Garten publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food Service, Corporate Wellness, Workplace, and Catering.


  Garten''s developer surface includes engineering blog, support, signup flow, authentication, and 19 more developer resources.'
random_paper: 61
scopes:
- name: Garten Scopes
  scope_count: 7
  slug: garten-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: emerging
  composite: 21.1
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 21.1
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/garten/refs/heads/main/screenshots/garten-2026-08-07T165538.png
security:
- kind: authentication
  name: Garten Authentication
  slug: garten-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Garten Domain Security
  slug: garten-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: garten
tags:
- Company
- Food Service
- Corporate Wellness
- Workplace
- Catering
- Employee Benefits
- Micro Market
- Facilities Management
- Hospitality
- Streaming Video
- MCP
website: https://garten.co/
---
