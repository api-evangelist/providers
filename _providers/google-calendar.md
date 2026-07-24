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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Google Calendar Agentic Access
  operation_count: 18
  slug: google-calendar-agentic-access
  summary_line: 18 operations · 11 acting
api_count: 4
apis:
- description: The Calendars API from Google Calendar — 6 operation(s) for calendars.
  name: Google Calendar Calendars API
  slug: google-calendar-calendars-api
- description: The Colors API from Google Calendar — 1 operation(s) for colors.
  name: Google Calendar Colors API
  slug: google-calendar-colors-api
- description: The freeBusy API from Google Calendar — 1 operation(s) for freebusy.
  name: Google Calendar freeBusy API
  slug: google-calendar-freebusy-api
- description: The Users API from Google Calendar — 2 operation(s) for users.
  name: Google Calendar Users API
  slug: google-calendar-users-api
artifact_total: 13
collections:
- collection_type: open
  name: Google Calendar API
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-calendar-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-calendar-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-calendar-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleworkspace
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/workspace/calendar
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/workspace/calendar/api/guides/overview
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/workspace/calendar/api/reference/rest
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/identity/protocols/oauth2
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.google.com/workspace/calendar/api/guides/quota
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.google.com/appsstatus/dashboard/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/workspace/calendar/api/support
- group: company
  title: ''
  type: Blog
  url: https://workspaceupdates.googleblog.com/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.jsonld
created: '2026-03-13'
description: The Google Calendar API provides RESTful access to Google Calendar data, enabling applications to create, view, and manage calendar events, access control lists, and user settings. It supports creating and managing multiple calendars, querying free/busy information, setting up push notifications for changes, and integrating calendar functionality into third-party applications.
finops:
- name: Google Calendar Finops
  service_category: API
  slug: google-calendar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-calendar.png
jsonld:
- class_count: 4
  name: Json Ld Context
  property_count: 4
  slug: json-ld
layout: provider
modified: '2026-05-19'
name: Google Calendar
nav: Providers
network: true
overview: 'Google Calendar publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Calendars API, Colors API, freeBusy API, and 1 more. Tagged areas include Availability, Calendar, Events, Google, and Google Workspace.


  The Google Calendar catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Calendar''s developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, engineering blog, and 8 more developer resources.'
plans:
- name: Google Calendar Plans Pricing
  plan_count: 3
  slug: google-calendar-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Google Calendar Rate Limits
  slug: google-calendar-rate-limits
rules:
- name: Google Calendar API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-calendar-jsonschema-spectral-rules
score:
  band: developing
  composite: 59.5
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 54.9
    developer_ergonomics: 45.7
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 59.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-calendar/refs/heads/main/screenshots/google-calendar-2026-06-20T182032.png
security:
- kind: domain-security
  name: Google Calendar Domain Security
  slug: google-calendar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Calendar Vulnerability Disclosure
  slug: google-calendar-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-calendar
tags:
- Availability
- Calendar
- Events
- Google
- Google Workspace
- Scheduling
website: https://developers.google.com/workspace/calendar
---
