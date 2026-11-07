---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 40
  human_in_the_loop: 1
  name: Convoy Agentic Access
  operation_count: 60
  slug: convoy-agentic-access
  summary_line: 60 operations · 40 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://us.getconvoy.cloud/api
  baseurl_source: declared
  description: Delivery Attempt related APIs
  name: Convoy Delivery Attempts API
  phrasing_intents:
  - id: GetDeliveryAttempts
    intent: List the delivery attempts for an event delivery
    question: How do I see every attempt Convoy made to deliver one webhook?
  - id: GetDeliveryAttempt
    intent: Retrieve a single delivery attempt
    question: Where can I see the request and response details of one specific webhook delivery attempt?
  phrasing_ops: 2
  slug: convoy-delivery-attempts-api
- baseURL: https://us.getconvoy.cloud/api
  baseurl_source: declared
  description: Endpoint related APIs
  name: Convoy Endpoints API
  phrasing_intents:
  - id: GetEndpoints
    intent: List webhook endpoints in a project
    question: Which webhook endpoints are registered in my Convoy project?
  - id: CreateEndpoint
    intent: Register a new webhook endpoint
    question: How do I add a new HTTPS URL that should receive my webhooks?
  - id: TestOAuth2Connection
    intent: Test an endpoint's OAuth2 token exchange
    question: Can I check that my OAuth2 client credentials work before attaching them to an endpoint?
  - id: DeleteEndpoint
    intent: Delete a webhook endpoint
    question: How do I permanently remove an endpoint that no longer needs webhooks?
  - id: GetEndpoint
    intent: Retrieve a webhook endpoint's details
    question: How do I look up the configuration of one specific endpoint?
  - id: UpdateEndpoint
    intent: Update an existing webhook endpoint
    question: Can I change the URL an existing endpoint delivers webhooks to?
  - id: ActivateEndpoint
    intent: Reactivate an inactive endpoint
    question: An endpoint was marked inactive after failures, how do I turn it back on?
  - id: ExpireSecret
    intent: Roll an endpoint's signing secret
    question: How do I rotate the webhook signing secret for an endpoint?
  phrasing_ops: 9
  slug: convoy-endpoints-api
- baseURL: https://us.getconvoy.cloud/api
  baseurl_source: declared
  description: EventDelivery related APIs
  name: Convoy Event Deliveries API
  phrasing_intents:
  - id: GetEventDeliveriesPaged
    intent: List event deliveries with filters
    question: Which webhook deliveries failed in my project over the last day?
  - id: BatchRetryEventDelivery
    intent: Retry many event deliveries at once
    question: Can I retry every failed delivery to an endpoint in one go?
  - id: ForceResendEventDeliveries
    intent: Force resend deliveries that already succeeded
    question: Can I resend a webhook that was already delivered successfully?
  - id: GetEventDelivery
    intent: Retrieve an event delivery
    question: What is the current status of one particular webhook delivery?
  - id: ResendEventDelivery
    intent: Retry a single event delivery
    question: How do I retry just one failed webhook delivery?
  phrasing_ops: 5
  slug: convoy-event-deliveries-api
- baseURL: https://us.getconvoy.cloud/api
  baseurl_source: declared
  description: Event related APIs
  name: Convoy Events API
  phrasing_intents:
  - id: GetEventsPaged
    intent: List events sent through a project
    question: Which events has my project sent in the past week?
  - id: CreateEndpointEvent
    intent: Send an event to one endpoint
    question: How do I send a webhook event to a single specific endpoint?
  - id: BatchReplayEvents
    intent: Replay many events at once
    question: Can I replay all the events from a date range after an outage?
  - id: CreateBroadcastEvent
    intent: Broadcast an event to all subscribed endpoints
    question: How do I send one event to every endpoint subscribed to its event type?
  - id: CreateDynamicEvent
    intent: Send an event to a URL without setup
    question: Can I send a webhook to a URL without creating an endpoint and subscription first?
  - id: CreateEndpointFanoutEvent
    intent: Fan out an event to an owner's endpoints
    question: How do I send one event to all endpoints that share an owner ID?
  - id: GetEndpointEvent
    intent: Retrieve an event
    question: Where can I see the payload and type of one event I sent?
  - id: ReplayEndpointEvent
    intent: Replay a single event as new
    question: How do I replay one event as if it were brand new?
  phrasing_ops: 8
  slug: convoy-events-api
