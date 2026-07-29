---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Fullstory Agentic Access
  operation_count: 19
  slug: fullstory-agentic-access
  summary_line: 19 operations · 9 acting
api_count: 11
apis:
- description: FullStory Sessions API for retrieving session metadata, replay URLs, and session-level details.
  name: FullStory Sessions API
  slug: fullstory-sessions-api
- description: Import large volumes of users and events asynchronously using batch import jobs that support up to 50,000 records per request.
  name: FullStory Batch Import API
  slug: fullstory-batch-import-api
- description: Create, retrieve, update, and delete webhook endpoints that receive real-time notifications from FullStory. Each endpoint has a destination URL, configured event types, signing secret, and enabled sta
  name: FullStory Endpoints API
  slug: fullstory-endpoints-api
- description: List available webhook event types that can be configured for endpoints. Some event types require subcategories and may be limited by plan.
  name: FullStory Event Types API
  slug: fullstory-event-types-api
- description: Send custom server-side events to FullStory. Events can be associated with sessions and users, and include custom properties for behavioral analysis.
  name: FullStory Events API
  slug: fullstory-events-api
- description: Create and manage asynchronous export jobs for segment data, including both individual and event exports.
  name: FullStory Exports API
  slug: fullstory-exports-api
- description: Query the status of long-running asynchronous operations such as segment exports, and retrieve results when complete.
  name: FullStory Operations API
  slug: fullstory-operations-api
- description: Retrieve segment metadata including name, creator, and creation time.
  name: FullStory Segments API
  slug: fullstory-segments-api
- description: Retrieve the full set of captured events for a specific session, including page views, clicks, and custom events.
  name: FullStory Session Events API
  slug: fullstory-session-events-api
- description: Generate AI-powered summaries of sessions using configurable prompt profiles. Summaries can be customized with pre and post prompts, response schemas, and session slicing options.
  name: FullStory Session Summaries API
  slug: fullstory-session-summaries-api
- description: Create, retrieve, update, and delete users in FullStory. Users can be anonymous or identified with a uid. Custom properties can be attached to enrich user profiles.
  name: FullStory Users API
  slug: fullstory-users-api
artifact_total: 54
asyncapis:
- description: FullStory delivers real-time webhook notifications when specific events occur within the platform. Supported event types include segment creation, segment threshold alerts, custom event processing, an
  name: FullStory Webhook Events
  slug: fullstory-webhooks-asyncapi
collections:
- collection_type: open
  name: FullStory Segments Export API
  slug: open-fullstory-segments-export-api
- collection_type: open
  name: FullStory Server API
  slug: open-fullstory-server-api
- collection_type: open
  name: FullStory Sessions API
  slug: open-fullstory-sessions-api
- collection_type: open
  name: FullStory Webhooks API
  slug: open-fullstory-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fullstory-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fullstory-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fullstory-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fullstory-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fullstory-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fullstorydev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fullstory
- group: company
  title: ''
  type: Website
  url: https://www.fullstory.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fullstory.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/fullstory-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fullstory-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fullstory-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.fullstory.com/blog/
created: '2026-05-08'
description: FullStory is a behavioral data platform delivering session replay, product analytics, and digital experience intelligence across web and mobile.
finops:
- name: Fullstory Finops
  service_category: Analytics
  slug: fullstory-finops
graphqls:
- description: 'This is a conceptual GraphQL schema for the FullStory digital experience analytics platform. It is derived from the public FullStory developer documentation, covering the Server-Side API v2, Sessions '
  name: FullStory GraphQL Schema
  slug: fullstory-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fullstory.png
json_schemas:
- name: BatchEventsImportRequest
  property_count: 1
  slug: fullstory-batcheventsimportrequest
- name: BatchJob
  property_count: 3
  slug: fullstory-batchjob
- name: BatchUserImportRequest
  property_count: 1
  slug: fullstory-batchuserimportrequest
- name: CreateEndpointRequest
  property_count: 2
  slug: fullstory-createendpointrequest
- name: CreateEventRequest
  property_count: 6
  slug: fullstory-createeventrequest
- name: CreateExportRequest
  property_count: 5
  slug: fullstory-createexportrequest
- name: CreateUserRequest
  property_count: 5
  slug: fullstory-createuserrequest
- name: Endpoint
  property_count: 6
  slug: fullstory-endpoint
- name: EndpointList
  property_count: 1
  slug: fullstory-endpointlist
- name: Error
  property_count: 2
  slug: fullstory-error
- name: FullStory Event
  property_count: 6
  slug: fullstory-event
- name: EventType
  property_count: 3
  slug: fullstory-eventtype
- name: EventTypeConfig
  property_count: 2
  slug: fullstory-eventtypeconfig
- name: EventTypeList
  property_count: 1
  slug: fullstory-eventtypelist
- name: Operation
  property_count: 8
  slug: fullstory-operation
- name: FullStory Segment
  property_count: 5
  slug: fullstory-segment
- name: SegmentList
  property_count: 2
  slug: fullstory-segmentlist
- name: FullStory Session
  property_count: 3
  slug: fullstory-session
- name: SessionEvent
  property_count: 3
  slug: fullstory-sessionevent
- name: SessionEvents
  property_count: 1
  slug: fullstory-sessionevents
- name: SessionList
  property_count: 1
  slug: fullstory-sessionlist
- name: SessionSummary
  property_count: 3
  slug: fullstory-sessionsummary
- name: UpdateEndpointRequest
  property_count: 4
  slug: fullstory-updateendpointrequest
- name: FullStory User
  property_count: 8
  slug: fullstory-user
- name: FullStory Webhook Endpoint
  property_count: 6
  slug: fullstory-webhook-endpoint
json_structures:
- name: Fullstory Structure
  property_count: 0
  slug: fullstory-structure
jsonld:
- class_count: 0
  name: Fullstory Context
  property_count: 7
  slug: fullstory-context
layout: provider
modified: '2026-05-19'
name: FullStory
nav: Providers
network: true
overview: 'FullStory publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Sessions API, Batch Import API, Endpoints API, and 8 more. Tagged areas include Session Replay, Product Analytics, Digital Experience, Behavioral Analytics, and Frontend Monitoring.


  The FullStory catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  FullStory''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Fullstory Plans Pricing
  plan_count: 1
  slug: fullstory-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 1
  name: Fullstory Rate Limits
  slug: fullstory-rate-limits
rules:
- name: FullStory API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: fullstory-asyncapi-spectral-rules
- name: FullStory API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: fullstory-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.2
  delta: -2.7
  facets:
    commercial_clarity: 36.8
    contract_quality: 79.6
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 47.9
    operational_transparency: 26.3
  previous_composite: 49.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fullstory/refs/heads/main/screenshots/fullstory-2026-06-20T181612.png
security:
- kind: authentication
  name: Fullstory Authentication
  slug: fullstory-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fullstory Domain Security
  slug: fullstory-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fullstory Vulnerability Disclosure
  slug: fullstory-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Fullstory Trust Center
  slug: fullstory-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, GDPR
slug: fullstory
tags:
- Session Replay
- Product Analytics
- Digital Experience
- Behavioral Analytics
- Frontend Monitoring
website: https://www.fullstory.com/
---
