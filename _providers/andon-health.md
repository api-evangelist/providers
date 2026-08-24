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
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.8
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: OAuth 2.0-authorized REST API that lets registered third-party applications read a consenting iHealth user's connected-device data (blood pressure and user-profile resources confirmed live). Developer
  name: iHealth Open API V2
  slug: ihealth-open-api-v2
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/andon-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ihealthlabs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ihealthlabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ihealthlabs.com/
- group: start
  title: ''
  type: SignUp
  url: https://developer.ihealthlabs.com/
- group: operate
  title: ''
  type: Support
  url: https://ihealthlabs.com/pages/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ihealthlabs.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ihealthlabs.com/policies/terms-of-service
- group: auth
  title: ''
  type: Authentication
  url: authentication/andon-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/andon-health-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/andon-health-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/andon-health-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/andon-health-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/andon-health-llms.txt
created: '2026-07-17'
description: Andon Health Co., Ltd. is a Tianjin, China-based medical device manufacturer, best known globally through its iHealth brand and its US subsidiary iHealth Labs Inc (founded 2010). The company designs connected consumer health hardware — wireless blood pressure monitors, smart glucose monitors, pulse oximeters, body-composition scales, infrared thermometers, and at-home rapid antigen tests (COVID-19, flu, RSV) — paired with the iHealth mobile apps and the iHealth Cloud. For developers, Andon Health/iHealth publishes the iHealth Open API V2, an OAuth 2.0-authorized REST API on api.ihealthlabs.com that lets third-party applications read a consenting user's device measurements (blood pressure and user profile resources are confirmed). The corporate andonhealth.com domain is currently parked/for-sale; the live surfaces are the ihealthlabs.com storefront, cloud.ihealthlabs.com, and the iHealth Developer Portal at developer.ihealthlabs.com.
image: https://ihealthlabs.com/cdn/shop/files/iHealth_logo.png
layout: provider
mcp_servers:
- description: ''
  name: Andon Health MCP Server
  slug: andon-health-mcp-server
modified: '2026-07-17'
name: Andon Health
nav: Providers
network: true
overview: 'Andon Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Devices, Digital Health, and Remote Patient Monitoring.


  Andon Health''s developer surface includes documentation, signup flow, support, authentication, and 10 more developer resources.'
random_paper: 6
scopes:
- name: Andon Health Scopes
  scope_count: 0
  slug: andon-health-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.4
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 22.4
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/andon-health/refs/heads/main/screenshots/andon-health-2026-07-25T200224.png
security:
- kind: authentication
  name: Andon Health Authentication
  slug: andon-health-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Andon Health Domain Security
  slug: andon-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: andon-health
tags:
- Company
- Healthcare
- Medical Devices
- Digital Health
- Remote Patient Monitoring
- Connected Health
- IoT
- Wearables
website: https://ihealthlabs.com/
---
