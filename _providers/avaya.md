---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.2
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 191
  human_in_the_loop: 8
  name: Avaya Agentic Access
  operation_count: 336
  slug: avaya-agentic-access
  summary_line: 336 operations · 191 acting · 8 human-in-the-loop
api_count: 80
apis:
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Includes token related operations.
  name: Avaya Access Token API
  slug: avaya-access-token-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: APIs to manage Accounts.
  name: Avaya Account API
  slug: avaya-account-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Agent location Routing APIs for System Administrator. It will enable agents connecting from different countries to be able to go through specific trunks or connection.
  name: Avaya Agent Location API
  slug: avaya-agent-location-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: The Agent Notes API from Avaya — 4 operation(s) for agent notes.
  name: Avaya Agent Notes API
  slug: avaya-agent-notes-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Monitor and manage agent status and activity
  name: Avaya Agents API
  slug: avaya-agents-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Messages related to non-session based communication with the contact center are considered to be asynchronous messages. Based on the information passed, the contact center will either model this again
  name: Avaya Asynchronous Messages API
  slug: avaya-asynchronous-messages-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Search or export audit records for auditable objects.
  name: Avaya Audit Records API
  slug: avaya-audit-records-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: The available phone numbers that can be added to the contact center.
  name: Avaya Available Phone Numbers API
  slug: avaya-available-phone-numbers-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Administration of Avaya Aura Device Service Elements. These API are expected to be called by an account administrator. AADS is the abbreviated form for Avaya Aura Device Service and is commonly used i
  name: Avaya Avaya Aura Device Services API
  slug: avaya-avaya-aura-device-services-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: APIs to manage Avaya Cloud Office element in voice service
  name: Avaya Avaya Cloud Office management API
  slug: avaya-avaya-cloud-office-management-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: APIs to manage Avaya Cloud Office SIP Trunk element in voice service
  name: Avaya Avaya Cloud Office SIP Trunks API
  slug: avaya-avaya-cloud-office-sip-trunks-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Bulk operations related to the Jobs responsible for creating users.
  name: Avaya Bulk Job API
  slug: avaya-bulk-job-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Bulk operations related to Users, Add, Update, Delete, Export.
  name: Avaya Bulk User API
  slug: avaya-bulk-user-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Trigger and complete calls
  name: Avaya Calls API
  slug: avaya-calls-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Manage outbound campaigns
  name: Avaya Campaigns API
  slug: avaya-campaigns-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Routing is implemented by matching the attributes specified on an engagement, either through customer choice or by business logic, against the attributes associated with the members of the pool of ava
  name: Avaya Category API
  slug: avaya-category-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: This API is used to get details of list of jobs or a single job for a specific Communication Manager. These API are expected to be called by an account administrator.
  name: Avaya Comm Manager Job Details API
  slug: avaya-comm-manager-job-details-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Administration of Communication Manager configuration. These API are expected to be called by an account administrator. CM is the abbreviated form for Communication Manager and is commonly used in the
  name: Avaya Communication Manager API
  slug: avaya-communication-manager-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: The countries in which available phone numbers are available.
  name: Avaya Country API
  slug: avaya-country-api
- baseURL: https://core.{customerId}.ec.avayacloud.com
  baseurl_source: declared
  description: The Dataset API from Avaya — 1 operation(s) for dataset.
  name: Avaya Dataset API
  slug: avaya-dataset-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Dictionaries contain translations for measures for a specific locale and measure producer.
  name: Avaya Dictionaries API
  slug: avaya-dictionaries-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: A Dimension is a collection of related contact center objects used to provide a view of measurement data.
  name: Avaya Dimensions API
  slug: avaya-dimensions-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Do Not Call list management
  name: Avaya DNC API
  slug: avaya-dnc-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Drafts prepared by an Agent at an early stage before it is in final form in response to Email or Messaging contact. At the moment, only one draft supported per engagement.
  name: Avaya Drafts API
  slug: avaya-drafts-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: An Element is a server instance which provides feature capability. Some examples of elements are Avaya Cloud Office, Chat Connector, Microsoft Teams and so on.
  name: Avaya Element Management API
  slug: avaya-element-management-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Represents a resource of the Contact Center being allocated. Engagements can be assigned to one or many Conversations, although this is not mandatory.
  name: Avaya Engagement API
  slug: avaya-engagement-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Inbound engagements can be created from the customer side which are then handled by contact center resources like agents, supervisors and bots. Session Id's can be passed on any explicit requests made
  name: Avaya Engagements API
  slug: avaya-engagements-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Management of non e164 Extension that are assigned to Account. These API are expected to be called by an account administrator.
  name: Avaya Extension API
  slug: avaya-extension-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Get Details of Gateway Connection Manager. These API are expected to be called by an account administrator.
  name: Avaya Gateway Connection Manager API
  slug: avaya-gateway-connection-manager-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: A Group is a logical collection of the resources like e.g. user. These groups can be assigned to a user to grant access to the resources present in the group.
  name: Avaya Group Management API
  slug: avaya-group-management-api
