---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
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
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 53
  human_in_the_loop: 1
  name: Adobe Experience Cloud Agentic Access
  operation_count: 110
  slug: adobe-experience-cloud-agentic-access
  summary_line: 110 operations · 53 acting · 1 human-in-the-loop
api_count: 36
apis:
- description: Adobe I/O Events enables developers to receive near-real-time notifications from Adobe services via webhooks and journal polling. Events are emitted when significant changes occur across Adobe Experie
  name: Adobe I/O Events
  slug: io-events
- description: Operations for managing Target activities (A/B, XT, MVT, AP)
  name: Adobe Experience Cloud Activities API
  slug: adobe-experience-cloud-activities-api
- description: Operations for managing Target audiences
  name: Adobe Experience Cloud Audiences API
  slug: adobe-experience-cloud-audiences-api
- description: Operations for batch data ingestion
  name: Adobe Experience Cloud Batches API
  slug: adobe-experience-cloud-batches-api
- description: Operations for managing calculated metrics
  name: Adobe Experience Cloud Calculated Metrics API
  slug: adobe-experience-cloud-calculated-metrics-api
- description: The Campaign API from Adobe Experience Cloud — 3 operation(s) for campaign.
  name: Adobe Experience Cloud Campaign API
  slug: adobe-experience-cloud-campaign-api
- description: Operations for managing marketing campaigns
  name: Adobe Experience Cloud Campaigns API
  slug: adobe-experience-cloud-campaigns-api
- description: Operations for managing XDM classes
  name: Adobe Experience Cloud Classes API
  slug: adobe-experience-cloud-classes-api
- description: Operations for managing offer collections
  name: Adobe Experience Cloud Collections API
  slug: adobe-experience-cloud-collections-api
- description: Operations for managing email and landing page content
  name: Adobe Experience Cloud Content API
  slug: adobe-experience-cloud-content-api
- description: Operations for managing reusable content templates
  name: Adobe Experience Cloud Content Templates API
  slug: adobe-experience-cloud-content-templates-api
- description: Operations for managing datasets in the Data Lake
  name: Adobe Experience Cloud Datasets API
  slug: adobe-experience-cloud-datasets-api
- description: Operations for managing saved date ranges
  name: Adobe Experience Cloud Date Ranges API
  slug: adobe-experience-cloud-date-ranges-api
- description: Operations for managing offer eligibility rules
  name: Adobe Experience Cloud Decision Rules API
  slug: adobe-experience-cloud-decision-rules-api
- description: Operations for real-time content delivery
  name: Adobe Experience Cloud Delivery API
  slug: adobe-experience-cloud-delivery-api
- description: Operations for retrieving dimension metadata
  name: Adobe Experience Cloud Dimensions API
  slug: adobe-experience-cloud-dimensions-api
- description: Operations for managing environments
  name: Adobe Experience Cloud Environments API
  slug: adobe-experience-cloud-environments-api
- description: Operations for identity namespace management
  name: Adobe Experience Cloud Identities API
  slug: adobe-experience-cloud-identities-api
- description: Operations for managing customer journeys
  name: Adobe Experience Cloud Journeys API
  slug: adobe-experience-cloud-journeys-api
- description: Operations for managing channel messages
  name: Adobe Experience Cloud Messages API
  slug: adobe-experience-cloud-messages-api
- description: Operations for retrieving resource metadata
  name: Adobe Experience Cloud Metadata API
  slug: adobe-experience-cloud-metadata-api
- description: Operations for retrieving metric metadata
  name: Adobe Experience Cloud Metrics API
  slug: adobe-experience-cloud-metrics-api
- description: Operations for offer decisioning
  name: Adobe Experience Cloud Offers API
  slug: adobe-experience-cloud-offers-api
- description: Operations for managing offer placements
  name: Adobe Experience Cloud Placements API
  slug: adobe-experience-cloud-placements-api
- description: Operations for managing subscriber profiles
  name: Adobe Experience Cloud Profiles API
  slug: adobe-experience-cloud-profiles-api
- description: Operations for managing Analysis Workspace projects
  name: Adobe Experience Cloud Projects API
  slug: adobe-experience-cloud-projects-api
- description: Operations for managing enterprise properties
  name: Adobe Experience Cloud Properties API
  slug: adobe-experience-cloud-properties-api
- description: Operations for the Query Service
  name: Adobe Experience Cloud Queries API
  slug: adobe-experience-cloud-queries-api
- description: Operations for managing report suites
  name: Adobe Experience Cloud Report Suites API
  slug: adobe-experience-cloud-report-suites-api
- description: Operations for retrieving analytics report data
  name: Adobe Experience Cloud Reports API
  slug: adobe-experience-cloud-reports-api
- description: Operations for managing platform sandboxes
  name: Adobe Experience Cloud Sandboxes API
  slug: adobe-experience-cloud-sandboxes-api
- description: Operations for managing XDM schemas via the Schema Registry
  name: Adobe Experience Cloud Schemas API
  slug: adobe-experience-cloud-schemas-api
- description: Operations for managing analytics segments
  name: Adobe Experience Cloud Segments API
  slug: adobe-experience-cloud-segments-api
- description: Operations for sending real-time transactional messages
  name: Adobe Experience Cloud Transactional Messages API
  slug: adobe-experience-cloud-transactional-messages-api
- description: Operations for managing analytics users
  name: Adobe Experience Cloud Users API
  slug: adobe-experience-cloud-users-api
- description: Operations for managing automated workflows
  name: Adobe Experience Cloud Workflows API
  slug: adobe-experience-cloud-workflows-api
arazzos:
- description: List report suites, fetch one's configuration, then run a report against it.
  name: Adobe Analytics Report Suite Discovery
  slug: adobe-experience-cloud-analytics-report-suite-discovery-workflow