- baseURL: https://us.getconvoy.cloud/api
  baseurl_source: declared
  description: Filters related APIs
  name: Convoy Filters API
  phrasing_intents:
  - id: GetFilters
    intent: List a subscription's filters
    question: Which filters are attached to a subscription?
  - id: CreateFilter
    intent: Add a filter to a subscription
    question: How do I make a subscription only receive events whose body matches certain values?
  - id: BulkCreateFilters
    intent: Create several subscription filters at once
    question: Can I add filters for many event types to a subscription in one request?
  - id: BulkUpdateFilters
    intent: Update several subscription filters at once
    question: Can I change many of a subscription's filters in a single call?
  - id: TestFilter
    intent: Test a subscription filter against a payload
    question: Would a sample payload pass the filter on my subscription for a given event type?
  - id: DeleteFilter
    intent: Delete a subscription filter
    question: How do I remove a filter so the subscription stops screening events by it?
  - id: GetFilter
    intent: Retrieve a single subscription filter
    question: What matching criteria does one specific filter use?
  - id: UpdateFilter
    intent: Update a single subscription filter
    question: How do I change the body matching rules on an existing filter?
  phrasing_ops: 8
  slug: convoy-filters-api
- baseURL: https://us.getconvoy.cloud/api
  baseurl_source: declared
  description: Meta Events related APIs
  name: Convoy Meta Events API
  phrasing_intents:
  - id: GetMetaEventsPaged
    intent: List a project's meta events
    question: Which meta events about my Convoy project's own activity were sent recently?
  - id: GetMetaEvent
    intent: Retrieve a meta event
    question: Where do I see the details of one meta event?
  - id: ResendMetaEvent
    intent: Retry a meta event
    question: How do I retry a meta event that failed to deliver?
  phrasing_ops: 3
  slug: convoy-meta-events-api
- baseURL: https://us.getconvoy.cloud/api
  baseurl_source: declared
  description: Onboard related APIs
  name: Convoy Onboard API
  phrasing_intents:
  - id: BulkOnboard
    intent: Bulk onboard endpoints with subscriptions
    question: Can I create many endpoints and their subscriptions from a CSV file?
  phrasing_ops: 1
  slug: convoy-onboard-api
- baseURL: https://us.getconvoy.cloud/api
  baseurl_source: declared
  description: Portal Links related APIs
  name: Convoy Portal Links API
  phrasing_intents:
  - id: LoadPortalLinksPaged
    intent: List customer portal links
    question: Which customer portal links have I created in my project?
  - id: CreatePortalLink
    intent: Create a customer portal link
    question: How do I give a customer a portal where they can see their own webhooks?
  - id: GetPortalLink
    intent: Retrieve a portal link
    question: Where can I see the URL and settings of one portal link?
  - id: UpdatePortalLink
    intent: Update a portal link
    question: How do I rename an existing portal link or point it at a different owner?
  - id: RefreshPortalLinkAuthToken
    intent: Get a portal link auth token
    question: How do I get a fresh auth token for a customer portal link?
  - id: RevokePortalLink
    intent: Revoke a portal link
    question: How do I cut off a customer's access to their webhook portal?
  phrasing_ops: 6
  slug: convoy-portal-links-api
- baseURL: https://us.getconvoy.cloud/api
  baseurl_source: declared
  description: Source related APIs
  name: Convoy Sources API
  phrasing_intents:
  - id: LoadSourcesPaged
    intent: List event sources
    question: Which sources are ingesting webhooks into my project?
  - id: CreateSource
    intent: Create an event source
    question: How do I set up a source to receive incoming webhooks from a third party?
  - id: DeleteSource
    intent: Delete an event source
    question: How do I permanently remove a source I no longer ingest from?
  - id: GetSource
    intent: Retrieve an event source
    question: Where can I see the ingest URL and verifier of one source?
  - id: UpdateSource
    intent: Update an event source
    question: How do I disable an existing source temporarily?
  phrasing_ops: 5
  slug: convoy-sources-api
