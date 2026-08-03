---
access_model:
  confidence: high
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Salesforce Marketing Cloud Agentic Access
  operation_count: 21
  slug: salesforce-marketing-cloud-agentic-access
  summary_line: 21 operations · 14 acting · 1 human-in-the-loop
api_count: 17
apis:
- description: Legacy SOAP-based API for Marketing Cloud operations, including email sends, subscriber management, and data extension operations.
  name: SOAP API
  slug: soap-api
- description: Specialized API for sending triggered, transactional messages including order confirmations, password resets, and real-time notifications.
  name: Transactional Messaging API
  slug: transactional-messaging-api
- description: API for creating, managing, and automating customer journeys across multiple channels and touchpoints.
  name: Journey Builder API
  slug: journey-builder-api
- description: API for managing data extensions, which are database tables used to store and segment customer data in Marketing Cloud.
  name: Data Extensions API
  slug: data-extensions-api
- description: API for creating and managing email send definitions, which define the configuration for sending emails to subscribers.
  name: Email Send Definition API
  slug: email-send-definition-api
- description: API for sending push notifications to mobile devices, managing device registrations, and tracking push message engagement.
  name: Mobile Push API
  slug: mobile-push-api
- description: API for sending SMS and MMS messages, managing mobile numbers, and handling keyword-based subscriptions.
  name: SMS/MMS API
  slug: smsmms-api
- description: API for managing marketing assets including images, documents, content blocks, and templates across Marketing Cloud.
  name: Asset API
  slug: asset-api
- description: API for leveraging AI-powered product and content recommendations to personalize customer experiences.
  name: Einstein Recommendations API
  slug: einstein-recommendations-api
- description: REST API for creating and manipulating marketing content in Content Builder, a single cross-channel repository for emails, images, text, content blocks, and other documents.
  name: Content Builder API
  slug: content-builder-api
- description: REST API for creating, reading, updating, and deleting contacts in Marketing Cloud.
  name: Contacts API
  slug: contacts-api
- description: API for initiating and managing marketing automations, including file upload, download, decryption, compression, and decompression operations within Automation Studio.
  name: Automation Studio API
  slug: automation-studio-api
- description: API for managing and performing marketing campaigns within Marketing Cloud.
  name: Campaign API
  slug: campaign-api
- description: API for registering callbacks and subscriptions to receive real-time event notifications from Marketing Cloud.
  name: Event Notification Service API
  slug: event-notification-service-api
- description: Manage marketing assets including images, documents, content blocks, and templates. The Asset API provides CRUD operations for all content types stored in Content Builder.
  name: Salesforce Marketing Cloud Assets API
  slug: salesforce-marketing-cloud-assets-api
- description: Create, retrieve, update, and delete contacts in Marketing Cloud. Contacts represent individuals who interact with your marketing campaigns across channels.
  name: Salesforce Marketing Cloud Contacts API
  slug: salesforce-marketing-cloud-contacts-api
- description: Create, manage, and automate customer journeys across multiple channels and touchpoints. Journeys define the automated workflows that guide customers through marketing interactions.
  name: Salesforce Marketing Cloud Journeys API
  slug: salesforce-marketing-cloud-journeys-api
artifact_total: 162
collections:
- collection_type: postman
  name: Salesforce Marketing Cloud REST Assets API
  slug: postman-salesforce-marketing-cloud-assets-api
- collection_type: postman
  name: Salesforce Marketing Cloud REST Assets Contacts API
  slug: postman-salesforce-marketing-cloud-contacts-api
- collection_type: postman
  name: Salesforce Marketing Cloud REST Assets Journeys API
  slug: postman-salesforce-marketing-cloud-journeys-api
- collection_type: open
  name: Salesforce Marketing Cloud REST API
  slug: open-salesforce-marketing-cloud
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/salesforce-marketing-cloud/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/salesforce-marketing-cloud-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salesforce-marketing-cloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/salesforce-marketing-cloud-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/salesforce-marketing-cloud-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://developer.salesforce.com/blogs/feed
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/salesforce-marketing-cloud-
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.salesforce.com/docs/marketing/marketing-cloud/overview
- group: docs
  title: ''
  type: Documentation
  url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/apis-overview.html
