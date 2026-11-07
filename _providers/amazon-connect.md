---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 21
  human_in_the_loop: 1
  name: Amazon Connect Agentic Access
  operation_count: 41
  slug: amazon-connect-agentic-access
  summary_line: 41 operations · 21 acting · 1 human-in-the-loop
api_count: 60
apis:
- description: Amazon Connect Streams is a browser-based integration API and JavaScript SDK that enables embedding and controlling the Amazon Connect Contact Control Panel (CCP) within your web application or CRM sy
  name: Amazon Connect Streams SDK
  slug: amazon-connect-streams-sdk
- description: The Amazon AppIntegrations service enables you to configure and reuse connections to external applications, powering third-party integrations in the Amazon Connect agent workspace.
  name: Amazon AppIntegrations API
  slug: amazon-appintegrations-api
- description: 'Amazon Connect Contact Lens enables you to analyze conversations between customers and agents using speech transcription, natural language processing, and intelligent search capabilities. It performs '
  name: Amazon Connect Contact Lens API
  slug: amazon-connect-contact-lens-api
- description: With the outbound campaigns feature of Amazon Connect, you can create high-volume outbound campaigns for appointment reminders, telemarketing, subscription renewals, or debt collection.
  name: Amazon Connect Outbound Campaigns API
  slug: amazon-connect-outbound-campaigns-api
- description: The outbound campaigns V2 API provides an updated interface for creating high-volume outbound campaigns including multi-channel support and availability in all Amazon Connect regions.
  name: Amazon Connect Outbound Campaigns V2 API
  slug: amazon-connect-outbound-campaigns-v2-api
- description: With Amazon Connect Cases, agents can track and manage customer issues that require multiple interactions, follow-up tasks, and teams in your contact center. A case represents a customer issue includi
  name: Amazon Connect Cases API
  slug: amazon-connect-cases-api
- description: The Amazon Connect Participant Service enables managing chat participants including agents, customers, and managers. Use it to send messages and events, manage connection state, share attachments, and
  name: Amazon Connect Participant Service API
  slug: amazon-connect-participant-service-api
- description: Amazon Connect Customer Profiles provides a unified customer profile for your contact center with pre-built connectors powered by AppFlow that make it easy to combine customer information from third-p
  name: Amazon Connect Customer Profiles API
  slug: amazon-connect-customer-profiles-api
- description: Amazon Q in Connect is a generative AI customer service assistant built on Amazon Bedrock. It provides real-time recommendations to help contact center agents resolve customer issues quickly and accur
  name: Amazon Q Connect API
  slug: amazon-q-connect-api
- description: Amazon Connect Voice ID provides real-time caller authentication and fraud risk detection to make voice interactions in contact centers more secure and efficient. Note - Voice ID end of support is sch
  name: Amazon Voice ID API
  slug: amazon-voice-id-api
- baseURL: https://connect.amazonaws.com
  baseurl_source: declared
  description: Operations for managing agent status configurations
  name: Amazon Connect Agent Statuses API
  slug: amazon-connect-agent-statuses-api
- baseURL: https://connect.amazonaws.com
  baseurl_source: declared
  description: Operations for authentication and federation
  name: Amazon Connect Authentication API
  slug: amazon-connect-authentication-api
- baseURL: https://connect.amazonaws.com
  baseurl_source: declared
  description: Operations for managing contact flows
  name: Amazon Connect Contact Flows API
  slug: amazon-connect-contact-flows-api
- baseURL: https://connect.amazonaws.com
  baseurl_source: declared
  description: Operations for managing contacts and contact interactions
  name: Amazon Connect Contacts API
  slug: amazon-connect-contacts-api
- baseURL: https://connect.amazonaws.com
  baseurl_source: declared
  description: Operations for managing hours of operation configurations
  name: Amazon Connect Hours of Operations API
  slug: amazon-connect-hours-of-operations-api
- baseURL: https://connect.amazonaws.com
  baseurl_source: declared
  description: Operations for managing Amazon Connect instances
  name: Amazon Connect Instances API
  slug: amazon-connect-instances-api
- baseURL: https://connect.amazonaws.com
  baseurl_source: declared
  description: Operations for retrieving real-time and historical metrics
  name: Amazon Connect Metrics API
  slug: amazon-connect-metrics-api
- baseURL: https://connect.amazonaws.com
  baseurl_source: declared
  description: Operations for managing queues
  name: Amazon Connect Queues API
  slug: amazon-connect-queues-api
- baseURL: https://connect.amazonaws.com
  baseurl_source: declared
  description: Operations for managing routing profiles
  name: Amazon Connect Routing Profiles API
  slug: amazon-connect-routing-profiles-api
- baseURL: https://connect.amazonaws.com
  baseurl_source: declared
  description: Operations for managing security profiles
  name: Amazon Connect Security Profiles API
  slug: amazon-connect-security-profiles-api
- baseURL: https://connect.amazonaws.com
  baseurl_source: declared
  description: Operations for tagging Amazon Connect resources
  name: Amazon Connect Tags API
  slug: amazon-connect-tags-api
