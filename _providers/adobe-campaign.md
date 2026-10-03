---
access_model:
  confidence: high
  label: Paid · Contact sales · API access gated
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - https://experienceleague.adobe.com/en/docs/campaign/campaign-v8/developer/apis/get-started-apis
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.5
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 25
  human_in_the_loop: 3
  name: Adobe Campaign Agentic Access
  operation_count: 35
  slug: adobe-campaign-agentic-access
  summary_line: 35 operations · 25 acting · 3 human-in-the-loop
api_count: 2
apis:
- description: 'An open-source JavaScript SDK that wraps Adobe Campaign Classic SOAP APIs in a simple, expressive, JavaScript-idiomatic interface. The SDK supports asynchronous promise-based operations for querying, '
  name: Adobe Campaign Classic JavaScript SDK
  slug: classic-javascript-sdk
- description: 'A Node.js JavaScript SDK wrapping Adobe Campaign Standard REST APIs for use in Adobe I/O Runtime and App Builder applications. Provides convenience methods for profile management, service operations, '
  name: Adobe I/O Campaign Standard SDK
  slug: io-campaign-standard-sdk
- description: Native mobile SDK extensions for iOS and Android that integrate Adobe Campaign push notifications, in-app messaging, and local notifications into mobile applications. Includes the Campaign Classic ext
  name: Adobe Experience Platform Mobile SDK - Campaign Extensions
  slug: experience-platform-mobile-sdk---campaign-extensions
- baseURL: https://mc.adobe.io/{ORGANIZATION}/campaign
  baseurl_source: declared
  description: Access custom resources defined in Campaign Standard, both profile-linked and standalone.
  name: Adobe Campaign Custom Resources API
  phrasing_intents:
  - id: listProfileLinkedCustomResources
    intent: List records of a profile-linked custom resource
    question: How do I read records from a custom resource that extends profiles in Adobe Campaign Standard?
  - id: listCustomResources
    intent: List records of a standalone custom resource
    question: How can I fetch records from a custom resource that isn't linked to profiles?
  phrasing_ops: 2
  slug: adobe-campaign-custom-resources-api
- baseURL: https://{instance}.campaign.adobe.com
  baseurl_source: declared
  description: Write, update, and delete data records using the xtk:session#Write method. Supports insert, insertOrUpdate, update, and delete operations via the _operation attribute.
  name: Adobe Campaign Data Management API
  phrasing_intents:
  - id: sessionWrite
    intent: Insert, update or delete a single data record
    question: How do I insert or update one record in a Campaign schema over SOAP?
  - id: sessionWriteCollection
    intent: Write many data records in one call
    question: How can I write a batch of records to a Campaign schema in one request?
  phrasing_ops: 2
  slug: adobe-campaign-data-management-api
- baseURL: https://{instance}.campaign.adobe.com
  baseurl_source: declared
  description: Prepare and submit message deliveries including email, SMS, and push notifications.
  name: Adobe Campaign Delivery API
  phrasing_intents:
  - id: deliveryPrepareAndStart
    intent: Prepare and immediately send a delivery
    question: How do I compute a delivery's target and start sending it in one step?
  - id: submitDelivery
    intent: Submit a delivery for processing
    question: How do I submit a delivery so Campaign picks it up for processing?
  phrasing_ops: 2
  slug: adobe-campaign-delivery-api
- baseURL: https://mc.adobe.io/{ORGANIZATION}/campaign
  baseurl_source: declared
  description: Retrieve marketing event history for profiles including delivery logs and mirror page links.
  name: Adobe Campaign Marketing History API
  phrasing_intents:
  - id: getMarketingHistory
    intent: Get a profile's marketing history
    question: How do I see which messages were sent to a specific profile?
  phrasing_ops: 1
  slug: adobe-campaign-marketing-history-api
- baseURL: https://mc.adobe.io/{ORGANIZATION}/campaign
  baseurl_source: declared
  description: Discover resource schemas, fields, filters, and data policies for Campaign Standard resources.
  name: Adobe Campaign Metadata API
  phrasing_intents:
  - id: getResourceMetadata
    intent: Describe a resource's fields and filters
    question: How do I find out which fields and data types a Campaign Standard resource has?
  phrasing_ops: 1
  slug: adobe-campaign-metadata-api
