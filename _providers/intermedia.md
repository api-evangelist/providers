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
api_count: 5
apis:
- description: The Intermedia Voice API enables developers to embed voice calling capabilities into CRMs, ERPs, ticketing systems, and other business applications.
  name: Intermedia Voice API
  slug: voice-api
- description: The Intermedia Meeting API enables integration of video conferencing capabilities, including starting and managing meetings from calendar platforms and business applications.
  name: Intermedia Meeting API
  slug: meeting-api
- description: The Intermedia Analytics API provides communication insights and calling data that can be consolidated into reporting and business intelligence tools.
  name: Intermedia Analytics API
  slug: analytics-api
- description: The Intermedia Address Book API aggregates user contacts from multiple sources into a unified directory accessible across Intermedia applications.
  name: Intermedia Address Book API
  slug: address-book-api
- description: The Intermedia Contact Center API delivers customer experience features including screen pops, dashboards, and omni-channel outreach campaigns for contact center integrations.
  name: Intermedia Contact Center API
  slug: contact-center-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/intermedia-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/intermedia-net
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/intermedia
- group: company
  title: ''
  type: Website
  url: https://www.intermedia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.intermedia.com/integrations/apis
- group: start
  title: ''
  type: Portal
  url: https://developer.intermedia.net/
- group: operate
  title: ''
  type: Support
  url: https://www.intermedia.com/support/
- group: company
  title: ''
  type: Blog
  url: https://blog.intermedia.com/feed/
created: '2024-11-13'
description: Intermedia is a cloud communications company serving over 145,000 businesses with an AI-powered platform spanning voice, video conferencing, chat, SMS, contact center, business email, productivity, file sharing, security, and archiving. The Intermedia Extend API platform exposes Voice, Meeting, Analytics, Address Book, and Contact Center APIs for embedding communications into CRMs, ERPs, ticketing systems, and custom business applications.
finops:
- name: Intermedia Finops
  service_category: API
  slug: intermedia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/intermedia.png
layout: provider
modified: '2026-04-28'
name: Intermedia
nav: Providers
network: true
overview: 'Intermedia publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, Communications, Contact Center, Video Conferencing, and Voice.


  Intermedia''s developer surface includes documentation, developer portal, support, engineering blog, and 4 more developer resources.'
plans:
- name: Intermedia Plans Pricing
  plan_count: 3
  slug: intermedia-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Intermedia Rate Limits
  slug: intermedia-rate-limits
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 16.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/intermedia/refs/heads/main/screenshots/intermedia-2026-06-20T183449.png
security:
- kind: domain-security
  name: Intermedia Domain Security
  slug: intermedia-domain-security
  summary_line: TLSv1.3 · DMARC
slug: intermedia
tags:
- Cloud
- Communications
- Contact Center
- Video Conferencing
- Voice
website: https://www.intermedia.com/
---
