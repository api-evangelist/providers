---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.7
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 92
  human_in_the_loop: 92
  name: Novu Agentic Access
  operation_count: 135
  slug: novu-agentic-access
  summary_line: 135 operations · 92 acting · 92 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.novu.co
  baseurl_source: declared
  description: Client-side API and React Inbox component for rendering an embedded in-app notification center, marking notifications as read / archived / snoozed, and managing per-user notification preferences direc
  name: Novu Inbox / In-App API
  slug: inbox-api
- description: Code-first workflow framework that lets developers define notification workflows in TypeScript / JavaScript using `@novu/framework`, then sync them to Novu Cloud (or a self-hosted instance) via the `n
  name: Novu Framework (Code-First Workflows)
  slug: framework
- description: Official Model Context Protocol server exposing the Novu REST API surface as MCP tools so AI agents (Claude Desktop, Cursor, agent frameworks) can trigger workflows, manage subscribers, list workflows
  name: Novu MCP Server
  slug: mcp-server
- baseURL: https://api.novu.co
  baseurl_source: declared
  description: The Activity API from Novu — 1 operation(s) for activity.
  name: Novu Activity API
  phrasing_intents:
  - id: InboundWebhooksController_handleWebhook
    intent: Report delivery provider engagement events
    question: How do I send delivery and engagement events from my email or SMS provider back into Novu?
  phrasing_ops: 1
  slug: novu-activity-api
- baseURL: https://api.novu.co
  baseurl_source: declared
  description: The Channel Connections API from Novu — 2 operation(s) for channel connections.
  name: Novu Channel Connections API
  phrasing_intents:
  - id: ChannelConnectionsController_listChannelConnections
    intent: List channel connections
    question: Which chat workspace connections have been set up for my subscribers?
  - id: ChannelConnectionsController_createChannelConnection
    intent: Create a channel connection
    question: How do I connect a chat workspace to an integration with its auth credentials?
  - id: ChannelConnectionsController_getChannelConnectionByIdentifier
    intent: Get a channel connection
    question: How can I look up the details of one channel connection by its identifier?
  - id: ChannelConnectionsController_updateChannelConnection
    intent: Update a channel connection
    question: How do I refresh the auth credentials on an existing channel connection?
  - id: ChannelConnectionsController_deleteChannelConnection
    intent: Delete a channel connection
    question: How do I remove a chat workspace connection I no longer use?
  phrasing_ops: 5
  slug: novu-channel-connections-api
- baseURL: https://api.novu.co
  baseurl_source: declared
  description: The Channel Endpoints API from Novu — 2 operation(s) for channel endpoints.
  name: Novu Channel Endpoints API
  phrasing_intents:
  - id: ChannelEndpointsController_listChannelEndpoints
    intent: List channel endpoints
    question: Which chat endpoints are registered for a given subscriber?
  - id: ChannelEndpointsController_createChannelEndpoint
    intent: Create a channel endpoint
    question: How do I register a new channel endpoint for a resource?
  - id: ChannelEndpointsController_getChannelEndpoint
    intent: Get a channel endpoint
    question: How do I look up one channel endpoint by its identifier?
  - id: ChannelEndpointsController_updateChannelEndpoint
    intent: Update a channel endpoint
    question: How do I change where an existing channel endpoint delivers to?
  - id: ChannelEndpointsController_deleteChannelEndpoint
    intent: Delete a channel endpoint
    question: How do I remove a channel endpoint so no more messages go to it?
  phrasing_ops: 5
  slug: novu-channel-endpoints-api
- baseURL: https://api.novu.co
  baseurl_source: declared
  description: The Contexts API from Novu — 2 operation(s) for contexts.
  name: Novu Contexts API
  phrasing_intents:
  - id: ContextsController_createContext
    intent: Create a context
    question: How do I create a new context with a type, id and custom data?
  - id: ContextsController_listContexts
    intent: List contexts
    question: How do I see all the contexts defined in my Novu environment?
  - id: ContextsController_updateContext
    intent: Update a context's data
    question: How do I change the data on an existing context without recreating it?
  - id: ContextsController_getContext
    intent: Get a context
    question: How do I fetch a single context by its type and id?
  - id: ContextsController_deleteContext
    intent: Delete a context
    question: How do I remove a context I no longer need?
  phrasing_ops: 5
  slug: novu-contexts-api
- baseURL: https://api.novu.co
  baseurl_source: declared
  description: Used to manage your inbound email domains.
  name: Novu Domains API
  phrasing_intents:
  - id: DomainsController_listDomains
    intent: List inbound-email domains
    question: Which inbound email domains are registered in my current environment?
  - id: DomainsController_createDomain
    intent: Register an inbound-email domain
    question: How do I set up a new domain so it can receive inbound email?
  - id: DomainsController_getDomain
    intent: Get a domain's configuration and DNS records
    question: How can I see the configuration and required DNS records for one of my domains?
  - id: DomainsController_updateDomain
    intent: Update a domain's metadata
    question: How do I change the metadata attached to an inbound domain?
  - id: DomainsController_deleteDomain
    intent: Delete an inbound-email domain
    question: What happens to a domain's routes when I delete the domain?
  - id: DomainsController_verifyDomain
    intent: Verify a domain's MX records
    question: I've added the MX records; how do I get Novu to re-check and verify my domain?
  - id: DomainsController_diagnoseDomain
    intent: Diagnose inbound DNS problems
    question: Why isn't my domain receiving inbound email?
  - id: DomainsController_listDomainRoutes
    intent: List a domain's routes
    question: Which addresses on my domain have inbound routes set up?
  phrasing_ops: 15
  slug: novu-domains-api
- baseURL: https://api.novu.co
  baseurl_source: declared
  description: The Environment Variables API from Novu — 3 operation(s) for environment variables.
  name: Novu Environment Variables API
  phrasing_intents:
  - id: EnvironmentVariablesController_listEnvironmentVariables
    intent: List environment variables
    question: What environment variables are defined for my Novu organization?
  - id: EnvironmentVariablesController_createEnvironmentVariable
    intent: Create an environment variable
    question: How do I add a new variable like BASE_URL for my workflows to use?
  - id: EnvironmentVariablesController_getEnvironmentVariableUsage
    intent: See which workflows use a variable
    question: Which workflows reference a given environment variable in their steps?
  - id: EnvironmentVariablesController_getEnvironmentVariable
    intent: Get an environment variable
    question: How do I look up a single environment variable by its key?
  - id: EnvironmentVariablesController_updateEnvironmentVariable
    intent: Update an environment variable
    question: How do I change a variable's value for just one environment?
  - id: EnvironmentVariablesController_deleteEnvironmentVariable
    intent: Delete an environment variable
    question: How do I remove an environment variable I no longer need?
  phrasing_ops: 6
  slug: novu-environment-variables-api
- baseURL: https://api.novu.co
  baseurl_source: declared
  description: Environments allow you to manage different stages of your application development lifecycle. Each environment has its own set of API keys and configurations, enabling you to separate development, stag
  name: Novu Environments API
  phrasing_intents:
  - id: EnvironmentsControllerV1_createEnvironment
    intent: Create an environment
    question: How do I add a staging environment with its own API keys?
  - id: EnvironmentsControllerV1_listMyEnvironments
    intent: List environments
    question: What environments does my Novu organization have?
  - id: EnvironmentsControllerV1_updateMyEnvironment
    intent: Update an environment
    question: How do I rename an environment or change its color?
  - id: EnvironmentsControllerV1_deleteEnvironment
    intent: Delete an environment
    question: What gets removed when I delete an environment?
  - id: EnvironmentsController_getEnvironmentTags
    intent: List workflow tags in an environment
    question: Which tags are used across the workflows in an environment?
  - id: EnvironmentsController_publishEnvironment
    intent: Publish resources to another environment
    question: How do I promote my development workflows to production?
  - id: EnvironmentsController_diffEnvironment
    intent: Compare two environments
    question: What's different between my development and production workflows?
  phrasing_ops: 7
  slug: novu-environments-api
- baseURL: https://api.novu.co
  baseurl_source: declared
  description: Events represent a change in state of a subscriber. They are used to trigger workflows, and enable you to send notifications to subscribers based on their actions.
  name: Novu Events API
  phrasing_intents:
  - id: EventsController_trigger
    intent: Trigger a workflow to send notifications
    question: How do I send a notification to a subscriber with Novu?
  - id: EventsController_triggerBulk
    intent: Trigger many events in one request
    question: Can I trigger several different workflows in a single API call?
  - id: EventsController_broadcastEventToAll
    intent: Broadcast a notification to all subscribers
    question: How do I send an announcement to every subscriber at once?
  - id: EventsController_cancel
    intent: Cancel a triggered event
    question: How do I stop a pending digest or delayed notification from going out?
  phrasing_ops: 4
  slug: novu-events-api
- baseURL: https://api.novu.co
  baseurl_source: declared
  description: With the help of the Integration Store, you can easily integrate your favorite delivery provider. During the runtime of the API, the Integrations Store is responsible for storing the configurations of
  name: Novu Integrations API
  phrasing_intents:
  - id: IntegrationsController_listIntegrations
    intent: List all channel integrations
    question: Which delivery providers have I integrated with Novu, active or not?
  - id: IntegrationsController_createIntegration
    intent: Add a delivery provider integration
    question: How do I connect a new email or SMS provider to Novu?
  - id: IntegrationsController_getActiveIntegrations
    intent: List active integrations
    question: Which of my integrations are currently turned on?
  - id: IntegrationsController_updateIntegrationById
    intent: Update an integration
    question: How do I rotate the API key on an existing provider integration?
  - id: IntegrationsController_removeIntegration
    intent: Delete an integration
    question: How do I remove a provider integration permanently?
  - id: IntegrationsController_autoConfigureIntegration
    intent: Auto-configure inbound webhooks for an integration
    question: Can Novu set up the webhook signing keys and endpoints for a provider automatically?
  - id: IntegrationsController_setIntegrationAsPrimary
    intent: Make an integration the primary provider
    question: How do I choose which email provider is used by default in a workflow?
  - id: IntegrationsController_getChatOAuthUrl
    intent: Generate a chat OAuth URL (deprecated)
    question: What was the older, deprecated endpoint for generating a chat OAuth link?
  phrasing_ops: 10
  slug: novu-integrations-api
- baseURL: https://api.novu.co
  baseurl_source: declared
  description: Layouts are reusable wrappers for your email notifications.
  name: Novu Layouts API
  phrasing_intents:
  - id: LayoutsController_create
    intent: Create a layout
    question: How do I create a new shared layout for my emails?
  - id: LayoutsController_list
    intent: List email layouts
    question: What layouts do I have available for my email templates?
  - id: LayoutsController_update
    intent: Update a layout
    question: How do I rename a layout or change its content?
  - id: LayoutsController_get
    intent: Get a layout
    question: How do I fetch the details of one layout?
  - id: LayoutsController__delete
    intent: Delete a layout
    question: How do I remove a layout I no longer use?
  - id: LayoutsController_duplicate
    intent: Duplicate a layout
    question: How do I copy an existing layout as a starting point for a new one?
  - id: LayoutsController_generatePreview
    intent: Preview a layout
    question: How can I see what a layout will look like with sample data?
  - id: LayoutsController_getUsage
    intent: See which workflows use a layout
    question: Which workflows are using a particular layout?
  phrasing_ops: 8
  slug: novu-layouts-api
- baseURL: https://api.novu.co
  baseurl_source: declared
  description: A message in Novu represents a notification delivered to a recipient on a particular channel. Messages contain information about the request that triggered its delivery, a view of the data sent to the
  name: Novu Messages API
  phrasing_intents:
  - id: MessagesController_getMessages
    intent: List sent messages
    question: How do I see the messages Novu has sent in this environment?
  - id: MessagesController_deleteMessage
    intent: Delete a message
    question: How do I delete a single message by its id?
  - id: MessagesController_deleteMessagesByTransactionId
    intent: Delete all messages from a trigger
    question: How do I delete every message produced by one triggered event?
  phrasing_ops: 3
  slug: novu-messages-api
- baseURL: https://api.novu.co
  baseurl_source: declared
  description: The Notifications API from Novu — 2 operation(s) for notifications.
  name: Novu Notifications API
  phrasing_intents:
  - id: NotificationsController_listNotifications
    intent: List triggered notification events
    question: How do I see the activity feed of workflows that were triggered?
  - id: NotificationsController_getNotification
    intent: Get a triggered event's details
    question: How can I see the execution logs and status of one triggered event?
  phrasing_ops: 2
  slug: novu-notifications-api
- baseURL: https://api.novu.co
  baseurl_source: declared
  description: A subscriber in Novu represents someone who should receive a message. A subscriber's profile information contains important attributes about the subscriber that will be used in messages (name, email).
  name: Novu Subscribers API
  phrasing_intents:
  - id: SubscribersV1Controller_bulkCreateSubscribers
    intent: Create many subscribers at once
    question: How do I import a large batch of users as subscribers in one request?
  - id: SubscribersV1Controller_updateSubscriberChannel
    intent: Replace a subscriber's provider credentials
    question: How do I overwrite a subscriber's push device tokens with a fresh set?
  - id: SubscribersV1Controller_modifySubscriberChannel
    intent: Add to a subscriber's provider credentials
    question: Can I append a new FCM device token to a subscriber without dropping the old ones?
  - id: SubscribersV1Controller_deleteSubscriberCredentials
    intent: Remove a subscriber's provider credentials
    question: How do I delete the stored push or chat credentials for a subscriber?
  - id: SubscribersV1Controller_updateSubscriberOnlineFlag
    intent: Set a subscriber's online status
    question: Can I mark a subscriber as online or offline?
  - id: SubscribersV1Controller_getNotificationsFeed
    intent: Get a subscriber's inbox feed (v1)
    question: What does the older page-based inbox feed endpoint return for a subscriber?
  - id: SubscribersV1Controller_getUnseenCount
    intent: Count a subscriber's unseen notifications
    question: How many unseen inbox notifications does a subscriber have for the bell badge?
  - id: SubscribersV1Controller_markMessagesAs
    intent: Mark specific inbox messages (v1)
    question: With the older v1 endpoint, can I mark several message ids as seen, read, unseen or unread at once?
  phrasing_ops: 35
  slug: novu-subscribers-api
- baseURL: https://api.novu.co
  baseurl_source: declared
  description: Topics are a way to group subscribers together so that they can be notified of events at once. A topic is identified by a custom key. This can be helpful for things like sending out marketing emails o
  name: Novu Topics API
  phrasing_intents:
  - id: TopicsV1Controller_getTopicSubscriber
    intent: Check if a subscriber is in a topic
    question: Is a particular subscriber part of a given topic?
  - id: TopicsController_listTopics
    intent: List topics
    question: What topics have I set up for group notifications?
  - id: TopicsController_upsertTopic
    intent: Create or update a topic
    question: How do I create a topic to notify a group of subscribers together?
  - id: TopicsController_getTopic
    intent: Get a topic
    question: How do I look up a topic by its key?
  - id: TopicsController_updateTopic
    intent: Rename a topic
    question: How do I change the display name of an existing topic?
  - id: TopicsController_deleteTopic
    intent: Delete a topic
    question: What happens to a topic's subscriptions when I delete it?
  - id: TopicsController_listTopicSubscriptions
    intent: List a topic's subscribers
    question: Who is subscribed to a given topic?
  - id: TopicsController_createTopicSubscriptions
    intent: Subscribe subscribers to a topic
    question: How do I add several subscribers to a topic at once?
  phrasing_ops: 11
  slug: novu-topics-api
- baseURL: https://api.novu.co
  baseurl_source: declared
  description: Used to localize your notifications to different languages.
  name: Novu Translations API
  phrasing_intents:
  - id: TranslationController_uploadTranslationFiles
    intent: Upload locale files for a workflow
    question: How do I upload JSON translation files for one workflow?
  - id: TranslationController_createTranslationEndpoint
    intent: Create or update a translation
    question: How do I add a translation for one locale to a workflow?
  - id: TranslationController_getMasterJsonEndpoint
    intent: Export all translations as master JSON
    question: Can I export every workflow's translations for a locale in one JSON file?
  - id: TranslationController_importMasterJsonEndpoint
    intent: Import translations from master JSON
    question: How do I import translations for many workflows at once from a JSON body?
  - id: TranslationController_uploadMasterJsonEndpoint
    intent: Upload a master translations file
    question: Can I upload a master translations file and have the locale detected from its filename?
  - id: TranslationController_getTranslationGroupEndpoint
    intent: Get a translation group
    question: Which locales have translations for a specific workflow or layout?
  - id: TranslationController_getSingleTranslation
    intent: Get one locale's translation
    question: How do I read the French strings for a particular workflow?
  - id: TranslationController_deleteTranslationEndpoint
    intent: Delete one locale's translation
    question: How do I remove just one language from a workflow's translations?
  phrasing_ops: 9
  slug: novu-translations-api
- baseURL: https://api.novu.co
  baseurl_source: declared
  description: All notifications are sent via a workflow. Each workflow acts as a container for the logic and blueprint that are associated with a type of notification in your system.
  name: Novu Workflows API
  phrasing_intents:
  - id: WorkflowController_create
    intent: Create a workflow
    question: How do I create a new notification workflow with email and in-app steps?
  - id: WorkflowController_searchWorkflows
    intent: List workflows
    question: What notification workflows exist in my environment?
  - id: WorkflowController_sync
    intent: Sync a workflow to another environment
    question: Can I copy a single workflow to my production environment?
  - id: WorkflowController_update
    intent: Replace a workflow's definition
    question: How do I fully replace a workflow's steps and preferences?
  - id: WorkflowController_getWorkflow
    intent: Get a workflow
    question: How do I fetch the full definition of one workflow?
  - id: WorkflowController_removeWorkflow
    intent: Delete a workflow
    question: What's the way to delete a workflow I no longer need?
  - id: WorkflowController_patchWorkflow
    intent: Partially update a workflow
    question: How do I deactivate a workflow without resending its steps?
  - id: WorkflowController_generatePreview
    intent: Preview a workflow step
    question: How can I see what a workflow step's message will look like with test data?
  phrasing_ops: 9
  slug: novu-workflows-api
- baseURL: https://api.novu.co
  baseurl_source: declared
  description: The Webhooks API from Novu — 0 operation(s) for webhooks.
  name: Novu Webhooks API
  slug: novu-webhooks-api
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
artifact_total: 160
asyncapis:
- description: Real-time WebSocket interface used by the Novu Notification Center / Inbox (the `<Inbox />` React component, `@novu/react-native`, the headless `@novu/js` SDK, and any custom client). The transport is
  name: Novu Notification Center WebSocket API
  slug: novu-asyncapi
collections:
- collection_type: postman
  name: Novu API
  slug: postman-novu
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Novu Activity API
  slug: open-novu-activity-api
- collection_type: open
  name: Novu Activity Channel Connections API
  slug: open-novu-channel-connections-api
- collection_type: open
  name: Novu Activity Channel Endpoints API
  slug: open-novu-channel-endpoints-api
- collection_type: open
  name: Novu Activity Contexts API
  slug: open-novu-contexts-api
- collection_type: open
  name: Novu Activity Domains API
  slug: open-novu-domains-api
- collection_type: open
  name: Novu Activity Environment Variables API
  slug: open-novu-environment-variables-api
- collection_type: open
  name: Novu Activity Environments API
  slug: open-novu-environments-api
- collection_type: open
  name: Novu Activity Events API
  slug: open-novu-events-api
- collection_type: open
  name: Novu Activity Integrations API
  slug: open-novu-integrations-api
- collection_type: open
  name: Novu Activity Layouts API
  slug: open-novu-layouts-api
- collection_type: open
  name: Novu Activity Messages API
  slug: open-novu-messages-api
- collection_type: open
  name: Novu Activity Notifications API
  slug: open-novu-notifications-api
- collection_type: open
  name: Novu Activity Subscribers API
  slug: open-novu-subscribers-api
- collection_type: open
  name: Novu Activity Topics API
  slug: open-novu-topics-api
- collection_type: open
  name: Novu Activity Translations API
  slug: open-novu-translations-api
- collection_type: open
  name: Novu Activity Workflows API
  slug: open-novu-workflows-api
- collection_type: open
  name: Novu API
  slug: open-novu
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/novuhq/novu-mcp-server/issues
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/novu/refs/heads/main/agentic-access/novu-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/novu-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/novu/refs/heads/main/security/novu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/novu-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/novu/refs/heads/main/authentication/novu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/novu-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/novu/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/novu/refs/heads/main/arazzo/novu-bulk-onboard-and-broadcast-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/novu-bulk-onboard-and-broadcast-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/novu/refs/heads/main/arazzo/novu-create-workflow-and-trigger-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/novu-create-workflow-and-trigger-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/novu/refs/heads/main/arazzo/novu-offboard-subscriber-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/novu-offboard-subscriber-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/novu/refs/heads/main/arazzo/novu-onboard-subscriber-and-notify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/novu-onboard-subscriber-and-notify-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/novu/refs/heads/main/arazzo/novu-provision-integration-and-set-primary-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/novu-provision-integration-and-set-primary-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/novu/refs/heads/main/arazzo/novu-set-preferences-then-notify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/novu-set-preferences-then-notify-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/novu/refs/heads/main/arazzo/novu-subscribe-existing-to-topic-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/novu-subscribe-existing-to-topic-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/novu/refs/heads/main/arazzo/novu-subscriber-inbox-triage-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/novu-subscriber-inbox-triage-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/novu/refs/heads/main/arazzo/novu-topic-broadcast-campaign-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/novu-topic-broadcast-campaign-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/novu/refs/heads/main/arazzo/novu-trigger-and-verify-delivery-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/novu-trigger-and-verify-delivery-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/novu/refs/heads/main/arazzo/novu-trigger-then-cancel-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/novu-trigger-then-cancel-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/novu/refs/heads/main/arazzo/novu-unsubscribe-from-topic-workflow.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/novu/refs/heads/main/plans/novu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/novu-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/novu/refs/heads/main/finops/novu-finops.yml
  title: ''
  type: FinOps
  url: finops/novu-finops.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/novu/refs/heads/main/rate-limits/novu-rate-limits.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/novu/refs/heads/main/rules/novu-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/novu-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/novu/refs/heads/main/vocabulary/novu-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/novu-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/novu/refs/heads/main/json-ld/novu-context.jsonld
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
mcp_servers:
- description: Remote MCP server at mcp.novu.co over HTTP.
  name: Novu MCP Server
  slug: novu
modified: '2026-05-29'
name: Novu
nav: Providers
network: true
overview: 'Novu publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Inbox / In-App API, Activity API, Channel Connections API, and 17 more. Tagged areas include Notification, Messaging, In-App, Email, and SMS.


  The Novu catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Novu''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, engineering blog, GitHub presence, and 52 more developer resources.'
plans:
- name: Novu Plans Pricing
  plan_count: 4
  slug: novu-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Novu Rate Limits
  slug: novu-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Novu API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: novu-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Novu API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: novu-jsonschema-spectral-rules
- effective_rule_count: 89
  extends:
  - spectral:oas
  name: Novu API Rules
  rule_count: 48
  severity_counts:
    error: 9
    hint: 0
    info: 11
    warn: 28
  slug: novu-spectral-rules
score:
  band: exemplar
  composite: 71.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 90.6
    catalog_earned_first_party: 0.0
    catalog_gap: 24.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 74.5
    contract_governance: 27.3
    contract_quality: 77.6
    developer_ergonomics: 83.3
    discoverability: 75.0
    operational_transparency: 54.7
  previous_composite: 71.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 20.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 33.3
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
- Notification
- Messaging
- In-App
- Email
- SMS
- Push
- Chat
- Workflows
- Open Source
- Subscribers
- Topic
- Inbox
- Workflow Orchestration
- Multi-Channel
- Digest
- MCP
- Framework
- React
- Real-Time
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
