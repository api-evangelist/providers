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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Savvycal Agentic Access
  operation_count: 16
  slug: savvycal-agentic-access
  summary_line: 16 operations · 5 acting
api_count: 6
apis:
- description: Retrieve information about the authenticated user.
  name: SavvyCal Current User API
  slug: savvycal-current-user-api
- description: Manage scheduled events and bookings.
  name: SavvyCal Events API
  slug: savvycal-events-api
- description: Create and manage scheduling links for booking.
  name: SavvyCal Scheduling Links API
  slug: savvycal-scheduling-links-api
- description: List and retrieve time zone information.
  name: SavvyCal Time Zones API
  slug: savvycal-time-zones-api
- description: Configure webhooks for real-time event notifications.
  name: SavvyCal Webhooks API
  slug: savvycal-webhooks-api
- description: Manage automation workflows.
  name: SavvyCal Workflows API
  slug: savvycal-workflows-api
artifact_total: 23
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/savvycal-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/savvycal-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/savvycal-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/savvycal-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/savvycal-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://savvycal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.savvycal.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/svycal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/savvycal
- group: company
  title: ''
  type: Blog
  url: https://savvycal.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://savvycal.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://savvycal.instatus.com/
- group: other
  title: ''
  type: X
  url: https://x.com/savvycal
- group: commercial
  title: ''
  type: Plans
  url: plans/savvycal-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/savvycal-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/savvycal-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/savvycal-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/savvycal-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/savvycal-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/savvycal-link-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/savvycal-webhook-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/savvycal-user-schema.json
- group: company
  title: ''
  type: BlogFeed
  url: https://savvycal.com/feed.xml
created: 2026-06-13
description: SavvyCal is a scheduling platform that provides a REST API for managing scheduling links, availability, calendar connections, overlay scheduling, and booking page customization. The API follows REST conventions, communicates in JSON, and supports both personal access tokens and OAuth 2.0 for authentication. Developers can build integrations that create and manage scheduling links, handle event bookings, configure webhooks for real-time notifications, and manage workflows. SavvyCal also offers a JavaScript embed library for embedding scheduling experiences directly into web applications.
examples:
- key_count: 14
  name: Savvycal Event Example
  slug: savvycal-event-example
- key_count: 13
  name: Savvycal Link Example
  slug: savvycal-link-example
- key_count: 7
  name: Savvycal Webhook Example
  slug: savvycal-webhook-example
finops:
- name: Savvycal Finops
  service_category: ''
  slug: savvycal-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/savvycal.png
json_schemas:
- name: Event
  property_count: 14
  slug: savvycal-event
- name: Link
  property_count: 13
  slug: savvycal-link
- name: User
  property_count: 10
  slug: savvycal-user
- name: Webhook
  property_count: 7
  slug: savvycal-webhook
jsonld:
- class_count: 44
  name: Savvycal Context
  property_count: 6
  slug: savvycal-context
layout: provider
modified: 2026-06-13
name: SavvyCal
nav: Providers
network: true
overview: 'SavvyCal publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Current User API, Events API, Scheduling Links API, and 3 more. Tagged areas include Scheduling, Calendar, Appointments, Availability, and Booking.


  The SavvyCal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SavvyCal''s developer surface includes authentication, documentation, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Savvycal Plans Pricing
  plan_count: 3
  slug: savvycal-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 2
  name: Savvycal Rate Limits
  slug: savvycal-rate-limits
rules:
- name: SavvyCal API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: savvycal-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.9
  delta: -0.7
  facets:
    commercial_clarity: 57.9
    contract_quality: 67.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 42.1
  previous_composite: 54.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/savvycal/refs/heads/main/screenshots/savvycal-2026-06-20T193443.png
security:
- kind: authentication
  name: Savvycal Authentication
  slug: savvycal-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Savvycal Domain Security
  slug: savvycal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Savvycal Vulnerability Disclosure
  slug: savvycal-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Savvycal Trust Center
  slug: savvycal-trust-center
  summary_line: SOC 2, ISO 27001
slug: savvycal
tags:
- Scheduling
- Calendar
- Appointments
- Availability
- Booking
- Meetings
- Webhooks
website: https://savvycal.com/
---
