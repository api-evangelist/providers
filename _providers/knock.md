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
  band: agent-aware
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
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.6
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 78
  human_in_the_loop: 3
  name: Knock Agentic Access
  operation_count: 116
  slug: knock-agentic-access
  summary_line: 116 operations · 78 acting · 3 human-in-the-loop
api_count: 19
apis:
- description: An Audience is a segment of users.
  name: Knock Audiences API
  slug: knock-audiences-api
- description: A bulk operation is a set of changes applied across zero or more records triggered via a call to the Knock API and performed asynchronously.
  name: Knock Bulk operations API
  slug: knock-bulk-operations-api
- description: Channel data is data that is specific to a recipient and a channel, like push tokens, or one or more Slack connections.
  name: Knock Channel data API
  slug: knock-channel-data-api
- description: The Feeds API from Knock — 2 operation(s) for feeds.
  name: Knock Feeds API
  slug: knock-feeds-api
- description: The Guides API from Knock — 8 operation(s) for guides.
  name: Knock Guides API
  slug: knock-guides-api
- description: The Integrations API from Knock — 2 operation(s) for integrations.
  name: Knock Integrations API
  slug: knock-integrations-api
- description: A message sent to a single recipient on a channel.
  name: Knock Messages API
  slug: knock-messages-api
- description: The Microsoft Teams API from Knock — 4 operation(s) for microsoft teams.
  name: Knock Microsoft Teams API
  slug: knock-microsoft-teams-api
- description: An object represents a resource in your system that you want to map into Knock.
  name: Knock Objects API
  slug: knock-objects-api
- description: Preferences are a way to configure how notifications are sent to recipients. They are a set of configuration that determines whether a recipient should receive a notification for a given workflow on a
  name: Knock Preferences API
  slug: knock-preferences-api
- description: A provider represents a third-party service that Knock integrates with and is configured via a channel.
  name: Knock Providers API
  slug: knock-providers-api
- description: A schedule is a per-recipient, timezone-aware configuration for when to invoke a workflow.
  name: Knock Schedules API
  slug: knock-schedules-api
- description: The Slack API from Knock — 3 operation(s) for slack.
  name: Knock Slack API
  slug: knock-slack-api
- description: A subscription represents a connection between a recipient and an object, used to represent a list.
  name: Knock Subscriptions API
  slug: knock-subscriptions-api
- description: A tenant represents a top-level entity from your system, like a company, organization, account, or workspace.
  name: Knock Tenants API
  slug: knock-tenants-api
- description: A user is an individual from your system, represented in Knock. They are most commonly a recipient of a notification.
  name: Knock Users API
  slug: knock-users-api
- description: A workflow run represents an individual execution of a workflow for a specific recipient.
  name: Knock Workflow recipient runs API
  slug: knock-workflow-recipient-runs-api
- description: Operations for triggering and canceling workflow executions.
  name: Knock Workflow Triggers API
  slug: knock-workflow-triggers-api
- description: A workflow is a structured set of steps that is triggered to produce notifications sent over channels.
  name: Knock Workflows API
  slug: knock-workflows-api
artifact_total: 48
asyncapis:
- description: 'AsyncAPI specification for Knock''s real-time in-app notification feed transport. Knock exposes a Phoenix Channels WebSocket that pushes feed updates to subscribed clients. The connection is initiated '
  name: Knock Real-Time In-App Feed (Phoenix Channels)
  slug: knock-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Knock Audiences API
  slug: open-knock-audiences-api
- collection_type: open
  name: Knock Audiences Bulk operations API
  slug: open-knock-bulk-operations-api
- collection_type: open
  name: Knock Audiences Channel data API
  slug: open-knock-channel-data-api
- collection_type: open
  name: Knock Audiences Feeds API
  slug: open-knock-feeds-api
- collection_type: open
  name: Knock Audiences Guides API
  slug: open-knock-guides-api
- collection_type: open
  name: Knock Audiences Integrations API
  slug: open-knock-integrations-api
- collection_type: open
  name: Knock Audiences Messages API
  slug: open-knock-messages-api
- collection_type: open
  name: Knock Audiences Microsoft Teams API
  slug: open-knock-microsoft-teams-api
- collection_type: open
  name: Knock Audiences Objects API
  slug: open-knock-objects-api
- collection_type: open
  name: Knock Audiences Preferences API
  slug: open-knock-preferences-api
- collection_type: open
  name: Knock Audiences Providers API
  slug: open-knock-providers-api
- collection_type: open
  name: Knock Audiences Schedules API
  slug: open-knock-schedules-api
- collection_type: open
  name: Knock Audiences Slack API
  slug: open-knock-slack-api
- collection_type: open
  name: Knock Audiences Subscriptions API
  slug: open-knock-subscriptions-api
- collection_type: open
  name: Knock Audiences Tenants API
  slug: open-knock-tenants-api
- collection_type: open
  name: Knock Audiences Users API
  slug: open-knock-users-api
- collection_type: open
  name: Knock Audiences Workflow recipient runs API
  slug: open-knock-workflow-recipient-runs-api
- collection_type: open
  name: Knock Audiences Workflow Triggers API
  slug: open-knock-workflow-triggers-api
- collection_type: open
  name: Knock Audiences Workflows API
  slug: open-knock-workflows-api
- collection_type: open
  name: Knock API
  slug: open-knock
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/knock-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/knock-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/knock-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/knocklabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/knockcrm
- group: company
  title: ''
  type: Website
  url: https://knock.app/
- group: commercial
  title: ''
  type: Plans
  url: plans/knock-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/knock-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/knock-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.knock.app/llms.txt
created: '2026-05-08'
description: Knock is a notification infrastructure platform with workflows, channels (email, SMS, push, in-app), preferences, and digests. Stripe-style API for sending and orchestrating multi-channel notifications.
finops:
- name: Knock Finops
  service_category: Notifications
  slug: knock-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/knock.png
layout: provider
modified: '2026-05-29'
name: Knock
nav: Providers
network: true
overview: 'Knock publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Audiences API, Bulk operations API, Channel data API, and 16 more. Tagged areas include Notification, Email, SMS, Push, and Workflows.


  The Knock catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Knock''s developer surface includes authentication and 9 more developer resources.'
plans:
- name: Knock Plans Pricing
  plan_count: 1
  slug: knock-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Knock Rate Limits
  slug: knock-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Knock API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: knock-asyncapi-spectral-rules
score:
  band: thin
  composite: 31.1
  delta: 1.9
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 11.4
    contract_quality: 62.1
    developer_ergonomics: 21.4
    discoverability: 81.5
    governance: 11.4
    operational_transparency: 7.9
  previous_composite: 29.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/knock/refs/heads/main/screenshots/knock-2026-06-20T184119.png
security:
- kind: authentication
  name: Knock Authentication
  slug: knock-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Knock Domain Security
  slug: knock-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: knock
tags:
- Notification
- Email
- SMS
- Push
- Workflows
website: https://knock.app/
---