- group: auth
  title: ''
  type: Authentication
  url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/authentication.html
- group: docs
  title: ''
  type: APIReference
  url: https://developer.salesforce.com/docs/marketing/marketing-cloud/references
- group: operate
  title: ''
  type: Support
  url: https://help.salesforce.com/s/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.salesforce.com/
- group: build
  title: ''
  type: SDKs
  url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/sdks.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.salesforce.com/company/legal/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.salesforce.com/products/marketing-cloud/pricing/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/release-notes.html
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/rate-limiting.html
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/salesforce-marketingcloud/SFDC-MC-REST-Style-Guide
- group: learn
  title: ''
  type: Training
  url: https://trailhead.salesforce.com/en/content/learn/trails/get-started-with-marketing-cloud
created: '2024-01-15'
description: Salesforce Marketing Cloud is a comprehensive digital marketing platform that enables businesses to manage customer journeys, email marketing, mobile messaging, social media marketing, advertising, and data analytics.
examples:
- key_count: 4
  name: Salesforce Marketing Cloud Asset Collection Example
  slug: salesforce-marketing-cloud-asset-collection-example
- key_count: 8
  name: Salesforce Marketing Cloud Asset Definition Example
  slug: salesforce-marketing-cloud-asset-definition-example
- key_count: 14
  name: Salesforce Marketing Cloud Asset Example
  slug: salesforce-marketing-cloud-asset-example
- key_count: 4
  name: Salesforce Marketing Cloud Asset Query Example
  slug: salesforce-marketing-cloud-asset-query-example
- key_count: 2
  name: Salesforce Marketing Cloud Asset Type Example
  slug: salesforce-marketing-cloud-asset-type-example
- key_count: 2
  name: Salesforce Marketing Cloud Attribute Set Example
  slug: salesforce-marketing-cloud-attribute-set-example
- key_count: 2
  name: Salesforce Marketing Cloud Attribute Sets Response Example
  slug: salesforce-marketing-cloud-attribute-sets-response-example
- key_count: 2
  name: Salesforce Marketing Cloud Attribute Value Example
  slug: salesforce-marketing-cloud-attribute-value-example
- key_count: 4
  name: Salesforce Marketing Cloud Category Collection Example
  slug: salesforce-marketing-cloud-category-collection-example
- key_count: 6
  name: Salesforce Marketing Cloud Contact Example
  slug: salesforce-marketing-cloud-contact-example
- key_count: 4
  name: Salesforce Marketing Cloud Contact Response Example
  slug: salesforce-marketing-cloud-contact-response-example
- key_count: 2
  name: Salesforce Marketing Cloud Contact Search Request Example
  slug: salesforce-marketing-cloud-contact-search-request-example
- key_count: 4
  name: Salesforce Marketing Cloud Contact Search Response Example
  slug: salesforce-marketing-cloud-contact-search-response-example
- key_count: 2
  name: Salesforce Marketing Cloud Create Contacts Request Example
  slug: salesforce-marketing-cloud-create-contacts-request-example
- key_count: 6
  name: Salesforce Marketing Cloud Createasset Example
  slug: salesforce-marketing-cloud-createasset-example
- key_count: 6
  name: Salesforce Marketing Cloud Createcontacts Example
  slug: salesforce-marketing-cloud-createcontacts-example
- key_count: 6
  name: Salesforce Marketing Cloud Createjourney Example
  slug: salesforce-marketing-cloud-createjourney-example
- key_count: 4
  name: Salesforce Marketing Cloud Delete Contact Response Example
  slug: salesforce-marketing-cloud-delete-contact-response-example
- key_count: 3
  name: Salesforce Marketing Cloud Entry Event Example
  slug: salesforce-marketing-cloud-entry-event-example
- key_count: 2
  name: Salesforce Marketing Cloud Entry Event Response Example
  slug: salesforce-marketing-cloud-entry-event-response-example
