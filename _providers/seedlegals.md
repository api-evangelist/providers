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
- description: Hosted Model Context Protocol server operated by SeedLegals at https://api.seedlegals.com/mcp. Discovered via RFC 8414 OAuth Authorization Server Metadata and RFC 9728 OAuth Protected Resource Metadat
  name: SeedLegals MCP Server
  slug: seedlegals-mcp-server
modified: '2026-07-21'
name: SeedLegals
nav: Providers
network: true
overview: 'SeedLegals is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business Applications, Legal Tech, Startups, and Fundraising.


  SeedLegals'' developer surface includes pricing, engineering blog, support, signup flow, authentication, and 10 more developer resources.'
random_paper: 20
scopes:
- name: Seedlegals Scopes
  scope_count: 7
  slug: seedlegals-scopes
  summary_line: 7 scopes · authorizationCode
screenshot: https://raw.githubusercontent.com/api-evangelist/seedlegals/refs/heads/main/screenshots/seedlegals-2026-09-02T154736.png
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
