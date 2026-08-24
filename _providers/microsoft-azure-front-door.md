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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Front Door Agentic Access
  operation_count: 7
  slug: microsoft-azure-front-door-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- description: Operations operations
  name: Azure Front Door Operations API
  slug: microsoft-azure-front-door-operations-api
- description: Profiles operations
  name: Azure Front Door Profiles API
  slug: microsoft-azure-front-door-profiles-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Front Door REST Operations API
  slug: open-microsoft-azure-front-door-operations-api
- collection_type: open
  name: Azure Front Door REST Operations Profiles API
  slug: open-microsoft-azure-front-door-profiles-api
- collection_type: open
  name: Azure Front Door REST API
  slug: open-microsoft-azure-front-door
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-front-door-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-front-door-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-front-door-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-front-door-scopes.yml
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
description: Azure Front Door Service enables you to define, manage, and monitor the global routing for your web traffic. The REST API supports configuring routing rules, backend pools, health probes, caching policies, and WAF rules for secure and performant application delivery at the edge.
finops:
- name: Microsoft Azure Front Door Finops
  service_category: API
  slug: microsoft-azure-front-door-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-front-door.png
layout: provider
modified: '2026-05-19'
name: Azure Front Door
nav: Providers
network: true
overview: 'Azure Front Door publishes 2 APIs on the [APIs.io](https://apis.io/) network: Operations API and Profiles API. Tagged areas include CDN, Edge, Global Routing, Load Balancing, and WAF.


  Azure Front Door''s developer surface includes authentication, developer portal, pricing, support, and 7 more developer resources.'
plans:
- name: Microsoft Azure Front Door Plans Pricing
  plan_count: 3
  slug: microsoft-azure-front-door-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Microsoft Azure Front Door Rate Limits
  slug: microsoft-azure-front-door-rate-limits
scopes:
- name: Microsoft Azure Front Door Scopes
  scope_count: 1
  slug: microsoft-azure-front-door-scopes
  summary_line: 1 scope · implicit
score:
  band: thin
  composite: 35.5
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 35.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-front-door/refs/heads/main/screenshots/microsoft-azure-front-door-2026-06-20T185415.png
security:
- kind: authentication
  name: Microsoft Azure Front Door Authentication
  slug: microsoft-azure-front-door-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Front Door Domain Security
  slug: microsoft-azure-front-door-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-front-door
tags:
- CDN
- Edge
- Global Routing
- Load Balancing
- WAF
website: https://portal.azure.com/
---
