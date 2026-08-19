---
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 32.5
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: Per-deployment REST API and Socket.IO event stream for Oosto OnWatch, the real-time watchlist alerting and person-of-interest monitoring product. Served from the customer's own OnWatch server under th
  name: Oosto OnWatch API
  slug: oosto-onwatch-api
- description: Per-deployment REST API for Oosto OnAccess, the facial access-control product (internal codename "Abraxas"), served from the customer's own OnAccess server under the /abx/api base path. Authentication
  name: Oosto OnAccess API
  slug: oosto-onaccess-api
artifact_total: 5
asyncapis:
- description: ''
  name: Anyvision Onwatch Events
  slug: anyvision-onwatch-events
common:
- group: company
  title: ''
  type: Website
  url: https://oosto.com/
- group: docs
  title: ''
  type: Documentation
  url: https://knowledge.oosto.com/docs
- group: operate
  title: ''
  type: Support
  url: https://oosto.com/support/
- group: company
  title: ''
  type: Blog
  url: https://oosto.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://oosto.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AnyVisionltd
- group: start
  title: ''
  type: SignUp
  url: https://oosto.com/demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://oosto.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oosto.com/privacy/
- group: company
  title: ''
  type: Partners
  url: https://oosto.com/partners/
- group: company
  title: ''
  type: Press
  url: https://oosto.com/press/
- group: build
  title: ''
  type: Packages
  url: packages/anyvision-packages.yml
- group: design
  title: ''
  type: Components
  url: components/anyvision-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/anyvision-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/anyvision-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/anyvision-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/anyvision-onwatch-events.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/anyvision-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://oosto.com/why-trust-us/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/anyvision-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anyvision-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anyvision-llms.txt
- group: other
  title: ''
  type: Forge
  url: https://forgeglobal.com/anyvision_stock/
created: '2026-08-06'
description: 'AnyVision Interactive Technologies is an Israeli computer-vision company that rebranded as Oosto in October 2021 and was acquired by Metropolis Technologies in January 2025 for USD 125M. It builds real-time facial recognition and video analytics ("Vision AI") for physical security and access control, sold as three products: Oosto OnWatch (real-time watchlist alerting and person-of-interest monitoring against live camera feeds), Oosto OnAccess (touchless facial access control, tailgating detection, visitor management), and Oosto Protect (cloud alerting). The platform is deployed on premises, at the edge on a Vision AI Appliance, on smart cameras via embedded SDKs, or in the cloud, and integrates with third-party VMS and access-control systems including Milestone, Genetec and Honeywell. Its APIs are per-deployment REST + Socket.IO surfaces shipped with the customer''s own installation, documented in a login-gated knowledge base, with public sample code on GitHub.'
image: https://oosto.com/wp-content/uploads/2024/04/oosto-home-social.png
layout: provider
modified: '2026-08-06'
name: AnyVision
nav: Providers
network: true
overview: 'AnyVision publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include facial-recognition, computer-vision, video-analytics, physical-security, and access-control.


  The AnyVision catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AnyVision''s developer surface includes documentation, support, engineering blog, signup flow, authentication, and 18 more developer resources.'
random_paper: 98
score:
  band: thin
  composite: 32.6
  delta: -3.4
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 45.1
    developer_ergonomics: 19.0
    discoverability: 77.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 36.0
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anyvision/refs/heads/main/screenshots/anyvision-2026-08-07T161431.png
security:
- kind: authentication
  name: Anyvision Authentication
  slug: anyvision-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Anyvision Domain Security
  slug: anyvision-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: anyvision
tags:
- facial-recognition
- computer-vision
- video-analytics
- physical-security
- access-control
- biometrics
- surveillance
- edge-ai
- watchlist-alerting
- visitor-management
- israel
- Company
website: https://oosto.com/
---