- baseURL: https://core.{customerId}.ec.avayacloud.com
  baseurl_source: declared
  description: Group membership operations
  name: Avaya Group Users API
  slug: avaya-group-users-api
- baseURL: https://core.{customerId}.ec.avayacloud.com
  baseurl_source: declared
  description: Group management operations
  name: Avaya Groups API
  slug: avaya-groups-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Holidays are non-working days where the contact center is not staffed by agents and therefore fall outside of the operating business hours.
  name: Avaya Holiday API
  slug: avaya-holiday-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: 'Administration of Avaya Hybrid Cloud Gateway. These API are expected to be called by an account administrator. HCG is the abbreviated form for Hybrid Cloud Gateway and is commonly used in the summary '
  name: Avaya Hybrid Cloud Gateway API
  slug: avaya-hybrid-cloud-gateway-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Administration of Hybrid Cloud Manager.This API is expected to be called by an account administrator.
  name: Avaya Hybrid Cloud Manager API
  slug: avaya-hybrid-cloud-manager-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Management of hybrid extensions assigned to users. These API are expected to be called by an account administrator.
  name: Avaya Hybrid Extension API
  slug: avaya-hybrid-extension-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Administration of Hybrid Skills. These APIs are expected to be called by an account administrator.
  name: Avaya Hybrid Skill API
  slug: avaya-hybrid-skill-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Represents the criteria with which a customer may be identified (Phone numbers, e-mail addresses, social media handles).
  name: Avaya Identifiers API
  slug: avaya-identifiers-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Indicators are used to indicate the status of the conversation or the activity. For example, when a customer is typing a message, the typing indicator is sent to the contact center.
  name: Avaya Indicators API
  slug: avaya-indicators-api
- baseURL: https://core.{customerId}.ec.avayacloud.com
  baseurl_source: declared
  description: The Interactions API from Avaya — 1 operation(s) for interactions.
  name: Avaya Interactions API
  slug: avaya-interactions-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Intervals are specific dates or working days of the week when the contact center is fully operational and staffed by agents and therefore fall with the operating business hours.
  name: Avaya Interval API
  slug: avaya-interval-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Represents the history of Conversations and Engagements that a Customer has had with the business.
  name: Avaya Journey API
  slug: avaya-journey-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: The API provides jwt token used by SDK
  name: Avaya JWT Token API
  slug: avaya-jwt-token-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: The Locales supported for a each measure producer.
  name: Avaya Locales API
  slug: avaya-locales-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: This API is for managing location profiles. These API are expected to be called by an account administrator.
  name: Avaya Location Profile API
  slug: avaya-location-profile-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Operations connected to measure producer management.
  name: Avaya Measure Producers API
  slug: avaya-measure-producers-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: This tag is used to upload or download media using signed URI.
  name: Avaya Media API
  slug: avaya-media-api