- baseURL: https://connect.amazonaws.com
  baseurl_source: declared
  description: Operations for managing Amazon Connect users and agents
  name: Amazon Connect Users API
  slug: amazon-connect-users-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Agent Status API from Amazon Connect — 2 operation(s) for connect agent status.
  name: Amazon Connect Connect Agent Status API
  slug: amazon-connect-agent-status-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Alias API from Amazon Connect — 4 operation(s) for connect alias.
  name: Amazon Connect Connect Alias API
  slug: amazon-connect-alias-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Association API from Amazon Connect — 1 operation(s) for connect association.
  name: Amazon Connect Connect Association API
  slug: amazon-connect-association-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Attached Files API from Amazon Connect — 2 operation(s) for connect attached files.
  name: Amazon Connect Connect Attached Files API
  slug: amazon-connect-attached-files-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Attached Files Configurations API from Amazon Connect — 2 operation(s) for connect attached files configurations.
  name: Amazon Connect Connect Attached Files Configurations API
  slug: amazon-connect-attached-files-configurations-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Attributes API from Amazon Connect — 3 operation(s) for connect attributes.
  name: Amazon Connect Connect Attributes API
  slug: amazon-connect-attributes-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Contact Evaluations API from Amazon Connect — 2 operation(s) for connect contact evaluations.
  name: Amazon Connect Connect Contact Evaluations API
  slug: amazon-connect-contact-evaluations-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Contact Flow Modules API from Amazon Connect — 2 operation(s) for connect contact flow modules.
  name: Amazon Connect Connect Contact Flow Modules API
  slug: amazon-connect-contact-flow-modules-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Content API from Amazon Connect — 3 operation(s) for connect content.
  name: Amazon Connect Connect Content API
  slug: amazon-connect-content-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Data Tables API from Amazon Connect — 2 operation(s) for connect data tables.
  name: Amazon Connect Connect Data Tables API
  slug: amazon-connect-data-tables-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Email Addresses API from Amazon Connect — 3 operation(s) for connect email addresses.
  name: Amazon Connect Connect Email Addresses API
  slug: amazon-connect-email-addresses-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Evaluation Forms API from Amazon Connect — 2 operation(s) for connect evaluation forms.
  name: Amazon Connect Connect Evaluation Forms API
  slug: amazon-connect-evaluation-forms-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Extraction Definitions API from Amazon Connect — 2 operation(s) for connect extraction definitions.
  name: Amazon Connect Connect Extraction Definitions API
  slug: amazon-connect-extraction-definitions-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Flow Associations API from Amazon Connect — 2 operation(s) for connect flow associations.
  name: Amazon Connect Connect Flow Associations API
  slug: amazon-connect-flow-associations-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Integration Associations API from Amazon Connect — 2 operation(s) for connect integration associations.
  name: Amazon Connect Connect Integration Associations API
  slug: amazon-connect-integration-associations-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Media API from Amazon Connect — 1 operation(s) for connect media.
  name: Amazon Connect Connect Media API
  slug: amazon-connect-media-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Metadata API from Amazon Connect — 6 operation(s) for connect metadata.
  name: Amazon Connect Connect Metadata API
  slug: amazon-connect-metadata-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Name API from Amazon Connect — 5 operation(s) for connect name.
  name: Amazon Connect Connect Name API
  slug: amazon-connect-name-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Notifications API from Amazon Connect — 4 operation(s) for connect notifications.
  name: Amazon Connect Connect Notifications API
  slug: amazon-connect-notifications-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Operations API from Amazon Connect — 133 operation(s) for connect operations.
  name: Amazon Connect Connect Operations API
  slug: amazon-connect-operations-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Overrides API from Amazon Connect — 2 operation(s) for connect overrides.
  name: Amazon Connect Connect Overrides API
  slug: amazon-connect-overrides-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Pages API from Amazon Connect — 2 operation(s) for connect pages.
  name: Amazon Connect Connect Pages API
  slug: amazon-connect-pages-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Phone Number API from Amazon Connect — 5 operation(s) for connect phone number.
  name: Amazon Connect Connect Phone Number API
  slug: amazon-connect-phone-number-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Predefined Attributes API from Amazon Connect — 2 operation(s) for connect predefined attributes.
  name: Amazon Connect Connect Predefined Attributes API
  slug: amazon-connect-predefined-attributes-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Prompts API from Amazon Connect — 2 operation(s) for connect prompts.
  name: Amazon Connect Connect Prompts API
  slug: amazon-connect-prompts-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Quick Connects API from Amazon Connect — 3 operation(s) for connect quick connects.
  name: Amazon Connect Connect Quick Connects API
  slug: amazon-connect-quick-connects-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Rules API from Amazon Connect — 2 operation(s) for connect rules.
  name: Amazon Connect Connect Rules API
  slug: amazon-connect-rules-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Storage Config API from Amazon Connect — 2 operation(s) for connect storage config.
  name: Amazon Connect Connect Storage Config API
  slug: amazon-connect-storage-config-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Task API from Amazon Connect — 2 operation(s) for connect task.
  name: Amazon Connect Connect Task API
  slug: amazon-connect-task-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Test Cases API from Amazon Connect — 2 operation(s) for connect test cases.
  name: Amazon Connect Connect Test Cases API
  slug: amazon-connect-test-cases-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Traffic Distribution Group API from Amazon Connect — 2 operation(s) for connect traffic distribution group.
  name: Amazon Connect Connect Traffic Distribution Group API
  slug: amazon-connect-traffic-distribution-group-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Use Cases API from Amazon Connect — 2 operation(s) for connect use cases.
  name: Amazon Connect Connect Use Cases API
  slug: amazon-connect-use-cases-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect User Hierarchy Groups API from Amazon Connect — 2 operation(s) for connect user hierarchy groups.
  name: Amazon Connect Connect User Hierarchy Groups API
  slug: amazon-connect-user-hierarchy-groups-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Values API from Amazon Connect — 8 operation(s) for connect values.
  name: Amazon Connect Connect Values API
  slug: amazon-connect-values-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Version API from Amazon Connect — 4 operation(s) for connect version.
  name: Amazon Connect Connect Version API
  slug: amazon-connect-version-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Versions API from Amazon Connect — 5 operation(s) for connect versions.
  name: Amazon Connect Connect Versions API
  slug: amazon-connect-versions-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Views API from Amazon Connect — 2 operation(s) for connect views.
  name: Amazon Connect Connect Views API
  slug: amazon-connect-views-api
- baseURL: https://github.com/amazon-connect/amazon-connect-streams
  baseurl_source: declared
  description: The Connect Workspaces API from Amazon Connect — 2 operation(s) for connect workspaces.
  name: Amazon Connect Connect Workspaces API
  slug: amazon-connect-workspaces-api
arazzos:
- description: Create a queue against an hours schedule, confirm it, and place an outbound call into it.
  name: Amazon Connect Create Queue and Place Outbound Call
  slug: amazon-connect-create-queue-and-place-call-workflow
- description: Create a routing profile with media concurrencies and assign it to an existing agent.
  name: Amazon Connect Create Routing Profile and Assign to User
  slug: amazon-connect-create-routing-profile-and-assign-workflow
