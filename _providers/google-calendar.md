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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Google Calendar Agentic Access
  operation_count: 18
  slug: google-calendar-agentic-access
  summary_line: 18 operations · 11 acting
api_count: 1
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
artifact_total: 22
collections:
- collection_type: postman
  name: Google Calendar Calendars API
  slug: postman-google-calendar-calendars-api
- collection_type: postman
  name: Google Calendar Calendars Colors API
  slug: postman-google-calendar-colors-api
- collection_type: postman
  name: Google Calendar Calendars freeBusy API
  slug: postman-google-calendar-freebusy-api
- collection_type: postman
  name: Google Calendar Calendars Users API
  slug: postman-google-calendar-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Calendar Calendars API
  slug: open-google-calendar-calendars-api
- collection_type: open
  name: Google Calendar Calendars Colors API
  slug: open-google-calendar-colors-api
- collection_type: open
  name: Google Calendar Calendars freeBusy API
  slug: open-google-calendar-freebusy-api
- collection_type: open
  name: Google Calendar Calendars Users API
  slug: open-google-calendar-users-api
- collection_type: open
  name: Google Calendar API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-calendar/overview
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
overview: 'Google Calendar publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Calendars API, Colors API, freeBusy API, and 1 more. Tagged areas include Availability, Calendar, Event, Google, and Google Workspace.


  The Google Calendar catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Calendar''s developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, engineering blog, and 9 more developer resources.'
plans:
- name: Google Calendar Plans Pricing
  plan_count: 3
  slug: google-calendar-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Google Calendar Rate Limits
  slug: google-calendar-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Google Calendar API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-calendar-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 13
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 61.1
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 47.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Event
- Google
- Google Workspace
- Scheduling
website: https://developers.google.com/workspace/calendar
---
