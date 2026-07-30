---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Cdk Global Agentic Access
  operation_count: 25
  slug: cdk-global-agentic-access
  summary_line: 25 operations · 12 acting
api_count: 13
apis:
- description: Fortellis is CDK Global's open automotive commerce platform — an API gateway, app marketplace, and developer community that brokers data flow between dealerships, ISVs, OEMs, heavy-truck, and powerspo
  name: Fortellis Platform
  slug: fortellis-platform
- description: AsyncAPI specification for the Fortellis Event Relay data-plane proxy used by event sources to publish events into Fortellis for fan-out to subscribers.
  name: Fortellis Event Relay Data Plane Proxy (AsyncAPI)
  slug: fortellis-event-relay-data-plane
- description: Hello World AsyncAPI reference distributed by Fortellis to teach the asynchronous API pattern, channel topology, and message envelope conventions used across Fortellis event APIs.
  name: Fortellis AsyncAPI Hello World Reference
  slug: fortellis-async-hello-world
- description: The adopt API from CDK Global — 2 operation(s) for adopt.
  name: CDK Global adopt API
  slug: cdk-global-adopt-api
- description: The adopt delete API from CDK Global — 1 operation(s) for adopt delete.
  name: CDK Global adopt delete API
  slug: cdk-global-adopt-delete-api
- description: The adopt update API from CDK Global — 1 operation(s) for adopt update.
  name: CDK Global adopt update API
  slug: cdk-global-adopt-update-api
- description: The cancel API from CDK Global — 1 operation(s) for cancel.
  name: CDK Global cancel API
  slug: cdk-global-cancel-api
- description: The create API from CDK Global — 1 operation(s) for create.
  name: CDK Global create API
  slug: cdk-global-create-api
- description: The events API from CDK Global — 1 operation(s) for events.
  name: CDK Global events API
  slug: cdk-global-events-api
- description: The manage API from CDK Global — 1 operation(s) for manage.
  name: CDK Global manage API
  slug: cdk-global-manage-api
- description: The query API from CDK Global — 6 operation(s) for query.
  name: CDK Global query API
  slug: cdk-global-query-api
- description: The Service Booking API from CDK Global — 6 operation(s) for service booking.
  name: CDK Global Service Booking API
  slug: cdk-global-service-booking-api
- description: The update API from CDK Global — 1 operation(s) for update.
  name: CDK Global update API
  slug: cdk-global-update-api
arazzos:
- description: Create a booking session, add a requested service item, and read it back.
  name: CDK Global Add Service Session Item
  slug: cdk-global-add-service-session-item-workflow
- description: Create a booking session, discover an available store and slot, and book it.
  name: CDK Global Book Service Session
  slug: cdk-global-book-service-session-workflow
- description: Find a customer's appointment, confirm it exists, then cancel it with a reason.
  name: CDK Global Cancel Service Appointment
  slug: cdk-global-cancel-appointment-workflow
- description: Add a record to the data domain store and read it back by its identifier.
  name: CDK Global Create Data Record
  slug: cdk-global-create-data-record-workflow
- description: List a store's open slots and pull the full detail of the first slot.
  name: CDK Global Inspect Available Slot
  slug: cdk-global-inspect-available-slot-workflow
- description: Health-check the parts store, then look up a product only when it is up.
  name: CDK Global Parts Availability Check
  slug: cdk-global-parts-availability-check-workflow
- description: List parts inventory, pull a product's detail, then read its size.
  name: CDK Global Parts Inventory Lookup
  slug: cdk-global-parts-inventory-lookup-workflow
- description: Read a service appointment, then relay it as an event to an event sink.
  name: CDK Global Relay Appointment Event
  slug: cdk-global-relay-appointment-event-workflow
- description: Confirm a booking session item exists, then remove it from the session.
  name: CDK Global Remove Service Session Item
  slug: cdk-global-remove-service-session-item-workflow
- description: Read an existing appointment, update its date/time, then confirm the change.
  name: CDK Global Reschedule Service Appointment
  slug: cdk-global-reschedule-appointment-workflow
- description: Create a service appointment for a vehicle and read it back to confirm.
  name: CDK Global Schedule Service Appointment
  slug: cdk-global-schedule-service-appointment-workflow