- baseURL: https://mc.adobe.io/{ORGANIZATION}/campaign
  baseurl_source: declared
  description: Retrieve organizational unit structures used for access control and data partitioning.
  name: Adobe Campaign Organizational Units API
  phrasing_intents:
  - id: listOrgUnits
    intent: List organizational units
    question: How do I see the organizational units that partition access in Adobe Campaign?
  phrasing_ops: 1
  slug: adobe-campaign-organizational-units-api
- baseURL: https://mc.adobe.io/{ORGANIZATION}/campaign
  baseurl_source: declared
  description: Create GDPR and CCPA privacy access and deletion requests for data subject compliance.
  name: Adobe Campaign Privacy API
  phrasing_intents:
  - id: createPrivacyRequest
    intent: Create a GDPR or CCPA privacy request
    question: How do I handle a GDPR request to delete someone's data in Adobe Campaign?
  phrasing_ops: 1
  slug: adobe-campaign-privacy-api
- baseURL: https://mc.adobe.io/{ORGANIZATION}/campaign
  baseurl_source: declared
  description: The ProfileAndServices API from Adobe Campaign — 2 operation(s) for profileandservices.
  name: Adobe Campaign ProfileAndServices API
  phrasing_intents:
  - id: listServices
    intent: List subscription services
    question: How do I see all the subscription services set up in Adobe Campaign?
  - id: createService
    intent: Create a subscription service
    question: How do I set up a new newsletter or subscription service?
  - id: getService
    intent: Get a subscription service
    question: How do I look up the details of one subscription service?
  - id: updateService
    intent: Update a subscription service
    question: How do I rename an existing subscription service?
  - id: deleteService
    intent: Delete a subscription service
    question: How do I permanently remove a subscription service I no longer use?
  phrasing_ops: 5
  slug: adobe-campaign-profileandservices-api
- baseURL: https://mc.adobe.io/{ORGANIZATION}/campaign
  baseurl_source: declared
  description: Manage recipient profiles including creation, retrieval, update, and deletion of contact records.
  name: Adobe Campaign Profiles API
  phrasing_intents:
  - id: listProfiles
    intent: List recipient profiles
    question: How do I list the recipient profiles in Adobe Campaign Standard?
  - id: createProfile
    intent: Create a recipient profile
    question: How do I add a new contact to Adobe Campaign?
  - id: getProfile
    intent: Get a recipient profile
    question: How do I look up a single recipient profile?
  - id: updateProfile
    intent: Update a recipient profile
    question: How do I change an existing contact's email or phone number?
  - id: deleteProfile
    intent: Delete a recipient profile
    question: How do I permanently remove a contact from Campaign?
  phrasing_ops: 5
  slug: adobe-campaign-profiles-api
- baseURL: https://{instance}.campaign.adobe.com
  baseurl_source: declared
  description: Execute queries against Campaign schemas using the xtk:queryDef interface. Supports get, getIfExists, select, and count operations with XPath field expressions, WHERE conditions, and pagination.
  name: Adobe Campaign Query Definition API
  phrasing_intents:
  - id: executeQuery
    intent: Query records from a Campaign schema
    question: How do I query records from any Campaign schema with XPath fields?
  phrasing_ops: 1
  slug: adobe-campaign-query-definition-api
- baseURL: https://{instance}.campaign.adobe.com
  baseurl_source: declared
  description: Push real-time transactional events for immediate or batched processing by the Message Center execution instances.
  name: Adobe Campaign Real-Time Events API
  phrasing_intents:
  - id: pushEvent
    intent: Push one real-time transactional event
    question: How do I send a single transactional event to Message Center over SOAP?
  - id: pushEvents
    intent: Push a batch of real-time events
    question: How can I send many transactional events to Message Center in one call?
  phrasing_ops: 2
  slug: adobe-campaign-real-time-events-api
- baseURL: https://{instance}.campaign.adobe.com
  baseurl_source: declared
  description: Authenticate and manage server sessions. Logon returns session and security tokens required for all subsequent API calls.
  name: Adobe Campaign Session Management API
  phrasing_intents:
  - id: sessionLogon
    intent: Log on and get session tokens
    question: How do I authenticate to the Adobe Campaign SOAP API with a username and password?
  - id: sessionLogout
    intent: Log out and invalidate the session
    question: How do I end my Campaign SOAP session when I'm done?
  phrasing_ops: 2
  slug: adobe-campaign-session-management-api