- baseURL: https://core.{customerId}.ec.avayacloud.com
  baseurl_source: declared
  description: Send end user messages to the contact center.
  name: Avaya Messaging API
  slug: avaya-messaging-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: APIs to manage Microsoft Teams element in voice service.
  name: Avaya Microsoft Teams management API
  slug: avaya-microsoft-teams-management-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: APIs to manage Microsoft Teams SIP Trunk element in voice service.
  name: Avaya Microsoft Teams SIP Trunks API
  slug: avaya-microsoft-teams-sip-trunks-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: APIs to manage a customer's organization structure
  name: Avaya Organization Structure API
  slug: avaya-organization-structure-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: APIs to manage Outbound Call Number Routing Rules in voice service by an account administrator.
  name: Avaya Outbound Number Routing Rules API
  slug: avaya-outbound-number-routing-rules-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: The Participant API from Avaya — 2 operation(s) for participant.
  name: Avaya Participant API
  slug: avaya-participant-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Management of phone numbers that are the entry point for contact center voice engagements. Phone number can be assigned and released.
  name: Avaya Phone Number API
  slug: avaya-phone-number-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: A Profile is a grouping of individual features which are provisioned with pre-defined values that can be applied to a User.
  name: Avaya Profile API
  slug: avaya-profile-api
- baseURL: https://core.{customerId}.ec.avayacloud.com
  baseurl_source: declared
  description: 'Operations related to profile management: Create, Get, Update, Delete, List profiles.'
  name: Avaya Profile Management API
  slug: avaya-profile-management-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: When a message for a conversation, represented by providerDialogId, is sent, a corresponding engagement and dialog is either created or existing engagement and dialog is utilized. The engagement and d
  name: Avaya Provider Dialogs API
  slug: avaya-provider-dialogs-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Queue's are used to identify a pool of contact center agents for which Customer engagements can be matched and routed.
  name: Avaya Queue API
  slug: avaya-queue-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Metrics associated with a routing queue.
  name: Avaya Queue Metrics API
  slug: avaya-queue-metrics-api
- baseURL: https://core.{customerId}.ec.avayacloud.com
  baseurl_source: declared
  description: Queue lifecycle management — create, retrieve, update, and delete queues.
  name: Avaya Queues API
  slug: avaya-queues-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Reason codes are a set of codes that agents can select from agent desktop clients to further describe their current activity or state. Reason Codes consist of a unique codeName, codeNumber and codeTyp
  name: Avaya Reason Codes API
  slug: avaya-reason-codes-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Manage outbound campaign records
  name: Avaya Records API
  slug: avaya-records-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: A Report is a collection of contact center measurements related to a particular dimension.
  name: Avaya Reports API
  slug: avaya-reports-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Resource Partitions are grouping of any resources like CLID which are used while making outgoing communication. These resource partitions ultimately assigned to the user. This will help to provide acc
  name: Avaya Resource Partition API
  slug: avaya-resource-partition-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Sessions are used to hold context information about the customer and the clients used by the customer. A customer can have multiple active sessions at the same time. Sessions can be passed on any expl
  name: Avaya Sessions API
  slug: avaya-sessions-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: This section is to used to generate signed uri for the respective request.
  name: Avaya Signed URI API
  slug: avaya-signed-uri-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: This API is used to get list of all SIP trunk elements and update caller id for an account administrator.
  name: Avaya SIP Trunks API
  slug: avaya-sip-trunks-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Manage skills and agent/campaigns assignments
  name: Avaya Skills API
  slug: avaya-skills-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Manage subscriptions for digital events.
  name: Avaya Subscriptions API
  slug: avaya-subscriptions-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Set of API to initiate synchronization of data from Aura to AXP admin. These API are expected to be called by an account administrator.
  name: Avaya Sync Aura Entities API
  slug: avaya-sync-aura-entities-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Administration of System Manager. These API are expected to be called by an account administrator.
  name: Avaya System Manager API
  slug: avaya-system-manager-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Timetables are a time zone specific schedule of holidays (non-working days) and intervals (working days).
  name: Avaya Timetable API
  slug: avaya-timetable-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Save transcript of a dialog that captures messages exchanged between different participants
  name: Avaya Transcript API
  slug: avaya-transcript-api
- baseURL: https://core.{customerId}.ec.avayacloud.com
  baseurl_source: declared
  description: The Transcription API from Avaya — 2 operation(s) for transcription.
  name: Avaya Transcription API
  slug: avaya-transcription-api