- description: Read a data-domain record, branch on whether it exists, then update it.
  name: CDK Global Update Data Record
  slug: cdk-global-update-data-record-workflow
- description: Create a booking session, query a requested item, and update its details.
  name: CDK Global Update Service Session Item
  slug: cdk-global-update-service-session-item-workflow
artifact_total: 61
asyncapis:
- description: Provides an Event Source (Publisher) the ability to post event through Fortellis Event Relay.
  name: Fortellis Event Relay Data API
  slug: fortellis-event-relay-data-plane-proxy-asyncapi
- description: This is the example hellos world asynchronous API.
  name: Hello World
  slug: fortellis-hello-world-asyncapi
collections:
- collection_type: postman
  name: appointments
  slug: postman-fortellis-appointments
- collection_type: postman
  name: Fortellis Event Relay Webhook
  slug: postman-fortellis-event-relay-webhook
- collection_type: postman
  name: Fortellis Sample Application
  slug: postman-fortellis-parts-store
- collection_type: postman
  name: Pet Adoption
  slug: postman-fortellis-pet-adoption
- collection_type: postman
  name: Booking Sessions
  slug: postman-fortellis-user-service
- collection_type: open
  name: appointments
  slug: open-fortellis-appointments
- collection_type: open
  name: Fortellis Event Relay Webhook
  slug: open-fortellis-event-relay-webhook
- collection_type: open
  name: Fortellis Sample Application
  slug: open-fortellis-parts-store
- collection_type: open
  name: Pet Adoption
  slug: open-fortellis-pet-adoption
- collection_type: open
  name: Booking Sessions
  slug: open-fortellis-user-service
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cdk-global-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cdk-global-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cdk-global-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cdk-global-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cdk-global/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cdk-global-add-service-session-item-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cdk-global-book-service-session-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cdk-global-cancel-appointment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cdk-global-create-data-record-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cdk-global-inspect-available-slot-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cdk-global-parts-availability-check-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cdk-global-parts-inventory-lookup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cdk-global-relay-appointment-event-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cdk-global-remove-service-session-item-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cdk-global-reschedule-appointment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cdk-global-schedule-service-appointment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cdk-global-update-data-record-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cdk-global-update-service-session-item-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.cdkglobal.com
- group: start
  title: ''
  type: Portal
  url: https://fortellis.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fortellis.io
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.fortellis.io
- group: start
  title: ''
  type: Signup
  url: https://sso.fortellis.io
- group: other
  title: ''
  type: Marketplace
  url: https://fortellis.io/marketplace
- group: operate
  title: ''
  type: Community
  url: https://fortellis.io/community
- group: auth
  title: ''
  type: Authentication
  url: https://identity.fortellis.io/oauth2/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Fortellis
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Fortellis/fortellis-cli
- group: build
  title: ''
  type: CLI
  url: https://www.npmjs.com/package/@fortellis/fortellis-cli
- group: build
  title: ''
  type: VSCodeExtension
  url: https://github.com/Fortellis/vscode-fortellis-spec-tools
- group: build
  title: ''
  type: GitHubAction
  url: https://github.com/Fortellis/api-spec-lint-action
- group: build
  title: ''
  type: GitHubAction
  url: https://github.com/Fortellis/api-spec-push-action
- group: build
  title: ''
  type: SpecLinter
  url: https://github.com/Fortellis/fortellis-spec-linter
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Fortellis/python-admin-api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Fortellis/Admin-API-Implementation-Java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Fortellis/admin-api-implementation
- group: build
  title: ''
  type: Sample
  url: https://github.com/Fortellis/Java-Public-Webhook-Example
- group: build
  title: ''
  type: Sample
  url: https://github.com/Fortellis/AuthorizationCodeFlowInDotNet
- group: build
  title: ''
  type: Sample
  url: https://github.com/Fortellis/ImplicitFlowInDotNet
- group: build
  title: ''
  type: Sample
  url: https://github.com/Fortellis/ClientCredentialsFlowIn.Net
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cdk-global
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/cdkglobal
- group: commercial
  title: ''
  type: Plans
  url: plans/cdk-global-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cdk-global-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cdk-global-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cdk-global-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/cdk-global-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/fortellis-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://fortellis.io/insights