- description: Describe an instance, then inventory its contact flows and queues once it is active.
  name: Amazon Connect Instance Configuration Overview
  slug: amazon-connect-instance-overview-workflow
- description: Create an hours-of-operation schedule, build a queue that uses it, and verify the queue.
  name: Amazon Connect Provision Queue with Hours of Operation
  slug: amazon-connect-provision-queue-with-hours-workflow
- description: Create an agent user, assign a routing profile, and confirm the final account state.
  name: Amazon Connect Provision Agent User
  slug: amazon-connect-provision-user-workflow
- description: Create a contact flow from flow-language content and read it back to verify it published.
  name: Amazon Connect Publish and Verify Contact Flow
  slug: amazon-connect-publish-contact-flow-workflow
- description: Confirm a queue is enabled, then pull live agent and in-queue metrics for it.
  name: Amazon Connect Queue Real-Time Health
  slug: amazon-connect-queue-realtime-health-workflow
- description: Search contacts in a time range, then describe and read the attributes of the first match.
  name: Amazon Connect Search and Inspect Contact
  slug: amazon-connect-search-and-inspect-contact-workflow
- description: Start a customer chat, confirm the contact, and attach routing attributes.
  name: Amazon Connect Start Chat Contact and Set Attributes
  slug: amazon-connect-start-chat-and-set-attributes-workflow
- description: Place an outbound voice call, then describe the contact and tag it with attributes.
  name: Amazon Connect Start Outbound Voice Contact and Track
  slug: amazon-connect-start-outbound-contact-and-track-workflow
- description: Create a task contact, confirm it through describe, then end the contact.
  name: Amazon Connect Start Task Contact and Stop It
  slug: amazon-connect-start-task-and-stop-workflow
- description: Read a user, update their identity information, then re-read to confirm the change.
  name: Amazon Connect Update User Identity Info
  slug: amazon-connect-update-user-identity-workflow
artifact_total: 378
collections:
- collection_type: postman
  name: Amazon Connect Service API
  slug: postman-amazon-connect
- collection_type: open
  name: Amazon Connect Service Agent Statuses API
  slug: open-amazon-connect-agent-statuses-api
- collection_type: open
  name: Amazon Connect Service Agent Statuses Authentication API
  slug: open-amazon-connect-authentication-api
- collection_type: open
  name: Amazon Connect Service Agent Statuses Contact Flows API
  slug: open-amazon-connect-contact-flows-api
- collection_type: open
  name: Amazon Connect Service Agent Statuses Contacts API
  slug: open-amazon-connect-contacts-api
- collection_type: open
  name: Amazon Connect Service Agent Statuses Hours of Operations API
  slug: open-amazon-connect-hours-of-operations-api
- collection_type: open
  name: Amazon Connect Service Agent Statuses Instances API
  slug: open-amazon-connect-instances-api
- collection_type: open
  name: Amazon Connect Service Agent Statuses Metrics API
  slug: open-amazon-connect-metrics-api
- collection_type: open
  name: Amazon Connect Service Agent Statuses Queues API
  slug: open-amazon-connect-queues-api
- collection_type: open
  name: Amazon Connect Service Agent Statuses Routing Profiles API
  slug: open-amazon-connect-routing-profiles-api
- collection_type: open
  name: Amazon Connect Service Agent Statuses Security Profiles API
  slug: open-amazon-connect-security-profiles-api
- collection_type: open
  name: Amazon Connect Service Agent Statuses Tags API
  slug: open-amazon-connect-tags-api
- collection_type: open
  name: Amazon Connect Service Agent Statuses Users API
  slug: open-amazon-connect-users-api
- collection_type: open
  name: Amazon Connect Service API
  slug: open-amazon-connect
common:
- group: operate
  href: https://artifacts.apis.io/amazon-connect/rate-limits/amazon-connect-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amazon-connect-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-connect/finops/amazon-connect-finops.yml
  title: ''
  type: FinOps
  url: finops/amazon-connect-finops.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-connect/plans/amazon-connect-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-connect-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/connect/
- group: agent
  href: https://artifacts.apis.io/amazon-connect/agentic-access/amazon-connect-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-connect-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/amazon-connect/security/amazon-connect-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-connect-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amazon-connect/security/amazon-connect-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-connect-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-connect/security/amazon-connect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-connect-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/amazon-connect/authentication/amazon-connect-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amazon-connect-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-connect/overview
- group: design
  href: https://artifacts.apis.io/amazon-connect/arazzo/amazon-connect-create-queue-and-place-call-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-connect-create-queue-and-place-call-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-connect/arazzo/amazon-connect-create-routing-profile-and-assign-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-connect-create-routing-profile-and-assign-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-connect/arazzo/amazon-connect-instance-overview-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-connect-instance-overview-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-connect/arazzo/amazon-connect-provision-queue-with-hours-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-connect-provision-queue-with-hours-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-connect/arazzo/amazon-connect-provision-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-connect-provision-user-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-connect/arazzo/amazon-connect-publish-contact-flow-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-connect-publish-contact-flow-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-connect/arazzo/amazon-connect-queue-realtime-health-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-connect-queue-realtime-health-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-connect/arazzo/amazon-connect-search-and-inspect-contact-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-connect-search-and-inspect-contact-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-connect/arazzo/amazon-connect-start-chat-and-set-attributes-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-connect-start-chat-and-set-attributes-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-connect/arazzo/amazon-connect-start-outbound-contact-and-track-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-connect-start-outbound-contact-and-track-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-connect/arazzo/amazon-connect-start-task-and-stop-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-connect-start-task-and-stop-workflow.yml
- group: design
  href: https://artifacts.apis.io/amazon-connect/arazzo/amazon-connect-update-user-identity-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-connect-update-user-identity-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/connect/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/connect/latest/adminguide/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/support/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/contact-center/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amazon-connect
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/connect/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-connect
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Security
  url: https://aws.amazon.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/connect/pricing/
- group: design
  href: https://artifacts.apis.io/amazon-connect/rules/amazon-connect-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/amazon-connect-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/amazon-connect/vocabulary/amazon-connect-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-connect-vocabulary.yaml
