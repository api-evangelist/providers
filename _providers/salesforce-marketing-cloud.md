---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: templated
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Salesforce Marketing Cloud Agentic Access
  operation_count: 21
  slug: salesforce-marketing-cloud-agentic-access
  summary_line: 21 operations · 12 acting · 1 human-in-the-loop
api_count: 1
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
  slug: sms-mms-api
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
- baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com
  baseurl_source: declared
  description: Manage marketing assets including images, documents, content blocks, and templates. The Asset API provides CRUD operations for all content types stored in Content Builder.
  name: Salesforce Marketing Cloud Assets API
  phrasing_intents:
  - id: listAssets
    intent: List Content Builder assets
    question: What emails, templates and images are in my Content Builder library?
  - id: createAsset
    intent: Create a Content Builder asset
    question: How do I upload a new HTML email into Content Builder programmatically?
  - id: getAsset
    intent: Retrieve one asset by id
    question: How can I pull the full content and folder of one specific asset?
  - id: updateAsset
    intent: Update an existing asset
    question: How do I change the HTML of an email that's already in Content Builder?
  - id: deleteAsset
    intent: Delete an asset permanently
    question: How do I remove an old email template from Content Builder?
  - id: queryAssets
    intent: Search assets with advanced query logic
    question: Can I search assets with AND/OR conditions that the simple list filter can't express?
  - id: listCategories
    intent: List Content Builder folders
    question: What folders are my Content Builder assets organized into?
  phrasing_ops: 7
  slug: salesforce-marketing-cloud-assets-api
- baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com
  baseurl_source: declared
  description: Create, retrieve, update, and delete contacts in Marketing Cloud. Contacts represent individuals who interact with your marketing campaigns across channels.
  name: Salesforce Marketing Cloud Contacts API
  phrasing_intents:
  - id: createContacts
    intent: Create a contact
    question: How do I add a new subscriber to Marketing Cloud's contact model?
  - id: searchContacts
    intent: Search contacts by criteria
    question: How do I find a contact when I only know their email address?
  - id: getContact
    intent: Retrieve a contact by contact key
    question: What attribute values are stored for a specific contact key?
  - id: updateContact
    intent: Update a contact's attributes
    question: How do I change an existing contact's email address without touching their other data?
  - id: deleteContact
    intent: Delete a contact and its data
    question: How do I remove a person and their data from Marketing Cloud entirely?
  - id: listAttributeSets
    intent: List contact attribute sets
    question: What attribute sets define the structure of contact data in my account?
  phrasing_ops: 6
  slug: salesforce-marketing-cloud-contacts-api
- baseURL: https://YOUR_SUBDOMAIN.rest.marketingcloudapis.com
  baseurl_source: declared
  description: Create, manage, and automate customer journeys across multiple channels and touchpoints. Journeys define the automated workflows that guide customers through marketing interactions.
  name: Salesforce Marketing Cloud Journeys API
  phrasing_intents:
  - id: listJourneys
    intent: List journeys in Journey Builder
    question: Which journeys do I have in Marketing Cloud and what status is each one in?
  - id: createJourney
    intent: Create a new journey
    question: How do I build a new customer journey through the API instead of Journey Builder's canvas?
  - id: getJourney
    intent: Retrieve one journey's full definition
    question: How can I see the activities, goals and exit criteria configured in a specific journey?
  - id: updateJourney
    intent: Update an existing journey
    question: Can I change the activities of a journey that's still in draft?
  - id: deleteJourney
    intent: Delete a journey
    question: Why can't I delete a journey that is currently running?
  - id: publishJourney
    intent: Publish a journey so contacts can enter
    question: How do I activate a journey so contacts start entering it?
  - id: stopJourney
    intent: Stop a running journey
    question: How do I halt a published journey that's sending the wrong messages?
  - id: fireEntryEvent
    intent: Inject a contact into a journey
    question: How do I push a single contact into a journey from my own app?
  phrasing_ops: 8
  slug: salesforce-marketing-cloud-journeys-api