- key_count: 3
  name: Salesforce Marketing Cloud Error Response Example
  slug: salesforce-marketing-cloud-error-response-example
- key_count: 6
  name: Salesforce Marketing Cloud Fireentryevent Example
  slug: salesforce-marketing-cloud-fireentryevent-example
- key_count: 5
  name: Salesforce Marketing Cloud Journey Activity Example
  slug: salesforce-marketing-cloud-journey-activity-example
- key_count: 4
  name: Salesforce Marketing Cloud Journey Collection Example
  slug: salesforce-marketing-cloud-journey-collection-example
- key_count: 8
  name: Salesforce Marketing Cloud Journey Definition Example
  slug: salesforce-marketing-cloud-journey-definition-example
- key_count: 14
  name: Salesforce Marketing Cloud Journey Example
  slug: salesforce-marketing-cloud-journey-example
- key_count: 3
  name: Salesforce Marketing Cloud Journey Exit Example
  slug: salesforce-marketing-cloud-journey-exit-example
- key_count: 4
  name: Salesforce Marketing Cloud Journey Goal Example
  slug: salesforce-marketing-cloud-journey-goal-example
- key_count: 5
  name: Salesforce Marketing Cloud Journey Trigger Example
  slug: salesforce-marketing-cloud-journey-trigger-example
- key_count: 2
  name: Salesforce Marketing Cloud Publish Response Example
  slug: salesforce-marketing-cloud-publish-response-example
- key_count: 6
  name: Salesforce Marketing Cloud Queryassets Example
  slug: salesforce-marketing-cloud-queryassets-example
- key_count: 6
  name: Salesforce Marketing Cloud Searchcontacts Example
  slug: salesforce-marketing-cloud-searchcontacts-example
- key_count: 1
  name: Salesforce Marketing Cloud Update Contact Request Example
  slug: salesforce-marketing-cloud-update-contact-request-example
features:
- description: Design, send, and track targeted email campaigns with dynamic content, personalization, and A/B testing capabilities.
  name: Email Marketing
- description: Create automated, multi-step customer journeys across email, SMS, push, and advertising channels with branching logic.
  name: Journey Builder
- description: Centralized contact database with attribute sets, segmentation, and cross-channel identity resolution.
  name: Contact Management
- description: Send real-time transactional messages like order confirmations and password resets with guaranteed delivery.
  name: Transactional Messaging
- description: Leverage AI-powered recommendations and predictive analytics to personalize content and optimize send times.
  name: Einstein AI Personalization
- description: Schedule and automate data imports, file transfers, SQL queries, and multi-step marketing workflows.
  name: Automation Studio
- description: Centralized content management system for creating, organizing, and reusing marketing assets across channels.
  name: Content Builder
- description: Subscribe to real-time webhook notifications for email tracking events, data changes, and audit activities.
  name: Event Notifications
finops:
- name: Salesforce Marketing Cloud Finops
  service_category: Marketing Automation
  slug: salesforce-marketing-cloud-finops
graphqls:
- description: Salesforce Marketing Cloud API covers email sends, automation, contacts, data extensions, journey builder, content builder, tracking events, and transactional messaging for digital marketing campaigns
  name: Salesforce Marketing Cloud GraphQL API
  slug: salesforce-marketing-cloud-graphql
image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
integrations:
- description: Bi-directional sync with Sales Cloud and Service Cloud for unified customer profiles and campaign attribution.
  name: Salesforce CRM
- description: Connect to unified customer data profiles for advanced segmentation and real-time personalization.
  name: Salesforce Data Cloud
- description: Track email campaign performance and website conversions with Google Analytics integration.
  name: Google Analytics
- description: Sync e-commerce customer data, purchase history, and cart events for targeted marketing automation.
  name: Shopify
- description: Integrate commerce data for personalized product recommendations and transactional messaging.
  name: Salesforce Commerce Cloud
json_schemas:
- name: AssetCollection
  property_count: 4
  slug: salesforce-marketing-cloud-asset-collection
- name: AssetDefinition
  property_count: 8
  slug: salesforce-marketing-cloud-asset-definition
