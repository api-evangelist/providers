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
  band: human-only
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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'RESTful API for managing B2B events including conferences, speakers, ticketing, attendee registration, contacts, sessions, and event analytics. Enables third-party developers and Bizzabo customers to '
  name: Bizzabo Public API
  slug: bizzabo-public-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bizzabo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bizzabo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://bizzabo.stoplight.io/docs/bizzabo-partner-apis/784b40317b1fa-introduction-to-bizzabo-s-open-application-programming-interface-api
- group: company
  title: ''
  type: Blog
  url: https://www.bizzabo.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bizzabo.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bizzabo.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bizzabo
- group: operate
  title: ''
  type: ContactUs
  url: https://www.bizzabo.com/contact-us
- group: start
  title: ''
  type: Login
  url: https://login.bizzabo.com/
created: '2026-06-13'
description: Bizzabo is a B2B event experience platform with REST APIs for managing conferences, speakers, ticketing, attendee data, and event analytics and performance metrics. The open API enables developers to build custom integrations, automate event workflows, synchronize attendee data with CRM and marketing platforms, and deliver personalized event experiences at scale.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bizzabo.png
jsonld:
- class_count: 0
  name: Apis Context
  property_count: 0
  slug: apis
layout: provider
modified: '2026-06-13'
name: Bizzabo
nav: Providers
network: true
overview: 'Bizzabo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Events, Event Management, B2B Events, Conference Management, and Ticketing.


  The Bizzabo catalog on APIs.io includes 1 JSON-LD context.


  Bizzabo''s developer surface includes documentation, engineering blog, pricing, and 6 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 18
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 22.6
  delta: -1.7
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 0.0
    contract_quality: 7.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 24.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bizzabo/refs/heads/main/screenshots/bizzabo-2026-06-20T173329.png
security:
- kind: domain-security
  name: Bizzabo Domain Security
  slug: bizzabo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bizzabo
tags:
- Events
- Event Management
- B2B Events
- Conference Management
- Ticketing
- Attendees
- Speakers
- Registration
- Analytics
- Event Technology
website: https://www.bizzabo.com/
---
