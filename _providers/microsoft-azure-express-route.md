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
  name: Microsoft Azure Express Route Agentic Access
  operation_count: 7
  slug: microsoft-azure-express-route-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- description: ExpressRoute Circuits operations
  name: Azure ExpressRoute ExpressRoute Circuits API
  slug: microsoft-azure-express-route-expressroute-circuits-api
- description: Operations operations
  name: Azure ExpressRoute Operations API
  slug: microsoft-azure-express-route-operations-api
artifact_total: 10
collections:
- collection_type: open
  name: Azure ExpressRoute REST API
  slug: open-microsoft-azure-express-route
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-express-route-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-express-route-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-express-route-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-express-route-scopes.yml
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
created: '2026-03-13'
description: Azure ExpressRoute lets you create private connections between Azure datacenters and infrastructure on your premises or in a colocation environment. The REST API enables management of circuits, peering, route filters, and ExpressRoute Global Reach for cross-premises connectivity.
finops:
- name: Microsoft Azure Express Route Finops
  service_category: API
  slug: microsoft-azure-express-route-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-express-route.png
layout: provider
modified: '2026-05-19'
name: Azure ExpressRoute
nav: Providers
network: true
overview: 'Azure ExpressRoute publishes 2 APIs on the [APIs.io](https://apis.io/) network: ExpressRoute Circuits API and Operations API. Tagged areas include ExpressRoute, Hybrid Network, Private Connectivity, and WAN.


  Azure ExpressRoute''s developer surface includes authentication, developer portal, pricing, support, and 7 more developer resources.'
plans:
- name: Microsoft Azure Express Route Plans Pricing
  plan_count: 3
  slug: microsoft-azure-express-route-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 5
  name: Microsoft Azure Express Route Rate Limits
  slug: microsoft-azure-express-route-rate-limits
scopes:
- name: Microsoft Azure Express Route Scopes
  scope_count: 1
  slug: microsoft-azure-express-route-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 43.5
  delta: -1.6
  facets:
    commercial_clarity: 71.1
    contract_quality: 55.1
    developer_ergonomics: 23.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 45.1
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
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-express-route/refs/heads/main/screenshots/microsoft-azure-express-route-2026-06-20T185415.png
security:
- kind: authentication
  name: Microsoft Azure Express Route Authentication
  slug: microsoft-azure-express-route-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Express Route Domain Security
  slug: microsoft-azure-express-route-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-express-route
tags:
- ExpressRoute
- Hybrid Network
- Private Connectivity
- WAN
website: https://portal.azure.com/
---