- baseURL: https://us.getconvoy.cloud/api
  baseurl_source: declared
  description: Subscription related APIs
  name: Convoy Subscriptions API
  phrasing_intents:
  - id: postV1ProjectsByProjectIDSourcesTestFunction
    intent: Test a source's transform function on a payload
    question: Can I dry-run the function attached to an incoming source before I save that source?
  - id: GetSubscriptions
    intent: List subscriptions
    question: Which subscriptions route events to my endpoints?
  - id: CreateSubscription
    intent: Subscribe an endpoint to events
    question: How do I connect an endpoint so it starts receiving events?
  - id: TestSubscriptionFilter
    intent: Validate a filter schema against a sample request
    question: Before saving a subscription, would my filter schema match this request?
  - id: TestSubscriptionFunction
    intent: Test a payload transform function
    question: Can I try my JavaScript transform function on a sample payload first?
  - id: DeleteSubscription
    intent: Delete a subscription
    question: How do I stop an endpoint from receiving events by removing its subscription?
  - id: GetSubscription
    intent: Retrieve a subscription
    question: What endpoint, source and filter does one subscription use?
  - id: UpdateSubscription
    intent: Update a subscription
    question: How do I change the retry policy on an existing subscription?
  phrasing_ops: 8
  slug: convoy-subscriptions-api
- baseURL: https://us.getconvoy.cloud/api
  baseurl_source: declared
  description: Event Types related APIs
  name: Convoy Event Types API
  phrasing_intents:
  - id: GetEventTypes
    intent: List a project's event types
    question: Which event types are defined in my Convoy project?
  - id: CreateEventType
    intent: Create an event type
    question: How do I register a new event type like invoice.created?
  - id: ImportOpenApiSpec
    intent: Import event types from an OpenAPI spec
    question: Can I load all my event types from an OpenAPI document instead of creating them one by one?
  - id: UpdateEventType
    intent: Update an existing event type
    question: How do I change the JSON schema of an event type that already exists?
  - id: DeprecateEventType
    intent: Deprecate an event type
    question: How do I mark an event type as deprecated so new subscribers stop using it?
  phrasing_ops: 5
  slug: convoy-event-types-api
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
artifact_total: 140
collections:
- collection_type: postman
  name: Convoy API Reference
  slug: postman-convoy
- collection_type: open
  name: Convoy API Reference Delivery Attempts API
  slug: open-convoy-delivery-attempts-api
- collection_type: open
  name: Convoy API Reference Delivery Attempts Endpoints API
  slug: open-convoy-endpoints-api
- collection_type: open
  name: Convoy API Reference Delivery Attempts Event Deliveries API
  slug: open-convoy-event-deliveries-api
- collection_type: open
  name: Convoy API Reference Delivery Attempts Events API
  slug: open-convoy-events-api
- collection_type: open
  name: Convoy API Reference Delivery Attempts EventTypes API
  slug: open-convoy-eventtypes-api
- collection_type: open
  name: Convoy API Reference Delivery Attempts Filters API
  slug: open-convoy-filters-api
- collection_type: open
  name: Convoy API Reference Delivery Attempts Meta Events API
  slug: open-convoy-meta-events-api
- collection_type: open
  name: Convoy API Reference Delivery Attempts Onboard API
  slug: open-convoy-onboard-api
- collection_type: open
  name: Convoy API Reference Delivery Attempts Portal Links API
  slug: open-convoy-portal-links-api
- collection_type: open
  name: Convoy API Reference Delivery Attempts Sources API
  slug: open-convoy-sources-api
- collection_type: open
  name: Convoy API Reference Delivery Attempts Subscriptions API
  slug: open-convoy-subscriptions-api
- collection_type: open
  name: Convoy API Reference
  slug: open-convoy
common:
- group: commercial
  href: https://artifacts.apis.io/convoy/finops/convoy-finops.yml
  title: ''
  type: FinOps
  url: finops/convoy-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.getconvoy.io/
