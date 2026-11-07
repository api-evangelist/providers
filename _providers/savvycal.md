---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Savvycal Agentic Access
  operation_count: 16
  slug: savvycal-agentic-access
  summary_line: 16 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.savvycal.com/v1
  baseurl_source: declared
  description: Retrieve information about the authenticated user.
  name: SavvyCal Current User API
  slug: savvycal-current-user-api
- baseURL: https://api.savvycal.com/v1
  baseurl_source: declared
  description: Manage scheduled events and bookings.
  name: SavvyCal Events API
  slug: savvycal-events-api
- baseURL: https://api.savvycal.com/v1
  baseurl_source: declared
  description: Create and manage scheduling links for booking.
  name: SavvyCal Scheduling Links API
  slug: savvycal-scheduling-links-api
- baseURL: https://api.savvycal.com/v1
  baseurl_source: declared
  description: Configure webhooks for real-time event notifications.
  name: SavvyCal Webhooks API
  slug: savvycal-webhooks-api
- baseURL: https://api.savvycal.com/v1
  baseurl_source: declared
  description: Manage automation workflows.
  name: SavvyCal Workflows API
  slug: savvycal-workflows-api
- baseURL: https://api.savvycal.com/v1
  baseurl_source: declared
  description: List and retrieve time zone information.
  name: SavvyCal Timezones API
  slug: savvycal-timezones-api
artifact_total: 30
collections:
- collection_type: open
  name: SavvyCal Meetings Current User API
  slug: open-savvycal-current-user-api
- collection_type: open
  name: SavvyCal Meetings Current User Events API
  slug: open-savvycal-events-api
- collection_type: open
  name: SavvyCal Meetings Current User Scheduling Links API
  slug: open-savvycal-scheduling-links-api
- collection_type: open
  name: SavvyCal Meetings Current User Time Zones API
  slug: open-savvycal-time-zones-api
- collection_type: open
  name: SavvyCal Meetings Current User Webhooks API
  slug: open-savvycal-webhooks-api
- collection_type: open
  name: SavvyCal Meetings Current User Workflows API
  slug: open-savvycal-workflows-api
common:
- group: other
  href: https://artifacts.apis.io/savvycal/capabilities/savvycal-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/savvycal-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/savvycal/agentic-access/savvycal-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/savvycal-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/savvycal/security/savvycal-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/savvycal-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/savvycal/security/savvycal-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/savvycal-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/savvycal/security/savvycal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/savvycal-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/savvycal/authentication/savvycal-authentication.yml
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
  href: https://artifacts.apis.io/savvycal/plans/savvycal-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/savvycal-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/savvycal/rate-limits/savvycal-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/savvycal-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/savvycal/finops/savvycal-finops.yml
  title: ''
  type: FinOps
  url: finops/savvycal-finops.yml
- group: design
  href: https://artifacts.apis.io/savvycal/vocabulary/savvycal-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/savvycal-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/savvycal/json-ld/savvycal-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/savvycal-context.jsonld
- group: docs
  href: https://artifacts.apis.io/savvycal/json-schema/savvycal-event-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/savvycal-event-schema.json
- group: docs
  href: https://artifacts.apis.io/savvycal/json-schema/savvycal-link-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/savvycal-link-schema.json
- group: docs
  href: https://artifacts.apis.io/savvycal/json-schema/savvycal-webhook-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/savvycal-webhook-schema.json
- group: docs
  href: https://artifacts.apis.io/savvycal/json-schema/savvycal-user-schema.json
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
- has_sources: false
  method: generated
  name: Savvycal Finops
  primary_unit: ''
  service_category: ''
  slug: savvycal-finops
  template: true
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
mcp_servers:
- description: Remote MCP server at savvycal.com over HTTP.
  name: SavvyCal MCP Server
  slug: savvycal
modified: 2026-06-13
name: SavvyCal
nav: Providers
network: true
overview: 'SavvyCal publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Current User API, Events API, Scheduling Links API, and 3 more. Tagged areas include Scheduling, Calendar, Appointments, Availability, and Booking.


  The SavvyCal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SavvyCal''s developer surface includes authentication, documentation, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Savvycal Plans Pricing
  plan_count: 3
  slug: savvycal-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Savvycal Rate Limits
  slug: savvycal-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: SavvyCal — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: savvycal-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 23.5
    contract_quality: 57.1
    developer_ergonomics: 21.4
    discoverability: 68.3
    operational_transparency: 21.1
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/savvycal/savvycal-2026-06-20T193443.png
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
- Webhook
website: https://savvycal.com/
---
