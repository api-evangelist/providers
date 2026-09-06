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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://zcal.co
  baseurl_source: spec
  description: Unlimited shareable scheduling links, meeting polls, and customizable booking pages let invitees self-serve a time. This is a product surface managed through the Zcal web application; there is no docu
  name: Zcal Scheduling Links
  slug: scheduling-links
- baseURL: https://zcal.co
  baseurl_source: spec
  description: 'Bookings (events) capture timing, hosts, attendees, location, and custom question responses. Booking data is surfaced to external systems through outbound webhooks rather than a queryable public REST '
  name: Zcal Bookings
  slug: bookings
- baseURL: https://zcal.co
  baseurl_source: spec
  description: Outbound webhooks POST a JSON payload to a subscriber URL when a booking is created, rescheduled, or cancelled. Payloads can be verified with an optional HMAC SHA-256 signature via the x-zcal-webhook-
  name: Zcal Integrations and Webhooks
  slug: integrations-webhooks
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zcal
  slug: open-zcal
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/zcal-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zcal-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zcal
- group: company
  title: ''
  type: Website
  url: https://zcal.co/
- group: docs
  title: ''
  type: Documentation
  url: https://help.zcal.co/
- group: commercial
  title: ''
  type: Plans
  url: plans/zcal-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zcal-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zcal-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://zcal.co/blog
created: '2026-06-21'
description: Zcal is a free scheduling platform for booking meetings via shareable scheduling links, meeting polls, and team pages (round-robin and collective). Zcal does not publish a general-purpose public REST API; programmatic integration is delivered through outbound webhooks (event.created, event.rescheduled, event.cancelled) and no-code connectors such as Zapier and Make, plus native integrations including Zoom, Stripe, Google Analytics, and Meta Pixel.
finops:
- name: Zcal Finops
  service_category: Scheduling and Collaboration
  slug: zcal-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zcal.png
layout: provider
modified: '2026-06-21'
name: Zcal
nav: Providers
network: true
overview: 'Zcal publishes 3 APIs on the [APIs.io](https://apis.io/) network: Scheduling Links, Bookings, and Integrations and Webhooks. Tagged areas include Scheduling, Calendar, Booking, Meetings, and Webhook.


  Zcal''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Zcal Plans Pricing
  plan_count: 3
  slug: zcal-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Zcal Rate Limits
  slug: zcal-rate-limits
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 55.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 29.9
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 28.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zcal/refs/heads/main/screenshots/zcal-2026-09-02T171458.png
security:
- kind: domain-security
  name: Zcal Domain Security
  slug: zcal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Zcal Trust Center
  slug: zcal-trust-center
  summary_line: SOC 2, ISO 27001
slug: zcal
tags:
- Scheduling
- Calendar
- Booking
- Meetings
- Webhook
website: https://zcal.co/
---