- group: other
  href: https://artifacts.apis.io/convoy/capabilities/convoy-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/convoy-capability-edges.yml
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
  href: https://artifacts.apis.io/convoy/agentic-access/convoy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/convoy-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/convoy/security/convoy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/convoy-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/convoy/authentication/convoy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/convoy-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/convoy/overview
- group: design
  href: https://artifacts.apis.io/convoy/arazzo/convoy-attach-filter-to-subscription-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/convoy-attach-filter-to-subscription-workflow.yml
- group: design
  href: https://artifacts.apis.io/convoy/arazzo/convoy-batch-retry-failed-deliveries-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/convoy-batch-retry-failed-deliveries-workflow.yml
- group: design
  href: https://artifacts.apis.io/convoy/arazzo/convoy-broadcast-event-and-track-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/convoy-broadcast-event-and-track-workflow.yml
- group: design
  href: https://artifacts.apis.io/convoy/arazzo/convoy-create-event-and-trace-delivery-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/convoy-create-event-and-trace-delivery-workflow.yml
- group: design
  href: https://artifacts.apis.io/convoy/arazzo/convoy-define-event-type-and-subscribe-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/convoy-define-event-type-and-subscribe-workflow.yml
- group: design
  href: https://artifacts.apis.io/convoy/arazzo/convoy-fanout-event-to-owner-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/convoy-fanout-event-to-owner-workflow.yml
- group: design
  href: https://artifacts.apis.io/convoy/arazzo/convoy-force-resend-deliveries-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/convoy-force-resend-deliveries-workflow.yml
- group: design
  href: https://artifacts.apis.io/convoy/arazzo/convoy-inspect-delivery-attempts-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/convoy-inspect-delivery-attempts-workflow.yml
- group: design
  href: https://artifacts.apis.io/convoy/arazzo/convoy-provision-endpoint-subscription-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/convoy-provision-endpoint-subscription-workflow.yml
- group: design
  href: https://artifacts.apis.io/convoy/arazzo/convoy-register-incoming-source-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/convoy-register-incoming-source-workflow.yml
- group: design
  href: https://artifacts.apis.io/convoy/arazzo/convoy-replay-event-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/convoy-replay-event-workflow.yml
- group: design
  href: https://artifacts.apis.io/convoy/arazzo/convoy-retry-failed-delivery-workflow.yml
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
  href: https://artifacts.apis.io/convoy/plans/convoy-plans-pricing.yml
  title: ''
  type: Plans
  url: ./plans/convoy-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/convoy/rate-limits/convoy-rate-limits.yml
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
- has_sources: true
  method: derived
  name: Convoy Finops
  primary_unit: subscription
  service_category: ''
  slug: convoy-finops
  template: false
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
overview: 'Convoy publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Delivery Attempts API, Endpoints API, Event Deliveries API, and 8 more. Tagged areas include Webhook, Webhook Gateway, Event Delivery, Eventing, and Messaging.


  The Convoy catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Convoy''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, signup flow, pricing, and 45 more developer resources.'
plans:
- name: Convoy Plans Pricing
  plan_count: 4
  slug: convoy-plans-pricing
- name: Convoy Price Estimates
  plan_count: 0
  slug: convoy-price-estimates
random_paper: 22
rate_limits:
- limit_count: 2
  name: Convoy Rate Limits
  slug: convoy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Convoy — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: convoy-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Convoy API Rules
  rule_count: 14
  severity_counts:
    error: 6
    hint: 3
    info: 0
    warn: 5
  slug: convoy-rules
score:
  band: exemplar
  composite: 68.5
  coverage:
    artifact_dirs: 24
    catalog_earned: 86.0
    catalog_earned_first_party: 20.0
    catalog_gap: 29.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 75.0
    contract_governance: 27.3
    contract_quality: 68.8
    developer_ergonomics: 70.2
    discoverability: 67.9
    operational_transparency: 65.8
  previous_composite: 68.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/convoy/convoy-2026-06-20T175006.png
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
- Webhook
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
website: https://www.getconvoy.io/
---
