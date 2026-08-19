---
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
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.2
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Hosted Model Context Protocol server operated by Acrisure at https://api.acrisure.com/v1/mcp. Production and live, protected by Microsoft Entra ID via an authorization-code + PKCE flow carrying the si
  name: Acrisure MCP Server
  slug: acrisure-mcp-server
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/acrisure-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acrisure-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.acrisure.com/
- group: company
  title: ''
  type: About
  url: https://www.acrisure.com/about-acrisure
- group: company
  title: ''
  type: Blog
  url: https://www.acrisure.com/blog
- group: company
  title: ''
  type: News
  url: https://www.acrisure.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.acrisure.com/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://customer.acrisure.com/portal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acrisure.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acrisure.com/privacy
- group: company
  title: ''
  type: Careers
  url: https://www.acrisure.com/careers
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/acrisure_stock/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/acrisure-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/acrisure-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.acrisure.com/.well-known/security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/acrisure-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/acrisure-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/acrisure-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/acrisure-conformance.yml
coverage:
  checked: '2026-08-06'
  detail: Acrisure runs a live OAuth-protected MCP server at api.acrisure.com/v1/mcp — proven by an application-level 403 on tools/list against a control sibling path that 404s — but publishes no OpenAPI, no tool list and no documentation for it anywhere, and its llms.txt and /ai/*.json endpoints still serve the unshipped Sitecore XM Cloud demo fixture for a fictional "Skate Park" skate-brand wholesaler instead of anything about Acrisure.
  evidence:
  - status: 403
    url: https://api.acrisure.com/v1/mcp
  - status: 404
    url: https://api.acrisure.com/v1/mcpZZZ
  - status: 200
    url: https://api.acrisure.com/.well-known/oauth-authorization-server
  - status: 404
    url: https://api.acrisure.com/.well-known/oauth-protected-resource
  - status: 200
    url: https://www.acrisure.com/llms.txt
  - status: 200
    url: https://www.acrisure.com/ai/summary.json
  - status: 404
    url: https://api.acrisure.com/v1/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-08-06'
description: Acrisure is a global fintech and insurance brokerage headquartered in Grand Rapids, Michigan, founded in 2005 and grown from $38M to roughly $5B in revenue with more than 19,000 colleagues across 500+ offices in over 20 countries. It sells commercial and personal insurance, employee benefits, payroll and HR, reinsurance, surety bonds, trade credit, mortgages, managed IT and cybersecurity through a partner-agency model rather than a developer platform. Acrisure publishes no developer portal, no API reference and no machine-readable specification of any kind, but it does operate an undocumented, OAuth-protected Model Context Protocol server at api.acrisure.com/v1/mcp behind Microsoft Entra ID — discoverable only from the `mcp_user` scope in its RFC 8414 authorization-server metadata.
image: https://edge.sitecorecloud.io/acrisurellc1-acrisure-prod-0dbe/media/Project/Acrisure/Acrisure-Site/Master-Site/Acrisure-Logo/acrisure-logo-large.png
layout: provider
mcp_servers:
- description: ''
  name: acrisure-mcp.yml
  slug: acrisure-mcpyml
modified: '2026-08-06'
name: Acrisure
nav: Providers
network: true
overview: 'Acrisure publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include insurance, insurance-brokerage, fintech, employee-benefits, and payroll-hr.


  Acrisure''s developer surface includes engineering blog, product news, support, signup flow, authentication, and 14 more developer resources.'
random_paper: 117
scopes:
- name: Acrisure Scopes
  scope_count: 2
  slug: acrisure-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 26.4
  delta: -4.6
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 5.3
  previous_composite: 31.0
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 72.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acrisure/refs/heads/main/screenshots/acrisure-2026-08-07T160845.png
security:
- kind: authentication
  name: Acrisure Authentication
  slug: acrisure-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Acrisure Domain Security
  slug: acrisure-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Acrisure Vulnerability Disclosure
  slug: acrisure-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: acrisure
tags:
- insurance
- insurance-brokerage
- fintech
- employee-benefits
- payroll-hr
- reinsurance
- risk-management
- cybersecurity
- mortgage
- surety-bonds
- mcp
- oauth2
website: https://www.acrisure.com/
---