created: '2024-01-15'
description: Amazon Connect is a cloud-based contact center service that makes it easy to set up and manage a customer contact center and provide reliable customer engagement at any scale, with omnichannel support for voice, chat, email, and task management. It includes AI-powered features for agent assistance, customer profiles, conversation analytics, and outbound campaign management.
examples:
- key_count: 4
  name: Agent Status Summary Example
  slug: agent-status-summary-example
- key_count: 6
  name: Amazon Connect Createcontactflow Example
  slug: amazon-connect-createcontactflow-example
- key_count: 6
  name: Amazon Connect Createhoursofoperation Example
  slug: amazon-connect-createhoursofoperation-example
- key_count: 6
  name: Amazon Connect Createinstance Example
  slug: amazon-connect-createinstance-example
- key_count: 6
  name: Amazon Connect Createqueue Example
  slug: amazon-connect-createqueue-example
- key_count: 6
  name: Amazon Connect Createroutingprofile Example
  slug: amazon-connect-createroutingprofile-example
- key_count: 6
  name: Amazon Connect Createuser Example
  slug: amazon-connect-createuser-example
- key_count: 6
  name: Amazon Connect Describecontact Example
  slug: amazon-connect-describecontact-example
- key_count: 6
  name: Amazon Connect Describecontactflow Example
  slug: amazon-connect-describecontactflow-example
- key_count: 6
  name: Amazon Connect Describeinstance Example
  slug: amazon-connect-describeinstance-example
- key_count: 6
  name: Amazon Connect Describequeue Example
  slug: amazon-connect-describequeue-example
- key_count: 6
  name: Amazon Connect Describeroutingprofile Example
  slug: amazon-connect-describeroutingprofile-example
- key_count: 6
  name: Amazon Connect Describeuser Example
  slug: amazon-connect-describeuser-example
- key_count: 6
  name: Amazon Connect Getcontactattributes Example
  slug: amazon-connect-getcontactattributes-example
- key_count: 6
  name: Amazon Connect Getcurrentmetricdata Example
  slug: amazon-connect-getcurrentmetricdata-example
- key_count: 6
  name: Amazon Connect Getmetricdata Example
  slug: amazon-connect-getmetricdata-example
- key_count: 11
  name: Amazon Connect Instance Example
  slug: amazon-connect-instance-example
- key_count: 6
  name: Amazon Connect Listagentstatuses Example
  slug: amazon-connect-listagentstatuses-example
- key_count: 6
  name: Amazon Connect Listcontactflows Example
  slug: amazon-connect-listcontactflows-example
- key_count: 6
  name: Amazon Connect Listhoursofoperations Example
  slug: amazon-connect-listhoursofoperations-example
- key_count: 6
  name: Amazon Connect Listinstances Example
  slug: amazon-connect-listinstances-example
- key_count: 6
  name: Amazon Connect Listqueues Example
  slug: amazon-connect-listqueues-example
- key_count: 6
  name: Amazon Connect Listroutingprofiles Example
  slug: amazon-connect-listroutingprofiles-example
- key_count: 6
  name: Amazon Connect Listsecurityprofiles Example
  slug: amazon-connect-listsecurityprofiles-example
- key_count: 6
  name: Amazon Connect Listtagsforresource Example
  slug: amazon-connect-listtagsforresource-example
- key_count: 6
  name: Amazon Connect Listusers Example
  slug: amazon-connect-listusers-example
- key_count: 6
  name: Amazon Connect Searchcontacts Example
  slug: amazon-connect-searchcontacts-example
- key_count: 6
  name: Amazon Connect Startchatcontact Example
  slug: amazon-connect-startchatcontact-example
- key_count: 6
  name: Amazon Connect Startoutboundvoicecontact Example
  slug: amazon-connect-startoutboundvoicecontact-example
- key_count: 6
  name: Amazon Connect Starttaskcontact Example
  slug: amazon-connect-starttaskcontact-example
- key_count: 6
  name: Amazon Connect Stopcontact Example
  slug: amazon-connect-stopcontact-example
- key_count: 6
  name: Amazon Connect Tagresource Example
  slug: amazon-connect-tagresource-example
- key_count: 6
  name: Amazon Connect Updatecontactattributes Example
  slug: amazon-connect-updatecontactattributes-example
- key_count: 6
  name: Amazon Connect Updateuseridentityinfo Example
  slug: amazon-connect-updateuseridentityinfo-example
- key_count: 11
  name: Contact Example
  slug: contact-example
- key_count: 8
  name: Contact Flow Example
  slug: contact-flow-example
- key_count: 5
  name: Contact Flow Summary Example
  slug: contact-flow-summary-example
- key_count: 6
  name: Contact Summary Example
  slug: contact-summary-example
- key_count: 5
  name: Create Contact Flow Request Example
  slug: create-contact-flow-request-example
- key_count: 2
  name: Create Contact Flow Response Example
  slug: create-contact-flow-response-example
- key_count: 5
  name: Create Hours Of Operation Request Example
  slug: create-hours-of-operation-request-example
- key_count: 2
  name: Create Hours Of Operation Response Example
  slug: create-hours-of-operation-response-example
- key_count: 7
  name: Create Instance Request Example
  slug: create-instance-request-example
- key_count: 2
  name: Create Instance Response Example
  slug: create-instance-response-example
- key_count: 6
  name: Create Queue Request Example
  slug: create-queue-request-example
- key_count: 2
  name: Create Queue Response Example
  slug: create-queue-response-example
- key_count: 6
  name: Create Routing Profile Request Example
  slug: create-routing-profile-request-example
- key_count: 2
  name: Create Routing Profile Response Example
  slug: create-routing-profile-response-example
- key_count: 9
  name: Create User Request Example
  slug: create-user-request-example
- key_count: 2
  name: Create User Response Example
  slug: create-user-response-example
- key_count: 1
  name: Describe Contact Flow Response Example
  slug: describe-contact-flow-response-example
- key_count: 1
  name: Describe Contact Response Example
  slug: describe-contact-response-example
