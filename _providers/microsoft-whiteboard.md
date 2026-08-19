---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.5
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Microsoft Graph Whiteboard API enables developers to manage Microsoft Whiteboard resources programmatically. Applications can create whiteboards, manage participants, and export whiteboard content
  name: Microsoft Graph Whiteboard API
  slug: graph-whiteboard-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-whiteboard-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-whiteboard-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: start
  title: ''
  type: Portal
  url: https://whiteboard.microsoft.com/
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/microsoft-365/microsoft-whiteboard/digital-whiteboard-app
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/graph/api/resources/whiteboard
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/
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
created: '2024-01-01'
description: Microsoft Whiteboard is a digital canvas for visual collaboration. It provides API access through Microsoft Graph for managing whiteboard resources, participants, and content programmatically.
finops:
- name: Microsoft Whiteboard Finops
  service_category: API
  slug: microsoft-whiteboard-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-whiteboard.png
layout: provider
modified: '2026-04-28'
name: Microsoft Whiteboard
nav: Providers
network: true
overview: 'Microsoft Whiteboard publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Collaboration, Microsoft, Microsoft 365, Visual Collaboration, and Whiteboard.


  Microsoft Whiteboard''s developer surface includes developer portal, documentation, authentication, support, and 6 more developer resources.'
plans:
- name: Microsoft Whiteboard Plans Pricing
  plan_count: 3
  slug: microsoft-whiteboard-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Microsoft Whiteboard Rate Limits
  slug: microsoft-whiteboard-rate-limits
score:
  band: emerging
  composite: 19.9
  delta: -1.6
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 21.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-whiteboard/refs/heads/main/screenshots/microsoft-whiteboard-2026-06-20T185544.png
security:
- kind: domain-security
  name: Microsoft Whiteboard Domain Security
  slug: microsoft-whiteboard-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Whiteboard Vulnerability Disclosure
  slug: microsoft-whiteboard-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-whiteboard
tags:
- Collaboration
- Microsoft
- Microsoft 365
- Visual Collaboration
- Whiteboard
website: https://www.microsoft.com/en-us/microsoft-365/microsoft-whiteboard/digital-whiteboard-app
---