- baseURL: https://{instance}.campaign.adobe.com
  baseurl_source: declared
  description: Subscribe and unsubscribe recipients to and from information services.
  name: Adobe Campaign Subscription API
  phrasing_intents:
  - id: subscribe
    intent: Subscribe a recipient to an information service
    question: How do I subscribe a recipient to an information service by the service's internal name?
  - id: unsubscribe
    intent: Unsubscribe a recipient from an information service
    question: How do I take a recipient off an information service using its internal name?
  phrasing_ops: 2
  slug: adobe-campaign-subscription-api
- baseURL: https://mc.adobe.io/{ORGANIZATION}/campaign
  baseurl_source: declared
  description: Subscribe and unsubscribe profiles to and from services.
  name: Adobe Campaign Subscriptions API
  phrasing_intents:
  - id: subscribeProfile
    intent: Subscribe a profile to a service
    question: How do I sign a profile up for a subscription service using the REST API?
  - id: unsubscribeProfile
    intent: Remove a profile's subscription from a service
    question: How do I remove a profile's subscription to a service by PKEY?
  phrasing_ops: 2
  slug: adobe-campaign-subscriptions-api
- baseURL: https://mc.adobe.io/{ORGANIZATION}/campaign
  baseurl_source: declared
  description: Trigger and monitor transactional messages across email, SMS, and push notification channels.
  name: Adobe Campaign Transactional Messages API
  phrasing_intents:
  - id: triggerTransactionalEvent
    intent: Trigger a transactional message
    question: How do I send an order confirmation email with Adobe Campaign Standard?
  - id: getTransactionalEventStatus
    intent: Check a transactional event's status
    question: How do I check whether a transactional message I triggered was delivered?
  phrasing_ops: 2
  slug: adobe-campaign-transactional-messages-api
- baseURL: https://{instance}.campaign.adobe.com
  baseurl_source: declared
  description: Start, stop, and signal workflows. PostEvent sends asynchronous signals to trigger workflow transitions.
  name: Adobe Campaign Workflow API
  phrasing_intents:
  - id: workflowStart
    intent: Start a stopped workflow over SOAP
    question: How do I start a stopped workflow by its internal ID using the SOAP API?
  - id: workflowStop
    intent: Stop a running workflow over SOAP
    question: How do I stop a running workflow by internal ID over SOAP?
  - id: workflowPostEvent
    intent: Signal a workflow's external signal activity
    question: How do I trigger an external signal activity inside a running workflow?
  phrasing_ops: 3
  slug: adobe-campaign-workflow-api
- baseURL: https://mc.adobe.io/{ORGANIZATION}/campaign
  baseurl_source: declared
  description: Control workflow execution including starting, pausing, resuming, and stopping marketing workflows.
  name: Adobe Campaign Workflows API
  phrasing_intents:
  - id: controlWorkflow
    intent: Start, pause, resume or stop a workflow
    question: How do I pause or resume a Campaign Standard workflow through the REST API?
  phrasing_ops: 1
  slug: adobe-campaign-workflows-api
artifact_total: 165
asyncapis:
- description: Event-driven transactional messaging system for Adobe Campaign. Supports triggering personalized messages across email, SMS, and push notification channels in response to real-time customer events. Ev
  name: Adobe Campaign Transactional Messaging Events
  slug: adobe-campaign-transactional-messaging-asyncapi-original
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Adobe Campaign Classic Custom Resources API
  slug: open-adobe-campaign-custom-resources-api
- collection_type: open
  name: Adobe Campaign Classic Custom Resources Data Management API
  slug: open-adobe-campaign-data-management-api
- collection_type: open
  name: Adobe Campaign Classic Custom Resources Delivery API
  slug: open-adobe-campaign-delivery-api
- collection_type: open
  name: Adobe Campaign Classic Custom Resources Marketing History API
  slug: open-adobe-campaign-marketing-history-api
- collection_type: open
  name: Adobe Campaign Classic Custom Resources Metadata API
  slug: open-adobe-campaign-metadata-api
- collection_type: open
  name: Adobe Campaign Classic Custom Resources Organizational Units API
  slug: open-adobe-campaign-organizational-units-api
- collection_type: open
  name: Adobe Campaign Classic Custom Resources Privacy API
  slug: open-adobe-campaign-privacy-api
- collection_type: open
  name: Adobe Campaign Classic Custom Resources ProfileAndServices API
  slug: open-adobe-campaign-profileandservices-api