- key_count: 1
  name: Describe Instance Response Example
  slug: describe-instance-response-example
- key_count: 1
  name: Describe Queue Response Example
  slug: describe-queue-response-example
- key_count: 1
  name: Describe Routing Profile Response Example
  slug: describe-routing-profile-response-example
- key_count: 1
  name: Describe User Response Example
  slug: describe-user-response-example
- key_count: 5
  name: Get Current Metric Data Request Example
  slug: get-current-metric-data-request-example
- key_count: 3
  name: Get Current Metric Data Response Example
  slug: get-current-metric-data-response-example
- key_count: 7
  name: Get Metric Data Request Example
  slug: get-metric-data-request-example
- key_count: 2
  name: Get Metric Data Response Example
  slug: get-metric-data-response-example
- key_count: 3
  name: Hours Of Operation Config Example
  slug: hours-of-operation-config-example
- key_count: 3
  name: Hours Of Operation Summary Example
  slug: hours-of-operation-summary-example
- key_count: 2
  name: Hours Of Operation Time Slice Example
  slug: hours-of-operation-time-slice-example
- key_count: 9
  name: Instance Example
  slug: instance-example
- key_count: 7
  name: Instance Summary Example
  slug: instance-summary-example
- key_count: 2
  name: List Agent Statuses Response Example
  slug: list-agent-statuses-response-example
- key_count: 2
  name: List Contact Flows Response Example
  slug: list-contact-flows-response-example
- key_count: 2
  name: List Hours Of Operations Response Example
  slug: list-hours-of-operations-response-example
- key_count: 2
  name: List Instances Response Example
  slug: list-instances-response-example
- key_count: 2
  name: List Queues Response Example
  slug: list-queues-response-example
- key_count: 2
  name: List Routing Profiles Response Example
  slug: list-routing-profiles-response-example
- key_count: 2
  name: List Security Profiles Response Example
  slug: list-security-profiles-response-example
- key_count: 2
  name: List Users Response Example
  slug: list-users-response-example
- key_count: 2
  name: Media Concurrency Example
  slug: media-concurrency-example
- key_count: 9
  name: Queue Example
  slug: queue-example
- key_count: 4
  name: Queue Summary Example
  slug: queue-summary-example
- key_count: 10
  name: Routing Profile Example
  slug: routing-profile-example
- key_count: 3
  name: Routing Profile Summary Example
  slug: routing-profile-summary-example
- key_count: 6
  name: Search Contacts Request Example
  slug: search-contacts-request-example
- key_count: 3
  name: Search Contacts Response Example
  slug: search-contacts-response-example
- key_count: 3
  name: Security Profile Summary Example
  slug: security-profile-summary-example
- key_count: 7
  name: Start Chat Contact Request Example
  slug: start-chat-contact-request-example
- key_count: 3
  name: Start Chat Contact Response Example
  slug: start-chat-contact-response-example
- key_count: 7
  name: Start Outbound Voice Contact Request Example
  slug: start-outbound-voice-contact-request-example
- key_count: 12
  name: Start Task Contact Request Example
  slug: start-task-contact-request-example
- key_count: 1
  name: Update User Identity Info Request Example
  slug: update-user-identity-info-request-example
- key_count: 10
  name: User Example
  slug: user-example
- key_count: 5
  name: User Identity Info Example
  slug: user-identity-info-example
- key_count: 4
  name: User Phone Config Example
  slug: user-phone-config-example
- key_count: 3
  name: User Summary Example
  slug: user-summary-example
features:
- description: Unified routing across voice, chat, email, and tasks through a single platform with skills-based routing and priority queuing.
  name: Omnichannel Routing
- description: Amazon Q in Connect provides real-time AI-generated recommendations and answers to help agents resolve customer issues faster.
  name: AI-Powered Agent Assist
- description: Drag-and-drop contact flow designer for building IVR, chatbot, and agent guidance workflows without extensive coding.
  name: Contact Flows
- description: Contact Lens provides speech transcription, sentiment analysis, and NLP-powered insights across all customer interactions.
  name: Conversational Analytics
- description: Unified customer profile combining CRM, ITSM, ERP, and contact history data for context-aware agent interactions.
  name: Customer Profiles
- description: High-volume multi-channel outbound campaigns with predictive dialer, answering machine detection, and multiple dialing modes.
  name: Outbound Campaigns
- description: Structured case tracking for customer issues requiring multiple interactions, follow-up tasks, and cross-team coordination.
  name: Cases Management
- description: In-app, web, and video calling with screen share capabilities using 16kHz high-quality audio with packet loss resistance.
  name: Voice and Video Calling
- description: Real-time and asynchronous messaging including SMS, WhatsApp Business, and Apple Messages for Business integration.
  name: Chat and Messaging
- description: Comprehensive dashboards and reporting for contact center performance optimization and workforce planning.
  name: Real-Time and Historical Metrics
finops:
- has_sources: true
  method: derived
  name: Amazon Connect Finops
  primary_unit: message sent or received
  service_category: ''
  slug: amazon-connect-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-connect.png
json_schemas:
- name: AgentStatusSummary
  property_count: 4
  slug: agent-status-summary
- name: AgentStatusSummary
  property_count: 4
  slug: amazon-connect-agentstatussummary
- name: Contact
  property_count: 11
  slug: amazon-connect-contact
- name: ContactFlow
  property_count: 8
  slug: amazon-connect-contactflow
- name: ContactFlowSummary
  property_count: 5
  slug: amazon-connect-contactflowsummary
- name: ContactSummary
  property_count: 6
  slug: amazon-connect-contactsummary
- name: CreateContactFlowRequest
  property_count: 5
  slug: amazon-connect-createcontactflowrequest
- name: CreateContactFlowResponse
  property_count: 2
  slug: amazon-connect-createcontactflowresponse
- name: CreateHoursOfOperationRequest
  property_count: 5
  slug: amazon-connect-createhoursofoperationrequest
- name: CreateHoursOfOperationResponse
  property_count: 2
  slug: amazon-connect-createhoursofoperationresponse
- name: CreateInstanceRequest
  property_count: 7
  slug: amazon-connect-createinstancerequest
