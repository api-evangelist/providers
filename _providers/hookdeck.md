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
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.2
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 62
  human_in_the_loop: 7
  name: Hookdeck Agentic Access
  operation_count: 116
  slug: hookdeck-agentic-access
  summary_line: 116 operations · 62 acting · 7 human-in-the-loop
api_count: 17
apis:
- description: Create, update, list, archive, pause, and unpause connections. A connection routes events from a Source to a Destination and may carry rules (retry, alert, transform, filter, delay) that determine how
  name: Hookdeck Connections API
  slug: hookdeck-connections-api
- description: Manage sources — the upstream endpoints (webhook senders or push channels) that ingest events into Hookdeck. Sources support platform-specific verification (Stripe, GitHub, Twilio, Shopify, and many m
  name: Hookdeck Sources API
  slug: hookdeck-sources-api
- description: Manage destinations — the downstream targets (HTTP endpoints, AWS SQS, Azure Service Bus, GCP Pub/Sub, Kafka, RabbitMQ, MongoDB, and more) where Hookdeck delivers events. Supports configurable auth me
  name: Hookdeck Destinations API
  slug: hookdeck-destinations-api
- description: List, retrieve, retry, mute, and inspect events and their delivery attempts. An event is any request Hookdeck received from a source; an attempt is each delivery try against a destination, including s
  name: Hookdeck Events API
  slug: hookdeck-events-api
- description: List and inspect raw requests received by Hookdeck. A request precedes events and is what gets accepted at the gateway boundary before verification, fan-out, transformation, and routing produce one or
  name: Hookdeck Requests API
  slug: hookdeck-requests-api
- description: 'Manage transformations — sandboxed JavaScript executed against events to mutate headers, body, path, or query string before delivery. Also includes a sandboxed run endpoint for testing transformation '
  name: Hookdeck Transformations API
  slug: hookdeck-transformations-api
- description: Save bookmarked events for quick replay and one-click testing during development. Bookmarks let your team capture canonical event payloads and trigger them on demand into any destination.
  name: Hookdeck Bookmarks API
  slug: hookdeck-bookmarks-api
- description: Track issues that occur on events, requests, and backpressure, and manage the triggers (rules) that open and route issues to Slack, Email, Microsoft Teams, Discord, BetterUptime, and other channels.
  name: Hookdeck Issues API
  slug: hookdeck-issues-api
- description: Query aggregated metrics for events, requests, and attempts — success counts, failure counts, response time, throughput, and SLA bands grouped by source, destination, or connection. Backs the dashboar
  name: Hookdeck Metrics API
  slug: hookdeck-metrics-api
- description: Configure platform integrations that adapt Hookdeck behavior for specific source platforms — including signature verification, header normalization, allowed event types, and platform-aware retries (e.
  name: Hookdeck Integrations API
  slug: hookdeck-integrations-api
- description: Manage how your team is notified when issues occur — channel routing, mute windows, per-team subscriptions, and the templates rendered to Slack, Email, Microsoft Teams, and Discord.
  name: Hookdeck Notifications API
  slug: hookdeck-notifications-api
- description: An attempt is any request that Hookdeck makes on behalf of an event.
  name: Hookdeck Attempts API
  slug: hookdeck-attempts-api
- description: Bulk cancel operations allow you to cancel multiple pending events at once.
  name: Hookdeck Bulk cancel events API
  slug: hookdeck-bulk-cancel-events-api
- description: Bulk retry operations allow you to retry many events at once. A bulk retry is first estimated, then created, then processed asynchronously.
  name: Hookdeck Bulk retry events API
  slug: hookdeck-bulk-retry-events-api
- description: Bulk retry ignored events allow you to retry many events that were previously ignored (for instance due to filter rules) at once.
  name: Hookdeck Bulk retry ignored events API
  slug: hookdeck-bulk-retry-ignored-events-api
- description: Bulk retry requests allow you to re-ingest many previously received requests at once.
  name: Hookdeck Bulk retry requests API
  slug: hookdeck-bulk-retry-requests-api
- description: Issue Triggers lets you setup rules that trigger issues when certain conditions are met.
  name: Hookdeck Issue Triggers API
  slug: hookdeck-issue-triggers-api
arazzos:
- description: Create a source, create an authentication integration, then attach the integration to the source.
  name: Hookdeck Attach an Integration to a New Source
  slug: hookdeck-attach-integration-to-source-workflow
- description: Create a transformation, run it against a sample request, then read it back.
  name: Hookdeck Author and Verify a Transformation
  slug: hookdeck-author-transformation-workflow
- description: Find a delivered event, bookmark its payload, then trigger the bookmark to replay it.
  name: Hookdeck Bookmark and Replay an Event
  slug: hookdeck-bookmark-and-replay-event-workflow
- description: Preview the impact of a bulk retry, start it, then poll until it completes.
  name: Hookdeck Bulk Retry Failed Events
  slug: hookdeck-bulk-retry-failed-events-workflow
- description: Find a queued event for a connection, inspect it, then cancel its delivery.
  name: Hookdeck Cancel a Pending Event
  slug: hookdeck-cancel-pending-event-workflow
- description: Read a source, disable it to stop ingestion, then delete it.
  name: Hookdeck Decommission a Source
  slug: hookdeck-decommission-source-workflow
- description: Create a connection along with its source and destination in a single call.
  name: Hookdeck Create an Inline Connection
  slug: hookdeck-inline-connection-workflow
- description: Resolve an event, list its delivery attempts, then read the latest attempt body.
  name: Hookdeck Investigate Event Delivery Attempts
  slug: hookdeck-investigate-event-attempts-workflow
- description: Read a connection, pause it for maintenance, then unpause it to drain held events.
  name: Hookdeck Pause and Resume a Connection
  slug: hookdeck-pause-resume-connection-workflow
- description: Create a source, create a destination, then wire them together with a connection.
  name: Hookdeck Provision a Connection
  slug: hookdeck-provision-connection-workflow
- description: Find a recent request, inspect it, replay it, then list the events it produced.
  name: Hookdeck Replay an Inbound Request
  slug: hookdeck-replay-request-workflow
- description: Find the most recent failed event, inspect it, and retry delivery.
  name: Hookdeck Retry a Failed Event
  slug: hookdeck-retry-failed-event-workflow
- description: Test new code against a sample request before persisting it to an existing transformation.
  name: Hookdeck Test Then Update a Transformation
  slug: hookdeck-update-transformation-workflow
- description: Idempotently create or update a connection by name, then confirm the result.
  name: Hookdeck Upsert a Connection by Name
  slug: hookdeck-upsert-connection-workflow
artifact_total: 102
collections:
- collection_type: postman
  name: Hookdeck Bookmarks API
  slug: postman-hookdeck-bookmarks-api
- collection_type: postman
  name: Hookdeck Bulk Operations API
  slug: postman-hookdeck-bulk-operations-api
- collection_type: postman
  name: Hookdeck Connections API
  slug: postman-hookdeck-connections-api
- collection_type: postman
  name: Hookdeck Destinations API
  slug: postman-hookdeck-destinations-api
- collection_type: postman
  name: Hookdeck Events API
  slug: postman-hookdeck-events-api
- collection_type: postman
  name: Hookdeck Integrations API
  slug: postman-hookdeck-integrations-api
- collection_type: postman
  name: Hookdeck Issues API
  slug: postman-hookdeck-issues-api
- collection_type: postman
  name: Hookdeck Metrics API
  slug: postman-hookdeck-metrics-api
- collection_type: postman
  name: Hookdeck Notifications API
  slug: postman-hookdeck-notifications-api
- collection_type: postman
  name: Hookdeck Requests API
  slug: postman-hookdeck-requests-api
- collection_type: postman
  name: Hookdeck Sources API
  slug: postman-hookdeck-sources-api
- collection_type: postman
  name: Hookdeck Transformations API
  slug: postman-hookdeck-transformations-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hookdeck Bookmarks Attempts API
  slug: open-hookdeck-attempts-api
- collection_type: open
  name: Hookdeck Attempts Bookmarks API
  slug: open-hookdeck-bookmarks-api
- collection_type: open
  name: Hookdeck Bookmarks Attempts Bulk cancel events API
  slug: open-hookdeck-bulk-cancel-events-api
- collection_type: open
  name: Hookdeck Bulk Operations API
  slug: open-hookdeck-bulk-operations-api
- collection_type: open
  name: Hookdeck Bookmarks Attempts Bulk retry events API
  slug: open-hookdeck-bulk-retry-events-api
- collection_type: open
  name: Hookdeck Bookmarks Attempts Bulk retry ignored events API
  slug: open-hookdeck-bulk-retry-ignored-events-api
- collection_type: open
  name: Hookdeck Bookmarks Attempts Bulk retry requests API
  slug: open-hookdeck-bulk-retry-requests-api
- collection_type: open
  name: Hookdeck Bookmarks Attempts Connections API
  slug: open-hookdeck-connections-api
- collection_type: open
  name: Hookdeck Bookmarks Attempts Destinations API
  slug: open-hookdeck-destinations-api
- collection_type: open
  name: Hookdeck Bookmarks Attempts Events API
  slug: open-hookdeck-events-api
- collection_type: open
  name: Hookdeck Bookmarks Attempts Integrations API
  slug: open-hookdeck-integrations-api
- collection_type: open
  name: Hookdeck Bookmarks Attempts Issue Triggers API
  slug: open-hookdeck-issue-triggers-api
- collection_type: open
  name: Hookdeck Bookmarks Attempts Issues API
  slug: open-hookdeck-issues-api
- collection_type: open
  name: Hookdeck Bookmarks Attempts Metrics API
  slug: open-hookdeck-metrics-api
- collection_type: open
  name: Hookdeck Bookmarks Attempts Notifications API
  slug: open-hookdeck-notifications-api
- collection_type: open
  name: Hookdeck Bookmarks Attempts Requests API
  slug: open-hookdeck-requests-api
- collection_type: open
  name: Hookdeck Bookmarks Attempts Sources API
  slug: open-hookdeck-sources-api
- collection_type: open
  name: Hookdeck Bookmarks Attempts Transformations API
  slug: open-hookdeck-transformations-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/hookdeck/hookdeck-api-schema/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/hookdeck/hookdeck-api-schema/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/hookdeck/.github/blob/master/CODE_OF_CONDUCT.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hookdeck-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hookdeck-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hookdeck-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/hookdeck/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hookdeck-attach-integration-to-source-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hookdeck-author-transformation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hookdeck-bookmark-and-replay-event-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hookdeck-bulk-retry-failed-events-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hookdeck-cancel-pending-event-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hookdeck-decommission-source-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hookdeck-inline-connection-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hookdeck-investigate-event-attempts-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hookdeck-pause-resume-connection-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hookdeck-provision-connection-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hookdeck-replay-request-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hookdeck-retry-failed-event-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hookdeck-update-transformation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hookdeck-upsert-connection-workflow.yml
- group: docs
  title: ''
  type: Documentation
  url: https://hookdeck.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://hookdeck.com/docs/api
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.hookdeck.com/2025-07-01/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://hookdeck.com/docs/hookdeck-basics
- group: auth
  title: ''
  type: Authentication
  url: https://hookdeck.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://hookdeck.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/hookdeck-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hookdeck-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hookdeck-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hookdeck-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://hookdeck.com/blog
- group: build
  title: ''
  type: CLI
  url: https://hookdeck.com/docs/cli
- group: build
  title: ''
  type: CLI
  url: https://github.com/hookdeck/hookdeck-cli
- group: build
  title: ''
  type: SDKs
  url: https://github.com/hookdeck/hookdeck-typescript-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/hookdeck/hookdeck-go-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/hookdeck/hookdeck-python-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/hookdeck/hookdeck-dotnet-sdk
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@hookdeck/sdk
- group: other
  title: ''
  type: TerraformProvider
  url: https://registry.terraform.io/providers/hookdeck/hookdeck/latest/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hookdeck
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/hookdeck/hookdeck-api-schema
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/hookdeck/outpost
- group: other
  title: ''
  type: OpenSource
  url: https://hookdeck.com/outpost
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/hookdeck/webhook-skills
- group: start
  title: ''
  type: GettingStarted
  url: https://hookdeck.com/docs/use-cases/receive-webhooks/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://hookdeck.com/docs/use-cases/send-webhooks
- group: docs
  title: ''
  type: Documentation
  url: https://hookdeck.com/event-gateway
- group: docs
  title: ''
  type: Documentation
  url: https://hookdeck.com/outpost
- group: operate
  title: ''
  type: ChangeLog
  url: https://hookdeck.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hookdeck.com/
- group: start
  title: ''
  type: Signup
  url: https://dashboard.hookdeck.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.hookdeck.com/signin
- group: operate
  title: ''
  type: Contact
  url: https://hookdeck.com/contact
- group: company
  title: ''
  type: About
  url: https://hookdeck.com/company
- group: other
  title: ''
  type: Customers
  url: https://hookdeck.com/customers
- group: company
  title: ''
  type: Careers
  url: https://hookdeck.com/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hookdeck.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hookdeck.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://trust.hookdeck.com
- group: other
  title: ''
  type: DataProcessingAddendum
  url: https://hookdeck.com/dpa
- group: other
  title: ''
  type: X
  url: https://x.com/Hookdeck
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hookdeck
- group: operate
  title: ''
  type: Slack
  url: https://join.slack.com/t/hookdeckdevelopers/shared_invite/zt-yw7hlyzp-EQuO3QvdiBlH9Tz2KZg5MQ
created: '2025-08-19'
description: Hookdeck is a Toronto-based webhook and event-infrastructure platform. The Hookdeck Event Gateway sits between webhook senders and your services to receive, verify, queue, retry, transform, filter, route, and observe events reliably at scale. Hookdeck exposes a fully versioned REST Admin API, a CLI for local development, language SDKs (TypeScript, Go, Python, .NET), a Terraform provider, and the open-source Outpost project for self-hostable outbound webhook delivery.
finops:
- name: Hookdeck Finops
  service_category: API
  slug: hookdeck-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hookdeck.png
json_schemas:
- name: Hookdeck EventAttempt
  property_count: 20
  slug: hookdeck-attempt
- name: Hookdeck Connection
  property_count: 12
  slug: hookdeck-connection
- name: Hookdeck Destination
  property_count: 9
  slug: hookdeck-destination
- name: Hookdeck Event
  property_count: 18
  slug: hookdeck-event
- name: Hookdeck Issue
  property_count: 0
  slug: hookdeck-issue
- name: Hookdeck Request
  property_count: 13
  slug: hookdeck-request
- name: Hookdeck Source
  property_count: 11
  slug: hookdeck-source
- name: Hookdeck Transformation
  property_count: 9
  slug: hookdeck-transformation
jsonld:
- class_count: 41
  name: Hookdeck Context
  property_count: 18
  slug: hookdeck-context
layout: provider
modified: '2026-05-25'
name: Hookdeck
nav: Providers
network: true
overview: 'Hookdeck publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Connections API, Sources API, Destinations API, and 14 more. Tagged areas include Webhook, Event Gateways, Gateways, Event, and Event Infrastructure.


  The Hookdeck catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Hookdeck''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, CLI, and 57 more developer resources.'
plans:
- name: Hookdeck Plans Pricing
  plan_count: 3
  slug: hookdeck-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Hookdeck Rate Limits
  slug: hookdeck-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Hookdeck API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: hookdeck-jsonschema-spectral-rules
score:
  band: strong
  composite: 56.5
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 9.8
    contract_quality: 76.4
    developer_ergonomics: 83.3
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 56.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hookdeck/refs/heads/main/screenshots/hookdeck-2026-06-20T182825.png
security:
- kind: authentication
  name: Hookdeck Authentication
  slug: hookdeck-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Hookdeck Domain Security
  slug: hookdeck-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 39
skills:
- name: chargebee-webhooks
  slug: chargebee-webhooks
- name: claude-managed-agents-webhooks
  slug: claude-managed-agents-webhooks
- name: clerk-webhooks
  slug: clerk-webhooks
- name: cursor-webhooks
  slug: cursor-webhooks
- name: deepgram-webhooks
  slug: deepgram-webhooks
- name: discord-webhooks
  slug: discord-webhooks
- name: elevenlabs-webhooks
  slug: elevenlabs-webhooks
- name: fusionauth-webhooks
  slug: fusionauth-webhooks
- name: gemini-webhooks
  slug: gemini-webhooks
- name: github-webhooks
  slug: github-webhooks
- name: gitlab-webhooks
  slug: gitlab-webhooks
- name: hookdeck-event-gateway-webhooks
  slug: hookdeck-event-gateway-webhooks
- name: hookdeck-event-gateway
  slug: hookdeck-event-gateway
- name: hubspot-webhooks
  slug: hubspot-webhooks
- name: huggingface-webhooks
  slug: huggingface-webhooks
- name: intercom-webhooks
  slug: intercom-webhooks
- name: knock-webhooks
  slug: knock-webhooks
- name: linear-webhooks
  slug: linear-webhooks
- name: mailgun-webhooks
  slug: mailgun-webhooks
- name: notion-webhooks
  slug: notion-webhooks
- name: openai-webhooks
  slug: openai-webhooks
- name: openclaw-webhooks
  slug: openclaw-webhooks
- name: orb-webhooks
  slug: orb-webhooks
- name: outpost
  slug: outpost
slug: hookdeck
tags:
- Webhook
- Event Gateways
- Gateways
- Event
- Event Infrastructure
- Event-Driven
- Messaging
- Queues
- Retries
- Transformation
- Observability
---