- collection_type: open
  name: Adobe Campaign Classic Custom Resources Profiles API
  slug: open-adobe-campaign-profiles-api
- collection_type: open
  name: Adobe Campaign Classic Custom Resources Query Definition API
  slug: open-adobe-campaign-query-definition-api
- collection_type: open
  name: Adobe Campaign Classic Custom Resources Real-Time Events API
  slug: open-adobe-campaign-real-time-events-api
- collection_type: open
  name: Adobe Campaign Classic Custom Resources Session Management API
  slug: open-adobe-campaign-session-management-api
- collection_type: open
  name: Adobe Campaign Classic Custom Resources Subscription API
  slug: open-adobe-campaign-subscription-api
- collection_type: open
  name: Adobe Campaign Classic Custom Resources Subscriptions API
  slug: open-adobe-campaign-subscriptions-api
- collection_type: open
  name: Adobe Campaign Classic Custom Resources Transactional Messages API
  slug: open-adobe-campaign-transactional-messages-api
- collection_type: open
  name: Adobe Campaign Classic Custom Resources Workflow API
  slug: open-adobe-campaign-workflow-api
- collection_type: open
  name: Adobe Campaign Classic Custom Resources Workflows API
  slug: open-adobe-campaign-workflows-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.adobe.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/capabilities/adobe-campaign-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/adobe-campaign-capability-edges.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/packages/adobe-campaign-packages.yml
  title: ''
  type: Packages
  url: packages/adobe-campaign-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/packages/adobe-campaign-packages.yml
  title: ''
  type: SDKs
  url: packages/adobe-campaign-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/well-known/adobe-campaign-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adobe-campaign-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/well-known/adobe-campaign-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/adobe-campaign-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/llms/adobe-campaign-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adobe-campaign-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/mcp/adobe-campaign-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/adobe-campaign-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/conformance/adobe-campaign-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adobe-campaign-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/security/adobe-campaign-trust-center.yml
  title: ''
  type: Compliance
  url: security/adobe-campaign-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/security/adobe-campaign-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/adobe-campaign-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/security/adobe-campaign-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/adobe-campaign-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/errors/adobe-campaign-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adobe-campaign-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/lifecycle/adobe-campaign-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/adobe-campaign-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/lifecycle/adobe-campaign-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/adobe-campaign-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/scopes/adobe-campaign-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/adobe-campaign-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/conventions/adobe-campaign-conventions.yml
  title: ''
  type: Conventions
  url: conventions/adobe-campaign-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/changelog/adobe-campaign-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/adobe-campaign-changelog.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/sandbox/adobe-campaign-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/adobe-campaign-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/data-model/adobe-campaign-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adobe-campaign-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/plans/adobe-campaign-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adobe-campaign-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/rate-limits/adobe-campaign-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/adobe-campaign-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/finops/adobe-campaign-finops.yml
  title: ''
  type: FinOps
  url: finops/adobe-campaign-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.adobe.com/
- group: docs
  title: ''
  type: Documentation
  url: https://experienceleague.adobe.com/en/docs/campaign/campaign-v8/campaign-home
- group: docs
  title: ''
  type: APIReference
  url: https://experienceleague.adobe.com/en/docs/campaign/campaign-v8/developer/apis/get-started-apis
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adobe
- group: start
  title: ''
  type: SignUp
  url: https://developer.adobe.com/console
- group: commercial
  title: ''
  type: Pricing
  url: https://business.adobe.com/products/campaign/adobe-campaign.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://experienceleague.adobe.com/en/docs/campaign/campaign-v8/releases/release-notes
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/adobe/acc-js-sdk/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/adobe/acc-js-sdk/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/adobe/acc-js-sdk/blob/master/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/adobe/acc-js-sdk/blob/master/LICENSE
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/agentic-access/adobe-campaign-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adobe-campaign-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/security/adobe-campaign-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/adobe-campaign-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/security/adobe-campaign-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adobe-campaign-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/authentication/adobe-campaign-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adobe-campaign-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/adobe-campaign
- group: start
  title: ''
  type: Portal
  url: https://developer.adobe.com/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.adobe.com/developer-console/docs/guides/authentication/
- group: start
  title: ''
  type: GettingStarted
  url: https://experienceleague.adobe.com/docs/campaign-learn/tutorials/overview.html