- name: CreateInstanceResponse
  property_count: 2
  slug: amazon-connect-createinstanceresponse
- name: CreateQueueRequest
  property_count: 6
  slug: amazon-connect-createqueuerequest
- name: CreateQueueResponse
  property_count: 2
  slug: amazon-connect-createqueueresponse
- name: CreateRoutingProfileRequest
  property_count: 6
  slug: amazon-connect-createroutingprofilerequest
- name: CreateRoutingProfileResponse
  property_count: 2
  slug: amazon-connect-createroutingprofileresponse
- name: CreateUserRequest
  property_count: 9
  slug: amazon-connect-createuserrequest
- name: CreateUserResponse
  property_count: 2
  slug: amazon-connect-createuserresponse
- name: DescribeContactFlowResponse
  property_count: 1
  slug: amazon-connect-describecontactflowresponse
- name: DescribeContactResponse
  property_count: 1
  slug: amazon-connect-describecontactresponse
- name: DescribeInstanceResponse
  property_count: 1
  slug: amazon-connect-describeinstanceresponse
- name: DescribeQueueResponse
  property_count: 1
  slug: amazon-connect-describequeueresponse
- name: DescribeRoutingProfileResponse
  property_count: 1
  slug: amazon-connect-describeroutingprofileresponse
- name: DescribeUserResponse
  property_count: 1
  slug: amazon-connect-describeuserresponse
- name: Error
  property_count: 2
  slug: amazon-connect-error
- name: GetCurrentMetricDataRequest
  property_count: 5
  slug: amazon-connect-getcurrentmetricdatarequest
- name: GetCurrentMetricDataResponse
  property_count: 3
  slug: amazon-connect-getcurrentmetricdataresponse
- name: GetMetricDataRequest
  property_count: 7
  slug: amazon-connect-getmetricdatarequest
- name: GetMetricDataResponse
  property_count: 2
  slug: amazon-connect-getmetricdataresponse
- name: HoursOfOperationConfig
  property_count: 3
  slug: amazon-connect-hoursofoperationconfig
- name: HoursOfOperationSummary
  property_count: 3
  slug: amazon-connect-hoursofoperationsummary
- name: HoursOfOperationTimeSlice
  property_count: 2
  slug: amazon-connect-hoursofoperationtimeslice
- name: Amazon Connect Instance
  property_count: 11
  slug: amazon-connect-instance
- name: InstanceSummary
  property_count: 7
  slug: amazon-connect-instancesummary
- name: ListAgentStatusesResponse
  property_count: 2
  slug: amazon-connect-listagentstatusesresponse
- name: ListContactFlowsResponse
  property_count: 2
  slug: amazon-connect-listcontactflowsresponse
- name: ListHoursOfOperationsResponse
  property_count: 2
  slug: amazon-connect-listhoursofoperationsresponse
- name: ListInstancesResponse
  property_count: 2
  slug: amazon-connect-listinstancesresponse
- name: ListQueuesResponse
  property_count: 2
  slug: amazon-connect-listqueuesresponse
- name: ListRoutingProfilesResponse
  property_count: 2
  slug: amazon-connect-listroutingprofilesresponse
- name: ListSecurityProfilesResponse
  property_count: 2
  slug: amazon-connect-listsecurityprofilesresponse
- name: ListUsersResponse
  property_count: 2
  slug: amazon-connect-listusersresponse
- name: MediaConcurrency
  property_count: 2
  slug: amazon-connect-mediaconcurrency
- name: Queue
  property_count: 9
  slug: amazon-connect-queue
- name: QueueSummary
  property_count: 4
  slug: amazon-connect-queuesummary
- name: RoutingProfile
  property_count: 10
  slug: amazon-connect-routingprofile
- name: RoutingProfileSummary
  property_count: 3
  slug: amazon-connect-routingprofilesummary
- name: SearchContactsRequest
  property_count: 6
  slug: amazon-connect-searchcontactsrequest
- name: SearchContactsResponse
  property_count: 3
  slug: amazon-connect-searchcontactsresponse
- name: SecurityProfileSummary
  property_count: 3
  slug: amazon-connect-securityprofilesummary
- name: StartChatContactRequest
  property_count: 7
  slug: amazon-connect-startchatcontactrequest
- name: StartChatContactResponse
  property_count: 3
  slug: amazon-connect-startchatcontactresponse
- name: StartOutboundVoiceContactRequest
  property_count: 7
  slug: amazon-connect-startoutboundvoicecontactrequest
- name: StartTaskContactRequest
  property_count: 12
  slug: amazon-connect-starttaskcontactrequest
- name: UpdateUserIdentityInfoRequest
  property_count: 1
  slug: amazon-connect-updateuseridentityinforequest
- name: User
  property_count: 10
  slug: amazon-connect-user
- name: UserIdentityInfo
  property_count: 5
  slug: amazon-connect-useridentityinfo
- name: UserPhoneConfig
  property_count: 4
  slug: amazon-connect-userphoneconfig
- name: UserSummary
  property_count: 3
  slug: amazon-connect-usersummary
- name: ContactFlow
  property_count: 8
  slug: contact-flow
- name: ContactFlowSummary
  property_count: 5
  slug: contact-flow-summary
- name: Contact
  property_count: 11
  slug: contact
- name: ContactSummary
  property_count: 6
  slug: contact-summary
- name: CreateContactFlowRequest
  property_count: 5
  slug: create-contact-flow-request
- name: CreateContactFlowResponse
  property_count: 2
  slug: create-contact-flow-response
- name: CreateHoursOfOperationRequest
  property_count: 5
  slug: create-hours-of-operation-request
- name: CreateHoursOfOperationResponse
  property_count: 2
  slug: create-hours-of-operation-response
- name: CreateInstanceRequest
  property_count: 7
  slug: create-instance-request
- name: CreateInstanceResponse
  property_count: 2
  slug: create-instance-response
- name: CreateQueueRequest
  property_count: 6
  slug: create-queue-request
- name: CreateQueueResponse
  property_count: 2
  slug: create-queue-response
- name: CreateRoutingProfileRequest
  property_count: 6
  slug: create-routing-profile-request
