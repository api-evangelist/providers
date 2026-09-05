---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Calendly Agentic Access
  operation_count: 35
  slug: calendly-agentic-access
  summary_line: 35 operations · 10 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.calendly.com
  baseurl_source: declared
  description: 'The Calendly Webhook API enables developers to receive real-time notifications when scheduling events occur in Calendly. By creating webhook subscriptions, applications can automatically receive data '
  name: Calendly Webhook API
  slug: webhook-api
- description: 'The Calendly Embed API allows developers to integrate Calendly scheduling pages directly into their websites and applications. It supports inline embeds, popup widgets, and popup text options, giving '
  name: Calendly Embed API
  slug: embed-api
- baseURL: https://api.calendly.com
  baseurl_source: declared
  description: Endpoints for retrieving activity log entries for an organization.
  name: Calendly Activity Log API
  slug: calendly-activity-log-api
- baseURL: https://api.calendly.com
  baseurl_source: declared
  description: Endpoints for viewing available times for event types and managing user availability schedules.
  name: Calendly Availability API
  slug: calendly-availability-api
- baseURL: https://api.calendly.com
  baseurl_source: declared
  description: Endpoints for handling data compliance requests such as deletion and retrieval of invitee data.
  name: Calendly Data Compliance API
  slug: calendly-data-compliance-api
- baseURL: https://api.calendly.com
  baseurl_source: declared
  description: Endpoints for listing, retrieving, and managing event types that define the kinds of meetings users can schedule.
  name: Calendly Event Types API
  slug: calendly-event-types-api
- baseURL: https://api.calendly.com
  baseurl_source: declared
  description: Endpoints for listing and retrieving organization groups.
  name: Calendly Groups API
  slug: calendly-groups-api
- baseURL: https://api.calendly.com
  baseurl_source: declared
  description: Endpoints for listing, retrieving, and creating invitees on scheduled events.
  name: Calendly Invitees API
  slug: calendly-invitees-api
- baseURL: https://api.calendly.com
  baseurl_source: declared
  description: Endpoints for managing organization memberships, invitations, and organization-level settings.
  name: Calendly Organizations API
  slug: calendly-organizations-api
- baseURL: https://api.calendly.com
  baseurl_source: declared
  description: Endpoints for listing and retrieving routing forms and their submissions.
  name: Calendly Routing Forms API
  slug: calendly-routing-forms-api
- baseURL: https://api.calendly.com
  baseurl_source: declared
  description: Endpoints for listing, retrieving, and canceling scheduled events (booked meetings).
  name: Calendly Scheduled Events API
  slug: calendly-scheduled-events-api
- baseURL: https://api.calendly.com
  baseurl_source: declared
  description: Endpoints for creating and managing shareable scheduling links.
  name: Calendly Shares API
  slug: calendly-shares-api
- baseURL: https://api.calendly.com
  baseurl_source: declared
  description: Endpoints for retrieving user information and managing user accounts within Calendly.
  name: Calendly Users API
  slug: calendly-users-api
- baseURL: https://api.calendly.com
  baseurl_source: declared
  description: Endpoints for creating, listing, retrieving, and deleting webhook subscriptions that receive real-time event notifications.
  name: Calendly Webhook Subscriptions API
  slug: calendly-webhook-subscriptions-api
artifact_total: 42
asyncapis:
- description: 'The Calendly Webhook API enables developers to receive real-time notifications when scheduling events occur in Calendly. By creating webhook subscriptions, applications can automatically receive data '
  name: Calendly Webhook Events
  slug: calendly-webhook-api-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Calendly Scheduling Activity Log API
  slug: open-calendly-activity-log-api
- collection_type: open
  name: Calendly Scheduling Activity Log Availability API
  slug: open-calendly-availability-api
- collection_type: open
  name: Calendly Scheduling Activity Log Data Compliance API
  slug: open-calendly-data-compliance-api
- collection_type: open
  name: Calendly Scheduling Activity Log Event Types API
  slug: open-calendly-event-types-api
- collection_type: open
  name: Calendly Scheduling Activity Log Groups API
  slug: open-calendly-groups-api
- collection_type: open
  name: Calendly Scheduling Activity Log Invitees API
  slug: open-calendly-invitees-api
- collection_type: open
  name: Calendly Scheduling Activity Log Organizations API
  slug: open-calendly-organizations-api
- collection_type: open
  name: Calendly Scheduling Activity Log Routing Forms API
  slug: open-calendly-routing-forms-api
- collection_type: open
  name: Calendly Scheduling Activity Log Scheduled Events API
  slug: open-calendly-scheduled-events-api
- collection_type: open
  name: Calendly Scheduling API
  slug: open-calendly-scheduling-api
- collection_type: open
  name: Calendly Scheduling Activity Log Shares API
  slug: open-calendly-shares-api
- collection_type: open
  name: Calendly Scheduling Activity Log Users API
  slug: open-calendly-users-api
- collection_type: open
  name: Calendly Scheduling Activity Log Webhook Subscriptions API
  slug: open-calendly-webhook-subscriptions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/calendly-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/calendly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/calendly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/calendly-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/calendly
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/calendly
- group: start
  title: ''
  type: Portal
  url: https://developer.calendly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.calendly.com/api-docs
- group: company
  title: ''
  type: Website
  url: https://calendly.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calendly.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://calendly.com/terms
- group: company
  title: ''
  type: Blog
  url: https://calendly.com/blog
- group: start
  title: ''
  type: Login
  url: https://calendly.com/login
- group: design
  title: ''
  type: JSONLD
  url: json-ld/calendly-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/calendly-event-type-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/calendly-scheduled-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/calendly-invitee-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.calendly.com/llms.txt
created: '2026-03-20'
description: Calendly is a scheduling automation platform that helps individuals, teams, and organizations automate the meeting lifecycle by removing the back-and-forth of scheduling. Their developer platform provides APIs for programmatically managing scheduling workflows, receiving real-time event notifications via webhooks, and embedding scheduling interfaces directly into third-party applications.
finops:
- name: Calendly Finops
  service_category: Productivity / Scheduling SaaS
  slug: calendly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/calendly.png
json_schemas:
- name: Calendly Event Type
  property_count: 20
  slug: calendly-event-type
- name: Calendly Invitee
  property_count: 21
  slug: calendly-invitee
- name: Calendly Scheduled Event
  property_count: 13
  slug: calendly-scheduled-event
jsonld:
- class_count: 0
  name: Calendly Context
  property_count: 9
  slug: calendly-context
layout: provider
modified: '2026-05-19'
name: Calendly
nav: Providers
network: true
overview: 'Calendly publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Webhook API, Activity Log API, Availability API, and 10 more. Tagged areas include Appointments, Automation, Booking, Calendars, and Meetings.


  The Calendly catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Calendly''s developer surface includes authentication, developer portal, documentation, engineering blog, and 14 more developer resources.'
plans:
- name: Calendly Plans Pricing
  plan_count: 4
  slug: calendly-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Calendly Rate Limits
  slug: calendly-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Calendly API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: calendly-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Calendly API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: calendly-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 54.5
    catalog_earned_first_party: 0.0
    catalog_gap: 60.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 13.6
    contract_quality: 67.6
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/calendly/refs/heads/main/screenshots/calendly-2026-06-20T173843.png
security:
- kind: authentication
  name: Calendly Authentication
  slug: calendly-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Calendly Domain Security
  slug: calendly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Calendly Vulnerability Disclosure
  slug: calendly-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: calendly
tags:
- Appointments
- Automation
- Booking
- Calendars
- Meetings
- Scheduling
website: https://calendly.com/
---