- description: Create an Analytics segment, confirm it, then run a report filtered by that segment.
  name: Adobe Analytics Segment-Filtered Report
  slug: adobe-experience-cloud-analytics-segment-report-workflow
- description: Create a subscriber profile, create a subscription service, then subscribe the profile to it.
  name: Adobe Campaign Profile Subscription
  slug: adobe-experience-cloud-campaign-profile-subscription-workflow
- description: Trigger a transactional message, then poll its delivery status until it leaves the pending state.
  name: Adobe Campaign Transactional Message
  slug: adobe-experience-cloud-campaign-transactional-message-workflow
- description: List Campaign workflows, fetch one by key, then start it with a workflow command.
  name: Adobe Campaign Workflow Execution
  slug: adobe-experience-cloud-campaign-workflow-execution-workflow
- description: Create a PQL segment definition, read it back, then confirm it appears in the segment list.
  name: Adobe Experience Platform Audience Segment Definition
  slug: adobe-experience-cloud-experience-platform-audience-segment-workflow
- description: Create a dataset, open a batch against it, then poll the batch until it finishes loading.
  name: Adobe Experience Platform Batch Ingestion
  slug: adobe-experience-cloud-experience-platform-batch-ingestion-workflow
- description: List identity namespaces, create a custom namespace, then look up a profile entity by identity.
  name: Adobe Experience Platform Identity and Profile Lookup
  slug: adobe-experience-cloud-experience-platform-identity-profile-lookup-workflow
- description: Submit a SQL query to Query Service, poll until it finishes, then list recent queries.
  name: Adobe Experience Platform Query Service Execution
  slug: adobe-experience-cloud-experience-platform-query-service-workflow
- description: Create an XDM schema, confirm it, then create and verify a dataset bound to it.
  name: Adobe Experience Platform Schema and Dataset Setup
  slug: adobe-experience-cloud-experience-platform-schema-dataset-setup-workflow
- description: Create a marketing campaign, confirm its configuration, then list campaigns to verify it.
  name: Adobe Journey Optimizer Campaign Launch
  slug: adobe-experience-cloud-journey-campaign-launch-workflow
- description: Create a draft journey, confirm it, publish it live, and optionally stop it again.
  name: Adobe Journey Optimizer Journey Create and Publish
  slug: adobe-experience-cloud-journey-create-publish-workflow
- description: Create a channel message, read it back, then list messages to confirm it.
  name: Adobe Journey Optimizer Message Authoring
  slug: adobe-experience-cloud-journey-message-authoring-workflow
- description: Create a personalized offer, read it back, then update its priority and content.
  name: Adobe Journey Optimizer Offer Decisioning
  slug: adobe-experience-cloud-journey-offer-decisioning-workflow
- description: Create an A/B activity, confirm its configuration, then activate it.
  name: Adobe Target AB Activity Lifecycle
  slug: adobe-experience-cloud-target-ab-activity-lifecycle-workflow
- description: Create a Target audience, create an offer, then assemble an A/B activity from them.
  name: Adobe Target Audience, Offer, and Activity Assembly
  slug: adobe-experience-cloud-target-audience-offer-activity-workflow
- description: List available offers, then fetch personalized content for a visitor session.
  name: Adobe Target Deliver Personalization
  slug: adobe-experience-cloud-target-deliver-personalization-workflow
artifact_total: 365
asyncapis:
- description: Adobe I/O Events enables developers to receive near-real-time notifications from Adobe services via webhooks and journal polling. Events are emitted when significant changes occur across Adobe Experie
  name: Adobe I/O Events
  slug: adobe-io-events-asyncapi
collections:
- collection_type: postman
  name: Adobe Experience Cloud Adobe Analytics 2.0 API
  slug: postman-adobe-analytics-api
- collection_type: postman
  name: Adobe Experience Cloud Adobe Campaign API
  slug: postman-adobe-campaign-api
- collection_type: postman
  name: Adobe Experience Cloud Adobe Experience Platform API
  slug: postman-adobe-experience-platform-api
- collection_type: postman
  name: Adobe Experience Cloud Adobe Journey Optimizer API
  slug: postman-adobe-journey-optimizer-api
- collection_type: postman
  name: Adobe Experience Cloud Adobe Target API
  slug: postman-adobe-target-api
- collection_type: open
  name: Adobe Experience Cloud Adobe Analytics 2.0 API
  slug: open-adobe-analytics-api
- collection_type: open
  name: Adobe Experience Cloud Adobe Campaign API
  slug: open-adobe-campaign-api
- collection_type: open
  name: Adobe Experience Cloud Adobe Experience Platform API
  slug: open-adobe-experience-platform-api
- collection_type: open
  name: Adobe Experience Cloud Adobe Journey Optimizer API
  slug: open-adobe-journey-optimizer-api
- collection_type: open
  name: Adobe Experience Cloud Adobe Target API
  slug: open-adobe-target-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adobe-experience-cloud-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/adobe-experience-cloud-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adobe-experience-cloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adobe-experience-cloud-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/adobe-experience-cloud/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-experience-cloud-analytics-report-suite-discovery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-experience-cloud-analytics-segment-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-experience-cloud-campaign-profile-subscription-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-experience-cloud-campaign-transactional-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-experience-cloud-campaign-workflow-execution-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-experience-cloud-experience-platform-audience-segment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-experience-cloud-experience-platform-batch-ingestion-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-experience-cloud-experience-platform-identity-profile-lookup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-experience-cloud-experience-platform-query-service-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-experience-cloud-experience-platform-schema-dataset-setup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-experience-cloud-journey-campaign-launch-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-experience-cloud-journey-create-publish-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-experience-cloud-journey-message-authoring-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-experience-cloud-journey-offer-decisioning-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-experience-cloud-target-ab-activity-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-experience-cloud-target-audience-offer-activity-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-experience-cloud-target-deliver-personalization-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/adobe-experience-cloud
