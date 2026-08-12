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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: The API surface behind Synergy, AccessFintech's post-trade collaboration network. The shipped web client calls a GraphQL endpoint at https://api.accessfintech.com/gql (operation name mirrored into the
  name: Synergy Platform API
  slug: synergy-platform-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.accessfintech.com/
- group: company
  title: ''
  type: Blog
  url: https://www.accessfintech.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.accessfintech.com/contact/
- group: start
  title: ''
  type: Login
  url: https://login.accessfintech.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.accessfintech.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/accessfintech
- group: auth
  title: ''
  type: Authentication
  url: authentication/accessfintech-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/accessfintech-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/accessfintech-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/accessfintech-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/accessfintech-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/accessfintech-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accessfintech-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accessfintech-domain-security.yml
coverage:
  checked: '2026-08-06'
  detail: 'The Synergy API is real and reachable — the shipped web client calls GraphQL at https://api.accessfintech.com/gql — but AccessFintech publishes no developer site at all: api.accessfintech.com answers every unknown path with the same 4700-byte React shell, /api/docs returns a bare 401, and anonymous GraphQL introspection is refused with a 403 at the CloudFront edge, so the contract is readable only with an onboarded member''s session.'
  evidence:
  - status: 403
    url: https://api.accessfintech.com/gql
  - status: 401
    url: https://api.accessfintech.com/api/docs
  - status: 403
    url: https://api.accessfintech.com/openapi.json
  - status: 404
    url: https://www.accessfintech.com/developers/
  - status: 200
    url: https://login.accessfintech.com/.well-known/openid-configuration
  reason: customer-only-docs
  state: gated
created: '2026-08-06'
description: 'AccessFintech operates Synergy, a post-trade data and workflow network for capital markets that connects buy-side firms, broker-dealers, custodians, hedge funds, order management systems and vendors onto a shared view of trade, settlement and collateral data. The platform normalizes fragmented data across securities, derivatives and alternatives, detects breaks and exceptions across counterparties, and lets the parties to a trade resolve them collaboratively on a single record instead of by email and reconciliation files. AccessFintech describes Synergy as API-first, with bi-directional integrations, ingestion of JSON, XML, CSV and delimited text over push or pull, and Snowflake-native data sharing on AWS. The API surface is not self-serve: the Synergy application and its GraphQL and REST endpoints sit behind an Okta-backed customer login at login.accessfintech.com, and no public developer portal, reference or machine-readable specification is published.'
image: https://www.accessfintech.com/wp-content/uploads/2026/05/favicon.png
layout: provider
modified: '2026-08-06'
name: AccessFintech
nav: Providers
network: true
overview: 'AccessFintech publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Capital Markets, Post-Trade, and Settlement.


  AccessFintech''s developer surface includes engineering blog, support, authentication, and 11 more developer resources.'
random_paper: 87
scopes:
- name: Accessfintech Scopes
  scope_count: 7
  slug: accessfintech-scopes
  summary_line: 7 scopes · authorizationCode/implicit/deviceCode
score:
  band: emerging
  composite: 19.1
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 19.1
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/accessfintech/refs/heads/main/screenshots/accessfintech-2026-08-07T160758.png
security:
- kind: authentication
  name: Accessfintech Authentication
  slug: accessfintech-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Accessfintech Domain Security
  slug: accessfintech-domain-security
  summary_line: TLSv1.3 · DMARC
slug: accessfintech
tags:
- Company
- Financial Services
- Capital Markets
- Post-Trade
- Settlement
- Data Networks
- Reconciliation
- Fintech
- GraphQL
website: https://www.accessfintech.com/
---
