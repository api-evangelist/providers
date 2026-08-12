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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: Authenticated flood forecasting and impact data delivered as GIS-native OGC WMS/WFS feeds, secured by AWS Cognito OAuth2/OIDC. Access is provisioned per customer; there is no public self-service devel
  name: FloodMapp Flood Intelligence API
  slug: floodmapp-flood-intelligence-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.floodmapp.com
- group: operate
  title: ''
  type: Support
  url: https://www.floodmapp.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.floodmapp.com/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.floodmapp.com/general-4
- group: start
  title: ''
  type: Login
  url: https://login.floodmapp.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/floodmapp-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/floodmapp-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/floodmapp-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/floodmapp-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/floodmapp-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/floodmapp-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/floodmapp-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/floodmapp-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/floodmapp-domain-security.yml
created: '2026-07-17'
description: FloodMapp is a flood intelligence technology company that provides real-time, impact-based flood forecasting and mapping for emergency managers, government agencies, and critical infrastructure operators. Its AI-driven hydrology and hydraulics models deliver street-level (1-meter resolution) flood impact forecasts, updated hourly, 24/7/365, using live rainfall, river and coastal gauge networks, and terrain data. Capabilities ship as three products — ForeCast (predictive), NowCast (real-time), and PostCast (post-event) — packaged into PREPARE and RESPOND solutions. FloodMapp delivers its data as GIS-native live feeds (OGC WMS/WFS layers) that integrate directly into Esri ArcGIS, ArcGIS Online, Google, Mapbox, and QGIS. The authenticated API surface at api.floodmapp.com is protected by AWS Cognito OAuth2/OIDC. FloodMapp is SOC 2 Type II certified and serves customers across the United States and Australia.
image: https://www.floodmapp.com
layout: provider
mcp_servers:
- description: ''
  name: floodmapp-mcp.yml
  slug: floodmapp-mcpyml
modified: '2026-07-19'
name: FloodMapp
nav: Providers
network: true
overview: 'FloodMapp publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Flood Intelligence, Flood Forecasting, Geospatial, and GIS.


  FloodMapp''s developer surface includes support, engineering blog, authentication, and 11 more developer resources.'
random_paper: 34
scopes:
- name: Floodmapp Scopes
  scope_count: 1
  slug: floodmapp-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 22.2
  delta: -1.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 23.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/floodmapp/refs/heads/main/screenshots/floodmapp-2026-07-25T214818.png
security:
- kind: authentication
  name: Floodmapp Authentication
  slug: floodmapp-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Floodmapp Domain Security
  slug: floodmapp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Floodmapp Trust Center
  slug: floodmapp-trust-center
  summary_line: SOC 2 Type II
slug: floodmapp
tags:
- Company
- Flood Intelligence
- Flood Forecasting
- Geospatial
- GIS
- Emergency Management
- Climate Risk
- Machine Learning
- Hydrology
website: https://www.floodmapp.com
---