- group: start
  title: ''
  type: Portal
  url: https://developer.adobe.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.adobe.com/developer-console/docs/guides/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.adobe.com/apis/
- group: company
  title: ''
  type: Blog
  url: https://blog.developer.adobe.com/
- group: operate
  title: ''
  type: Support
  url: https://experienceleague.adobe.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adobe.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adobe.com/privacy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adobe.com/
- group: start
  title: ''
  type: Console
  url: https://developer.adobe.com/console/
- group: start
  title: ''
  type: Signup
  url: https://developer.adobe.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.adobe.com/developer-console/docs/guides/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adobe
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AdobeDeveloperTV
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.adobe.com/events/docs/whats_new/
- group: design
  title: ''
  type: SpectralRules
  url: rules/adobe-experience-cloud-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/adobe-experience-cloud-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/adobe-experience-cloud-analytics-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/adobe-experience-cloud-campaign-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/adobe-experience-cloud-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/adobe-experience-cloud-experience-platform-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/adobe-experience-cloud-io-events-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/adobe-experience-cloud-journey-optimizer-api-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/adobe-experience-cloud-target-api-context.jsonld
created: '2025-01-01'
description: Adobe Experience Cloud is an integrated suite of applications and services for digital marketing, analytics, advertising, and commerce. It provides tools for content management, personalization, customer journey orchestration, audience segmentation, real-time customer data platforms, offer decisioning, and cross-channel campaign execution, enabling organizations to deliver personalized customer experiences at scale.
examples:
- key_count: 8
  name: Adobe Experience Cloud Campaign
  slug: adobe-experience-cloud-campaign
- key_count: 8
  name: Adobe Experience Cloud Event
  slug: adobe-experience-cloud-event
- key_count: 8
  name: Adobe Experience Cloud Journey
  slug: adobe-experience-cloud-journey
- key_count: 8
  name: Adobe Experience Cloud Offer
  slug: adobe-experience-cloud-offer
- key_count: 8
  name: Adobe Experience Cloud Profile
  slug: adobe-experience-cloud-profile
- key_count: 8
  name: Adobe Experience Cloud Segment
  slug: adobe-experience-cloud-segment
- key_count: 7
  name: Analytics Api Calculated Metric Example
  slug: analytics-api-calculated-metric-example
- key_count: 3
  name: Analytics Api Calculated Metric List Example
  slug: analytics-api-calculated-metric-list-example
- key_count: 2
  name: Analytics Api Date Range List Example
  slug: analytics-api-date-range-list-example
- key_count: 5
  name: Analytics Api Dimension Example
  slug: analytics-api-dimension-example
- key_count: 5
  name: Analytics Api Metric Example
  slug: analytics-api-metric-example
- key_count: 5
  name: Analytics Api Project Example
  slug: analytics-api-project-example
- key_count: 2
  name: Analytics Api Project List Example
  slug: analytics-api-project-list-example
- key_count: 5
  name: Analytics Api Report Request Example
  slug: analytics-api-report-request-example
- key_count: 6
  name: Analytics Api Report Response Example
  slug: analytics-api-report-response-example
- key_count: 5
  name: Analytics Api Report Suite Example
  slug: analytics-api-report-suite-example
- key_count: 3
  name: Analytics Api Report Suite List Example
  slug: analytics-api-report-suite-list-example
- key_count: 7
  name: Analytics Api Segment Example
  slug: analytics-api-segment-example
- key_count: 3
  name: Analytics Api Segment List Example
  slug: analytics-api-segment-list-example
- key_count: 6
  name: Analytics Api User Example
  slug: analytics-api-user-example
- key_count: 3
  name: Analytics Api User List Example
  slug: analytics-api-user-list-example
- key_count: 6
  name: Campaign Api Email Example
  slug: campaign-api-email-example
- key_count: 1
  name: Campaign Api Email List Example
  slug: campaign-api-email-list-example
- key_count: 8
  name: Campaign Api Profile Example
  slug: campaign-api-profile-example
- key_count: 5
  name: Campaign Api Profile Input Example
  slug: campaign-api-profile-input-example
- key_count: 2
  name: Campaign Api Profile List Example
  slug: campaign-api-profile-list-example
- key_count: 5
  name: Campaign Api Service Example
  slug: campaign-api-service-example
- key_count: 3
  name: Campaign Api Service Input Example
  slug: campaign-api-service-input-example
- key_count: 1
  name: Campaign Api Service List Example
  slug: campaign-api-service-list-example
- key_count: 2
  name: Campaign Api Transactional Message Request Example
  slug: campaign-api-transactional-message-request-example
- key_count: 4
  name: Campaign Api Transactional Message Response Example
  slug: campaign-api-transactional-message-response-example
- key_count: 5
  name: Campaign Api Workflow Example
  slug: campaign-api-workflow-example
- key_count: 1
  name: Campaign Api Workflow List Example
  slug: campaign-api-workflow-list-example
- key_count: 4
  name: Experience Platform Api Batch Example
  slug: experience-platform-api-batch-example
- key_count: 1
  name: Experience Platform Api Class List Example
  slug: experience-platform-api-class-list-example
- key_count: 6
  name: Experience Platform Api Dataset Example
  slug: experience-platform-api-dataset-example
- key_count: 3
  name: Experience Platform Api Dataset Input Example
  slug: experience-platform-api-dataset-input-example
- key_count: 6
  name: Experience Platform Api Identity Namespace Example
  slug: experience-platform-api-identity-namespace-example
- key_count: 4
  name: Experience Platform Api Identity Namespace Input Example
  slug: experience-platform-api-identity-namespace-input-example
- key_count: 2
  name: Experience Platform Api Profile Entity Example
  slug: experience-platform-api-profile-entity-example
- key_count: 8
  name: Experience Platform Api Query Example
  slug: experience-platform-api-query-example
