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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 40
  human_in_the_loop: 1
  name: Convoy Agentic Access
  operation_count: 60
  slug: convoy-agentic-access
  summary_line: 60 operations · 40 acting · 1 human-in-the-loop
api_count: 11
apis:
- description: Delivery Attempt related APIs
  name: Convoy Delivery Attempts API
  slug: convoy-delivery-attempts-api
- description: Endpoint related APIs
  name: Convoy Endpoints API
  slug: convoy-endpoints-api
- description: EventDelivery related APIs
  name: Convoy Event Deliveries API
  slug: convoy-event-deliveries-api
- description: Event related APIs
  name: Convoy Events API
  slug: convoy-events-api
- description: Event Types related APIs
  name: Convoy EventTypes API
  slug: convoy-eventtypes-api
- description: Filters related APIs
  name: Convoy Filters API
  slug: convoy-filters-api
- description: Meta Events related APIs
  name: Convoy Meta Events API
  slug: convoy-meta-events-api
- description: Onboard related APIs
  name: Convoy Onboard API
  slug: convoy-onboard-api
- description: Portal Links related APIs
  name: Convoy Portal Links API
  slug: convoy-portal-links-api
- description: Source related APIs
  name: Convoy Sources API
  slug: convoy-sources-api
- description: Subscription related APIs
  name: Convoy Subscriptions API
  slug: convoy-subscriptions-api
arazzos:
- description: Create a subscription, attach a body-matching filter, and confirm the filter list.
  name: Convoy Attach Filter to Subscription
  slug: convoy-attach-filter-to-subscription-workflow
- description: Detect failed deliveries for an endpoint and batch retry them in one call.
  name: Convoy Batch Retry Failed Deliveries
  slug: convoy-batch-retry-failed-deliveries-workflow
- description: Broadcast an event to all matching subscriptions and trace the resulting event.
  name: Convoy Broadcast Event and Track
  slug: convoy-broadcast-event-and-track-workflow
- description: Publish an event to an endpoint, find its delivery, and read the delivery attempts.
  name: Convoy Create Event and Trace Delivery
  slug: convoy-create-event-and-trace-delivery-workflow
- description: Define a project event type, create an endpoint, and subscribe filtered to that type.
  name: Convoy Define Event Type and Subscribe
  slug: convoy-define-event-type-and-subscribe-workflow
- description: Confirm endpoints exist for an owner, fan out an event to them, and verify it landed.
  name: Convoy Fan Out Event to Owner
  slug: convoy-fanout-event-to-owner-workflow
- description: Find a recent successful delivery for an endpoint and force resend it by ID.
  name: Convoy Force Resend Successful Deliveries
  slug: convoy-force-resend-deliveries-workflow
- description: Retrieve an event delivery, list its attempts, and drill into a single attempt.
  name: Convoy Inspect Delivery Attempts
  slug: convoy-inspect-delivery-attempts-workflow
- description: Stand up a webhook endpoint, subscribe it, send a first event, and confirm delivery.
  name: Convoy Provision Endpoint and Subscription
  slug: convoy-provision-endpoint-subscription-workflow
- description: Create an HMAC-verified incoming source and subscribe it to an endpoint.
  name: Convoy Register Incoming Source
  slug: convoy-register-incoming-source-workflow
- description: Pick a recent event, replay it as a fresh event, and trace the new deliveries.
  name: Convoy Replay Event
  slug: convoy-replay-event-workflow
- description: Find a failed event delivery, retry it, and inspect the resulting delivery attempts.
  name: Convoy Retry a Failed Delivery
  slug: convoy-retry-failed-delivery-workflow
artifact_total: 128
collections:
- collection_type: postman
  name: Convoy API Reference
  slug: postman-convoy
- collection_type: open
  name: Convoy API Reference
  slug: open-convoy
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/frain-dev/convoy/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/frain-dev/convoy/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/frain-dev/convoy/blob/main/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/convoy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/convoy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/convoy-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/convoy/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/convoy-attach-filter-to-subscription-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/convoy-batch-retry-failed-deliveries-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/convoy-broadcast-event-and-track-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/convoy-create-event-and-trace-delivery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/convoy-define-event-type-and-subscribe-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/convoy-fanout-event-to-owner-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/convoy-force-resend-deliveries-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/convoy-inspect-delivery-attempts-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/convoy-provision-endpoint-subscription-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/convoy-register-incoming-source-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/convoy-replay-event-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/convoy-retry-failed-delivery-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://getconvoy.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://getconvoy.io/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://getconvoy.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://getconvoy.io/docs/api-reference/welcome
- group: start
  title: ''
  type: GettingStarted
  url: https://getconvoy.io/docs/quickstart
