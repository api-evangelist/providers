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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.1
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.wrapbook.com/
- group: company
  title: ''
  type: Blog
  url: https://www.wrapbook.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.wrapbook.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.wrapbook.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.wrapbook.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wrapbook.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wrapbook.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wrapbook
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wrapbook-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wrapbook-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wrapbook-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wrapbook-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wrapbook-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/wrapbook-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wrapbook-domain-security.yml
created: '2026-07-17'
description: Wrapbook is an AI-powered production payroll and accounting platform for film, TV, and commercial production, combining crew onboarding, payroll, accounts payable, purchase orders, production accounting, and real-time cost reporting in one system. It integrates with accounting software including QuickBooks, Sage Intacct, Oracle NetSuite, and Acumatica, and imports budgets from Movie Magic, Hot Budget, and Showbiz. Wrapbook publishes no public developer API, but its production app exposes an RFC 8414 OAuth 2.0 authorization server with 21 read-only accounting, payroll, budget, and purchase-order scopes that power those integrations. Backed by a16z, Bessemer Venture Partners, and Uncork Capital.
image: https://avatars.githubusercontent.com/u/40865417
layout: provider
modified: '2026-07-21'
name: Wrapbook
nav: Providers
network: true
overview: 'Wrapbook is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Entertainment, Payroll, Production Accounting, and Accounts Payable.


  Wrapbook''s developer surface includes engineering blog, support, signup flow, authentication, changelog, and 10 more developer resources.'
random_paper: 8
scopes:
- name: Wrapbook Scopes
  scope_count: 21
  slug: wrapbook-scopes
  summary_line: 21 scopes · authorizationCode
score:
  band: emerging
  composite: 22.1
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 22.1
  provenance:
    conformance: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Wrapbook Authentication
  slug: wrapbook-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Wrapbook Domain Security
  slug: wrapbook-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wrapbook
tags:
- Company
- Entertainment
- Payroll
- Production Accounting
- Accounts Payable
- Film
- Television
- Fintech
website: https://www.wrapbook.com/
---