- key_count: 2
  name: Experience Platform Api Query List Example
  slug: experience-platform-api-query-list-example
- key_count: 5
  name: Experience Platform Api Sandbox Example
  slug: experience-platform-api-sandbox-example
- key_count: 1
  name: Experience Platform Api Sandbox List Example
  slug: experience-platform-api-sandbox-list-example
- key_count: 5
  name: Experience Platform Api Schema Example
  slug: experience-platform-api-schema-example
- key_count: 4
  name: Experience Platform Api Schema Input Example
  slug: experience-platform-api-schema-input-example
- key_count: 2
  name: Experience Platform Api Schema List Example
  slug: experience-platform-api-schema-list-example
- key_count: 6
  name: Experience Platform Api Segment Definition Example
  slug: experience-platform-api-segment-definition-example
- key_count: 5
  name: Experience Platform Api Segment Definition Input Example
  slug: experience-platform-api-segment-definition-input-example
- key_count: 2
  name: Experience Platform Api Segment Definition List Example
  slug: experience-platform-api-segment-definition-list-example
- key_count: 6
  name: Journey Optimizer Api Campaign Example
  slug: journey-optimizer-api-campaign-example
- key_count: 5
  name: Journey Optimizer Api Campaign Input Example
  slug: journey-optimizer-api-campaign-input-example
- key_count: 2
  name: Journey Optimizer Api Campaign List Example
  slug: journey-optimizer-api-campaign-list-example
- key_count: 3
  name: Journey Optimizer Api Collection Example
  slug: journey-optimizer-api-collection-example
- key_count: 2
  name: Journey Optimizer Api Collection Input Example
  slug: journey-optimizer-api-collection-input-example
- key_count: 1
  name: Journey Optimizer Api Collection List Example
  slug: journey-optimizer-api-collection-list-example
- key_count: 5
  name: Journey Optimizer Api Content Template Example
  slug: journey-optimizer-api-content-template-example
- key_count: 3
  name: Journey Optimizer Api Content Template Input Example
  slug: journey-optimizer-api-content-template-input-example
- key_count: 2
  name: Journey Optimizer Api Content Template List Example
  slug: journey-optimizer-api-content-template-list-example
- key_count: 4
  name: Journey Optimizer Api Decision Rule Example
  slug: journey-optimizer-api-decision-rule-example
- key_count: 3
  name: Journey Optimizer Api Decision Rule Input Example
  slug: journey-optimizer-api-decision-rule-input-example
- key_count: 1
  name: Journey Optimizer Api Decision Rule List Example
  slug: journey-optimizer-api-decision-rule-list-example
- key_count: 7
  name: Journey Optimizer Api Journey Example
  slug: journey-optimizer-api-journey-example
- key_count: 4
  name: Journey Optimizer Api Journey Input Example
  slug: journey-optimizer-api-journey-input-example
- key_count: 2
  name: Journey Optimizer Api Journey List Example
  slug: journey-optimizer-api-journey-list-example
- key_count: 5
  name: Journey Optimizer Api Message Example
  slug: journey-optimizer-api-message-example
- key_count: 3
  name: Journey Optimizer Api Message Input Example
  slug: journey-optimizer-api-message-input-example
- key_count: 2
  name: Journey Optimizer Api Message List Example
  slug: journey-optimizer-api-message-list-example
- key_count: 7
  name: Journey Optimizer Api Offer Example
  slug: journey-optimizer-api-offer-example
- key_count: 6
  name: Journey Optimizer Api Offer Input Example
  slug: journey-optimizer-api-offer-input-example
- key_count: 2
  name: Journey Optimizer Api Offer List Example
  slug: journey-optimizer-api-offer-list-example
- key_count: 4
  name: Journey Optimizer Api Placement Example
  slug: journey-optimizer-api-placement-example
- key_count: 3
  name: Journey Optimizer Api Placement Input Example
  slug: journey-optimizer-api-placement-input-example
- key_count: 1
  name: Journey Optimizer Api Placement List Example
  slug: journey-optimizer-api-placement-list-example
- key_count: 8
  name: Target Api Activity Example
  slug: target-api-activity-example
- key_count: 5
  name: Target Api Activity Input Example
  slug: target-api-activity-input-example
- key_count: 4
  name: Target Api Activity List Example
  slug: target-api-activity-list-example
- key_count: 4
  name: Target Api Audience Example
  slug: target-api-audience-example
- key_count: 3
  name: Target Api Audience Input Example
  slug: target-api-audience-input-example
- key_count: 4
  name: Target Api Audience List Example
  slug: target-api-audience-list-example
- key_count: 3
  name: Target Api Delivery Request Example
  slug: target-api-delivery-request-example
- key_count: 3
  name: Target Api Delivery Response Example
  slug: target-api-delivery-response-example
- key_count: 1
  name: Target Api Environment List Example
  slug: target-api-environment-list-example
- key_count: 5
  name: Target Api Offer Example
  slug: target-api-offer-example
- key_count: 3
  name: Target Api Offer Input Example
  slug: target-api-offer-input-example
- key_count: 4
  name: Target Api Offer List Example
  slug: target-api-offer-list-example
- key_count: 2
  name: Target Api Property List Example
  slug: target-api-property-list-example
features:
- description: Build and query unified customer profiles from multiple data sources using the Experience Platform APIs.
  name: Real-Time Customer Profiles
- description: Retrieve dimensional reports, calculated metrics, and segment data from Adobe Analytics via REST API.
  name: Analytics Reporting
- description: Create, manage, and retrieve results for A/B tests and automated personalization activities via Adobe Target API.
  name: A/B and Multivariate Testing
- description: Orchestrate email, SMS, push, and in-app campaigns programmatically using Adobe Campaign and Journey Optimizer APIs.
  name: Multi-Channel Campaign Execution