- name: AssetQuery
  property_count: 4
  slug: salesforce-marketing-cloud-asset-query
- name: Asset
  property_count: 14
  slug: salesforce-marketing-cloud-asset
- name: AssetType
  property_count: 2
  slug: salesforce-marketing-cloud-asset-type
- name: AssetCollection
  property_count: 4
  slug: salesforce-marketing-cloud-assetcollection
- name: AssetDefinition
  property_count: 9
  slug: salesforce-marketing-cloud-assetdefinition
- name: AssetQuery
  property_count: 4
  slug: salesforce-marketing-cloud-assetquery
- name: AssetType
  property_count: 2
  slug: salesforce-marketing-cloud-assettype
- name: AttributeSet
  property_count: 2
  slug: salesforce-marketing-cloud-attribute-set
- name: AttributeSetsResponse
  property_count: 2
  slug: salesforce-marketing-cloud-attribute-sets-response
- name: AttributeValue
  property_count: 2
  slug: salesforce-marketing-cloud-attribute-value
- name: AttributeSet
  property_count: 2
  slug: salesforce-marketing-cloud-attributeset
- name: AttributeSetsResponse
  property_count: 2
  slug: salesforce-marketing-cloud-attributesetsresponse
- name: AttributeValue
  property_count: 2
  slug: salesforce-marketing-cloud-attributevalue
- name: CategoryCollection
  property_count: 4
  slug: salesforce-marketing-cloud-category-collection
- name: CategoryCollection
  property_count: 4
  slug: salesforce-marketing-cloud-categorycollection
- name: ContactResponse
  property_count: 4
  slug: salesforce-marketing-cloud-contact-response
- name: Contact
  property_count: 6
  slug: salesforce-marketing-cloud-contact
- name: ContactSearchRequest
  property_count: 2
  slug: salesforce-marketing-cloud-contact-search-request
- name: ContactSearchResponse
  property_count: 4
  slug: salesforce-marketing-cloud-contact-search-response
- name: ContactResponse
  property_count: 4
  slug: salesforce-marketing-cloud-contactresponse
- name: ContactSearchRequest
  property_count: 2
  slug: salesforce-marketing-cloud-contactsearchrequest
- name: ContactSearchResponse
  property_count: 4
  slug: salesforce-marketing-cloud-contactsearchresponse
- name: CreateContactsRequest
  property_count: 2
  slug: salesforce-marketing-cloud-create-contacts-request
- name: CreateContactsRequest
  property_count: 2
  slug: salesforce-marketing-cloud-createcontactsrequest
- name: DeleteContactResponse
  property_count: 4
  slug: salesforce-marketing-cloud-delete-contact-response
- name: DeleteContactResponse
  property_count: 4
  slug: salesforce-marketing-cloud-deletecontactresponse
- name: EntryEventResponse
  property_count: 2
  slug: salesforce-marketing-cloud-entry-event-response
- name: EntryEvent
  property_count: 3
  slug: salesforce-marketing-cloud-entry-event
- name: EntryEvent
  property_count: 3
  slug: salesforce-marketing-cloud-entryevent
- name: EntryEventResponse
  property_count: 2
  slug: salesforce-marketing-cloud-entryeventresponse
- name: ErrorResponse
  property_count: 3
  slug: salesforce-marketing-cloud-error-response
- name: ErrorResponse
  property_count: 3
  slug: salesforce-marketing-cloud-errorresponse
- name: JourneyActivity
  property_count: 5
  slug: salesforce-marketing-cloud-journey-activity
- name: JourneyCollection
  property_count: 4
  slug: salesforce-marketing-cloud-journey-collection
- name: JourneyDefinition
  property_count: 8
  slug: salesforce-marketing-cloud-journey-definition
- name: JourneyExit
  property_count: 3
  slug: salesforce-marketing-cloud-journey-exit
- name: JourneyGoal
  property_count: 4
  slug: salesforce-marketing-cloud-journey-goal
- name: Journey
  property_count: 14
  slug: salesforce-marketing-cloud-journey
- name: JourneyTrigger
  property_count: 5
  slug: salesforce-marketing-cloud-journey-trigger
