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
    auth_clarity: false
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
  score: 17.3
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Programmatic access to the Tanaza Cloud dashboard data set across three documented API families — Network Management, Network Monitoring, and Application — plus Push Contact Notifications webhooks. Re
  name: Tanaza Cloud API
  slug: tanaza-cloud-api
artifact_total: 3
asyncapis:
- description: ''
  name: Tanaza Push Notifications Webhooks
  slug: tanaza-push-notifications-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.tanaza.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.tanaza.com/
- group: docs
  title: ''
  type: Documentation
  url: https://success.tanaza.com/s/article/Tanaza-APIs-Overview
- group: docs
  title: ''
  type: APIReference
  url: https://success.tanaza.com/s/article/Network-Status-APIs
- group: operate
  title: ''
  type: Support
  url: https://support.tanaza.com/
- group: company
  title: ''
  type: Blog
  url: https://www.tanaza.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tanaza.com/tanaza-pricing-plans/
- group: start
  title: ''
  type: SignUp
  url: https://app.tanaza.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tanaza.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tanaza.com/legal/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tanaza
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tanaza-push-notifications-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tanaza-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tanaza-llms.txt
created: '2026-07-17'
description: Tanaza is a hardware-agnostic, cloud-based Wi-Fi management platform, headquartered in Milan, Italy, that lets managed service providers, system integrators, and businesses configure, monitor, and operate Wi-Fi access points, SSIDs, and networks from a single dashboard. Alongside its cloud management platform, Tanaza operates Classic Hotspot, a guest-Wi-Fi / captive-portal product with social login, paid Wi-Fi vouchers, splash-page editing, and analytics. Tanaza exposes three API families — a Network Management API, a Network Monitoring API, and an Application API — that give developers programmatic access to the Tanaza Cloud dashboard data set (networks, access points, MAC addresses, active SSIDs, connected clients, and signal strength in dBm), plus a Push Contact Notifications webhook feature that delivers event notifications to a customer-hosted endpoint over HTTP POST.
image: https://www.tanaza.com/wp-content/uploads/2020/03/hito-tanaza-logo.png
layout: provider
modified: '2026-07-21'
name: Tanaza
nav: Providers
network: true
overview: 'Tanaza publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wi-Fi, Networking, Cloud Management, and Access Points.


  The Tanaza catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tanaza''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, and 8 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 10.7
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - italy-southern-europe
  previous_composite: 17.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tanaza/refs/heads/main/screenshots/tanaza-2026-09-02T162518.png
security:
- kind: domain-security
  name: Tanaza Domain Security
  slug: tanaza-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: tanaza
tags:
- Company
- Wi-Fi
- Networking
- Cloud Management
- Access Points
- Hotspot
- Captive Portal
- Monitoring
- Managed Service Provider
- Telecommunications
website: https://www.tanaza.com/
---