- description: Subscribe to near-real-time events from all Adobe Experience Cloud products via Adobe I/O Events.
  name: Webhook Event Streaming
- description: Manage offers, placements, and decisioning rules for personalized content delivery using Journey Optimizer APIs.
  name: Offer Decisioning
- description: Ingest batch and streaming data and register schemas using Experience Platform APIs.
  name: Data Ingestion and Schema Registry
- description: Resolve customer identities across devices and channels using Experience Platform Identity Service API.
  name: Identity Resolution
- description: Create and evaluate audience segments using Experience Platform Segmentation Service API.
  name: Audience Segmentation
- description: Secure all APIs using OAuth 2.0 server-to-server credentials via Adobe Developer Console.
  name: OAuth 2.0 and JWT Authentication
finops:
- name: Adobe Experience Cloud Finops
  service_category: Marketing + Analytics + DXP SaaS
  slug: adobe-experience-cloud-finops
image: /assets/icons/adobe-experience-cloud.png
integrations:
- description: Sync customer data and campaign results between Adobe Experience Cloud and Salesforce CRM.
  name: Salesforce
- description: Ingest data from Azure Data Lake and Blob Storage into Adobe Experience Platform.
  name: Microsoft Azure
- description: Connect Google BigQuery datasets to Adobe Experience Platform for data ingestion and activation.
  name: Google BigQuery
- description: Integrate Workfront project management with Adobe Experience Cloud for content workflow automation.
  name: Workfront
- description: Sync lead data and campaign activities between Marketo Engage and Adobe Experience Cloud.
  name: Marketo Engage
- description: Connect ServiceNow customer data with Adobe Experience Cloud for unified customer service experiences.
  name: ServiceNow
- description: Connect Snowflake data warehouse to Experience Platform for federated audience composition.
  name: Snowflake
json_schemas:
- name: Adobe Experience Cloud Campaign
  property_count: 11
  slug: adobe-experience-cloud-campaign
- name: Adobe Experience Cloud Event
  property_count: 9
  slug: adobe-experience-cloud-event
- name: Adobe Experience Cloud Journey
  property_count: 11
  slug: adobe-experience-cloud-journey
- name: Adobe Experience Cloud Offer
  property_count: 14
  slug: adobe-experience-cloud-offer
- name: Adobe Experience Cloud Profile
  property_count: 10
  slug: adobe-experience-cloud-profile
- name: Adobe Experience Cloud Segment
  property_count: 14
  slug: adobe-experience-cloud-segment
- name: CalculatedMetricList
  property_count: 3
  slug: analytics-api-calculated-metric-list
- name: CalculatedMetric
  property_count: 7
  slug: analytics-api-calculated-metric
- name: DateRangeList
  property_count: 2
  slug: analytics-api-date-range-list
- name: Dimension
  property_count: 5
  slug: analytics-api-dimension
- name: Metric
  property_count: 5
  slug: analytics-api-metric
- name: ProjectList
  property_count: 2
  slug: analytics-api-project-list
- name: Project
  property_count: 5
  slug: analytics-api-project
- name: ReportRequest
  property_count: 5
  slug: analytics-api-report-request
- name: ReportResponse
  property_count: 6
  slug: analytics-api-report-response
- name: ReportSuiteList
  property_count: 3
  slug: analytics-api-report-suite-list
- name: ReportSuite
  property_count: 5
  slug: analytics-api-report-suite
- name: SegmentList
  property_count: 3
  slug: analytics-api-segment-list
- name: Segment
  property_count: 7
  slug: analytics-api-segment
- name: UserList
  property_count: 3
  slug: analytics-api-user-list
- name: User
  property_count: 6
  slug: analytics-api-user
- name: EmailList
  property_count: 1
  slug: campaign-api-email-list
- name: Email
  property_count: 6
  slug: campaign-api-email
- name: ProfileInput
  property_count: 5
  slug: campaign-api-profile-input
- name: ProfileList
  property_count: 2
  slug: campaign-api-profile-list
- name: Profile
  property_count: 8
  slug: campaign-api-profile
- name: ServiceInput
  property_count: 3
  slug: campaign-api-service-input
- name: ServiceList
  property_count: 1
  slug: campaign-api-service-list
- name: Service
  property_count: 5
  slug: campaign-api-service
- name: TransactionalMessageRequest
  property_count: 2
  slug: campaign-api-transactional-message-request
- name: TransactionalMessageResponse
  property_count: 4
  slug: campaign-api-transactional-message-response
- name: WorkflowList
  property_count: 1
  slug: campaign-api-workflow-list
- name: Workflow
  property_count: 5
  slug: campaign-api-workflow
- name: Batch
  property_count: 4
  slug: experience-platform-api-batch
- name: ClassList
  property_count: 1
  slug: experience-platform-api-class-list
- name: DatasetInput
  property_count: 3
  slug: experience-platform-api-dataset-input
- name: Dataset
  property_count: 6
  slug: experience-platform-api-dataset
- name: IdentityNamespaceInput
  property_count: 4
  slug: experience-platform-api-identity-namespace-input
- name: IdentityNamespace
  property_count: 6
  slug: experience-platform-api-identity-namespace
- name: ProfileEntity
  property_count: 2
  slug: experience-platform-api-profile-entity
- name: QueryList
  property_count: 2
  slug: experience-platform-api-query-list
- name: Query
  property_count: 8
  slug: experience-platform-api-query
- name: SandboxList
  property_count: 1
  slug: experience-platform-api-sandbox-list
- name: Sandbox
  property_count: 5
  slug: experience-platform-api-sandbox
- name: SchemaInput
  property_count: 4
  slug: experience-platform-api-schema-input
- name: SchemaList
  property_count: 2
  slug: experience-platform-api-schema-list
- name: Schema
  property_count: 5
  slug: experience-platform-api-schema
