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
    consent_identity: true
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
  score: 22.5
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Official hosted Model Context Protocol server for Rohlik online grocery. Search the catalog, manage a cart, discover recipes, track and repeat orders, manage shopping lists, and reach customer service
  name: Rohlik MCP Server
  slug: rohlik-mcp-server
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: http://rohlik.cz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rohlik.cz/mcp-docs
- group: docs
  title: ''
  type: Documentation
  url: https://rohlik.cz/mcp-docs
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rohlik-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rohlik-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/rohlik-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rohlik-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rohlik-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rohlik-lifecycle.yml
- group: operate
  title: ''
  type: Support
  url: https://www.rohlik.cz/stranka/kontakt
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.rohlik.cz/stranka/caste-dotazy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rohlik.cz/xtra
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rohlik.cz/stranka/vseobecne-obchodni-podminky
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rohlik.cz/stranka/zasady-zpracovani-osobnich-udaju
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rohlikgroup
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rohlik-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/rohlik-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rohlik-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rohlik-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.rohlik.cz/.well-known/security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rohlik-llms.txt
created: '2026-07-17'
description: Rohlik (Rohlik Group) is a European online grocery service founded in 2014 by Tomáš Čupr and headquartered in Prague, Czechia. It operates fast, same-day and sub-hour grocery delivery across several markets under local brands — rohlik.cz in Czechia, Knuspr in Germany, Gurkerl in Austria, Kifli in Hungary, and Rohlik in Romania — combining an owned fulfillment/logistics stack with a wide fresh and private-label assortment. On the developer side, Rohlik runs an official hosted Model Context Protocol (MCP) server that lets AI assistants search the catalog, build and manage a cart, discover recipes, track and repeat orders, and manage shopping lists on behalf of a signed-in customer, secured with OAuth 2.0 / OpenID Connect via identity.rohlik.cz. Rohlik is backed by Index Ventures and Partech.
image: https://cdn.rohlik.cz/images/company/rohlik-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: rohlik-mcp.yml
  slug: rohlik-mcpyml
modified: '2026-07-21'
name: Rohlik
nav: Providers
network: true
overview: 'Rohlik publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Grocery, E-commerce, and Delivery.


  Rohlik''s developer surface includes documentation, authentication, support, pricing, and 17 more developer resources.'
random_paper: 49
scopes:
- name: Rohlik Scopes
  scope_count: 3
  slug: rohlik-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: emerging
  composite: 26.8
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 26.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Rohlik Authentication
  slug: rohlik-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Rohlik Domain Security
  slug: rohlik-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Rohlik Vulnerability Disclosure
  slug: rohlik-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: rohlik
tags:
- Company
- Retail
- Grocery
- E-commerce
- Delivery
- Logistics
- MCP
- OAuth
- Europe
website: http://rohlik.cz
---