- group: operate
  title: ''
  type: Support
  url: https://experienceleague.adobe.com/docs/customer-one/using/home.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adobe.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adobe.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adobe.com/privacy.html
- group: company
  title: ''
  type: Blog
  url: https://business.adobe.com/blog/
created: '2024-01-01'
description: 'Adobe Campaign is Adobe''s enterprise cross-channel campaign management and marketing automation platform, orchestrating email, SMS, push, direct mail and web messaging against a customer-owned marketing database. It ships two distinct programmable surfaces: a JSON REST API on https://mc.adobe.io/{ORGANIZATION}/campaign covering profiles, services and subscriptions, custom resources, workflows, privacy requests and transactional messaging, authenticated with an Adobe IMS OAuth Server-to-Server bearer token plus an X-Api-Key; and the Campaign Classic SOAP-over-HTTP surface on the customer''s own instance host, authenticated with a session-token pair from xtk:session#Logon. Campaign v8 is the current generation, Campaign Classic v7 is the legacy on-premise line, and Adobe has deprecated Campaign Standard in favour of Adobe Journey Optimizer. The data model is extended per tenant, so the deployed shape must be discovered at runtime rather than assumed from a specification.'
examples:
- key_count: 2
  name: Adobe Campaign Classic Delivery Request Example
  slug: adobe-campaign-classic-delivery-request-example
- key_count: 1
  name: Adobe Campaign Classic Push Event Request Example
  slug: adobe-campaign-classic-push-event-request-example
- key_count: 1
  name: Adobe Campaign Classic Push Event Response Example
  slug: adobe-campaign-classic-push-event-response-example
- key_count: 1
  name: Adobe Campaign Classic Push Events Request Example
  slug: adobe-campaign-classic-push-events-request-example
- key_count: 1
  name: Adobe Campaign Classic Query Definition Example
  slug: adobe-campaign-classic-query-definition-example
- key_count: 1
  name: Adobe Campaign Classic Query Result Example
  slug: adobe-campaign-classic-query-result-example
- key_count: 2
  name: Adobe Campaign Classic Session Logon Request Example
  slug: adobe-campaign-classic-session-logon-request-example
- key_count: 3
  name: Adobe Campaign Classic Session Logon Response Example
  slug: adobe-campaign-classic-session-logon-response-example
- key_count: 3
  name: Adobe Campaign Classic Soap Fault Example
  slug: adobe-campaign-classic-soap-fault-example
- key_count: 3
  name: Adobe Campaign Classic Subscription Request Example
  slug: adobe-campaign-classic-subscription-request-example
- key_count: 3
  name: Adobe Campaign Classic Workflow Post Event Request Example
  slug: adobe-campaign-classic-workflow-post-event-request-example
- key_count: 1
  name: Adobe Campaign Classic Workflow Request Example
  slug: adobe-campaign-classic-workflow-request-example
- key_count: 1
  name: Adobe Campaign Classic Write Collection Request Example
  slug: adobe-campaign-classic-write-collection-request-example
- key_count: 1
  name: Adobe Campaign Classic Write Request Example
  slug: adobe-campaign-classic-write-request-example
- key_count: 1
  name: Adobe Campaign Classic Write Response Example
  slug: adobe-campaign-classic-write-response-example
- key_count: 2
  name: Adobe Campaign Standard Marketing History Example
  slug: adobe-campaign-standard-marketing-history-example
- key_count: 4
  name: Adobe Campaign Standard Org Unit Example
  slug: adobe-campaign-standard-org-unit-example
- key_count: 5
  name: Adobe Campaign Standard Privacy Request Example
  slug: adobe-campaign-standard-privacy-request-example
- key_count: 2
  name: Adobe Campaign Standard Privacy Request Response Example
  slug: adobe-campaign-standard-privacy-request-response-example
- key_count: 8
  name: Adobe Campaign Standard Profile Create Example
  slug: adobe-campaign-standard-profile-create-example
- key_count: 10
  name: Adobe Campaign Standard Profile Example
  slug: adobe-campaign-standard-profile-example
- key_count: 10
  name: Adobe Campaign Standard Profile Update Example
  slug: adobe-campaign-standard-profile-update-example
- key_count: 3
  name: Adobe Campaign Standard Service Create Example
  slug: adobe-campaign-standard-service-create-example
- key_count: 8
  name: Adobe Campaign Standard Service Example
  slug: adobe-campaign-standard-service-example
