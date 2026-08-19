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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: verified
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 112
  human_in_the_loop: 3
  name: Knock App Agentic Access
  operation_count: 181
  slug: knock-app-agentic-access
  summary_line: 181 operations · 112 acting · 3 human-in-the-loop
api_count: 35
apis:
- description: Outbound webhooks fire message lifecycle (sent, delivered, seen, read, interacted, archived, link_clicked, bounced, undelivered) and environment-change (workflow / email_layout / translation / partial
  name: Knock Outbound Webhooks
  slug: knock-webhooks
- description: Resources for managing your Knock account.
  name: Knock Accounts API
  slug: knock-app-accounts-api
- description: The API keys API from Knock — 1 operation(s) for api keys.
  name: Knock API keys API
  slug: knock-app-api-keys-api
- description: The Audiences API from Knock — 4 operation(s) for audiences.
  name: Knock Audiences API
  slug: knock-app-audiences-api
- description: Branches in Knock are a way to isolate changes to your Knock resources.
  name: Knock Branches API
  slug: knock-app-branches-api
- description: The Broadcasts API from Knock — 5 operation(s) for broadcasts.
  name: Knock Broadcasts API
  slug: knock-app-broadcasts-api
- description: The Bulk operations API from Knock — 12 operation(s) for bulk operations.
  name: Knock Bulk operations API
  slug: knock-app-bulk-operations-api
- description: The Channel data API from Knock — 2 operation(s) for channel data.
  name: Knock Channel data API
  slug: knock-app-channel-data-api
- description: The Channel Groups API from Knock — 2 operation(s) for channel groups.
  name: Knock Channel Groups API
  slug: knock-app-channel-groups-api
- description: The Channels API from Knock — 2 operation(s) for channels.
  name: Knock Channels API
  slug: knock-app-channels-api
- description: Commits are versioned changes to resources.
  name: Knock Commits API
  slug: knock-app-commits-api
- description: Email layouts wrap your email templates and provide a consistent look and feel.
  name: Knock Email layouts API
  slug: knock-app-email-layouts-api
- description: Environments are isolated instances of your account that map to your infrastructure.
  name: Knock Environments API
  slug: knock-app-environments-api
- description: The Feeds API from Knock — 2 operation(s) for feeds.
  name: Knock Feeds API
  slug: knock-app-feeds-api
- description: Guides let you define in-app guides that can be displayed to users based on priority and other conditions.
  name: Knock Guides API
  slug: knock-app-guides-api
- description: The Integrations API from Knock — 2 operation(s) for integrations.
  name: Knock Integrations API
  slug: knock-app-integrations-api
- description: The Members API from Knock — 2 operation(s) for members.
  name: Knock Members API
  slug: knock-app-members-api
- description: A message type allows you to specify an in-app schema that defines the fields available for your in-app notifications.
  name: Knock Message types API
  slug: knock-app-message-types-api
- description: The Messages API from Knock — 24 operation(s) for messages.
  name: Knock Messages API
  slug: knock-app-messages-api
- description: The Microsoft Teams API from Knock — 4 operation(s) for microsoft teams.
  name: Knock Microsoft Teams API
  slug: knock-app-microsoft-teams-api
- description: The Objects API from Knock — 19 operation(s) for objects.
  name: Knock Objects API
  slug: knock-app-objects-api
- description: Partials allow you to reuse content across templates.
  name: Knock Partials API
  slug: knock-app-partials-api
- description: The Preferences API from Knock — 16 operation(s) for preferences.
  name: Knock Preferences API
  slug: knock-app-preferences-api
- description: The Providers API from Knock — 7 operation(s) for providers.
  name: Knock Providers API
  slug: knock-app-providers-api
- description: The Schedules API from Knock — 3 operation(s) for schedules.
  name: Knock Schedules API
  slug: knock-app-schedules-api
- description: The Slack API from Knock — 3 operation(s) for slack.
  name: Knock Slack API
  slug: knock-app-slack-api
- description: The Subscriptions API from Knock — 4 operation(s) for subscriptions.
  name: Knock Subscriptions API
  slug: knock-app-subscriptions-api
- description: The Templates API from Knock — 1 operation(s) for templates.
  name: Knock Templates API
  slug: knock-app-templates-api
- description: The Tenants API from Knock — 4 operation(s) for tenants.
  name: Knock Tenants API
  slug: knock-app-tenants-api
- description: Translations are per-locale string files that can be used in your templates.
  name: Knock Translations API
  slug: knock-app-translations-api
- description: The Users API from Knock — 28 operation(s) for users.
  name: Knock Users API
  slug: knock-app-users-api
- description: The Variables API from Knock — 2 operation(s) for variables.
  name: Knock Variables API
  slug: knock-app-variables-api
- description: The Workflow recipient runs API from Knock — 2 operation(s) for workflow recipient runs.
  name: Knock Workflow recipient runs API
  slug: knock-app-workflow-recipient-runs-api
- description: The Workflow Triggers API from Knock — 2 operation(s) for workflow triggers.
  name: Knock Workflow Triggers API
  slug: knock-app-workflow-triggers-api
- description: Workflows let you express your cross-channel notification logic.
  name: Knock Workflows API
  slug: knock-app-workflows-api
arazzos:
- description: Bulk identify a batch of users, wait for the operation to complete, then notify them.
  name: Knock Bulk Identify Users and Notify
  slug: knock-app-bulk-identify-users-notify-workflow
- description: Bulk upsert objects in a collection, wait for completion, then notify one object.
  name: Knock Bulk Set Objects and Notify
  slug: knock-app-bulk-set-objects-notify-workflow
- description: Bulk upsert tenants, wait for the operation to complete, then list tenants to verify.
  name: Knock Bulk Set Tenants and Verify
  slug: knock-app-bulk-set-tenants-verify-workflow
- description: Identify a recipient, trigger a cancellable workflow, then cancel it by key.
  name: Knock Cancellable Workflow Trigger
  slug: knock-app-cancellable-workflow-trigger-workflow
- description: Identify a recipient, apply their notification preferences, then trigger a workflow for them.
  name: Knock Identify User, Set Preferences, and Trigger Workflow
  slug: knock-app-identify-user-set-preferences-trigger-workflow
- description: Identify a surviving user, merge a duplicate into it, then notify the merged user.
  name: Knock Merge Users and Re-notify
  slug: knock-app-merge-users-and-renotify-workflow
- description: Upsert an object, set its preference set, then audit messages sent to it.
  name: Knock Set Object Preferences and Audit Messages
  slug: knock-app-object-preferences-message-audit-workflow
- description: Create an object, subscribe recipients to it, then notify subscribers via a workflow.
  name: Knock Set Object, Add Subscriptions, and Notify
  slug: knock-app-object-subscriptions-notify-workflow
- description: Identify a user, register their channel data, then read their in-app feed.
  name: Knock Register Push Token and Read Feed
  slug: knock-app-register-push-token-and-read-feed-workflow
- description: Identify a recipient, create a recurring schedule, then verify it was registered.
  name: Knock Schedule a Recurring Workflow
  slug: knock-app-schedule-recurring-workflow-workflow
- description: Set a tenant, identify a member user, then notify them scoped to the tenant.
  name: Knock Tenant Onboarding and Notify
  slug: knock-app-tenant-onboarding-notify-workflow
- description: Trigger a workflow, find the resulting in-app message, then archive it.
  name: Knock Trigger Then Archive Feed Message
  slug: knock-app-trigger-then-archive-feed-message-workflow
- description: Trigger a workflow then locate the generated message and read its rendered content.
  name: Knock Trigger Workflow and Inspect Message Content
  slug: knock-app-trigger-workflow-inspect-message-content-workflow
- description: Trigger a workflow and poll its per-recipient run until it completes.
  name: Knock Trigger Workflow and Track Recipient Run
  slug: knock-app-trigger-workflow-track-recipient-run-workflow
artifact_total: 159
asyncapis:
- description: Knock fires outbound webhook events for message lifecycle (sent, delivered, seen, read, interacted, archived, link_clicked, bounced, undelivered) and for environment changes (workflow / email_layout /
  name: Knock Outbound Webhooks
  slug: knock-webhooks-asyncapi
collections:
- collection_type: postman
  name: Knock Audiences API
  slug: postman-knock-audiences-api
- collection_type: postman
  name: Knock Bulk Operations API
  slug: postman-knock-bulk-operations-api
- collection_type: postman
  name: Knock Channels API
  slug: postman-knock-channels-api
- collection_type: postman
  name: Knock Integrations API
  slug: postman-knock-integrations-api
- collection_type: postman
  name: Knock Management API (mAPI)
  slug: postman-knock-management-api
- collection_type: postman
  name: Knock Messages API
  slug: postman-knock-messages-api
- collection_type: postman
  name: Knock Notify API
  slug: postman-knock-notify-api
- collection_type: postman
  name: Knock Objects API
  slug: postman-knock-objects-api
- collection_type: postman
  name: Knock Providers API
  slug: postman-knock-providers-api
- collection_type: postman
  name: Knock Schedules API
  slug: postman-knock-schedules-api
- collection_type: postman
  name: Knock Tenants API
  slug: postman-knock-tenants-api
- collection_type: postman
  name: Knock Users API
  slug: postman-knock-users-api
- collection_type: postman
  name: Knock Workflows API
  slug: postman-knock-workflows-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Knock Audiences Accounts API
  slug: open-knock-app-accounts-api
- collection_type: open
  name: Knock Audiences Accounts API keys API
  slug: open-knock-app-api-keys-api
- collection_type: open
  name: Knock Accounts Audiences API
  slug: open-knock-app-audiences-api
- collection_type: open
  name: Knock Audiences Accounts Branches API
  slug: open-knock-app-branches-api
- collection_type: open
  name: Knock Audiences Accounts Broadcasts API
  slug: open-knock-app-broadcasts-api
- collection_type: open
  name: Knock Audiences Accounts Bulk operations API
  slug: open-knock-app-bulk-operations-api
- collection_type: open
  name: Knock Audiences Accounts Channel data API
  slug: open-knock-app-channel-data-api
- collection_type: open
  name: Knock Audiences Accounts Channel Groups API
  slug: open-knock-app-channel-groups-api
- collection_type: open
  name: Knock Audiences Accounts Channels API
  slug: open-knock-app-channels-api
- collection_type: open
  name: Knock Audiences Accounts Commits API
  slug: open-knock-app-commits-api
- collection_type: open
  name: Knock Audiences Accounts Email layouts API
  slug: open-knock-app-email-layouts-api
- collection_type: open
  name: Knock Audiences Accounts Environments API
  slug: open-knock-app-environments-api
- collection_type: open
  name: Knock Audiences Accounts Feeds API
  slug: open-knock-app-feeds-api
- collection_type: open
  name: Knock Audiences Accounts Guides API
  slug: open-knock-app-guides-api
- collection_type: open
  name: Knock Audiences Accounts Integrations API
  slug: open-knock-app-integrations-api
- collection_type: open
  name: Knock Audiences Accounts Members API
  slug: open-knock-app-members-api
- collection_type: open
  name: Knock Audiences Accounts Message types API
  slug: open-knock-app-message-types-api
- collection_type: open
  name: Knock Audiences Accounts Messages API
  slug: open-knock-app-messages-api
- collection_type: open
  name: Knock Audiences Accounts Microsoft Teams API
  slug: open-knock-app-microsoft-teams-api
- collection_type: open
  name: Knock Audiences Accounts Objects API
  slug: open-knock-app-objects-api
- collection_type: open
  name: Knock Audiences Accounts Partials API
  slug: open-knock-app-partials-api
- collection_type: open
  name: Knock Audiences Accounts Preferences API
  slug: open-knock-app-preferences-api
- collection_type: open
  name: Knock Audiences Accounts Providers API
  slug: open-knock-app-providers-api
- collection_type: open
  name: Knock Audiences Accounts Schedules API
  slug: open-knock-app-schedules-api
- collection_type: open
  name: Knock Audiences Accounts Slack API
  slug: open-knock-app-slack-api
- collection_type: open
  name: Knock Audiences Accounts Subscriptions API
  slug: open-knock-app-subscriptions-api
- collection_type: open
  name: Knock Audiences Accounts Templates API
  slug: open-knock-app-templates-api
- collection_type: open
  name: Knock Audiences Accounts Tenants API
  slug: open-knock-app-tenants-api
- collection_type: open
  name: Knock Audiences Accounts Translations API
  slug: open-knock-app-translations-api
- collection_type: open
  name: Knock Audiences Accounts Users API
  slug: open-knock-app-users-api
- collection_type: open
  name: Knock Audiences Accounts Variables API
  slug: open-knock-app-variables-api
- collection_type: open
  name: Knock Audiences Accounts Workflow recipient runs API
  slug: open-knock-app-workflow-recipient-runs-api
- collection_type: open
  name: Knock Audiences Accounts Workflow Triggers API
  slug: open-knock-app-workflow-triggers-api
- collection_type: open
  name: Knock Audiences Accounts Workflows API
  slug: open-knock-app-workflows-api
- collection_type: open
  name: Knock Audiences API
  slug: open-knock-audiences-api
- collection_type: open
  name: Knock Bulk Operations API
  slug: open-knock-bulk-operations-api
- collection_type: open
  name: Knock Channels API
  slug: open-knock-channels-api
- collection_type: open
  name: Knock Integrations API
  slug: open-knock-integrations-api
- collection_type: open
  name: Knock Management API (mAPI)
  slug: open-knock-management-api
- collection_type: open
  name: Knock Messages API
  slug: open-knock-messages-api
- collection_type: open
  name: Knock Notify API
  slug: open-knock-notify-api
- collection_type: open
  name: Knock Objects API
  slug: open-knock-objects-api
- collection_type: open
  name: Knock Providers API
  slug: open-knock-providers-api
- collection_type: open
  name: Knock Schedules API
  slug: open-knock-schedules-api
- collection_type: open
  name: Knock Tenants API
  slug: open-knock-tenants-api
- collection_type: open
  name: Knock Users API
  slug: open-knock-users-api
- collection_type: open
  name: Knock Workflows API
  slug: open-knock-workflows-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/knock-app-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/knock-app-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/knock-app-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/knock-app-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/knock-app-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/knock-app-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/knock-app-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/knock-app-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/knock-app-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/knock-app-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/knock-app-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/knock-app-sandbox.yml
- group: build
  title: ''
  type: CLI
  url: cli/knock-app-cli.yml
- group: design
  title: ''
  type: Components
  url: components/knock-app-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/knock-app-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/knock-app-audiences-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/knock-app-bulk-operations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/knock-app-channels-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/knock-app-integrations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/knock-app-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/knock-app-messages-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/knock-app-notify-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/knock-app-objects-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/knock-app-providers-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/knock-app-schedules-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/knock-app-tenants-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/knock-app-users-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/knock-app-workflows-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/knock/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/knock-app-bulk-identify-users-notify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/knock-app-bulk-set-objects-notify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/knock-app-bulk-set-tenants-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/knock-app-cancellable-workflow-trigger-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/knock-app-identify-user-set-preferences-trigger-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/knock-app-merge-users-and-renotify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/knock-app-object-preferences-message-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/knock-app-object-subscriptions-notify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/knock-app-register-push-token-and-read-feed-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/knock-app-schedule-recurring-workflow-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/knock-app-tenant-onboarding-notify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/knock-app-trigger-then-archive-feed-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/knock-app-trigger-workflow-inspect-message-content-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/knock-app-trigger-workflow-track-recipient-run-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://knock.app
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knock.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knock.app/api-reference/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knock.app/mapi
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.knock.app/getting-started/what-is-knock
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.knock.app/getting-started/quick-start/general
- group: start
  title: ''
  type: Signup
  url: https://dashboard.knock.app/signup
- group: auth
  title: ''
  type: Authentication
  url: https://docs.knock.app/api-reference/overview/authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.knock.app/api-reference/overview/rate-limits
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.knock.app/api-reference/overview/batch-rate-limits
- group: design
  title: ''
  type: Idempotency
  url: https://docs.knock.app/api-reference/overview/idempotent-requests
- group: design
  title: ''
  type: Pagination
  url: https://docs.knock.app/api-reference/overview/pagination
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.knock.app/api-reference/overview/errors
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.knock.app/api-reference/overview/error-codes
- group: operate
  title: ''
  type: StatusPage
  url: https://status.knock.app
- group: operate
  title: ''
  type: ChangeLog
  url: https://knock.app/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/knock-app-changelog.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://knock.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://knock.app/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://knock.app/legal/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.knock.app
- group: company
  title: ''
  type: Blog
  url: https://knock.app/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/knocklabs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-elixir
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-dotnet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-swift
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-flutter
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/javascript
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-mgmt-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-mgmt-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-mgmt-go
- group: build
  title: ''
  type: Tools
  url: https://github.com/knocklabs/knock-cli
- group: build
  title: ''
  type: Tools
  url: https://mcp.knock.app/mcp
- group: build
  title: ''
  type: Tools
  url: https://github.com/knocklabs/knock-mcp
- group: build
  title: ''
  type: Tools
  url: https://github.com/knocklabs/agent-toolkit
- group: build
  title: ''
  type: Tools
  url: https://github.com/knocklabs/telegraph
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/knocklabs/in-app-notifications-example-nextjs
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/knocklabs/slack-kit-example
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/knocklabs/ios-example-app
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/knocklabs/ai-agent-examples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/knocklabs/workflow-templates
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/knocklabs/notion-feed-example
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/knocklabs/marketplace-example
- group: build
  title: ''
  type: Plugins
  url: https://github.com/knocklabs/react-notification-feed
- group: design
  title: ''
  type: Webhooks
  url: https://docs.knock.app/developer-tools/outbound-webhooks/overview
- group: design
  title: ''
  type: Webhooks
  url: https://docs.knock.app/developer-tools/outbound-webhooks/event-types
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/knock-webhooks-asyncapi.yml
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
- group: design
  title: ''
  type: JSONLD
  url: json-ld/knock-app-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/knock-app-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/knock-app-rules.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knock.app/ai/mcp-server
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knock.app/ai/agent
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knock.app/ai/skills
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knock.app/ai/agent-function
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knock.app/developer-tools/service-tokens
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knock.app/concepts/environments
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knock.app/concepts/commits
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knock.app/template-editor/reference-liquid-helpers
- group: operate
  title: ''
  type: Forums
  url: https://knock.app/community
created: '2026-05-25'
description: Knock is notifications infrastructure as a service — a product and customer messaging platform you use to power transactional, lifecycle, broadcast, and in-product messaging across email, SMS, push, in-app, in-app guides, chat (Slack / Discord / Teams / WhatsApp), and outbound webhooks. Knock exposes two REST surfaces — a runtime API (api.knock.app) for triggering workflows and managing recipients/messages, and a Management API (control.knock.app) for resource CRUD — together with official SDKs in Node, Python, Ruby, Go, Elixir, Java, .NET, PHP and mobile (Swift, Kotlin, Flutter, React Native, Expo); a CLI; a remote MCP server; an agent toolkit for OpenAI / AI SDK / Langchain / Mastra; outbound webhooks; AI agent workflow steps; SlackKit and TeamsKit; and a git-style environment / branch / commit model for safe promotion of notification resources.
examples:
- key_count: 2
  name: Knock Create Schedule Example
  slug: knock-create-schedule-example
- key_count: 2
  name: Knock Identify User Example
  slug: knock-identify-user-example
- key_count: 2
  name: Knock Trigger Workflow Example
  slug: knock-trigger-workflow-example
features:
- Cross-channel notification workflows — email, SMS, push, in-app, in-app guides, chat (Slack/Discord/Teams/WhatsApp), and outbound webhooks from one trigger
- Workflow function steps — batch, delay, branch, experiment, throttle, fetch (HTTP), AI agent, trigger-workflow, update-user / update-tenant / update-object / update-data / update-audience
- Drag-and-drop workflow builder used collaboratively by engineering, product, and growth
- Broadcasts — one-time messages to audience-targeted groups from the Knock dashboard
- Guides — in-app lifecycle messaging using your own components and design system
- Recipients model — Users, non-user Objects, and Tenants with channel data and properties
- Preferences — per-channel, per-workflow, per-category preference sets enforced automatically on every run and broadcast
- Audiences — static and dynamic user segments that automatically drive lifecycle workflow triggers
- Schedules — one-off and recurring (timezone-aware) workflow firing
- Subscriptions — many-to-many fan-out from Objects to recipient lists
- Conditions — dynamic control flow on trigger data, recipient properties, and prior step status
- Templates — drag-and-drop editor + Liquid; partials, branding, translations (i18n), email layouts
- Real-time in-app feed API plus pre-built React, JavaScript, iOS, Android, Flutter, React Native, Expo, and Vue/Nuxt SDKs
- Outbound webhook events for full message lifecycle and environment change tracking
- Customer-facing webhook channel (let your customers configure their own webhook destinations)
- Idempotent requests via Idempotency-Key
- Cursor-based pagination
- Tiered per-endpoint rate limits (1, 5, 60, 200, 1000 req/sec) scoped per environment or per signed user
- Enhanced security mode with signed user tokens (JWT)
- Environments + Branches + Commits — git-style resource workflow with promotion across dev/staging/prod
- Knock CLI for local-first resource management against the Management API
- Knock MCP server (remote) at mcp.knock.app/mcp — OAuth 2.1 + PKCE; tool groups for resources, commits, debug, data, and docs
- Knock Agent Toolkit — AI SDK, OpenAI function-calling, Langchain, Mastra, and local MCP server bindings
- AI agent function step inside workflows for prompt-driven enrichment and personalization
- Knock skills — procedural knowledge packages for AI agents working with Knock
- SlackKit and TeamsKit — drop-in OAuth + channel-data UX for connecting customer Slack/Teams workspaces
- Data warehouse / Segment / Datadog observability streams
- Source events — trigger workflows from CDPs (Segment, Rudderstack) or reverse-ETL (Hightouch, Census)
- Multi-tenancy with per-tenant branding and locked preferences (Enterprise)
- SAML 2.0 SSO, SCIM directory sync, HIPAA / BAA on Enterprise
- Official SDKs in Node, Python, Ruby, Go, Elixir, Java, .NET, PHP, plus mobile (Swift, Kotlin, Flutter, React Native, Expo) and Management-API SDKs (Node, Python, Go)
finops:
- name: Knock Finops
  service_category: ''
  slug: knock-finops
graphqls:
- description: 'title: Knock GraphQL Schema'
  name: Knock GraphQL Schema
  slug: knock-app-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/knock-app.png
json_schemas:
- name: Knock Message
  property_count: 19
  slug: knock-message
- name: Knock Workflow Trigger Request
  property_count: 5
  slug: knock-workflow-trigger
jsonld:
- class_count: 0
  name: Knock App Context
  property_count: 11
  slug: knock-app-context
layout: provider
mcp_servers:
- description: ''
  name: knock-app-mcp.yml
  slug: knock-app-mcpyml
modified: '2026-06-20'
name: Knock
nav: Providers
network: true
overview: 'Knock publishes 35 APIs on the [APIs.io](https://apis.io/) network, including Outbound Webhooks, Accounts API, API keys API, and 32 more. Tagged areas include Notifications, Messaging, Infrastructure, Workflows, and Cross-Channel.


  The Knock catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Knock''s developer surface includes authentication, sandbox, CLI, developer portal, documentation, getting-started guide, signup flow, and 105 more developer resources.'
plans:
- name: Knock Plans Pricing
  plan_count: 3
  slug: knock-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Knock Rate Limits
  slug: knock-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Knock API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: knock-app-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Knock API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: knock-app-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Knock API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 3
  slug: knock-app-rules
score:
  band: exemplar
  composite: 71.5
  delta: -3.2
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 43.2
    contract_quality: 75.0
    developer_ergonomics: 85.7
    discoverability: 77.8
    governance: 43.2
    operational_transparency: 73.7
  previous_composite: 74.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 34
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 27.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/knock-app/refs/heads/main/screenshots/knock-app-2026-06-20T184113.png
security:
- kind: authentication
  name: Knock App Authentication
  slug: knock-app-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Knock App Domain Security
  slug: knock-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: knock-app
tags:
- Notifications
- Messaging
- Infrastructure
- Workflows
- Cross-Channel
- Email
- SMS
- Push
- In-App
- Chat
- Slack
- Webhooks
- MCP
- AI Agents
- Developer Platform
website: https://knock.app
---