- group: start
  title: ''
  type: Signup
  url: https://dashboard.getconvoy.io/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.getconvoy.io/login
- group: commercial
  title: ''
  type: Pricing
  url: https://getconvoy.io/pricing
- group: commercial
  title: ''
  type: Plans
  url: ./plans/convoy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: ./rate-limits/convoy-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://getconvoy.io/changelog
- group: company
  title: ''
  type: Blog
  url: https://getconvoy.io/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getconvoy.io
- group: auth
  title: ''
  type: Security
  url: https://getconvoy.io/docs/product-manual/signatures
- group: auth
  title: ''
  type: Compliance
  url: https://getconvoy.io/pricing
- group: operate
  title: ''
  type: Support
  url: mailto:support@getconvoy.io
- group: operate
  title: ''
  type: Contact
  url: https://getconvoy.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/frain-dev
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/frain-dev/convoy
- group: build
  title: ''
  type: SDKs
  url: https://github.com/frain-dev/convoy-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/frain-dev/convoy.js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/frain-dev/convoy-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/frain-dev/convoy-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/frain-dev/convoy.rb
- group: build
  title: ''
  type: CLI
  url: https://github.com/frain-dev/convoy-cli
- group: build
  title: ''
  type: CLI
  url: https://github.com/frain-dev/homebrew-tools
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/frain-dev/convoy-playground
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/frain-dev/webhooks-with-kafka-demo
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/frain-dev/convoy-paystack
- group: other
  title: ''
  type: Regions
  url: ''
- group: other
  title: ''
  type: Customers
  url: ''
- group: agent
  title: ''
  type: LlmsText
  url: https://eu.getconvoy.cloud/llms.txt
created: '2026-05-22'
description: Convoy is an open-source, cloud-native webhooks gateway used to securely ingest, persist, debug, deliver, and manage events. It positions itself as "the complete solution for secure, scalable, and reliable webhook delivery," covering both outbound (sending) and inbound (receiving) webhooks with retries, payload signing, fan-out, rate limiting, message broker ingestion, and customer-facing portals. Convoy is offered as a self-hosted open-source project (Elastic License v2.0, with the OpenAPI spec under MPL 2.0) and a fully managed cloud service in US and EU regions.
examples:
- key_count: 14
  name: Convoy Delivery Attempt Example
  slug: convoy-delivery-attempt-example
- key_count: 15
  name: Convoy Endpoint Example
  slug: convoy-endpoint-example
- key_count: 9
  name: Convoy Event Delivery Example
  slug: convoy-event-delivery-example
- key_count: 8
  name: Convoy Event Example
  slug: convoy-event-example
- key_count: 8
  name: Convoy Event Type Example
  slug: convoy-event-type-example
- key_count: 4
  name: Convoy Op Activateendpoint Example
  slug: convoy-op-activateendpoint-example
- key_count: 4
  name: Convoy Op Batchreplayevents Example
  slug: convoy-op-batchreplayevents-example
- key_count: 4
  name: Convoy Op Batchretryeventdelivery Example
  slug: convoy-op-batchretryeventdelivery-example
- key_count: 4
  name: Convoy Op Bulkcreatefilters Example
  slug: convoy-op-bulkcreatefilters-example
- key_count: 4
  name: Convoy Op Bulkonboard Example
  slug: convoy-op-bulkonboard-example
- key_count: 4
  name: Convoy Op Bulkupdatefilters Example
  slug: convoy-op-bulkupdatefilters-example
- key_count: 4
  name: Convoy Op Createbroadcastevent Example
  slug: convoy-op-createbroadcastevent-example
- key_count: 4
  name: Convoy Op Createdynamicevent Example
  slug: convoy-op-createdynamicevent-example
- key_count: 4
  name: Convoy Op Createendpoint Example
  slug: convoy-op-createendpoint-example
- key_count: 4
  name: Convoy Op Createendpointevent Example
  slug: convoy-op-createendpointevent-example
- key_count: 4
  name: Convoy Op Createendpointfanoutevent Example
  slug: convoy-op-createendpointfanoutevent-example
- key_count: 4
  name: Convoy Op Createeventtype Example
  slug: convoy-op-createeventtype-example
- key_count: 4
  name: Convoy Op Createfilter Example
  slug: convoy-op-createfilter-example
- key_count: 4
  name: Convoy Op Createportallink Example
  slug: convoy-op-createportallink-example
- key_count: 4
  name: Convoy Op Createsource Example
  slug: convoy-op-createsource-example
- key_count: 4
  name: Convoy Op Createsubscription Example
  slug: convoy-op-createsubscription-example
