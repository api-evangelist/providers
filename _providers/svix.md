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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 68.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 79
  human_in_the_loop: 0
  name: Svix Agentic Access
  operation_count: 128
  slug: svix-agentic-access
  summary_line: 128 operations · 79 acting
api_count: 21
apis:
- description: 'The self-hostable open source Svix server (svix-webhooks repo). Smaller surface area than the hosted product (no Stream, no Ingest, no Connectors, no Background Tasks, no multi-region) — 29 paths, 46 '
  name: Svix Open Source Server API
  slug: open-source-server
- description: Consumer Applications are where messages are sent to. In most cases you would want to have one application for each of your users.
  name: Svix Application API
  slug: svix-application-api
- description: Easily give your users access to our pre-built management UI.
  name: Svix Authentication API
  slug: svix-authentication-api
- description: The background tasks that have been executed for your environment.
  name: Svix Background Task API
  slug: svix-background-task-api
- description: Connectors allow you to connect applications to external services.
  name: Svix Connector API
  slug: svix-connector-api
- description: Endpoints are the URLs messages will be sent to. Each application can have up to 50 endpoints and each message sent to that application will be sent to all of them (unless they are not subscribed to t
  name: Svix Endpoint API
  slug: svix-endpoint-api
- description: Manage your environments like development, staging and production.
  name: Svix Environment API
  slug: svix-environment-api
- description: The Event API from Svix — 2 operation(s) for event.
  name: Svix Event API
  slug: svix-event-api
- description: Event types are identifiers denoting the type of message being sent. Event types are primarily used to decide which events are sent to which endpoint.
  name: Svix Event Type API
  slug: svix-event-type-api
- description: Health checks for the API.
  name: Svix Health API
  slug: svix-health-api
- description: Configure where Svix Ingest sends messages.
  name: Svix Ingest Endpoint API
  slug: svix-ingest-endpoint-api
- description: The Ingest Source API from Svix — 4 operation(s) for ingest source.
  name: Svix Ingest Source API
  slug: svix-ingest-source-api
- description: Integrations are services your users connect an application to. An integration can manage the application and its endpoints.
  name: Svix Integration API
  slug: svix-integration-api
- description: Messages are the webhook events being sent.
  name: Svix Message API
  slug: svix-message-api
- description: Attempts to deliver `Message`s to `Endpoint`s.
  name: Svix Message Attempt API
  slug: svix-message-attempt-api
- description: The Sink API from Svix — 6 operation(s) for sink.
  name: Svix Sink API
  slug: svix-sink-api
- description: Generate statistics about your Svix utilization
  name: Svix Statistics API
  slug: svix-statistics-api
- description: The Stream API from Svix — 2 operation(s) for stream.
  name: Svix Stream API
  slug: svix-stream-api
- description: The Stream Authentication API from Svix — 5 operation(s) for stream authentication.
  name: Svix Stream Authentication API
  slug: svix-stream-authentication-api
- description: The Stream Event Type API from Svix — 2 operation(s) for stream event type.
  name: Svix Stream Event Type API
  slug: svix-stream-event-type-api
- description: Configure where operational webhooks are sent to.
  name: Svix Webhook Endpoint API
  slug: svix-webhook-endpoint-api
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
artifact_total: 91
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
- group: commercial
  title: ''
  type: License
  url: https://github.com/svix/svix-webhooks/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/svix-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/svix-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/svix-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/svix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/svix-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/svix/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/svix-create-app-portal-access-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/svix-create-integration-and-key-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/svix-decommission-application-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/svix-endpoint-health-check-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/svix-ingest-source-and-endpoint-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/svix-operational-webhook-setup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/svix-provision-and-send-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/svix-recover-failed-webhooks-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/svix-register-event-type-and-send-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/svix-resend-failed-attempt-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/svix-rotate-endpoint-secret-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/svix-rotate-ingest-source-token-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/svix-rotate-integration-key-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/svix-send-message-and-confirm-delivery-workflow.yml
- group: design
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
  title: ''
  type: Plans
  url: plans/svix-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/svix-rate-limits.yml
- group: commercial
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
  title: ''
  type: Rules
  url: rules/svix-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/svix-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/svix-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.svix.com/llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/svix-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/svix-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/svix-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/svix-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/svix-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/svix-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/svix-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/svix-operational-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/svix-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/svix-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/svix-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/svix-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/svix-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/svix-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/svix-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/svix-cli.yml
- group: design
  title: ''
  type: Components
  url: components/svix-components.yml
- group: start
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
- description: ''
  name: Consumer App Portal MCP (remote, hosted)
  slug: consumer-app-portal-mcp-remote-hosted
modified: '2026-08-13'
name: Svix
nav: Providers
network: true
overview: 'Svix publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Application API, Authentication API, Background Task API, and 17 more. Tagged areas include Webhooks, Webhooks As A Service, Webhook Delivery, Webhook Sending, and Event Driven.


  The Svix catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Svix''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, signup flow, pricing, and 80 more developer resources.'
plans:
- name: Svix Plans Pricing
  plan_count: 3
  slug: svix-plans-pricing
random_paper: 17
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
  composite: 79.3
  delta: -4.8
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 55.3
    contract_quality: 75.3
    developer_ergonomics: 83.3
    discoverability: 83.3
    governance: 55.3
    operational_transparency: 84.2
  previous_composite: 84.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 50.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
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
- Webhooks
- Webhooks As A Service
- Webhook Delivery
- Webhook Sending
- Event Driven
- Eventing
- Messaging
- Pub Sub
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
- Multi Tenant
- Multi Region
- Enterprise
- SaaS
- Developer Platform
- API
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
website: https://dashboard.svix.com
---