artifact_total: 174
asyncapis:
- description: ''
  name: Salesforce Marketing Cloud Webhooks
  slug: salesforce-marketing-cloud-webhooks
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
  name: Salesforce Marketing Cloud REST Assets API
  slug: open-salesforce-marketing-cloud-assets-api
- collection_type: open
  name: Salesforce Marketing Cloud REST Assets Contacts API
  slug: open-salesforce-marketing-cloud-contacts-api
- collection_type: open
  name: Salesforce Marketing Cloud REST Assets Journeys API
  slug: open-salesforce-marketing-cloud-journeys-api
- collection_type: open
  name: Salesforce Marketing Cloud REST API
  slug: open-salesforce-marketing-cloud
common:
- group: design
  href: https://artifacts.apis.io/salesforce-marketing-cloud/rules/salesforce-marketing-cloud-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/salesforce-marketing-cloud-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/salesforce-marketing-cloud/rules/salesforce-marketing-cloud-rules.yml
  title: ''
  type: Spectral
  url: rules/salesforce-marketing-cloud-rules.yml
- group: design
  href: https://artifacts.apis.io/salesforce-marketing-cloud/rules/salesforce-marketing-cloud-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/salesforce-marketing-cloud-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/salesforce-marketing-cloud/json-ld/salesforce-marketing-cloud-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/salesforce-marketing-cloud-context.jsonld
- group: design
  href: https://artifacts.apis.io/salesforce-marketing-cloud/vocabulary/salesforce-marketing-cloud-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/salesforce-marketing-cloud-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/salesforce-marketing-cloud/security/salesforce-marketing-cloud-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/salesforce-marketing-cloud-trust-center.yml
- group: other
  href: https://artifacts.apis.io/salesforce-marketing-cloud/hosts/salesforce-marketing-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/salesforce-marketing-cloud-hosts.yml
- group: build
  href: https://artifacts.apis.io/salesforce-marketing-cloud/integrations/salesforce-marketing-cloud-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/salesforce-marketing-cloud-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/salesforce-marketing-cloud/vendors/salesforce-marketing-cloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/salesforce-marketing-cloud-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.salesforce.com/media/
- group: other
  title: ''
  type: Leadership
  url: https://www.salesforce.com/company/leadership/
- group: commercial
  href: https://artifacts.apis.io/salesforce-marketing-cloud/finops/salesforce-marketing-cloud-finops.yml
  title: ''
  type: FinOps
  url: finops/salesforce-marketing-cloud-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.salesforce.com/
- group: other
  href: https://artifacts.apis.io/salesforce-marketing-cloud/capabilities/salesforce-marketing-cloud-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/salesforce-marketing-cloud-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/salesforce-marketingcloud/SFDC-MC-REST-Style-Guide/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/salesforce-marketingcloud/SFDC-MC-REST-Style-Guide/releases
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/salesforce-marketing-cloud/overview
- group: agent
  href: https://artifacts.apis.io/salesforce-marketing-cloud/agentic-access/salesforce-marketing-cloud-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/salesforce-marketing-cloud-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/salesforce-marketing-cloud/security/salesforce-marketing-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/salesforce-marketing-cloud-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/salesforce-marketing-cloud/authentication/salesforce-marketing-cloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/salesforce-marketing-cloud-authentication.yml
- group: auth
  href: https://artifacts.apis.io/salesforce-marketing-cloud/scopes/salesforce-marketing-cloud-scopes.yml
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
  url: https://help.salesforce.com/s/articleView?id=sf.mc_rn_release_notes.htm&type=5
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/rate-limiting.html
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/salesforce-marketingcloud/SFDC-MC-REST-Style-Guide
- group: build
  href: https://artifacts.apis.io/salesforce-marketing-cloud/packages/salesforce-marketing-cloud-packages.yml
  title: ''
  type: Packages
  url: packages/salesforce-marketing-cloud-packages.yml
