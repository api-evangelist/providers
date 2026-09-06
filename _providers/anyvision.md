---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
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
overview: 'AnyVision publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Facial Recognition, Computer-Vision, Video Analytics, Physical Security, and Access Control.


  The AnyVision catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AnyVision''s developer surface includes documentation, support, engineering blog, signup flow, authentication, and 18 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 29.9
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Facial Recognition
- Computer-Vision
- Video Analytics
- Physical Security
- Access Control
- Biometrics
- Surveillance
- Edge AI
- watchlist-alerting
- Visitor Management
- Israel
- Company
website: https://oosto.com/
---