- baseURL: https://core.{customerId}.ec.avayacloud.com
  baseurl_source: declared
  description: Endpoints for creating and retrieving transcript messages
  name: Avaya Transcripts API
  slug: avaya-transcripts-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Represents a user in the system. A user can be an Agent, Supervisor or an Administrator.
  name: Avaya User API
  slug: avaya-user-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Represents the set of rules to be followed for the user passwords.
  name: Avaya User Password Policy API
  slug: avaya-user-password-policy-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Manage system users
  name: Avaya Users API
  slug: avaya-users-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: A UX Profile represents a layout that can be applied to a user when using Avaya Workspaces.
  name: Avaya UX Profile API
  slug: avaya-ux-profile-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: APIs to export the Voice Numbers and Agent Extensions and its associated fields in a CSV file for account administrator.
  name: Avaya Voice Numbers And Extensions API
  slug: avaya-voice-numbers-and-extensions-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Represents Voice Plan of configured Communication Managers for Account Administrator. These API are expected to be called by an account administrator.
  name: Avaya Voice Plan API
  slug: avaya-voice-plan-api
- baseURL: https://core.{customerId}.ec.avayacloud.com
  baseurl_source: declared
  description: The Workflow Sessions API from Avaya — 5 operation(s) for workflow sessions.
  name: Avaya Workflow Sessions API
  slug: avaya-workflow-sessions-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Workspaces is a web-based application that provides a unified agent desktop. This API return the URL details.
  name: Avaya Workspaces API
  slug: avaya-workspaces-api
- baseURL: https://{region}.api.avayacloud.com
  baseurl_source: declared
  description: Manage data sets within campaigns
  name: Avaya Datasets API
  slug: avaya-datasets-api
artifact_total: 93
asyncapis:
- description: ''
  name: Avaya Webhooks
  slug: avaya-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.avaya.com/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.avayacloud.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.avayacloud.com/avaya-infinity/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developers.avayacloud.com/avaya-infinity/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.avayacloud.com/avaya-infinity/docs/quick-start
- group: operate
  title: ''
  type: Support
  url: https://support.avaya.com/support/en/public