- name: SegmentDefinitionInput
  property_count: 5
  slug: experience-platform-api-segment-definition-input
- name: SegmentDefinitionList
  property_count: 2
  slug: experience-platform-api-segment-definition-list
- name: SegmentDefinition
  property_count: 6
  slug: experience-platform-api-segment-definition
- name: CampaignInput
  property_count: 5
  slug: journey-optimizer-api-campaign-input
- name: CampaignList
  property_count: 2
  slug: journey-optimizer-api-campaign-list
- name: Campaign
  property_count: 6
  slug: journey-optimizer-api-campaign
- name: CollectionInput
  property_count: 2
  slug: journey-optimizer-api-collection-input
- name: CollectionList
  property_count: 1
  slug: journey-optimizer-api-collection-list
- name: Collection
  property_count: 3
  slug: journey-optimizer-api-collection
- name: ContentTemplateInput
  property_count: 3
  slug: journey-optimizer-api-content-template-input
- name: ContentTemplateList
  property_count: 2
  slug: journey-optimizer-api-content-template-list
- name: ContentTemplate
  property_count: 5
  slug: journey-optimizer-api-content-template
- name: DecisionRuleInput
  property_count: 3
  slug: journey-optimizer-api-decision-rule-input
- name: DecisionRuleList
  property_count: 1
  slug: journey-optimizer-api-decision-rule-list
- name: DecisionRule
  property_count: 4
  slug: journey-optimizer-api-decision-rule
- name: JourneyInput
  property_count: 4
  slug: journey-optimizer-api-journey-input
- name: JourneyList
  property_count: 2
  slug: journey-optimizer-api-journey-list
- name: Journey
  property_count: 7
  slug: journey-optimizer-api-journey
- name: MessageInput
  property_count: 3
  slug: journey-optimizer-api-message-input
- name: MessageList
  property_count: 2
  slug: journey-optimizer-api-message-list
- name: Message
  property_count: 5
  slug: journey-optimizer-api-message
- name: OfferInput
  property_count: 6
  slug: journey-optimizer-api-offer-input
- name: OfferList
  property_count: 2
  slug: journey-optimizer-api-offer-list
- name: Offer
  property_count: 7
  slug: journey-optimizer-api-offer
- name: PlacementInput
  property_count: 3
  slug: journey-optimizer-api-placement-input
- name: PlacementList
  property_count: 1
  slug: journey-optimizer-api-placement-list
- name: Placement
  property_count: 4
  slug: journey-optimizer-api-placement
- name: ActivityInput
  property_count: 5
  slug: target-api-activity-input
- name: ActivityList
  property_count: 4
  slug: target-api-activity-list
- name: Activity
  property_count: 8
  slug: target-api-activity
- name: AudienceInput
  property_count: 3
  slug: target-api-audience-input
- name: AudienceList
  property_count: 4
  slug: target-api-audience-list
- name: Audience
  property_count: 4
  slug: target-api-audience
- name: DeliveryRequest
  property_count: 3
  slug: target-api-delivery-request
- name: DeliveryResponse
  property_count: 3
  slug: target-api-delivery-response
- name: EnvironmentList
  property_count: 1
  slug: target-api-environment-list
- name: OfferInput
  property_count: 3
  slug: target-api-offer-input
- name: OfferList
  property_count: 4
  slug: target-api-offer-list
- name: Offer
  property_count: 5
  slug: target-api-offer
- name: PropertyList
  property_count: 2
  slug: target-api-property-list
json_structures:
- name: Adobe Experience Cloud Campaign
  property_count: 11
  slug: adobe-experience-cloud-campaign
- name: Adobe Experience Cloud Event
  property_count: 9
  slug: adobe-experience-cloud-event
- name: Adobe Experience Cloud Journey
  property_count: 11
  slug: adobe-experience-cloud-journey
- name: Adobe Experience Cloud Offer
  property_count: 14
  slug: adobe-experience-cloud-offer
- name: Adobe Experience Cloud Profile
  property_count: 10
  slug: adobe-experience-cloud-profile
- name: Adobe Experience Cloud Segment
  property_count: 14
  slug: adobe-experience-cloud-segment
- name: Analytics Api Calculated Metric List Structure
  property_count: 3
  slug: analytics-api-calculated-metric-list-structure
- name: Analytics Api Calculated Metric Structure
  property_count: 7
  slug: analytics-api-calculated-metric-structure
- name: Analytics Api Date Range List Structure
  property_count: 2
  slug: analytics-api-date-range-list-structure
- name: Analytics Api Dimension Structure
  property_count: 5
  slug: analytics-api-dimension-structure
- name: Analytics Api Metric Structure
  property_count: 5
  slug: analytics-api-metric-structure
- name: Analytics Api Project List Structure
  property_count: 2
  slug: analytics-api-project-list-structure
- name: Analytics Api Project Structure
  property_count: 5
  slug: analytics-api-project-structure
- name: Analytics Api Report Request Structure
  property_count: 5
  slug: analytics-api-report-request-structure
- name: Analytics Api Report Response Structure
  property_count: 6
  slug: analytics-api-report-response-structure
- name: Analytics Api Report Suite List Structure
  property_count: 3
  slug: analytics-api-report-suite-list-structure
- name: Analytics Api Report Suite Structure
  property_count: 5
  slug: analytics-api-report-suite-structure
- name: Analytics Api Segment List Structure
  property_count: 3
  slug: analytics-api-segment-list-structure
- name: Analytics Api Segment Structure
  property_count: 7
  slug: analytics-api-segment-structure
- name: Analytics Api User List Structure
  property_count: 3
  slug: analytics-api-user-list-structure
- name: Analytics Api User Structure
  property_count: 6
  slug: analytics-api-user-structure
- name: Campaign Api Email List Structure
  property_count: 1
  slug: campaign-api-email-list-structure
- name: Campaign Api Email Structure
  property_count: 6
  slug: campaign-api-email-structure
