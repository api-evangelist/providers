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
  band: human-only
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: RESTful JSON tracking API that aggregates shipment data from 1,000+ global carriers with automatic carrier detection, real-time webhook push notifications, and standardized tracking event normalizatio
  name: Parcel Monitor Tracking API
  slug: parcel-monitor-tracking-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parcel-monitor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.parcelmonitor.com
- group: other
  title: ''
  type: Developer
  url: https://www.parcelmonitor.com/track-parcel-express-tracking-api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.parcelmonitor.com/track-parcel-express-tracking-api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.parcelmonitor.com/track-parcel-express-tracking-api/
- group: start
  title: ''
  type: Signup
  url: https://www.parcelmonitor.com/track-parcel-express-tracking-api/
- group: operate
  title: ''
  type: Contact
  url: https://resources.parcelperform.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.parcelmonitor.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.parcelmonitor.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.parcelmonitor.com/blog/
created: '2026-06-13'
description: Global parcel tracking REST API aggregating real-time tracking data from 1,000+ carriers worldwide, enabling e-commerce shipment visibility, delivery analytics, and webhook-driven notifications across 170+ countries.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/parcel-monitor.png
layout: provider
modified: '2026-06-13'
name: Parcel Monitor
nav: Providers
network: true
overview: 'Parcel Monitor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Shipping, Package Tracking, Logistics, Carriers, and Delivery.


  Parcel Monitor''s developer surface includes documentation, pricing, signup flow, engineering blog, and 6 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 3
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 52.0
    catalog_earned_first_party: 0.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parcel-monitor/refs/heads/main/screenshots/parcel-monitor-2026-06-20T191403.png
security:
- kind: domain-security
  name: Parcel Monitor Domain Security
  slug: parcel-monitor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: parcel-monitor
tags:
- Shipping
- Package Tracking
- Logistics
- Carriers
- Delivery
- Webhook
- E-Commerce
website: https://www.parcelmonitor.com
---
