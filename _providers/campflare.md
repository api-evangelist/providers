---
access_model:
  confidence: medium
  label: Freemium · Requires approval
  onboarding: approval
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.8
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Real-time campground availability data at the campsite level across all public campgrounds Campflare tracks. Developers can query current and upcoming availability, inspect amenities (hookups, facilit
  name: Campflare Availability & Alerts API
  slug: campflare-availability-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/campflare-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/campflare
- group: company
  title: ''
  type: Website
  url: https://campflare.com/
- group: docs
  title: ''
  type: Documentation
  url: https://campflare.com/api
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://campflare.com/updates
- group: operate
  title: ''
  type: FAQ
  url: https://campflare.com/info
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/us/app/campflare/id1670055811
- group: operate
  title: ''
  type: Contact
  url: mailto:contact@campflare.com
created: '2024-11-14'
description: Campflare provides real-time campground availability data and cancellation alerts as a public API. The platform tracks campsites across every major public reservation system in North America and notifies users (via webhook) the moment a site matching their criteria becomes available. Campflare's data and services are open to the public programmatically — individuals and non-profits get free access to all APIs, while commercial use requires a paid license. Campflare also powers partner products such as Hipcamp Alerts. Current API access is invite-only; requests go to contact@campflare.com and are typically granted within 24–48 hours.
finops:
- name: Campflare Finops
  service_category: API
  slug: campflare-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/campflare.png
layout: provider
modified: '2026-04-23'
name: Campflare
nav: Providers
network: true
overview: 'Campflare publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Campgrounds, Outdoor, Recreation, Availability, and Alerts.


  Campflare''s developer surface includes documentation, release notes, FAQ, and 5 more developer resources.'
plans:
- name: Campflare Plans Pricing
  plan_count: 3
  slug: campflare-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Campflare Rate Limits
  slug: campflare-rate-limits
score:
  band: emerging
  composite: 18.1
  delta: 3.7
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 14.4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/campflare/refs/heads/main/screenshots/campflare-2026-06-20T173909.png
security:
- kind: domain-security
  name: Campflare Domain Security
  slug: campflare-domain-security
  summary_line: TLSv1.3
slug: campflare
tags:
- Campgrounds
- Outdoor
- Recreation
- Availability
- Alerts
- Webhook
- Reservations
website: https://campflare.com/
---