- name: CreateRoutingProfileResponse
  property_count: 2
  slug: create-routing-profile-response
- name: CreateUserRequest
  property_count: 9
  slug: create-user-request
- name: CreateUserResponse
  property_count: 2
  slug: create-user-response
- name: DescribeContactFlowResponse
  property_count: 1
  slug: describe-contact-flow-response
- name: DescribeContactResponse
  property_count: 1
  slug: describe-contact-response
- name: DescribeInstanceResponse
  property_count: 1
  slug: describe-instance-response
- name: DescribeQueueResponse
  property_count: 1
  slug: describe-queue-response
- name: DescribeRoutingProfileResponse
  property_count: 1
  slug: describe-routing-profile-response
- name: DescribeUserResponse
  property_count: 1
  slug: describe-user-response
- name: GetCurrentMetricDataRequest
  property_count: 5
  slug: get-current-metric-data-request
- name: GetCurrentMetricDataResponse
  property_count: 3
  slug: get-current-metric-data-response
- name: GetMetricDataRequest
  property_count: 7
  slug: get-metric-data-request
- name: GetMetricDataResponse
  property_count: 2
  slug: get-metric-data-response
- name: HoursOfOperationConfig
  property_count: 3
  slug: hours-of-operation-config
- name: HoursOfOperationSummary
  property_count: 3
  slug: hours-of-operation-summary
- name: HoursOfOperationTimeSlice
  property_count: 2
  slug: hours-of-operation-time-slice
- name: Instance
  property_count: 9
  slug: instance
- name: InstanceSummary
  property_count: 7
  slug: instance-summary
- name: ListAgentStatusesResponse
  property_count: 2
  slug: list-agent-statuses-response
- name: ListContactFlowsResponse
  property_count: 2
  slug: list-contact-flows-response
- name: ListHoursOfOperationsResponse
  property_count: 2
  slug: list-hours-of-operations-response
- name: ListInstancesResponse
  property_count: 2
  slug: list-instances-response
- name: ListQueuesResponse
  property_count: 2
  slug: list-queues-response
- name: ListRoutingProfilesResponse
  property_count: 2
  slug: list-routing-profiles-response
- name: ListSecurityProfilesResponse
  property_count: 2
  slug: list-security-profiles-response
- name: ListUsersResponse
  property_count: 2
  slug: list-users-response
- name: MediaConcurrency
  property_count: 2
  slug: media-concurrency
- name: Queue
  property_count: 9
  slug: queue
- name: QueueSummary
  property_count: 4
  slug: queue-summary
- name: RoutingProfile
  property_count: 10
  slug: routing-profile
- name: RoutingProfileSummary
  property_count: 3
  slug: routing-profile-summary
- name: SearchContactsRequest
  property_count: 6
  slug: search-contacts-request
- name: SearchContactsResponse
  property_count: 3
  slug: search-contacts-response
- name: SecurityProfileSummary
  property_count: 3
  slug: security-profile-summary
- name: StartChatContactRequest
  property_count: 7
  slug: start-chat-contact-request
- name: StartChatContactResponse
  property_count: 3
  slug: start-chat-contact-response
- name: StartOutboundVoiceContactRequest
  property_count: 7
  slug: start-outbound-voice-contact-request
- name: StartTaskContactRequest
  property_count: 12
  slug: start-task-contact-request
- name: UpdateUserIdentityInfoRequest
  property_count: 1
  slug: update-user-identity-info-request
- name: UserIdentityInfo
  property_count: 5
  slug: user-identity-info
- name: UserPhoneConfig
  property_count: 4
  slug: user-phone-config
- name: User
  property_count: 10
  slug: user
- name: UserSummary
  property_count: 3
  slug: user-summary
json_structures:
- name: Agent Status Summary Structure
  property_count: 4
  slug: agent-status-summary-structure
- name: Amazon Connect Instance Structure
  property_count: 11
  slug: amazon-connect-instance-structure
- name: Amazon Connect Structure
  property_count: 0
  slug: amazon-connect-structure
- name: Contact Flow Structure
  property_count: 8
  slug: contact-flow-structure
- name: Contact Flow Summary Structure
  property_count: 5
  slug: contact-flow-summary-structure
- name: Contact Structure
  property_count: 11
  slug: contact-structure
- name: Contact Summary Structure
  property_count: 6
  slug: contact-summary-structure
- name: Create Contact Flow Request Structure
  property_count: 5
  slug: create-contact-flow-request-structure
- name: Create Contact Flow Response Structure
  property_count: 2
  slug: create-contact-flow-response-structure
- name: Create Hours Of Operation Request Structure
  property_count: 5
  slug: create-hours-of-operation-request-structure
- name: Create Hours Of Operation Response Structure
  property_count: 2
  slug: create-hours-of-operation-response-structure
- name: Create Instance Request Structure
  property_count: 7
  slug: create-instance-request-structure
- name: Create Instance Response Structure
  property_count: 2
  slug: create-instance-response-structure
- name: Create Queue Request Structure
  property_count: 6
  slug: create-queue-request-structure
- name: Create Queue Response Structure
  property_count: 2
  slug: create-queue-response-structure
- name: Create Routing Profile Request Structure
  property_count: 6
  slug: create-routing-profile-request-structure
- name: Create Routing Profile Response Structure
  property_count: 2
  slug: create-routing-profile-response-structure
- name: Create User Request Structure
  property_count: 9
  slug: create-user-request-structure
- name: Create User Response Structure
  property_count: 2
  slug: create-user-response-structure
- name: Describe Contact Flow Response Structure
  property_count: 1
  slug: describe-contact-flow-response-structure
- name: Describe Contact Response Structure
  property_count: 1
  slug: describe-contact-response-structure
- name: Describe Instance Response Structure
  property_count: 1
  slug: describe-instance-response-structure
- name: Describe Queue Response Structure
  property_count: 1
  slug: describe-queue-response-structure
- name: Describe Routing Profile Response Structure
  property_count: 1
  slug: describe-routing-profile-response-structure
- name: Describe User Response Structure
  property_count: 1
  slug: describe-user-response-structure
