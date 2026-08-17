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
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: REST API on Autodesk Platform Services (APS) exposing BuildingConnected preconstruction data — opportunities, bid packages, and users — versioned under /v2 and secured with Autodesk OAuth 2.0.
  name: BuildingConnected API
  slug: buildingconnected-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/buildingconnected-trust-center.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aps.autodesk.com/
- group: company
  title: ''
  type: Website
  url: https://www.buildingconnected.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://aps.autodesk.com/en/docs/buildingconnected/v2/developers_guide/basics/
- group: operate
  title: ''
  type: Support
  url: https://aps.autodesk.com/en/support/get-help
- group: company
  title: ''
  type: Blog
  url: https://aps.autodesk.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/autodesk-platform-services
- group: commercial
  title: ''
  type: Pricing
  url: https://www.buildingconnected.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.buildingconnected.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.autodesk.com/company/legal-notices-trademarks/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.autodesk.com/company/legal-notices-trademarks/privacy-statement
- group: operate
  title: ''
  type: StatusPage
  url: https://health.autodesk.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/buildingconnected-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/buildingconnected-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/buildingconnected-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/buildingconnected-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/buildingconnected-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/buildingconnected-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/buildingconnected-llms.txt
created: '2026-07-17'
description: BuildingConnected is a preconstruction and bid-management platform for the commercial construction industry, now part of Autodesk Construction Cloud. Its products — Bid Board Pro for general contractors and subcontractors, and TradeTapp for subcontractor risk qualification — help teams send, track, and manage bid invitations across the largest construction network in North America. Autodesk acquired BuildingConnected in 2018, and its data is accessible programmatically through the BuildingConnected API on Autodesk Platform Services (APS), a REST API secured with Autodesk's OAuth 2.0 (two-legged and three-legged) authentication and versioned under a /v2 URI path.
image: https://construction.autodesk.com/products/buildingconnected/
layout: provider
modified: '2026-07-18'
name: Buildingconnected
nav: Providers
network: true
overview: 'Buildingconnected publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Preconstruction, Bid Management, and Construction Technology.


  Buildingconnected''s developer surface includes getting-started guide, support, engineering blog, pricing, authentication, and 14 more developer resources.'
random_paper: 5
scopes:
- name: Buildingconnected Scopes
  scope_count: 16
  slug: buildingconnected-scopes
  summary_line: 16 scopes
score:
  band: thin
  composite: 29.8
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 37.0
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 29.8
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/buildingconnected/refs/heads/main/screenshots/buildingconnected-2026-07-25T204053.png
security:
- kind: authentication
  name: Buildingconnected Authentication
  slug: buildingconnected-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Buildingconnected Domain Security
  slug: buildingconnected-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Buildingconnected Trust Center
  slug: buildingconnected-trust-center
  summary_line: GDPR
slug: buildingconnected
tags:
- Company
- Construction
- Preconstruction
- Bid Management
- Construction Technology
- Autodesk
- Autodesk Platform Services
- Subcontractor Management
website: https://www.buildingconnected.com/
---