- name: Campaign Api Profile Input Structure
  property_count: 5
  slug: campaign-api-profile-input-structure
- name: Campaign Api Profile List Structure
  property_count: 2
  slug: campaign-api-profile-list-structure
- name: Campaign Api Profile Structure
  property_count: 8
  slug: campaign-api-profile-structure
- name: Campaign Api Service Input Structure
  property_count: 3
  slug: campaign-api-service-input-structure
- name: Campaign Api Service List Structure
  property_count: 1
  slug: campaign-api-service-list-structure
- name: Campaign Api Service Structure
  property_count: 5
  slug: campaign-api-service-structure
- name: Campaign Api Transactional Message Request Structure
  property_count: 2
  slug: campaign-api-transactional-message-request-structure
- name: Campaign Api Transactional Message Response Structure
  property_count: 4
  slug: campaign-api-transactional-message-response-structure
- name: Campaign Api Workflow List Structure
  property_count: 1
  slug: campaign-api-workflow-list-structure
- name: Campaign Api Workflow Structure
  property_count: 5
  slug: campaign-api-workflow-structure
- name: Experience Platform Api Batch Structure
  property_count: 4
  slug: experience-platform-api-batch-structure
- name: Experience Platform Api Class List Structure
  property_count: 1
  slug: experience-platform-api-class-list-structure
- name: Experience Platform Api Dataset Input Structure
  property_count: 3
  slug: experience-platform-api-dataset-input-structure
- name: Experience Platform Api Dataset Structure
  property_count: 6
  slug: experience-platform-api-dataset-structure
- name: Experience Platform Api Identity Namespace Input Structure
  property_count: 4
  slug: experience-platform-api-identity-namespace-input-structure
- name: Experience Platform Api Identity Namespace Structure
  property_count: 6
  slug: experience-platform-api-identity-namespace-structure
- name: Experience Platform Api Profile Entity Structure
  property_count: 2
  slug: experience-platform-api-profile-entity-structure
- name: Experience Platform Api Query List Structure
  property_count: 2
  slug: experience-platform-api-query-list-structure
- name: Experience Platform Api Query Structure
  property_count: 8
  slug: experience-platform-api-query-structure
- name: Experience Platform Api Sandbox List Structure
  property_count: 1
  slug: experience-platform-api-sandbox-list-structure
- name: Experience Platform Api Sandbox Structure
  property_count: 4
  slug: experience-platform-api-sandbox-structure
- name: Experience Platform Api Schema Input Structure
  property_count: 4
  slug: experience-platform-api-schema-input-structure
- name: Experience Platform Api Schema List Structure
  property_count: 2
  slug: experience-platform-api-schema-list-structure
- name: Experience Platform Api Schema Structure
  property_count: 5
  slug: experience-platform-api-schema-structure
- name: Experience Platform Api Segment Definition Input Structure
  property_count: 5
  slug: experience-platform-api-segment-definition-input-structure
- name: Experience Platform Api Segment Definition List Structure
  property_count: 2
  slug: experience-platform-api-segment-definition-list-structure
- name: Experience Platform Api Segment Definition Structure
  property_count: 6
  slug: experience-platform-api-segment-definition-structure
- name: Journey Optimizer Api Campaign Input Structure
  property_count: 5
  slug: journey-optimizer-api-campaign-input-structure
- name: Journey Optimizer Api Campaign List Structure
  property_count: 2
  slug: journey-optimizer-api-campaign-list-structure
- name: Journey Optimizer Api Campaign Structure
  property_count: 6
  slug: journey-optimizer-api-campaign-structure
- name: Journey Optimizer Api Collection Input Structure
  property_count: 2
  slug: journey-optimizer-api-collection-input-structure
- name: Journey Optimizer Api Collection List Structure
  property_count: 1
  slug: journey-optimizer-api-collection-list-structure
- name: Journey Optimizer Api Collection Structure
  property_count: 3
  slug: journey-optimizer-api-collection-structure
- name: Journey Optimizer Api Content Template Input Structure
  property_count: 3
  slug: journey-optimizer-api-content-template-input-structure
- name: Journey Optimizer Api Content Template List Structure
  property_count: 2
  slug: journey-optimizer-api-content-template-list-structure
- name: Journey Optimizer Api Content Template Structure
  property_count: 5
  slug: journey-optimizer-api-content-template-structure
- name: Journey Optimizer Api Decision Rule Input Structure
  property_count: 3
  slug: journey-optimizer-api-decision-rule-input-structure
- name: Journey Optimizer Api Decision Rule List Structure
  property_count: 1
  slug: journey-optimizer-api-decision-rule-list-structure
- name: Journey Optimizer Api Decision Rule Structure
  property_count: 4
  slug: journey-optimizer-api-decision-rule-structure
- name: Journey Optimizer Api Journey Input Structure
  property_count: 4
  slug: journey-optimizer-api-journey-input-structure
- name: Journey Optimizer Api Journey List Structure
  property_count: 2
  slug: journey-optimizer-api-journey-list-structure
- name: Journey Optimizer Api Journey Structure
  property_count: 7
  slug: journey-optimizer-api-journey-structure
- name: Journey Optimizer Api Message Input Structure
  property_count: 3
  slug: journey-optimizer-api-message-input-structure
- name: Journey Optimizer Api Message List Structure
  property_count: 2
  slug: journey-optimizer-api-message-list-structure
- name: Journey Optimizer Api Message Structure
  property_count: 5
  slug: journey-optimizer-api-message-structure
- name: Journey Optimizer Api Offer Input Structure
  property_count: 6
  slug: journey-optimizer-api-offer-input-structure
- name: Journey Optimizer Api Offer List Structure
  property_count: 2
  slug: journey-optimizer-api-offer-list-structure