- group: company
  title: ''
  type: Blog
  url: https://www.avaya.com/en/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/avaya
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/avaya/
- group: start
  title: ''
  type: SignUp
  url: https://developers.avayacloud.com/avaya-infinity/docs/obtaining-a-client-id-and-secret-from-avaya
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avaya.com/en/privacy/commitment/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.avaya.com/en/legal/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/avaya-axp/avaya-experience-platform
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/plans/avaya-plans-pricing.yml
  title: ''
  type: Pricing
  url: plans/avaya-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/plans/avaya-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/avaya-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/rate-limits/avaya-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/avaya-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/packages/avaya-packages.yml
  title: ''
  type: Packages
  url: packages/avaya-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/packages/avaya-packages.yml
  title: ''
  type: SDKs
  url: packages/avaya-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/cli/avaya-cli.yml
  title: ''
  type: CLI
  url: cli/avaya-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/components/avaya-components.yml
  title: ''
  type: Components
  url: components/avaya-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/well-known/avaya-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avaya-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/well-known/avaya-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/avaya-api-catalog.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/llms/avaya-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avaya-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/asyncapi/avaya-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/avaya-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/conventions/avaya-conventions.yml
  title: ''
  type: Conventions
  url: conventions/avaya-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/errors/avaya-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/avaya-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/data-model/avaya-data-model.yml
  title: ''
  type: DataModel
  url: data-model/avaya-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/lifecycle/avaya-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/avaya-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.avayacloud.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.avayacloud.com/avaya-experience-platform/docs/api-deprecation-notices
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/changelog/avaya-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/avaya-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/conformance/avaya-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avaya-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.avaya.com/en/trust-center/compliance/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/security/avaya-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/avaya-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/security/avaya-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/avaya-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://support.avaya.com/css/public/documents/100045520
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/security/avaya-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avaya-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/authentication/avaya-authentication.yml
  title: ''
  type: Authentication
  url: authentication/avaya-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/scopes/avaya-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/avaya-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/agentic-access/avaya-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/avaya-agentic-access.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/mcp/avaya-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/avaya-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-admin-account-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-admin-account-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-admin-element-inventory-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-admin-element-inventory-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-admin-group-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-admin-group-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-admin-match-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-admin-match-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-admin-timetable-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-admin-timetable-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-admin-user-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-admin-user-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-admin-voice-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-admin-voice-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-analytics-historical-data-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-analytics-historical-data-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-analytics-historical-data-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-analytics-historical-data-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-analytics-producer-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-analytics-producer-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-auth-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-auth-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-customer-journey-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-customer-journey-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-digital-custom-chat-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-digital-custom-chat-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-digital-custom-messaging-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-digital-custom-messaging-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-digital-notification-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-digital-notification-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-digital-sdk-auth-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-digital-sdk-auth-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-digital-signed-media-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-digital-signed-media-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-digital-signed-media-uri-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-digital-signed-media-uri-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-draft-retrieval-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-draft-retrieval-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-draft-save-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-draft-save-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-notification-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-notification-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-routing-queue-metrics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-routing-queue-metrics-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-transcript-retrieval-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-transcript-retrieval-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-axp-transcript-save-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-axp-transcript-save-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-access-token-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-access-token-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-analytics-historical-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-analytics-historical-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-groups-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-groups-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-messaging-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-messaging-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-notification-service-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-notification-service-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-notifications-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-notifications-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-outbound-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-outbound-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-profile-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-profile-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-queue-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-queue-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-queue-metrics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-queue-metrics-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-transcription-interactions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-transcription-interactions-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-transcripts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-transcripts-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-user-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-user-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-workflow-execution-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-workflow-execution-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-workflow-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-workflow-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/overlays/avaya-infinity-workflow-sessions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/avaya-infinity-workflow-sessions-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-open-interfaces-sessionserviceinterface.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-open-interfaces-sessionserviceinterface.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-open-interfaces-contactserviceinterface.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-open-interfaces-contactserviceinterface.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-open-interfaces-addressserviceinterface.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-open-interfaces-addressserviceinterface.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-open-interfaces-terminalconnectionserviceinterface.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-open-interfaces-terminalconnectionserviceinterface.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-open-interfaces-agentserviceinterface.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-open-interfaces-agentserviceinterface.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-open-interfaces-terminalserviceinterface.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-open-interfaces-terminalserviceinterface.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-open-interfaces-agentterminalserviceinterface.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-open-interfaces-agentterminalserviceinterface.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-open-interfaces-connectionserviceinterface.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-open-interfaces-connectionserviceinterface.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-open-interfaces-contactmanagerserviceinterface.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-open-interfaces-contactmanagerserviceinterface.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-open-interfaces-openqinterface.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-open-interfaces-openqinterface.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-open-interfaces-dalcallbackserviceinterface.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-open-interfaces-dalcallbackserviceinterface.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-open-interfaces-agentterminalconnectionserviceinterface.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-open-interfaces-agentterminalconnectionserviceinterface.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-open-interfaces-userserviceinterface.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-open-interfaces-userserviceinterface.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-open-interfaces-routepointconnectionserviceinterface.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-open-interfaces-routepointconnectionserviceinterface.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-open-interfaces-metricsserviceinterface.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-open-interfaces-metricsserviceinterface.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-open-interfaces-routepointaddressserviceinterface.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-open-interfaces-routepointaddressserviceinterface.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-open-interfaces-notificationproducerinterface.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-open-interfaces-notificationproducerinterface.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-open-interfaces-opennetworkinginterface.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-open-interfaces-opennetworkinginterface.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-open-interfaces-statsnotificationproducerinterface.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-open-interfaces-statsnotificationproducerinterface.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-ccmm-agent-agentemailws.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-ccmm-agent-agentemailws.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-ccmm-agent-agentwebcommws.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-ccmm-agent-agentwebcommws.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-ccmm-agent-agentcontactws.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-ccmm-agent-agentcontactws.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-ccmm-agent-agentutilityws.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-ccmm-agent-agentutilityws.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-ccmm-outbound-outboundcontactws.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-ccmm-outbound-outboundcontactws.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-ccmm-outbound-outboundcampaignws.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-ccmm-outbound-outboundcampaignws.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-aacc-ccmm-outbound-outboundutilityws.wsdl
  title: ''
  type: WSDL
  url: wsdl/avaya-aacc-ccmm-outbound-outboundutilityws.wsdl
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/wsdl/avaya-wsdl.yml
  title: ''
  type: WSDL
  url: wsdl/avaya-wsdl.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/grpc/avaya-ip-office-mtcti3.proto
  title: ''
  type: Protobuf
  url: grpc/avaya-ip-office-mtcti3.proto
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/grpc/avaya-protobuf.yml
  title: ''
  type: Protobuf
  url: grpc/avaya-protobuf.yml