- name: JourneyActivity
  property_count: 5
  slug: salesforce-marketing-cloud-journeyactivity
- name: JourneyCollection
  property_count: 4
  slug: salesforce-marketing-cloud-journeycollection
- name: JourneyDefinition
  property_count: 8
  slug: salesforce-marketing-cloud-journeydefinition
- name: JourneyExit
  property_count: 3
  slug: salesforce-marketing-cloud-journeyexit
- name: JourneyGoal
  property_count: 4
  slug: salesforce-marketing-cloud-journeygoal
- name: JourneyTrigger
  property_count: 5
  slug: salesforce-marketing-cloud-journeytrigger
- name: PublishResponse
  property_count: 2
  slug: salesforce-marketing-cloud-publish-response
- name: PublishResponse
  property_count: 2
  slug: salesforce-marketing-cloud-publishresponse
- name: UpdateContactRequest
  property_count: 1
  slug: salesforce-marketing-cloud-update-contact-request
- name: UpdateContactRequest
  property_count: 1
  slug: salesforce-marketing-cloud-updatecontactrequest
json_structures:
- name: Salesforce Marketing Cloud Asset Collection Structure
  property_count: 4
  slug: salesforce-marketing-cloud-asset-collection-structure
- name: Salesforce Marketing Cloud Asset Definition Structure
  property_count: 8
  slug: salesforce-marketing-cloud-asset-definition-structure
- name: Salesforce Marketing Cloud Asset Query Structure
  property_count: 4
  slug: salesforce-marketing-cloud-asset-query-structure
- name: Salesforce Marketing Cloud Asset Structure
  property_count: 14
  slug: salesforce-marketing-cloud-asset-structure
- name: Salesforce Marketing Cloud Asset Type Structure
  property_count: 2
  slug: salesforce-marketing-cloud-asset-type-structure
- name: Salesforce Marketing Cloud Attribute Set Structure
  property_count: 2
  slug: salesforce-marketing-cloud-attribute-set-structure
- name: Salesforce Marketing Cloud Attribute Sets Response Structure
  property_count: 2
  slug: salesforce-marketing-cloud-attribute-sets-response-structure
- name: Salesforce Marketing Cloud Attribute Value Structure
  property_count: 2
  slug: salesforce-marketing-cloud-attribute-value-structure
- name: Salesforce Marketing Cloud Category Collection Structure
  property_count: 4
  slug: salesforce-marketing-cloud-category-collection-structure
- name: Salesforce Marketing Cloud Contact Response Structure
  property_count: 4
  slug: salesforce-marketing-cloud-contact-response-structure
- name: Salesforce Marketing Cloud Contact Search Request Structure
  property_count: 2
  slug: salesforce-marketing-cloud-contact-search-request-structure
- name: Salesforce Marketing Cloud Contact Search Response Structure
  property_count: 4
  slug: salesforce-marketing-cloud-contact-search-response-structure
- name: Salesforce Marketing Cloud Contact Structure
  property_count: 6
  slug: salesforce-marketing-cloud-contact-structure
- name: Salesforce Marketing Cloud Create Contacts Request Structure
  property_count: 2
  slug: salesforce-marketing-cloud-create-contacts-request-structure
- name: Salesforce Marketing Cloud Delete Contact Response Structure
  property_count: 4
  slug: salesforce-marketing-cloud-delete-contact-response-structure
- name: Salesforce Marketing Cloud Entry Event Response Structure
  property_count: 2
  slug: salesforce-marketing-cloud-entry-event-response-structure
- name: Salesforce Marketing Cloud Entry Event Structure
  property_count: 3
  slug: salesforce-marketing-cloud-entry-event-structure
- name: Salesforce Marketing Cloud Error Response Structure
  property_count: 3
  slug: salesforce-marketing-cloud-error-response-structure
- name: Salesforce Marketing Cloud Journey Activity Structure
  property_count: 5
  slug: salesforce-marketing-cloud-journey-activity-structure