- key_count: 4
  name: Convoy Op Deleteendpoint Example
  slug: convoy-op-deleteendpoint-example
- key_count: 4
  name: Convoy Op Deletefilter Example
  slug: convoy-op-deletefilter-example
- key_count: 4
  name: Convoy Op Deletesource Example
  slug: convoy-op-deletesource-example
- key_count: 4
  name: Convoy Op Deletesubscription Example
  slug: convoy-op-deletesubscription-example
- key_count: 4
  name: Convoy Op Deprecateeventtype Example
  slug: convoy-op-deprecateeventtype-example
- key_count: 4
  name: Convoy Op Expiresecret Example
  slug: convoy-op-expiresecret-example
- key_count: 4
  name: Convoy Op Forceresendeventdeliveries Example
  slug: convoy-op-forceresendeventdeliveries-example
- key_count: 4
  name: Convoy Op Getdeliveryattempt Example
  slug: convoy-op-getdeliveryattempt-example
- key_count: 4
  name: Convoy Op Getdeliveryattempts Example
  slug: convoy-op-getdeliveryattempts-example
- key_count: 4
  name: Convoy Op Getendpoint Example
  slug: convoy-op-getendpoint-example
- key_count: 4
  name: Convoy Op Getendpointevent Example
  slug: convoy-op-getendpointevent-example
- key_count: 4
  name: Convoy Op Getendpoints Example
  slug: convoy-op-getendpoints-example
- key_count: 4
  name: Convoy Op Geteventdeliveriespaged Example
  slug: convoy-op-geteventdeliveriespaged-example
- key_count: 4
  name: Convoy Op Geteventdelivery Example
  slug: convoy-op-geteventdelivery-example
- key_count: 4
  name: Convoy Op Geteventspaged Example
  slug: convoy-op-geteventspaged-example
- key_count: 4
  name: Convoy Op Geteventtypes Example
  slug: convoy-op-geteventtypes-example
- key_count: 4
  name: Convoy Op Getfilter Example
  slug: convoy-op-getfilter-example
- key_count: 4
  name: Convoy Op Getfilters Example
  slug: convoy-op-getfilters-example
- key_count: 4
  name: Convoy Op Getmetaevent Example
  slug: convoy-op-getmetaevent-example
- key_count: 4
  name: Convoy Op Getmetaeventspaged Example
  slug: convoy-op-getmetaeventspaged-example
- key_count: 4
  name: Convoy Op Getportallink Example
  slug: convoy-op-getportallink-example
- key_count: 4
  name: Convoy Op Getsource Example
  slug: convoy-op-getsource-example
- key_count: 4
  name: Convoy Op Getsubscription Example
  slug: convoy-op-getsubscription-example
- key_count: 4
  name: Convoy Op Getsubscriptions Example
  slug: convoy-op-getsubscriptions-example
- key_count: 4
  name: Convoy Op Importopenapispec Example
  slug: convoy-op-importopenapispec-example
- key_count: 4
  name: Convoy Op Loadportallinkspaged Example
  slug: convoy-op-loadportallinkspaged-example
- key_count: 4
  name: Convoy Op Loadsourcespaged Example
  slug: convoy-op-loadsourcespaged-example
- key_count: 4
  name: Convoy Op Pauseendpoint Example
  slug: convoy-op-pauseendpoint-example
- key_count: 4
  name: Convoy Op Post V1 Projects Projectid Sources Test Function Example
  slug: convoy-op-post-v1-projects-projectid-sources-test-function-example
- key_count: 4
  name: Convoy Op Refreshportallinkauthtoken Example
  slug: convoy-op-refreshportallinkauthtoken-example
- key_count: 4
  name: Convoy Op Replayendpointevent Example
  slug: convoy-op-replayendpointevent-example
- key_count: 4
  name: Convoy Op Resendeventdelivery Example
  slug: convoy-op-resendeventdelivery-example
- key_count: 4
  name: Convoy Op Resendmetaevent Example
  slug: convoy-op-resendmetaevent-example
- key_count: 4
  name: Convoy Op Revokeportallink Example
  slug: convoy-op-revokeportallink-example
- key_count: 4
  name: Convoy Op Testfilter Example
  slug: convoy-op-testfilter-example
- key_count: 4
  name: Convoy Op Testoauth2Connection Example
  slug: convoy-op-testoauth2connection-example
- key_count: 4
  name: Convoy Op Testsubscriptionfilter Example
  slug: convoy-op-testsubscriptionfilter-example
- key_count: 4
  name: Convoy Op Testsubscriptionfunction Example
  slug: convoy-op-testsubscriptionfunction-example
