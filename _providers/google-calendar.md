---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Google Calendar Agentic Access
  operation_count: 18
  slug: google-calendar-agentic-access
  summary_line: 18 operations · 10 acting
api_count: 1
apis:
- baseURL: https://www.googleapis.com/calendar/v3
  baseurl_source: declared
  description: The Calendars API from Google Calendar — 6 operation(s) for calendars.
  name: Google Calendar Calendars API
  slug: google-calendar-calendars-api
- baseURL: https://www.googleapis.com/calendar/v3
  baseurl_source: declared
  description: The Colors API from Google Calendar — 1 operation(s) for colors.
  name: Google Calendar Colors API
  slug: google-calendar-colors-api
- baseURL: https://www.googleapis.com/calendar/v3
  baseurl_source: declared
  description: The Users API from Google Calendar — 2 operation(s) for users.
  name: Google Calendar Users API
  slug: google-calendar-users-api
- baseURL: https://www.googleapis.com/calendar/v3
  baseurl_source: declared
  description: The Free Busy API from Google Calendar — 1 operation(s) for free busy.
  name: Google Calendar Free Busy API
  slug: google-calendar-free-busy-api
artifact_total: 21
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
- group: commercial
  href: https://artifacts.apis.io/google-calendar/plans/google-calendar-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-calendar-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-calendar/rate-limits/google-calendar-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-calendar-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-calendar/finops/google-calendar-finops.yml
  title: ''
  type: FinOps
  url: finops/google-calendar-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-calendar/overview
- group: agent
  href: https://artifacts.apis.io/google-calendar/agentic-access/google-calendar-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-calendar-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-calendar/security/google-calendar-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-calendar-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-calendar/security/google-calendar-domain-security.yml
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
  href: https://artifacts.apis.io/google-calendar/json-ld/json-ld.jsonld
  title: ''
  type: JSONLD
  url: json-ld/json-ld.jsonld
created: '2026-03-13'
description: The Google Calendar API provides RESTful access to Google Calendar data, enabling applications to create, view, and manage calendar events, access control lists, and user settings. It supports creating and managing multiple calendars, querying free/busy information, setting up push notifications for changes, and integrating calendar functionality into third-party applications.
finops:
- has_sources: true
  method: derived
  name: Google Calendar Finops
  primary_unit: ''
  service_category: ''
  slug: google-calendar-finops
  template: true
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
overview: 'Google Calendar publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Calendars API, Colors API, Users API, and 1 more. Tagged areas include Availability, Calendar, Event, Google, and Google Workspace.


  The Google Calendar catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Calendar''s developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, engineering blog, and 13 more developer resources.'
plans:
- name: Google Calendar Plans Pricing
  plan_count: 1
  slug: google-calendar-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Google Calendar Rate Limits
  slug: google-calendar-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Google Calendar — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-calendar-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 61.7
    catalog_earned_first_party: 8.0
    catalog_gap: 53.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 9.8
    contract_quality: 55.6
    developer_ergonomics: 51.2
    discoverability: 66.1
    operational_transparency: 36.8
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/google-calendar/google-calendar-2026-06-20T182032.png
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
website: https://www.google.com/
---