created: '2026-01-01'
description: 'Avaya is a global enterprise communications company whose developer surface spans two cloud platforms: Avaya Infinity, the cloud-native customer experience platform launched in 2025, and Avaya Experience Platform (AXP), the CCaaS generation that preceded it. Between them they publish 40 OpenAPI 3.0 documents and 367 operations across administration (users, groups, profiles, queues, timetables, extensions, Communication Manager and hybrid cloud gateways), customer journey and engagement history, digital chat and custom messaging, transcripts, historical and real-time analytics, workflow sessions, outbound campaigns, and a webhook/WebSocket event surface. Authentication is a bearer JWT issued by a per-tenant Keycloak realm, carried alongside a tenant appkey header; every path is rooted at an account id and the Infinity host itself is per-tenant. Avaya publishes an llms.txt, an RFC 9727 API catalog, a public Postman workspace and first-party JavaScript SDKs, but no MCP server,
  no idempotency mechanism and no public pricing.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/avaya.png
layout: provider
modified: '2026-09-17'
name: Avaya
nav: Providers
network: true
overview: 'Avaya publishes 84 APIs on the [APIs.io](https://apis.io/) network, including Access Token API, Account API, Agent Location API, and 81 more. Tagged areas include Communications, Contact Center, Collaboration, Artificial Intelligence, and UCaaS.


  The Avaya catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Avaya''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 104 more developer resources.'
plans:
- name: Avaya Plans Pricing
  plan_count: 0
  slug: avaya-plans-pricing
press:
- date: ''
  title: Avaya Chooses Gemini Enterprise and Google Workspace ...
  url: https://www.businesswire.com/news/home/20251230219645/en/Avaya-Chooses-Gemini-Enterprise-and-Google-Workspace-for-AI-Driven-Collaboration-and-Next-Gen-Workplace-Productivity
- date: ''
  title: 'Avaya news: Avaya Infinity to support secure AI interaction'
  url: https://www.convergedsystems.com/blog/avaya-news-july-2025-avaya-infinity-platform-to-add-ai-model-context-protocol-mcp/
- date: ''
  title: 'Avaya Infinity Platform: AI-Powered CCaaS & CX Solutions'
  url: https://www.avaya.com/en/products/infinity-platform/
- date: ''
  title: Avaya to support Model Context Protocol, collaborate with ...
  url: https://www.linkedin.com/posts/avaya_avaya-is-thrilled-to-share-that-the-avaya-activity-7353409534989635584-MN14
- date: ''
  title: Artificial Intelligence | Avaya Trust Center
  url: https://www.avaya.com/en/trust-center/artificial-intelligence/
random_paper: 2
rate_limits:
- limit_count: 0
  name: Avaya Rate Limits
  slug: avaya-rate-limits
scopes:
- name: Avaya Scopes
  scope_count: 1
  slug: avaya-scopes
  summary_line: 1 scope · clientCredentials/password
score:
  band: developing
  composite: 52.5
  coverage:
    artifact_dirs: 29
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.1
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 65.3
    developer_ergonomics: 37.5
    discoverability: 78.6
    operational_transparency: 36.8
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 84
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/avaya/refs/heads/main/screenshots/avaya-2026-06-20T172723.png
security:
- kind: authentication
  name: Avaya Authentication
  slug: avaya-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Avaya Domain Security
  slug: avaya-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Avaya Vulnerability Disclosure
  slug: avaya-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Avaya Trust Center
  slug: avaya-trust-center
  summary_line: FedRAMP
slug: avaya
tags:
- Communications
- Contact Center
- Collaboration
- Artificial Intelligence
- UCaaS
- CCaaS
- Customer Experience
- Telephony
- Webhook
- Enterprise Software
- Unified Communications
- Customer Service
website: https://www.avaya.com/en/
---