created: '2026-05-22'
description: CDK Global is the dominant U.S. dealer management system (DMS) provider, serving roughly 15,000 automotive dealerships with software covering sales, F&I, fixed operations, parts, CRM, and digital retail. CDK was spun out of ADP in 2014 and acquired by Brookfield Business Partners in July 2022 for $8.3B (taken private). The company operates the Fortellis platform — a developer marketplace and integration hub with 135+ published APIs, 425+ marketplace apps, 82,000+ dealer integrations, and 6.7B+ API transactions per year — exposing CDK DMS data to ISVs, OEMs, and third-party automotive systems. CDK suffered a major BlackSuit ransomware attack on June 19, 2024, paying ~$25M in bitcoin to restore service over roughly two weeks; the outage caused an estimated $605M in dealer losses and triggered numerous lawsuits.
examples:
- key_count: 2
  name: Fortellis Create Appointment Example
  slug: fortellis-create-appointment-example
- key_count: 2
  name: Fortellis Create Booking Session Example
  slug: fortellis-create-booking-session-example
- key_count: 3
  name: Fortellis Event Relay Webhook Delivery Example
  slug: fortellis-event-relay-webhook-delivery-example
- key_count: 2
  name: Fortellis Get Part Info Example
  slug: fortellis-get-part-info-example
- key_count: 2
  name: Fortellis Query Appointments Example
  slug: fortellis-query-appointments-example
finops:
- name: Cdk Global Finops
  service_category: Dealer Management Software / Automotive API Platform
  slug: cdk-global-finops
image: https://avatars.githubusercontent.com/u/46600511
json_schemas:
- name: Fortellis Booking Session
  property_count: 7
  slug: fortellis-booking-session
- name: Fortellis Event
  property_count: 6
  slug: fortellis-event
- name: Fortellis Marketplace App
  property_count: 8
  slug: fortellis-marketplace-app
- name: Fortellis Part
  property_count: 8
  slug: fortellis-part
- name: Fortellis Service Appointment
  property_count: 10
  slug: fortellis-service-appointment
json_structures:
- name: Fortellis Event Structure
  property_count: 0
  slug: fortellis-event-structure
- name: Fortellis Service Appointment Structure
  property_count: 0
  slug: fortellis-service-appointment-structure
jsonld:
- class_count: 0
  name: Cdk Global Context
  property_count: 9
  slug: cdk-global-context
layout: provider
modified: '2026-05-23'
name: CDK Global
nav: Providers
network: true
overview: 'CDK Global publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Fortellis Event Relay Data Plane Proxy (AsyncAPI), Fortellis AsyncAPI Hello World Reference, adopt API, and 9 more. Tagged areas include Automotive, Dealer Management, DMS, Auto Retail, and F&I.


  The CDK Global catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 3 Spectral governance rulesets.


  CDK Global''s developer surface includes authentication, developer portal, documentation, API reference, signup flow, CLI, engineering blog, and 42 more developer resources.'
plans:
- name: Cdk Global Plans Pricing
  plan_count: 6
  slug: cdk-global-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 4
  name: Cdk Global Rate Limits
  slug: cdk-global-rate-limits
rules:
- name: CDK Global API Rules
  rule_count: 3
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 3
  slug: cdk-global-asyncapi-spectral-rules
- name: CDK Global API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cdk-global-jsonschema-spectral-rules
- name: CDK Global API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 3
    info: 0
    warn: 5
  slug: fortellis-rules
scopes:
- name: Cdk Global Scopes
  scope_count: 3
  slug: cdk-global-scopes
  summary_line: 3 scopes · implicit
score:
  band: developing
  composite: 55.3
  delta: -6.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.5
    developer_ergonomics: 67.4
    discoverability: 64.8
    governance: 62.5
    operational_transparency: 36.8
  previous_composite: 61.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/cdk-global/refs/heads/main/screenshots/cdk-global-2026-06-20T174106.png
security:
- kind: authentication
  name: Cdk Global Authentication
  slug: cdk-global-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cdk Global Domain Security
  slug: cdk-global-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cdk-global
tags:
- Automotive
- Dealer Management
- DMS
- Auto Retail
- F&I
- Fixed Operations
- Parts
- CRM
- Digital Retail
- Marketplace
- Developer Platform
- Events
- Webhooks
- AsyncAPI
website: https://www.cdkglobal.com
---
