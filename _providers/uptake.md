---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
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
  score: 2.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Uptake's customer-provisioned REST API. The gateway is live at api.uptake.com (AWS API Gateway behind Cloudflare) and answers every anonymous request with HTTP 403 ForbiddenException; a sibling gatewa
  name: Uptake Platform API
  slug: uptake-platform-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uptake-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://uptake.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/uptake_stock/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uptake
- group: start
  title: ''
  type: Login
  url: https://fleet.uptake.com/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/uptake-tech
- group: operate
  title: ''
  type: Support
  url: https://uptake.com/legal/support-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uptake.com/legal/lmaster-subscription-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uptake.com/privacy-notice/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/uptake-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uptake-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/uptake-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uptake-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/uptake-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uptake-llms.txt
coverage:
  checked: '2026-08-05'
  detail: Uptake's former developer portal at developer.uptake.com now returns nginx 404 and its user guide and release notes are Google Sites that 302 to a Google account sign-in, so the only anonymous machine-readable surface left on the estate is the Okta OIDC discovery document at start.uptake.com; the live gateway at api.uptake.com answers 403 ForbiddenException on every path with no WWW-Authenticate challenge, and integration partners are told to hand their token to an Uptake account representative rather than read a spec.
  evidence:
  - status: 404
    url: https://developer.uptake.com/
  - status: 403
    url: https://api.uptake.com/openapi.json
  - status: 302
    url: https://sites.google.com/uptake.com/uptake-user-guide/home
  - status: 200
    url: https://start.uptake.com/.well-known/openid-configuration
  reason: customer-only-docs
  state: gated
created: '2026-08-05'
description: Uptake Technologies is a Chicago-based industrial AI and predictive-maintenance software company founded in 2014 by Eric Lefkofsky and Brad Keywell. Its SaaS platform ingests telematics, sensor, fluid-analysis and work-order data from heavy commercial fleets and industrial assets, then applies machine-learning failure models — backed by an Asset Strategy Library of roughly 800 equipment types and tens of thousands of failure modes acquired with Asset Performance Technologies in 2018 — to predict component failure before it happens. Products include Uptake Fleet and Radar (predictive maintenance alerts), Compass (work-order data cleansing), Fusion (operational-technology data to cloud) and Scout (rules-based alerting), delivered through the fleet.uptake.com web application, a Geotab Marketplace add-in, and a customer-provisioned REST API gateway at api.uptake.com. Bosch announced its acquisition of Uptake in March 2026.
image: https://avatars.githubusercontent.com/u/26656201?v=4
layout: provider
modified: '2026-08-05'
name: Uptake
nav: Providers
network: true
overview: 'Uptake publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Industrial AI, Predictive Maintenance, Asset Performance Management, and Fleet Management.


  Uptake''s developer surface includes engineering blog, support, authentication, and 12 more developer resources.'
random_paper: 20
scopes:
- name: Uptake Scopes
  scope_count: 0
  slug: uptake-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 11.8
    commercial_clarity: 11.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 14.6
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Uptake Authentication
  slug: uptake-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Uptake Domain Security
  slug: uptake-domain-security
  summary_line: TLSv1.3 · DMARC
slug: uptake
tags:
- Company
- Industrial AI
- Predictive Maintenance
- Asset Performance Management
- Fleet Management
- Telematics
- Machine-Learning
- Industrial IoT
website: https://uptake.com/
---
