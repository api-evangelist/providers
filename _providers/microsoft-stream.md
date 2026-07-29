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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Microsoft Stream (on SharePoint) provides video management capabilities through Microsoft Graph and SharePoint APIs. Videos are stored in OneDrive and SharePoint, enabling developers to upload, manage
  name: Microsoft Graph Stream Video API
  slug: graph-video-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-stream-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: start
  title: ''
  type: Portal
  url: https://www.microsoft365.com/
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/microsoft-365/microsoft-stream
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/stream/
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
description: Microsoft Stream is an intelligent video service for enterprise video management. Videos are stored in OneDrive and SharePoint with video-specific capabilities accessible through Microsoft Graph and SharePoint APIs.
finops:
- name: Microsoft Stream Finops
  service_category: API
  slug: microsoft-stream-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-stream.png
layout: provider
modified: '2026-04-28'
name: Microsoft Stream
nav: Providers
network: true
overview: 'Microsoft Stream publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Microsoft, Microsoft 365, Streaming, and Video.


  Microsoft Stream''s developer surface includes developer portal, documentation, authentication, support, and 5 more developer resources.'
plans:
- name: Microsoft Stream Plans Pricing
  plan_count: 3
  slug: microsoft-stream-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 5
  name: Microsoft Stream Rate Limits
  slug: microsoft-stream-rate-limits
score:
  band: thin
  composite: 29.3
  delta: -2.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 31.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-stream/refs/heads/main/screenshots/microsoft-stream-2026-06-20T185535.png
security:
- kind: domain-security
  name: Microsoft Stream Domain Security
  slug: microsoft-stream-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: microsoft-stream
tags:
- Microsoft
- Microsoft 365
- Streaming
- Video
website: https://www.microsoft.com/en-us/microsoft-365/microsoft-stream
---
