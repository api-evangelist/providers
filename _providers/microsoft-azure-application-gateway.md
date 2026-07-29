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
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Application Gateway Agentic Access
  operation_count: 7
  slug: microsoft-azure-application-gateway-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- description: Application Gateways operations
  name: Azure Application Gateway Application Gateways API
  slug: microsoft-azure-application-gateway-application-gateways-api
- description: Operations operations
  name: Azure Application Gateway Operations API
  slug: microsoft-azure-application-gateway-operations-api
artifact_total: 10
collections:
- collection_type: open
  name: Azure Application Gateway REST API
  slug: open-microsoft-azure-application-gateway
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-application-gateway-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-application-gateway-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-application-gateway-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-application-gateway-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/feed/
created: '2026-03-13'
description: Learn how the Application Gateway is a Network Service which provides HTTP Load balancing as a Service to Azure customers.
finops:
- name: Microsoft Azure Application Gateway Finops
  service_category: API
  slug: microsoft-azure-application-gateway-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-application-gateway.png
layout: provider
modified: '2026-05-19'
name: Azure Application Gateway
nav: Providers
network: true
overview: 'Azure Application Gateway publishes 2 APIs on the [APIs.io](https://apis.io/) network: Application Gateways API and Operations API. Tagged areas include Layer 7, Load Balancing, Reverse Proxy, and WAF.


  Azure Application Gateway''s developer surface includes authentication, developer portal, pricing, support, engineering blog, and 7 more developer resources.'
plans:
- name: Microsoft Azure Application Gateway Plans Pricing
  plan_count: 3
  slug: microsoft-azure-application-gateway-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 5
  name: Microsoft Azure Application Gateway Rate Limits
  slug: microsoft-azure-application-gateway-rate-limits
scopes:
- name: Microsoft Azure Application Gateway Scopes
  scope_count: 1
  slug: microsoft-azure-application-gateway-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 43.0
  delta: -1.2
  facets:
    commercial_clarity: 71.1
    contract_quality: 55.1
    developer_ergonomics: 26.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 44.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-application-gateway/refs/heads/main/screenshots/microsoft-azure-application-gateway-2026-06-20T185354.png
security:
- kind: authentication
  name: Microsoft Azure Application Gateway Authentication
  slug: microsoft-azure-application-gateway-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Application Gateway Domain Security
  slug: microsoft-azure-application-gateway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-application-gateway
tags:
- Layer 7
- Load Balancing
- Reverse Proxy
- WAF
website: https://portal.azure.com/
---
