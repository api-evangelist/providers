---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-10-17'
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
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/oosto/refs/heads/main/security/oosto-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oosto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oosto.com
- group: docs
  title: ''
  type: Documentation
  url: https://knowledge.oosto.com/docs/
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
  url: https://oosto.com/blog/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://oosto.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oosto.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oosto
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AnyVisionltd
created: '2026-07-17'
description: Oosto (formerly AnyVision) is an enterprise vision-AI company providing real-time facial recognition, watchlist alerting, and video analytics for physical security, safety, and touchless access control. Its platform spans OnWatch real-time watchlist monitoring, OnAccess touchless facial-recognition access control, and Oosto Protect edge-to-cloud video analytics (person-of-interest detection, body/skeleton and pose/action recognition, and liveness detection), delivered via cloud, on-premises, and SDK deployments and integrating with existing VMS and camera systems. Backed by SoftBank Vision Fund. Oosto exposes no public self-serve developer API; its technical documentation lives in a login-gated partner knowledge base.
image: https://oosto.com/wp-content/uploads/2024/04/oosto-home-social.png
layout: provider
modified: '2026-07-20'
name: Oosto
nav: Providers
network: true
overview: 'Oosto is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Facial Recognition, Computer Vision, and Video Analytics.


  The Oosto catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Oosto''s developer surface includes documentation, support, engineering blog, and 7 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 14.4
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 10.4
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 17.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/oosto/refs/heads/main/screenshots/oosto-2026-08-07T190444.png
security:
- kind: authentication
  name: Anyvision Authentication
  slug: anyvision-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Oosto Domain Security
  slug: oosto-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: oosto
tags:
- Company
- Enterprise
- Facial Recognition
- Computer Vision
- Video Analytics
- Physical Security
- Access Control
- Artificial Intelligence
- Biometrics
- Acquired
- Surveillance
- Edge AI
- watchlist-alerting
- Visitor Management
- Israel
website: https://oosto.com
---