- key_count: 4
  name: Adobe Campaign Standard Service Update Example
  slug: adobe-campaign-standard-service-update-example
- key_count: 1
  name: Adobe Campaign Standard Subscription Request Example
  slug: adobe-campaign-standard-subscription-request-example
- key_count: 6
  name: Adobe Campaign Standard Transactional Event Example
  slug: adobe-campaign-standard-transactional-event-example
- key_count: 3
  name: Adobe Campaign Standard Transactional Event Response Example
  slug: adobe-campaign-standard-transactional-event-response-example
- key_count: 4
  name: Adobe Campaign Standard Transactional Event Status Example
  slug: adobe-campaign-standard-transactional-event-status-example
- key_count: 1
  name: Adobe Campaign Standard Workflow Command Example
  slug: adobe-campaign-standard-workflow-command-example
features:
- description: Design and execute campaigns across email, SMS, push, direct mail, and web channels.
  name: Cross-Channel Campaign Orchestration
- description: Manage customer profiles, segments, and audiences for targeted messaging.
  name: Profile and Audience Management
- description: Send transactional and marketing emails with personalization and A/B testing.
  name: Email Delivery
- description: Build and execute automated marketing workflows with visual workflow designer.
  name: Workflow Automation
- description: Trigger personalized messages in real time based on customer events and behaviors.
  name: Real-Time Messaging
- description: Access campaign performance metrics, delivery statistics, and audience insights.
  name: Reporting and Analytics
- description: Dynamic content blocks and personalization fields for tailored messaging.
  name: Content Personalization
- description: Send mobile push notifications to iOS and Android devices.
  name: Push Notifications
- description: Send SMS campaigns and transactional messages to mobile subscribers.
  name: SMS Messaging
- description: Create and manage landing pages for campaign responses and lead capture.
  name: Landing Pages
finops:
- name: Adobe Campaign Finops
  service_category: Marketing Automation
  slug: adobe-campaign-finops
image: /assets/icons/adobe-campaign.png
integrations:
- description: Native integration with AEM, Analytics, and Target for unified marketing.
  name: Adobe Experience Cloud
- description: Real-time customer profile and audience sharing with AEP.
  name: Adobe Experience Platform
- description: CRM integration for syncing contacts, leads, and campaign data.
  name: Salesforce
- description: CRM integration for contact synchronization and campaign tracking.
  name: Microsoft Dynamics
json_schemas:
- name: DeliveryRequest
  property_count: 2
  slug: adobe-campaign-classic-delivery-request
- name: PushEventRequest
  property_count: 1
  slug: adobe-campaign-classic-push-event-request
- name: PushEventResponse
  property_count: 1
  slug: adobe-campaign-classic-push-event-response
- name: PushEventsRequest
  property_count: 1
  slug: adobe-campaign-classic-push-events-request
- name: QueryDefinition
  property_count: 1
  slug: adobe-campaign-classic-query-definition
- name: QueryResult
  property_count: 1
  slug: adobe-campaign-classic-query-result
- name: SessionLogonRequest
  property_count: 2
  slug: adobe-campaign-classic-session-logon-request
- name: SessionLogonResponse
  property_count: 3
  slug: adobe-campaign-classic-session-logon-response
- name: SOAPFault
  property_count: 3
  slug: adobe-campaign-classic-soap-fault
- name: SubscriptionRequest
  property_count: 3
  slug: adobe-campaign-classic-subscription-request
- name: WorkflowPostEventRequest
  property_count: 3
  slug: adobe-campaign-classic-workflow-post-event-request
- name: WorkflowRequest
  property_count: 1
  slug: adobe-campaign-classic-workflow-request
- name: WriteCollectionRequest
  property_count: 1
  slug: adobe-campaign-classic-write-collection-request
- name: WriteRequest
  property_count: 1
  slug: adobe-campaign-classic-write-request
- name: WriteResponse
  property_count: 1
  slug: adobe-campaign-classic-write-response
- name: MarketingHistory
  property_count: 2
  slug: adobe-campaign-standard-marketing-history
- name: OrgUnit
  property_count: 4
  slug: adobe-campaign-standard-org-unit
- name: PrivacyRequestResponse
  property_count: 2
  slug: adobe-campaign-standard-privacy-request-response
- name: PrivacyRequest
  property_count: 5
  slug: adobe-campaign-standard-privacy-request
