---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-17'
api_count: 5
apis:
- description: Embed Loom's recording experience directly into your web app. The recordSDK lets users record screen, mic, and camera, and uploads the resulting video to a Loom-hosted account. Authenticated via OAuth
  name: Loom recordSDK
  slug: loom-record-sdk
- description: Embed the Loom video player into a web page or app, with playback controls, captions, and engagement events. Includes an oEmbed endpoint for converting a Loom URL into rich embed HTML.
  name: Loom embedSDK
  slug: loom-embed-sdk
- description: oEmbed-compatible endpoint that returns rich embed metadata (HTML, thumbnail, width, height) for a given Loom video URL.
  name: Loom oEmbed API
  slug: loom-oembed-api
- description: SCIM 2.0 user and group provisioning endpoint for Enterprise customers. Integrates with Okta, Azure AD, OneLogin, and other IdPs to automate workspace membership.
  name: Loom SCIM Provisioning API
  slug: loom-scim-api
- description: SAML 2.0 single sign-on configuration for Enterprise workspaces. Configurable per workspace from the admin console; not a customer-callable REST API but documented as part of the Loom platform integra
  name: Loom SSO (SAML) Configuration
  slug: loom-sso-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/loom-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loom-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/useloom
- group: company
  title: ''
  type: Website
  url: https://www.loom.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.loom.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.loom.com/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/loomhq
- group: commercial
  title: ''
  type: Plans
  url: plans/loom-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/loom-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/loom-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://www.atlassian.com/blog/loom
created: '2026-05-08'
description: Loom is an async video messaging platform (now part of Atlassian) used by teams to record screen, voice, and camera. The Loom developer platform exposes the recordSDK and embedSDK for embedding recording and playback into other apps, plus SCIM provisioning and SSO/admin APIs available on Business and Enterprise plans.
finops:
- name: Loom Finops
  service_category: Productivity
  slug: loom-finops
graphqls:
- description: This document describes the conceptual GraphQL schema for the Loom async video messaging platform. Loom exposes its capabilities through REST APIs (recordSDK, embedSDK, oEmbed, SCIM) and this schema r
  name: Loom GraphQL Schema
  slug: loom-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loom.png
layout: provider
modified: '2026-05-30'
name: Loom
nav: Providers
network: true
overview: 'Loom publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Productivity, Video, Async, Communication, and SaaS.


  Loom''s developer surface includes pricing, GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: Loom Plans Pricing
  plan_count: 4
  slug: loom-plans-pricing
random_paper: 141
rate_limits:
- limit_count: 4
  name: Loom Rate Limits
  slug: loom-rate-limits
score:
  band: thin
  composite: 28.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 43.2
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 28.9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loom/refs/heads/main/screenshots/loom-2026-06-20T184719.png
security:
- kind: domain-security
  name: Loom Domain Security
  slug: loom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Loom Trust Center
  slug: loom-trust-center
  summary_line: FedRAMP
slug: loom
tags:
- Productivity
- Video
- Async
- Communication
- SaaS
website: https://www.loom.com/
---
