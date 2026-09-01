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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 25
  human_in_the_loop: 1
  name: Ably Agentic Access
  operation_count: 44
  slug: ably-agentic-access
  summary_line: 44 operations · 25 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: The apps API from Ably — 3 operation(s) for apps.
  name: Ably apps API
  slug: ably-apps-api
- description: The Authentication API from Ably — 1 operation(s) for authentication.
  name: Ably Authentication API
  slug: ably-authentication-api
- description: The History API from Ably — 2 operation(s) for history.
  name: Ably History API
  slug: ably-history-api
- description: The keys API from Ably — 3 operation(s) for keys.
  name: Ably keys API
  slug: ably-keys-api
- description: The namespaces API from Ably — 2 operation(s) for namespaces.
  name: Ably namespaces API
  slug: ably-namespaces-api
- description: The Publishing API from Ably — 1 operation(s) for publishing.
  name: Ably Publishing API
  slug: ably-publishing-api
- description: The Push API from Ably — 6 operation(s) for push.
  name: Ably Push API
  slug: ably-push-api
- description: The queues API from Ably — 2 operation(s) for queues.
  name: Ably queues API
  slug: ably-queues-api
- description: The rules API from Ably — 2 operation(s) for rules.
  name: Ably rules API
  slug: ably-rules-api
- description: The Stats API from Ably — 2 operation(s) for stats.
  name: Ably Stats API
  slug: ably-stats-api
- description: The Status API from Ably — 3 operation(s) for status.
  name: Ably Status API
  slug: ably-status-api
- description: The tokens API from Ably — 1 operation(s) for tokens.
  name: Ably tokens API
  slug: ably-tokens-api
artifact_total: 121
asyncapis:
- description: AsyncAPI 3.0 description of the Ably realtime messaging surface. Ably exposes pub/sub channels, presence, push notifications, and history over a native WebSocket-based protocol, with additional access
  name: Ably Realtime Protocol
  slug: ably-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Control API v1 apps API
  slug: open-ably-apps-api
- collection_type: open
  name: Control API v1 apps Authentication API
  slug: open-ably-authentication-api
- collection_type: open
  name: Control API v1
  slug: open-ably-control-api
- collection_type: open
  name: Control API v1 apps History API
  slug: open-ably-history-api
- collection_type: open
  name: Control API v1 apps keys API
  slug: open-ably-keys-api
- collection_type: open
  name: Control API v1 apps namespaces API
  slug: open-ably-namespaces-api
- collection_type: open
  name: Platform API
  slug: open-ably-platform-api
- collection_type: open
  name: Control API v1 apps Publishing API
  slug: open-ably-publishing-api
- collection_type: open
  name: Control API v1 apps Push API
  slug: open-ably-push-api
- collection_type: open
  name: Control API v1 apps queues API
  slug: open-ably-queues-api
- collection_type: open
  name: Control API v1 apps rules API
  slug: open-ably-rules-api
- collection_type: open
  name: Control API v1 apps Stats API
  slug: open-ably-stats-api
- collection_type: open
  name: Control API v1 apps Status API
  slug: open-ably-status-api
- collection_type: open
  name: Control API v1 apps tokens API
  slug: open-ably-tokens-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ably-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ably-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ably-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ably-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ably-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ably-realtime
- group: start
  title: ''
  type: Portal
  url: https://ably.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ably.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://ably.com/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ably
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ably.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/ably-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ably-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ably-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://ably.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://voltaire.ably.com/blog/rss.xml
created: '2026-05-08'
description: Ably is a realtime messaging platform offering pub/sub, presence, push notifications, chat, LiveSync, and integrations over WebSocket and HTTP. Ably publishes its OpenAPI specifications publicly via the ably/open-specs GitHub repository, with separate specs for the Platform API (REST messaging surface) and the Control API (account, app, and key management).
examples:
- key_count: 6
  name: Ably Requestaccesstoken Example
  slug: ably-requestaccesstoken-example
- key_count: 6
  name: Ably Subscribepushdevicetochannel Example
  slug: ably-subscribepushdevicetochannel-example
finops:
- name: Ably Finops
  service_category: Realtime Infrastructure
  slug: ably-finops
