---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
api_count: 2
apis:
- baseURL: https://thepicklr.com/wp-json
  baseurl_source: declared
  description: The public read surface of thepicklr.com, served by WordPress core and the site's plugins. Anonymous GET returns the franchise's own published content — 157 club location records, 53 pages, 23 blog po
  name: The Picklr WordPress REST API
  slug: the-picklr-wordpress-rest-api
- description: 'Three Model Context Protocol endpoints registered under the mcp REST namespace on thepicklr.com, exposed by the Novamira WordPress plugin (v1.11.4). The canonical one, /wp-json/mcp/novamira-oauth, is '
  name: The Picklr MCP Server
  slug: the-picklr-mcp-server
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-picklr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thepicklr.com/
- group: company
  title: ''
  type: Blog
  url: https://thepicklr.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://thepicklr.com/membership-and-pricing/
- group: operate
  title: ''
  type: HelpCenter
  url: https://thepicklr.com/membership-faqs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thepicklr.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thepicklr.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/the-picklr-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/the-picklr-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/the-picklr-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-picklr-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/the-picklr-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/the-picklr-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/the-picklr-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/the-picklr-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/the-picklr-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/the-picklr-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/the-picklr-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/the-picklr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/the-picklr-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-30'
description: 'The Picklr is the largest indoor pickleball club franchise in North America, founded in 2021 in Utah by Jorge Barragan and Austin Wood and franchising since March 2023. It operates membership-based indoor facilities offering unlimited court reservations, open play, adult and junior coaching academies, leagues, tournaments and corporate events, with a single membership valid at every club nationwide. The company publishes no developer programme and sells no API product. It does, however, serve a genuine machine-readable surface from its own domain: a public WordPress REST API exposing 157 club locations plus pages, posts, press and events; a published llms.txt; and three live Model Context Protocol endpoints advertised through RFC 8414 and RFC 9728 discovery documents and gated by an OAuth 2.1 authorization server with PKCE and dynamic client registration. Court booking, membership billing and reservations run on PlayByPoint, a third-party platform, and are outside any Picklr-owned
  contract.'
image: https://thepicklr.com/wp-content/uploads/2022/12/logo.svg
layout: provider
mcp_servers:
- description: thepicklr.com serves live, remotely reachable Model Context Protocol endpoints. They are exposed by the Novamira WordPress plugin (v1.11.4) through the WordPress MCP adapter, and the site advertises t
  name: The Picklr MCP Server
  slug: the-picklr-mcp-server
modified: '2026-08-30'
name: The Picklr
nav: Providers
network: true
overview: 'The Picklr publishes 1 API on the [APIs.io](https://apis.io/) network: WordPress REST API. Tagged areas include Company, Sports, Pickleball, Fitness, and Franchising.


  The Picklr''s developer surface includes engineering blog, pricing, authentication, and 18 more developer resources.'
plans:
- name: The Picklr Plans Pricing
  plan_count: 6
  slug: the-picklr-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: The Picklr Rate Limits
  slug: the-picklr-rate-limits
scopes:
- name: The Picklr Scopes
  scope_count: 0
  slug: the-picklr-scopes
  summary_line: OAuth 2.0 · no documented scopes
screenshot: https://raw.githubusercontent.com/api-evangelist/the-picklr/refs/heads/main/screenshots/the-picklr-2026-09-02T163406.png
security:
- kind: authentication
  name: The Picklr Authentication
  slug: the-picklr-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: The Picklr Domain Security
  slug: the-picklr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: the-picklr
tags:
- Company
- Sports
- Pickleball
- Fitness
- Franchising
- Recreation
- Health and Wellness
- Consumer
- Content Management
- MCP
website: https://thepicklr.com/
---
