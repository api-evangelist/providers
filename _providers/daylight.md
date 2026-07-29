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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Daylight's partner/product API surface at api.daylight.ai, protected by OAuth2 / OpenID Connect (Bearer token, authorization server at auth.app.daylight.ai). Access is authenticated (returns 401 witho
  name: Daylight API
  slug: daylight-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://daylight.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.daylight.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.daylight.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.daylight.ai
- group: company
  title: ''
  type: Blog
  url: https://daylight.ai/blog
- group: operate
  title: ''
  type: Support
  url: mailto:contact@daylight.ai
- group: start
  title: ''
  type: SignUp
  url: https://app.daylight.ai/
- group: start
  title: ''
  type: Login
  url: https://app.daylight.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://daylight.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://daylight.ai/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/daylight-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/daylight-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/daylight-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/daylight-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/daylight-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/daylight-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/daylight-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/daylight-llms.txt
created: '2026-07-17'
description: Daylight (Daylight Security) is an AI-native Managed Detection and Response (MDR) provider delivering what it calls Managed Agentic Security Services (MASS) — combining agentic AI with elite human analysts to run security operations end-to-end, from real-time threat detection through Tier 1 triage, deep Tier 3 investigations, and full incident response, 24x7x365. The platform ingests signals across endpoints, cloud, and networks, learns each customer's business context (identity platforms, HR systems, even Slack), and connects into the customer stack (AWS, Google Cloud, Microsoft 365, Snowflake, Slack, Microsoft Teams). Daylight exposes a partner API at api.daylight.ai (OAuth2 / OIDC, Bearer) plus an OAuth-protected Model Context Protocol (MCP) server so security teams can connect investigations to AI assistants such as Claude and Cursor. Daylight is SOC 2 Type II certified and ISO 27001 compliant. Founded in 2024 by Hagai Shapira and Eldad Rudich; backed by Craft Ventures,
  Bain Capital Ventures, and Maple VC ($40M raised). Added to the API Evangelist network from VC-portfolio discovery.
image: https://cdn.prod.website-files.com/6854103d33b88163dcd9a2c7/69ea1501c915392df9b01d4c_new-thumbnail.jpg
layout: provider
mcp_servers:
- description: ''
  name: daylight-mcp.yml
  slug: daylight-mcpyml
modified: '2026-07-18'
name: Daylight
nav: Providers
network: true
overview: 'Daylight publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Managed Detection and Response, and MDR.


  Daylight''s developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, and 12 more developer resources.'
random_paper: 7
scopes:
- name: Daylight Scopes
  scope_count: 2
  slug: daylight-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: thin
  composite: 28.6
  delta: 0.9
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 27.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/daylight/refs/heads/main/screenshots/daylight-2026-07-25T211450.png
security:
- kind: authentication
  name: Daylight Authentication
  slug: daylight-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Daylight Domain Security
  slug: daylight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: daylight
tags:
- Company
- Security
- Cybersecurity
- Managed Detection and Response
- MDR
- Threat Detection
- Incident Response
- Agentic AI
- SOC
- MCP
website: https://daylight.ai/
---
