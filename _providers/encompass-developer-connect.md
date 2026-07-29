---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Encompass Developer Connect Agentic Access
  operation_count: 6
  slug: encompass-developer-connect-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 3
apis:
- description: OAuth 2.0 token operations for issuing and revoking access tokens against Encompass Developer Connect. Supports user impersonation, ISV partner API user, and federated SAML SSO grant flows.
  name: Encompass Developer Connect Authentication API
  slug: encompass-developer-connect-authentication-api
- description: Operations for searching and filtering Encompass loan pipelines, including saved pipeline views and ad-hoc cursor-based queries across the loan portfolio.
  name: Encompass Developer Connect Loan Pipeline API
  slug: encompass-developer-connect-loan-pipeline-api
- description: Operations for retrieving, creating, updating, and deleting Encompass loan files and the rich loan field data model used across the mortgage origination lifecycle.
  name: Encompass Developer Connect Loans API
  slug: encompass-developer-connect-loans-api
artifact_total: 11
collections:
- collection_type: open
  name: Encompass Developer Connect API
  slug: open-encompass-developer-connect
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/encompass-developer-connect-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/encompass-developer-connect-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/encompass-developer-connect-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/encompass-developer-connect-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ICEMortgageTechnology
- group: company
  title: ''
  type: Website
  url: https://developer.icemortgagetechnology.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.icemortgagetechnology.com/developer-connect/docs/welcome
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.icemortgagetechnology.com/developer-connect/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developer.icemortgagetechnology.com/developer-connect/docs/authentication-and-authorization
- group: operate
  title: ''
  type: Forums
  url: https://developer.icemortgagetechnology.com/developer-connect/docs/developer-forum
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developer.icemortgagetechnology.com/developer-connect/docs/release-notes
- group: commercial
  title: ''
  type: Pricing
  url: https://www.icemortgagetechnology.com/encompass
- group: company
  title: ''
  type: Blog
  url: https://developer.icemortgagetechnology.com/developer-connect/docs/blogs
created: '2025-02-21'
description: Encompass Developer Connect is the ICE Mortgage Technology REST API platform that allows developers to configure, customize, and administer loan information and resources programmatically. It covers loan manufacturing, loan pipeline, product and pricing, compliance, documents and eFolder, loan data extracts, and loan folders. Access is authenticated via OAuth 2.0 with support for user impersonation, ISV partner API users, and federated SAML SSO.
finops:
- name: Encompass Developer Connect Finops
  service_category: API
  slug: encompass-developer-connect-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/encompass-developer-connect.png
layout: provider
modified: '2026-05-19'
name: Encompass Developer Connect
nav: Providers
network: true
overview: 'Encompass Developer Connect publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Loan Pipeline API, and Loans API. Tagged areas include Encompass, ICE Mortgage Technology, Loan Origination, Lending, and Mortgage.


  Encompass Developer Connect''s developer surface includes authentication, documentation, getting-started guide, release notes, pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Encompass Developer Connect Plans Pricing
  plan_count: 3
  slug: encompass-developer-connect-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Encompass Developer Connect Rate Limits
  slug: encompass-developer-connect-rate-limits
scopes:
- name: Encompass Developer Connect Scopes
  scope_count: 2
  slug: encompass-developer-connect-scopes
  summary_line: 2 scopes · password/clientCredentials
score:
  band: developing
  composite: 46.0
  delta: -2.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.0
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/encompass-developer-connect/refs/heads/main/screenshots/encompass-developer-connect-2026-06-20T180652.png
security:
- kind: authentication
  name: Encompass Developer Connect Authentication
  slug: encompass-developer-connect-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Encompass Developer Connect Domain Security
  slug: encompass-developer-connect-domain-security
  summary_line: TLSv1.3 · DMARC
slug: encompass-developer-connect
tags:
- Encompass
- ICE Mortgage Technology
- Loan Origination
- Lending
- Mortgage
- REST API
website: https://developer.icemortgagetechnology.com/
---
