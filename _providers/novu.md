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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 92
  human_in_the_loop: 92
  name: Novu Agentic Access
  operation_count: 135
  slug: novu-agentic-access
  summary_line: 135 operations · 92 acting · 92 human-in-the-loop
api_count: 19
apis:
- description: Client-side API and React Inbox component for rendering an embedded in-app notification center, marking notifications as read / archived / snoozed, and managing per-user notification preferences direc
  name: Novu Inbox / In-App API
  slug: inbox-api
- description: Code-first workflow framework that lets developers define notification workflows in TypeScript / JavaScript using `@novu/framework`, then sync them to Novu Cloud (or a self-hosted instance) via the `n
  name: Novu Framework (Code-First Workflows)
  slug: framework
- description: Official Model Context Protocol server exposing the Novu REST API surface as MCP tools so AI agents (Claude Desktop, Cursor, agent frameworks) can trigger workflows, manage subscribers, list workflows
  name: Novu MCP Server
  slug: mcp-server
- description: The Activity API from Novu — 1 operation(s) for activity.
  name: Novu Activity API
  slug: novu-activity-api
- description: The Channel Connections API from Novu — 2 operation(s) for channel connections.
  name: Novu Channel Connections API
  slug: novu-channel-connections-api
- description: The Channel Endpoints API from Novu — 2 operation(s) for channel endpoints.
  name: Novu Channel Endpoints API
  slug: novu-channel-endpoints-api
- description: The Contexts API from Novu — 2 operation(s) for contexts.
  name: Novu Contexts API
  slug: novu-contexts-api
- description: Used to manage your inbound email domains.
  name: Novu Domains API
  slug: novu-domains-api
- description: The Environment Variables API from Novu — 3 operation(s) for environment variables.
  name: Novu Environment Variables API
  slug: novu-environment-variables-api
- description: Environments allow you to manage different stages of your application development lifecycle. Each environment has its own set of API keys and configurations, enabling you to separate development, stag
  name: Novu Environments API
  slug: novu-environments-api
- description: Events represent a change in state of a subscriber. They are used to trigger workflows, and enable you to send notifications to subscribers based on their actions.
  name: Novu Events API
  slug: novu-events-api
- description: With the help of the Integration Store, you can easily integrate your favorite delivery provider. During the runtime of the API, the Integrations Store is responsible for storing the configurations of
  name: Novu Integrations API
  slug: novu-integrations-api
- description: Layouts are reusable wrappers for your email notifications.
  name: Novu Layouts API
  slug: novu-layouts-api
- description: A message in Novu represents a notification delivered to a recipient on a particular channel. Messages contain information about the request that triggered its delivery, a view of the data sent to the
  name: Novu Messages API
  slug: novu-messages-api
- description: The Notifications API from Novu — 2 operation(s) for notifications.
  name: Novu Notifications API
  slug: novu-notifications-api
- description: A subscriber in Novu represents someone who should receive a message. A subscriber's profile information contains important attributes about the subscriber that will be used in messages (name, email).
  name: Novu Subscribers API
  slug: novu-subscribers-api
- description: Topics are a way to group subscribers together so that they can be notified of events at once. A topic is identified by a custom key. This can be helpful for things like sending out marketing emails o
  name: Novu Topics API
  slug: novu-topics-api
- description: Used to localize your notifications to different languages.
  name: Novu Translations API
  slug: novu-translations-api
- description: All notifications are sent via a workflow. Each workflow acts as a container for the logic and blueprint that are associated with a type of notification in your system.
  name: Novu Workflows API
  slug: novu-workflows-api
arazzos:
- description: Create many subscribers in one call, then broadcast a single announcement to all subscribers.
  name: Novu Bulk Onboard Subscribers and Broadcast an Announcement
  slug: novu-bulk-onboard-and-broadcast-workflow
- description: Define a new in-app notification workflow, then immediately trigger it to a subscriber.
  name: Novu Create a Workflow and Trigger It
  slug: novu-create-workflow-and-trigger-workflow
- description: Confirm a subscriber, audit their topic subscriptions, then delete the subscriber and all associated data.
  name: Novu Offboard a Subscriber
  slug: novu-offboard-subscriber-workflow
- description: Create a subscriber, trigger a workflow to them, and read back the resulting event.
  name: Novu Onboard a Subscriber and Send Their First Notification
  slug: novu-onboard-subscriber-and-notify-workflow
- description: Create a channel integration, promote it to primary for its channel, and confirm it is active.
  name: Novu Provision a Delivery Integration and Make It Primary
  slug: novu-provision-integration-and-set-primary-workflow
- description: Confirm a subscriber exists, set their workflow channel preferences, then trigger a respectful notification.
  name: Novu Set Subscriber Preferences Then Notify
  slug: novu-set-preferences-then-notify-workflow
- description: Find a subscriber by search, subscribe them to a topic, and confirm the subscription.
  name: Novu Subscribe an Existing Subscriber to a Topic
  slug: novu-subscribe-existing-to-topic-workflow
- description: Confirm a subscriber, read their unread in-app inbox, then mark all notifications as read.
  name: Novu Subscriber Inbox Triage
  slug: novu-subscriber-inbox-triage-workflow
- description: Create a topic, subscribe an audience to it, and trigger a single notification to the whole topic.
  name: Novu Topic Broadcast Campaign
  slug: novu-topic-broadcast-campaign-workflow
- description: Trigger a workflow to a subscriber, then inspect the event and the per-channel messages it produced.
  name: Novu Trigger a Notification and Verify Delivery
  slug: novu-trigger-and-verify-delivery-workflow
- description: Trigger a workflow with a caller-supplied transactionId, then cancel any pending delay or digest using that id.
  name: Novu Trigger a Deferred Notification and Cancel It
  slug: novu-trigger-then-cancel-workflow
- description: Remove a set of subscribers from a topic, then list the remaining subscriptions to confirm.
  name: Novu Unsubscribe Subscribers From a Topic
  slug: novu-unsubscribe-from-topic-workflow
artifact_total: 141
asyncapis:
- description: Real-time WebSocket interface used by the Novu Notification Center / Inbox (the `<Inbox />` React component, `@novu/react-native`, the headless `@novu/js` SDK, and any custom client). The transport is
  name: Novu Notification Center WebSocket API
  slug: novu-asyncapi
collections:
- collection_type: postman
  name: Novu API
  slug: postman-novu
- collection_type: open
  name: Novu API
  slug: open-novu
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/novu-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/novu-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/novu-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/novu/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/novu-bulk-onboard-and-broadcast-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/novu-create-workflow-and-trigger-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/novu-offboard-subscriber-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/novu-onboard-subscriber-and-notify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/novu-provision-integration-and-set-primary-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/novu-set-preferences-then-notify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/novu-subscribe-existing-to-topic-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/novu-subscriber-inbox-triage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/novu-topic-broadcast-campaign-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/novu-trigger-and-verify-delivery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/novu-trigger-then-cancel-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/novu-unsubscribe-from-topic-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://novu.co
- group: start
  title: ''
  type: Portal
  url: https://docs.novu.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.novu.co
- group: start
  title: ''
  type: Signup
  url: https://web.novu.co/auth/signup
- group: start
  title: ''
  type: Login
  url: https://web.novu.co
- group: commercial
  title: ''
  type: Pricing
  url: https://novu.co/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/novu-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/novu-finops.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/novu-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://novu.co/blog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/novuhq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/novuhq
- group: build
  title: novuhq/novu (main monorepo, 39k+ stars)
  type: GitHubRepository
  url: https://github.com/novuhq/novu
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/novuhq/novu
- group: commercial
  title: MIT License
  type: License
  url: https://github.com/novuhq/novu/blob/next/LICENSE
- group: build
  title: ''
  type: SDKs
  url: https://docs.novu.co/sdks/introduction
- group: build
  title: Novu CLI
  type: CLI
  url: https://docs.novu.co/community/run-in-local-machine
- group: other
  title: Novu Framework
  type: Framework
  url: https://docs.novu.co/framework/overview
- group: other
  title: Novu Inbox
  type: Inbox
  url: https://docs.novu.co/platform/inbox/overview
- group: operate
  title: ''
  type: ChangeLog
  url: https://novu.co/changelog
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/novuhq/novu/releases
- group: operate
  title: ''
  type: StatusPage
  url: https://status.novu.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://novu.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://novu.co/privacy
- group: operate
  title: Novu Discord
  type: Community
  url: https://discord.gg/novu
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/novu
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@novuhq
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.novu.co/llms.txt
- group: design
  title: ''
  type: SpectralRules
  url: rules/novu-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/novu-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/novu-context.jsonld
- group: build
  title: Novu MCP Server
  type: Tools
  url: https://github.com/novuhq/novu-mcp-server
- group: build
  title: Maily — block-based email editor (used by Novu Cloud)
  type: Tools
  url: https://github.com/novuhq/maily.to
- group: build
  title: actions-novu-sync — GitHub Action to sync workflows to Novu Cloud
  type: Tools
  url: https://github.com/novuhq/actions-novu-sync
- group: build
  title: Stripe → Novu webhook bridge
  type: Tools
  url: https://github.com/novuhq/stripe-to-novu-webhooks
- group: build
  title: Clerk → Novu webhook bridge
  type: Tools
  url: https://github.com/novuhq/clerk-to-novu-webhooks
- group: build
  title: Segment → Novu webhook bridge
  type: Tools
  url: https://github.com/novuhq/segment-to-novu-webhooks
- group: build
  title: Community Kubernetes manifests for self-hosting
  type: Tools
  url: https://github.com/novuhq/community-k8s
- group: learn
  title: Inbox Playground
  type: Tutorials
  url: https://github.com/novuhq/inbox-playground
- group: learn
  title: Novu Examples
  type: Tutorials
  url: https://github.com/novuhq/examples
- group: learn
  title: Awesome Novu
  type: Tutorials
  url: https://github.com/novuhq/awesome-novu
- group: learn
  title: ''
  type: Tutorials
  url: https://docs.novu.co/guides
created: '2026-05-23'
description: Novu is the open-source notification infrastructure for developers. A single REST API and workflow engine route a triggered event across in-app inbox, email, SMS, push, chat (Slack / Discord / MS Teams / WhatsApp) and custom channels — with subscriber preferences, topics, digest, snooze, and full workflow orchestration on top. Ships with the embeddable React Inbox component, the Novu Framework for code-first workflow authoring, language SDKs for nine ecosystems, a Postman collection, an MCP server, GitHub Action sync, the Maily block-based email editor, framework starters for Next.js / Remix / Nuxt / SvelteKit, and webhook bridges for Stripe / Clerk / Segment.
examples:
- key_count: 1
  name: Novu Add Subscribers To Topic Example
  slug: novu-add-subscribers-to-topic-example
- key_count: 2
  name: Novu Broadcast Event Example
  slug: novu-broadcast-event-example
- key_count: 1
  name: Novu Bulk Create Subscribers Example
  slug: novu-bulk-create-subscribers-example
- key_count: 3
  name: Novu Create Environment Example
  slug: novu-create-environment-example
- key_count: 5
  name: Novu Create Integration Example
  slug: novu-create-integration-example
- key_count: 9
  name: Novu Create Subscriber Example
  slug: novu-create-subscriber-example
- key_count: 2
  name: Novu Create Topic Example
  slug: novu-create-topic-example
- key_count: 4
  name: Novu Error Response Example
  slug: novu-error-response-example
- key_count: 5
  name: Novu List Messages Example
  slug: novu-list-messages-example
- key_count: 1
  name: Novu Trigger Event Bulk Example
  slug: novu-trigger-event-bulk-example
- key_count: 5
  name: Novu Trigger Event Example
  slug: novu-trigger-event-example
- key_count: 11
  name: Novu Workflow Response Example
  slug: novu-workflow-response-example
features:
- description: Author a single workflow tree that fans out across in-app, email, SMS, push, and chat with branching, delay, and digest steps.
  name: Multi-channel Workflow Orchestration
- description: Drop-in <Inbox /> React (and React Native) component with per-user preferences, read / archive / snooze, themes (Novu / Notion / Linear), and full headless API access.
  name: Embedded React Inbox
- description: First-class Subscribers resource with credentials per channel, locale, timezone, preferences, and bulk import.
  name: Subscriber Identity
- description: Named broadcast groups subscribed by users for one-call fan-out to thousands of subscribers.
  name: Topics for Fan-out
- description: Aggregate high-frequency triggers into a single delivery using configurable digest windows and back-off keys.
  name: Digest Engine
- description: Define workflows in TypeScript using @novu/framework and sync to Novu Cloud via novu-sync or a GitHub Action.
  name: Code-First Framework
- description: WYSIWYG block-based editor (open-sourced as Maily.to) powered by React Email under the hood.
  name: Block-Based Email Editor
- description: Reusable tenant and organization context objects referenced by trigger payloads for multi-tenant routing.
  name: Tenant / Context Objects
- description: IETF-style RateLimit-* headers on every response, Idempotency-Key on every mutating request.
  name: Idempotency + RateLimit Headers
- description: Official Model Context Protocol server exposing the Novu REST API to AI agents.
  name: MCP Server
- description: Apache-/MIT-licensed monorepo with Docker Compose and community Kubernetes manifests for fully self-hosted deployments.
  name: Self-Hosting
- description: TypeScript, Python, Go, PHP, C#, Java, Elixir, Kotlin, Ruby, Rust, .NET clients.
  name: 9 Language SDKs
finops:
- name: Novu Finops
  service_category: API
  slug: novu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/novu.png
integrations:
- description: Outbound email integration via SendGrid credentials.
  name: SendGrid
- description: Outbound email integration via Mailgun.
  name: Mailgun
- description: Outbound email integration via Resend.
  name: Resend
- description: Outbound transactional email via Postmark.
  name: Postmark
- description: Outbound email via Amazon Simple Email Service.
  name: AWS SES
- description: SMS delivery via Twilio.
  name: Twilio
- description: SMS delivery via MessageBird.
  name: MessageBird
- description: SMS delivery via Plivo.
  name: Plivo
- description: Mobile push delivery via FCM.
  name: Firebase Cloud Messaging
- description: iOS push delivery via APNs.
  name: Apple Push Notification Service
- description: Push delivery via OneSignal.
  name: OneSignal
- description: Chat notifications to Slack channels and users.
  name: Slack
- description: Chat notifications to MS Teams channels.
  name: Microsoft Teams
- description: Chat notifications to Discord channels.
  name: Discord
- description: Conversational notifications via WhatsApp.
  name: WhatsApp
- description: Billing-event-to-notification bridge via stripe-to-novu-webhooks.
  name: Stripe
- description: Authentication-event-to-notification bridge via clerk-to-novu-webhooks.
  name: Clerk
- description: CDP-event-to-notification bridge via segment-to-novu-webhooks.
  name: Segment
- description: First-class React Inbox component and Next.js helpers.
  name: React
- description: actions-novu-sync syncs framework workflows to Novu Cloud on every push.
  name: GitHub Actions
json_schemas:
- name: BulkSubscriberCreateDto
  property_count: 1
  slug: novu-bulk-subscriber-create-dto
- name: BulkTriggerEventDto
  property_count: 1
  slug: novu-bulk-trigger-event-dto
- name: CreateEnvironmentRequestDto
  property_count: 3
  slug: novu-create-environment-request-dto
- name: CreateIntegrationRequestDto
  property_count: 11
  slug: novu-create-integration-request-dto
- name: CreateSubscriberRequestDto
  property_count: 9
  slug: novu-create-subscriber-request-dto
- name: CreateWorkflowDto
  property_count: 12
  slug: novu-create-workflow-dto
- name: EnvironmentResponseDto
  property_count: 8
  slug: novu-environment-response-dto
- name: ErrorDto
  property_count: 6
  slug: novu-error-dto
- name: IntegrationResponseDto
  property_count: 16
  slug: novu-integration-response-dto
- name: LayoutResponseDto
  property_count: 13
  slug: novu-layout-response-dto
- name: MessageResponseDto
  property_count: 35
  slug: novu-message-response-dto
- name: SubscriberPayloadDto
  property_count: 10
  slug: novu-subscriber-payload-dto
- name: SubscriberResponseDto
  property_count: 20
  slug: novu-subscriber-response-dto
- name: TopicResponseDto
  property_count: 5
  slug: novu-topic-response-dto
- name: TriggerEventRequestDto
  property_count: 8
  slug: novu-trigger-event-request-dto
- name: TriggerEventResponseDto
  property_count: 6
  slug: novu-trigger-event-response-dto
- name: UpdateEnvironmentRequestDto
  property_count: 6
  slug: novu-update-environment-request-dto
- name: UpdateIntegrationRequestDto
  property_count: 8
  slug: novu-update-integration-request-dto
- name: UpdateWorkflowDto
  property_count: 12
  slug: novu-update-workflow-dto
- name: WorkflowResponseDto
  property_count: 23
  slug: novu-workflow-response-dto
json_structures:
- name: Novu Bulk Subscriber Create Dto Structure
  property_count: 0
  slug: novu-bulk-subscriber-create-dto-structure
- name: Novu Bulk Trigger Event Dto Structure
  property_count: 0
  slug: novu-bulk-trigger-event-dto-structure
- name: Novu Create Environment Request Dto Structure
  property_count: 0
  slug: novu-create-environment-request-dto-structure
- name: Novu Create Integration Request Dto Structure
  property_count: 0
  slug: novu-create-integration-request-dto-structure
- name: Novu Create Subscriber Request Dto Structure
  property_count: 0
  slug: novu-create-subscriber-request-dto-structure
- name: Novu Create Workflow Dto Structure
  property_count: 0
  slug: novu-create-workflow-dto-structure
- name: Novu Environment Response Dto Structure
  property_count: 0
  slug: novu-environment-response-dto-structure
- name: Novu Error Dto Structure
  property_count: 0
  slug: novu-error-dto-structure
- name: Novu Integration Response Dto Structure
  property_count: 0
  slug: novu-integration-response-dto-structure
- name: Novu Layout Response Dto Structure
  property_count: 0
  slug: novu-layout-response-dto-structure
- name: Novu Message Response Dto Structure
  property_count: 0
  slug: novu-message-response-dto-structure
- name: Novu Subscriber Payload Dto Structure
  property_count: 0
  slug: novu-subscriber-payload-dto-structure
- name: Novu Subscriber Response Dto Structure
  property_count: 0
  slug: novu-subscriber-response-dto-structure
- name: Novu Topic Response Dto Structure
  property_count: 0
  slug: novu-topic-response-dto-structure
- name: Novu Trigger Event Request Dto Structure
  property_count: 0
  slug: novu-trigger-event-request-dto-structure
- name: Novu Trigger Event Response Dto Structure
  property_count: 0
  slug: novu-trigger-event-response-dto-structure
- name: Novu Update Environment Request Dto Structure
  property_count: 0
  slug: novu-update-environment-request-dto-structure
- name: Novu Update Integration Request Dto Structure
  property_count: 0
  slug: novu-update-integration-request-dto-structure
- name: Novu Update Workflow Dto Structure
  property_count: 0
  slug: novu-update-workflow-dto-structure
- name: Novu Workflow Response Dto Structure
  property_count: 0
  slug: novu-workflow-response-dto-structure
jsonld:
- class_count: 20
  name: Novu Context
  property_count: 105
  slug: novu-context
layout: provider
modified: '2026-05-29'
name: Novu
nav: Providers
network: true
overview: 'Novu publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Inbox / In-App API, Activity API, Channel Connections API, and 14 more. Tagged areas include Notifications, Messaging, In App, Email, and SMS.


  The Novu catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Novu''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, engineering blog, GitHub presence, and 51 more developer resources.'
plans:
- name: Novu Plans Pricing
  plan_count: 4
  slug: novu-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 4
  name: Novu Rate Limits
  slug: novu-rate-limits
rules:
- name: Novu API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: novu-asyncapi-spectral-rules
- name: Novu API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: novu-jsonschema-spectral-rules
- name: Novu API Rules
  rule_count: 48
  severity_counts:
    error: 9
    hint: 0
    info: 11
    warn: 28
  slug: novu-spectral-rules
score:
  band: strong
  composite: 65.0
  delta: -9.8
  facets:
    commercial_clarity: 84.2
    contract_quality: 81.5
    developer_ergonomics: 52.2
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 68.4
  previous_composite: 74.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/novu/refs/heads/main/screenshots/novu-2026-06-20T190442.png
security:
- kind: authentication
  name: Novu Authentication
  slug: novu-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Novu Domain Security
  slug: novu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: novu
solutions:
- description: Managed Novu hosted by the Novu team. Free / Pro / Team / Enterprise plans.
  name: Novu Cloud
- description: Run the full Novu monorepo on your own infrastructure under MIT license. Docker Compose for development, community Kubernetes manifests for production.
  name: Self-Hosted Open Source
- description: EU-resident Novu Cloud deployment at eu.api.novu.co.
  name: Novu EU Cloud
- description: HIPAA BAA, custom SSO, SCIM directory sync, and custom data-residency regions (US, EU, UK, Singapore, Australia, Japan, South Korea).
  name: Enterprise (HIPAA, SSO, SCIM)
tags:
- Notifications
- Messaging
- In App
- Email
- SMS
- Push
- Chat
- Workflows
- Open Source
- Subscribers
- Topics
- Inbox
- Workflow Orchestration
- Multi Channel
- Digest
- MCP
- Framework
- React
use_cases:
- description: Welcome sequences combining transactional email, in-app inbox messages, and reminders.
  name: Product Onboarding
- description: Order confirmations, password resets, magic links, payment receipts, and shipping updates.
  name: Transactional Notifications
- description: Comment mentions, document shares, and review requests delivered to the in-app inbox and email.
  name: Real-Time Collaboration Alerts
- description: Trial reminders, renewal warnings, dunning, and cancellation flows driven by billing events.
  name: Subscription Lifecycle
- description: Sign-up confirmations, MFA prompts, suspicious-login alerts, and OTP codes.
  name: Authentication Events
- description: Product announcements and weekly digests fanned out via topics.
  name: Marketing Broadcasts
- description: On-call paging, deploy notifications, and incident updates routed through Slack / MS Teams.
  name: Operational Alerts
- description: Per-customer routing using tenant context and subscriber data inheritance.
  name: Multi-Tenant SaaS
- description: Agent workflows triggering Novu via the MCP server to keep humans in the loop.
  name: AI Agent Notifications
website: https://novu.co
---