- name: Journey Optimizer Api Offer Structure
  property_count: 7
  slug: journey-optimizer-api-offer-structure
- name: Journey Optimizer Api Placement Input Structure
  property_count: 3
  slug: journey-optimizer-api-placement-input-structure
- name: Journey Optimizer Api Placement List Structure
  property_count: 1
  slug: journey-optimizer-api-placement-list-structure
- name: Journey Optimizer Api Placement Structure
  property_count: 4
  slug: journey-optimizer-api-placement-structure
- name: Target Api Activity Input Structure
  property_count: 5
  slug: target-api-activity-input-structure
- name: Target Api Activity List Structure
  property_count: 4
  slug: target-api-activity-list-structure
- name: Target Api Activity Structure
  property_count: 8
  slug: target-api-activity-structure
- name: Target Api Audience Input Structure
  property_count: 3
  slug: target-api-audience-input-structure
- name: Target Api Audience List Structure
  property_count: 4
  slug: target-api-audience-list-structure
- name: Target Api Audience Structure
  property_count: 4
  slug: target-api-audience-structure
- name: Target Api Delivery Request Structure
  property_count: 3
  slug: target-api-delivery-request-structure
- name: Target Api Delivery Response Structure
  property_count: 3
  slug: target-api-delivery-response-structure
- name: Target Api Environment List Structure
  property_count: 1
  slug: target-api-environment-list-structure
- name: Target Api Offer Input Structure
  property_count: 3
  slug: target-api-offer-input-structure
- name: Target Api Offer List Structure
  property_count: 4
  slug: target-api-offer-list-structure
- name: Target Api Offer Structure
  property_count: 5
  slug: target-api-offer-structure
- name: Target Api Property List Structure
  property_count: 2
  slug: target-api-property-list-structure
jsonld:
- class_count: 18
  name: Adobe Experience Cloud Analytics Api Context
  property_count: 34
  slug: adobe-experience-cloud-analytics-api-context
- class_count: 14
  name: Adobe Experience Cloud Campaign Api Context
  property_count: 20
  slug: adobe-experience-cloud-campaign-api-context
- class_count: 7
  name: Adobe Experience Cloud Context
  property_count: 11
  slug: adobe-experience-cloud-context
- class_count: 20
  name: Adobe Experience Cloud Experience Platform Api Context
  property_count: 37
  slug: adobe-experience-cloud-experience-platform-api-context
- class_count: 10
  name: Adobe Experience Cloud Io Events Context
  property_count: 122
  slug: adobe-experience-cloud-io-events-context
- class_count: 27
  name: Adobe Experience Cloud Journey Optimizer Api Context
  property_count: 28
  slug: adobe-experience-cloud-journey-optimizer-api-context
- class_count: 15
  name: Adobe Experience Cloud Target Api Context
  property_count: 28
  slug: adobe-experience-cloud-target-api-context
layout: provider
modified: '2026-04-19'
name: Adobe Experience Cloud
nav: Providers
network: true
overview: 'Adobe Experience Cloud publishes 36 APIs on the [APIs.io](https://apis.io/) network, including Adobe I/O Events, Activities API, Audiences API, and 33 more. Tagged areas include Analytics, Customer Experience, Digital Marketing, Personalization, and Campaign Management.


  The Adobe Experience Cloud catalog on APIs.io includes 1 event-driven AsyncAPI specification, 7 JSON-LD contexts, and 3 Spectral governance rulesets.


  Adobe Experience Cloud''s developer surface includes authentication, developer portal, documentation, engineering blog, support, developer console, signup flow, and 39 more developer resources.'
plans:
- name: Adobe Experience Cloud Plans Pricing
  plan_count: 5
  slug: adobe-experience-cloud-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 4
  name: Adobe Experience Cloud Rate Limits
  slug: adobe-experience-cloud-rate-limits
rules:
- name: Adobe Experience Cloud API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: adobe-experience-cloud-asyncapi-spectral-rules
- name: Adobe Experience Cloud API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: adobe-experience-cloud-jsonschema-spectral-rules
- name: Adobe Experience Cloud API Rules
  rule_count: 37
  severity_counts:
    error: 16
    hint: 0
    info: 3
    warn: 18
  slug: adobe-experience-cloud-spectral-rules
score:
  band: strong
  composite: 64.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 80.8
    developer_ergonomics: 56.5
    discoverability: 59.3
    governance: 52.1
    operational_transparency: 68.4
  previous_composite: 64.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 35
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adobe-experience-cloud/refs/heads/main/screenshots/adobe-experience-cloud-2026-06-20T164907.png
security:
- kind: authentication
  name: Adobe Experience Cloud Authentication
  slug: adobe-experience-cloud-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Adobe Experience Cloud Domain Security
  slug: adobe-experience-cloud-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adobe Experience Cloud Vulnerability Disclosure
  slug: adobe-experience-cloud-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: adobe-experience-cloud
tags:
- Analytics
- Customer Experience
- Digital Marketing
- Personalization
- Campaign Management
- Journey Orchestration
use_cases:
- description: Ingest data from multiple sources, resolve identities, and activate unified customer profiles for personalization.
  name: Customer Data Platform
- description: Automate campaign creation, scheduling, and execution across email, SMS, and push channels using Campaign and Journey Optimizer APIs.
  name: Marketing Automation
- description: Extract Adobe Analytics data into custom dashboards, BI tools, and data warehouses via the Analytics 2.0 API.
  name: Digital Analytics Reporting
- description: Deliver personalized content and offers in real time using Adobe Target and Journey Optimizer APIs.
  name: Real-Time Personalization
- description: Build reactive integrations that respond to Experience Cloud events such as profile updates, campaign completions, and audience changes.
  name: Event-Driven Workflows
- description: Create and activate audiences across paid media, email, and on-site channels using Experience Platform Segmentation API.
  name: Audience Activation
website: https://developer.adobe.com/
---