- name: Salesforce Marketing Cloud Journey Collection Structure
  property_count: 4
  slug: salesforce-marketing-cloud-journey-collection-structure
- name: Salesforce Marketing Cloud Journey Definition Structure
  property_count: 8
  slug: salesforce-marketing-cloud-journey-definition-structure
- name: Salesforce Marketing Cloud Journey Exit Structure
  property_count: 3
  slug: salesforce-marketing-cloud-journey-exit-structure
- name: Salesforce Marketing Cloud Journey Goal Structure
  property_count: 4
  slug: salesforce-marketing-cloud-journey-goal-structure
- name: Salesforce Marketing Cloud Journey Structure
  property_count: 14
  slug: salesforce-marketing-cloud-journey-structure
- name: Salesforce Marketing Cloud Journey Trigger Structure
  property_count: 5
  slug: salesforce-marketing-cloud-journey-trigger-structure
- name: Salesforce Marketing Cloud Publish Response Structure
  property_count: 2
  slug: salesforce-marketing-cloud-publish-response-structure
- name: Salesforce Marketing Cloud Structure
  property_count: 0
  slug: salesforce-marketing-cloud-structure
- name: Salesforce Marketing Cloud Update Contact Request Structure
  property_count: 1
  slug: salesforce-marketing-cloud-update-contact-request-structure
jsonld:
- class_count: 0
  name: Salesforce Marketing Cloud Context
  property_count: 0
  slug: salesforce-marketing-cloud-context
layout: provider
modified: '2026-05-19'
name: Salesforce Marketing Cloud
nav: Providers
network: true
overview: 'Salesforce Marketing Cloud publishes 3 APIs on the [APIs.io](https://apis.io/) network: Assets API, Contacts API, and Journeys API. Tagged areas include Automation, Customer Journey, Digital Marketing, Email, and Marketing.


  The Salesforce Marketing Cloud catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Salesforce Marketing Cloud''s developer surface includes authentication, engineering blog, documentation, API reference, support, pricing, changelog, and 13 more developer resources.'
plans:
- name: Salesforce Marketing Cloud Plans Pricing
  plan_count: 1
  slug: salesforce-marketing-cloud-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 1
  name: Salesforce Marketing Cloud Rate Limits
  slug: salesforce-marketing-cloud-rate-limits
rules:
- name: Salesforce Marketing Cloud API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: salesforce-marketing-cloud-jsonschema-spectral-rules
- name: Salesforce Marketing Cloud API Rules
  rule_count: 18
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 9
  slug: salesforce-marketing-cloud-spectral-rules
scopes:
- name: Salesforce Marketing Cloud Scopes
  scope_count: 42
  slug: salesforce-marketing-cloud-scopes
  summary_line: 42 scopes · clientCredentials
score:
  band: strong
  composite: 59.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 68.4
    developer_ergonomics: 52.2
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 59.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/salesforce-marketing-cloud/refs/heads/main/screenshots/salesforce-marketing-cloud-2026-06-20T193349.png
security:
- kind: authentication
  name: Salesforce Marketing Cloud Authentication
  slug: salesforce-marketing-cloud-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Salesforce Marketing Cloud Domain Security
  slug: salesforce-marketing-cloud-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: salesforce-marketing-cloud
tags:
- Automation
- Customer Journey
- Digital Marketing
- Email
- Marketing
- Personalization
use_cases:
- description: Automate multi-step welcome sequences across email and SMS to guide new customers through product adoption.
  name: Customer Onboarding Journeys
- description: Trigger personalized follow-up emails and push notifications when customers abandon shopping carts.
  name: Abandoned Cart Recovery
- description: Coordinate marketing messages across email, SMS, push, and advertising for unified campaign execution.
  name: Cross-Channel Campaign Orchestration
- description: Manage subscriber preferences, segment audiences, and automate re-engagement campaigns for inactive contacts.
  name: Subscriber Lifecycle Management
- description: React to customer behaviors in real time with triggered messages based on website visits, purchases, or app activity.
  name: Real-Time Event-Driven Marketing
website: https://developer.salesforce.com/docs/marketing/marketing-cloud/overview
---