- group: build
  href: https://artifacts.apis.io/salesforce-marketing-cloud/packages/salesforce-marketing-cloud-packages.yml
  title: ''
  type: SDKs
  url: packages/salesforce-marketing-cloud-packages.yml
- group: agent
  href: https://artifacts.apis.io/salesforce-marketing-cloud/well-known/salesforce-marketing-cloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/salesforce-marketing-cloud-well-known.yml
- group: agent
  href: https://artifacts.apis.io/salesforce-marketing-cloud/mcp/salesforce-marketing-cloud-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/salesforce-marketing-cloud-mcp.yml
- group: build
  href: https://artifacts.apis.io/salesforce-marketing-cloud/mcp/salesforce-marketing-cloud-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/salesforce-marketing-cloud-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/salesforce-marketing-cloud/llms/salesforce-marketing-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/salesforce-marketing-cloud-llms.txt
- group: design
  href: https://artifacts.apis.io/salesforce-marketing-cloud/conformance/salesforce-marketing-cloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/salesforce-marketing-cloud-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://compliance.salesforce.com/
- group: design
  href: https://artifacts.apis.io/salesforce-marketing-cloud/errors/salesforce-marketing-cloud-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/salesforce-marketing-cloud-problem-types.yml
- group: design
  href: https://artifacts.apis.io/salesforce-marketing-cloud/lifecycle/salesforce-marketing-cloud-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/salesforce-marketing-cloud-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/api_rest_eol.htm
- group: auth
  href: https://artifacts.apis.io/salesforce-marketing-cloud/security/salesforce-marketing-cloud-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/salesforce-marketing-cloud-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.salesforce.com/company/disclosure/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.salesforce.com/
- group: design
  href: https://artifacts.apis.io/salesforce-marketing-cloud/conventions/salesforce-marketing-cloud-conventions.yml
  title: ''
  type: Conventions
  url: conventions/salesforce-marketing-cloud-conventions.yml
- group: design
  href: https://artifacts.apis.io/salesforce-marketing-cloud/conventions/salesforce-marketing-cloud-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/salesforce-marketing-cloud-conventions.yml
- group: operate
  href: https://artifacts.apis.io/salesforce-marketing-cloud/changelog/salesforce-marketing-cloud-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/salesforce-marketing-cloud-changelog.yml
- group: design
  href: https://artifacts.apis.io/salesforce-marketing-cloud/components/salesforce-marketing-cloud-components.yml
  title: ''
  type: Components
  url: components/salesforce-marketing-cloud-components.yml
- group: design
  href: https://artifacts.apis.io/salesforce-marketing-cloud/data-model/salesforce-marketing-cloud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/salesforce-marketing-cloud-data-model.yml
- group: design
  href: https://artifacts.apis.io/salesforce-marketing-cloud/asyncapi/salesforce-marketing-cloud-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/salesforce-marketing-cloud-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/salesforce-marketing-cloud/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/salesforce-marketing-cloud/plans/salesforce-marketing-cloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/salesforce-marketing-cloud-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/salesforce-marketing-cloud/rate-limits/salesforce-marketing-cloud-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/salesforce-marketing-cloud-rate-limits.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/salesforce-marketingcloud
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.salesforce.com/company/legal/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://www.salesforce.com/form/signup/freetrial-marketing-cloud/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/get-started-index.html
created: '2024-01-15'
description: 'Salesforce Marketing Cloud Engagement is an enterprise digital marketing platform for customer journeys, email marketing, mobile messaging (SMS/MMS and push), advertising, content management and marketing data. Its API surface is tenant-scoped: every REST call goes to https://{subdomain}.rest.marketingcloudapis.com and every SOAP call to https://{subdomain}.soap.marketingcloudapis.com, with OAuth 2.0 tokens issued per tenant from https://{subdomain}.auth.marketingcloudapis.com/v2/token and scopes granted to an Installed Package rather than requested at authorization time. Product areas are versioned independently at v1 behind route prefixes (/asset, /contacts, /interaction, /data, /messaging, /push, /sms, /automation, /hub, /platform). Salesforce also operates a first-party hosted MCP server for Marketing Cloud Engagement, generally available since June 2026, exposing 142 tools across eleven product areas, and an outbound webhook product, the Event Notification Service, with
  HMAC-SHA256 signed callbacks.'
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
- has_sources: true
  method: derived
  name: Salesforce Marketing Cloud Finops
  primary_unit: org
  service_category: ''
  slug: salesforce-marketing-cloud-finops
  template: false
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
mcp_servers:
- description: Remote MCP server at mai-mce-mcp-cdp1.sfdc-yfeipo.svc.sfdcfc.net over HTTP requiring OAuth; 142 tools listed.
  name: MCP Server for Marketing Cloud Engagement
  slug: mcp-server-for-marketing-cloud-engagement
