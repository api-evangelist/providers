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
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: templated
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.4
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 137
  human_in_the_loop: 1
  name: Svix Agentic Access
  operation_count: 230
  slug: svix-agentic-access
  summary_line: 230 operations · 137 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: 'The self-hostable open source Svix server (svix-webhooks repo). Smaller surface area than the hosted product (no Stream, no Ingest, no Connectors, no Background Tasks, no multi-region) — 29 paths, 46 '
  name: Svix Open Source Server API
  slug: open-source-server
- baseURL: https://api.svix.com
  baseurl_source: declared
  description: Consumer Applications are where messages are sent to. In most cases you would want to have one application for each of your users.
  name: Svix Application API
  phrasing_intents:
  - id: v1.application.list
    intent: List my applications
    question: Which applications — one per customer — exist in my Svix environment?
  - id: v1.application.create
    intent: Create an application for a customer
    question: How do I create an application to hold one customer's webhook endpoints?
  - id: v1.application.get
    intent: Get an application
    question: What name, uid and metadata does a given application have?
  - id: v1.application.update
    intent: Create or replace an application
    question: Can I upsert an application by ID so it's created if missing?
  - id: v1.application.delete
    intent: Delete an application
    question: How do I remove an application when a customer leaves?
  - id: v1.application.patch
    intent: Change some fields of an application
    question: Can I rename an application without resending its other settings?
  - id: v1.application.patch-alert-email
    intent: Set an application's alert email
    question: Where do delivery alerts for an application get emailed, and can I change it?
  - id: v1.application.count-active
    intent: Count applications with an active endpoint
    question: How many of my applications have at least one active endpoint?
  phrasing_ops: 9
  slug: svix-application-api
- baseURL: https://api.svix.com
  baseurl_source: declared
  description: Easily give your users access to our pre-built management UI.
  name: Svix Authentication API
  phrasing_intents:
  - id: v1.authentication.app-portal-access
    intent: Get a magic link to the Consumer App Portal
    question: How do I give my customer a login link to their webhook portal in Svix?
  - id: v1.authentication.whoami
    intent: Show which account the current token belongs to
    question: Which account is my current API token tied to?
  - id: v1.authentication.logout
    intent: Log out an app token
    question: How do I log out an application portal token when the session ends?
  - id: v1.authentication.expire-all
    intent: Expire every token for an application
    question: How do I revoke all portal tokens issued for one application at once?
  - id: v1.authentication.org-group-admin-token.list
    intent: List org group admin tokens
    question: What org group API tokens have been created for my organization group?
  - id: v1.authentication.org-group-admin-token.create
    intent: Create an org group admin token
    question: How do I create a token that works across my org group but not on apps or messages?
  - id: v1.authentication.org-group-admin-token.update
    intent: Rename an org group admin token
    question: How do I rename an existing org group token?
  - id: v1.authentication.org-group-admin-token.expire
    intent: Expire an org group admin token
    question: How do I revoke an org group admin token that leaked?
  phrasing_ops: 21
  slug: svix-authentication-api
- baseURL: https://api.svix.com
  baseurl_source: declared
  description: The background tasks that have been executed for your environment.
  name: Svix Background Task API
  phrasing_intents:
  - id: v1.background-task.list
    intent: List recent background tasks
    question: Which background jobs has my account run in the last 90 days?
  - id: v1.background-task.get
    intent: Check a background task's status
    question: Has my export or expunge background task finished yet?
  phrasing_ops: 2
  slug: svix-background-task-api
- baseURL: https://api.svix.com
  baseurl_source: declared
  description: Connectors allow you to connect applications to external services.
  name: Svix Connector API
  phrasing_intents:
  - id: v1.connector.list
    intent: List connectors
    question: What connectors have I built for my Svix environment?
  - id: v1.connector.create
    intent: Create a connector
    question: How do I publish a new pre-built connector that my customers can pick for their endpoints?
  - id: v1.connector.get
    intent: Get a connector
    question: What transformation and allowed event types does a specific connector have?
  - id: v1.connector.update
    intent: Create or replace a connector
    question: Can I upsert a connector so it's created if that ID doesn't exist yet?
  - id: v1.connector.delete
    intent: Delete a connector
    question: How do I remove a connector I no longer offer?
  - id: v1.connector.patch
    intent: Change some fields of a connector
    question: Can I update just a connector's logo or description?
  - id: v1.connector.options.get
    intent: Get a connector's options
    question: What options are configured on a connector?
  - id: v1.connector.options.set
    intent: Set a connector's options
    question: How do I change the options on a connector?
  phrasing_ops: 13
  slug: svix-connector-api