- name: Get Current Metric Data Request Structure
  property_count: 5
  slug: get-current-metric-data-request-structure
- name: Get Current Metric Data Response Structure
  property_count: 3
  slug: get-current-metric-data-response-structure
- name: Get Metric Data Request Structure
  property_count: 7
  slug: get-metric-data-request-structure
- name: Get Metric Data Response Structure
  property_count: 2
  slug: get-metric-data-response-structure
- name: Hours Of Operation Config Structure
  property_count: 3
  slug: hours-of-operation-config-structure
- name: Hours Of Operation Summary Structure
  property_count: 3
  slug: hours-of-operation-summary-structure
- name: Hours Of Operation Time Slice Structure
  property_count: 2
  slug: hours-of-operation-time-slice-structure
- name: Instance Structure
  property_count: 9
  slug: instance-structure
- name: Instance Summary Structure
  property_count: 7
  slug: instance-summary-structure
- name: List Agent Statuses Response Structure
  property_count: 2
  slug: list-agent-statuses-response-structure
- name: List Contact Flows Response Structure
  property_count: 2
  slug: list-contact-flows-response-structure
- name: List Hours Of Operations Response Structure
  property_count: 2
  slug: list-hours-of-operations-response-structure
- name: List Instances Response Structure
  property_count: 2
  slug: list-instances-response-structure
- name: List Queues Response Structure
  property_count: 2
  slug: list-queues-response-structure
- name: List Routing Profiles Response Structure
  property_count: 2
  slug: list-routing-profiles-response-structure
- name: List Security Profiles Response Structure
  property_count: 2
  slug: list-security-profiles-response-structure
- name: List Users Response Structure
  property_count: 2
  slug: list-users-response-structure
- name: Media Concurrency Structure
  property_count: 2
  slug: media-concurrency-structure
- name: Queue Structure
  property_count: 9
  slug: queue-structure
- name: Queue Summary Structure
  property_count: 4
  slug: queue-summary-structure
- name: Routing Profile Structure
  property_count: 10
  slug: routing-profile-structure
- name: Routing Profile Summary Structure
  property_count: 3
  slug: routing-profile-summary-structure
- name: Search Contacts Request Structure
  property_count: 6
  slug: search-contacts-request-structure
- name: Search Contacts Response Structure
  property_count: 3
  slug: search-contacts-response-structure
- name: Security Profile Summary Structure
  property_count: 3
  slug: security-profile-summary-structure
- name: Start Chat Contact Request Structure
  property_count: 7
  slug: start-chat-contact-request-structure
- name: Start Chat Contact Response Structure
  property_count: 3
  slug: start-chat-contact-response-structure
- name: Start Outbound Voice Contact Request Structure
  property_count: 7
  slug: start-outbound-voice-contact-request-structure
- name: Start Task Contact Request Structure
  property_count: 12
  slug: start-task-contact-request-structure
- name: Update User Identity Info Request Structure
  property_count: 1
  slug: update-user-identity-info-request-structure
- name: User Identity Info Structure
  property_count: 5
  slug: user-identity-info-structure
- name: User Phone Config Structure
  property_count: 4
  slug: user-phone-config-structure
- name: User Structure
  property_count: 10
  slug: user-structure
- name: User Summary Structure
  property_count: 3
  slug: user-summary-structure
jsonld:
- class_count: 61
  name: Amazon Connect Context
  property_count: 132
  slug: amazon-connect-context
layout: provider
modified: '2026-09-16'
name: Amazon Connect
nav: Providers
network: true
overview: 'Amazon Connect is listed with 60 APIs on the [APIs.io](https://apis.io/) network, including Agent Statuses API, Authentication API, Contact Flows API, and 57 more. Tagged areas include Amazon Web Services, Chat, Contact Center, Customer Service, and Voice.


  The Amazon Connect catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Connect''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 37 more developer resources.'
plans:
- name: Amazon Connect Plans Pricing
  plan_count: 4
  slug: amazon-connect-plans-pricing
- name: Amazon Connect Price Estimates
  plan_count: 0
  slug: amazon-connect-price-estimates
random_paper: 21
rate_limits:
- limit_count: 22
  name: Amazon Connect Rate Limits
  slug: amazon-connect-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Amazon Connect — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-connect-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Amazon Connect API Rules
  rule_count: 42
  severity_counts:
    error: 16
    hint: 0
    info: 3
    warn: 23
  slug: amazon-connect-spectral-rules
score:
  band: exemplar
  composite: 72.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 84.0
    catalog_earned_first_party: 12.0
    catalog_gap: 31.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 93.4
    contract_governance: 27.3
    contract_quality: 75.5
    developer_ergonomics: 89.3
    discoverability: 66.1
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 70.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 51
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/amazon-connect/amazon-connect-2026-06-20T171608.png
security:
- kind: authentication
  name: Amazon Connect Authentication
  slug: amazon-connect-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Amazon Connect Domain Security
  slug: amazon-connect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Connect Vulnerability Disclosure
  slug: amazon-connect-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Connect Trust Center
  slug: amazon-connect-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-connect
tags:
- Amazon Web Services
- Chat
- Contact Center
- Customer Service
- Voice
- Artificial Intelligence
- Omnichannel
use_cases:
- description: Deploy an omnichannel contact center handling voice, chat, email, and messaging with intelligent routing to the right agents.
  name: Customer Support Contact Center
- description: Build conversational AI flows that handle common customer requests in 30+ languages without agent involvement.
  name: AI-Powered Self-Service
- description: Reduce average handle time with real-time AI guidance, unified agent workspace, and automated post-contact work.
  name: Agent Productivity Improvement
- description: Run appointment reminders, subscription renewals, payment notifications, and telemarketing campaigns at scale.
  name: Outbound Customer Engagement
- description: Use Voice ID for real-time caller authentication and fraud risk detection in voice contact center interactions.
  name: Fraud Prevention
- description: Analyze 100% of customer interactions with Contact Lens for regulatory compliance and quality assurance.
  name: Compliance and Quality Monitoring
website: https://aws.amazon.com/connect/
---