- name: ProfileCreate
  property_count: 8
  slug: adobe-campaign-standard-profile-create
- name: Profile
  property_count: 15
  slug: adobe-campaign-standard-profile
- name: ProfileUpdate
  property_count: 11
  slug: adobe-campaign-standard-profile-update
- name: ServiceCreate
  property_count: 3
  slug: adobe-campaign-standard-service-create
- name: Service
  property_count: 8
  slug: adobe-campaign-standard-service
- name: ServiceUpdate
  property_count: 4
  slug: adobe-campaign-standard-service-update
- name: SubscriptionRequest
  property_count: 1
  slug: adobe-campaign-standard-subscription-request
- name: TransactionalEventResponse
  property_count: 3
  slug: adobe-campaign-standard-transactional-event-response
- name: TransactionalEvent
  property_count: 6
  slug: adobe-campaign-standard-transactional-event
- name: TransactionalEventStatus
  property_count: 4
  slug: adobe-campaign-standard-transactional-event-status
- name: WorkflowCommand
  property_count: 1
  slug: adobe-campaign-standard-workflow-command
json_structures:
- name: Adobe Campaign Classic Delivery Request Structure
  property_count: 2
  slug: adobe-campaign-classic-delivery-request-structure
- name: Adobe Campaign Classic Push Event Request Structure
  property_count: 1
  slug: adobe-campaign-classic-push-event-request-structure
- name: Adobe Campaign Classic Push Event Response Structure
  property_count: 1
  slug: adobe-campaign-classic-push-event-response-structure
- name: Adobe Campaign Classic Push Events Request Structure
  property_count: 1
  slug: adobe-campaign-classic-push-events-request-structure
- name: Adobe Campaign Classic Query Definition Structure
  property_count: 1
  slug: adobe-campaign-classic-query-definition-structure
- name: Adobe Campaign Classic Query Result Structure
  property_count: 1
  slug: adobe-campaign-classic-query-result-structure
- name: Adobe Campaign Classic Session Logon Request Structure
  property_count: 2
  slug: adobe-campaign-classic-session-logon-request-structure
- name: Adobe Campaign Classic Session Logon Response Structure
  property_count: 3
  slug: adobe-campaign-classic-session-logon-response-structure
- name: Adobe Campaign Classic Soap Fault Structure
  property_count: 3
  slug: adobe-campaign-classic-soap-fault-structure
- name: Adobe Campaign Classic Subscription Request Structure
  property_count: 3
  slug: adobe-campaign-classic-subscription-request-structure
- name: Adobe Campaign Classic Workflow Post Event Request Structure
  property_count: 3
  slug: adobe-campaign-classic-workflow-post-event-request-structure
- name: Adobe Campaign Classic Workflow Request Structure
  property_count: 1
  slug: adobe-campaign-classic-workflow-request-structure
- name: Adobe Campaign Classic Write Collection Request Structure
  property_count: 1
  slug: adobe-campaign-classic-write-collection-request-structure
- name: Adobe Campaign Classic Write Request Structure
  property_count: 1
  slug: adobe-campaign-classic-write-request-structure
- name: Adobe Campaign Classic Write Response Structure
  property_count: 1
  slug: adobe-campaign-classic-write-response-structure
- name: Adobe Campaign Standard Marketing History Structure
  property_count: 2
  slug: adobe-campaign-standard-marketing-history-structure
- name: Adobe Campaign Standard Org Unit Structure
  property_count: 4
  slug: adobe-campaign-standard-org-unit-structure
- name: Adobe Campaign Standard Privacy Request Response Structure
  property_count: 2
  slug: adobe-campaign-standard-privacy-request-response-structure
- name: Adobe Campaign Standard Privacy Request Structure
  property_count: 5
  slug: adobe-campaign-standard-privacy-request-structure
- name: Adobe Campaign Standard Profile Create Structure
  property_count: 8
  slug: adobe-campaign-standard-profile-create-structure
- name: Adobe Campaign Standard Profile Structure
  property_count: 15
  slug: adobe-campaign-standard-profile-structure
- name: Adobe Campaign Standard Profile Update Structure
  property_count: 11
  slug: adobe-campaign-standard-profile-update-structure
- name: Adobe Campaign Standard Service Create Structure
  property_count: 3
  slug: adobe-campaign-standard-service-create-structure
