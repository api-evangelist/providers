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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.1
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: River's GraphQL data API secured with OAuth 2.0 authorization-code + PKCE and OpenID Connect. Read scopes cover account balances, transactions, identity, and payment networks.
  name: River API
  slug: river-api
artifact_total: 6
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/river-financial-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://river.com
- group: operate
  title: ''
  type: Support
  url: https://river.com/support
- group: start
  title: ''
  type: SignUp
  url: https://river.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://river.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://river.com/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/riverfinancial
- group: operate
  title: ''
  type: StatusPage
  url: https://status.river.com
- group: auth
  title: ''
  type: Compliance
  url: https://river.com/security
- group: auth
  title: ''
  type: Security
  url: https://river.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/river-financial-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/river-financial-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/river-financial-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/river-financial-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/river-financial-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/river-financial-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/river-financial-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/river-financial-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/river-financial-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/river-financial-llms.txt
created: '2026-07-17'
description: 'River Financial Inc. (river.com) is a regulated U.S.-based Bitcoin brokerage and bank for long-term investors, operating under NMLS ID #1906809. Customers can buy, sell, send, and receive bitcoin, get paid in bitcoin via direct deposit, and earn interest on cash balances paid in bitcoin. River holds 100% of customer bitcoin in full-reserve multisig cold storage, publishes monthly third-party Proof of Reserves attestations, and provides FDIC insurance on cash up to $250,000 through partner bank Lead Bank. River exposes a GraphQL data API at https://river.com/api secured by an OAuth 2.0 authorization-code + PKCE flow with OpenID Connect discovery (balances, transactions, identity, and payment network read scopes). Surfaced as a polychain portfolio company and enriched from River''s public well-known, OIDC, and security surfaces.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/river-financial.png
layout: provider
mcp_servers:
- description: ''
  name: River Financial MCP Server
  slug: river-financial-mcp-server
modified: '2026-07-21'
name: River Financial
nav: Providers
network: true
overview: 'River Financial publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bitcoin Services, Cryptocurrency, Financial-Services, and Banking.


  River Financial''s developer surface includes support, signup flow, authentication, and 17 more developer resources.'
random_paper: 18
scopes:
- name: River Financial Scopes
  scope_count: 6
  slug: river-financial-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: thin
  composite: 31.8
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 31.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 67.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: River Financial Authentication
  slug: river-financial-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: River Financial Domain Security
  slug: river-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: River Financial Vulnerability Disclosure
  slug: river-financial-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: river-financial
tags:
- Company
- Bitcoin Services
- Cryptocurrency
- Financial-Services
- Banking
- Authentication
website: https://river.com
---