graphqls:
- description: Conceptual GraphQL schema for the [Ably](https://ably.com/) realtime messaging platform.
  name: Ably GraphQL Schema
  slug: ably-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ably.png
json_schemas:
- name: amqp_external_rule_patch
  property_count: 5
  slug: ably-amqp-external-rule-patch
- name: amqp_external_rule_post
  property_count: 4
  slug: ably-amqp-external-rule-post
- name: amqp_external_rule_response
  property_count: 11
  slug: ably-amqp-external-rule-response
- name: amqp_rule_patch
  property_count: 5
  slug: ably-amqp-rule-patch
- name: amqp_rule_post
  property_count: 5
  slug: ably-amqp-rule-post
- name: amqp_rule_response
  property_count: 11
  slug: ably-amqp-rule-response
- name: app_patch
  property_count: 9
  slug: ably-app-patch
- name: app_pkcs12
  property_count: 2
  slug: ably-app-pkcs12
- name: app_post
  property_count: 9
  slug: ably-app-post
- name: app_response
  property_count: 7
  slug: ably-app-response
- name: aws_access_keys_response
  property_count: 2
  slug: ably-aws-access-keys-response
- name: aws_access_keys
  property_count: 3
  slug: ably-aws-access-keys
- name: aws_assume_role
  property_count: 2
  slug: ably-aws-assume-role
- name: aws_kinesis_rule_patch
  property_count: 5
  slug: ably-aws-kinesis-rule-patch
- name: aws_kinesis_rule_post
  property_count: 5
  slug: ably-aws-kinesis-rule-post
- name: aws_kinesis_rule_response
  property_count: 11
  slug: ably-aws-kinesis-rule-response
- name: aws_lambda_rule_patch
  property_count: 5
  slug: ably-aws-lambda-rule-patch
- name: aws_lambda_rule_post
  property_count: 5
  slug: ably-aws-lambda-rule-post
- name: aws_lambda_rule_response
  property_count: 11
  slug: ably-aws-lambda-rule-response
- name: aws_sqs_rule_patch
  property_count: 5
  slug: ably-aws-sqs-rule-patch
- name: aws_sqs_rule_post
  property_count: 5
  slug: ably-aws-sqs-rule-post
- name: aws_sqs_rule_response
  property_count: 11
  slug: ably-aws-sqs-rule-response
- name: azure_function_rule_patch
  property_count: 5
  slug: ably-azure-function-rule-patch
- name: azure_function_rule_post
  property_count: 5
  slug: ably-azure-function-rule-post
- name: azure_function_rule_response
  property_count: 11
  slug: ably-azure-function-rule-response
- name: ChannelDetails
  property_count: 4
  slug: ably-channeldetails
- name: ChannelStatus
  property_count: 2
  slug: ably-channelstatus
- name: cloudflare_worker_rule_patch
  property_count: 5
  slug: ably-cloudflare-worker-rule-patch
- name: cloudflare_worker_rule_post
  property_count: 5
  slug: ably-cloudflare-worker-rule-post
- name: cloudflare_worker_rule_response
  property_count: 11
  slug: ably-cloudflare-worker-rule-response
- name: DeviceDetails
  property_count: 8
  slug: ably-devicedetails
- name: error
  property_count: 5
  slug: ably-error
- name: Extras
  property_count: 1
  slug: ably-extras
- name: google_cloud_function_rule_patch
  property_count: 5
  slug: ably-google-cloud-function-rule-patch
- name: google_cloud_function_rule_post
  property_count: 4
  slug: ably-google-cloud-function-rule-post
- name: google_cloud_function_rule_response
  property_count: 11
  slug: ably-google-cloud-function-rule-response
- name: http_rule_patch
  property_count: 5
  slug: ably-http-rule-patch
- name: http_rule_post
  property_count: 5
  slug: ably-http-rule-post
- name: http_rule_response
  property_count: 11
  slug: ably-http-rule-response
- name: ifttt_rule_patch
  property_count: 5
  slug: ably-ifttt-rule-patch
- name: ifttt_rule_post
  property_count: 5
  slug: ably-ifttt-rule-post
- name: ifttt_rule_response
  property_count: 11
  slug: ably-ifttt-rule-response
- name: ingress_postgres_outbox_rule_patch
  property_count: 3
  slug: ably-ingress-postgres-outbox-rule-patch
- name: ingress_postgres_outbox_rule_post
  property_count: 3
  slug: ably-ingress-postgres-outbox-rule-post
- name: ingress_postgres_outbox_rule_response
  property_count: 9
  slug: ably-ingress-postgres-outbox-rule-response
- name: kafka_rule_patch
  property_count: 5
  slug: ably-kafka-rule-patch
- name: kafka_rule_post
  property_count: 5
  slug: ably-kafka-rule-post
- name: kafka_rule_response
  property_count: 11
  slug: ably-kafka-rule-response
- name: key_patch
  property_count: 2
  slug: ably-key-patch
- name: key_post
  property_count: 2
  slug: ably-key-post
- name: key_response
  property_count: 8
  slug: ably-key-response
- name: me
  property_count: 3
  slug: ably-me
- name: Message
  property_count: 8
  slug: ably-message
- name: namespace_patch
  property_count: 9
  slug: ably-namespace-patch
- name: namespace_post
  property_count: 10
  slug: ably-namespace-post
- name: namespace_response
  property_count: 12
  slug: ably-namespace-response
- name: Notification
  property_count: 5
  slug: ably-notification
- name: Occupancy
  property_count: 5
  slug: ably-occupancy
- name: PresenceMessage
  property_count: 8
  slug: ably-presencemessage
- name: pulsar_rule_patch
  property_count: 5
  slug: ably-pulsar-rule-patch
- name: pulsar_rule_post
  property_count: 5
  slug: ably-pulsar-rule-post
- name: pulsar_rule_response
  property_count: 11
  slug: ably-pulsar-rule-response
- name: pulsar_token_auth
  property_count: 2
  slug: ably-pulsar-token-auth
- name: Push
  property_count: 5
  slug: ably-push
- name: queue_response
  property_count: 13
  slug: ably-queue-response
- name: queue
  property_count: 4
  slug: ably-queue
- name: Recipient
  property_count: 6
  slug: ably-recipient
- name: rule_patch
  property_count: 0
  slug: ably-rule-patch
- name: rule_post
  property_count: 0
  slug: ably-rule-post
- name: rule_response
  property_count: 0
  slug: ably-rule-response
- name: rule_source_patch
  property_count: 2
  slug: ably-rule-source-patch
- name: rule_source
  property_count: 2
  slug: ably-rule-source
- name: SignedTokenRequest
  property_count: 0
  slug: ably-signedtokenrequest
- name: TokenDetails
  property_count: 5
  slug: ably-tokendetails
- name: TokenRequest
  property_count: 5
  slug: ably-tokenrequest
- name: unsupported_rule_response
  property_count: 11
  slug: ably-unsupported-rule-response
- name: zapier_rule_patch
  property_count: 5
  slug: ably-zapier-rule-patch
- name: zapier_rule_post
  property_count: 5
  slug: ably-zapier-rule-post
- name: zapier_rule_response
  property_count: 11
  slug: ably-zapier-rule-response
json_structures:
- name: Ably Structure
  property_count: 0
  slug: ably-structure
layout: provider
modified: '2026-05-29'
name: Ably
nav: Providers
network: true
overview: 'Ably publishes 12 APIs on the [APIs.io](https://apis.io/) network, including apps API, Authentication API, History API, and 9 more. Tagged areas include Real-Time, WebSockets, Pub-Sub, Messaging, and Streaming.


  The Ably catalog on APIs.io includes 1 event-driven AsyncAPI specification and 2 Spectral governance rulesets.


  Ably''s developer surface includes authentication, developer portal, documentation, pricing, GitHub presence, engineering blog, and 10 more developer resources.'
plans:
- name: Ably Plans Pricing
  plan_count: 5
  slug: ably-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 8
  name: Ably Rate Limits
  slug: ably-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Ably API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: ably-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Ably API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ably-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 64.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 13.6
    contract_quality: 66.2
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 13.6
    operational_transparency: 28.9
  previous_composite: 43.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ably/refs/heads/main/screenshots/ably-2026-06-20T163221.png
security:
- kind: authentication
  name: Ably Authentication
  slug: ably-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Ably Domain Security
  slug: ably-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ably Vulnerability Disclosure
  slug: ably-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ably Trust Center
  slug: ably-trust-center
  summary_line: SOC 2, GDPR
slug: ably
tags:
- Real-Time
- WebSockets
- Pub-Sub
- Messaging
- Streaming
- Push Notifications
- Chat
- LiveSync
website: https://ably.com/
---