- name: Adobe Campaign Standard Service Structure
  property_count: 8
  slug: adobe-campaign-standard-service-structure
- name: Adobe Campaign Standard Service Update Structure
  property_count: 4
  slug: adobe-campaign-standard-service-update-structure
- name: Adobe Campaign Standard Subscription Request Structure
  property_count: 1
  slug: adobe-campaign-standard-subscription-request-structure
- name: Adobe Campaign Standard Transactional Event Response Structure
  property_count: 3
  slug: adobe-campaign-standard-transactional-event-response-structure
- name: Adobe Campaign Standard Transactional Event Status Structure
  property_count: 4
  slug: adobe-campaign-standard-transactional-event-status-structure
- name: Adobe Campaign Standard Transactional Event Structure
  property_count: 6
  slug: adobe-campaign-standard-transactional-event-structure
- name: Adobe Campaign Standard Workflow Command Structure
  property_count: 1
  slug: adobe-campaign-standard-workflow-command-structure
jsonld:
- class_count: 29
  name: Adobe Campaign Context
  property_count: 57
  slug: adobe-campaign-context
layout: provider
modified: '2026-08-13'
name: Adobe Campaign
nav: Providers
network: true
overview: 'Adobe Campaign publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Custom Resources API, Data Management API, Delivery API, and 17 more. Tagged areas include Campaign Management, Customer Experience, Email Marketing, Marketing Automation, and Multi-Channel Marketing.


  The Adobe Campaign catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Adobe Campaign''s developer surface includes changelog, sandbox, documentation, API reference, signup flow, pricing, release notes, and 41 more developer resources.'
plans:
- name: Adobe Campaign Plans Pricing
  plan_count: 2
  slug: adobe-campaign-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Adobe Campaign Rate Limits
  slug: adobe-campaign-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Adobe Campaign API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: adobe-campaign-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Adobe Campaign API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: adobe-campaign-jsonschema-spectral-rules
- effective_rule_count: 17
  extends: []
  name: Adobe Campaign API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 2
  slug: adobe-campaign-spectral-rules
scopes:
- name: Adobe Campaign Scopes
  scope_count: 0
  slug: adobe-campaign-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 72.0
  coverage:
    artifact_dirs: 33
    catalog_earned: 71.5
    catalog_earned_first_party: 16.0
    catalog_gap: 43.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 31.8
    contract_quality: 68.2
    developer_ergonomics: 72.0
    discoverability: 73.2
    operational_transparency: 65.8
  open_source:
    applies: true
    score: 40.0
  previous_composite: 72.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 44.2
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://raw.githubusercontent.com/api-evangelist/adobe-campaign/refs/heads/main/screenshots/adobe-campaign-2026-06-20T164822.png
security:
- kind: authentication
  name: Adobe Campaign Authentication
  slug: adobe-campaign-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Adobe Campaign Domain Security
  slug: adobe-campaign-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adobe Campaign Vulnerability Disclosure
  slug: adobe-campaign-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Adobe Campaign Trust Center
  slug: adobe-campaign-trust-center
  summary_line: trust center published
slug: adobe-campaign
solutions:
- description: Cloud-native marketing automation with modern REST APIs and visual workflow designer.
  name: Adobe Campaign Standard
- description: On-premises/hybrid marketing automation with SOAP and JavaScript APIs.
  name: Adobe Campaign Classic
- description: Latest generation combining Campaign Classic power with cloud scalability.
  name: Adobe Campaign v8
tags:
- Campaign Management
- Customer Experience
- Email Marketing
- Marketing Automation
- Multi-Channel Marketing
- Transactional Messaging
- Customer Data
- Adobe Experience Cloud
- SMS
- Push Notifications
- Workflow Automation
- Privacy
use_cases:
- description: Design, personalize, and send email campaigns with tracking and analytics.
  name: Email Marketing Campaigns
- description: Build multi-step customer journeys with triggers, conditions, and automated actions.
  name: Customer Journey Orchestration
- description: Send real-time transactional emails and SMS for order confirmations and alerts.
  name: Transactional Messaging
- description: Automate lead scoring and nurture sequences based on engagement data.
  name: Lead Nurturing
- description: Build dynamic audience segments for targeted campaign delivery.
  name: Audience Segmentation
- description: Coordinate messaging across email, SMS, push, and direct mail channels.
  name: Cross-Channel Coordination
website: https://www.adobe.com/
---
