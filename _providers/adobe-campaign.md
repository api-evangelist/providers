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
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-09-01'
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
- description: Access custom resources defined in Campaign Standard, both profile-linked and standalone.
  name: Adobe Campaign Custom Resources API
  slug: adobe-campaign-custom-resources-api
- description: Write, update, and delete data records using the xtk:session#Write method. Supports insert, insertOrUpdate, update, and delete operations via the _operation attribute.
  name: Adobe Campaign Data Management API
  slug: adobe-campaign-data-management-api
- description: Prepare and submit message deliveries including email, SMS, and push notifications.
  name: Adobe Campaign Delivery API
  slug: adobe-campaign-delivery-api
- description: Retrieve marketing event history for profiles including delivery logs and mirror page links.
  name: Adobe Campaign Marketing History API
  slug: adobe-campaign-marketing-history-api
- description: Discover resource schemas, fields, filters, and data policies for Campaign Standard resources.
  name: Adobe Campaign Metadata API
  slug: adobe-campaign-metadata-api
- description: Retrieve organizational unit structures used for access control and data partitioning.
  name: Adobe Campaign Organizational Units API
  slug: adobe-campaign-organizational-units-api
- description: Create GDPR and CCPA privacy access and deletion requests for data subject compliance.
  name: Adobe Campaign Privacy API
  slug: adobe-campaign-privacy-api
- description: The ProfileAndServices API from Adobe Campaign — 2 operation(s) for profileandservices.
  name: Adobe Campaign ProfileAndServices API
  slug: adobe-campaign-profileandservices-api
- description: Manage recipient profiles including creation, retrieval, update, and deletion of contact records.
  name: Adobe Campaign Profiles API
  slug: adobe-campaign-profiles-api
- description: Execute queries against Campaign schemas using the xtk:queryDef interface. Supports get, getIfExists, select, and count operations with XPath field expressions, WHERE conditions, and pagination.
  name: Adobe Campaign Query Definition API
  slug: adobe-campaign-query-definition-api
- description: Push real-time transactional events for immediate or batched processing by the Message Center execution instances.
  name: Adobe Campaign Real-Time Events API
  slug: adobe-campaign-real-time-events-api
- description: Authenticate and manage server sessions. Logon returns session and security tokens required for all subsequent API calls.
  name: Adobe Campaign Session Management API
  slug: adobe-campaign-session-management-api
- description: Subscribe and unsubscribe recipients to and from information services.
  name: Adobe Campaign Subscription API
  slug: adobe-campaign-subscription-api
- description: Subscribe and unsubscribe profiles to and from services.
  name: Adobe Campaign Subscriptions API
  slug: adobe-campaign-subscriptions-api
- description: Trigger and monitor transactional messages across email, SMS, and push notification channels.
  name: Adobe Campaign Transactional Messages API
  slug: adobe-campaign-transactional-messages-api
- description: Start, stop, and signal workflows. PostEvent sends asynchronous signals to trigger workflow transitions.
  name: Adobe Campaign Workflow API
  slug: adobe-campaign-workflow-api
- description: Control workflow execution including starting, pausing, resuming, and stopping marketing workflows.
  name: Adobe Campaign Workflows API
  slug: adobe-campaign-workflows-api
artifact_total: 166
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/adobe-campaign-capability-edges.yml
- group: build
  title: ''
  type: Packages
  url: packages/adobe-campaign-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/adobe-campaign-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/adobe-campaign-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/adobe-campaign-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adobe-campaign-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/adobe-campaign-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adobe-campaign-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/adobe-campaign-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/adobe-campaign-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/adobe-campaign-vulnerability-disclosure.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/adobe-campaign-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adobe-campaign-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/adobe-campaign-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/adobe-campaign-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adobe-campaign-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/adobe-campaign-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/adobe-campaign-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/adobe-campaign-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adobe-campaign-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adobe-campaign-rate-limits.yml
- group: commercial
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
  title: ''
  type: AgenticAccess
  url: agentic-access/adobe-campaign-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/adobe-campaign-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adobe-campaign-domain-security.yml
- group: auth
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
mcp_servers:
- description: ''
  name: Adobe Campaign MCP Server
  slug: adobe-campaign-mcp-server
modified: '2026-08-13'
name: Adobe Campaign
nav: Providers
network: true
overview: 'Adobe Campaign publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Custom Resources API, Data Management API, Delivery API, and 14 more. Tagged areas include Campaign Management, Customer Experience, Email Marketing, Marketing Automation, and Multi-Channel Marketing.


  The Adobe Campaign catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Adobe Campaign''s developer surface includes changelog, sandbox, documentation, API reference, signup flow, pricing, release notes, and 40 more developer resources.'
plans:
- name: Adobe Campaign Plans Pricing
  plan_count: 2
  slug: adobe-campaign-plans-pricing
random_paper: 19
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
  composite: 72.6
  coverage:
    artifact_dirs: 32
    catalog_gap: 43.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 31.8
    contract_quality: 75.0
    developer_ergonomics: 72.0
    discoverability: 75.9
    governance: 31.8
    operational_transparency: 57.9
  open_source:
    applies: true
    score: 40.0
  previous_composite: 72.6
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
    score: 73.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
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
- Workflow-Automation
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
website: https://developer.adobe.com/
---