- key_count: 4
  name: Convoy Op Updateendpoint Example
  slug: convoy-op-updateendpoint-example
- key_count: 4
  name: Convoy Op Updateeventtype Example
  slug: convoy-op-updateeventtype-example
- key_count: 4
  name: Convoy Op Updatefilter Example
  slug: convoy-op-updatefilter-example
- key_count: 4
  name: Convoy Op Updateportallink Example
  slug: convoy-op-updateportallink-example
- key_count: 4
  name: Convoy Op Updatesource Example
  slug: convoy-op-updatesource-example
- key_count: 4
  name: Convoy Op Updatesubscription Example
  slug: convoy-op-updatesubscription-example
- key_count: 11
  name: Convoy Portal Link Example
  slug: convoy-portal-link-example
- key_count: 9
  name: Convoy Source Example
  slug: convoy-source-example
- key_count: 11
  name: Convoy Subscription Example
  slug: convoy-subscription-example
features:
- GitHub
- Shopify
- Twitter/X
- Mono
- Generic HTTP (HMAC, Basic Auth, API Key, or Custom verification)
finops:
- name: Convoy Finops
  service_category: ''
  slug: convoy-finops
image: https://avatars.githubusercontent.com/u/64033435?s=200&v=4
json_schemas:
- name: Convoy DeliveryAttempt
  property_count: 17
  slug: convoy-delivery-attempt
- name: Convoy Endpoint
  property_count: 22
  slug: convoy-endpoint
- name: Convoy EventDelivery
  property_count: 25
  slug: convoy-event-delivery
- name: Convoy Event
  property_count: 20
  slug: convoy-event
- name: Convoy EventType
  property_count: 6
  slug: convoy-event-type
- name: Convoy PortalLink
  property_count: 15
  slug: convoy-portal-link
- name: Convoy Source
  property_count: 19
  slug: convoy-source
- name: Convoy Subscription
  property_count: 16
  slug: convoy-subscription
json_structures:
- name: Convoy Delivery Attempt Structure
  property_count: 17
  slug: convoy-delivery-attempt-structure
- name: Convoy Endpoint Structure
  property_count: 22
  slug: convoy-endpoint-structure
- name: Convoy Event Delivery Structure
  property_count: 25
  slug: convoy-event-delivery-structure
- name: Convoy Event Structure
  property_count: 20
  slug: convoy-event-structure
- name: Convoy Event Type Structure
  property_count: 6
  slug: convoy-event-type-structure
- name: Convoy Portal Link Structure
  property_count: 15
  slug: convoy-portal-link-structure
- name: Convoy Source Structure
  property_count: 19
  slug: convoy-source-structure
- name: Convoy Subscription Structure
  property_count: 16
  slug: convoy-subscription-structure
jsonld:
- class_count: 48
  name: Convoy Context
  property_count: 10
  slug: convoy-context
layout: provider
modified: '2026-05-22'
name: Convoy
nav: Providers
network: true
overview: 'Convoy publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Delivery Attempts API, Endpoints API, Event Deliveries API, and 8 more. Tagged areas include Webhooks, Webhook Gateway, Event Delivery, Eventing, and Messaging.


  The Convoy catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Convoy''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, signup flow, pricing, and 42 more developer resources.'
plans:
- name: Convoy Plans Pricing
  plan_count: 3
  slug: convoy-plans-pricing
random_paper: 90
rate_limits:
- limit_count: 2
  name: Convoy Rate Limits
  slug: convoy-rate-limits
rules:
- name: Convoy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: convoy-jsonschema-spectral-rules
- name: Convoy API Rules
  rule_count: 14
  severity_counts:
    error: 6
    hint: 3
    info: 0
    warn: 5
  slug: convoy-rules
score:
  band: exemplar
  composite: 72.6
  delta: 6.3
  facets:
    commercial_clarity: 71.1
    contract_quality: 77.0
    developer_ergonomics: 78.3
    discoverability: 75.9
    governance: 58.3
    operational_transparency: 68.4
  previous_composite: 66.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/convoy/refs/heads/main/screenshots/convoy-2026-06-20T175006.png
security:
- kind: authentication
  name: Convoy Authentication
  slug: convoy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Convoy Domain Security
  slug: convoy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: convoy
tags:
- Webhooks
- Webhook Gateway
- Event Delivery
- Eventing
- Messaging
- Integration
- API Infrastructure
use_cases:
- Webhook gateway between microservices and external consumers
- Receiving webhooks from third-party providers and routing to internal services
- Replacing in-house retry/signing/observability code for webhooks
- Customer-facing webhook dashboards via embeddable portal links
- Bridging message brokers to HTTP endpoints
website: https://getconvoy.io/docs/
---