- baseURL: https://api.svix.com
  baseurl_source: declared
  description: Endpoints are the URLs messages will be sent to. Each application can have up to 50 endpoints and each message sent to that application will be sent to all of them (unless they are not subscribed to t
  name: Svix Endpoint API
  phrasing_intents:
  - id: v1.endpoint.list
    intent: List an application's webhook endpoints
    question: Which webhook endpoints are registered for one of my Svix applications?
  - id: v1.endpoint.create
    intent: Add a webhook endpoint to an application
    question: How do I register a new webhook URL for one of my applications?
  - id: v1.endpoint.get
    intent: Get a webhook endpoint's details
    question: What URL, filters and settings does a specific webhook endpoint have?
  - id: v1.endpoint.update
    intent: Create or replace a webhook endpoint
    question: Can I upsert an endpoint by its ID so it's created if it doesn't exist yet?
  - id: v1.endpoint.delete
    intent: Delete a webhook endpoint
    question: How do I remove a webhook endpoint a customer no longer uses?
  - id: v1.endpoint.patch
    intent: Change some settings of a webhook endpoint
    question: Can I disable an endpoint without resending its whole configuration?
  - id: v1.endpoint.get_connector
    intent: Get the connector linked to an endpoint
    question: Which connector is an endpoint built from?
  - id: v1.sink.list
    intent: List an application's sinks
    question: What sinks are set up for an application alongside its endpoints?
  phrasing_ops: 35
  slug: svix-endpoint-api
- baseURL: https://api.svix.com
  baseurl_source: declared
  description: Manage your environments like development, staging and production.
  name: Svix Environment API
  phrasing_intents:
  - id: v1.management.environment.list
    intent: List environments
    question: Which environments exist in my Svix account?
  - id: v1.management.environment.create
    intent: Create an environment
    question: How do I add a separate environment, such as a staging one?
  - id: v1.management.environment.get
    intent: Get an environment
    question: What are the name and type of a given environment?
  - id: v1.management.environment.update
    intent: Rename an environment
    question: How do I rename an environment?
  - id: v1.management.environment.delete
    intent: Delete an environment
    question: How do I delete an environment I no longer use?
  - id: v1.environment.export
    intent: Export the environment's settings and event types
    question: How do I download all my org settings and event types as a JSON file?
  - id: v1.environment.import
    intent: Import settings and event types into an environment
    question: How do I copy event types and settings from one environment into another?
  phrasing_ops: 7
  slug: svix-environment-api
- baseURL: https://api.svix.com
  baseurl_source: declared
  description: The Event API from Svix — 2 operation(s) for event.
  name: Svix Event API
  phrasing_intents:
  - id: v1.streaming.events.get
    intent: Poll events from a poller sink
    question: How do I iterate over stream events through a poller-type sink?
  - id: v1.streaming.events.create
    intent: Publish events to a stream
    question: How do I push events into a Svix stream?
  - id: v1.streaming.events.get-latest
    intent: Get a stream's most recent events
    question: What are the latest events published to my stream?
  phrasing_ops: 3
  slug: svix-event-api
- baseURL: https://api.svix.com
  baseurl_source: declared
  description: Event types are identifiers denoting the type of message being sent. Event types are primarily used to decide which events are sent to which endpoint.
  name: Svix Event Type API
  phrasing_intents:
  - id: v1.event-type.list
    intent: List webhook event types
    question: What event types have I defined for my webhooks?
  - id: v1.event-type.create
    intent: Create or unarchive an event type
    question: How do I register a new webhook event type like invoice.paid in Svix?
  - id: v1.event-type.import-openapi
    intent: Import event types from an OpenAPI spec
    question: How do I create event types from the webhooks section of my OpenAPI document?
  - id: v1.event-type.get
    intent: Get an event type
    question: What schema and description does a given event type have?
  - id: v1.event-type.update
    intent: Create or replace an event type
    question: How do I upsert an event type by name, creating it if it's missing?
  - id: v1.event-type.delete
    intent: Archive or expunge an event type
    question: How do I retire an event type so no new messages can be sent with it?
  - id: v1.event-type.patch
    intent: Partially update an event type
    question: How do I mark an existing event type as deprecated?
  - id: v1.event-type.get-retry-schedule
    intent: Get an event type's retry schedule
    question: How often are failed deliveries of a particular event type retried?
  phrasing_ops: 10
  slug: svix-event-type-api
- baseURL: https://api.svix.com
  baseurl_source: declared
  description: Health checks for the API.
  name: Svix Health API
  phrasing_intents:
  - id: v1.health.get
    intent: Check the API server is up
    question: Is the Svix API up and running right now?
  phrasing_ops: 1
  slug: svix-health-api
- baseURL: https://api.svix.com
  baseurl_source: declared
  description: Configure where Svix Ingest sends messages.
  name: Svix Ingest Endpoint API
  phrasing_intents:
  - id: v1.ingest.endpoint.list
    intent: List an ingest source's endpoints
    question: Which endpoints are forwarding webhooks from my ingest source?
  - id: v1.ingest.endpoint.create
    intent: Add an endpoint to an ingest source
    question: How do I forward incoming webhooks from an ingest source to my own URL?
  - id: v1.ingest.endpoint.get
    intent: Get an ingest endpoint
    question: What URL and settings does a particular ingest endpoint have?
  - id: v1.ingest.endpoint.update
    intent: Create or replace an ingest endpoint
    question: How do I change the destination URL of an existing ingest endpoint?
  - id: v1.ingest.endpoint.delete
    intent: Delete an ingest endpoint
    question: How do I stop an ingest source from forwarding to one of its endpoints?
  - id: v1.ingest.endpoint.get-secret
    intent: Get an ingest endpoint's signing secret
    question: Where's the secret I need to verify webhooks forwarded by an ingest endpoint?
  - id: v1.ingest.endpoint.rotate-secret
    intent: Rotate an ingest endpoint's signing secret
    question: How do I rotate the signing secret on an ingest endpoint?
  - id: v1.ingest.endpoint.get-headers
    intent: Get an ingest endpoint's extra headers
    question: What additional headers are sent when an ingest endpoint forwards a webhook?
  phrasing_ops: 11
  slug: svix-ingest-endpoint-api
- baseURL: https://api.svix.com
  baseurl_source: declared
  description: The Ingest Source API from Svix — 4 operation(s) for ingest source.
  name: Svix Ingest Source API
  phrasing_intents:
  - id: v1.ingest.source.list
    intent: List ingest sources
    question: Which ingest sources have I set up to receive incoming webhooks?
  - id: v1.ingest.source.create
    intent: Create an ingest source
    question: How do I create a source to receive webhooks from a third-party sender?
  - id: v1.ingest.source.get
    intent: Get an ingest source
    question: What is the ingest URL and configuration of a specific source?
  - id: v1.ingest.source.update
    intent: Create or replace an ingest source
    question: Can I upsert an ingest source so it's created if missing?
  - id: v1.ingest.source.delete
    intent: Delete an ingest source
    question: How do I remove an ingest source I no longer receive webhooks on?
  - id: v1.ingest.source.patch
    intent: Change some fields of an ingest source
    question: Can I rename an ingest source without replacing it?
  - id: v1.ingest.source.rotate-token
    intent: Rotate an ingest source's URL token
    question: How do I get a new ingest URL if the old one leaked?
  - id: v1.ingest.dashboard
    intent: Open the consumer portal for an ingest source
    question: How do I get a consumer portal link for an ingest source?
  phrasing_ops: 8
  slug: svix-ingest-source-api
- baseURL: https://api.svix.com
  baseurl_source: declared
  description: Integrations are services your users connect an application to. An integration can manage the application and its endpoints.
  name: Svix Integration API
  phrasing_intents:
  - id: v1.integration.list
    intent: List an application's integrations
    question: Which integrations are set up for one of my applications?
  - id: v1.integration.create
    intent: Create an integration for an application
    question: How do I add an integration to an application?
  - id: v1.integration.get
    intent: Get an integration
    question: What name and feature flags does a given integration have?
  - id: v1.integration.update
    intent: Update an integration
    question: How do I rename an integration?
  - id: v1.integration.delete
    intent: Delete an integration
    question: How do I remove an integration from an application?
  - id: v1.integration.rotate-key
    intent: Rotate an integration's key
    question: How do I replace an integration key that may have leaked?
  - id: v1.integration.get-key
    intent: Get an integration's key
    question: Where do I find the key for an integration?
  phrasing_ops: 7
  slug: svix-integration-api
- baseURL: https://api.svix.com
  baseurl_source: declared
  description: Messages are the webhook events being sent.
  name: Svix Message API
  phrasing_intents:
  - id: v1.message.list
    intent: List an application's messages
    question: How do I list the webhook messages sent for one application?
  - id: v1.message.create
    intent: Send a webhook message to an application
    question: How do I send a webhook event to all of a customer's endpoints with Svix?
  - id: v1.message.precheck
    intent: Check if any endpoint listens for an event
    question: Is any active endpoint actually listening for this event type before I send it?
  - id: v1.message.events
    intent: Read the stream of created messages for an app
    question: How do I consume the feed of messages created for an application in order?
  - id: v1.message.get
    intent: Get a message by ID or event ID
    question: How do I look up a single message I sent?
  - id: v1.message.expunge-content
    intent: Delete one message's payload
    question: I sent a message with sensitive data by mistake — how do I wipe its payload?
  - id: v1.message.search
    intent: Search an application's messages
    question: How do I search an app's messages by tag, channel and date range in one request?
  - id: v1.message.expunge-all-contents
    intent: Delete every message payload in an app
    question: How do I purge all message payloads stored for an application?
  phrasing_ops: 15
  slug: svix-message-api
- baseURL: https://api.svix.com
  baseurl_source: declared
  description: Attempts to deliver `Message`s to `Endpoint`s.
  name: Svix Message Attempt API
  phrasing_intents:
  - id: v1.message-attempt.list-by-endpoint
    intent: List delivery attempts to an endpoint
    question: What delivery attempts were made to a specific endpoint recently?
  - id: v1.message-attempt.count-by-endpoint
    intent: Count delivery attempts to an endpoint
    question: How many failed delivery attempts has an endpoint had?
  - id: v1.message-attempt.list-by-msg
    intent: List delivery attempts for a message
    question: Was a particular webhook message delivered, and how many tries did it take?
  - id: v1.message-attempt.list-attempted-messages
    intent: List messages sent to an endpoint
    question: Which messages has an endpoint been sent, with the latest attempt result for each?
  - id: v1.message-attempt.list-attempted-destinations
    intent: List endpoints a message was sent to
    question: Which endpoints did a given webhook message go out to?
  - id: v1.message-attempt.get-headers
    intent: Get the headers used on a delivery attempt
    question: What HTTP headers were sent with a specific webhook delivery attempt?
  - id: v1.message-attempt.get
    intent: Get a single delivery attempt
    question: What response code and body did one delivery attempt get back?
  - id: v1.message-attempt.expunge-content
    intent: Delete a delivery attempt's response body
    question: An endpoint returned sensitive data in its response — how do I delete that stored body?
  phrasing_ops: 9
  slug: svix-message-attempt-api
- baseURL: https://api.svix.com
  baseurl_source: declared
  description: The Sink API from Svix — 6 operation(s) for sink.
  name: Svix Sink API
  phrasing_intents:
  - id: v1.streaming.sink.get-last-acked-event
    intent: Get the last event a sink acknowledged
    question: How far has my stream sink gotten — what's the last event it acked?
  - id: v1.streaming.sink.events.get-next-event
    intent: Get a sink's oldest unacknowledged event
    question: What's the next event my sink hasn't acked yet?
  - id: v1.streaming.sink.list
    intent: List a stream's sinks
    question: Which sinks are attached to my stream?
  - id: v1.streaming.sink.create
    intent: Create a sink on a stream
    question: How do I add a new sink to a Svix stream?
  - id: v1.streaming.sink.get
    intent: Get a sink's configuration
    question: What is the configuration of a specific sink on my stream?
  - id: v1.streaming.sink.update
    intent: Create or fully replace a sink
    question: How do I upsert a sink so it's created if it doesn't exist yet?
  - id: v1.streaming.sink.delete
    intent: Delete a sink
    question: How do I remove a sink from a stream?
  - id: v1.streaming.sink.patch
    intent: Partially update a sink
    question: How do I pause a sink by changing just its status?
  phrasing_ops: 16
  slug: svix-sink-api
- baseURL: https://api.svix.com
  baseurl_source: declared
  description: Generate statistics about your Svix utilization
  name: Svix Statistics API
  phrasing_intents:
  - id: v1.statistics.aggregate-event-types
    intent: Calculate event type subscriptions across all apps
    question: Which event types is each of my applications explicitly subscribed to?
  - id: v1.statistics.aggregate-app-stats
    intent: Calculate message attempt counts for all apps
    question: How many message destinations did each application use over a billing period?
  - id: v1.statistics.endpoint-count
    intent: Count active and disabled endpoints
    question: How many active and disabled endpoints are in my environment?
  - id: v1.stats.app-attempts
    intent: Get an app's attempt stats grouped by period
    question: How did one application's delivery attempts trend day by day?
  phrasing_ops: 4
  slug: svix-statistics-api
- baseURL: https://api.svix.com
  baseurl_source: declared
  description: The Stream API from Svix — 2 operation(s) for stream.
  name: Svix Stream API
  phrasing_intents:
  - id: v1.streaming.simulate-transformation
    intent: Test a stream transformation on sample events
    question: How do I try out stream transformation code against sample events before deploying it?
  - id: v1.streaming.stream.list
    intent: List streams
    question: What streams does my organization have in Svix Stream?
  - id: v1.streaming.stream.create
    intent: Create a stream
    question: How do I set up a new event stream?
  - id: v1.streaming.stream.get
    intent: Get a stream
    question: What are the details of a particular stream?
  - id: v1.streaming.stream.update
    intent: Create or replace a stream
    question: How do I upsert a stream so it's created if the id doesn't exist?
  - id: v1.streaming.stream.delete
    intent: Delete a stream
    question: How do I delete a stream I no longer need?
  - id: v1.streaming.stream.patch
    intent: Partially update a stream
    question: How do I change just a stream's description?
  - id: v1.streaming.stream.patch-alert-email
    intent: Set a stream's alert email
    question: Where do alerts about a stream get emailed, and how do I change it?
  phrasing_ops: 8
  slug: svix-stream-api
- baseURL: https://api.svix.com
  baseurl_source: declared
  description: The Stream Authentication API from Svix — 5 operation(s) for stream authentication.
  name: Svix Stream Authentication API
  phrasing_intents:
  - id: v1.authentication.stream-portal-access
    intent: Get a magic link to the Stream Consumer Portal
    question: How do I give a customer a login link to their stream consumer portal?
  - id: v1.authentication.stream-logout
    intent: Log out a stream token
    question: How do I log out a stream portal token when a user signs out?
  - id: v1.authentication.stream-expire-all
    intent: Expire every token for a stream
    question: How do I revoke all portal tokens issued for a stream?
  - id: v1.authentication.rotate-stream-poller-token
    intent: Rotate a stream sink's poller token
    question: How do I rotate the token for polling events from a stream sink?
  - id: v1.authentication.get-stream-poller-token
    intent: Get a stream sink's current poller token
    question: Where do I find the current token for polling a stream sink?
  phrasing_ops: 5
  slug: svix-stream-authentication-api
- baseURL: https://api.svix.com
  baseurl_source: declared
  description: The Stream Event Type API from Svix — 2 operation(s) for stream event type.
  name: Svix Stream Event Type API
  phrasing_intents:
  - id: v1.streaming.event-type.list
    intent: List stream event types
    question: What event types are defined for my streams?
  - id: v1.streaming.event-type.create
    intent: Create a stream event type
    question: How do I define a new event type for Svix Stream?
  - id: v1.streaming.event-type.get
    intent: Get a stream event type
    question: What does a particular stream event type look like?
  - id: v1.streaming.event-type.update
    intent: Create or replace a stream event type
    question: How do I upsert a stream event type by name?
  - id: v1.streaming.event-type.delete
    intent: Delete a stream event type
    question: How do I delete a stream event type?
  - id: v1.streaming.event-type.patch
    intent: Partially update a stream event type
    question: How do I deprecate a stream event type without redefining it?
  phrasing_ops: 6
  slug: svix-stream-event-type-api
- baseURL: https://api.svix.com
  baseurl_source: declared
  description: Configure where operational webhooks are sent to.
  name: Svix Webhook Endpoint API
  phrasing_intents:
  - id: v1.operational-webhook.endpoint.list
    intent: List operational webhook endpoints
    question: Which URLs receive my Svix operational webhooks about my account?
  - id: v1.operational-webhook.endpoint.create
    intent: Create an operational webhook endpoint
    question: How do I get notified when something happens in my account, like an endpoint being disabled?
  - id: v1.operational-webhook.endpoint.get
    intent: Get an operational webhook endpoint
    question: What are the settings of one operational webhook endpoint?
  - id: v1.operational-webhook.endpoint.update
    intent: Create or replace an operational webhook endpoint
    question: How do I change the URL of an operational webhook endpoint?
  - id: v1.operational-webhook.endpoint.delete
    intent: Delete an operational webhook endpoint
    question: How do I stop receiving operational webhooks at a URL?
  - id: v1.operational-webhook.endpoint.get-secret
    intent: Get an operational webhook endpoint's secret
    question: Where is the secret to verify operational webhooks from Svix?
  - id: v1.operational-webhook.endpoint.rotate-secret
    intent: Rotate an operational webhook endpoint's secret
    question: How do I rotate the signing secret for my operational webhooks?
  - id: v1.operational-webhook.endpoint.get-headers
    intent: Get an operational webhook endpoint's headers
    question: What extra headers are sent with my operational webhooks?
  phrasing_ops: 9
  slug: svix-webhook-endpoint-api
- baseURL: http://localhost:8071
  baseurl_source: declared
  description: The Webhook API from Svix — 0 operation(s) for webhook.
  name: Svix Webhook API
  slug: svix-webhook-api
- baseURL: http://localhost:8071
  baseurl_source: declared
  description: The Broadcast API from Svix — 1 operation(s) for broadcast.
  name: Svix Broadcast API
  phrasing_intents:
  - id: v1.message.broadcast
    intent: Broadcast a message to every application
    question: How do I send the same webhook event to all of my customers at once?
  phrasing_ops: 1
  slug: svix-broadcast-api
- baseURL: http://localhost:8071
  baseurl_source: declared
  description: The Environment-Settings API from Svix — 3 operation(s) for environment-settings.
  name: Svix Environment Settings API
  phrasing_intents:
  - id: v1.environment.get-settings
    intent: Get the environment's settings
    question: What settings are applied to the environment my API key belongs to?
  - id: v1.management.environment-settings.get
    intent: Get dashboard environment settings
    question: How do I see the full dashboard settings for my environment, like branding and retry policy?
  - id: v1.management.environment-settings.update
    intent: Replace the environment's settings
    question: How do I update all of my environment's settings in one full replace?
  - id: v1.management.environment-settings.patch
    intent: Change individual environment settings
    question: How do I turn on just one feature, like transformations, without resending every setting?
  - id: v1.management.environment-settings.get-otel-config
    intent: Get the OpenTelemetry export config
    question: Where is my environment sending OpenTelemetry data?
  - id: v1.management.environment-settings.update-otel-config
    intent: Set the OpenTelemetry export config
    question: How do I send Svix telemetry to my own OpenTelemetry collector?
  - id: v1.management.environment-settings.delete-otel-config
    intent: Remove the OpenTelemetry export config
    question: How do I stop exporting telemetry to my OpenTelemetry collector?
  phrasing_ops: 7
  slug: svix-environment-settings-api
- baseURL: http://localhost:8071
  baseurl_source: declared
  description: The Events API from Svix — 1 operation(s) for events.
  name: Svix Events API
  phrasing_intents:
  - id: v1.events.stream
    intent: Read the operational events stream
    question: How can I poll the operational webhook events for my environment instead of receiving them?
  phrasing_ops: 1
  slug: svix-events-api
- baseURL: http://localhost:8071
  baseurl_source: declared
  description: The Inbound API from Svix — 1 operation(s) for inbound.
  name: Svix Inbound API
  phrasing_intents:
  - id: v1.inbound.rotate-url
    intent: Rotate an application's inbound URL
    question: How do I get a new inbound URL for an application and kill the old one?
  phrasing_ops: 1
  slug: svix-inbound-api
- baseURL: http://localhost:8071
  baseurl_source: declared
  description: The Ingest Logs API from Svix — 1 operation(s) for ingest logs.
  name: Svix Ingest Logs API
  phrasing_intents:
  - id: v1.ingest.log.list
    intent: List an ingest source's logs
    question: How do I see the log of webhooks my ingest source received?
  phrasing_ops: 1
  slug: svix-ingest-logs-api
- baseURL: http://localhost:8071
  baseurl_source: declared
  description: The Webhook Sink API from Svix — 10 operation(s) for webhook sink.
  name: Svix Webhook Sink API
  phrasing_intents:
  - id: v1.app.stream.sink.list
    intent: List an application's stream sinks
    question: Which stream sinks are batching events out of one of my applications?
  - id: v1.app.stream.sink.create
    intent: Create a stream sink for an application
    question: How do I set up a stream sink that delivers events in batches?
  - id: v1.app.stream.sink.get
    intent: Get a stream sink
    question: What batch size and status does a particular stream sink have?
  - id: v1.app.stream.sink.upsert
    intent: Create or replace a stream sink
    question: Can I upsert a stream sink so it's created if that ID doesn't exist?
  - id: v1.app.stream.sink.delete
    intent: Delete a stream sink
    question: How do I remove a stream sink I no longer need?
  - id: v1.app.stream.sink.patch
    intent: Change some settings of a stream sink
    question: Can I pause a stream sink by changing only its status?
  - id: v1.app.stream.sink-transformation-get
    intent: Get a stream sink's transformation code
    question: What transformation code runs on events before a stream sink sends them?
  - id: v1.app.stream.sink.transformation-partial-update
    intent: Set or remove a stream sink's transformation
    question: How do I attach transformation code to a stream sink?
  phrasing_ops: 16
  slug: svix-webhook-sink-api
- baseURL: http://localhost:8071
  baseurl_source: declared
  description: The Webhooks AutoConfig API from Svix — 3 operation(s) for webhooks autoconfig.
  name: Svix Webhooks AutoConfig API
  phrasing_intents:
  - id: v1.endpoint.auto-config.create
    intent: Start an endpoint auto-config flow
    question: How do I let a customer finish configuring their own webhook endpoint later?
  - id: v1.endpoint.auto-config.get
    intent: Get an endpoint's auto-config token
    question: Can I see the auto-config token issued for an endpoint?
  - id: v1.endpoint.auto-config.update
    intent: Complete an auto-config endpoint's details
    question: How do I fill in the destination for an endpoint created through auto-config?
  - id: v1.endpoint.auto-config.rotate
    intent: Rotate an auto-config endpoint's auth token
    question: How do I issue a new auth token for an auto-config endpoint?
  phrasing_ops: 4
  slug: svix-webhooks-autoconfig-api
arazzos:
- description: Create an application and mint a magic-link URL into its embedded App Portal.
  name: Svix Provision Application and Open App Portal
  slug: svix-create-app-portal-access-workflow
- description: Create an integration on an application and read back its API key.
  name: Svix Create Integration and Retrieve Key
  slug: svix-create-integration-and-key-workflow
- description: List an application's endpoints, branch on whether one exists, delete it, then delete the application.
  name: Svix Decommission an Application
  slug: svix-decommission-application-workflow
- description: Send an example message to an endpoint and read its delivery statistics.
  name: Svix Endpoint Health Check
  slug: svix-endpoint-health-check-workflow
- description: Create an ingest source, attach an ingest endpoint, and read back the source's ingest URL.
  name: Svix Create Ingest Source and Endpoint
  slug: svix-ingest-source-and-endpoint-workflow
- description: Register an operational webhook endpoint and retrieve its signing secret.
  name: Svix Set Up Operational Webhook Endpoint
  slug: svix-operational-webhook-setup-workflow
- description: Create an application, register a webhook endpoint, send a message, and inspect the delivery attempts.
  name: Svix Provision Application and Send First Message
  slug: svix-provision-and-send-message-workflow
- description: Trigger recovery of an endpoint's failed messages and poll the background task to completion.
  name: Svix Recover Failed Webhooks
  slug: svix-recover-failed-webhooks-workflow
- description: Create an event type, subscribe an endpoint to it, and send the event type's example message.
  name: Svix Register Event Type and Send Example
  slug: svix-register-event-type-and-send-workflow
- description: Find a failing delivery attempt for a message and resend it to its endpoint.
  name: Svix Resend a Failed Message Attempt
  slug: svix-resend-failed-attempt-workflow
- description: Rotate a webhook endpoint's signing secret and read back the new secret value.
  name: Svix Rotate Endpoint Signing Secret
  slug: svix-rotate-endpoint-secret-workflow
- description: Rotate an ingest source's token and return its refreshed ingest URL.
  name: Svix Rotate Ingest Source Token
  slug: svix-rotate-ingest-source-token-workflow
- description: Rotate an integration's API key and read back the new key value.
  name: Svix Rotate Integration Key
  slug: svix-rotate-integration-key-workflow
- description: Send a message to an existing application and poll its attempts until delivery succeeds.
  name: Svix Send Message and Confirm Delivery
  slug: svix-send-message-and-confirm-delivery-workflow
- description: Create a stream, attach a poller sink, publish events, and poll the sink for them.
  name: Svix Create Stream with Poller Sink and Send Events
  slug: svix-stream-sink-and-poll-events-workflow
artifact_total: 100
asyncapis:
- description: ''
  name: Svix Operational Webhooks
  slug: svix-operational-webhooks
collections:
- collection_type: postman
  name: Svix API
  slug: postman-svix-openapi
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Svix Application API
  slug: open-svix-application-api
- collection_type: open
  name: Svix Application Authentication API
  slug: open-svix-authentication-api
- collection_type: open
  name: Svix Application Background Task API
  slug: open-svix-background-task-api
- collection_type: open
  name: Svix Application Connector API
  slug: open-svix-connector-api
- collection_type: open
  name: Svix Application Endpoint API
  slug: open-svix-endpoint-api
- collection_type: open
  name: Svix Application Environment API
  slug: open-svix-environment-api
- collection_type: open
  name: Svix Application Event API
  slug: open-svix-event-api
- collection_type: open
  name: Svix Application Event Type API
  slug: open-svix-event-type-api
- collection_type: open
  name: Svix Application Health API
  slug: open-svix-health-api
- collection_type: open
  name: Svix Application Ingest Endpoint API
  slug: open-svix-ingest-endpoint-api
- collection_type: open
  name: Svix Application Ingest Source API
  slug: open-svix-ingest-source-api
- collection_type: open
  name: Svix Application Integration API
  slug: open-svix-integration-api
- collection_type: open
  name: Svix Application Message API
  slug: open-svix-message-api
- collection_type: open
  name: Svix Application Message Attempt API
  slug: open-svix-message-attempt-api
- collection_type: open
  name: Svix Application Sink API
  slug: open-svix-sink-api
- collection_type: open
  name: Svix Application Statistics API
  slug: open-svix-statistics-api
- collection_type: open
  name: Svix Application Stream API
  slug: open-svix-stream-api
- collection_type: open
  name: Svix Application Stream Authentication API
  slug: open-svix-stream-authentication-api
- collection_type: open
  name: Svix Application Stream Event Type API
  slug: open-svix-stream-event-type-api
- collection_type: open
  name: Svix Application Webhook Endpoint API
  slug: open-svix-webhook-endpoint-api
- collection_type: open
  name: Svix API
  slug: open-svix
common:
- group: company
  title: ''
  type: Website
  url: https://www.svix.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/capabilities/svix-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/svix-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/svix/svix-webhooks/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/svix/svix-webhooks/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/svix/svix-webhooks/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/svix/svix-webhooks/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/svix/svix-webhooks/blob/main/LICENSE
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/agentic-access/svix-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/svix-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/security/svix-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/svix-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/security/svix-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/svix-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/security/svix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/svix-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/authentication/svix-authentication.yml
  title: ''
  type: Authentication
  url: authentication/svix-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/svix/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/arazzo/svix-create-app-portal-access-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/svix-create-app-portal-access-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/arazzo/svix-create-integration-and-key-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/svix-create-integration-and-key-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/arazzo/svix-decommission-application-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/svix-decommission-application-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/arazzo/svix-endpoint-health-check-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/svix-endpoint-health-check-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/arazzo/svix-ingest-source-and-endpoint-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/svix-ingest-source-and-endpoint-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/arazzo/svix-operational-webhook-setup-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/svix-operational-webhook-setup-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/arazzo/svix-provision-and-send-message-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/svix-provision-and-send-message-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/arazzo/svix-recover-failed-webhooks-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/svix-recover-failed-webhooks-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/arazzo/svix-register-event-type-and-send-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/svix-register-event-type-and-send-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/arazzo/svix-resend-failed-attempt-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/svix-resend-failed-attempt-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/arazzo/svix-rotate-endpoint-secret-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/svix-rotate-endpoint-secret-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/arazzo/svix-rotate-ingest-source-token-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/svix-rotate-ingest-source-token-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/arazzo/svix-rotate-integration-key-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/svix-rotate-integration-key-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/arazzo/svix-send-message-and-confirm-delivery-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/svix-send-message-and-confirm-delivery-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/arazzo/svix-stream-sink-and-poll-events-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/svix-stream-sink-and-poll-events-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://www.svix.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.svix.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.svix.com
- group: docs
  title: ''
  type: APIReference
  url: https://api.svix.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.svix.com/quickstart
- group: learn
  title: ''
  type: Tutorials
  url: https://docs.svix.com/tutorials
- group: start
  title: ''
  type: Signup
  url: https://dashboard.svix.com
- group: start
  title: ''
  type: Login
  url: https://dashboard.svix.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.svix.com/pricing/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/plans/svix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/svix-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/rate-limits/svix-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/svix-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/finops/svix-finops.yml
  title: ''
  type: FinOps
  url: finops/svix-finops.yml
- group: other
  title: ''
  type: Regions
  url: https://docs.svix.com/multi-region
- group: auth
  title: ''
  type: Authentication
  url: https://docs.svix.com/api-keys
- group: auth
  title: ''
  type: Security
  url: https://www.svix.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://www.svix.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.svix.com/security/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.svix.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.svix.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.svix.com
- group: company
  title: ''
  type: Blog
  url: https://www.svix.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/svix/svix-webhooks/blob/main/ChangeLog.md
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/svix/svix-webhooks/releases
- group: operate
  title: ''
  type: Support
  url: mailto:support@svix.com
- group: operate
  title: ''
  type: Contact
  url: https://www.svix.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/svix
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/svix/svix-webhooks
- group: start
  title: ''
  type: Console
  url: https://dashboard.svix.com
- group: start
  title: ''
  type: Sandbox
  url: https://play.svix.com
- group: build
  title: ''
  type: CLI
  url: https://github.com/svix/svix-webhooks/tree/main/svix-cli
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/svix/
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/svix
- group: build
  title: ''
  type: SDKs
  url: https://github.com/svix/svix-webhooks/tree/main/go
- group: build
  title: ''
  type: SDKs
  url: https://central.sonatype.com/artifact/com.svix/svix
- group: build
  title: ''
  type: SDKs
  url: https://github.com/svix/svix-webhooks/tree/main/kotlin
- group: build
  title: ''
  type: SDKs
  url: https://rubygems.org/gems/svix
- group: build
  title: ''
  type: SDKs
  url: https://www.nuget.org/packages/Svix
- group: build
  title: ''
  type: SDKs
  url: https://packagist.org/packages/svix/svix
- group: build
  title: ''
  type: SDKs
  url: https://crates.io/crates/svix
- group: other
  title: ''
  type: X
  url: https://twitter.com/SvixHQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/svix
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/rules/svix-rules.yml
  title: ''
  type: Rules
  url: rules/svix-rules.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/json-schema/
  title: ''
  type: JSONSchema
  url: json-schema/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/json-ld/svix-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/svix-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/vocabulary/svix-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/svix-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.svix.com/llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/packages/svix-packages.yml
  title: ''
  type: Packages
  url: packages/svix-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/packages/svix-packages.yml
  title: ''
  type: SDKs
  url: packages/svix-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/well-known/svix-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/svix-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/well-known/svix-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/svix-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/mcp/svix-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/svix-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/mcp/svix-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/svix-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/llms/svix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/svix-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/asyncapi/svix-operational-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/svix-operational-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/conventions/svix-conventions.yml
  title: ''
  type: Conventions
  url: conventions/svix-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/conventions/svix-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/svix-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/errors/svix-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/svix-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/lifecycle/svix-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/svix-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/conformance/svix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/svix-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/data-model/svix-data-model.yml
  title: ''
  type: DataModel
  url: data-model/svix-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/changelog/svix-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/svix-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/cli/svix-cli.yml
  title: ''
  type: CLI
  url: cli/svix-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/components/svix-components.yml
  title: ''
  type: Components
  url: components/svix-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/sandbox/svix-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/svix-sandbox.yml
created: '2026-05-22'
description: Svix is an enterprise webhooks-as-a-service platform on the sending side of the webhook market. It provides a single API for delivering reliable, secure, low-latency webhooks at scale, with hosted UIs (Consumer App Portal), a polyglot SDK pipeline, an open source server, and adjacent products for streaming (Stream) and webhook ingestion (Ingest). Hosted offering is multi-region (US, EU, CA, AU, IN) with SOC 2 Type II, HIPAA, PCI-DSS attestations.
examples:
- key_count: 5
  name: Svix App Portal Access Example
  slug: svix-app-portal-access-example
- key_count: 5
  name: Svix Application Create Example
  slug: svix-application-create-example
- key_count: 5
  name: Svix Endpoint Create Example
  slug: svix-endpoint-create-example
- key_count: 5
  name: Svix Endpoint Secret Rotate Example
  slug: svix-endpoint-secret-rotate-example
- key_count: 5
  name: Svix Event Type Create Example
  slug: svix-event-type-create-example
- key_count: 5
  name: Svix Ingest Source Create Example
  slug: svix-ingest-source-create-example
- key_count: 5
  name: Svix Message Attempt List Example
  slug: svix-message-attempt-list-example
- key_count: 5
  name: Svix Message Create Example
  slug: svix-message-create-example
finops:
- name: Svix Finops
  service_category: ''
  slug: svix-finops
image: https://www.svix.com/static/img/brand-padded.svg
json_schemas:
- name: Svix Application
  property_count: 8
  slug: svix-application
- name: Svix Endpoint
  property_count: 12
  slug: svix-endpoint
- name: Svix Event Type
  property_count: 9
  slug: svix-event-type
- name: Svix Message Attempt
  property_count: 11
  slug: svix-message-attempt
- name: Svix Message
  property_count: 8
  slug: svix-message
json_structures:
- name: Svix Application Structure
  property_count: 0
  slug: svix-application-structure
- name: Svix Endpoint Structure
  property_count: 0
  slug: svix-endpoint-structure
- name: Svix Event Type Structure
  property_count: 0
  slug: svix-event-type-structure
- name: Svix Message Structure
  property_count: 0
  slug: svix-message-structure
jsonld:
- class_count: 38
  name: Svix Context
  property_count: 9
  slug: svix-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.us.svix.com over HTTP requiring an API key; 13 tools listed.
  name: Consumer App Portal MCP (remote, hosted)
  slug: consumer-app-portal-mcp
modified: '2026-08-13'
name: Svix
nav: Providers
network: true
overview: 'Svix publishes 29 APIs on the [APIs.io](https://apis.io/) network, including Application API, Authentication API, Background Task API, and 26 more. Tagged areas include Webhook, Webhooks As A Service, Webhook Delivery, Webhook Sending, and Event-Driven.


  The Svix catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Svix''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, signup flow, pricing, and 86 more developer resources.'
plans:
- name: Svix Plans Pricing
  plan_count: 3
  slug: svix-plans-pricing
- name: Svix Price Estimates
  plan_count: 0
  slug: svix-price-estimates
random_paper: 18
rate_limits:
- limit_count: 4
  name: Svix Rate Limits
  slug: svix-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Svix API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: svix-jsonschema-spectral-rules
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: Svix API Rules
  rule_count: 14
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 8
  slug: svix-rules
score:
  band: exemplar
  composite: 76.7
  coverage:
    artifact_dirs: 36
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 45.5
    contract_quality: 66.1
    developer_ergonomics: 79.8
    discoverability: 60.0
    operational_transparency: 81.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - global
  open_source:
    applies: true
    score: 100.0
  previous_composite: 76.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 28
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 28.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/svix/refs/heads/main/screenshots/svix-2026-06-20T194748.png
security:
- kind: authentication
  name: Svix Authentication
  slug: svix-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Svix Domain Security
  slug: svix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Svix Vulnerability Disclosure
  slug: svix-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Svix Trust Center
  slug: svix-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA, GDPR
skill_count: 2
skills:
- name: receiving-webhooks
  slug: receiving-webhooks
- name: svix-sending-webhooks
  slug: svix-sending-webhooks
slug: svix
tags:
- Webhook
- Webhooks As A Service
- Webhook Delivery
- Webhook Sending
- Event-Driven
- Eventing
- Messaging
- Pub-Sub
- Streaming
- Ingest
- Integration
- Reliability
- Retries
- Deliverability
- Signing
- Verification
- HMAC
- Standard Webhooks
- Multi-Tenant
- Multi-Region
- Enterprise
- Software-as-a-Service
- Developer Platform
- REST
- SOC 2
- HIPAA
- PCI DSS
- GDPR
- Open Source
- Rust
- Polyglot SDK
- Terraform
- CLI
website: https://www.svix.com/
---
