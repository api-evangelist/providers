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
  scored_at: '2026-09-05'
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
- group: start
  title: ''
  type: DeveloperPortal
  url: https://campflare.com/api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://campflare.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://campflare.com/legal
- group: operate
  title: ''
  type: Support
  url: https://campflare.com/feedback
- group: start
  title: ''
  type: Login
  url: https://campflare.com/auth
- group: operate
  title: ''
  type: StatusPage
  url: https://status.campflare.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/campflare-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/campflare-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/campflare-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/campflare-llms.txt
coverage:
  checked: '2026-09-05'
  detail: Campflare's only developer page states "The Campflare API is temporarily invite only. Please reach out to contact@campflare.com for access" and stands in for a reference — there is no operation list, no schema and no machine-readable contract behind it, so every spec probe against campflare.com and the live API host api.campflare.com missed.
  evidence:
  - status: 200
    url: https://campflare.com/api
  - status: 404
    url: https://api.campflare.com/openapi.json
  - status: 200
    url: https://api.campflare.com/v2
  - status: 404
    url: https://campflare.com/llms.txt
  reason: sales-gate
  state: gated
created: '2024-11-14'
description: Campflare provides real-time campground availability data and cancellation alerts as a public API. The platform tracks campsites across every major public reservation system in North America and notifies users (via webhook) the moment a site matching their criteria becomes available. Campflare's data and services are open to the public programmatically — individuals and non-profits get free access to all APIs, while commercial use requires a paid license. Campflare also powers partner products such as Hipcamp Alerts. Current API access is invite-only; requests go to contact@campflare.com and are typically granted within 24–48 hours.
finops:
- name: Campflare Finops
  service_category: API
  slug: campflare-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/campflare.png
layout: provider
modified: '2026-09-05'
name: Campflare
nav: Providers
network: true
overview: 'Campflare publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Campgrounds, Outdoor, Recreation, Availability, and Alerts.


  Campflare''s developer surface includes documentation, FAQ, support, and 14 more developer resources.'
plans:
- name: Campflare Plans Pricing
  plan_count: 2
  slug: campflare-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Campflare Rate Limits
  slug: campflare-rate-limits
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.0
  facets:
    access_clarity: 56.6
    commercial_clarity: 56.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 18.1
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
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