modified: '2026-08-13'
name: Salesforce Marketing Cloud
nav: Providers
network: true
overview: 'Salesforce Marketing Cloud publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Assets API, Contacts API, Journeys API, and 14 more. Tagged areas include Automation, Content Management, Customer Journey, Digital Marketing, and Email.


  The Salesforce Marketing Cloud catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Salesforce Marketing Cloud''s developer surface includes authentication, engineering blog, documentation, API reference, support, pricing, changelog, and 55 more developer resources.'
plans:
- name: Salesforce Marketing Cloud Plans Pricing
  plan_count: 11
  slug: salesforce-marketing-cloud-plans-pricing
- name: Salesforce Marketing Cloud Price Estimates
  plan_count: 0
  slug: salesforce-marketing-cloud-price-estimates
random_paper: 10
rate_limits:
- limit_count: 3
  name: Salesforce Marketing Cloud Rate Limits
  slug: salesforce-marketing-cloud-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Salesforce Marketing Cloud — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: salesforce-marketing-cloud-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: Salesforce Marketing Cloud API Rules
  rule_count: 20
  severity_counts:
    error: 18
    hint: 0
    info: 1
    warn: 1
  slug: salesforce-marketing-cloud-rules
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Salesforce Marketing Cloud API Rules
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
  band: exemplar
  composite: 80.5
  coverage:
    artifact_dirs: 40
    catalog_earned: 85.0
    catalog_earned_first_party: 24.0
    catalog_gap: 30.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 100.0
    contract_governance: 45.5
    contract_quality: 74.3
    developer_ergonomics: 76.8
    discoverability: 73.3
    operational_transparency: 84.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 80.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 44.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/salesforce-marketing-cloud/salesforce-marketing-cloud-2026-06-20T193349.png
security:
- kind: authentication
  name: Salesforce Marketing Cloud Authentication
  slug: salesforce-marketing-cloud-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Salesforce Marketing Cloud Domain Security
  slug: salesforce-marketing-cloud-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Salesforce Marketing Cloud Vulnerability Disclosure
  slug: salesforce-marketing-cloud-vulnerability-disclosure
  summary_line: Hackerone · security.txt
- kind: trust-center
  name: Salesforce Marketing Cloud Trust Center
  slug: salesforce-marketing-cloud-trust-center
  summary_line: SOC 1, SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, CSA STAR, GDPR
skill_count: 4
skills:
- name: connect-mcp-server
  slug: salesforce-marketing-cloud-connect-mcp-server
- name: create-and-publish-journey
  slug: salesforce-marketing-cloud-create-and-publish-journey
- name: enter-contact-into-journey
  slug: salesforce-marketing-cloud-enter-contact-into-journey
- name: manage-content-assets
  slug: salesforce-marketing-cloud-manage-content-assets
slug: salesforce-marketing-cloud
tags:
- Automation
- Content Management
- Customer Journey
- Digital Marketing
- Email
- Marketing
- Marketing Automation
- MCP
- Mobile Messaging
- Personalization
- SMS
- Webhook
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
website: https://www.salesforce.com/
---
