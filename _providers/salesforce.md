---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.2
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 172
  human_in_the_loop: 5
  name: Salesforce Agentic Access
  operation_count: 389
  slug: salesforce-agentic-access
  summary_line: 389 operations · 172 acting · 5 human-in-the-loop
api_count: 4
apis:
- description: The Salesforce REST API provides a simple and powerful web service interface to interact with Salesforce org data. It supports creating, reading, updating, deleting, and querying records using SOQL an
  name: Salesforce REST API
  slug: salesforce-rest-api
- description: The Salesforce SOAP API enables developers to use SOAP calls to create, retrieve, update, and delete records such as accounts, leads, and custom objects. It provides robust enterprise-grade integratio
  name: Salesforce SOAP API
  slug: salesforce-soap-api
- description: 'The Salesforce Bulk API is a specialized REST-based interface that enables asynchronous processing of large numbers of records. It is optimized for loading or deleting large sets of data and supports '
  name: Salesforce Bulk API
  slug: salesforce-bulk-api
- description: The Salesforce Streaming API uses a publish-subscribe model based on Bayeux/CometD to push near-real-time event notifications to subscribed clients. It supports PushTopic events for record changes and
  name: Salesforce Streaming API
  slug: salesforce-streaming-api
- description: The Salesforce Metadata API is a SOAP-based API that enables developers to retrieve, deploy, create, update, and delete customizations for Salesforce organizations. It is the foundation for tools like
  name: Salesforce Metadata API
  slug: salesforce-metadata-api
- description: The Salesforce Tooling API provides SOAP and REST interfaces for building developer tools for Force.com applications. It exposes fine-grained access to Apex code, Visualforce pages, and other metadata
  name: Salesforce Tooling API
  slug: salesforce-tooling-api
- description: 'The Salesforce Connect REST API (formerly Chatter API) provides access to Salesforce Chatter feeds, groups, users, topics, and file sharing features. It also exposes Experience Cloud (community) data '
  name: Salesforce Connect API (Chatter)
  slug: salesforce-connect-api
- description: The Salesforce Analytics REST API (also known as CRM Analytics or Wave API) provides programmatic access to CRM Analytics datasets, lenses, dashboards, and queries. Developers can read and write analy
  name: Salesforce Analytics REST API
  slug: salesforce-analytics-rest-api
- description: The Salesforce Reports and Dashboards REST API enables developers to programmatically access report results, list reports and dashboards, and run and filter reports. It supports accessing standard and
  name: Salesforce Reports and Dashboards REST API
  slug: salesforce-reports-and-dashboards-rest-api
- description: The Salesforce Einstein Platform Services API provides REST-based access to Salesforce AI capabilities including image classification, object detection, and sentiment analysis. Developers can train cu
  name: Salesforce Einstein Platform Services API
  slug: salesforce-einstein-platform-services-api
- description: The Salesforce Einstein Prediction Service API enables programmatic access to Einstein Analytics predictions and forecasts built on CRM data. It allows applications to retrieve AI-driven predictions f
  name: Salesforce Einstein Prediction Service API
  slug: salesforce-einstein-prediction-service-api
- description: The Salesforce GraphQL API provides a GraphQL interface to query and mutate Salesforce data. It allows clients to request exactly the data they need in a single request, reducing over-fetching and und
  name: Salesforce GraphQL API
  slug: salesforce-graphql-api
- description: The Salesforce Pub/Sub API is a gRPC-based API for publishing and subscribing to platform events, change data capture events, and other event types in real time. It supersedes the CometD-based Streami
  name: Salesforce Pub/Sub API
  slug: salesforce-pub-sub-api
- description: Salesforce Platform Events enables event-driven integration architectures built on the Salesforce platform. Developers define custom event types as Salesforce objects and publish or subscribe to event
  name: Salesforce Platform Events API
  slug: salesforce-platform-events-api
- description: Salesforce Change Data Capture delivers change events that represent changes to Salesforce records including creates, updates, deletes, and undeletes. It enables external systems to receive near-real-
  name: Salesforce Change Data Capture API
  slug: salesforce-change-data-capture-api
- description: The Salesforce Composite API allows developers to combine multiple Salesforce REST API requests into a single HTTP call. It reduces the number of round trips to the server and supports dependent reque
  name: Salesforce Composite API
  slug: salesforce-composite-api
- description: Salesforce Apex REST enables developers to expose custom Apex classes as RESTful web services. By annotating Apex classes and methods with @RestResource and HTTP method annotations, developers can cre
  name: Salesforce Apex REST API
  slug: salesforce-apex-rest-api
- description: The Salesforce Data Cloud API provides programmatic access to Data Cloud (formerly Customer Data Platform) for ingesting, querying, and managing unified customer profiles. It enables applications to r
  name: Salesforce Data Cloud API
  slug: salesforce-data-cloud-api
- description: The Salesforce Marketing Cloud SOAP API is a full-featured SOAP web service interface for Marketing Cloud that supports subscriber management, email send operations, automation activities, and data ex
  name: Salesforce Marketing Cloud SOAP API
  slug: salesforce-marketing-cloud-soap-api
- description: The Salesforce Pardot API (now called Account Engagement API) provides programmatic access to Pardot marketing automation data including prospects, campaigns, forms, lists, and email statistics for B2
  name: Salesforce Pardot API (Account Engagement)
  slug: salesforce-pardot-api
- description: The Salesforce Commerce Cloud Open Commerce API (OCAPI) provides a REST interface for accessing Salesforce B2C Commerce data and functionality including products, catalogs, orders, promotions, and cus
  name: Salesforce Commerce Cloud OCAPI
  slug: salesforce-commerce-cloud-ocapi
- description: The Salesforce Commerce Cloud Shopper APIs (SCAPI) are a modern set of REST APIs for building B2C Commerce storefronts and headless commerce experiences. They cover shopper authentication, products, s
  name: Salesforce Commerce Cloud Shopper APIs (SCAPI)
  slug: salesforce-commerce-cloud-shopper-apis
- description: The Salesforce Field Service API provides access to Field Service Lightning data and operations including work orders, service appointments, resource scheduling, and mobile workforce management. It en
  name: Salesforce Field Service API
  slug: salesforce-field-service-api
- description: The Salesforce Health Cloud API provides FHIR R4-compliant REST APIs and platform APIs for accessing patient and provider data in Health Cloud. It enables healthcare applications to interact with clin
  name: Salesforce Health Cloud API
  slug: salesforce-health-cloud-api
- description: The Salesforce Financial Services Cloud API exposes financial services-specific data objects including financial accounts, assets, liabilities, financial goals, and household relationships. It enables
  name: Salesforce Financial Services Cloud API
  slug: salesforce-financial-services-cloud-api
- description: The Salesforce Experience Cloud API provides REST access to Experience Cloud (formerly Community Cloud) data including community membership, navigation, managed content, and knowledge articles. It ena
  name: Salesforce Experience Cloud API
  slug: salesforce-experience-cloud-api
- description: The MuleSoft Anypoint Platform API provides programmatic access to the MuleSoft integration platform including API Manager, Runtime Manager, Exchange, and Access Management. It enables automation of A
  name: Salesforce MuleSoft Anypoint Platform API
  slug: salesforce-mulesoft-anypoint-platform-api
- description: The Tableau REST API enables developers to programmatically manage Tableau Server and Tableau Cloud resources including workbooks, data sources, views, sites, users, and groups. It supports automation
  name: Salesforce Tableau REST API
  slug: salesforce-tableau-rest-api
- description: Lightning Web Components (LWC) is Salesforce's standards-based JavaScript framework for building UI components on the Salesforce platform. It uses modern web standards including custom elements, templ
  name: Salesforce Lightning Web Components (LWC)
  slug: salesforce-lightning-web-components
- description: Salesforce Aura Components is the legacy JavaScript component framework for building dynamic web applications on the Salesforce platform. It provides a data binding model, event system, and Apex contr
  name: Salesforce Aura Components
  slug: salesforce-aura-components
- description: The Salesforce Lightning Design System (SLDS) provides HTML and CSS component blueprints, design tokens, and utility classes for building applications visually consistent with Salesforce Lightning Exp
  name: Salesforce Lightning Design System (SLDS)
  slug: salesforce-lightning-design-system
- description: The Salesforce Agentforce Agent API is a REST API that enables developers to communicate with AI agents directly, starting sessions, sending messages, receiving responses, and ending sessions. It supp
  name: Salesforce Agentforce Agent API
  slug: salesforce-agentforce-agent-api
- description: The Salesforce Models API provides Apex classes and REST endpoints that connect applications to large language models (LLMs) from Salesforce partners including Anthropic, Google, and OpenAI. It suppor
  name: Salesforce Models API
  slug: salesforce-models-api
- description: The Salesforce Interaction Service API enables automation and customization of the Bring Your Own Channel (BYOC) experience for messaging. It sends inbound messaging interactions from external end-use
  name: Salesforce Interaction Service API
  slug: salesforce-interaction-service-api
- description: The Salesforce B2B Commerce API provides REST endpoints for handling commerce data in B2B and D2C storefronts. It offers support for address management, cart management, checkout processing, order man
  name: Salesforce B2B Commerce API
  slug: salesforce-b2b-commerce-api
- description: The Salesforce Actions API provides a unified interface for invoking standard and custom actions across the Salesforce platform. It supports Apex actions, Flow actions, quick actions, and invocable ac
  name: Salesforce Actions API
  slug: salesforce-actions-api
- description: The Salesforce IoT REST API provides programmatic access to Salesforce IoT data including contexts, orchestrations, and usage data. It enables developers to manage IoT events and orchestration rules f
  name: Salesforce IoT REST API
  slug: salesforce-iot-api
- description: The Salesforce Service Cloud Voice API provides Telephony Integration REST API and Voice Toolkit API for programmatically managing voice calls and integrating telephony systems with Salesforce. It sup
  name: Salesforce Service Cloud Voice API
  slug: salesforce-service-cloud-voice-api
- description: The Salesforce Mobile SDK provides libraries and tools for building native and hybrid mobile applications on iOS and Android that integrate with the Salesforce platform. It supports Swift, Objective-C
  name: Salesforce Mobile SDK
  slug: salesforce-mobile-sdk
- description: The Abort API from Salesforce — 2 operation(s) for abort.
  name: Salesforce Abort API
  slug: salesforce-abort-api
- description: The Access API from Salesforce — 1 operation(s) for access.
  name: Salesforce Access API
  slug: salesforce-access-api
- description: The Accounts API from Salesforce — 1 operation(s) for accounts.
  name: Salesforce Accounts API
  slug: salesforce-accounts-api
- description: The Actions API from Salesforce — 16 operation(s) for actions.
  name: Salesforce Actions API
  slug: salesforce-actions-api
- description: The Active API from Salesforce — 1 operation(s) for active.
  name: Salesforce Active API
  slug: salesforce-active-api
- description: The Add API from Salesforce — 2 operation(s) for add.
  name: Salesforce Add API
  slug: salesforce-add-api
- description: The Agent API from Salesforce — 2 operation(s) for agent.
  name: Salesforce Agent API
  slug: salesforce-agent-api
- description: The All API from Salesforce — 4 operation(s) for all.
  name: Salesforce All API
  slug: salesforce-all-api
- description: The Amend API from Salesforce — 1 operation(s) for amend.
  name: Salesforce Amend API
  slug: salesforce-amend-api
- description: The Applications API from Salesforce — 6 operation(s) for applications.
  name: Salesforce Applications API
  slug: salesforce-applications-api
- description: The Appointment API from Salesforce — 2 operation(s) for appointment.
  name: Salesforce Appointment API
  slug: salesforce-appointment-api
- description: The Approvals API from Salesforce — 1 operation(s) for approvals.
  name: Salesforce Approvals API
  slug: salesforce-approvals-api
- description: Operations for managing Marketing Cloud Content Builder assets including emails, images, and other content items.
  name: Salesforce Assets API
  slug: salesforce-assets-api
- description: The Async API from Salesforce — 1 operation(s) for async.
  name: Salesforce Async API
  slug: salesforce-async-api
- description: OAuth 2.0 token operations for obtaining access tokens using client credentials or authorization code flows.
  name: Salesforce Authentication API
  slug: salesforce-authentication-api
- description: The Authorize API from Salesforce — 1 operation(s) for authorize.
  name: Salesforce Authorize API
  slug: salesforce-authorize-api
- description: The Based API from Salesforce — 1 operation(s) for based.
  name: Salesforce Based API
  slug: salesforce-based-api
- description: The Basic API from Salesforce — 1 operation(s) for basic.
  name: Salesforce Basic API
  slug: salesforce-basic-api
- description: The Batch API from Salesforce — 7 operation(s) for batch.
  name: Salesforce Batch API
  slug: salesforce-batch-api
- description: The Benefits API from Salesforce — 1 operation(s) for benefits.
  name: Salesforce Benefits API
  slug: salesforce-benefits-api
- description: The Blobs API from Salesforce — 1 operation(s) for blobs.
  name: Salesforce Blobs API
  slug: salesforce-blobs-api
- description: The Bulk API from Salesforce — 6 operation(s) for bulk.
  name: Salesforce Bulk API
  slug: salesforce-bulk-api
- description: The Bundles API from Salesforce — 1 operation(s) for bundles.
  name: Salesforce Bundles API
  slug: salesforce-bundles-api
- description: The Calculate API from Salesforce — 1 operation(s) for calculate.
  name: Salesforce Calculate API
  slug: salesforce-calculate-api
- description: The Call API from Salesforce — 1 operation(s) for call.
  name: Salesforce Call API
  slug: salesforce-call-api
- description: The Cancel API from Salesforce — 1 operation(s) for cancel.
  name: Salesforce Cancel API
  slug: salesforce-cancel-api
- description: The Capability API from Salesforce — 1 operation(s) for capability.
  name: Salesforce Capability API
  slug: salesforce-capability-api
- description: The Change API from Salesforce — 1 operation(s) for change.
  name: Salesforce Change API
  slug: salesforce-change-api
- description: The Channel API from Salesforce — 5 operation(s) for channel.
  name: Salesforce Channel API
  slug: salesforce-channel-api
- description: The Child API from Salesforce — 1 operation(s) for child.
  name: Salesforce Child API
  slug: salesforce-child-api
- description: The Client API from Salesforce — 1 operation(s) for client.
  name: Salesforce Client API
  slug: salesforce-client-api
- description: The Clone API from Salesforce — 1 operation(s) for clone.
  name: Salesforce Clone API
  slug: salesforce-clone-api
- description: The Collections API from Salesforce — 4 operation(s) for collections.
  name: Salesforce Collections API
  slug: salesforce-collections-api
- description: Get, edit, and delete comments.
  name: Salesforce Comments API
  slug: salesforce-comments-api
- description: The Commitment API from Salesforce — 1 operation(s) for commitment.
  name: Salesforce Commitment API
  slug: salesforce-commitment-api
- description: The Compact API from Salesforce — 1 operation(s) for compact.
  name: Salesforce Compact API
  slug: salesforce-compact-api
- description: The Completion API from Salesforce — 1 operation(s) for completion.
  name: Salesforce Completion API
  slug: salesforce-completion-api
- description: The Composite API executes a series of REST API requests in a single POST request, or retrieves a list of other composite resources with a GET request. There are three types of Composite requests some
  name: Salesforce Composite API
  slug: salesforce-composite-api
- description: The Configuration API from Salesforce — 3 operation(s) for configuration.
  name: Salesforce Configuration API
  slug: salesforce-configuration-api
- description: The Connect API from Salesforce — 3 operation(s) for connect.
  name: Salesforce Connect API
  slug: salesforce-connect-api
- description: The Consent API from Salesforce — 1 operation(s) for consent.
  name: Salesforce Consent API
  slug: salesforce-consent-api
- description: Operations for listing, retrieving, and deleting Marketing Cloud contact records.
  name: Salesforce Contacts API
  slug: salesforce-contacts-api
- description: The Content API from Salesforce — 1 operation(s) for content.
  name: Salesforce Content API
  slug: salesforce-content-api
- description: The Conversation API from Salesforce — 1 operation(s) for conversation.
  name: Salesforce Conversation API
  slug: salesforce-conversation-api
- description: The Corporate API from Salesforce — 1 operation(s) for corporate.
  name: Salesforce Corporate API
  slug: salesforce-corporate-api
- description: The Count API from Salesforce — 1 operation(s) for count.
  name: Salesforce Count API
  slug: salesforce-count-api
- description: The Create API from Salesforce — 23 operation(s) for create.
  name: Salesforce Create API
  slug: salesforce-create-api
- description: The Creation API from Salesforce — 2 operation(s) for creation.
  name: Salesforce Creation API
  slug: salesforce-creation-api
- description: The Credential API from Salesforce — 6 operation(s) for credential.
  name: Salesforce Credential API
  slug: salesforce-credential-api
- description: '> Use these Connect API endpoints to get credentials for OAuth consumers of an external client app. Collections returns credentials for all consumers associated with an external client app. Resources '
  name: Salesforce Credentials API
  slug: salesforce-credentials-api
- description: The Data API from Salesforce — 16 operation(s) for data.
  name: Salesforce Data API
  slug: salesforce-data-api
- description: Operations for reading and writing rows in Marketing Cloud Data Extensions, which are custom tables for storing subscriber data and campaign data.
  name: Salesforce Data Extensions API
  slug: salesforce-data-extensions-api
- description: The Decision API from Salesforce — 1 operation(s) for decision.
  name: Salesforce Decision API
  slug: salesforce-decision-api
- description: The Definition API from Salesforce — 1 operation(s) for definition.
  name: Salesforce Definition API
  slug: salesforce-definition-api
- description: The Definitions API from Salesforce — 1 operation(s) for definitions.
  name: Salesforce Definitions API
  slug: salesforce-definitions-api
- description: The Deletes API from Salesforce — 20 operation(s) for deletes.
  name: Salesforce Deletes API
  slug: salesforce-deletes-api
- description: The Dependencies API from Salesforce — 1 operation(s) for dependencies.
  name: Salesforce Dependencies API
  slug: salesforce-dependencies-api
- description: The Describe API from Salesforce — 13 operation(s) for describe.
  name: Salesforce Describe API
  slug: salesforce-describe-api
- description: The Directories API from Salesforce — 1 operation(s) for directories.
  name: Salesforce Directories API
  slug: salesforce-directories-api
- description: The Download API from Salesforce — 1 operation(s) for download.
  name: Salesforce Download API
  slug: salesforce-download-api
- description: The Elements API from Salesforce — 6 operation(s) for elements.
  name: Salesforce Elements API
  slug: salesforce-elements-api
- description: The Eligible API from Salesforce — 1 operation(s) for eligible.
  name: Salesforce Eligible API
  slug: salesforce-eligible-api
- description: The Events API from Salesforce — 16 operation(s) for events.
  name: Salesforce Events API
  slug: salesforce-events-api
- description: The Exchange API from Salesforce — 1 operation(s) for exchange.
  name: Salesforce Exchange API
  slug: salesforce-exchange-api
- description: The Execution API from Salesforce — 1 operation(s) for execution.
  name: Salesforce Execution API
  slug: salesforce-execution-api
- description: The Exit API from Salesforce — 1 operation(s) for exit.
  name: Salesforce Exit API
  slug: salesforce-exit-api
- description: The Expression API from Salesforce — 4 operation(s) for expression.
  name: Salesforce Expression API
  slug: salesforce-expression-api
- description: The External API from Salesforce — 3 operation(s) for external.
  name: Salesforce External API
  slug: salesforce-external-api
- description: The Failed API from Salesforce — 1 operation(s) for failed.
  name: Salesforce Failed API
  slug: salesforce-failed-api
- description: The Favorite API from Salesforce — 3 operation(s) for favorite.
  name: Salesforce Favorite API
  slug: salesforce-favorite-api
- description: The Field API from Salesforce — 4 operation(s) for field.
  name: Salesforce Field API
  slug: salesforce-field-api
- description: The Files API from Salesforce — 7 operation(s) for files.
  name: Salesforce Files API
  slug: salesforce-files-api
- description: The Flow API from Salesforce — 2 operation(s) for flow.
  name: Salesforce Flow API
  slug: salesforce-flow-api
- description: The Following API from Salesforce — 1 operation(s) for following.
  name: Salesforce Following API
  slug: salesforce-following-api
- description: The Game API from Salesforce — 1 operation(s) for game.
  name: Salesforce Game API
  slug: salesforce-game-api
- description: The Games API from Salesforce — 1 operation(s) for games.
  name: Salesforce Games API
  slug: salesforce-games-api
- description: The General API from Salesforce — 2 operation(s) for general.
  name: Salesforce General API
  slug: salesforce-general-api
- description: The Get API from Salesforce — 71 operation(s) for get.
  name: Salesforce Get API
  slug: salesforce-get-api
- description: The Gift API from Salesforce — 1 operation(s) for gift.
  name: Salesforce Gift API
  slug: salesforce-gift-api
- description: Get groups and group members. Create groups, invites, and members.
  name: Salesforce Groups API
  slug: salesforce-groups-api
- description: The History API from Salesforce — 1 operation(s) for history.
  name: Salesforce History API
  slug: salesforce-history-api
- description: The Identifiers API from Salesforce — 6 operation(s) for identifiers.
  name: Salesforce Identifiers API
  slug: salesforce-identifiers-api
- description: The Image API from Salesforce — 1 operation(s) for image.
  name: Salesforce Image API
  slug: salesforce-image-api
- description: The Individual API from Salesforce — 1 operation(s) for individual.
  name: Salesforce Individual API
  slug: salesforce-individual-api
- description: The Info API from Salesforce — 4 operation(s) for info.
  name: Salesforce Info API
  slug: salesforce-info-api
- description: Operations for uploading CSV data to ingest jobs and retrieving job results (successful, failed, and unprocessed records).
  name: Salesforce Ingest Job Data API
  slug: salesforce-ingest-job-data-api
- description: Operations for creating and managing ingest jobs that insert, update, upsert, delete, or hard delete records in bulk using CSV data.
  name: Salesforce Ingest Jobs API
  slug: salesforce-ingest-jobs-api
- description: The Initialize API from Salesforce — 3 operation(s) for initialize.
  name: Salesforce Initialize API
  slug: salesforce-initialize-api
- description: The Initiate API from Salesforce — 3 operation(s) for initiate.
  name: Salesforce Initiate API
  slug: salesforce-initiate-api
- description: The Instant API from Salesforce — 1 operation(s) for instant.
  name: Salesforce Instant API
  slug: salesforce-instant-api
- description: The Integration API from Salesforce — 1 operation(s) for integration.
  name: Salesforce Integration API
  slug: salesforce-integration-api
- description: The Invoke API from Salesforce — 1 operation(s) for invoke.
  name: Salesforce Invoke API
  slug: salesforce-invoke-api
- description: The Items API from Salesforce — 6 operation(s) for items.
  name: Salesforce Items API
  slug: salesforce-items-api
- description: Operations for listing and retrieving Marketing Cloud Journey Builder journeys (interactions) and firing journey entry events.
  name: Salesforce Journeys API
  slug: salesforce-journeys-api
- description: The Keys API from Salesforce — 1 operation(s) for keys.
  name: Salesforce Keys API
  slug: salesforce-keys-api
- description: The Knowledge API from Salesforce — 1 operation(s) for knowledge.
  name: Salesforce Knowledge API
  slug: salesforce-knowledge-api
- description: The Layouts API from Salesforce — 6 operation(s) for layouts.
  name: Salesforce Layouts API
  slug: salesforce-layouts-api
- description: The Lightning API from Salesforce — 6 operation(s) for lightning.
  name: Salesforce Lightning API
  slug: salesforce-lightning-api
- description: Retrieve list view data and metadata for use in UI components
  name: Salesforce List Views API
  slug: salesforce-list-views-api
- description: The Lists API from Salesforce — 20 operation(s) for lists.
  name: Salesforce Lists API
  slug: salesforce-lists-api
- description: Lookup field search endpoints
  name: Salesforce Lookups API
  slug: salesforce-lookups-api
- description: The Member API from Salesforce — 7 operation(s) for member.
  name: Salesforce Member API
  slug: salesforce-member-api
- description: Operations for creating and tracking email and SMS message sends, including triggered sends and transactional messages.
  name: Salesforce Messaging API
  slug: salesforce-messaging-api
- description: The Models API from Salesforce — 2 operation(s) for models.
  name: Salesforce Models API
  slug: salesforce-models-api
- description: The Oauth API from Salesforce — 5 operation(s) for oauth.
  name: Salesforce Oauth API
  slug: salesforce-oauth-api
- description: Retrieve object metadata including fields, layouts, and picklists
  name: Salesforce Object Info API
  slug: salesforce-object-info-api
- description: The Order API from Salesforce — 2 operation(s) for order.
  name: Salesforce Order API
  slug: salesforce-order-api
- description: The Password API from Salesforce — 3 operation(s) for password.
  name: Salesforce Password API
  slug: salesforce-password-api
- description: The Photo API from Salesforce — 2 operation(s) for photo.
  name: Salesforce Photo API
  slug: salesforce-photo-api
- description: Dependent and independent picklist value endpoints
  name: Salesforce Picklists API
  slug: salesforce-picklists-api
- description: The Post API from Salesforce — 7 operation(s) for post.
  name: Salesforce Post API
  slug: salesforce-post-api
- description: The Predict API from Salesforce — 1 operation(s) for predict.
  name: Salesforce Predict API
  slug: salesforce-predict-api
- description: The Process API from Salesforce — 2 operation(s) for process.
  name: Salesforce Process API
  slug: salesforce-process-api
- description: The Product API from Salesforce — 2 operation(s) for product.
  name: Salesforce Product API
  slug: salesforce-product-api
- description: 'The [promotion APIs](https://developer.salesforce.com/docs/atlas.en-us.loyalty.meta/loyalty/loyalty_promotion_apis_reference.htm) allow you to set eligibility rules and limits for a promotion, choose '
  name: Salesforce Promotion API
  slug: salesforce-promotion-api
- description: The Queries API from Salesforce — 5 operation(s) for queries.
  name: Salesforce Queries API
  slug: salesforce-queries-api
- description: Operations for retrieving the results of completed query jobs as CSV data.
  name: Salesforce Query Job Results API
  slug: salesforce-query-job-results-api
- description: Operations for creating and managing query jobs that extract large volumes of data from Salesforce using SOQL.
  name: Salesforce Query Jobs API
  slug: salesforce-query-jobs-api
- description: The Quote API from Salesforce — 3 operation(s) for quote.
  name: Salesforce Quote API
  slug: salesforce-quote-api
- description: The Record API from Salesforce — 17 operation(s) for record.
  name: Salesforce Record API
  slug: salesforce-record-api
- description: The Records API from Salesforce — 8 operation(s) for records.
  name: Salesforce Records API
  slug: salesforce-records-api
- description: The Redeem API from Salesforce — 1 operation(s) for redeem.
  name: Salesforce Redeem API
  slug: salesforce-redeem-api
- description: The Refresh API from Salesforce — 1 operation(s) for refresh.
  name: Salesforce Refresh API
  slug: salesforce-refresh-api
- description: The Relationships API from Salesforce — 1 operation(s) for relationships.
  name: Salesforce Relationships API
  slug: salesforce-relationships-api
- description: The Requests API from Salesforce — 2 operation(s) for requests.
  name: Salesforce Requests API
  slug: salesforce-requests-api
- description: The Resources API from Salesforce — 2 operation(s) for resources.
  name: Salesforce Resources API
  slug: salesforce-resources-api
- description: The Retrieves API from Salesforce — 10 operation(s) for retrieves.
  name: Salesforce Retrieves API
  slug: salesforce-retrieves-api
- description: The Revoke API from Salesforce — 4 operation(s) for revoke.
  name: Salesforce Revoke API
  slug: salesforce-revoke-api
- description: The Rows API from Salesforce — 2 operation(s) for rows.
  name: Salesforce Rows API
  slug: salesforce-rows-api
- description: The Runs API from Salesforce — 3 operation(s) for runs.
  name: Salesforce Runs API
  slug: salesforce-runs-api
- description: Manage sandboxes
  name: Salesforce Sandbox API
  slug: salesforce-sandbox-api
- description: The Scheduling API from Salesforce — 1 operation(s) for scheduling.
  name: Salesforce Scheduling API
  slug: salesforce-scheduling-api
- description: The Search API from Salesforce — 9 operation(s) for search.
  name: Salesforce Search API
  slug: salesforce-search-api
- description: The Soap API from Salesforce — 3 operation(s) for soap.
  name: Salesforce Soap API
  slug: salesforce-soap-api
- description: The Suggested API from Salesforce — 3 operation(s) for suggested.
  name: Salesforce Suggested API
  slug: salesforce-suggested-api
- description: The Summaries API from Salesforce — 1 operation(s) for summaries.
  name: Salesforce Summaries API
  slug: salesforce-summaries-api
- description: The Table API from Salesforce — 4 operation(s) for table.
  name: Salesforce Table API
  slug: salesforce-table-api
- description: The Tabs API from Salesforce — 1 operation(s) for tabs.
  name: Salesforce Tabs API
  slug: salesforce-tabs-api
- description: The Themes API from Salesforce — 1 operation(s) for themes.
  name: Salesforce Themes API
  slug: salesforce-themes-api
- description: The Trees API from Salesforce — 1 operation(s) for trees.
  name: Salesforce Trees API
  slug: salesforce-trees-api
- description: The Update API from Salesforce — 20 operation(s) for update.
  name: Salesforce Update API
  slug: salesforce-update-api
- description: The Versions API from Salesforce — 4 operation(s) for versions.
  name: Salesforce Versions API
  slug: salesforce-versions-api
arazzos:
- description: Run the full Bulk API 2.0 delete lifecycle — create a delete ingest job, upload a CSV of Ids, close, poll, and read successful results.
  name: Salesforce Bulk Delete Records
  slug: salesforce-bulk-delete-records-workflow
- description: Run the full Bulk API 2.0 insert lifecycle — create an ingest job, upload CSV, close, poll, and read successful results.
  name: Salesforce Bulk Insert Records
  slug: salesforce-bulk-insert-records-workflow
- description: Run the Bulk API 2.0 query lifecycle — create a query job, poll until JobComplete, and download the result CSV.
  name: Salesforce Bulk Query
  slug: salesforce-bulk-query-workflow
- description: Run the full Bulk API 2.0 upsert lifecycle — create an upsert ingest job keyed on an external Id field, upload CSV, close, poll, and read successful results.
  name: Salesforce Bulk Upsert Records
  slug: salesforce-bulk-upsert-records-workflow
- description: Create an Account and then create a Contact that belongs to it.
  name: Salesforce Create Account with Contact
  slug: salesforce-create-account-with-contacts-workflow
- description: Create a support Case associated with an existing Contact and Account.
  name: Salesforce Create Case for Contact
  slug: salesforce-create-case-for-contact-workflow
- description: Create a Lead, then create the related Task and Campaign Member records that move it through the sales process.
  name: Salesforce Create Lead and Follow-up Records
  slug: salesforce-create-lead-and-convert-workflow
- description: Create an Opportunity and then attach an OpportunityContactRole linking a Contact to the deal.
  name: Salesforce Create Opportunity with Contact Role
  slug: salesforce-create-opportunity-with-contact-role-workflow
- description: Create an SObject record then retrieve it by its newly assigned record id.
  name: Salesforce Create Record
  slug: salesforce-create-record-workflow
- description: Delete an SObject record by id after confirming it exists.
  name: Salesforce Delete Record
  slug: salesforce-delete-record-workflow
- description: List all SObjects in the org then fully describe one object's metadata.
  name: Salesforce Describe SObject
  slug: salesforce-describe-sobject-workflow
- description: Discover an object's list views, then load the records for a chosen list view.
  name: Salesforce Get Records for a List View
  slug: salesforce-get-list-view-records-workflow
- description: Read the current org governor limits and remaining quotas.
  name: Salesforce Get Org Limits
  slug: salesforce-get-org-limits-workflow
- description: Resolve an object's record type, then fetch its picklist field values.
  name: Salesforce Get Picklist Values for a Record Type
  slug: salesforce-get-picklist-values-workflow
- description: Fetch a record's UI API representation with its object metadata and layout fields.
  name: Salesforce Get a Record UI Representation
  slug: salesforce-get-record-ui-workflow
- description: Authenticate, read a specific contact by its contact key, then delete it.
  name: Salesforce Marketing Cloud Look Up and Remove a Contact
  slug: salesforce-mc-manage-contacts-workflow
- description: Authenticate, upsert rows into a Data Extension, then read the rows back.
  name: Salesforce Marketing Cloud Upsert and Read Data Extension Rows
  slug: salesforce-mc-manage-data-extension-workflow
- description: Authenticate, find a published journey, inspect it, then fire an entry event.
  name: Salesforce Marketing Cloud Enter a Contact into a Journey
  slug: salesforce-mc-manage-journey-workflow
- description: Authenticate, fire a triggered email send, then poll the recipient's send status.
  name: Salesforce Marketing Cloud Send a Triggered Email
  slug: salesforce-mc-send-triggered-email-workflow
- description: Run a SOQL query then page additional results via the queryMore token.
  name: Salesforce SOQL Query
  slug: salesforce-soql-query-workflow
- description: Run a SOSL full-text search across multiple SObjects in a single call.
  name: Salesforce SOSL Search
  slug: salesforce-sosl-search-workflow
- description: Update fields on an existing SObject record then read it back to confirm.
  name: Salesforce Update Record
  slug: salesforce-update-record-workflow
- description: Create or update an SObject record keyed on an external id field value.
  name: Salesforce Upsert by External Id
  slug: salesforce-upsert-by-external-id-workflow
artifact_total: 5737
asyncapis:
- description: Salesforce Change Data Capture (CDC) delivers change events that represent changes to Salesforce records including creates, updates, deletes, and undeletes. Subscribers receive rich change events with
  name: Salesforce Change Data Capture API
  slug: salesforce-change-data-capture-asyncapi
- description: Salesforce Platform Events enables event-driven integration architectures on the Salesforce platform. Developers define custom event types as Salesforce objects with the __e suffix and publish or subs
  name: Salesforce Platform Events API
  slug: salesforce-platform-events-asyncapi
- description: The Salesforce Streaming API uses a publish-subscribe model based on Bayeux/CometD to push near-real-time event notifications to subscribed clients. It supports PushTopic events (triggered by SOQL que
  name: Salesforce Streaming API
  slug: salesforce-streaming-asyncapi
collections:
- collection_type: postman
  name: Salesforce Bulk API 2.0
  slug: postman-salesforce-bulk-api-2
- collection_type: postman
  name: Salesforce Marketing Cloud REST API
  slug: postman-salesforce-marketing-cloud-rest
- collection_type: postman
  name: Salesforce REST API
  slug: postman-salesforce-rest-api
- collection_type: postman
  name: Salesforce UI API
  slug: postman-salesforce-ui-api
- collection_type: postman
  name: Salesforce
  slug: postman-salesforce
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort API
  slug: open-salesforce-abort-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Access API
  slug: open-salesforce-access-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Accounts API
  slug: open-salesforce-accounts-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Actions API
  slug: open-salesforce-actions-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Active API
  slug: open-salesforce-active-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Add API
  slug: open-salesforce-add-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Agent API
  slug: open-salesforce-agent-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort All API
  slug: open-salesforce-all-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Amend API
  slug: open-salesforce-amend-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Applications API
  slug: open-salesforce-applications-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort AppMenu API
  slug: open-salesforce-appmenu-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Appointment API
  slug: open-salesforce-appointment-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Approvals API
  slug: open-salesforce-approvals-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Assets API
  slug: open-salesforce-assets-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Async API
  slug: open-salesforce-async-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Authentication API
  slug: open-salesforce-authentication-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Authorize API
  slug: open-salesforce-authorize-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Based API
  slug: open-salesforce-based-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Basic API
  slug: open-salesforce-basic-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Batch API
  slug: open-salesforce-batch-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Benefits API
  slug: open-salesforce-benefits-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Blobs API
  slug: open-salesforce-blobs-api
- collection_type: open
  name: Salesforce Bulk API 2.0
  slug: open-salesforce-bulk-api-2
- collection_type: open
  name: Salesforce API 2.0 Abort Bulk API
  slug: open-salesforce-bulk-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Bundles API
  slug: open-salesforce-bundles-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Calculate API
  slug: open-salesforce-calculate-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Call API
  slug: open-salesforce-call-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Cancel API
  slug: open-salesforce-cancel-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Candidates API
  slug: open-salesforce-candidates-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Capability API
  slug: open-salesforce-capability-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Cart API
  slug: open-salesforce-cart-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Change API
  slug: open-salesforce-change-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Channel API
  slug: open-salesforce-channel-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Chart API
  slug: open-salesforce-chart-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Checks API
  slug: open-salesforce-checks-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Child API
  slug: open-salesforce-child-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Client API
  slug: open-salesforce-client-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Clone API
  slug: open-salesforce-clone-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Close API
  slug: open-salesforce-close-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Collections API
  slug: open-salesforce-collections-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Comments API
  slug: open-salesforce-comments-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Commitment API
  slug: open-salesforce-commitment-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Compact API
  slug: open-salesforce-compact-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Completion API
  slug: open-salesforce-completion-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Composite API
  slug: open-salesforce-composite-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Configuration API
  slug: open-salesforce-configuration-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Connect API
  slug: open-salesforce-connect-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Consent API
  slug: open-salesforce-consent-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Contacts API
  slug: open-salesforce-contacts-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Content API
  slug: open-salesforce-content-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Conversation API
  slug: open-salesforce-conversation-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Corporate API
  slug: open-salesforce-corporate-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Count API
  slug: open-salesforce-count-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Create API
  slug: open-salesforce-create-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Creation API
  slug: open-salesforce-creation-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Credential API
  slug: open-salesforce-credential-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Credentials API
  slug: open-salesforce-credentials-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Custom API
  slug: open-salesforce-custom-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Data API
  slug: open-salesforce-data-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Data Extensions API
  slug: open-salesforce-data-extensions-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Decision API
  slug: open-salesforce-decision-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Definition API
  slug: open-salesforce-definition-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Definitions API
  slug: open-salesforce-definitions-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Deletes API
  slug: open-salesforce-deletes-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Dependencies API
  slug: open-salesforce-dependencies-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Describe API
  slug: open-salesforce-describe-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Detail API
  slug: open-salesforce-detail-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Developer API
  slug: open-salesforce-developer-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Directories API
  slug: open-salesforce-directories-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Discovery API
  slug: open-salesforce-discovery-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Download API
  slug: open-salesforce-download-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Dynamic API
  slug: open-salesforce-dynamic-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Edit API
  slug: open-salesforce-edit-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Element API
  slug: open-salesforce-element-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Elements API
  slug: open-salesforce-elements-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Eligible API
  slug: open-salesforce-eligible-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Endpoint API
  slug: open-salesforce-endpoint-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Entries API
  slug: open-salesforce-entries-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Events API
  slug: open-salesforce-events-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Exchange API
  slug: open-salesforce-exchange-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Execution API
  slug: open-salesforce-execution-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Exit API
  slug: open-salesforce-exit-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Exports API
  slug: open-salesforce-exports-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Expression API
  slug: open-salesforce-expression-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort External API
  slug: open-salesforce-external-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Failed API
  slug: open-salesforce-failed-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Favorite API
  slug: open-salesforce-favorite-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Feed API
  slug: open-salesforce-feed-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Feedback API
  slug: open-salesforce-feedback-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Field API
  slug: open-salesforce-field-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Files API
  slug: open-salesforce-files-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Flow API
  slug: open-salesforce-flow-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Following API
  slug: open-salesforce-following-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Game API
  slug: open-salesforce-game-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Games API
  slug: open-salesforce-games-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort General API
  slug: open-salesforce-general-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Generate API
  slug: open-salesforce-generate-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Get API
  slug: open-salesforce-get-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Gift API
  slug: open-salesforce-gift-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Gifts API
  slug: open-salesforce-gifts-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Global API
  slug: open-salesforce-global-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Graph API
  slug: open-salesforce-graph-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Groups API
  slug: open-salesforce-groups-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort History API
  slug: open-salesforce-history-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Identifiers API
  slug: open-salesforce-identifiers-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Image API
  slug: open-salesforce-image-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Individual API
  slug: open-salesforce-individual-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Info API
  slug: open-salesforce-info-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Information API
  slug: open-salesforce-information-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Ingest Job Data API
  slug: open-salesforce-ingest-job-data-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Ingest Jobs API
  slug: open-salesforce-ingest-jobs-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Initialize API
  slug: open-salesforce-initialize-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Initiate API
  slug: open-salesforce-initiate-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Instant API
  slug: open-salesforce-instant-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Integration API
  slug: open-salesforce-integration-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Invites API
  slug: open-salesforce-invites-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Invoke API
  slug: open-salesforce-invoke-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Item API
  slug: open-salesforce-item-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Items API
  slug: open-salesforce-items-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Jobs API
  slug: open-salesforce-jobs-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Journals API
  slug: open-salesforce-journals-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Journeys API
  slug: open-salesforce-journeys-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Keys API
  slug: open-salesforce-keys-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Knowledge API
  slug: open-salesforce-knowledge-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Language API
  slug: open-salesforce-language-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Last API
  slug: open-salesforce-last-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Launch API
  slug: open-salesforce-launch-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Layout API
  slug: open-salesforce-layout-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Layouts API
  slug: open-salesforce-layouts-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Lightning API
  slug: open-salesforce-lightning-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Limits API
  slug: open-salesforce-limits-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Link API
  slug: open-salesforce-link-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort List Views API
  slug: open-salesforce-list-views-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Lists API
  slug: open-salesforce-lists-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Loader API
  slug: open-salesforce-loader-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Login API
  slug: open-salesforce-login-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Logs API
  slug: open-salesforce-logs-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Lookups API
  slug: open-salesforce-lookups-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Managed API
  slug: open-salesforce-managed-api
- collection_type: open
  name: Salesforce Marketing Cloud REST API
  slug: open-salesforce-marketing-cloud-rest
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Member API
  slug: open-salesforce-member-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Members API
  slug: open-salesforce-members-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Memberships API
  slug: open-salesforce-memberships-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Messages API
  slug: open-salesforce-messages-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Messaging API
  slug: open-salesforce-messaging-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Method API
  slug: open-salesforce-method-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Metrics API
  slug: open-salesforce-metrics-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Models API
  slug: open-salesforce-models-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Multiple API
  slug: open-salesforce-multiple-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Named API
  slug: open-salesforce-named-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Names API
  slug: open-salesforce-names-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Navigation API
  slug: open-salesforce-navigation-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort News API
  slug: open-salesforce-news-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Notation API
  slug: open-salesforce-notation-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Oauth API
  slug: open-salesforce-oauth-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Object Info API
  slug: open-salesforce-object-info-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Objects API
  slug: open-salesforce-objects-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Order API
  slug: open-salesforce-order-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Pages API
  slug: open-salesforce-pages-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Parallel API
  slug: open-salesforce-parallel-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Password API
  slug: open-salesforce-password-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Payments API
  slug: open-salesforce-payments-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Personalized API
  slug: open-salesforce-personalized-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Photo API
  slug: open-salesforce-photo-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Picklists API
  slug: open-salesforce-picklists-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Platform API
  slug: open-salesforce-platform-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Post API
  slug: open-salesforce-post-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Predict API
  slug: open-salesforce-predict-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Prices API
  slug: open-salesforce-prices-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Procedure API
  slug: open-salesforce-procedure-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Process API
  slug: open-salesforce-process-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Product API
  slug: open-salesforce-product-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Profile API
  slug: open-salesforce-profile-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Promotion API
  slug: open-salesforce-promotion-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Promotions API
  slug: open-salesforce-promotions-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Prompts API
  slug: open-salesforce-prompts-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Publish API
  slug: open-salesforce-publish-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Quantity API
  slug: open-salesforce-quantity-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Queries API
  slug: open-salesforce-queries-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Query API
  slug: open-salesforce-query-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Query Job Results API
  slug: open-salesforce-query-job-results-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Query Jobs API
  slug: open-salesforce-query-jobs-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort QueryAll API
  slug: open-salesforce-queryall-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Quote API
  slug: open-salesforce-quote-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Read API
  slug: open-salesforce-read-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Recent API
  slug: open-salesforce-recent-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Recently API
  slug: open-salesforce-recently-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Record API
  slug: open-salesforce-record-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Records API
  slug: open-salesforce-records-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Redeem API
  slug: open-salesforce-redeem-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Refresh API
  slug: open-salesforce-refresh-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Registration API
  slug: open-salesforce-registration-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Related API
  slug: open-salesforce-related-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Relationships API
  slug: open-salesforce-relationships-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Relay API
  slug: open-salesforce-relay-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Relevant API
  slug: open-salesforce-relevant-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Requests API
  slug: open-salesforce-requests-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Resources API
  slug: open-salesforce-resources-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Response API
  slug: open-salesforce-response-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Rest API
  slug: open-salesforce-rest-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Result API
  slug: open-salesforce-result-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Results API
  slug: open-salesforce-results-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Retrieves API
  slug: open-salesforce-retrieves-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Revoke API
  slug: open-salesforce-revoke-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Reward API
  slug: open-salesforce-reward-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Rows API
  slug: open-salesforce-rows-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Rules API
  slug: open-salesforce-rules-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Runs API
  slug: open-salesforce-runs-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Sale API
  slug: open-salesforce-sale-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Sandbox API
  slug: open-salesforce-sandbox-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Save API
  slug: open-salesforce-save-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Schedules API
  slug: open-salesforce-schedules-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Scheduling API
  slug: open-salesforce-scheduling-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Schema API
  slug: open-salesforce-schema-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Scope API
  slug: open-salesforce-scope-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Search API
  slug: open-salesforce-search-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Selected API
  slug: open-salesforce-selected-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Self API
  slug: open-salesforce-self-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Sets API
  slug: open-salesforce-sets-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Settings API
  slug: open-salesforce-settings-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Shares API
  slug: open-salesforce-shares-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Single API
  slug: open-salesforce-single-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Slots API
  slug: open-salesforce-slots-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Soap API
  slug: open-salesforce-soap-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort SObjects API
  slug: open-salesforce-sobjects-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Spec API
  slug: open-salesforce-spec-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Standard API
  slug: open-salesforce-standard-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort State API
  slug: open-salesforce-state-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Status API
  slug: open-salesforce-status-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Submit API
  slug: open-salesforce-submit-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Subscriptions API
  slug: open-salesforce-subscriptions-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Suggested API
  slug: open-salesforce-suggested-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Suggestions API
  slug: open-salesforce-suggestions-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Summaries API
  slug: open-salesforce-summaries-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Supported API
  slug: open-salesforce-supported-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Sync API
  slug: open-salesforce-sync-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Table API
  slug: open-salesforce-table-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Tables API
  slug: open-salesforce-tables-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Tabs API
  slug: open-salesforce-tabs-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Templates API
  slug: open-salesforce-templates-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Tests API
  slug: open-salesforce-tests-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Text API
  slug: open-salesforce-text-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Theme API
  slug: open-salesforce-theme-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Themes API
  slug: open-salesforce-themes-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Toggle API
  slug: open-salesforce-toggle-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Tokens API
  slug: open-salesforce-tokens-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Transaction API
  slug: open-salesforce-transaction-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Trees API
  slug: open-salesforce-trees-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Type API
  slug: open-salesforce-type-api
- collection_type: open
  name: Salesforce UI API
  slug: open-salesforce-ui-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Undelete API
  slug: open-salesforce-undelete-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Update API
  slug: open-salesforce-update-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Upload API
  slug: open-salesforce-upload-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Usage API
  slug: open-salesforce-usage-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Users API
  slug: open-salesforce-users-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Values API
  slug: open-salesforce-values-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Versions API
  slug: open-salesforce-versions-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort View API
  slug: open-salesforce-view-api
- collection_type: open
  name: Salesforce Bulk API 2.0 Abort Views API
  slug: open-salesforce-views-api
- collection_type: open
  name: Salesforce
  slug: open-salesforce
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/salesforce-capability-edges.yml
- group: build
  title: ''
  type: SDKs
  url: packages/salesforce-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/salesforce-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/salesforce-rate-limits.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/salesforce-lifecycle.yml
- group: auth
  title: ''
  type: Compliance
  url: security/salesforce-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/salesforce-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/salesforce-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/salesforce-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salesforce-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/salesforce-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/salesforce-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/salesforce-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/salesforce-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/salesforce-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/salesforce-llms.txt
- group: other
  title: ''
  type: Protobuf
  url: grpc/salesforce-pubsub-api.proto
- group: design
  title: ''
  type: Conformance
  url: conformance/salesforce-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/salesforce-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/salesforce-lifecycle.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/salesforce-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/salesforce-trust-center.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/salesforce-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/salesforce-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/salesforce-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/salesforce-cli.yml
- group: design
  title: ''
  type: Components
  url: components/salesforce-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/salesforce-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/salesforce-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/salesforce-rest-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/salesforce-bulk-api-2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/salesforce-ui-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/salesforce-marketing-cloud-rest-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/salesforce/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-bulk-delete-records-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-bulk-insert-records-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-bulk-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-bulk-upsert-records-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-create-account-with-contacts-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-create-case-for-contact-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-create-lead-and-convert-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-create-opportunity-with-contact-role-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-create-record-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-delete-record-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-describe-sobject-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-get-list-view-records-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-get-org-limits-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-get-picklist-values-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-get-record-ui-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-mc-manage-contacts-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-mc-manage-data-extension-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-mc-manage-journey-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-mc-send-triggered-email-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-soql-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-sosl-search-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-update-record-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-upsert-by-external-id-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.salesforce.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.salesforce.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://trailhead.salesforce.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.salesforce.com/
- group: operate
  title: ''
  type: Support
  url: https://help.salesforce.com/
- group: operate
  title: ''
  type: Community
  url: https://trailblazers.salesforce.com/
- group: auth
  title: ''
  type: Authentication
  url: https://help.salesforce.com/s/articleView?id=sf.remoteaccess_authenticate.htm
- group: docs
  title: ''
  type: OAuth Documentation
  url: https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_flows.htm
- group: design
  title: ''
  type: API Versions
  url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/dome_versions.htm
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/salesforce-developers/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/salesforce
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.salesforce.com/company/legal/agreements/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.salesforce.com/company/privacy/
- group: start
  title: ''
  type: Signup
  url: https://login.salesforce.com/
- group: start
  title: ''
  type: Signup
  url: https://developer.salesforce.com/signup
- group: start
  title: ''
  type: Console
  url: https://login.salesforce.com/
- group: other
  title: ''
  type: Marketplace
  url: https://appexchange.salesforce.com/
- group: company
  title: ''
  type: Blog
  url: https://developer.salesforce.com/blogs/
- group: build
  title: ''
  type: SDKs
  url: https://developer.salesforce.com/tools/salesforcecli
- group: build
  title: ''
  type: SDKs
  url: https://developer.salesforce.com/tools/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.salesforce.com/release-notes/
- group: operate
  title: ''
  type: StackOverflow
  url: https://salesforce.stackexchange.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.salesforce.com/pricing/
- group: other
  title: ''
  type: X
  url: https://twitter.com/salesforcedevs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/salesforce-developers
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@salesforcedevelopers
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm
- group: auth
  title: ''
  type: Security
  url: https://security.salesforce.com/security-advisories
- group: auth
  title: ''
  type: Security
  url: https://developer.salesforce.com/developer-centers/security
- group: auth
  title: ''
  type: Security
  url: https://developer.salesforce.com/docs/atlas.en-us.secure_coding_guide.meta/secure_coding_guide/secure_coding_guidelines.htm
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://help.salesforce.com/s/articleView?id=release-notes.salesforce_release_notes.htm&language=en_US
- group: other
  title: ''
  type: Events
  url: https://www.salesforce.com/events/
- group: other
  title: ''
  type: Events
  url: https://www.salesforce.com/dreamforce/
- group: start
  title: ''
  type: Portal
  url: https://developer.salesforce.com/developer-centers/integration-apis
- group: build
  title: ''
  type: API Library
  url: https://developer.salesforce.com/docs/apis
- group: start
  title: ''
  type: Portal
  url: https://developer.salesforce.com/developer-centers/mobile
- group: design
  title: ''
  type: JSONLD
  url: json-ld/salesforce-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/salesforce-sobject-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/salesforce-query-result-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/salesforce-bulk-job-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/salesforce-rest-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/salesforce-bulk-2-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/salesforce-ui-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/salesforce-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/salesforce-vocabulary.yaml
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/airkit/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/buddy-media/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/cimulate/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/clockwise/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/convergence/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/demandware/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/exact-target/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/heroku/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/informatica/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/mulesoft/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/own-ownbackup/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/pardot/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/regrello/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/salesforce-automation/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/salesforce-commerce-cloud/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/salesforce-experience-cloud/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/salesforce-sales-cloud/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/slack/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/spiff/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/spindle-technologies/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/steelbrick/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/tableau/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/vlocity/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/zoomin/
created: '2025-06-05'
description: Salesforce is a cloud-based customer relationship management (CRM) platform that provides a comprehensive suite of enterprise applications for sales, service, marketing, commerce, analytics and AI. Its Lightning Platform exposes REST, SOAP, Bulk 2.0, Streaming, GraphQL, Metadata, Tooling and gRPC Pub/Sub APIs, alongside the Agentforce agent and models APIs, letting developers query, write and subscribe to org data programmatically.
examples:
- key_count: 3
  name: Salesforce 0 F94 H000000 Uf2X Sag Example
  slug: salesforce-0-f94-h000000-uf2x-sag-example
- key_count: 3
  name: Salesforce 00 B58000002Ssin Eaa Example
  slug: salesforce-00-b58000002ssin-eaa-example
- key_count: 11
  name: Salesforce 00 Qb0000003P O Qs Mam Example
  slug: salesforce-00-qb0000003p-o-qs-mam-example
- key_count: 11
  name: Salesforce 00 Qb0000003P Ordma2 Example
  slug: salesforce-00-qb0000003p-ordma2-example
- key_count: 3
  name: Salesforce 0014 H00002 Lb R7 Qqav Example
  slug: salesforce-0014-h00002-lb-r7-qqav-example
- key_count: 3
  name: Salesforce 0014 H00002 Lb R7 Qqav1 Example
  slug: salesforce-0014-h00002-lb-r7-qqav1-example
- key_count: 3
  name: Salesforce 00158000006 Qb Oh Aao Example
  slug: salesforce-00158000006-qb-oh-aao-example
- key_count: 3
  name: Salesforce 00158000006 Qb Oh Aao1 Example
  slug: salesforce-00158000006-qb-oh-aao1-example
- key_count: 3
  name: Salesforce 00158000006 Qb Oh Aao2 Example
  slug: salesforce-00158000006-qb-oh-aao2-example
- key_count: 3
  name: Salesforce 00358000006Woxw Aaa Example
  slug: salesforce-00358000006woxw-aaa-example
- key_count: 2
  name: Salesforce 00H B0000000 Jr Bria0 Example
  slug: salesforce-00h-b0000000-jr-bria0-example
- key_count: 2
  name: Salesforce 01 Bb0000002R P3 Imau Example
  slug: salesforce-01-bb0000002r-p3-imau-example
- key_count: 2
  name: Salesforce 01 Bb0000002R P3 Jmau Example
  slug: salesforce-01-bb0000002r-p3-jmau-example
- key_count: 2
  name: Salesforce 01 Bb0000002R P3 Lmau Example
  slug: salesforce-01-bb0000002r-p3-lmau-example
- key_count: 2
  name: Salesforce 01 Bb0000002R P3 Mmau Example
  slug: salesforce-01-bb0000002r-p3-mmau-example
- key_count: 2
  name: Salesforce 01 Bb0000002R P3 Nmau Example
  slug: salesforce-01-bb0000002r-p3-nmau-example
- key_count: 1
  name: Salesforce 012000000000000 Aaa Example
  slug: salesforce-012000000000000-aaa-example
- key_count: 5
  name: Salesforce 012000000000000 Aaa1 Example
  slug: salesforce-012000000000000-aaa1-example
- key_count: 2
  name: Salesforce 404 Because Version59.0 Not Present In Target Org1 Example
  slug: salesforce-404-because-version59.0-not-present-in-target-org1-example
- key_count: 10
  name: Salesforce Aborta Job Query Example
  slug: salesforce-aborta-job-query-example
- key_count: 1
  name: Salesforce Aborta Job Query Request Example
  slug: salesforce-aborta-job-query-request-example
- key_count: 31
  name: Salesforce About Me Example
  slug: salesforce-about-me-example
- key_count: 19
  name: Salesforce Access Records Example
  slug: salesforce-access-records-example
- key_count: 6
  name: Salesforce Account Brand Example
  slug: salesforce-account-brand-example
- key_count: 1
  name: Salesforce Account Create Example
  slug: salesforce-account-create-example
- key_count: 2
  name: Salesforce Account Custom Field Example
  slug: salesforce-account-custom-field-example
- key_count: 1
  name: Salesforce Account Delete Example
  slug: salesforce-account-delete-example
- key_count: 2
  name: Salesforce Account Example
  slug: salesforce-account-example
- key_count: 6
  name: Salesforce Account History Example
  slug: salesforce-account-history-example
- key_count: 2
  name: Salesforce Account Number Example
  slug: salesforce-account-number-example
- key_count: 31
  name: Salesforce Account Number1 Example
  slug: salesforce-account-number1-example
- key_count: 2
  name: Salesforce Account Number2 Example
  slug: salesforce-account-number2-example
- key_count: 2
  name: Salesforce Account Number4 Example
  slug: salesforce-account-number4-example
- key_count: 6
  name: Salesforce Account Partner Example
  slug: salesforce-account-partner-example
- key_count: 3
  name: Salesforce Account S Object Example
  slug: salesforce-account-s-object-example
- key_count: 2
  name: Salesforce Account Source Example
  slug: salesforce-account-source-example
- key_count: 31
  name: Salesforce Account Source1 Example
  slug: salesforce-account-source1-example
- key_count: 1
  name: Salesforce Account Update Example
  slug: salesforce-account-update-example
- key_count: 3
  name: Salesforce Account10 Example
  slug: salesforce-account10-example
- key_count: 1
  name: Salesforce Account11 Example
  slug: salesforce-account11-example
- key_count: 6
  name: Salesforce Account12 Example
  slug: salesforce-account12-example
- key_count: 23
  name: Salesforce Account13 Example
  slug: salesforce-account13-example
- key_count: 8
  name: Salesforce Account15 Example
  slug: salesforce-account15-example
- key_count: 4
  name: Salesforce Account16 Example
  slug: salesforce-account16-example
- key_count: 3
  name: Salesforce Account17 Example
  slug: salesforce-account17-example
- key_count: 3
  name: Salesforce Account18 Example
  slug: salesforce-account18-example
- key_count: 1
  name: Salesforce Account7 Example
  slug: salesforce-account7-example
- key_count: 2
  name: Salesforce Accounts Example
  slug: salesforce-accounts-example
- key_count: 2
  name: Salesforce Accountswith Cursors Pagination Example
  slug: salesforce-accountswith-cursors-pagination-example
- key_count: 2
  name: Salesforce Accountswith Filter Example
  slug: salesforce-accountswith-filter-example
- key_count: 1
  name: Salesforce Actions Example
  slug: salesforce-actions-example
- key_count: 19
  name: Salesforce Actions1 Example
  slug: salesforce-actions1-example
- key_count: 19
  name: Salesforce Actions10 Example
  slug: salesforce-actions10-example
- key_count: 1
  name: Salesforce Actions11 Example
  slug: salesforce-actions11-example
- key_count: 19
  name: Salesforce Actions12 Example
  slug: salesforce-actions12-example
- key_count: 1
  name: Salesforce Actions13 Example
  slug: salesforce-actions13-example
- key_count: 19
  name: Salesforce Actions14 Example
  slug: salesforce-actions14-example
- key_count: 1
  name: Salesforce Actions15 Example
  slug: salesforce-actions15-example
- key_count: 1
  name: Salesforce Actions17 Example
  slug: salesforce-actions17-example
- key_count: 19
  name: Salesforce Actions18 Example
  slug: salesforce-actions18-example
- key_count: 1
  name: Salesforce Actions19 Example
  slug: salesforce-actions19-example
- key_count: 2
  name: Salesforce Actions2 Example
  slug: salesforce-actions2-example
- key_count: 1
  name: Salesforce Actions21 Example
  slug: salesforce-actions21-example
- key_count: 19
  name: Salesforce Actions22 Example
  slug: salesforce-actions22-example
- key_count: 1
  name: Salesforce Actions23 Example
  slug: salesforce-actions23-example
- key_count: 19
  name: Salesforce Actions24 Example
  slug: salesforce-actions24-example
- key_count: 19
  name: Salesforce Actions3 Example
  slug: salesforce-actions3-example
- key_count: 1
  name: Salesforce Actions5 Example
  slug: salesforce-actions5-example
- key_count: 19
  name: Salesforce Actions6 Example
  slug: salesforce-actions6-example
- key_count: 1
  name: Salesforce Actions7 Example
  slug: salesforce-actions7-example
- key_count: 19
  name: Salesforce Actions8 Example
  slug: salesforce-actions8-example
- key_count: 1
  name: Salesforce Actions9 Example
  slug: salesforce-actions9-example
- key_count: 1
  name: Salesforce Activateable Example
  slug: salesforce-activateable-example
- key_count: 1
  name: Salesforce Active C Example
  slug: salesforce-active-c-example
- key_count: 31
  name: Salesforce Active C1 Example
  slug: salesforce-active-c1-example
- key_count: 2
  name: Salesforce Active C2 Example
  slug: salesforce-active-c2-example
- key_count: 2
  name: Salesforce Active C4 Example
  slug: salesforce-active-c4-example
- key_count: 6
  name: Salesforce Active Scratch Org Example
  slug: salesforce-active-scratch-org-example
- key_count: 6
  name: Salesforce Active Scratch Org History Example
  slug: salesforce-active-scratch-org-history-example
- key_count: 2
  name: Salesforce Active Scratch Orgs Example
  slug: salesforce-active-scratch-orgs-example
- key_count: 19
  name: Salesforce Actor Example
  slug: salesforce-actor-example
- key_count: 3
  name: Salesforce Addanitemtoacart Request Example
  slug: salesforce-addanitemtoacart-request-example
- key_count: 2
  name: Salesforce Addenrichedfieldstochannelmember Request Example
  slug: salesforce-addenrichedfieldstochannelmember-request-example
- key_count: 2
  name: Salesforce Addfilterexpressioninchannelmember Request Example
  slug: salesforce-addfilterexpressioninchannelmember-request-example
- key_count: 2
  name: Salesforce Additional Data Example
  slug: salesforce-additional-data-example
- key_count: 1
  name: Salesforce Additional Field Values Example
  slug: salesforce-additional-field-values-example
- key_count: 1
  name: Salesforce Additional Loyalty Member Currency Fields Example
  slug: salesforce-additional-loyalty-member-currency-fields-example
- key_count: 1
  name: Salesforce Additional Properties Example
  slug: salesforce-additional-properties-example
- key_count: 1
  name: Salesforce Address Example
  slug: salesforce-address-example
- key_count: 6
  name: Salesforce Address1 Example
  slug: salesforce-address1-example
- key_count: 31
  name: Salesforce Address5 Example
  slug: salesforce-address5-example
- key_count: 1
  name: Salesforce Aggregation Results Example
  slug: salesforce-aggregation-results-example
- key_count: 31
  name: Salesforce Alias Example
  slug: salesforce-alias-example
- key_count: 2
  name: Salesforce Alias4 Example
  slug: salesforce-alias4-example
- key_count: 2
  name: Salesforce Analytics External Data Size Mb Example
  slug: salesforce-analytics-external-data-size-mb-example
- key_count: 1
  name: Salesforce Annotation Example
  slug: salesforce-annotation-example
- key_count: 2
  name: Salesforce Annual Revenue Example
  slug: salesforce-annual-revenue-example
- key_count: 31
  name: Salesforce Annual Revenue1 Example
  slug: salesforce-annual-revenue1-example
- key_count: 2
  name: Salesforce Annual Revenue2 Example
  slug: salesforce-annual-revenue2-example
- key_count: 2
  name: Salesforce Annual Revenue3 Example
  slug: salesforce-annual-revenue3-example
- key_count: 6
  name: Salesforce Api Anomaly Event Store Example
  slug: salesforce-api-anomaly-event-store-example
- key_count: 6
  name: Salesforce App Analytics Query Request Example
  slug: salesforce-app-analytics-query-request-example
- key_count: 18
  name: Salesforce App Example
  slug: salesforce-app-example
- key_count: 3
  name: Salesforce App Menu Example
  slug: salesforce-app-menu-example
- key_count: 6
  name: Salesforce App Menu Item Example
  slug: salesforce-app-menu-item-example
- key_count: 1
  name: Salesforce Application Json Example
  slug: salesforce-application-json-example
- key_count: 1
  name: Salesforce Application Json1 Example
  slug: salesforce-application-json1-example
- key_count: 2
  name: Salesforce Applied Promotion Example
  slug: salesforce-applied-promotion-example
- key_count: 6
  name: Salesforce Asset Example
  slug: salesforce-asset-example
- key_count: 6
  name: Salesforce Asset History Example
  slug: salesforce-asset-history-example
- key_count: 6
  name: Salesforce Asset Relationship Example
  slug: salesforce-asset-relationship-example
- key_count: 6
  name: Salesforce Asset Relationship History Example
  slug: salesforce-asset-relationship-history-example
- key_count: 2
  name: Salesforce Assignment Example
  slug: salesforce-assignment-example
- key_count: 2
  name: Salesforce Assistant Name Example
  slug: salesforce-assistant-name-example
- key_count: 2
  name: Salesforce Assistant Phone Example
  slug: salesforce-assistant-phone-example
- key_count: 1
  name: Salesforce Associate Entity Type Example
  slug: salesforce-associate-entity-type-example
- key_count: 1
  name: Salesforce Associate Parent Entity Example
  slug: salesforce-associate-parent-entity-example
- key_count: 4
  name: Salesforce Associated Account Details Example
  slug: salesforce-associated-account-details-example
- key_count: 1
  name: Salesforce Associated Actions Example
  slug: salesforce-associated-actions-example
- key_count: 4
  name: Salesforce Associated Contact Details Example
  slug: salesforce-associated-contact-details-example
- key_count: 4
  name: Salesforce Associated Contact Example
  slug: salesforce-associated-contact-example
- key_count: 2
  name: Salesforce Attributes Example
  slug: salesforce-attributes-example
- key_count: 1
  name: Salesforce Attributes14 Example
  slug: salesforce-attributes14-example
- key_count: 2
  name: Salesforce Attributes15 Example
  slug: salesforce-attributes15-example
- key_count: 2
  name: Salesforce Attributes22 Example
  slug: salesforce-attributes22-example
- key_count: 3
  name: Salesforce Attributes29 Example
  slug: salesforce-attributes29-example
- key_count: 1
  name: Salesforce Attributes3 Example
  slug: salesforce-attributes3-example
- key_count: 2
  name: Salesforce Attributes35 Example
  slug: salesforce-attributes35-example
- key_count: 2
  name: Salesforce Attributes4 Example
  slug: salesforce-attributes4-example
- key_count: 3
  name: Salesforce Authorization Code Example
  slug: salesforce-authorization-code-example
- key_count: 6
  name: Salesforce Authorization Form Consent Example
  slug: salesforce-authorization-form-consent-example
- key_count: 6
  name: Salesforce Authorization Form Consent History Example
  slug: salesforce-authorization-form-consent-history-example
- key_count: 6
  name: Salesforce Authorization Form Data Use Example
  slug: salesforce-authorization-form-data-use-example
- key_count: 6
  name: Salesforce Authorization Form Data Use History Example
  slug: salesforce-authorization-form-data-use-history-example
- key_count: 6
  name: Salesforce Authorization Form Example
  slug: salesforce-authorization-form-example
- key_count: 6
  name: Salesforce Authorization Form History Example
  slug: salesforce-authorization-form-history-example
- key_count: 6
  name: Salesforce Authorization Form Text Example
  slug: salesforce-authorization-form-text-example
- key_count: 6
  name: Salesforce Authorization Form Text History Example
  slug: salesforce-authorization-form-text-history-example
- key_count: 6
  name: Salesforce Background Operation Example
  slug: salesforce-background-operation-example
- key_count: 31
  name: Salesforce Badge Text Example
  slug: salesforce-badge-text-example
- key_count: 3
  name: Salesforce Banner Photo Example
  slug: salesforce-banner-photo-example
- key_count: 10
  name: Salesforce Batch Info Example
  slug: salesforce-batch-info-example
- key_count: 1
  name: Salesforce Batch Info List Example
  slug: salesforce-batch-info-list-example
- key_count: 2
  name: Salesforce Batch Request Example
  slug: salesforce-batch-request-example
- key_count: 3
  name: Salesforce Bearer Auth Example
  slug: salesforce-bearer-auth-example
- key_count: 2
  name: Salesforce Billing Address Example
  slug: salesforce-billing-address-example
- key_count: 8
  name: Salesforce Billing Address1 Example
  slug: salesforce-billing-address1-example
- key_count: 31
  name: Salesforce Billing Address2 Example
  slug: salesforce-billing-address2-example
- key_count: 2
  name: Salesforce Billing City Example
  slug: salesforce-billing-city-example
- key_count: 31
  name: Salesforce Billing City1 Example
  slug: salesforce-billing-city1-example
- key_count: 2
  name: Salesforce Billing City2 Example
  slug: salesforce-billing-city2-example
- key_count: 2
  name: Salesforce Billing City3 Example
  slug: salesforce-billing-city3-example
- key_count: 2
  name: Salesforce Billing Country Example
  slug: salesforce-billing-country-example
- key_count: 31
  name: Salesforce Billing Country1 Example
  slug: salesforce-billing-country1-example
- key_count: 2
  name: Salesforce Billing Country2 Example
  slug: salesforce-billing-country2-example
- key_count: 2
  name: Salesforce Billing Country3 Example
  slug: salesforce-billing-country3-example
- key_count: 2
  name: Salesforce Billing Geocode Accuracy Example
  slug: salesforce-billing-geocode-accuracy-example
- key_count: 31
  name: Salesforce Billing Geocode Accuracy1 Example
  slug: salesforce-billing-geocode-accuracy1-example
- key_count: 2
  name: Salesforce Billing Latitude Example
  slug: salesforce-billing-latitude-example
- key_count: 31
  name: Salesforce Billing Latitude1 Example
  slug: salesforce-billing-latitude1-example
- key_count: 2
  name: Salesforce Billing Longitude Example
  slug: salesforce-billing-longitude-example
- key_count: 31
  name: Salesforce Billing Longitude1 Example
  slug: salesforce-billing-longitude1-example
- key_count: 2
  name: Salesforce Billing Postal Code Example
  slug: salesforce-billing-postal-code-example
- key_count: 31
  name: Salesforce Billing Postal Code1 Example
  slug: salesforce-billing-postal-code1-example
- key_count: 2
  name: Salesforce Billing Postal Code2 Example
  slug: salesforce-billing-postal-code2-example
- key_count: 2
  name: Salesforce Billing Postal Code3 Example
  slug: salesforce-billing-postal-code3-example
- key_count: 2
  name: Salesforce Billing State Example
  slug: salesforce-billing-state-example
- key_count: 31
  name: Salesforce Billing State1 Example
  slug: salesforce-billing-state1-example
- key_count: 2
  name: Salesforce Billing State2 Example
  slug: salesforce-billing-state2-example
- key_count: 2
  name: Salesforce Billing State3 Example
  slug: salesforce-billing-state3-example
- key_count: 2
  name: Salesforce Billing Street Example
  slug: salesforce-billing-street-example
- key_count: 31
  name: Salesforce Billing Street1 Example
  slug: salesforce-billing-street1-example
- key_count: 2
  name: Salesforce Billing Street2 Example
  slug: salesforce-billing-street2-example
- key_count: 2
  name: Salesforce Billing Street3 Example
  slug: salesforce-billing-street3-example
- key_count: 3
  name: Salesforce Birthdate Example
  slug: salesforce-birthdate-example
- key_count: 3
  name: Salesforce Body Example
  slug: salesforce-body-example
- key_count: 3
  name: Salesforce Body1 Example
  slug: salesforce-body1-example
- key_count: 3
  name: Salesforce Body11 Example
  slug: salesforce-body11-example
- key_count: 1
  name: Salesforce Body12 Example
  slug: salesforce-body12-example
- key_count: 3
  name: Salesforce Body14 Example
  slug: salesforce-body14-example
- key_count: 3
  name: Salesforce Body15 Example
  slug: salesforce-body15-example
- key_count: 1
  name: Salesforce Body16 Example
  slug: salesforce-body16-example
- key_count: 1
  name: Salesforce Body17 Example
  slug: salesforce-body17-example
- key_count: 1
  name: Salesforce Body18 Example
  slug: salesforce-body18-example
- key_count: 1
  name: Salesforce Body19 Example
  slug: salesforce-body19-example
- key_count: 2
  name: Salesforce Body2 Example
  slug: salesforce-body2-example
- key_count: 1
  name: Salesforce Body20 Example
  slug: salesforce-body20-example
- key_count: 1
  name: Salesforce Body21 Example
  slug: salesforce-body21-example
- key_count: 1
  name: Salesforce Body22 Example
  slug: salesforce-body22-example
- key_count: 1
  name: Salesforce Body23 Example
  slug: salesforce-body23-example
- key_count: 16
  name: Salesforce Body24 Example
  slug: salesforce-body24-example
- key_count: 23
  name: Salesforce Body25 Example
  slug: salesforce-body25-example
- key_count: 21
  name: Salesforce Body26 Example
  slug: salesforce-body26-example
- key_count: 3
  name: Salesforce Body4 Example
  slug: salesforce-body4-example
- key_count: 1
  name: Salesforce Body5 Example
  slug: salesforce-body5-example
- key_count: 3
  name: Salesforce Body6 Example
  slug: salesforce-body6-example
- key_count: 1
  name: Salesforce Body7 Example
  slug: salesforce-body7-example
- key_count: 1
  name: Salesforce Bookmarks Example
  slug: salesforce-bookmarks-example
- key_count: 3
  name: Salesforce Brand Image Example
  slug: salesforce-brand-image-example
- key_count: 3
  name: Salesforce Bulk 2 Error Example
  slug: salesforce-bulk-2-error-example
- key_count: 17
  name: Salesforce Bulk 2 Ingest Job Info Example
  slug: salesforce-bulk-2-ingest-job-info-example
- key_count: 7
  name: Salesforce Bulk 2 Ingest Job Request Example
  slug: salesforce-bulk-2-ingest-job-request-example
- key_count: 15
  name: Salesforce Bulk 2 Query Job Info Example
  slug: salesforce-bulk-2-query-job-info-example
- key_count: 5
  name: Salesforce Bulk 2 Query Job Request Example
  slug: salesforce-bulk-2-query-job-request-example
- key_count: 1
  name: Salesforce Bulk Close Job Request Example
  slug: salesforce-bulk-close-job-request-example
- key_count: 3
  name: Salesforce Bulk Create Job Request Example
  slug: salesforce-bulk-create-job-request-example
- key_count: 6
  name: Salesforce Business Brand Example
  slug: salesforce-business-brand-example
- key_count: 6
  name: Salesforce Business Hours Example
  slug: salesforce-business-hours-example
- key_count: 4
  name: Salesforce Calculate Price New Sale Bundles Request Example
  slug: salesforce-calculate-price-new-sale-bundles-request-example
- key_count: 3
  name: Salesforce Calculate Price New Sale Request Example
  slug: salesforce-calculate-price-new-sale-request-example
- key_count: 3
  name: Salesforce Calculate Price New Salewith Discounts Request Example
  slug: salesforce-calculate-price-new-salewith-discounts-request-example
- key_count: 3
  name: Salesforce Callout Options Example
  slug: salesforce-callout-options-example
- key_count: 1
  name: Salesforce Campaign Example
  slug: salesforce-campaign-example
- key_count: 6
  name: Salesforce Campaign History Example
  slug: salesforce-campaign-history-example
- key_count: 6
  name: Salesforce Campaign Member Example
  slug: salesforce-campaign-member-example
- key_count: 6
  name: Salesforce Campaign Member Status Example
  slug: salesforce-campaign-member-status-example
- key_count: 6
  name: Salesforce Campaign4 Example
  slug: salesforce-campaign4-example
- key_count: 1
  name: Salesforce Cancela Voucher Request Example
  slug: salesforce-cancela-voucher-request-example
- key_count: 12
  name: Salesforce Capabilities Example
  slug: salesforce-capabilities-example
- key_count: 1
  name: Salesforce Capabilities1 Example
  slug: salesforce-capabilities1-example
- key_count: 4
  name: Salesforce Capabilities6 Example
  slug: salesforce-capabilities6-example
- key_count: 4
  name: Salesforce Capabilities8 Example
  slug: salesforce-capabilities8-example
- key_count: 11
  name: Salesforce Card Payment Method Example
  slug: salesforce-card-payment-method-example
- key_count: 5
  name: Salesforce Cart Detail Example
  slug: salesforce-cart-detail-example
- key_count: 1
  name: Salesforce Cart Example
  slug: salesforce-cart-example
- key_count: 4
  name: Salesforce Cart Line Detail Example
  slug: salesforce-cart-line-detail-example
- key_count: 6
  name: Salesforce Case Comment Example
  slug: salesforce-case-comment-example
- key_count: 6
  name: Salesforce Case Contact Role Example
  slug: salesforce-case-contact-role-example
- key_count: 6
  name: Salesforce Case Example
  slug: salesforce-case-example
- key_count: 6
  name: Salesforce Case History Example
  slug: salesforce-case-history-example
- key_count: 1
  name: Salesforce Changeeventrelaystate Request Example
  slug: salesforce-changeeventrelaystate-request-example
- key_count: 6
  name: Salesforce Channel Program Example
  slug: salesforce-channel-program-example
- key_count: 6
  name: Salesforce Channel Program History Example
  slug: salesforce-channel-program-history-example
- key_count: 6
  name: Salesforce Channel Program Level Example
  slug: salesforce-channel-program-level-example
- key_count: 6
  name: Salesforce Channel Program Level History Example
  slug: salesforce-channel-program-level-history-example
- key_count: 2
  name: Salesforce Channel Program Level Name Example
  slug: salesforce-channel-program-level-name-example
- key_count: 31
  name: Salesforce Channel Program Level Name1 Example
  slug: salesforce-channel-program-level-name1-example
- key_count: 6
  name: Salesforce Channel Program Member Example
  slug: salesforce-channel-program-member-example
- key_count: 6
  name: Salesforce Channel Program Member History Example
  slug: salesforce-channel-program-member-history-example
- key_count: 2
  name: Salesforce Channel Program Name Example
  slug: salesforce-channel-program-name-example
- key_count: 31
  name: Salesforce Channel Program Name1 Example
  slug: salesforce-channel-program-name1-example
- key_count: 4
  name: Salesforce Chatter Likes Example
  slug: salesforce-chatter-likes-example
- key_count: 1
  name: Salesforce Child Accounts Example
  slug: salesforce-child-accounts-example
- key_count: 8
  name: Salesforce Child Relationship Example
  slug: salesforce-child-relationship-example
- key_count: 5
  name: Salesforce Child Relationship2 Example
  slug: salesforce-child-relationship2-example
- key_count: 31
  name: Salesforce City Example
  slug: salesforce-city-example
- key_count: 2
  name: Salesforce City2 Example
  slug: salesforce-city2-example
- key_count: 2
  name: Salesforce City3 Example
  slug: salesforce-city3-example
- key_count: 2
  name: Salesforce Clean Status Example
  slug: salesforce-clean-status-example
- key_count: 31
  name: Salesforce Clean Status2 Example
  slug: salesforce-clean-status2-example
- key_count: 5
  name: Salesforce Clean Status4 Example
  slug: salesforce-clean-status4-example
- key_count: 2
  name: Salesforce Client Info Example
  slug: salesforce-client-info-example
- key_count: 2
  name: Salesforce Close Date Example
  slug: salesforce-close-date-example
- key_count: 2
  name: Salesforce Close Example
  slug: salesforce-close-example
- key_count: 1
  name: Salesforce Closeor Aborta Job Request Example
  slug: salesforce-closeor-aborta-job-request-example
- key_count: 7
  name: Salesforce Code Coverage Example
  slug: salesforce-code-coverage-example
- key_count: 4
  name: Salesforce Code Coverage Warning Example
  slug: salesforce-code-coverage-warning-example
- key_count: 3
  name: Salesforce Color Example
  slug: salesforce-color-example
- key_count: 6
  name: Salesforce Column Wrap Example
  slug: salesforce-column-wrap-example
- key_count: 6
  name: Salesforce Comm Subscription Channel Type Example
  slug: salesforce-comm-subscription-channel-type-example
- key_count: 6
  name: Salesforce Comm Subscription Channel Type History Example
  slug: salesforce-comm-subscription-channel-type-history-example
- key_count: 6
  name: Salesforce Comm Subscription Example
  slug: salesforce-comm-subscription-example
- key_count: 6
  name: Salesforce Comm Subscription History Example
  slug: salesforce-comm-subscription-history-example
- key_count: 1
  name: Salesforce Comment Edit Request Example
  slug: salesforce-comment-edit-request-example
- key_count: 1
  name: Salesforce Comments Example
  slug: salesforce-comments-example
- key_count: 15
  name: Salesforce Commitment Example
  slug: salesforce-commitment-example
- key_count: 12
  name: Salesforce Commitment1 Example
  slug: salesforce-commitment1-example
- key_count: 31
  name: Salesforce Community Nickname Example
  slug: salesforce-community-nickname-example
- key_count: 31
  name: Salesforce Company Duns Number Example
  slug: salesforce-company-duns-number-example
- key_count: 31
  name: Salesforce Company Example
  slug: salesforce-company-example
- key_count: 31
  name: Salesforce Company Name Example
  slug: salesforce-company-name-example
- key_count: 2
  name: Salesforce Company1 Example
  slug: salesforce-company1-example
- key_count: 2
  name: Salesforce Components Example
  slug: salesforce-components-example
- key_count: 2
  name: Salesforce Composite Batch Request Example
  slug: salesforce-composite-batch-request-example
- key_count: 1
  name: Salesforce Composite Graph Request Example
  slug: salesforce-composite-graph-request-example
- key_count: 1
  name: Salesforce Composite Request Example
  slug: salesforce-composite-request-example
- key_count: 4
  name: Salesforce Composite Request1 Example
  slug: salesforce-composite-request1-example
- key_count: 4
  name: Salesforce Composite Request2 Example
  slug: salesforce-composite-request2-example
- key_count: 4
  name: Salesforce Composite Request3 Example
  slug: salesforce-composite-request3-example
- key_count: 4
  name: Salesforce Composite Request4 Example
  slug: salesforce-composite-request4-example
- key_count: 4
  name: Salesforce Composite Request5 Example
  slug: salesforce-composite-request5-example
- key_count: 4
  name: Salesforce Composite Request6 Example
  slug: salesforce-composite-request6-example
- key_count: 4
  name: Salesforce Composite Response Example
  slug: salesforce-composite-response-example
- key_count: 2
  name: Salesforce Concurrent Async Get Report Instances Example
  slug: salesforce-concurrent-async-get-report-instances-example
- key_count: 2
  name: Salesforce Concurrent Einstein Data Insights Story Creation Example
  slug: salesforce-concurrent-einstein-data-insights-story-creation-example
- key_count: 2
  name: Salesforce Concurrent Einstein Discovery Story Creation Example
  slug: salesforce-concurrent-einstein-discovery-story-creation-example
- key_count: 2
  name: Salesforce Concurrent Sync Report Runs Example
  slug: salesforce-concurrent-sync-report-runs-example
- key_count: 1
  name: Salesforce Condition Example
  slug: salesforce-condition-example
- key_count: 1
  name: Salesforce Conditions Example
  slug: salesforce-conditions-example
- key_count: 3
  name: Salesforce Conditions List Example
  slug: salesforce-conditions-list-example
- key_count: 2
  name: Salesforce Conditions List1 Example
  slug: salesforce-conditions-list1-example
- key_count: 7
  name: Salesforce Constructor Example
  slug: salesforce-constructor-example
- key_count: 6
  name: Salesforce Consumption Rate Example
  slug: salesforce-consumption-rate-example
- key_count: 6
  name: Salesforce Consumption Rate History Example
  slug: salesforce-consumption-rate-history-example
- key_count: 6
  name: Salesforce Consumption Schedule Example
  slug: salesforce-consumption-schedule-example
- key_count: 6
  name: Salesforce Consumption Schedule History Example
  slug: salesforce-consumption-schedule-history-example
- key_count: 1
  name: Salesforce Contact Example
  slug: salesforce-contact-example
- key_count: 6
  name: Salesforce Contact History Example
  slug: salesforce-contact-history-example
- key_count: 6
  name: Salesforce Contact Point Type Consent Example
  slug: salesforce-contact-point-type-consent-example
- key_count: 6
  name: Salesforce Contact Point Type Consent History Example
  slug: salesforce-contact-point-type-consent-history-example
- key_count: 6
  name: Salesforce Contact Request Example
  slug: salesforce-contact-request-example
- key_count: 3
  name: Salesforce Contact S Object Example
  slug: salesforce-contact-s-object-example
- key_count: 1
  name: Salesforce Contact2 Example
  slug: salesforce-contact2-example
- key_count: 6
  name: Salesforce Contact3 Example
  slug: salesforce-contact3-example
- key_count: 1
  name: Salesforce Contacts Example
  slug: salesforce-contacts-example
- key_count: 2
  name: Salesforce Contacts Ordered Example
  slug: salesforce-contacts-ordered-example
- key_count: 2
  name: Salesforce Contacts1 Example
  slug: salesforce-contacts1-example
- key_count: 2
  name: Salesforce Contactswith Account Name Example
  slug: salesforce-contactswith-account-name-example
- key_count: 6
  name: Salesforce Content Document Example
  slug: salesforce-content-document-example
- key_count: 6
  name: Salesforce Content Document History Example
  slug: salesforce-content-document-history-example
- key_count: 6
  name: Salesforce Content Document Link Example
  slug: salesforce-content-document-link-example
- key_count: 1
  name: Salesforce Content Example
  slug: salesforce-content-example
- key_count: 6
  name: Salesforce Content Version Example
  slug: salesforce-content-version-example
- key_count: 6
  name: Salesforce Content Version History Example
  slug: salesforce-content-version-history-example
- key_count: 6
  name: Salesforce Content Workspace Example
  slug: salesforce-content-workspace-example
- key_count: 1
  name: Salesforce Content1 Example
  slug: salesforce-content1-example
- key_count: 2
  name: Salesforce Context Example
  slug: salesforce-context-example
- key_count: 2
  name: Salesforce Context1 Example
  slug: salesforce-context1-example
- key_count: 2
  name: Salesforce Context2 Example
  slug: salesforce-context2-example
- key_count: 6
  name: Salesforce Contract Contact Role Example
  slug: salesforce-contract-contact-role-example
- key_count: 6
  name: Salesforce Contract Example
  slug: salesforce-contract-example
- key_count: 6
  name: Salesforce Contract History Example
  slug: salesforce-contract-history-example
- key_count: 1
  name: Salesforce Contract Renewer Api Request Example
  slug: salesforce-contract-renewer-api-request-example
- key_count: 7
  name: Salesforce Conversation Entry Example
  slug: salesforce-conversation-entry-example
- key_count: 31
  name: Salesforce Converted Date Example
  slug: salesforce-converted-date-example
- key_count: 5
  name: Salesforce Corporate Member Enrollments Example
  slug: salesforce-corporate-member-enrollments-example
- key_count: 5
  name: Salesforce Corporate Member Enrollments Request Example
  slug: salesforce-corporate-member-enrollments-request-example
- key_count: 31
  name: Salesforce Country Example
  slug: salesforce-country-example
- key_count: 2
  name: Salesforce Country2 Example
  slug: salesforce-country2-example
- key_count: 2
  name: Salesforce Create Account Success Example
  slug: salesforce-create-account-success-example
- key_count: 1
  name: Salesforce Create Asset From Order Request Example
  slug: salesforce-create-asset-from-order-request-example
- key_count: 9
  name: Salesforce Create Clone Sandbox Request Example
  slug: salesforce-create-clone-sandbox-request-example
- key_count: 2
  name: Salesforce Create Commitments Request Example
  slug: salesforce-create-commitments-request-example
- key_count: 5
  name: Salesforce Create Credential Request Example
  slug: salesforce-create-credential-request-example
- key_count: 2
  name: Salesforce Create Custom Example
  slug: salesforce-create-custom-example
- key_count: 1
  name: Salesforce Create Example
  slug: salesforce-create-example
- key_count: 5
  name: Salesforce Create External Credential Request Example
  slug: salesforce-create-external-credential-request-example
- key_count: 2
  name: Salesforce Create Gifts Request Example
  slug: salesforce-create-gifts-request-example
- key_count: 7
  name: Salesforce Create Named Credential Request Example
  slug: salesforce-create-named-credential-request-example
- key_count: 2
  name: Salesforce Create Order Evergreen Termed Request Example
  slug: salesforce-create-order-evergreen-termed-request-example
- key_count: 1
  name: Salesforce Create Order From Quote Request Example
  slug: salesforce-create-order-from-quote-request-example
- key_count: 2
  name: Salesforce Create Order One Time Request Example
  slug: salesforce-create-order-one-time-request-example
- key_count: 2
  name: Salesforce Create Order With Bundle Request Example
  slug: salesforce-create-order-with-bundle-request-example
- key_count: 5
  name: Salesforce Create Payment Method Request Example
  slug: salesforce-create-payment-method-request-example
- key_count: 2
  name: Salesforce Create Pledge Commitments Request Example
  slug: salesforce-create-pledge-commitments-request-example
- key_count: 5
  name: Salesforce Create Sandbox Example
  slug: salesforce-create-sandbox-example
- key_count: 8
  name: Salesforce Create Table Request Example
  slug: salesforce-create-table-request-example
- key_count: 4
  name: Salesforce Createa Favorite Request Example
  slug: salesforce-createa-favorite-request-example
- key_count: 11
  name: Salesforce Createa Favoritelistview Example
  slug: salesforce-createa-favoritelistview-example
- key_count: 11
  name: Salesforce Createa Record Example
  slug: salesforce-createa-record-example
- key_count: 3
  name: Salesforce Createa Record Request Example
  slug: salesforce-createa-record-request-example
- key_count: 1
  name: Salesforce Createable Example
  slug: salesforce-createable-example
- key_count: 2
  name: Salesforce Createand Save Quote Proposal Api Request Example
  slug: salesforce-createand-save-quote-proposal-api-request-example
- key_count: 2
  name: Salesforce Createchannel Request Example
  slug: salesforce-createchannel-request-example
- key_count: 2
  name: Salesforce Createchannel Request1 Example
  slug: salesforce-createchannel-request1-example
- key_count: 2
  name: Salesforce Createchannelmember Request Example
  slug: salesforce-createchannelmember-request-example
- key_count: 2
  name: Salesforce Createchannelmember Request1 Example
  slug: salesforce-createchannelmember-request1-example
- key_count: 3
  name: Salesforce Created By Example
  slug: salesforce-created-by-example
- key_count: 2
  name: Salesforce Created By3 Example
  slug: salesforce-created-by3-example
- key_count: 2
  name: Salesforce Created Date Example
  slug: salesforce-created-date-example
- key_count: 2
  name: Salesforce Created Date14 Example
  slug: salesforce-created-date14-example
- key_count: 31
  name: Salesforce Created Date2 Example
  slug: salesforce-created-date2-example
- key_count: 2
  name: Salesforce Created Date5 Example
  slug: salesforce-created-date5-example
- key_count: 2
  name: Salesforce Createeventrelay Request Example
  slug: salesforce-createeventrelay-request-example
- key_count: 2
  name: Salesforce Createjob Request Example
  slug: salesforce-createjob-request-example
- key_count: 2
  name: Salesforce Createmanagedeventsubscription Request Example
  slug: salesforce-createmanagedeventsubscription-request-example
- key_count: 2
  name: Salesforce Createnamedcredential Request1 Example
  slug: salesforce-createnamedcredential-request1-example
- key_count: 2
  name: Salesforce Createor Update Quote Request Example
  slug: salesforce-createor-update-quote-request-example
- key_count: 6
  name: Salesforce Credential Stuffing Event Store Example
  slug: salesforce-credential-stuffing-event-store-example
- key_count: 1
  name: Salesforce Credentials Example
  slug: salesforce-credentials-example
- key_count: 4
  name: Salesforce Credit Pointsto Members Example
  slug: salesforce-credit-pointsto-members-example
- key_count: 1
  name: Salesforce Credit Pointsto Members Request Example
  slug: salesforce-credit-pointsto-members-request-example
- key_count: 6
  name: Salesforce Csp Trusted Site Example
  slug: salesforce-csp-trusted-site-example
- key_count: 31
  name: Salesforce Current Generators C Example
  slug: salesforce-current-generators-c-example
- key_count: 2
  name: Salesforce Current Generators C1 Example
  slug: salesforce-current-generators-c1-example
- key_count: 1
  name: Salesforce Custom Example
  slug: salesforce-custom-example
- key_count: 3
  name: Salesforce Custom Header Example
  slug: salesforce-custom-header-example
- key_count: 4
  name: Salesforce Custom Header1 Example
  slug: salesforce-custom-header1-example
- key_count: 1
  name: Salesforce Custom Setting Example
  slug: salesforce-custom-setting-example
- key_count: 6
  name: Salesforce Customdata Example
  slug: salesforce-customdata-example
- key_count: 6
  name: Salesforce Customer Example
  slug: salesforce-customer-example
- key_count: 1
  name: Salesforce Customer Priority C Example
  slug: salesforce-customer-priority-c-example
- key_count: 31
  name: Salesforce Customer Priority C1 Example
  slug: salesforce-customer-priority-c1-example
- key_count: 2
  name: Salesforce Customer Priority C2 Example
  slug: salesforce-customer-priority-c2-example
- key_count: 2
  name: Salesforce Customer Priority C4 Example
  slug: salesforce-customer-priority-c4-example
- key_count: 2
  name: Salesforce Daily Analytics Dataflow Job Executions Example
  slug: salesforce-daily-analytics-dataflow-job-executions-example
- key_count: 2
  name: Salesforce Daily Analytics Uploaded Files Size Mb Example
  slug: salesforce-daily-analytics-uploaded-files-size-mb-example
- key_count: 2
  name: Salesforce Daily Api Requests Example
  slug: salesforce-daily-api-requests-example
- key_count: 2
  name: Salesforce Daily Async Apex Executions Example
  slug: salesforce-daily-async-apex-executions-example
- key_count: 2
  name: Salesforce Daily Async Apex Tests Example
  slug: salesforce-daily-async-apex-tests-example
- key_count: 2
  name: Salesforce Daily Bulk Api Batches Example
  slug: salesforce-daily-bulk-api-batches-example
- key_count: 2
  name: Salesforce Daily Bulk V2 Query File Storage Mb Example
  slug: salesforce-daily-bulk-v2-query-file-storage-mb-example
- key_count: 2
  name: Salesforce Daily Bulk V2 Query Jobs Example
  slug: salesforce-daily-bulk-v2-query-jobs-example
- key_count: 2
  name: Salesforce Daily Delivered Platform Events Example
  slug: salesforce-daily-delivered-platform-events-example
- key_count: 2
  name: Salesforce Daily Durable Generic Streaming Api Events Example
  slug: salesforce-daily-durable-generic-streaming-api-events-example
- key_count: 2
  name: Salesforce Daily Durable Streaming Api Events Example
  slug: salesforce-daily-durable-streaming-api-events-example
- key_count: 2
  name: Salesforce Daily Einstein Data Insights Story Creation Example
  slug: salesforce-daily-einstein-data-insights-story-creation-example
- key_count: 2
  name: Salesforce Daily Einstein Discovery Optimization Job Runs Example
  slug: salesforce-daily-einstein-discovery-optimization-job-runs-example
- key_count: 2
  name: Salesforce Daily Einstein Discovery Predict Api Calls Example
  slug: salesforce-daily-einstein-discovery-predict-api-calls-example
- key_count: 2
  name: Salesforce Daily Einstein Discovery Predictions By Cdc Example
  slug: salesforce-daily-einstein-discovery-predictions-by-cdc-example
- key_count: 2
  name: Salesforce Daily Einstein Discovery Story Creation Example
  slug: salesforce-daily-einstein-discovery-story-creation-example
- key_count: 2
  name: Salesforce Daily Functions Api Call Limit Example
  slug: salesforce-daily-functions-api-call-limit-example
- key_count: 2
  name: Salesforce Daily Generic Streaming Api Events Example
  slug: salesforce-daily-generic-streaming-api-events-example
- key_count: 2
  name: Salesforce Daily Scratch Orgs Example
  slug: salesforce-daily-scratch-orgs-example
- key_count: 2
  name: Salesforce Daily Standard Volume Platform Events Example
  slug: salesforce-daily-standard-volume-platform-events-example
- key_count: 2
  name: Salesforce Daily Streaming Api Events Example
  slug: salesforce-daily-streaming-api-events-example
- key_count: 6
  name: Salesforce Dand B Company Example
  slug: salesforce-dand-b-company-example
- key_count: 1
  name: Salesforce Data Example
  slug: salesforce-data-example
- key_count: 2
  name: Salesforce Data Storage Mb Example
  slug: salesforce-data-storage-mb-example
- key_count: 1
  name: Salesforce Data Translation Enabled Example
  slug: salesforce-data-translation-enabled-example
- key_count: 6
  name: Salesforce Data Use Legal Basis Example
  slug: salesforce-data-use-legal-basis-example
- key_count: 6
  name: Salesforce Data Use Legal Basis History Example
  slug: salesforce-data-use-legal-basis-history-example
- key_count: 6
  name: Salesforce Data Use Purpose Example
  slug: salesforce-data-use-purpose-example
- key_count: 6
  name: Salesforce Data Use Purpose History Example
  slug: salesforce-data-use-purpose-history-example
- key_count: 1
  name: Salesforce Data10 Example
  slug: salesforce-data10-example
- key_count: 1
  name: Salesforce Data11 Example
  slug: salesforce-data11-example
- key_count: 1
  name: Salesforce Data12 Example
  slug: salesforce-data12-example
- key_count: 1
  name: Salesforce Data13 Example
  slug: salesforce-data13-example
- key_count: 1
  name: Salesforce Data3 Example
  slug: salesforce-data3-example
- key_count: 1
  name: Salesforce Data4 Example
  slug: salesforce-data4-example
- key_count: 1
  name: Salesforce Data6 Example
  slug: salesforce-data6-example
- key_count: 1
  name: Salesforce Data7 Example
  slug: salesforce-data7-example
- key_count: 6
  name: Salesforce Dataweave Key Mapping Mdt Example
  slug: salesforce-dataweave-key-mapping-mdt-example
- key_count: 6
  name: Salesforce Dataweave Mapping Mdt Example
  slug: salesforce-dataweave-mapping-mdt-example
- key_count: 4
  name: Salesforce Debit Pointsfrom Members Example
  slug: salesforce-debit-pointsfrom-members-example
- key_count: 1
  name: Salesforce Debit Pointsfrom Members Request Example
  slug: salesforce-debit-pointsfrom-members-request-example
- key_count: 1
  name: Salesforce Decision Model Notation Export Request Example
  slug: salesforce-decision-model-notation-export-request-example
- key_count: 3
  name: Salesforce Decision Table Example
  slug: salesforce-decision-table-example
- key_count: 9
  name: Salesforce Decision Table1 Example
  slug: salesforce-decision-table1-example
- key_count: 1
  name: Salesforce Deep Cloneable Example
  slug: salesforce-deep-cloneable-example
- key_count: 1
  name: Salesforce Default Group Banner Example
  slug: salesforce-default-group-banner-example
- key_count: 3
  name: Salesforce Default Group Image Example
  slug: salesforce-default-group-image-example
- key_count: 31
  name: Salesforce Default Group Notification Frequency Example
  slug: salesforce-default-group-notification-frequency-example
- key_count: 1
  name: Salesforce Default Page Banner Example
  slug: salesforce-default-page-banner-example
- key_count: 1
  name: Salesforce Default User Banner Example
  slug: salesforce-default-user-banner-example
- key_count: 3
  name: Salesforce Default User Image Example
  slug: salesforce-default-user-image-example
- key_count: 6
  name: Salesforce Delegated Account Example
  slug: salesforce-delegated-account-example
- key_count: 6
  name: Salesforce Delegated Account History Example
  slug: salesforce-delegated-account-history-example
- key_count: 1
  name: Salesforce Deletable Example
  slug: salesforce-deletable-example
- key_count: 2
  name: Salesforce Delete Account Example
  slug: salesforce-delete-account-example
- key_count: 3
  name: Salesforce Delete Credential Request Example
  slug: salesforce-delete-credential-request-example
- key_count: 6
  name: Salesforce Delete Event Example
  slug: salesforce-delete-event-example
- key_count: 2
  name: Salesforce Department Example
  slug: salesforce-department-example
- key_count: 31
  name: Salesforce Department1 Example
  slug: salesforce-department1-example
- key_count: 1
  name: Salesforce Describe Metadata Example
  slug: salesforce-describe-metadata-example
- key_count: 1
  name: Salesforce Describe Metadata Response Example
  slug: salesforce-describe-metadata-response-example
- key_count: 1
  name: Salesforce Describe Value Type Example
  slug: salesforce-describe-value-type-example
- key_count: 1
  name: Salesforce Describe Value Type Response Example
  slug: salesforce-describe-value-type-response-example
- key_count: 45
  name: Salesforce Describeeventchannel Example
  slug: salesforce-describeeventchannel-example
- key_count: 2
  name: Salesforce Description3 Example
  slug: salesforce-description3-example
- key_count: 31
  name: Salesforce Description5 Example
  slug: salesforce-description5-example
- key_count: 2
  name: Salesforce Description6 Example
  slug: salesforce-description6-example
- key_count: 3
  name: Salesforce Designation Example
  slug: salesforce-designation-example
- key_count: 2
  name: Salesforce Designation1 Example
  slug: salesforce-designation1-example
- key_count: 2
  name: Salesforce Detail Example
  slug: salesforce-detail-example
- key_count: 3
  name: Salesforce Detail1 Example
  slug: salesforce-detail1-example
- key_count: 2
  name: Salesforce Detail10 Example
  slug: salesforce-detail10-example
- key_count: 2
  name: Salesforce Detail13 Example
  slug: salesforce-detail13-example
- key_count: 3
  name: Salesforce Detail14 Example
  slug: salesforce-detail14-example
- key_count: 2
  name: Salesforce Detail3 Example
  slug: salesforce-detail3-example
- key_count: 3
  name: Salesforce Detail4 Example
  slug: salesforce-detail4-example
- key_count: 2
  name: Salesforce Detail7 Example
  slug: salesforce-detail7-example
- key_count: 2
  name: Salesforce Detail8 Example
  slug: salesforce-detail8-example
- key_count: 31
  name: Salesforce Developer Name Example
  slug: salesforce-developer-name-example
- key_count: 31
  name: Salesforce Digest Frequency Example
  slug: salesforce-digest-frequency-example
- key_count: 2
  name: Salesforce Disambiguation Field Example
  slug: salesforce-disambiguation-field-example
- key_count: 6
  name: Salesforce Display Column Example
  slug: salesforce-display-column-example
- key_count: 31
  name: Salesforce Division Example
  slug: salesforce-division-example
- key_count: 31
  name: Salesforce Does Include Bosses Example
  slug: salesforce-does-include-bosses-example
- key_count: 9
  name: Salesforce Donor Example
  slug: salesforce-donor-example
- key_count: 1
  name: Salesforce Donor Options Example
  slug: salesforce-donor-options-example
- key_count: 8
  name: Salesforce Donor1 Example
  slug: salesforce-donor1-example
- key_count: 8
  name: Salesforce Donor3 Example
  slug: salesforce-donor3-example
- key_count: 2
  name: Salesforce Duns Number Example
  slug: salesforce-duns-number-example
- key_count: 31
  name: Salesforce Duns Number1 Example
  slug: salesforce-duns-number1-example
- key_count: 6
  name: Salesforce Duplicate Record Item Example
  slug: salesforce-duplicate-record-item-example
- key_count: 6
  name: Salesforce Duplicate Record Set Example
  slug: salesforce-duplicate-record-set-example
- key_count: 2
  name: Salesforce Durable Streaming Api Concurrent Clients Example
  slug: salesforce-durable-streaming-api-concurrent-clients-example
- key_count: 1
  name: Salesforce Edge Example
  slug: salesforce-edge-example
- key_count: 1
  name: Salesforce Edge10 Example
  slug: salesforce-edge10-example
- key_count: 1
  name: Salesforce Edge6 Example
  slug: salesforce-edge6-example
- key_count: 1
  name: Salesforce Edge7 Example
  slug: salesforce-edge7-example
- key_count: 6
  name: Salesforce Edit Example
  slug: salesforce-edit-example
- key_count: 6
  name: Salesforce Edit6 Example
  slug: salesforce-edit6-example
- key_count: 3
  name: Salesforce Eligible Channel Example
  slug: salesforce-eligible-channel-example
- key_count: 2
  name: Salesforce Eligible Customer Events Example
  slug: salesforce-eligible-customer-events-example
- key_count: 3
  name: Salesforce Eligible Enrollment Period Example
  slug: salesforce-eligible-enrollment-period-example
- key_count: 2
  name: Salesforce Eligible Loyalty Tier Example
  slug: salesforce-eligible-loyalty-tier-example
- key_count: 1
  name: Salesforce Eligible Product Category Example
  slug: salesforce-eligible-product-category-example
- key_count: 1
  name: Salesforce Eligible Product Example
  slug: salesforce-eligible-product-example
- key_count: 1
  name: Salesforce Eligible Promotions Request Example
  slug: salesforce-eligible-promotions-request-example
- key_count: 31
  name: Salesforce Employee Number Example
  slug: salesforce-employee-number-example
- key_count: 6
  name: Salesforce Engagement Channel Type Example
  slug: salesforce-engagement-channel-type-example
- key_count: 6
  name: Salesforce Engagement Channel Type History Example
  slug: salesforce-engagement-channel-type-history-example
- key_count: 1
  name: Salesforce Enriched Field Example
  slug: salesforce-enriched-field-example
- key_count: 1
  name: Salesforce Enrollfor Promotions Request Example
  slug: salesforce-enrollfor-promotions-request-example
- key_count: 19
  name: Salesforce Entity Example
  slug: salesforce-entity-example
- key_count: 2
  name: Salesforce Entity Label Example
  slug: salesforce-entity-label-example
- key_count: 2
  name: Salesforce Envelope Example
  slug: salesforce-envelope-example
- key_count: 2
  name: Salesforce Envelope1 Example
  slug: salesforce-envelope1-example
- key_count: 1
  name: Salesforce Envelope2 Example
  slug: salesforce-envelope2-example
- key_count: 2
  name: Salesforce Envelope3 Example
  slug: salesforce-envelope3-example
- key_count: 1
  name: Salesforce Envelope4 Example
  slug: salesforce-envelope4-example
- key_count: 2
  name: Salesforce Envelope5 Example
  slug: salesforce-envelope5-example
- key_count: 1
  name: Salesforce Envelope6 Example
  slug: salesforce-envelope6-example
- key_count: 2
  name: Salesforce Envelope7 Example
  slug: salesforce-envelope7-example
- key_count: 1
  name: Salesforce Error Code Example
  slug: salesforce-error-code-example
- key_count: 3
  name: Salesforce Error Example
  slug: salesforce-error-example
- key_count: 2
  name: Salesforce Error Info Example
  slug: salesforce-error-info-example
- key_count: 2
  name: Salesforce Errors Example
  slug: salesforce-errors-example
- key_count: 2
  name: Salesforce Errors12 Example
  slug: salesforce-errors12-example
- key_count: 1
  name: Salesforce Errors5 Example
  slug: salesforce-errors5-example
- key_count: 3
  name: Salesforce Errors7 Example
  slug: salesforce-errors7-example
- key_count: 5
  name: Salesforce Expression Set Creation Request Example
  slug: salesforce-expression-set-creation-request-example
- key_count: 2
  name: Salesforce Expression Set Invocation Request Example
  slug: salesforce-expression-set-invocation-request-example
- key_count: 5
  name: Salesforce Expression Set Update Request Example
  slug: salesforce-expression-set-update-request-example
- key_count: 2
  name: Salesforce Extended Details Example
  slug: salesforce-extended-details-example
- key_count: 1
  name: Salesforce Extended Error Code Example
  slug: salesforce-extended-error-code-example
- key_count: 2
  name: Salesforce Extended Error Details Example
  slug: salesforce-extended-error-details-example
- key_count: 2
  name: Salesforce Extended Error Details1 Example
  slug: salesforce-extended-error-details1-example
- key_count: 31
  name: Salesforce Extension Example
  slug: salesforce-extension-example
- key_count: 11
  name: Salesforce External Credential Example
  slug: salesforce-external-credential-example
- key_count: 4
  name: Salesforce External Credential1 Example
  slug: salesforce-external-credential1-example
- key_count: 1
  name: Salesforce External Credential2 Example
  slug: salesforce-external-credential2-example
- key_count: 11
  name: Salesforce Favorite Example
  slug: salesforce-favorite-example
- key_count: 2
  name: Salesforce Favorite1 Example
  slug: salesforce-favorite1-example
- key_count: 2
  name: Salesforce Fax Example
  slug: salesforce-fax-example
- key_count: 31
  name: Salesforce Fax2 Example
  slug: salesforce-fax2-example
- key_count: 2
  name: Salesforce Fax4 Example
  slug: salesforce-fax4-example
- key_count: 2
  name: Salesforce Fax5 Example
  slug: salesforce-fax5-example
- key_count: 2
  name: Salesforce Feed Element Example
  slug: salesforce-feed-element-example
- key_count: 1
  name: Salesforce Feed Elements Batch Post Request Example
  slug: salesforce-feed-elements-batch-post-request-example
- key_count: 18
  name: Salesforce Feed Elements Capability Comments Items Example
  slug: salesforce-feed-elements-capability-comments-items-example
- key_count: 4
  name: Salesforce Feed Elements Postand Search Request Example
  slug: salesforce-feed-elements-postand-search-request-example
- key_count: 1
  name: Salesforce Feed Enabled Example
  slug: salesforce-feed-enabled-example
- key_count: 3
  name: Salesforce Field Example
  slug: salesforce-field-example
- key_count: 1
  name: Salesforce Field Mapping List Example
  slug: salesforce-field-mapping-list-example
- key_count: 57
  name: Salesforce Field1 Example
  slug: salesforce-field1-example
- key_count: 2
  name: Salesforce Field2 Example
  slug: salesforce-field2-example
- key_count: 2
  name: Salesforce Field3 Example
  slug: salesforce-field3-example
- key_count: 4
  name: Salesforce Field4 Example
  slug: salesforce-field4-example
- key_count: 4
  name: Salesforce Field5 Example
  slug: salesforce-field5-example
- key_count: 57
  name: Salesforce Field9 Example
  slug: salesforce-field9-example
- key_count: 2
  name: Salesforce Fields Example
  slug: salesforce-fields-example
- key_count: 35
  name: Salesforce Fields11 Example
  slug: salesforce-fields11-example
- key_count: 70
  name: Salesforce Fields15 Example
  slug: salesforce-fields15-example
- key_count: 3
  name: Salesforce Fields16 Example
  slug: salesforce-fields16-example
- key_count: 2
  name: Salesforce Fields17 Example
  slug: salesforce-fields17-example
- key_count: 17
  name: Salesforce Fields18 Example
  slug: salesforce-fields18-example
- key_count: 57
  name: Salesforce Fields2 Example
  slug: salesforce-fields2-example
- key_count: 1
  name: Salesforce Fields20 Example
  slug: salesforce-fields20-example
- key_count: 42
  name: Salesforce Fields21 Example
  slug: salesforce-fields21-example
- key_count: 37
  name: Salesforce Fields27 Example
  slug: salesforce-fields27-example
- key_count: 14
  name: Salesforce Fields3 Example
  slug: salesforce-fields3-example
- key_count: 36
  name: Salesforce Fields31 Example
  slug: salesforce-fields31-example
- key_count: 3
  name: Salesforce Fields38 Example
  slug: salesforce-fields38-example
- key_count: 4
  name: Salesforce Fields39 Example
  slug: salesforce-fields39-example
- key_count: 60
  name: Salesforce Fields4 Example
  slug: salesforce-fields4-example
- key_count: 12
  name: Salesforce Fields40 Example
  slug: salesforce-fields40-example
- key_count: 7
  name: Salesforce Fields41 Example
  slug: salesforce-fields41-example
- key_count: 18
  name: Salesforce Fields5 Example
  slug: salesforce-fields5-example
- key_count: 196
  name: Salesforce Fields6 Example
  slug: salesforce-fields6-example
- key_count: 35
  name: Salesforce Fields7 Example
  slug: salesforce-fields7-example
- key_count: 2
  name: Salesforce Fields8 Example
  slug: salesforce-fields8-example
- key_count: 48
  name: Salesforce File Information Example
  slug: salesforce-file-information-example
- key_count: 2
  name: Salesforce File Storage Mb Example
  slug: salesforce-file-storage-mb-example
- key_count: 1
  name: Salesforce Files Example
  slug: salesforce-files-example
- key_count: 2
  name: Salesforce First Name Example
  slug: salesforce-first-name-example
- key_count: 31
  name: Salesforce First Name1 Example
  slug: salesforce-first-name1-example
- key_count: 2
  name: Salesforce First Name4 Example
  slug: salesforce-first-name4-example
- key_count: 11
  name: Salesforce First Transaction Example
  slug: salesforce-first-transaction-example
- key_count: 6
  name: Salesforce Flow Interview Example
  slug: salesforce-flow-interview-example
- key_count: 6
  name: Salesforce Flow Orchestration Instance Example
  slug: salesforce-flow-orchestration-instance-example
- key_count: 6
  name: Salesforce Flow Orchestration Stage Instance Example
  slug: salesforce-flow-orchestration-stage-instance-example
- key_count: 6
  name: Salesforce Flow Orchestration Step Instance Example
  slug: salesforce-flow-orchestration-step-instance-example
- key_count: 6
  name: Salesforce Flow Orchestration Work Item Example
  slug: salesforce-flow-orchestration-work-item-example
- key_count: 3
  name: Salesforce Flows Example
  slug: salesforce-flows-example
- key_count: 31
  name: Salesforce Forecast Enabled Example
  slug: salesforce-forecast-enabled-example
- key_count: 3
  name: Salesforce Forgot Password Change Password Request Example
  slug: salesforce-forgot-password-change-password-request-example
- key_count: 2
  name: Salesforce Forgot Password Initialize Request Example
  slug: salesforce-forgot-password-initialize-request-example
- key_count: 1
  name: Salesforce Full Example
  slug: salesforce-full-example
- key_count: 1
  name: Salesforce Generate Open Api Schema Example
  slug: salesforce-generate-open-api-schema-example
- key_count: 2
  name: Salesforce Generate Quote Document Api Request Example
  slug: salesforce-generate-quote-document-api-request-example
- key_count: 5
  name: Salesforce Generate Response Basedon Prompt Template Example
  slug: salesforce-generate-response-basedon-prompt-template-example
- key_count: 6
  name: Salesforce Generated Data Example
  slug: salesforce-generated-data-example
- key_count: 3
  name: Salesforce Generation Example
  slug: salesforce-generation-example
- key_count: 31
  name: Salesforce Geocode Accuracy Example
  slug: salesforce-geocode-accuracy-example
- key_count: 11
  name: Salesforce Get Active Theme Example
  slug: salesforce-get-active-theme-example
- key_count: 4
  name: Salesforce Get All Navigation Items Example
  slug: salesforce-get-all-navigation-items-example
- key_count: 9
  name: Salesforce Get Appointment Slots Request Example
  slug: salesforce-get-appointment-slots-request-example
- key_count: 2
  name: Salesforce Get Apps Example
  slug: salesforce-get-apps-example
- key_count: 8
  name: Salesforce Get Child Records Example
  slug: salesforce-get-child-records-example
- key_count: 3
  name: Salesforce Get Default Valuesto Clonea Record Example
  slug: salesforce-get-default-valuesto-clonea-record-example
- key_count: 3
  name: Salesforce Get Default Valuesto Createa Record Example
  slug: salesforce-get-default-valuesto-createa-record-example
- key_count: 1
  name: Salesforce Get Example
  slug: salesforce-get-example
- key_count: 1
  name: Salesforce Get Favorites Example
  slug: salesforce-get-favorites-example
- key_count: 3
  name: Salesforce Get Global Actions Example
  slug: salesforce-get-global-actions-example
- key_count: 18
  name: Salesforce Get Last Selected App Example
  slug: salesforce-get-last-selected-app-example
- key_count: 3
  name: Salesforce Get Lightning Page Actions Example
  slug: salesforce-get-lightning-page-actions-example
- key_count: 3
  name: Salesforce Get List View Chart Actions Example
  slug: salesforce-get-list-view-chart-actions-example
- key_count: 3
  name: Salesforce Get List View Header Actions Example
  slug: salesforce-get-list-view-header-actions-example
- key_count: 18
  name: Salesforce Get List View Metadataby Api Name Example
  slug: salesforce-get-list-view-metadataby-api-name-example
- key_count: 3
  name: Salesforce Get List View Record Actions Example
  slug: salesforce-get-list-view-record-actions-example
- key_count: 16
  name: Salesforce Get List View Records Example
  slug: salesforce-get-list-view-records-example
- key_count: 5
  name: Salesforce Get List View Records Request Example
  slug: salesforce-get-list-view-records-request-example
- key_count: 16
  name: Salesforce Get List View Recordsper Api Name Example
  slug: salesforce-get-list-view-recordsper-api-name-example
- key_count: 12
  name: Salesforce Get List Viewsforan Object Example
  slug: salesforce-get-list-viewsforan-object-example
- key_count: 3
  name: Salesforce Get Lookup Field Actions Example
  slug: salesforce-get-lookup-field-actions-example
- key_count: 2
  name: Salesforce Get Lookup Field Suggestions Example
  slug: salesforce-get-lookup-field-suggestions-example
- key_count: 8
  name: Salesforce Get Lookup Field Suggestionsfora Specified Object Example
  slug: salesforce-get-lookup-field-suggestionsfora-specified-object-example
- key_count: 1
  name: Salesforce Get Member Promotions Request Example
  slug: salesforce-get-member-promotions-request-example
- key_count: 3
  name: Salesforce Get Mru List View Actions Example
  slug: salesforce-get-mru-list-view-actions-example
- key_count: 23
  name: Salesforce Get Object Metadata Example
  slug: salesforce-get-object-metadata-example
- key_count: 3
  name: Salesforce Get Parallel Resultsfora Query Job Example
  slug: salesforce-get-parallel-resultsfora-query-job-example
- key_count: 3
  name: Salesforce Get Photo Actions Example
  slug: salesforce-get-photo-actions-example
- key_count: 5
  name: Salesforce Get Record Dataand Object Metadata Example
  slug: salesforce-get-record-dataand-object-metadata-example
- key_count: 3
  name: Salesforce Get Record Detail Page Actions Example
  slug: salesforce-get-record-detail-page-actions-example
- key_count: 3
  name: Salesforce Get Record Edit Page Actions Example
  slug: salesforce-get-record-edit-page-actions-example
- key_count: 8
  name: Salesforce Get Record Layout Metadata Example
  slug: salesforce-get-record-layout-metadata-example
- key_count: 3
  name: Salesforce Get Related List Actions Example
  slug: salesforce-get-related-list-actions-example
- key_count: 3
  name: Salesforce Get Related List Record Actions Example
  slug: salesforce-get-related-list-record-actions-example
- key_count: 17
  name: Salesforce Get Sandbox Example
  slug: salesforce-get-sandbox-example
- key_count: 6
  name: Salesforce Get Sandbox Status Example
  slug: salesforce-get-sandbox-status-example
- key_count: 3
  name: Salesforce Get Tooling Describe Example
  slug: salesforce-get-tooling-describe-example
- key_count: 45
  name: Salesforce Get Tooling Describe S Object Example
  slug: salesforce-get-tooling-describe-s-object-example
- key_count: 2
  name: Salesforce Get Tooling Metadata S Object Example
  slug: salesforce-get-tooling-metadata-s-object-example
- key_count: 2
  name: Salesforce Get Valuesfor All Picklist Fieldsofa Record Type Example
  slug: salesforce-get-valuesfor-all-picklist-fieldsofa-record-type-example
- key_count: 5
  name: Salesforce Get Valuesfora Picklist Field Example
  slug: salesforce-get-valuesfora-picklist-field-example
- key_count: 2
  name: Salesforce Geta Batchof Records Example
  slug: salesforce-geta-batchof-records-example
- key_count: 1
  name: Salesforce Geta Directoryof Supported Objects Example
  slug: salesforce-geta-directoryof-supported-objects-example
- key_count: 11
  name: Salesforce Geta Favorite Example
  slug: salesforce-geta-favorite-example
- key_count: 11
  name: Salesforce Geta Record Example
  slug: salesforce-geta-record-example
- key_count: 6
  name: Salesforce Getallmanagedeventsubscriptions Example
  slug: salesforce-getallmanagedeventsubscriptions-example
- key_count: 18
  name: Salesforce Getan App Example
  slug: salesforce-getan-app-example
- key_count: 18
  name: Salesforce Getchannelmember Example
  slug: salesforce-getchannelmember-example
- key_count: 1
  name: Salesforce Getconversationentries Example
  slug: salesforce-getconversationentries-example
- key_count: 16
  name: Salesforce Geteventchannel Example
  slug: salesforce-geteventchannel-example
- key_count: 5
  name: Salesforce Gettestresults Example
  slug: salesforce-gettestresults-example
- key_count: 2
  name: Salesforce Getteststatus Example
  slug: salesforce-getteststatus-example
- key_count: 2
  name: Salesforce Gift Commitment Custom Field Example
  slug: salesforce-gift-commitment-custom-field-example
- key_count: 2
  name: Salesforce Gift Commitment Schedule Custom Field Example
  slug: salesforce-gift-commitment-schedule-custom-field-example
- key_count: 20
  name: Salesforce Gift Example
  slug: salesforce-gift-example
- key_count: 2
  name: Salesforce Gift Transaction Custom Field Example
  slug: salesforce-gift-transaction-custom-field-example
- key_count: 2
  name: Salesforce Giftcommitment Example
  slug: salesforce-giftcommitment-example
- key_count: 2
  name: Salesforce Giftcommitmentschedule Example
  slug: salesforce-giftcommitmentschedule-example
- key_count: 2
  name: Salesforce Giftdefaultdesignation Example
  slug: salesforce-giftdefaultdesignation-example
- key_count: 2
  name: Salesforce Gifttransaction Example
  slug: salesforce-gifttransaction-example
- key_count: 2
  name: Salesforce Gifttransactiondesignation Example
  slug: salesforce-gifttransactiondesignation-example
- key_count: 3
  name: Salesforce Global Example
  slug: salesforce-global-example
- key_count: 2
  name: Salesforce Graph Example
  slug: salesforce-graph-example
- key_count: 1
  name: Salesforce Graph Response Example
  slug: salesforce-graph-response-example
- key_count: 3
  name: Salesforce Graph1 Example
  slug: salesforce-graph1-example
- key_count: 2
  name: Salesforce Graph2 Example
  slug: salesforce-graph2-example
- key_count: 2
  name: Salesforce Graph3 Example
  slug: salesforce-graph3-example
- key_count: 2
  name: Salesforce Graph4 Example
  slug: salesforce-graph4-example
- key_count: 2
  name: Salesforce Graph5 Example
  slug: salesforce-graph5-example
- key_count: 25
  name: Salesforce Group Example
  slug: salesforce-group-example
- key_count: 2
  name: Salesforce Group Invites Request Example
  slug: salesforce-group-invites-request-example
- key_count: 8
  name: Salesforce Group Members Private Post Example
  slug: salesforce-group-members-private-post-example
- key_count: 23
  name: Salesforce Group1 Example
  slug: salesforce-group1-example
- key_count: 6
  name: Salesforce Group2 Example
  slug: salesforce-group2-example
- key_count: 1
  name: Salesforce Has Subtypes Example
  slug: salesforce-has-subtypes-example
- key_count: 3
  name: Salesforce Header Example
  slug: salesforce-header-example
- key_count: 1
  name: Salesforce Header4 Example
  slug: salesforce-header4-example
- key_count: 1
  name: Salesforce Header5 Example
  slug: salesforce-header5-example
- key_count: 1
  name: Salesforce Header8 Example
  slug: salesforce-header8-example
- key_count: 2
  name: Salesforce Home Phone Example
  slug: salesforce-home-phone-example
- key_count: 1
  name: Salesforce Http Headers Example
  slug: salesforce-http-headers-example
- key_count: 5
  name: Salesforce Icon Example
  slug: salesforce-icon-example
- key_count: 6
  name: Salesforce Image Example
  slug: salesforce-image-example
- key_count: 6
  name: Salesforce Image History Example
  slug: salesforce-image-history-example
- key_count: 2
  name: Salesforce Implicit Example
  slug: salesforce-implicit-example
- key_count: 2
  name: Salesforce Industry Example
  slug: salesforce-industry-example
- key_count: 31
  name: Salesforce Industry1 Example
  slug: salesforce-industry1-example
- key_count: 2
  name: Salesforce Industry2 Example
  slug: salesforce-industry2-example
- key_count: 2
  name: Salesforce Industry3 Example
  slug: salesforce-industry3-example
- key_count: 3
  name: Salesforce Info Example
  slug: salesforce-info-example
- key_count: 2
  name: Salesforce Information Example
  slug: salesforce-information-example
- key_count: 2
  name: Salesforce Infos Example
  slug: salesforce-infos-example
- key_count: 4
  name: Salesforce Initiate Amend Quantity Request Example
  slug: salesforce-initiate-amend-quantity-request-example
- key_count: 3
  name: Salesforce Initiate Cancellation Request Example
  slug: salesforce-initiate-cancellation-request-example
- key_count: 1
  name: Salesforce Initiate Renewal Request Example
  slug: salesforce-initiate-renewal-request-example
- key_count: 1
  name: Salesforce Input Example
  slug: salesforce-input-example
- key_count: 1
  name: Salesforce Input1 Example
  slug: salesforce-input1-example
- key_count: 2
  name: Salesforce Input2 Example
  slug: salesforce-input2-example
- key_count: 3
  name: Salesforce Inputs Example
  slug: salesforce-inputs-example
- key_count: 1
  name: Salesforce Inputs1 Example
  slug: salesforce-inputs1-example
- key_count: 1
  name: Salesforce Inputs2 Example
  slug: salesforce-inputs2-example
- key_count: 1
  name: Salesforce Inputs3 Example
  slug: salesforce-inputs3-example
- key_count: 1
  name: Salesforce Interactions Example
  slug: salesforce-interactions-example
- key_count: 1
  name: Salesforce Invitees Example
  slug: salesforce-invitees-example
- key_count: 2
  name: Salesforce Invoke Request Example
  slug: salesforce-invoke-request-example
- key_count: 6
  name: Salesforce Ip Address Range Example
  slug: salesforce-ip-address-range-example
- key_count: 31
  name: Salesforce Is Active Example
  slug: salesforce-is-active-example
- key_count: 31
  name: Salesforce Is Converted Example
  slug: salesforce-is-converted-example
- key_count: 2
  name: Salesforce Is Customer Portal Example
  slug: salesforce-is-customer-portal-example
- key_count: 31
  name: Salesforce Is Customer Portal1 Example
  slug: salesforce-is-customer-portal1-example
- key_count: 2
  name: Salesforce Is Deleted Example
  slug: salesforce-is-deleted-example
- key_count: 31
  name: Salesforce Is Deleted2 Example
  slug: salesforce-is-deleted2-example
- key_count: 31
  name: Salesforce Is Ext Indicator Visible Example
  slug: salesforce-is-ext-indicator-visible-example
- key_count: 1
  name: Salesforce Is Interface Example
  slug: salesforce-is-interface-example
- key_count: 2
  name: Salesforce Is Partner Example
  slug: salesforce-is-partner-example
- key_count: 31
  name: Salesforce Is Partner1 Example
  slug: salesforce-is-partner1-example
- key_count: 31
  name: Salesforce Is Portal Enabled Example
  slug: salesforce-is-portal-enabled-example
- key_count: 31
  name: Salesforce Is Profile Photo Active Example
  slug: salesforce-is-profile-photo-active-example
- key_count: 1
  name: Salesforce Is Subtype Example
  slug: salesforce-is-subtype-example
- key_count: 31
  name: Salesforce Is Unread By Owner Example
  slug: salesforce-is-unread-by-owner-example
- key_count: 1
  name: Salesforce Issuea Voucher Request Example
  slug: salesforce-issuea-voucher-request-example
- key_count: 1
  name: Salesforce Item Example
  slug: salesforce-item-example
- key_count: 1
  name: Salesforce Items Example
  slug: salesforce-items-example
- key_count: 2
  name: Salesforce Items17 Example
  slug: salesforce-items17-example
- key_count: 1
  name: Salesforce Items18 Example
  slug: salesforce-items18-example
- key_count: 2
  name: Salesforce Items19 Example
  slug: salesforce-items19-example
- key_count: 2
  name: Salesforce Items20 Example
  slug: salesforce-items20-example
- key_count: 2
  name: Salesforce Items22 Example
  slug: salesforce-items22-example
- key_count: 2
  name: Salesforce Items23 Example
  slug: salesforce-items23-example
- key_count: 2
  name: Salesforce Jigsaw Example
  slug: salesforce-jigsaw-example
- key_count: 31
  name: Salesforce Jigsaw2 Example
  slug: salesforce-jigsaw2-example
- key_count: 3
  name: Salesforce Json Example
  slug: salesforce-json-example
- key_count: 6
  name: Salesforce Key Example
  slug: salesforce-key-example
- key_count: 1
  name: Salesforce Key Prefix Example
  slug: salesforce-key-prefix-example
- key_count: 1
  name: Salesforce Label Example
  slug: salesforce-label-example
- key_count: 1
  name: Salesforce Label Plural Example
  slug: salesforce-label-plural-example
- key_count: 31
  name: Salesforce Language Locale Key Example
  slug: salesforce-language-locale-key-example
- key_count: 3
  name: Salesforce Last Activity Date Example
  slug: salesforce-last-activity-date-example
- key_count: 31
  name: Salesforce Last Activity Date2 Example
  slug: salesforce-last-activity-date2-example
- key_count: 2
  name: Salesforce Last Cu Request Date Example
  slug: salesforce-last-cu-request-date-example
- key_count: 2
  name: Salesforce Last Cu Update Date Example
  slug: salesforce-last-cu-update-date-example
- key_count: 19
  name: Salesforce Last Edited By Example
  slug: salesforce-last-edited-by-example
- key_count: 31
  name: Salesforce Last Login Date Example
  slug: salesforce-last-login-date-example
- key_count: 3
  name: Salesforce Last Modified By Example
  slug: salesforce-last-modified-by-example
- key_count: 2
  name: Salesforce Last Modified By3 Example
  slug: salesforce-last-modified-by3-example
- key_count: 2
  name: Salesforce Last Modified Date Example
  slug: salesforce-last-modified-date-example
- key_count: 2
  name: Salesforce Last Modified Date14 Example
  slug: salesforce-last-modified-date14-example
- key_count: 31
  name: Salesforce Last Modified Date2 Example
  slug: salesforce-last-modified-date2-example
- key_count: 2
  name: Salesforce Last Modified Date5 Example
  slug: salesforce-last-modified-date5-example
- key_count: 2
  name: Salesforce Last Name Example
  slug: salesforce-last-name-example
- key_count: 31
  name: Salesforce Last Name1 Example
  slug: salesforce-last-name1-example
- key_count: 2
  name: Salesforce Last Name4 Example
  slug: salesforce-last-name4-example
- key_count: 31
  name: Salesforce Last Password Change Date Example
  slug: salesforce-last-password-change-date-example
- key_count: 3
  name: Salesforce Last Referenced Date Example
  slug: salesforce-last-referenced-date-example
- key_count: 31
  name: Salesforce Last Referenced Date2 Example
  slug: salesforce-last-referenced-date2-example
- key_count: 3
  name: Salesforce Last Viewed Date Example
  slug: salesforce-last-viewed-date-example
- key_count: 31
  name: Salesforce Last Viewed Date2 Example
  slug: salesforce-last-viewed-date2-example
- key_count: 31
  name: Salesforce Latitude Example
  slug: salesforce-latitude-example
- key_count: 1
  name: Salesforce Launch Flow Request Example
  slug: salesforce-launch-flow-request-example
- key_count: 3
  name: Salesforce Layout Component Example
  slug: salesforce-layout-component-example
- key_count: 5
  name: Salesforce Layout Component1 Example
  slug: salesforce-layout-component1-example
- key_count: 8
  name: Salesforce Layout Example
  slug: salesforce-layout-example
- key_count: 7
  name: Salesforce Layout Item Example
  slug: salesforce-layout-item-example
- key_count: 7
  name: Salesforce Layout Item1 Example
  slug: salesforce-layout-item1-example
- key_count: 1
  name: Salesforce Layout Row Example
  slug: salesforce-layout-row-example
- key_count: 1
  name: Salesforce Layout Row1 Example
  slug: salesforce-layout-row1-example
- key_count: 1
  name: Salesforce Layout User States Example
  slug: salesforce-layout-user-states-example
- key_count: 8
  name: Salesforce Layout1 Example
  slug: salesforce-layout1-example
- key_count: 1
  name: Salesforce Layoutable Example
  slug: salesforce-layoutable-example
- key_count: 1
  name: Salesforce Layouts Example
  slug: salesforce-layouts-example
- key_count: 1
  name: Salesforce Lead Example
  slug: salesforce-lead-example
- key_count: 6
  name: Salesforce Lead History Example
  slug: salesforce-lead-history-example
- key_count: 2
  name: Salesforce Lead Source Example
  slug: salesforce-lead-source-example
- key_count: 31
  name: Salesforce Lead Source1 Example
  slug: salesforce-lead-source1-example
- key_count: 2
  name: Salesforce Lead Source2 Example
  slug: salesforce-lead-source2-example
- key_count: 5
  name: Salesforce Lead Source4 Example
  slug: salesforce-lead-source4-example
- key_count: 23
  name: Salesforce Lead1 Example
  slug: salesforce-lead1-example
- key_count: 6
  name: Salesforce Lead2 Example
  slug: salesforce-lead2-example
- key_count: 5
  name: Salesforce Level C Example
  slug: salesforce-level-c-example
- key_count: 8
  name: Salesforce Likes Example
  slug: salesforce-likes-example
- key_count: 52
  name: Salesforce Limits Example
  slug: salesforce-limits-example
- key_count: 5
  name: Salesforce Links Example
  slug: salesforce-links-example
- key_count: 2
  name: Salesforce Links11 Example
  slug: salesforce-links11-example
- key_count: 2
  name: Salesforce Links13 Example
  slug: salesforce-links13-example
- key_count: 1
  name: Salesforce Links3 Example
  slug: salesforce-links3-example
- key_count: 6
  name: Salesforce Links7 Example
  slug: salesforce-links7-example
- key_count: 4
  name: Salesforce Links9 Example
  slug: salesforce-links9-example
- key_count: 4
  name: Salesforce List Example
  slug: salesforce-list-example
- key_count: 2
  name: Salesforce List Metadata Example
  slug: salesforce-list-metadata-example
- key_count: 2
  name: Salesforce List Metadata Query Example
  slug: salesforce-list-metadata-query-example
- key_count: 1
  name: Salesforce List Metadata Response Example
  slug: salesforce-list-metadata-response-example
- key_count: 4
  name: Salesforce List Reference Example
  slug: salesforce-list-reference-example
- key_count: 6
  name: Salesforce List Sandboxes Example
  slug: salesforce-list-sandboxes-example
- key_count: 3
  name: Salesforce List View Chart Instance Example
  slug: salesforce-list-view-chart-instance-example
- key_count: 6
  name: Salesforce Listchannelmembers Example
  slug: salesforce-listchannelmembers-example
- key_count: 6
  name: Salesforce Listeventchannels Example
  slug: salesforce-listeventchannels-example
- key_count: 6
  name: Salesforce Listnamedcredentials Example
  slug: salesforce-listnamedcredentials-example
- key_count: 2
  name: Salesforce Location Example
  slug: salesforce-location-example
- key_count: 31
  name: Salesforce Longitude Example
  slug: salesforce-longitude-example
- key_count: 1
  name: Salesforce Lookup Results Example
  slug: salesforce-lookup-results-example
- key_count: 2
  name: Salesforce Lookup Table Request Example
  slug: salesforce-lookup-table-request-example
- key_count: 1
  name: Salesforce Lookup Table Request1 Example
  slug: salesforce-lookup-table-request1-example
- key_count: 1
  name: Salesforce Loyalty Program Currency Example
  slug: salesforce-loyalty-program-currency-example
- key_count: 1
  name: Salesforce Loyalty Program Example
  slug: salesforce-loyalty-program-example
- key_count: 2
  name: Salesforce M200 Example
  slug: salesforce-m200-example
- key_count: 2
  name: Salesforce M304 Example
  slug: salesforce-m304-example
- key_count: 6
  name: Salesforce Macro Example
  slug: salesforce-macro-example
- key_count: 6
  name: Salesforce Macro History Example
  slug: salesforce-macro-history-example
- key_count: 2
  name: Salesforce Mailing Address Example
  slug: salesforce-mailing-address-example
- key_count: 2
  name: Salesforce Mailing City Example
  slug: salesforce-mailing-city-example
- key_count: 2
  name: Salesforce Mailing Country Example
  slug: salesforce-mailing-country-example
- key_count: 2
  name: Salesforce Mailing Geocode Accuracy Example
  slug: salesforce-mailing-geocode-accuracy-example
- key_count: 5
  name: Salesforce Mailing Geocode Accuracy1 Example
  slug: salesforce-mailing-geocode-accuracy1-example
- key_count: 2
  name: Salesforce Mailing Latitude Example
  slug: salesforce-mailing-latitude-example
- key_count: 2
  name: Salesforce Mailing Longitude Example
  slug: salesforce-mailing-longitude-example
- key_count: 2
  name: Salesforce Mailing Postal Code Example
  slug: salesforce-mailing-postal-code-example
- key_count: 2
  name: Salesforce Mailing State Example
  slug: salesforce-mailing-state-example
- key_count: 2
  name: Salesforce Mailing Street Example
  slug: salesforce-mailing-street-example
- key_count: 6
  name: Salesforce Managed Content Example
  slug: salesforce-managed-content-example
- key_count: 6
  name: Salesforce Managed Content Variant Example
  slug: salesforce-managed-content-variant-example
- key_count: 1
  name: Salesforce Match Billing Address C Example
  slug: salesforce-match-billing-address-c-example
- key_count: 1
  name: Salesforce Member Benefits Example
  slug: salesforce-member-benefits-example
- key_count: 11
  name: Salesforce Member Benefits1 Example
  slug: salesforce-member-benefits1-example
- key_count: 20
  name: Salesforce Member Currency Example
  slug: salesforce-member-currency-example
- key_count: 24
  name: Salesforce Member Profile Example
  slug: salesforce-member-profile-example
- key_count: 12
  name: Salesforce Member Tier Example
  slug: salesforce-member-tier-example
- key_count: 2
  name: Salesforce Member Vouchers Example
  slug: salesforce-member-vouchers-example
- key_count: 6
  name: Salesforce Merchandise C Example
  slug: salesforce-merchandise-c-example
- key_count: 6
  name: Salesforce Merchandising Mix C Example
  slug: salesforce-merchandising-mix-c-example
- key_count: 1
  name: Salesforce Mergeable Example
  slug: salesforce-mergeable-example
- key_count: 1
  name: Salesforce Message Example
  slug: salesforce-message-example
- key_count: 2
  name: Salesforce Message Segment Example
  slug: salesforce-message-segment-example
- key_count: 4
  name: Salesforce Message Segment1 Example
  slug: salesforce-message-segment1-example
- key_count: 6
  name: Salesforce Message Segment11 Example
  slug: salesforce-message-segment11-example
- key_count: 4
  name: Salesforce Message Segment2 Example
  slug: salesforce-message-segment2-example
- key_count: 9
  name: Salesforce Message Segment3 Example
  slug: salesforce-message-segment3-example
- key_count: 4
  name: Salesforce Message Segment5 Example
  slug: salesforce-message-segment5-example
- key_count: 2
  name: Salesforce Metadata Example
  slug: salesforce-metadata-example
- key_count: 6
  name: Salesforce Metadata Objects Example
  slug: salesforce-metadata-objects-example
- key_count: 3
  name: Salesforce Metadata1 Example
  slug: salesforce-metadata1-example
- key_count: 4
  name: Salesforce Metadata10 Example
  slug: salesforce-metadata10-example
- key_count: 4
  name: Salesforce Metadata12 Example
  slug: salesforce-metadata12-example
- key_count: 1
  name: Salesforce Metadata13 Example
  slug: salesforce-metadata13-example
- key_count: 2
  name: Salesforce Metadata14 Example
  slug: salesforce-metadata14-example
- key_count: 5
  name: Salesforce Metadata15 Example
  slug: salesforce-metadata15-example
- key_count: 4
  name: Salesforce Metadata17 Example
  slug: salesforce-metadata17-example
- key_count: 1
  name: Salesforce Metadata18 Example
  slug: salesforce-metadata18-example
- key_count: 3
  name: Salesforce Metadata2 Example
  slug: salesforce-metadata2-example
- key_count: 2
  name: Salesforce Metadata3 Example
  slug: salesforce-metadata3-example
- key_count: 3
  name: Salesforce Metadata6 Example
  slug: salesforce-metadata6-example
- key_count: 4
  name: Salesforce Metadata7 Example
  slug: salesforce-metadata7-example
- key_count: 5
  name: Salesforce Metadata9 Example
  slug: salesforce-metadata9-example
- key_count: 8
  name: Salesforce Method Example
  slug: salesforce-method-example
- key_count: 6
  name: Salesforce Mix Item C Example
  slug: salesforce-mix-item-c-example
- key_count: 2
  name: Salesforce Mobile Phone Example
  slug: salesforce-mobile-phone-example
- key_count: 31
  name: Salesforce Mobile Phone1 Example
  slug: salesforce-mobile-phone1-example
- key_count: 2
  name: Salesforce Mobile Phone3 Example
  slug: salesforce-mobile-phone3-example
- key_count: 4
  name: Salesforce Mobile Sdk Example
  slug: salesforce-mobile-sdk-example
- key_count: 1
  name: Salesforce Model Example
  slug: salesforce-model-example
- key_count: 3
  name: Salesforce Model Field Example
  slug: salesforce-model-field-example
- key_count: 18
  name: Salesforce Model1 Example
  slug: salesforce-model1-example
- key_count: 6
  name: Salesforce Model3 Example
  slug: salesforce-model3-example
- key_count: 2
  name: Salesforce Monthly Einstein Discovery Story Creation Example
  slug: salesforce-monthly-einstein-discovery-story-creation-example
- key_count: 5
  name: Salesforce Motif Example
  slug: salesforce-motif-example
- key_count: 1
  name: Salesforce Mru Enabled Example
  slug: salesforce-mru-enabled-example
- key_count: 1
  name: Salesforce Mute Example
  slug: salesforce-mute-example
- key_count: 2
  name: Salesforce My Subscription Example
  slug: salesforce-my-subscription-example
- key_count: 2
  name: Salesforce Naics Code Example
  slug: salesforce-naics-code-example
- key_count: 31
  name: Salesforce Naics Code1 Example
  slug: salesforce-naics-code1-example
- key_count: 2
  name: Salesforce Naics Desc Example
  slug: salesforce-naics-desc-example
- key_count: 31
  name: Salesforce Naics Desc1 Example
  slug: salesforce-naics-desc1-example
- key_count: 31
  name: Salesforce Name Or Alias Example
  slug: salesforce-name-or-alias-example
- key_count: 1
  name: Salesforce Name13 Example
  slug: salesforce-name13-example
- key_count: 2
  name: Salesforce Name14 Example
  slug: salesforce-name14-example
- key_count: 31
  name: Salesforce Name16 Example
  slug: salesforce-name16-example
- key_count: 31
  name: Salesforce Name17 Example
  slug: salesforce-name17-example
- key_count: 23
  name: Salesforce Name18 Example
  slug: salesforce-name18-example
- key_count: 31
  name: Salesforce Name19 Example
  slug: salesforce-name19-example
- key_count: 2
  name: Salesforce Name21 Example
  slug: salesforce-name21-example
- key_count: 2
  name: Salesforce Name42 Example
  slug: salesforce-name42-example
- key_count: 6
  name: Salesforce Named Credential Example
  slug: salesforce-named-credential-example
- key_count: 6
  name: Salesforce Namespace Registry Example
  slug: salesforce-namespace-registry-example
- key_count: 6
  name: Salesforce Namespace Registry History Example
  slug: salesforce-namespace-registry-history-example
- key_count: 15
  name: Salesforce Nav Item Example
  slug: salesforce-nav-item-example
- key_count: 15
  name: Salesforce Nav Item2 Example
  slug: salesforce-nav-item2-example
- key_count: 15
  name: Salesforce Nav Item3 Example
  slug: salesforce-nav-item3-example
- key_count: 15
  name: Salesforce Nav Item5 Example
  slug: salesforce-nav-item5-example
- key_count: 15
  name: Salesforce Nav Item6 Example
  slug: salesforce-nav-item6-example
- key_count: 2
  name: Salesforce Node Example
  slug: salesforce-node-example
- key_count: 4
  name: Salesforce Node10 Example
  slug: salesforce-node10-example
- key_count: 3
  name: Salesforce Node6 Example
  slug: salesforce-node6-example
- key_count: 5
  name: Salesforce Node7 Example
  slug: salesforce-node7-example
- key_count: 6
  name: Salesforce Note Example
  slug: salesforce-note-example
- key_count: 1
  name: Salesforce Number Of Contacts C Example
  slug: salesforce-number-of-contacts-c-example
- key_count: 2
  name: Salesforce Number Of Employees Example
  slug: salesforce-number-of-employees-example
- key_count: 31
  name: Salesforce Number Of Employees1 Example
  slug: salesforce-number-of-employees1-example
- key_count: 2
  name: Salesforce Number Of Employees2 Example
  slug: salesforce-number-of-employees2-example
- key_count: 2
  name: Salesforce Number Of Employees7 Example
  slug: salesforce-number-of-employees7-example
- key_count: 31
  name: Salesforce Number Of Failed Logins Example
  slug: salesforce-number-of-failed-logins-example
- key_count: 1
  name: Salesforce Numberof Locations C Example
  slug: salesforce-numberof-locations-c-example
- key_count: 31
  name: Salesforce Numberof Locations C1 Example
  slug: salesforce-numberof-locations-c1-example
- key_count: 2
  name: Salesforce Numberof Locations C2 Example
  slug: salesforce-numberof-locations-c2-example
- key_count: 2
  name: Salesforce Numberof Locations C5 Example
  slug: salesforce-numberof-locations-c5-example
- key_count: 3
  name: Salesforce O Auth2 Example
  slug: salesforce-o-auth2-example
- key_count: 2
  name: Salesforce Object Describe Example
  slug: salesforce-object-describe-example
- key_count: 28
  name: Salesforce Object Describe1 Example
  slug: salesforce-object-describe1-example
- key_count: 4
  name: Salesforce Object Infos Example
  slug: salesforce-object-infos-example
- key_count: 2
  name: Salesforce Object Infos1 Example
  slug: salesforce-object-infos1-example
- key_count: 172
  name: Salesforce Objects Example
  slug: salesforce-objects-example
- key_count: 31
  name: Salesforce Offline Pda Trial Expiration Date Example
  slug: salesforce-offline-pda-trial-expiration-date-example
- key_count: 31
  name: Salesforce Offline Trial Expiration Date Example
  slug: salesforce-offline-trial-expiration-date-example
- key_count: 2
  name: Salesforce Opportunities Closing Soon Example
  slug: salesforce-opportunities-closing-soon-example
- key_count: 2
  name: Salesforce Opportunities Closing Soon Explicit And Example
  slug: salesforce-opportunities-closing-soon-explicit-and-example
- key_count: 2
  name: Salesforce Opportunities Early Stage Example
  slug: salesforce-opportunities-early-stage-example
- key_count: 2
  name: Salesforce Opportunities Not Closed Example
  slug: salesforce-opportunities-not-closed-example
- key_count: 6
  name: Salesforce Opportunity Contact Role Example
  slug: salesforce-opportunity-contact-role-example
- key_count: 1
  name: Salesforce Opportunity Example
  slug: salesforce-opportunity-example
- key_count: 6
  name: Salesforce Opportunity Field History Example
  slug: salesforce-opportunity-field-history-example
- key_count: 6
  name: Salesforce Opportunity History Example
  slug: salesforce-opportunity-history-example
- key_count: 6
  name: Salesforce Opportunity Line Item Example
  slug: salesforce-opportunity-line-item-example
- key_count: 6
  name: Salesforce Opportunity Partner Example
  slug: salesforce-opportunity-partner-example
- key_count: 1
  name: Salesforce Opportunity3 Example
  slug: salesforce-opportunity3-example
- key_count: 6
  name: Salesforce Opportunity4 Example
  slug: salesforce-opportunity4-example
- key_count: 1
  name: Salesforce Opt Outfroma Promotion Request Example
  slug: salesforce-opt-outfroma-promotion-request-example
- key_count: 6
  name: Salesforce Order Example
  slug: salesforce-order-example
- key_count: 6
  name: Salesforce Order History Example
  slug: salesforce-order-history-example
- key_count: 6
  name: Salesforce Order Item Example
  slug: salesforce-order-item-example
- key_count: 6
  name: Salesforce Order Item History Example
  slug: salesforce-order-item-history-example
- key_count: 3
  name: Salesforce Ordered By Info Example
  slug: salesforce-ordered-by-info-example
- key_count: 6
  name: Salesforce Org Metric Example
  slug: salesforce-org-metric-example
- key_count: 6
  name: Salesforce Org Metric Scan Result Example
  slug: salesforce-org-metric-scan-result-example
- key_count: 6
  name: Salesforce Org Metric Scan Summary Example
  slug: salesforce-org-metric-scan-summary-example
- key_count: 6
  name: Salesforce Organization Example
  slug: salesforce-organization-example
- key_count: 2
  name: Salesforce Other Address Example
  slug: salesforce-other-address-example
- key_count: 2
  name: Salesforce Other City Example
  slug: salesforce-other-city-example
- key_count: 2
  name: Salesforce Other Country Example
  slug: salesforce-other-country-example
- key_count: 2
  name: Salesforce Other Geocode Accuracy Example
  slug: salesforce-other-geocode-accuracy-example
- key_count: 5
  name: Salesforce Other Geocode Accuracy1 Example
  slug: salesforce-other-geocode-accuracy1-example
- key_count: 2
  name: Salesforce Other Latitude Example
  slug: salesforce-other-latitude-example
- key_count: 2
  name: Salesforce Other Longitude Example
  slug: salesforce-other-longitude-example
- key_count: 2
  name: Salesforce Other Phone Example
  slug: salesforce-other-phone-example
- key_count: 2
  name: Salesforce Other Postal Code Example
  slug: salesforce-other-postal-code-example
- key_count: 2
  name: Salesforce Other State Example
  slug: salesforce-other-state-example
- key_count: 2
  name: Salesforce Other Street Example
  slug: salesforce-other-street-example
- key_count: 1
  name: Salesforce Out Of Office Example
  slug: salesforce-out-of-office-example
- key_count: 31
  name: Salesforce Out Of Office Message Example
  slug: salesforce-out-of-office-message-example
- key_count: 3
  name: Salesforce Outcome Example
  slug: salesforce-outcome-example
- key_count: 1
  name: Salesforce Output Example
  slug: salesforce-output-example
- key_count: 1
  name: Salesforce Output Parameters Example
  slug: salesforce-output-parameters-example
- key_count: 1
  name: Salesforce Output Parameters1 Example
  slug: salesforce-output-parameters1-example
- key_count: 1
  name: Salesforce Output Parameters2 Example
  slug: salesforce-output-parameters2-example
- key_count: 1
  name: Salesforce Output Parameters3 Example
  slug: salesforce-output-parameters3-example
- key_count: 1
  name: Salesforce Output Values Example
  slug: salesforce-output-values-example
- key_count: 1
  name: Salesforce Output Values1 Example
  slug: salesforce-output-values1-example
- key_count: 2
  name: Salesforce Output1 Example
  slug: salesforce-output1-example
- key_count: 1
  name: Salesforce Output2 Example
  slug: salesforce-output2-example
- key_count: 5
  name: Salesforce Output4 Example
  slug: salesforce-output4-example
- key_count: 2
  name: Salesforce Outreach Source Code Example
  slug: salesforce-outreach-source-code-example
- key_count: 19
  name: Salesforce Owner Example
  slug: salesforce-owner-example
- key_count: 2
  name: Salesforce Owner11 Example
  slug: salesforce-owner11-example
- key_count: 2
  name: Salesforce Owner4 Example
  slug: salesforce-owner4-example
- key_count: 2
  name: Salesforce Owner6 Example
  slug: salesforce-owner6-example
- key_count: 2
  name: Salesforce Ownership Example
  slug: salesforce-ownership-example
- key_count: 31
  name: Salesforce Ownership1 Example
  slug: salesforce-ownership1-example
- key_count: 2
  name: Salesforce Ownership2 Example
  slug: salesforce-ownership2-example
- key_count: 2
  name: Salesforce Ownership4 Example
  slug: salesforce-ownership4-example
- key_count: 2
  name: Salesforce Package2 Version Creates Example
  slug: salesforce-package2-version-creates-example
- key_count: 8
  name: Salesforce Page Example
  slug: salesforce-page-example
- key_count: 4
  name: Salesforce Page Info Example
  slug: salesforce-page-info-example
- key_count: 3
  name: Salesforce Page Reference Example
  slug: salesforce-page-reference-example
- key_count: 3
  name: Salesforce Page Reference6 Example
  slug: salesforce-page-reference6-example
- key_count: 8
  name: Salesforce Page1 Example
  slug: salesforce-page1-example
- key_count: 4
  name: Salesforce Parameter Example
  slug: salesforce-parameter-example
- key_count: 5
  name: Salesforce Parameter1 Example
  slug: salesforce-parameter1-example
- key_count: 5
  name: Salesforce Parameter4 Example
  slug: salesforce-parameter4-example
- key_count: 2
  name: Salesforce Parameter5 Example
  slug: salesforce-parameter5-example
- key_count: 7
  name: Salesforce Parent Example
  slug: salesforce-parent-example
- key_count: 20
  name: Salesforce Parent2 Example
  slug: salesforce-parent2-example
- key_count: 2
  name: Salesforce Parent4 Example
  slug: salesforce-parent4-example
- key_count: 2
  name: Salesforce Parent7 Example
  slug: salesforce-parent7-example
- key_count: 6
  name: Salesforce Partner Example
  slug: salesforce-partner-example
- key_count: 6
  name: Salesforce Partner Fund Allocation Example
  slug: salesforce-partner-fund-allocation-example
- key_count: 6
  name: Salesforce Partner Fund Allocation History Example
  slug: salesforce-partner-fund-allocation-history-example
- key_count: 6
  name: Salesforce Partner Fund Claim Example
  slug: salesforce-partner-fund-claim-example
- key_count: 6
  name: Salesforce Partner Fund Claim History Example
  slug: salesforce-partner-fund-claim-history-example
- key_count: 6
  name: Salesforce Partner Fund Request Example
  slug: salesforce-partner-fund-request-example
- key_count: 6
  name: Salesforce Partner Fund Request History Example
  slug: salesforce-partner-fund-request-history-example
- key_count: 6
  name: Salesforce Partner Marketing Budget Example
  slug: salesforce-partner-marketing-budget-example
- key_count: 6
  name: Salesforce Partner Marketing Budget History Example
  slug: salesforce-partner-marketing-budget-history-example
- key_count: 6
  name: Salesforce Party Consent Example
  slug: salesforce-party-consent-example
- key_count: 6
  name: Salesforce Party Consent History Example
  slug: salesforce-party-consent-history-example
- key_count: 2
  name: Salesforce Password Example
  slug: salesforce-password-example
- key_count: 3
  name: Salesforce Passwordless Login Initialize Request Example
  slug: salesforce-passwordless-login-initialize-request-example
- key_count: 1
  name: Salesforce Paths Example
  slug: salesforce-paths-example
- key_count: 16
  name: Salesforce Payment Instrument Example
  slug: salesforce-payment-instrument-example
- key_count: 2
  name: Salesforce Paymentinstrument1 Example
  slug: salesforce-paymentinstrument1-example
- key_count: 6
  name: Salesforce Period Example
  slug: salesforce-period-example
- key_count: 3
  name: Salesforce Permission Sets Example
  slug: salesforce-permission-sets-example
- key_count: 2
  name: Salesforce Phone Example
  slug: salesforce-phone-example
- key_count: 31
  name: Salesforce Phone2 Example
  slug: salesforce-phone2-example
- key_count: 2
  name: Salesforce Phone5 Example
  slug: salesforce-phone5-example
- key_count: 2
  name: Salesforce Phone9 Example
  slug: salesforce-phone9-example
- key_count: 7
  name: Salesforce Photo Example
  slug: salesforce-photo-example
- key_count: 7
  name: Salesforce Photo15 Example
  slug: salesforce-photo15-example
- key_count: 2
  name: Salesforce Photos Example
  slug: salesforce-photos-example
- key_count: 6
  name: Salesforce Picklist Field Values Example
  slug: salesforce-picklist-field-values-example
- key_count: 5
  name: Salesforce Picklist Value Example
  slug: salesforce-picklist-value-example
- key_count: 5
  name: Salesforce Picklist Value1 Example
  slug: salesforce-picklist-value1-example
- key_count: 5
  name: Salesforce Picklist Value2 Example
  slug: salesforce-picklist-value2-example
- key_count: 5
  name: Salesforce Picklist Value31 Example
  slug: salesforce-picklist-value31-example
- key_count: 4
  name: Salesforce Platform Event Schemaby Event Name Example
  slug: salesforce-platform-event-schemaby-event-name-example
- key_count: 31
  name: Salesforce Portal Role Example
  slug: salesforce-portal-role-example
- key_count: 3
  name: Salesforce Post Example
  slug: salesforce-post-example
- key_count: 1
  name: Salesforce Post Tooling S Object Request Example
  slug: salesforce-post-tooling-s-object-request-example
- key_count: 31
  name: Salesforce Postal Code Example
  slug: salesforce-postal-code-example
- key_count: 2
  name: Salesforce Postal Code2 Example
  slug: salesforce-postal-code2-example
- key_count: 2
  name: Salesforce Postal Code3 Example
  slug: salesforce-postal-code3-example
- key_count: 1
  name: Salesforce Potential Value C Example
  slug: salesforce-potential-value-c-example
- key_count: 3
  name: Salesforce Predict Example
  slug: salesforce-predict-example
- key_count: 4
  name: Salesforce Predict Request Example
  slug: salesforce-predict-request-example
- key_count: 14
  name: Salesforce Prediction Definitions1 Example
  slug: salesforce-prediction-definitions1-example
- key_count: 4
  name: Salesforce Prediction Example
  slug: salesforce-prediction-example
- key_count: 2
  name: Salesforce Prediction1 Example
  slug: salesforce-prediction1-example
- key_count: 14
  name: Salesforce Predictiondefinitionmetadata Example
  slug: salesforce-predictiondefinitionmetadata-example
- key_count: 4
  name: Salesforce Predictiondefinitions Example
  slug: salesforce-predictiondefinitions-example
- key_count: 3
  name: Salesforce Predictionmodels Example
  slug: salesforce-predictionmodels-example
- key_count: 2
  name: Salesforce Prescribable Field Example
  slug: salesforce-prescribable-field-example
- key_count: 6
  name: Salesforce Pricebook Entry Example
  slug: salesforce-pricebook-entry-example
- key_count: 6
  name: Salesforce Pricebook Entry History Example
  slug: salesforce-pricebook-entry-history-example
- key_count: 6
  name: Salesforce Pricebook2 Example
  slug: salesforce-pricebook2-example
- key_count: 6
  name: Salesforce Pricebook2 History Example
  slug: salesforce-pricebook2-history-example
- key_count: 31
  name: Salesforce Primary C Example
  slug: salesforce-primary-c-example
- key_count: 2
  name: Salesforce Primary C1 Example
  slug: salesforce-primary-c1-example
- key_count: 3
  name: Salesforce Principal Example
  slug: salesforce-principal-example
- key_count: 7
  name: Salesforce Principal1 Example
  slug: salesforce-principal1-example
- key_count: 7
  name: Salesforce Process Approvals Submit Request Example
  slug: salesforce-process-approvals-submit-request-example
- key_count: 6
  name: Salesforce Process Definition Example
  slug: salesforce-process-definition-example
- key_count: 6
  name: Salesforce Process Instance Example
  slug: salesforce-process-instance-example
- key_count: 2
  name: Salesforce Process Parameter Example
  slug: salesforce-process-parameter-example
- key_count: 2
  name: Salesforce Process Parameter1 Example
  slug: salesforce-process-parameter1-example
- key_count: 2
  name: Salesforce Process Parameter2 Example
  slug: salesforce-process-parameter2-example
- key_count: 2
  name: Salesforce Process Parameter3 Example
  slug: salesforce-process-parameter3-example
- key_count: 1
  name: Salesforce Process Parameter4 Example
  slug: salesforce-process-parameter4-example
- key_count: 4
  name: Salesforce Process Parameter5 Example
  slug: salesforce-process-parameter5-example
- key_count: 2
  name: Salesforce Process Parameter7 Example
  slug: salesforce-process-parameter7-example
- key_count: 5
  name: Salesforce Process Parameter8 Example
  slug: salesforce-process-parameter8-example
- key_count: 3
  name: Salesforce Process Parameter9 Example
  slug: salesforce-process-parameter9-example
- key_count: 1
  name: Salesforce Processing Options Example
  slug: salesforce-processing-options-example
- key_count: 6
  name: Salesforce Product Consumption Schedule Example
  slug: salesforce-product-consumption-schedule-example
- key_count: 2
  name: Salesforce Product Context Example
  slug: salesforce-product-context-example
- key_count: 1
  name: Salesforce Product Context1 Example
  slug: salesforce-product-context1-example
- key_count: 31
  name: Salesforce Product Interest C Example
  slug: salesforce-product-interest-c-example
- key_count: 2
  name: Salesforce Product Interest C1 Example
  slug: salesforce-product-interest-c1-example
- key_count: 6
  name: Salesforce Product2 Example
  slug: salesforce-product2-example
- key_count: 6
  name: Salesforce Product2 History Example
  slug: salesforce-product2-history-example
- key_count: 6
  name: Salesforce Profile Skill Endorsement Example
  slug: salesforce-profile-skill-endorsement-example
- key_count: 6
  name: Salesforce Profile Skill Endorsement History Example
  slug: salesforce-profile-skill-endorsement-history-example
- key_count: 6
  name: Salesforce Profile Skill Example
  slug: salesforce-profile-skill-example
- key_count: 6
  name: Salesforce Profile Skill History Example
  slug: salesforce-profile-skill-history-example
- key_count: 6
  name: Salesforce Profile Skill User Example
  slug: salesforce-profile-skill-user-example
- key_count: 6
  name: Salesforce Profile Skill User History Example
  slug: salesforce-profile-skill-user-history-example
- key_count: 6
  name: Salesforce Promotion Eligibility Example
  slug: salesforce-promotion-eligibility-example
- key_count: 8
  name: Salesforce Promotion Limits Example
  slug: salesforce-promotion-limits-example
- key_count: 11
  name: Salesforce Promotions Creation Request Example
  slug: salesforce-promotions-creation-request-example
- key_count: 2
  name: Salesforce Properties Example
  slug: salesforce-properties-example
- key_count: 29
  name: Salesforce Properties1 Example
  slug: salesforce-properties1-example
- key_count: 3
  name: Salesforce Properties10 Example
  slug: salesforce-properties10-example
- key_count: 60
  name: Salesforce Properties12 Example
  slug: salesforce-properties12-example
- key_count: 1
  name: Salesforce Properties2 Example
  slug: salesforce-properties2-example
- key_count: 2
  name: Salesforce Properties3 Example
  slug: salesforce-properties3-example
- key_count: 74
  name: Salesforce Properties4 Example
  slug: salesforce-properties4-example
- key_count: 2
  name: Salesforce Properties5 Example
  slug: salesforce-properties5-example
- key_count: 4
  name: Salesforce Properties6 Example
  slug: salesforce-properties6-example
- key_count: 1
  name: Salesforce Properties7 Example
  slug: salesforce-properties7-example
- key_count: 5
  name: Salesforce Properties8 Example
  slug: salesforce-properties8-example
- key_count: 4
  name: Salesforce Properties9 Example
  slug: salesforce-properties9-example
- key_count: 2
  name: Salesforce Publish Callback Usage In Apex Example
  slug: salesforce-publish-callback-usage-in-apex-example
- key_count: 2
  name: Salesforce Publishmultipleevents Request Example
  slug: salesforce-publishmultipleevents-request-example
- key_count: 3
  name: Salesforce Publishsingleevent Example
  slug: salesforce-publishsingleevent-example
- key_count: 3
  name: Salesforce Publishsingleevent Request Example
  slug: salesforce-publishsingleevent-request-example
- key_count: 3
  name: Salesforce Query All Example
  slug: salesforce-query-all-example
- key_count: 1
  name: Salesforce Query Example
  slug: salesforce-query-example
- key_count: 1
  name: Salesforce Query10 Example
  slug: salesforce-query10-example
- key_count: 3
  name: Salesforce Query11 Example
  slug: salesforce-query11-example
- key_count: 1
  name: Salesforce Query3 Example
  slug: salesforce-query3-example
- key_count: 1
  name: Salesforce Query4 Example
  slug: salesforce-query4-example
- key_count: 1
  name: Salesforce Query6 Example
  slug: salesforce-query6-example
- key_count: 1
  name: Salesforce Query7 Example
  slug: salesforce-query7-example
- key_count: 1
  name: Salesforce Queryable Example
  slug: salesforce-queryable-example
- key_count: 6
  name: Salesforce Quick Text Example
  slug: salesforce-quick-text-example
- key_count: 6
  name: Salesforce Quick Text History Example
  slug: salesforce-quick-text-history-example
- key_count: 1
  name: Salesforce Quote Term Reader Api Request Example
  slug: salesforce-quote-term-reader-api-request-example
- key_count: 2
  name: Salesforce Rating Example
  slug: salesforce-rating-example
- key_count: 31
  name: Salesforce Rating1 Example
  slug: salesforce-rating1-example
- key_count: 2
  name: Salesforce Rating2 Example
  slug: salesforce-rating2-example
- key_count: 2
  name: Salesforce Rating3 Example
  slug: salesforce-rating3-example
- key_count: 3
  name: Salesforce Read By Example
  slug: salesforce-read-by-example
- key_count: 1
  name: Salesforce Read Product Api Request Example
  slug: salesforce-read-product-api-request-example
- key_count: 2
  name: Salesforce Recent Items Example
  slug: salesforce-recent-items-example
- key_count: 19
  name: Salesforce Recipient Example
  slug: salesforce-recipient-example
- key_count: 6
  name: Salesforce Recommendation Example
  slug: salesforce-recommendation-example
- key_count: 6
  name: Salesforce Record Action Example
  slug: salesforce-record-action-example
- key_count: 1
  name: Salesforce Record Count Example
  slug: salesforce-record-count-example
- key_count: 11
  name: Salesforce Record Example
  slug: salesforce-record-example
- key_count: 6
  name: Salesforce Record Type Example
  slug: salesforce-record-type-example
- key_count: 8
  name: Salesforce Record Type Info Example
  slug: salesforce-record-type-info-example
- key_count: 1
  name: Salesforce Record Type Infos Example
  slug: salesforce-record-type-infos-example
- key_count: 6
  name: Salesforce Record10 Example
  slug: salesforce-record10-example
- key_count: 20
  name: Salesforce Record11 Example
  slug: salesforce-record11-example
- key_count: 14
  name: Salesforce Record12 Example
  slug: salesforce-record12-example
- key_count: 2
  name: Salesforce Record13 Example
  slug: salesforce-record13-example
- key_count: 70
  name: Salesforce Record14 Example
  slug: salesforce-record14-example
- key_count: 2
  name: Salesforce Record15 Example
  slug: salesforce-record15-example
- key_count: 2
  name: Salesforce Record16 Example
  slug: salesforce-record16-example
- key_count: 9
  name: Salesforce Record17 Example
  slug: salesforce-record17-example
- key_count: 2
  name: Salesforce Record18 Example
  slug: salesforce-record18-example
- key_count: 13
  name: Salesforce Record19 Example
  slug: salesforce-record19-example
- key_count: 8
  name: Salesforce Record2 Example
  slug: salesforce-record2-example
- key_count: 2
  name: Salesforce Record20 Example
  slug: salesforce-record20-example
- key_count: 14
  name: Salesforce Record21 Example
  slug: salesforce-record21-example
- key_count: 2
  name: Salesforce Record22 Example
  slug: salesforce-record22-example
- key_count: 13
  name: Salesforce Record23 Example
  slug: salesforce-record23-example
- key_count: 5
  name: Salesforce Record24 Example
  slug: salesforce-record24-example
- key_count: 4
  name: Salesforce Record25 Example
  slug: salesforce-record25-example
- key_count: 11
  name: Salesforce Record27 Example
  slug: salesforce-record27-example
- key_count: 11
  name: Salesforce Record28 Example
  slug: salesforce-record28-example
- key_count: 4
  name: Salesforce Record3 Example
  slug: salesforce-record3-example
- key_count: 6
  name: Salesforce Record4 Example
  slug: salesforce-record4-example
- key_count: 5
  name: Salesforce Record5 Example
  slug: salesforce-record5-example
- key_count: 3
  name: Salesforce Record6 Example
  slug: salesforce-record6-example
- key_count: 3
  name: Salesforce Record7 Example
  slug: salesforce-record7-example
- key_count: 19
  name: Salesforce Record8 Example
  slug: salesforce-record8-example
- key_count: 5
  name: Salesforce Record9 Example
  slug: salesforce-record9-example
- key_count: 2
  name: Salesforce Records Example
  slug: salesforce-records-example
- key_count: 11
  name: Salesforce Records1 Example
  slug: salesforce-records1-example
- key_count: 11
  name: Salesforce Records2 Example
  slug: salesforce-records2-example
- key_count: 11
  name: Salesforce Records3 Example
  slug: salesforce-records3-example
- key_count: 10
  name: Salesforce Records4 Example
  slug: salesforce-records4-example
- key_count: 2
  name: Salesforce Redeem Voucher Example
  slug: salesforce-redeem-voucher-example
- key_count: 2
  name: Salesforce Redeem Voucher Request Example
  slug: salesforce-redeem-voucher-request-example
- key_count: 2
  name: Salesforce Reference Example
  slug: salesforce-reference-example
- key_count: 2
  name: Salesforce Reference To Info Example
  slug: salesforce-reference-to-info-example
- key_count: 2
  name: Salesforce Refresh Sandbox Request Example
  slug: salesforce-refresh-sandbox-request-example
- key_count: 1
  name: Salesforce Region C Example
  slug: salesforce-region-c-example
- key_count: 5
  name: Salesforce Registration Initialize Request Example
  slug: salesforce-registration-initialize-request-example
- key_count: 4
  name: Salesforce Related Named Credential Example
  slug: salesforce-related-named-credential-example
- key_count: 2
  name: Salesforce Renewed Contract Example
  slug: salesforce-renewed-contract-example
- key_count: 1
  name: Salesforce Replicateable Example
  slug: salesforce-replicateable-example
- key_count: 6
  name: Salesforce Report Anomaly Event Store Example
  slug: salesforce-report-anomaly-event-store-example
- key_count: 6
  name: Salesforce Report Example
  slug: salesforce-report-example
- key_count: 1
  name: Salesforce Request Body Example
  slug: salesforce-request-body-example
- key_count: 8
  name: Salesforce Request Example
  slug: salesforce-request-example
- key_count: 2
  name: Salesforce Request Product Information Bundled Components Request Example
  slug: salesforce-request-product-information-bundled-components-request-example
- key_count: 3
  name: Salesforce Request Product Information No Bundles Request Example
  slug: salesforce-request-product-information-no-bundles-request-example
- key_count: 2
  name: Salesforce Requested Group Example
  slug: salesforce-requested-group-example
- key_count: 48
  name: Salesforce Resourcesby Version Example
  slug: salesforce-resourcesby-version-example
- key_count: 2
  name: Salesforce Rest Api Error Example
  slug: salesforce-rest-api-error-example
- key_count: 3
  name: Salesforce Rest Api Version Example
  slug: salesforce-rest-api-version-example
- key_count: 3
  name: Salesforce Rest Composite Request Example
  slug: salesforce-rest-composite-request-example
- key_count: 1
  name: Salesforce Rest Composite Response Example
  slug: salesforce-rest-composite-response-example
- key_count: 3
  name: Salesforce Rest Error Example
  slug: salesforce-rest-error-example
- key_count: 4
  name: Salesforce Rest Query Result Example
  slug: salesforce-rest-query-result-example
- key_count: 11
  name: Salesforce Rest S Object Describe Example
  slug: salesforce-rest-s-object-describe-example
- key_count: 2
  name: Salesforce Rest S Object Record Example
  slug: salesforce-rest-s-object-record-example
- key_count: 1
  name: Salesforce Rest Search Result Example
  slug: salesforce-rest-search-result-example
- key_count: 2
  name: Salesforce Result Example
  slug: salesforce-result-example
- key_count: 1
  name: Salesforce Result Page Example
  slug: salesforce-result-page-example
- key_count: 2
  name: Salesforce Result1 Example
  slug: salesforce-result1-example
- key_count: 21
  name: Salesforce Result2 Example
  slug: salesforce-result2-example
- key_count: 2
  name: Salesforce Result21 Example
  slug: salesforce-result21-example
- key_count: 4
  name: Salesforce Result3 Example
  slug: salesforce-result3-example
- key_count: 4
  name: Salesforce Result4 Example
  slug: salesforce-result4-example
- key_count: 11
  name: Salesforce Result5 Example
  slug: salesforce-result5-example
- key_count: 11
  name: Salesforce Result6 Example
  slug: salesforce-result6-example
- key_count: 1
  name: Salesforce Results Example
  slug: salesforce-results-example
- key_count: 2
  name: Salesforce Results1 Example
  slug: salesforce-results1-example
- key_count: 1
  name: Salesforce Results2 Example
  slug: salesforce-results2-example
- key_count: 1
  name: Salesforce Results3 Example
  slug: salesforce-results3-example
- key_count: 2
  name: Salesforce Results4 Example
  slug: salesforce-results4-example
- key_count: 4
  name: Salesforce Resultwithdefaultnav Example
  slug: salesforce-resultwithdefaultnav-example
- key_count: 4
  name: Salesforce Resultwithpersonalizednav Example
  slug: salesforce-resultwithpersonalizednav-example
- key_count: 1
  name: Salesforce Retail Location Group Example
  slug: salesforce-retail-location-group-example
- key_count: 6
  name: Salesforce Retrieve Open Api Schema Example
  slug: salesforce-retrieve-open-api-schema-example
- key_count: 1
  name: Salesforce Retrieveable Example
  slug: salesforce-retrieveable-example
- key_count: 14
  name: Salesforce Reward Example
  slug: salesforce-reward-example
- key_count: 4
  name: Salesforce Rich Input Example
  slug: salesforce-rich-input-example
- key_count: 5
  name: Salesforce Run Decision Matrix Example
  slug: salesforce-run-decision-matrix-example
- key_count: 1
  name: Salesforce Run Decision Matrix Request Example
  slug: salesforce-run-decision-matrix-request-example
- key_count: 1
  name: Salesforce Run Expression Set Request Example
  slug: salesforce-run-expression-set-request-example
- key_count: 1
  name: Salesforce Run Setting Example
  slug: salesforce-run-setting-example
- key_count: 2
  name: Salesforce Runagenttest Example
  slug: salesforce-runagenttest-example
- key_count: 1
  name: Salesforce Runagenttest Request Example
  slug: salesforce-runagenttest-request-example
- key_count: 2
  name: Salesforce S Object Collections Create Request Example
  slug: salesforce-s-object-collections-create-request-example
- key_count: 3
  name: Salesforce S Object Collections Update Example
  slug: salesforce-s-object-collections-update-example
- key_count: 2
  name: Salesforce S Object Collections Update Request Example
  slug: salesforce-s-object-collections-update-request-example
- key_count: 2
  name: Salesforce S Object Collections Upsert Request Example
  slug: salesforce-s-object-collections-upsert-request-example
- key_count: 3
  name: Salesforce S Object Create Example
  slug: salesforce-s-object-create-example
- key_count: 1
  name: Salesforce S Object Create Request Example
  slug: salesforce-s-object-create-request-example
- key_count: 45
  name: Salesforce S Object Describe Example
  slug: salesforce-s-object-describe-example
- key_count: 2
  name: Salesforce S Object Root Info Example
  slug: salesforce-s-object-root-info-example
- key_count: 1
  name: Salesforce S Object Rows Update Request Example
  slug: salesforce-s-object-rows-update-request-example
- key_count: 1
  name: Salesforce S Object Tree Request Example
  slug: salesforce-s-object-tree-request-example
- key_count: 4
  name: Salesforce S Objects Example
  slug: salesforce-s-objects-example
- key_count: 2
  name: Salesforce S Objects1 Example
  slug: salesforce-s-objects1-example
- key_count: 2
  name: Salesforce Salutation Example
  slug: salesforce-salutation-example
- key_count: 31
  name: Salesforce Salutation1 Example
  slug: salesforce-salutation1-example
- key_count: 2
  name: Salesforce Salutation2 Example
  slug: salesforce-salutation2-example
- key_count: 5
  name: Salesforce Salutation4 Example
  slug: salesforce-salutation4-example
- key_count: 3
  name: Salesforce Sample Lightning Page Example
  slug: salesforce-sample-lightning-page-example
- key_count: 2
  name: Salesforce Save Result Example
  slug: salesforce-save-result-example
- key_count: 1
  name: Salesforce Schema Example
  slug: salesforce-schema-example
- key_count: 2
  name: Salesforce Schema1 Example
  slug: salesforce-schema1-example
- key_count: 1
  name: Salesforce Schema10 Example
  slug: salesforce-schema10-example
- key_count: 6
  name: Salesforce Schemas Example
  slug: salesforce-schemas-example
- key_count: 17
  name: Salesforce Scopes Example
  slug: salesforce-scopes-example
- key_count: 1
  name: Salesforce Scopes1 Example
  slug: salesforce-scopes1-example
- key_count: 6
  name: Salesforce Scorecard Association Example
  slug: salesforce-scorecard-association-example
- key_count: 6
  name: Salesforce Scorecard Example
  slug: salesforce-scorecard-example
- key_count: 6
  name: Salesforce Scorecard Metric Example
  slug: salesforce-scorecard-metric-example
- key_count: 6
  name: Salesforce Scratch Org Info Example
  slug: salesforce-scratch-org-info-example
- key_count: 6
  name: Salesforce Scratch Org Info History Example
  slug: salesforce-scratch-org-info-history-example
- key_count: 6
  name: Salesforce Search Promotion Rule Example
  slug: salesforce-search-promotion-rule-example
- key_count: 2
  name: Salesforce Search Record Example
  slug: salesforce-search-record-example
- key_count: 1
  name: Salesforce Searchable Example
  slug: salesforce-searchable-example
- key_count: 7
  name: Salesforce Section Example
  slug: salesforce-section-example
- key_count: 5
  name: Salesforce Section User States Example
  slug: salesforce-section-user-states-example
- key_count: 7
  name: Salesforce Section1 Example
  slug: salesforce-section1-example
- key_count: 3
  name: Salesforce Security Example
  slug: salesforce-security-example
- key_count: 3
  name: Salesforce Security Schemes Example
  slug: salesforce-security-schemes-example
- key_count: 6
  name: Salesforce Seller Example
  slug: salesforce-seller-example
- key_count: 6
  name: Salesforce Seller History Example
  slug: salesforce-seller-history-example
- key_count: 19
  name: Salesforce Sender Example
  slug: salesforce-sender-example
- key_count: 31
  name: Salesforce Sender Name Example
  slug: salesforce-sender-name-example
- key_count: 3
  name: Salesforce Sender1 Example
  slug: salesforce-sender1-example
- key_count: 1
  name: Salesforce Server Example
  slug: salesforce-server-example
- key_count: 1
  name: Salesforce Session Header Example
  slug: salesforce-session-header-example
- key_count: 1
  name: Salesforce Session Header1 Example
  slug: salesforce-session-header1-example
- key_count: 1
  name: Salesforce Session Header4 Example
  slug: salesforce-session-header4-example
- key_count: 6
  name: Salesforce Session Hijacking Event Store Example
  slug: salesforce-session-hijacking-event-store-example
- key_count: 3
  name: Salesforce Settings Example
  slug: salesforce-settings-example
- key_count: 6
  name: Salesforce Setup Assistant Step Example
  slug: salesforce-setup-assistant-step-example
- key_count: 2
  name: Salesforce Share Example
  slug: salesforce-share-example
- key_count: 2
  name: Salesforce Shipping Address Example
  slug: salesforce-shipping-address-example
- key_count: 8
  name: Salesforce Shipping Address1 Example
  slug: salesforce-shipping-address1-example
- key_count: 8
  name: Salesforce Shipping Address11 Example
  slug: salesforce-shipping-address11-example
- key_count: 8
  name: Salesforce Shipping Address12 Example
  slug: salesforce-shipping-address12-example
- key_count: 31
  name: Salesforce Shipping Address2 Example
  slug: salesforce-shipping-address2-example
- key_count: 2
  name: Salesforce Shipping City Example
  slug: salesforce-shipping-city-example
- key_count: 31
  name: Salesforce Shipping City1 Example
  slug: salesforce-shipping-city1-example
- key_count: 2
  name: Salesforce Shipping City2 Example
  slug: salesforce-shipping-city2-example
- key_count: 2
  name: Salesforce Shipping City4 Example
  slug: salesforce-shipping-city4-example
- key_count: 2
  name: Salesforce Shipping Country Example
  slug: salesforce-shipping-country-example
- key_count: 31
  name: Salesforce Shipping Country1 Example
  slug: salesforce-shipping-country1-example
- key_count: 2
  name: Salesforce Shipping Country2 Example
  slug: salesforce-shipping-country2-example
- key_count: 2
  name: Salesforce Shipping Country4 Example
  slug: salesforce-shipping-country4-example
- key_count: 2
  name: Salesforce Shipping Geocode Accuracy Example
  slug: salesforce-shipping-geocode-accuracy-example
- key_count: 31
  name: Salesforce Shipping Geocode Accuracy1 Example
  slug: salesforce-shipping-geocode-accuracy1-example
- key_count: 2
  name: Salesforce Shipping Latitude Example
  slug: salesforce-shipping-latitude-example
- key_count: 31
  name: Salesforce Shipping Latitude1 Example
  slug: salesforce-shipping-latitude1-example
- key_count: 2
  name: Salesforce Shipping Longitude Example
  slug: salesforce-shipping-longitude-example
- key_count: 31
  name: Salesforce Shipping Longitude1 Example
  slug: salesforce-shipping-longitude1-example
- key_count: 2
  name: Salesforce Shipping Postal Code Example
  slug: salesforce-shipping-postal-code-example
- key_count: 31
  name: Salesforce Shipping Postal Code1 Example
  slug: salesforce-shipping-postal-code1-example
- key_count: 2
  name: Salesforce Shipping Postal Code2 Example
  slug: salesforce-shipping-postal-code2-example
- key_count: 2
  name: Salesforce Shipping Postal Code4 Example
  slug: salesforce-shipping-postal-code4-example
- key_count: 2
  name: Salesforce Shipping State Example
  slug: salesforce-shipping-state-example
- key_count: 31
  name: Salesforce Shipping State1 Example
  slug: salesforce-shipping-state1-example
- key_count: 2
  name: Salesforce Shipping State2 Example
  slug: salesforce-shipping-state2-example
- key_count: 2
  name: Salesforce Shipping State4 Example
  slug: salesforce-shipping-state4-example
- key_count: 2
  name: Salesforce Shipping Street Example
  slug: salesforce-shipping-street-example
- key_count: 31
  name: Salesforce Shipping Street1 Example
  slug: salesforce-shipping-street1-example
- key_count: 2
  name: Salesforce Shipping Street2 Example
  slug: salesforce-shipping-street2-example
- key_count: 2
  name: Salesforce Shipping Street4 Example
  slug: salesforce-shipping-street4-example
- key_count: 31
  name: Salesforce Sic Code C Example
  slug: salesforce-sic-code-c-example
- key_count: 2
  name: Salesforce Sic Code C1 Example
  slug: salesforce-sic-code-c1-example
- key_count: 2
  name: Salesforce Sic Desc Example
  slug: salesforce-sic-desc-example
- key_count: 31
  name: Salesforce Sic Desc1 Example
  slug: salesforce-sic-desc1-example
- key_count: 2
  name: Salesforce Sic Example
  slug: salesforce-sic-example
- key_count: 31
  name: Salesforce Sic1 Example
  slug: salesforce-sic1-example
- key_count: 2
  name: Salesforce Sic2 Example
  slug: salesforce-sic2-example
- key_count: 2
  name: Salesforce Sic4 Example
  slug: salesforce-sic4-example
- key_count: 31
  name: Salesforce Signature Example
  slug: salesforce-signature-example
- key_count: 2
  name: Salesforce Site Example
  slug: salesforce-site-example
- key_count: 6
  name: Salesforce Site History Example
  slug: salesforce-site-history-example
- key_count: 31
  name: Salesforce Site1 Example
  slug: salesforce-site1-example
- key_count: 2
  name: Salesforce Site2 Example
  slug: salesforce-site2-example
- key_count: 2
  name: Salesforce Sla Expiration Date C Example
  slug: salesforce-sla-expiration-date-c-example
- key_count: 31
  name: Salesforce Sla Expiration Date C1 Example
  slug: salesforce-sla-expiration-date-c1-example
- key_count: 2
  name: Salesforce Sla Expiration Date C2 Example
  slug: salesforce-sla-expiration-date-c2-example
- key_count: 2
  name: Salesforce Sla Expiration Date C4 Example
  slug: salesforce-sla-expiration-date-c4-example
- key_count: 1
  name: Salesforce Sla Serial Number C Example
  slug: salesforce-sla-serial-number-c-example
- key_count: 31
  name: Salesforce Sla Serial Number C1 Example
  slug: salesforce-sla-serial-number-c1-example
- key_count: 2
  name: Salesforce Sla Serial Number C2 Example
  slug: salesforce-sla-serial-number-c2-example
- key_count: 2
  name: Salesforce Sla Serial Number C4 Example
  slug: salesforce-sla-serial-number-c4-example
- key_count: 1
  name: Salesforce Slac Example
  slug: salesforce-slac-example
- key_count: 31
  name: Salesforce Slac1 Example
  slug: salesforce-slac1-example
- key_count: 2
  name: Salesforce Slac2 Example
  slug: salesforce-slac2-example
- key_count: 2
  name: Salesforce Slac4 Example
  slug: salesforce-slac4-example
- key_count: 3
  name: Salesforce Sobjects Contact Example
  slug: salesforce-sobjects-contact-example
- key_count: 28
  name: Salesforce Sobjects2 Example
  slug: salesforce-sobjects2-example
- key_count: 6
  name: Salesforce Solution History Example
  slug: salesforce-solution-history-example
- key_count: 1
  name: Salesforce Stage Name Example
  slug: salesforce-stage-name-example
- key_count: 31
  name: Salesforce State Example
  slug: salesforce-state-example
- key_count: 2
  name: Salesforce State2 Example
  slug: salesforce-state2-example
- key_count: 6
  name: Salesforce Static Resource Example
  slug: salesforce-static-resource-example
- key_count: 1
  name: Salesforce Status Code Example
  slug: salesforce-status-code-example
- key_count: 2
  name: Salesforce Status Example
  slug: salesforce-status-example
- key_count: 2
  name: Salesforce Status1 Example
  slug: salesforce-status1-example
- key_count: 6
  name: Salesforce Status200 Record Found Example
  slug: salesforce-status200-record-found-example
- key_count: 4
  name: Salesforce Status200 Success Example
  slug: salesforce-status200-success-example
- key_count: 3
  name: Salesforce Status200 Success2 Example
  slug: salesforce-status200-success2-example
- key_count: 5
  name: Salesforce Status200 Successfull Example
  slug: salesforce-status200-successfull-example
- key_count: 6
  name: Salesforce Status200 Successfully Updated Example
  slug: salesforce-status200-successfully-updated-example
- key_count: 2
  name: Salesforce Status200 Update Commitment Database Failure Example
  slug: salesforce-status200-update-commitment-database-failure-example
- key_count: 2
  name: Salesforce Status200 Update Commitment Success Example
  slug: salesforce-status200-update-commitment-success-example
- key_count: 1
  name: Salesforce Status201 Accepted But Warning Example
  slug: salesforce-status201-accepted-but-warning-example
- key_count: 3
  name: Salesforce Status201 Bad Request Example
  slug: salesforce-status201-bad-request-example
- key_count: 4
  name: Salesforce Status201 Create Commitment Success Example
  slug: salesforce-status201-create-commitment-success-example
- key_count: 4
  name: Salesforce Status201 Create Commitment Success1 Example
  slug: salesforce-status201-create-commitment-success1-example
- key_count: 4
  name: Salesforce Status201 Create Gift Success Example
  slug: salesforce-status201-create-gift-success-example
- key_count: 1
  name: Salesforce Status201 Error Example
  slug: salesforce-status201-error-example
- key_count: 1
  name: Salesforce Status201 Key Pair Not Found Example
  slug: salesforce-status201-key-pair-not-found-example
- key_count: 6
  name: Salesforce Status201 Success Created Only Mandatory Fields Example
  slug: salesforce-status201-success-created-only-mandatory-fields-example
- key_count: 3
  name: Salesforce Status201 Success Example
  slug: salesforce-status201-success-example
- key_count: 1
  name: Salesforce Status201 Success1 Example
  slug: salesforce-status201-success1-example
- key_count: 1
  name: Salesforce Status201 Success2 Example
  slug: salesforce-status201-success2-example
- key_count: 3
  name: Salesforce Status201 Success3 Example
  slug: salesforce-status201-success3-example
- key_count: 4
  name: Salesforce Status201 Success4 Example
  slug: salesforce-status201-success4-example
- key_count: 5
  name: Salesforce Status201 Success5 Example
  slug: salesforce-status201-success5-example
- key_count: 4
  name: Salesforce Status201 Update Commitment Success Example
  slug: salesforce-status201-update-commitment-success-example
- key_count: 4
  name: Salesforce Status201 Update Transaction Payment Success Example
  slug: salesforce-status201-update-transaction-payment-success-example
- key_count: 2
  name: Salesforce Status400 Active Expression Can Not Be Deleted1 Example
  slug: salesforce-status400-active-expression-can-not-be-deleted1-example
- key_count: 2
  name: Salesforce Status400 Bad Request1 Example
  slug: salesforce-status400-bad-request1-example
- key_count: 2
  name: Salesforce Status400 Duplicate1 Example
  slug: salesforce-status400-duplicate1-example
- key_count: 5
  name: Salesforce Status400 Empty Expression Set Api Name1 Example
  slug: salesforce-status400-empty-expression-set-api-name1-example
- key_count: 5
  name: Salesforce Status400 Expression Not Found1 Example
  slug: salesforce-status400-expression-not-found1-example
- key_count: 2
  name: Salesforce Status400 Instance Not Found1 Example
  slug: salesforce-status400-instance-not-found1-example
- key_count: 2
  name: Salesforce Status400 Matrix Not Found1 Example
  slug: salesforce-status400-matrix-not-found1-example
- key_count: 2
  name: Salesforce Status400 Missing Mandatory Body Field1 Example
  slug: salesforce-status400-missing-mandatory-body-field1-example
- key_count: 2
  name: Salesforce Status400 Previously Deleted Record1 Example
  slug: salesforce-status400-previously-deleted-record1-example
- key_count: 2
  name: Salesforce Status400 Try To Delete Previously Deleted1 Example
  slug: salesforce-status400-try-to-delete-previously-deleted1-example
- key_count: 2
  name: Salesforce Status400 Unknown Exception1 Example
  slug: salesforce-status400-unknown-exception1-example
- key_count: 2
  name: Salesforce Status400 Unrecognized Body Field1 Example
  slug: salesforce-status400-unrecognized-body-field1-example
- key_count: 2
  name: Salesforce Status401 Unauthorized1 Example
  slug: salesforce-status401-unauthorized1-example
- key_count: 2
  name: Salesforce Status404 Not Found1 Example
  slug: salesforce-status404-not-found1-example
- key_count: 2
  name: Salesforce Status404 Record Not Found1 Example
  slug: salesforce-status404-record-not-found1-example
- key_count: 2
  name: Salesforce Status500 Empty Body But Record Exist1 Example
  slug: salesforce-status500-empty-body-but-record-exist1-example
- key_count: 2
  name: Salesforce Status500 Empty Body1 Example
  slug: salesforce-status500-empty-body1-example
- key_count: 2
  name: Salesforce Status500 Error No Body1 Example
  slug: salesforce-status500-error-no-body1-example
- key_count: 2
  name: Salesforce Status500 Unexpected Error1 Example
  slug: salesforce-status500-unexpected-error1-example
- key_count: 2
  name: Salesforce Status500 Unknown Exception1 Example
  slug: salesforce-status500-unknown-exception1-example
- key_count: 31
  name: Salesforce Status8 Example
  slug: salesforce-status8-example
- key_count: 2
  name: Salesforce Status9 Example
  slug: salesforce-status9-example
- key_count: 31
  name: Salesforce Stay In Touch Note Example
  slug: salesforce-stay-in-touch-note-example
- key_count: 31
  name: Salesforce Stay In Touch Signature Example
  slug: salesforce-stay-in-touch-signature-example
- key_count: 31
  name: Salesforce Stay In Touch Subject Example
  slug: salesforce-stay-in-touch-subject-example
- key_count: 10
  name: Salesforce Step Example
  slug: salesforce-step-example
- key_count: 1
  name: Salesforce Store Example
  slug: salesforce-store-example
- key_count: 2
  name: Salesforce Streaming Api Concurrent Clients Example
  slug: salesforce-streaming-api-concurrent-clients-example
- key_count: 6
  name: Salesforce Streaming Channel Example
  slug: salesforce-streaming-channel-example
- key_count: 31
  name: Salesforce Street Example
  slug: salesforce-street-example
- key_count: 2
  name: Salesforce Street2 Example
  slug: salesforce-street2-example
- key_count: 2
  name: Salesforce Street3 Example
  slug: salesforce-street3-example
- key_count: 7
  name: Salesforce Subject Example
  slug: salesforce-subject-example
- key_count: 19
  name: Salesforce Subscriber Example
  slug: salesforce-subscriber-example
- key_count: 7
  name: Salesforce Succesful User Photo Example
  slug: salesforce-succesful-user-photo-example
- key_count: 1
  name: Salesforce Success Example
  slug: salesforce-success-example
- key_count: 6
  name: Salesforce Success1 Example
  slug: salesforce-success1-example
- key_count: 4
  name: Salesforce Successful Asset Token Flow Example
  slug: salesforce-successful-asset-token-flow-example
- key_count: 9
  name: Salesforce Successful Authentication Configuration Endpoint Example
  slug: salesforce-successful-authentication-configuration-endpoint-example
- key_count: 24
  name: Salesforce Successful Bulk Close Job Example
  slug: salesforce-successful-bulk-close-job-example
- key_count: 24
  name: Salesforce Successful Bulk Create Job Example
  slug: salesforce-successful-bulk-create-job-example
- key_count: 8
  name: Salesforce Successful Client Credentials Flow Basicauthorizationheader Example
  slug: salesforce-successful-client-credentials-flow-basicauthorizationheader-example
- key_count: 8
  name: Salesforce Successful Client Credentials Flow Example
  slug: salesforce-successful-client-credentials-flow-example
- key_count: 10
  name: Salesforce Successful Closeor Aborta Job Example
  slug: salesforce-successful-closeor-aborta-job-example
- key_count: 18
  name: Salesforce Successful Comment Edit Example
  slug: salesforce-successful-comment-edit-example
- key_count: 18
  name: Salesforce Successful Comment Example
  slug: salesforce-successful-comment-example
- key_count: 1
  name: Salesforce Successful Composite Example
  slug: salesforce-successful-composite-example
- key_count: 1
  name: Salesforce Successful Composite Graph Example
  slug: salesforce-successful-composite-graph-example
- key_count: 6
  name: Salesforce Successful Create Credential Example
  slug: salesforce-successful-create-credential-example
- key_count: 10
  name: Salesforce Successful Create External Credential Example
  slug: salesforce-successful-create-external-credential-example
- key_count: 10
  name: Salesforce Successful Create Named Credential Example
  slug: salesforce-successful-create-named-credential-example
- key_count: 13
  name: Salesforce Successful Createjob Example
  slug: salesforce-successful-createjob-example
- key_count: 12
  name: Salesforce Successful Createjob Query Example
  slug: salesforce-successful-createjob-query-example
- key_count: 5
  name: Salesforce Successful Createjob Query Request Example
  slug: salesforce-successful-createjob-query-request-example
- key_count: 9
  name: Salesforce Successful Device Flow2 Example
  slug: salesforce-successful-device-flow2-example
- key_count: 2
  name: Salesforce Successful Feed Elements Batch Post Example
  slug: salesforce-successful-feed-elements-batch-post-example
- key_count: 21
  name: Salesforce Successful Feed Elements Postand Search Example
  slug: salesforce-successful-feed-elements-postand-search-example
- key_count: 21
  name: Salesforce Successful Feed Elements Postand Search1 Example
  slug: salesforce-successful-feed-elements-postand-search1-example
- key_count: 5
  name: Salesforce Successful File Shares Example
  slug: salesforce-successful-file-shares-example
- key_count: 5
  name: Salesforce Successful Files Shares Link Example
  slug: salesforce-successful-files-shares-link-example
- key_count: 5
  name: Salesforce Successful Following Example
  slug: salesforce-successful-following-example
- key_count: 5
  name: Salesforce Successful Following Post Example
  slug: salesforce-successful-following-post-example
- key_count: 3
  name: Salesforce Successful Get All Query Jobs Example
  slug: salesforce-successful-get-all-query-jobs-example
- key_count: 7
  name: Salesforce Successful Get Credential Example
  slug: salesforce-successful-get-credential-example
- key_count: 11
  name: Salesforce Successful Get External Credentialsby Developer Name Example
  slug: salesforce-successful-get-external-credentialsby-developer-name-example
- key_count: 19
  name: Salesforce Successful Get Job Info Example
  slug: salesforce-successful-get-job-info-example
- key_count: 15
  name: Salesforce Successful Get Job Info Query Example
  slug: salesforce-successful-get-job-info-query-example
- key_count: 16
  name: Salesforce Successful Get Job Info Query1 Example
  slug: salesforce-successful-get-job-info-query1-example
- key_count: 10
  name: Salesforce Successful Get Named Credentialby Developer Name Example
  slug: salesforce-successful-get-named-credentialby-developer-name-example
- key_count: 5
  name: Salesforce Successful Group Members Example
  slug: salesforce-successful-group-members-example
- key_count: 2
  name: Salesforce Successful Group Members Private Example
  slug: salesforce-successful-group-members-private-example
- key_count: 8
  name: Salesforce Successful Group Membership Requests Private Example
  slug: salesforce-successful-group-membership-requests-private-example
- key_count: 5
  name: Salesforce Successful Jwt Bearer Token Flow Example
  slug: salesforce-successful-jwt-bearer-token-flow-example
- key_count: 1
  name: Salesforce Successful List External Credentials Example
  slug: salesforce-successful-list-external-credentials-example
- key_count: 1
  name: Salesforce Successful List Named Credentials Example
  slug: salesforce-successful-list-named-credentials-example
- key_count: 4
  name: Salesforce Successful Listof Groups Example
  slug: salesforce-successful-listof-groups-example
- key_count: 25
  name: Salesforce Successful Listof Groups Post Example
  slug: salesforce-successful-listof-groups-post-example
- key_count: 9
  name: Salesforce Successful News Feed Elements Example
  slug: salesforce-successful-news-feed-elements-example
- key_count: 6
  name: Salesforce Successful O Auth Username Password Login Example
  slug: salesforce-successful-o-auth-username-password-login-example
- key_count: 9
  name: Salesforce Successful Record Feed Elements Example
  slug: salesforce-successful-record-feed-elements-example
- key_count: 8
  name: Salesforce Successful Refresh Token Example
  slug: salesforce-successful-refresh-token-example
- key_count: 3
  name: Salesforce Successful S Object Collections Create Example
  slug: salesforce-successful-s-object-collections-create-example
- key_count: 3
  name: Salesforce Successful S Object Collections Delete Example
  slug: salesforce-successful-s-object-collections-delete-example
- key_count: 3
  name: Salesforce Successful S Object Collections Retrieve Example
  slug: salesforce-successful-s-object-collections-retrieve-example
- key_count: 4
  name: Salesforce Successful S Object Collections Upsert Example
  slug: salesforce-successful-s-object-collections-upsert-example
- key_count: 2
  name: Salesforce Successful S Object Tree Example
  slug: salesforce-successful-s-object-tree-example
- key_count: 1
  name: Salesforce Successful Salesforce Keys Example
  slug: salesforce-successful-salesforce-keys-example
- key_count: 10
  name: Salesforce Successful Update External Credential Example
  slug: salesforce-successful-update-external-credential-example
- key_count: 10
  name: Salesforce Successful Update Named Credential Example
  slug: salesforce-successful-update-named-credential-example
- key_count: 24
  name: Salesforce Successful User Info Example
  slug: salesforce-successful-user-info-example
- key_count: 9
  name: Salesforce Successful User Messages General Example
  slug: salesforce-successful-user-messages-general-example
- key_count: 9
  name: Salesforce Successful User Profile Feed Elements Example
  slug: salesforce-successful-user-profile-feed-elements-example
- key_count: 49
  name: Salesforce Successful Users Files General Example
  slug: salesforce-successful-users-files-general-example
- key_count: 9
  name: Salesforce Successful Web Server Flow2 Example
  slug: salesforce-successful-web-server-flow2-example
- key_count: 3
  name: Salesforce Successfull Get All Jobs Example
  slug: salesforce-successfull-get-all-jobs-example
- key_count: 2
  name: Salesforce Supported Scope Example
  slug: salesforce-supported-scope-example
- key_count: 13
  name: Salesforce Symbol Table Example
  slug: salesforce-symbol-table-example
- key_count: 2
  name: Salesforce System Modstamp Example
  slug: salesforce-system-modstamp-example
- key_count: 2
  name: Salesforce System Modstamp10 Example
  slug: salesforce-system-modstamp10-example
- key_count: 31
  name: Salesforce System Modstamp2 Example
  slug: salesforce-system-modstamp2-example
- key_count: 9
  name: Salesforce Tab Example
  slug: salesforce-tab-example
- key_count: 6
  name: Salesforce Table Declaration Example
  slug: salesforce-table-declaration-example
- key_count: 7
  name: Salesforce Test Case Example
  slug: salesforce-test-case-example
- key_count: 2
  name: Salesforce Test Credential Example
  slug: salesforce-test-credential-example
- key_count: 11
  name: Salesforce Test Result Example
  slug: salesforce-test-result-example
- key_count: 2
  name: Salesforce Theme Info Example
  slug: salesforce-theme-info-example
- key_count: 3
  name: Salesforce Theme Item Example
  slug: salesforce-theme-item-example
- key_count: 1
  name: Salesforce Themes Example
  slug: salesforce-themes-example
- key_count: 6
  name: Salesforce Threat Detection Feedback Example
  slug: salesforce-threat-detection-feedback-example
- key_count: 2
  name: Salesforce Ticker Symbol Example
  slug: salesforce-ticker-symbol-example
- key_count: 31
  name: Salesforce Ticker Symbol1 Example
  slug: salesforce-ticker-symbol1-example
- key_count: 2
  name: Salesforce Ticker Symbol2 Example
  slug: salesforce-ticker-symbol2-example
- key_count: 2
  name: Salesforce Tier Example
  slug: salesforce-tier-example
- key_count: 2
  name: Salesforce Tier Group Example
  slug: salesforce-tier-group-example
- key_count: 31
  name: Salesforce Title1 Example
  slug: salesforce-title1-example
- key_count: 2
  name: Salesforce Title4 Example
  slug: salesforce-title4-example
- key_count: 7
  name: Salesforce Tooling Execute Anonymous Example
  slug: salesforce-tooling-execute-anonymous-example
- key_count: 6
  name: Salesforce Tooling Query Example
  slug: salesforce-tooling-query-example
- key_count: 10
  name: Salesforce Tooling Run Tests Sync Example
  slug: salesforce-tooling-run-tests-sync-example
- key_count: 1
  name: Salesforce Tooling Search Example
  slug: salesforce-tooling-search-example
- key_count: 6
  name: Salesforce Topic Assignment Example
  slug: salesforce-topic-assignment-example
- key_count: 6
  name: Salesforce Topic Example
  slug: salesforce-topic-example
- key_count: 3
  name: Salesforce Topics Example
  slug: salesforce-topics-example
- key_count: 2
  name: Salesforce Topics2 Example
  slug: salesforce-topics2-example
- key_count: 2
  name: Salesforce Tradestyle Example
  slug: salesforce-tradestyle-example
- key_count: 31
  name: Salesforce Tradestyle1 Example
  slug: salesforce-tradestyle1-example
- key_count: 4
  name: Salesforce Transaction History Example
  slug: salesforce-transaction-history-example
- key_count: 5
  name: Salesforce Transaction History Request Example
  slug: salesforce-transaction-history-request-example
- key_count: 8
  name: Salesforce Transaction Journal Example
  slug: salesforce-transaction-journal-example
- key_count: 7
  name: Salesforce Transaction Journal2 Example
  slug: salesforce-transaction-journal2-example
- key_count: 6
  name: Salesforce Transaction Journal3 Example
  slug: salesforce-transaction-journal3-example
- key_count: 17
  name: Salesforce Transaction Journal4 Example
  slug: salesforce-transaction-journal4-example
- key_count: 8
  name: Salesforce Transaction Journal5 Example
  slug: salesforce-transaction-journal5-example
- key_count: 1
  name: Salesforce Transaction Journals Execution Request Example
  slug: salesforce-transaction-journals-execution-request-example
- key_count: 2
  name: Salesforce Transaction Journals Simulation Request Example
  slug: salesforce-transaction-journals-simulation-request-example
- key_count: 4
  name: Salesforce Transaction Ledger Summary Example
  slug: salesforce-transaction-ledger-summary-example
- key_count: 6
  name: Salesforce Translation Example
  slug: salesforce-translation-example
- key_count: 1
  name: Salesforce Triggerable Example
  slug: salesforce-triggerable-example
- key_count: 4
  name: Salesforce Type Example
  slug: salesforce-type-example
- key_count: 4
  name: Salesforce Type1 Example
  slug: salesforce-type1-example
- key_count: 2
  name: Salesforce Type10 Example
  slug: salesforce-type10-example
- key_count: 4
  name: Salesforce Type11 Example
  slug: salesforce-type11-example
- key_count: 4
  name: Salesforce Type12 Example
  slug: salesforce-type12-example
- key_count: 2
  name: Salesforce Type13 Example
  slug: salesforce-type13-example
- key_count: 2
  name: Salesforce Type4 Example
  slug: salesforce-type4-example
- key_count: 1
  name: Salesforce Type5 Example
  slug: salesforce-type5-example
- key_count: 31
  name: Salesforce Type7 Example
  slug: salesforce-type7-example
- key_count: 2
  name: Salesforce Ui Error Response Example
  slug: salesforce-ui-error-response-example
- key_count: 8
  name: Salesforce Ui Field Representation Example
  slug: salesforce-ui-field-representation-example
- key_count: 2
  name: Salesforce Ui Field Value Representation Example
  slug: salesforce-ui-field-value-representation-example
- key_count: 5
  name: Salesforce Ui List View Collection Example
  slug: salesforce-ui-list-view-collection-example
- key_count: 4
  name: Salesforce Ui List View Result Example
  slug: salesforce-ui-list-view-result-example
- key_count: 4
  name: Salesforce Ui List View Summary Example
  slug: salesforce-ui-list-view-summary-example
- key_count: 2
  name: Salesforce Ui Lookup Records Collection Example
  slug: salesforce-ui-lookup-records-collection-example
- key_count: 11
  name: Salesforce Ui Object Info Representation Example
  slug: salesforce-ui-object-info-representation-example
- key_count: 4
  name: Salesforce Ui Picklist Value Example
  slug: salesforce-ui-picklist-value-example
- key_count: 1
  name: Salesforce Ui Picklist Values Collection Example
  slug: salesforce-ui-picklist-values-collection-example
- key_count: 2
  name: Salesforce Ui Record Input Example
  slug: salesforce-ui-record-input-example
- key_count: 12
  name: Salesforce Ui Record Representation Example
  slug: salesforce-ui-record-representation-example
- key_count: 1
  name: Salesforce Uiapi Example
  slug: salesforce-uiapi-example
- key_count: 1
  name: Salesforce Uiapi10 Example
  slug: salesforce-uiapi10-example
- key_count: 1
  name: Salesforce Uiapi11 Example
  slug: salesforce-uiapi11-example
- key_count: 1
  name: Salesforce Uiapi12 Example
  slug: salesforce-uiapi12-example
- key_count: 1
  name: Salesforce Uiapi13 Example
  slug: salesforce-uiapi13-example
- key_count: 1
  name: Salesforce Uiapi3 Example
  slug: salesforce-uiapi3-example
- key_count: 1
  name: Salesforce Uiapi4 Example
  slug: salesforce-uiapi4-example
- key_count: 1
  name: Salesforce Uiapi6 Example
  slug: salesforce-uiapi6-example
- key_count: 1
  name: Salesforce Uiapi7 Example
  slug: salesforce-uiapi7-example
- key_count: 1
  name: Salesforce Undeletable Example
  slug: salesforce-undeletable-example
- key_count: 1
  name: Salesforce Undelete Example
  slug: salesforce-undelete-example
- key_count: 1
  name: Salesforce Unenrolla Member Request Example
  slug: salesforce-unenrolla-member-request-example
- key_count: 3
  name: Salesforce Up Down Vote Example
  slug: salesforce-up-down-vote-example
- key_count: 2
  name: Salesforce Upate Account Success Example
  slug: salesforce-upate-account-success-example
- key_count: 1
  name: Salesforce Update Commitment Payments Request Example
  slug: salesforce-update-commitment-payments-request-example
- key_count: 12
  name: Salesforce Update Commitments Request Example
  slug: salesforce-update-commitments-request-example
- key_count: 5
  name: Salesforce Update Credential Request Example
  slug: salesforce-update-credential-request-example
- key_count: 10
  name: Salesforce Update Example
  slug: salesforce-update-example
- key_count: 4
  name: Salesforce Update External Credential Request Example
  slug: salesforce-update-external-credential-request-example
- key_count: 1
  name: Salesforce Update Gift Transaction Payments Request Example
  slug: salesforce-update-gift-transaction-payments-request-example
- key_count: 18
  name: Salesforce Update Last Selected App Example
  slug: salesforce-update-last-selected-app-example
- key_count: 1
  name: Salesforce Update Member Details Request Example
  slug: salesforce-update-member-details-request-example
- key_count: 1
  name: Salesforce Update Member Tier Request Example
  slug: salesforce-update-member-tier-request-example
- key_count: 6
  name: Salesforce Update Named Credential Request Example
  slug: salesforce-update-named-credential-request-example
- key_count: 12
  name: Salesforce Update Table Request Example
  slug: salesforce-update-table-request-example
- key_count: 11
  name: Salesforce Update Usageofa Favorite Example
  slug: salesforce-update-usageofa-favorite-example
- key_count: 2
  name: Salesforce Update1 Example
  slug: salesforce-update1-example
- key_count: 1
  name: Salesforce Updatea Batchof Favorites Example
  slug: salesforce-updatea-batchof-favorites-example
- key_count: 1
  name: Salesforce Updatea Batchof Favorites Request Example
  slug: salesforce-updatea-batchof-favorites-request-example
- key_count: 11
  name: Salesforce Updatea Favorite Example
  slug: salesforce-updatea-favorite-example
- key_count: 2
  name: Salesforce Updatea Favorite Request Example
  slug: salesforce-updatea-favorite-request-example
- key_count: 11
  name: Salesforce Updatea Record Example
  slug: salesforce-updatea-record-example
- key_count: 2
  name: Salesforce Updatea Record Request Example
  slug: salesforce-updatea-record-request-example
- key_count: 1
  name: Salesforce Updateable Example
  slug: salesforce-updateable-example
- key_count: 2
  name: Salesforce Updatechannel Request Example
  slug: salesforce-updatechannel-request-example
- key_count: 2
  name: Salesforce Updateeventrelay Request Example
  slug: salesforce-updateeventrelay-request-example
- key_count: 2
  name: Salesforce Updatemanagedeventsubscription Request Example
  slug: salesforce-updatemanagedeventsubscription-request-example
- key_count: 2
  name: Salesforce Updatenamedcredential Request1 Example
  slug: salesforce-updatenamedcredential-request1-example
- key_count: 1
  name: Salesforce Upsell Opportunity C Example
  slug: salesforce-upsell-opportunity-c-example
- key_count: 31
  name: Salesforce Upsell Opportunity C1 Example
  slug: salesforce-upsell-opportunity-c1-example
- key_count: 2
  name: Salesforce Upsell Opportunity C2 Example
  slug: salesforce-upsell-opportunity-c2-example
- key_count: 2
  name: Salesforce Upsell Opportunity C4 Example
  slug: salesforce-upsell-opportunity-c4-example
- key_count: 19
  name: Salesforce User Example
  slug: salesforce-user-example
- key_count: 31
  name: Salesforce User Permissions Call Center Auto Login Example
  slug: salesforce-user-permissions-call-center-auto-login-example
- key_count: 31
  name: Salesforce User Permissions Interaction User Example
  slug: salesforce-user-permissions-interaction-user-example
- key_count: 31
  name: Salesforce User Permissions Jigsaw Prospecting User Example
  slug: salesforce-user-permissions-jigsaw-prospecting-user-example
- key_count: 31
  name: Salesforce User Permissions Knowledge User Example
  slug: salesforce-user-permissions-knowledge-user-example
- key_count: 31
  name: Salesforce User Permissions Marketing User Example
  slug: salesforce-user-permissions-marketing-user-example
- key_count: 31
  name: Salesforce User Permissions Offline User Example
  slug: salesforce-user-permissions-offline-user-example
- key_count: 31
  name: Salesforce User Permissions Sf Content User Example
  slug: salesforce-user-permissions-sf-content-user-example
- key_count: 31
  name: Salesforce User Permissions Siteforce Contributor User Example
  slug: salesforce-user-permissions-siteforce-contributor-user-example
- key_count: 31
  name: Salesforce User Permissions Siteforce Publisher User Example
  slug: salesforce-user-permissions-siteforce-publisher-user-example
- key_count: 31
  name: Salesforce User Permissions Support User Example
  slug: salesforce-user-permissions-support-user-example
- key_count: 31
  name: Salesforce User Permissions Work Dot Com User Feature Example
  slug: salesforce-user-permissions-work-dot-com-user-feature-example
- key_count: 31
  name: Salesforce User Preferences Activity Reminders Popup Example
  slug: salesforce-user-preferences-activity-reminders-popup-example
- key_count: 31
  name: Salesforce User Preferences Apex Pages Developer Mode Example
  slug: salesforce-user-preferences-apex-pages-developer-mode-example
- key_count: 31
  name: Salesforce User Preferences Cache Diagnostics Example
  slug: salesforce-user-preferences-cache-diagnostics-example
- key_count: 31
  name: Salesforce User Preferences Create Lex Apps Wt Shown Example
  slug: salesforce-user-preferences-create-lex-apps-wt-shown-example
- key_count: 31
  name: Salesforce User Preferences Dedupe Storage Migration Complete Example
  slug: salesforce-user-preferences-dedupe-storage-migration-complete-example
- key_count: 31
  name: Salesforce User Preferences Disable File Share Notifications For Api Example
  slug: salesforce-user-preferences-disable-file-share-notifications-for-api-example
- key_count: 31
  name: Salesforce User Preferences Enable Auto Sub For Feeds Example
  slug: salesforce-user-preferences-enable-auto-sub-for-feeds-example
- key_count: 31
  name: Salesforce User Preferences Event Reminders Checkbox Default Example
  slug: salesforce-user-preferences-event-reminders-checkbox-default-example
- key_count: 2
  name: Salesforce User Preferences Example
  slug: salesforce-user-preferences-example
- key_count: 31
  name: Salesforce User Preferences Favorites Show Top Favorites Example
  slug: salesforce-user-preferences-favorites-show-top-favorites-example
- key_count: 31
  name: Salesforce User Preferences Favorites Wt Shown Example
  slug: salesforce-user-preferences-favorites-wt-shown-example
- key_count: 31
  name: Salesforce User Preferences First Time In Lightning Example
  slug: salesforce-user-preferences-first-time-in-lightning-example
- key_count: 31
  name: Salesforce User Preferences Global Nav Bar Wt Shown Example
  slug: salesforce-user-preferences-global-nav-bar-wt-shown-example
- key_count: 31
  name: Salesforce User Preferences Has Celebration Badge Example
  slug: salesforce-user-preferences-has-celebration-badge-example
- key_count: 31
  name: Salesforce User Preferences Heavy Page Prompt Enabled Example
  slug: salesforce-user-preferences-heavy-page-prompt-enabled-example
- key_count: 31
  name: Salesforce User Preferences Jigsaw List User Example
  slug: salesforce-user-preferences-jigsaw-list-user-example
- key_count: 31
  name: Salesforce User Preferences Lightning Experience Preferred Example
  slug: salesforce-user-preferences-lightning-experience-preferred-example
- key_count: 31
  name: Salesforce User Preferences Ltng Promo Reserved10 User Pref Example
  slug: salesforce-user-preferences-ltng-promo-reserved10-user-pref-example
- key_count: 31
  name: Salesforce User Preferences Ltng Promo Reserved16 User Pref Example
  slug: salesforce-user-preferences-ltng-promo-reserved16-user-pref-example
- key_count: 31
  name: Salesforce User Preferences Ltng Promo Reserved19 User Pref Example
  slug: salesforce-user-preferences-ltng-promo-reserved19-user-pref-example
- key_count: 31
  name: Salesforce User Preferences New Lightning Report Run Page Enabled Example
  slug: salesforce-user-preferences-new-lightning-report-run-page-enabled-example
- key_count: 31
  name: Salesforce User Preferences Path Assistant Collapsed Example
  slug: salesforce-user-preferences-path-assistant-collapsed-example
- key_count: 31
  name: Salesforce User Preferences Preview Custom Theme Example
  slug: salesforce-user-preferences-preview-custom-theme-example
- key_count: 31
  name: Salesforce User Preferences Preview Lightning Example
  slug: salesforce-user-preferences-preview-lightning-example
- key_count: 31
  name: Salesforce User Preferences Read Receipt Last Toggle Value Example
  slug: salesforce-user-preferences-read-receipt-last-toggle-value-example
- key_count: 31
  name: Salesforce User Preferences Receive No Notifications As Approver Example
  slug: salesforce-user-preferences-receive-no-notifications-as-approver-example
- key_count: 31
  name: Salesforce User Preferences Receive Notifications As Delegated Approver Example
  slug: salesforce-user-preferences-receive-notifications-as-delegated-approver-example
- key_count: 31
  name: Salesforce User Preferences Record Home Reserved Wt Shown Example
  slug: salesforce-user-preferences-record-home-reserved-wt-shown-example
- key_count: 31
  name: Salesforce User Preferences Record Home Section Collapse Wt Shown Example
  slug: salesforce-user-preferences-record-home-section-collapse-wt-shown-example
- key_count: 31
  name: Salesforce User Preferences Reminder Sound Off Example
  slug: salesforce-user-preferences-reminder-sound-off-example
- key_count: 31
  name: Salesforce User Preferences Reverse Open Activities View Example
  slug: salesforce-user-preferences-reverse-open-activities-view-example
- key_count: 31
  name: Salesforce User Preferences Sales Essentials Setup Assistant Completed Example
  slug: salesforce-user-preferences-sales-essentials-setup-assistant-completed-example
- key_count: 31
  name: Salesforce User Preferences Setup Assistant User Pref1 Example
  slug: salesforce-user-preferences-setup-assistant-user-pref1-example
- key_count: 31
  name: Salesforce User Preferences Show City To External Users Example
  slug: salesforce-user-preferences-show-city-to-external-users-example
- key_count: 31
  name: Salesforce User Preferences Show City To Guest Users Example
  slug: salesforce-user-preferences-show-city-to-guest-users-example
- key_count: 31
  name: Salesforce User Preferences Show Country To External Users Example
  slug: salesforce-user-preferences-show-country-to-external-users-example
- key_count: 31
  name: Salesforce User Preferences Show Country To Guest Users Example
  slug: salesforce-user-preferences-show-country-to-guest-users-example
- key_count: 31
  name: Salesforce User Preferences Show Fax To External Users Example
  slug: salesforce-user-preferences-show-fax-to-external-users-example
- key_count: 31
  name: Salesforce User Preferences Show Fax To Guest Users Example
  slug: salesforce-user-preferences-show-fax-to-guest-users-example
- key_count: 31
  name: Salesforce User Preferences Show Forecasting Change Signals Example
  slug: salesforce-user-preferences-show-forecasting-change-signals-example
- key_count: 31
  name: Salesforce User Preferences Show Manager To External Users Example
  slug: salesforce-user-preferences-show-manager-to-external-users-example
- key_count: 31
  name: Salesforce User Preferences Show Manager To Guest Users Example
  slug: salesforce-user-preferences-show-manager-to-guest-users-example
- key_count: 31
  name: Salesforce User Preferences Show Mobile Phone To External Users Example
  slug: salesforce-user-preferences-show-mobile-phone-to-external-users-example
- key_count: 31
  name: Salesforce User Preferences Show Mobile Phone To Guest Users Example
  slug: salesforce-user-preferences-show-mobile-phone-to-guest-users-example
- key_count: 31
  name: Salesforce User Preferences Show Postal Code To External Users Example
  slug: salesforce-user-preferences-show-postal-code-to-external-users-example
- key_count: 31
  name: Salesforce User Preferences Show Postal Code To Guest Users Example
  slug: salesforce-user-preferences-show-postal-code-to-guest-users-example
- key_count: 31
  name: Salesforce User Preferences Show Profile Pic To Guest Users Example
  slug: salesforce-user-preferences-show-profile-pic-to-guest-users-example
- key_count: 31
  name: Salesforce User Preferences Show State To External Users Example
  slug: salesforce-user-preferences-show-state-to-external-users-example
- key_count: 31
  name: Salesforce User Preferences Show State To Guest Users Example
  slug: salesforce-user-preferences-show-state-to-guest-users-example
- key_count: 31
  name: Salesforce User Preferences Show Street Address To External Users Example
  slug: salesforce-user-preferences-show-street-address-to-external-users-example
- key_count: 31
  name: Salesforce User Preferences Show Street Address To Guest Users Example
  slug: salesforce-user-preferences-show-street-address-to-guest-users-example
- key_count: 31
  name: Salesforce User Preferences Show Title To External Users Example
  slug: salesforce-user-preferences-show-title-to-external-users-example
- key_count: 31
  name: Salesforce User Preferences Show Title To Guest Users Example
  slug: salesforce-user-preferences-show-title-to-guest-users-example
- key_count: 31
  name: Salesforce User Preferences Show Work Phone To External Users Example
  slug: salesforce-user-preferences-show-work-phone-to-external-users-example
- key_count: 31
  name: Salesforce User Preferences Show Work Phone To Guest Users Example
  slug: salesforce-user-preferences-show-work-phone-to-guest-users-example
- key_count: 31
  name: Salesforce User Preferences Sort Feed By Comment Example
  slug: salesforce-user-preferences-sort-feed-by-comment-example
- key_count: 31
  name: Salesforce User Preferences Suppress Event Sfx Reminders Example
  slug: salesforce-user-preferences-suppress-event-sfx-reminders-example
- key_count: 31
  name: Salesforce User Preferences Suppress Task Sfx Reminders Example
  slug: salesforce-user-preferences-suppress-task-sfx-reminders-example
- key_count: 31
  name: Salesforce User Preferences Task Reminders Checkbox Default Example
  slug: salesforce-user-preferences-task-reminders-checkbox-default-example
- key_count: 31
  name: Salesforce User Preferences Today Getting Started Example
  slug: salesforce-user-preferences-today-getting-started-example
- key_count: 31
  name: Salesforce User Preferences Trailhead Badge Created Example
  slug: salesforce-user-preferences-trailhead-badge-created-example
- key_count: 31
  name: Salesforce User Preferences User Debug Mode Pref Example
  slug: salesforce-user-preferences-user-debug-mode-pref-example
- key_count: 6
  name: Salesforce User Role Example
  slug: salesforce-user-role-example
- key_count: 31
  name: Salesforce User Type Example
  slug: salesforce-user-type-example
- key_count: 19
  name: Salesforce User3 Example
  slug: salesforce-user3-example
- key_count: 19
  name: Salesforce User4 Example
  slug: salesforce-user4-example
- key_count: 23
  name: Salesforce User7 Example
  slug: salesforce-user7-example
- key_count: 6
  name: Salesforce User8 Example
  slug: salesforce-user8-example
- key_count: 4
  name: Salesforce Userdata Example
  slug: salesforce-userdata-example
- key_count: 31
  name: Salesforce Username Example
  slug: salesforce-username-example
- key_count: 11
  name: Salesforce Value Example
  slug: salesforce-value-example
- key_count: 11
  name: Salesforce Value2 Example
  slug: salesforce-value2-example
- key_count: 10
  name: Salesforce Value22 Example
  slug: salesforce-value22-example
- key_count: 4
  name: Salesforce Value6 Example
  slug: salesforce-value6-example
- key_count: 8
  name: Salesforce Variable Example
  slug: salesforce-variable-example
- key_count: 5
  name: Salesforce Verified Example
  slug: salesforce-verified-example
- key_count: 9
  name: Salesforce Version Example
  slug: salesforce-version-example
- key_count: 11
  name: Salesforce Version2 Example
  slug: salesforce-version2-example
- key_count: 3
  name: Salesforce Version5 Example
  slug: salesforce-version5-example
- key_count: 8
  name: Salesforce View Example
  slug: salesforce-view-example
- key_count: 2
  name: Salesforce Warnings Example
  slug: salesforce-warnings-example
- key_count: 2
  name: Salesforce Website Example
  slug: salesforce-website-example
- key_count: 31
  name: Salesforce Website1 Example
  slug: salesforce-website1-example
- key_count: 2
  name: Salesforce Website2 Example
  slug: salesforce-website2-example
- key_count: 2
  name: Salesforce Website5 Example
  slug: salesforce-website5-example
- key_count: 6
  name: Salesforce Work Badge Definition History Example
  slug: salesforce-work-badge-definition-history-example
- key_count: 2
  name: Salesforce Year Started Example
  slug: salesforce-year-started-example
- key_count: 31
  name: Salesforce Year Started1 Example
  slug: salesforce-year-started1-example
features:
- 'Sales Cloud editions: Starter $25, Pro $65, Enterprise $175, Unlimited $350, Agentforce 1 $550 per user/mo'
- Service Cloud, Marketing Cloud, Commerce Cloud, Data Cloud, Tableau
- REST API, SOAP API, Bulk API v1/v2, Streaming/CDC API, Composite API
- Apex programming language and Lightning Web Components
- AppExchange marketplace
- 'Daily API calls: 100k Pro, 1M Enterprise, 5M Unlimited'
- 'Concurrent long-running API calls: 25 (75 on Performance/Unlimited)'
- 'Bulk API v1 batches: 15,000/day'
- 'Streaming events: 250k/day'
- Sandbox environments (Developer/Partial/Full)
- Salesforce DX for source-driven development
- Einstein Predictions and Generative AI (edition-gated)
- Salesforce Data Cloud (CDP) with credit-based metering
- Multi-org architecture for large enterprises
- Industry Clouds (Financial, Health, Manufacturing, etc.)
- Mulesoft for integration (separate licensing)
finops:
- name: Salesforce Finops
  service_category: CRM
  slug: salesforce-finops
graphqls:
- description: The Salesforce GraphQL API provides a GraphQL interface to query and mutate Salesforce data. It allows clients to request exactly the data they need in a single request, reducing over-fetching and und
  name: Salesforce GraphQL API
  slug: salesforce-graphql
image: https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg
integrations:
- description: Native integration platform for connecting Salesforce with any application, data source, or API.
  name: MuleSoft Anypoint
- description: Advanced analytics and data visualization through the Tableau REST API and Salesforce data connectors.
  name: Tableau
- description: Embed Salesforce data and workflows into Slack channels for team collaboration.
  name: Slack
- description: Deploy custom applications on Heroku with direct Salesforce data synchronization via Heroku Connect.
  name: Heroku
- description: AWS integrations for Service Cloud Voice with Amazon Connect and Data Cloud event bridges.
  name: Amazon Web Services
- description: BigQuery connectors and Google Workspace integrations for analytics and productivity.
  name: Google Cloud
- description: Outlook and Teams integrations for email tracking, calendar sync, and collaborative selling.
  name: Microsoft
- description: Thousands of pre-built integrations and applications available through the Salesforce AppExchange marketplace.
  name: AppExchange Partners
json_schemas:
- name: 0F94H000000UF2xSAG
  property_count: 3
  slug: salesforce-0-f94-h000000-uf2x-sag
- name: 00B58000002ssinEAA
  property_count: 3
  slug: salesforce-00-b58000002ssin-eaa
- name: 00QB0000003pOQsMAM
  property_count: 11
  slug: salesforce-00-qb0000003p-o-qs-mam
- name: 00QB0000003pORDMA2
  property_count: 11
  slug: salesforce-00-qb0000003p-ordma2
- name: 0014H00002LbR7QQAV
  property_count: 3
  slug: salesforce-0014-h00002-lb-r7-qqav
- name: 0014H00002LbR7QQAV1
  property_count: 3
  slug: salesforce-0014-h00002-lb-r7-qqav1
- name: 00158000006QBOhAAO
  property_count: 3
  slug: salesforce-00158000006-qb-oh-aao
- name: 00158000006QBOhAAO1
  property_count: 3
  slug: salesforce-00158000006-qb-oh-aao1
- name: 00158000006QBOhAAO2
  property_count: 3
  slug: salesforce-00158000006-qb-oh-aao2
- name: 00358000006woxwAAA
  property_count: 3
  slug: salesforce-00358000006woxw-aaa
- name: 00hB0000000JrBRIA0
  property_count: 2
  slug: salesforce-00h-b0000000-jr-bria0
- name: 01BB0000002rP3IMAU
  property_count: 2
  slug: salesforce-01-bb0000002r-p3-imau
- name: 01BB0000002rP3JMAU
  property_count: 2
  slug: salesforce-01-bb0000002r-p3-jmau
- name: 01BB0000002rP3LMAU
  property_count: 2
  slug: salesforce-01-bb0000002r-p3-lmau
- name: 01BB0000002rP3MMAU
  property_count: 2
  slug: salesforce-01-bb0000002r-p3-mmau
- name: 01BB0000002rP3NMAU
  property_count: 2
  slug: salesforce-01-bb0000002r-p3-nmau
- name: 012000000000000AAA
  property_count: 1
  slug: salesforce-012000000000000-aaa
- name: 012000000000000AAA1
  property_count: 5
  slug: salesforce-012000000000000-aaa1
- name: 404-BecauseVersion59.0NotPresentInTargetOrg1
  property_count: 2
  slug: salesforce-404-because-version59.0-not-present-in-target-org1
- name: AbortaJobQueryRequest
  property_count: 1
  slug: salesforce-aborta-job-query-request
- name: AbortaJobQuery
  property_count: 10
  slug: salesforce-aborta-job-query
- name: AboutMe
  property_count: 31
  slug: salesforce-about-me
- name: AccessRecords
  property_count: 19
  slug: salesforce-access-records
- name: AccountBrand
  property_count: 6
  slug: salesforce-account-brand
- name: AccountCreate
  property_count: 1
  slug: salesforce-account-create
- name: AccountCustomField
  property_count: 2
  slug: salesforce-account-custom-field
- name: AccountDelete
  property_count: 1
  slug: salesforce-account-delete
- name: AccountHistory
  property_count: 6
  slug: salesforce-account-history
- name: AccountId
  property_count: 2
  slug: salesforce-account-id
- name: AccountId1
  property_count: 31
  slug: salesforce-account-id1
- name: AccountId2
  property_count: 2
  slug: salesforce-account-id2
- name: AccountNumber
  property_count: 2
  slug: salesforce-account-number
- name: AccountNumber1
  property_count: 31
  slug: salesforce-account-number1
- name: AccountNumber2
  property_count: 2
  slug: salesforce-account-number2
- name: AccountNumber4
  property_count: 2
  slug: salesforce-account-number4
- name: AccountPartner
  property_count: 6
  slug: salesforce-account-partner
- name: AccountSObject
  property_count: 3
  slug: salesforce-account-s-object
- name: Account
  property_count: 2
  slug: salesforce-account
- name: AccountSource
  property_count: 2
  slug: salesforce-account-source
- name: AccountSource1
  property_count: 31
  slug: salesforce-account-source1
- name: AccountUpdate
  property_count: 1
  slug: salesforce-account-update
- name: Account10
  property_count: 3
  slug: salesforce-account10
- name: Account11
  property_count: 1
  slug: salesforce-account11
- name: Account12
  property_count: 6
  slug: salesforce-account12
- name: Account13
  property_count: 23
  slug: salesforce-account13
- name: Account15
  property_count: 8
  slug: salesforce-account15
- name: Account16
  property_count: 4
  slug: salesforce-account16
- name: Account17
  property_count: 3
  slug: salesforce-account17
- name: Account18
  property_count: 3
  slug: salesforce-account18
- name: Account7
  property_count: 1
  slug: salesforce-account7
- name: AccountbyId
  property_count: 2
  slug: salesforce-accountby-id
- name: Accounts
  property_count: 2
  slug: salesforce-accounts
- name: AccountswithCursorsPagination
  property_count: 2
  slug: salesforce-accountswith-cursors-pagination
- name: AccountswithFilter
  property_count: 2
  slug: salesforce-accountswith-filter
- name: ActionOverride
  property_count: 5
  slug: salesforce-action-override
- name: Actions
  property_count: 1
  slug: salesforce-actions
- name: Actions1
  property_count: 19
  slug: salesforce-actions1
- name: Actions10
  property_count: 19
  slug: salesforce-actions10
- name: Actions11
  property_count: 1
  slug: salesforce-actions11
- name: Actions12
  property_count: 19
  slug: salesforce-actions12
- name: Actions13
  property_count: 1
  slug: salesforce-actions13
- name: Actions14
  property_count: 19
  slug: salesforce-actions14
- name: Actions15
  property_count: 1
  slug: salesforce-actions15
- name: Actions17
  property_count: 1
  slug: salesforce-actions17
- name: Actions18
  property_count: 19
  slug: salesforce-actions18
- name: Actions19
  property_count: 1
  slug: salesforce-actions19
- name: Actions2
  property_count: 2
  slug: salesforce-actions2
- name: Actions21
  property_count: 1
  slug: salesforce-actions21
- name: Actions22
  property_count: 19
  slug: salesforce-actions22
- name: Actions23
  property_count: 1
  slug: salesforce-actions23
- name: Actions24
  property_count: 19
  slug: salesforce-actions24
- name: Actions3
  property_count: 19
  slug: salesforce-actions3
- name: Actions5
  property_count: 1
  slug: salesforce-actions5
- name: Actions6
  property_count: 19
  slug: salesforce-actions6
- name: Actions7
  property_count: 1
  slug: salesforce-actions7
- name: Actions8
  property_count: 19
  slug: salesforce-actions8
- name: Actions9
  property_count: 1
  slug: salesforce-actions9
- name: Activateable
  property_count: 1
  slug: salesforce-activateable
- name: ActiveC
  property_count: 1
  slug: salesforce-active-c
- name: ActiveC1
  property_count: 31
  slug: salesforce-active-c1
- name: ActiveC2
  property_count: 2
  slug: salesforce-active-c2
- name: ActiveC4
  property_count: 2
  slug: salesforce-active-c4
- name: ActiveScratchOrgHistory
  property_count: 6
  slug: salesforce-active-scratch-org-history
- name: ActiveScratchOrg
  property_count: 6
  slug: salesforce-active-scratch-org
- name: ActiveScratchOrgs
  property_count: 2
  slug: salesforce-active-scratch-orgs
- name: Actor
  property_count: 19
  slug: salesforce-actor
- name: AddanitemtoacartRequest
  property_count: 3
  slug: salesforce-addanitemtoacart-request
- name: AddenrichedfieldstochannelmemberRequest
  property_count: 2
  slug: salesforce-addenrichedfieldstochannelmember-request
- name: AddfilterexpressioninchannelmemberRequest
  property_count: 2
  slug: salesforce-addfilterexpressioninchannelmember-request
- name: AdditionalData
  property_count: 2
  slug: salesforce-additional-data
- name: AdditionalFieldValues
  property_count: 1
  slug: salesforce-additional-field-values
- name: AdditionalLoyaltyMemberCurrencyFields
  property_count: 1
  slug: salesforce-additional-loyalty-member-currency-fields
- name: AdditionalProperties
  property_count: 1
  slug: salesforce-additional-properties
- name: Address
  property_count: 1
  slug: salesforce-address
- name: Address1
  property_count: 6
  slug: salesforce-address1
- name: Address5
  property_count: 31
  slug: salesforce-address5
- name: AggregationResults
  property_count: 1
  slug: salesforce-aggregation-results
- name: Alias
  property_count: 31
  slug: salesforce-alias
- name: Alias4
  property_count: 2
  slug: salesforce-alias4
- name: AnalyticsExternalDataSizeMB
  property_count: 2
  slug: salesforce-analytics-external-data-size-mb
- name: Annotation
  property_count: 1
  slug: salesforce-annotation
- name: AnnualRevenue
  property_count: 2
  slug: salesforce-annual-revenue
- name: AnnualRevenue1
  property_count: 31
  slug: salesforce-annual-revenue1
- name: AnnualRevenue2
  property_count: 2
  slug: salesforce-annual-revenue2
- name: AnnualRevenue3
  property_count: 2
  slug: salesforce-annual-revenue3
- name: ApiAnomalyEventStore
  property_count: 6
  slug: salesforce-api-anomaly-event-store
- name: AppAnalyticsQueryRequest
  property_count: 6
  slug: salesforce-app-analytics-query-request
- name: AppMenuItem
  property_count: 6
  slug: salesforce-app-menu-item
- name: AppMenu
  property_count: 3
  slug: salesforce-app-menu
- name: App
  property_count: 18
  slug: salesforce-app
- name: ApplicationJson
  property_count: 1
  slug: salesforce-application-json
- name: ApplicationJson1
  property_count: 1
  slug: salesforce-application-json1
- name: AppliedPromotion
  property_count: 2
  slug: salesforce-applied-promotion
- name: AssetHistory
  property_count: 6
  slug: salesforce-asset-history
- name: AssetIds
  property_count: 1
  slug: salesforce-asset-ids
- name: AssetRelationshipHistory
  property_count: 6
  slug: salesforce-asset-relationship-history
- name: AssetRelationship
  property_count: 6
  slug: salesforce-asset-relationship
- name: Asset
  property_count: 6
  slug: salesforce-asset
- name: Assignment
  property_count: 2
  slug: salesforce-assignment
- name: AssistantName
  property_count: 2
  slug: salesforce-assistant-name
- name: AssistantPhone
  property_count: 2
  slug: salesforce-assistant-phone
- name: AssociateEntityType
  property_count: 1
  slug: salesforce-associate-entity-type
- name: AssociateParentEntity
  property_count: 1
  slug: salesforce-associate-parent-entity
- name: AssociatedAccountDetails
  property_count: 4
  slug: salesforce-associated-account-details
- name: AssociatedActions
  property_count: 1
  slug: salesforce-associated-actions
- name: AssociatedContactDetails
  property_count: 4
  slug: salesforce-associated-contact-details
- name: AssociatedContact
  property_count: 4
  slug: salesforce-associated-contact
- name: Attributes
  property_count: 2
  slug: salesforce-attributes
- name: Attributes14
  property_count: 1
  slug: salesforce-attributes14
- name: Attributes15
  property_count: 2
  slug: salesforce-attributes15
- name: Attributes22
  property_count: 2
  slug: salesforce-attributes22
- name: Attributes29
  property_count: 3
  slug: salesforce-attributes29
- name: Attributes3
  property_count: 1
  slug: salesforce-attributes3
- name: Attributes35
  property_count: 2
  slug: salesforce-attributes35
- name: Attributes4
  property_count: 2
  slug: salesforce-attributes4
- name: AuthorizationCode
  property_count: 3
  slug: salesforce-authorization-code
- name: AuthorizationFormConsentHistory
  property_count: 6
  slug: salesforce-authorization-form-consent-history
- name: AuthorizationFormConsent
  property_count: 6
  slug: salesforce-authorization-form-consent
- name: AuthorizationFormDataUseHistory
  property_count: 6
  slug: salesforce-authorization-form-data-use-history
- name: AuthorizationFormDataUse
  property_count: 6
  slug: salesforce-authorization-form-data-use
- name: AuthorizationFormHistory
  property_count: 6
  slug: salesforce-authorization-form-history
- name: AuthorizationForm
  property_count: 6
  slug: salesforce-authorization-form
- name: AuthorizationFormTextHistory
  property_count: 6
  slug: salesforce-authorization-form-text-history
- name: AuthorizationFormText
  property_count: 6
  slug: salesforce-authorization-form-text
- name: BackgroundOperation
  property_count: 6
  slug: salesforce-background-operation
- name: BadgeText
  property_count: 31
  slug: salesforce-badge-text
- name: BannerPhotoId
  property_count: 31
  slug: salesforce-banner-photo-id
- name: BannerPhoto
  property_count: 3
  slug: salesforce-banner-photo
- name: BannerPhotoUrl
  property_count: 31
  slug: salesforce-banner-photo-url
- name: batchInfoList
  property_count: 1
  slug: salesforce-batch-info-list
- name: batchInfo
  property_count: 10
  slug: salesforce-batch-info
- name: BatchRequest
  property_count: 2
  slug: salesforce-batch-request
- name: BearerAuth
  property_count: 3
  slug: salesforce-bearer-auth
- name: BillingAddress
  property_count: 2
  slug: salesforce-billing-address
- name: BillingAddress1
  property_count: 8
  slug: salesforce-billing-address1
- name: BillingAddress2
  property_count: 31
  slug: salesforce-billing-address2
- name: BillingCity
  property_count: 2
  slug: salesforce-billing-city
- name: BillingCity1
  property_count: 31
  slug: salesforce-billing-city1
- name: BillingCity2
  property_count: 2
  slug: salesforce-billing-city2
- name: BillingCity3
  property_count: 2
  slug: salesforce-billing-city3
- name: BillingCountry
  property_count: 2
  slug: salesforce-billing-country
- name: BillingCountry1
  property_count: 31
  slug: salesforce-billing-country1
- name: BillingCountry2
  property_count: 2
  slug: salesforce-billing-country2
- name: BillingCountry3
  property_count: 2
  slug: salesforce-billing-country3
- name: BillingGeocodeAccuracy
  property_count: 2
  slug: salesforce-billing-geocode-accuracy
- name: BillingGeocodeAccuracy1
  property_count: 31
  slug: salesforce-billing-geocode-accuracy1
- name: BillingLatitude
  property_count: 2
  slug: salesforce-billing-latitude
- name: BillingLatitude1
  property_count: 31
  slug: salesforce-billing-latitude1
- name: BillingLongitude
  property_count: 2
  slug: salesforce-billing-longitude
- name: BillingLongitude1
  property_count: 31
  slug: salesforce-billing-longitude1
- name: BillingPostalCode
  property_count: 2
  slug: salesforce-billing-postal-code
- name: BillingPostalCode1
  property_count: 31
  slug: salesforce-billing-postal-code1
- name: BillingPostalCode2
  property_count: 2
  slug: salesforce-billing-postal-code2
- name: BillingPostalCode3
  property_count: 2
  slug: salesforce-billing-postal-code3
- name: BillingState
  property_count: 2
  slug: salesforce-billing-state
- name: BillingState1
  property_count: 31
  slug: salesforce-billing-state1
- name: BillingState2
  property_count: 2
  slug: salesforce-billing-state2
- name: BillingState3
  property_count: 2
  slug: salesforce-billing-state3
- name: BillingStreet
  property_count: 2
  slug: salesforce-billing-street
- name: BillingStreet1
  property_count: 31
  slug: salesforce-billing-street1
- name: BillingStreet2
  property_count: 2
  slug: salesforce-billing-street2
- name: BillingStreet3
  property_count: 2
  slug: salesforce-billing-street3
- name: Birthdate
  property_count: 3
  slug: salesforce-birthdate
- name: Body
  property_count: 3
  slug: salesforce-body
- name: Body1
  property_count: 3
  slug: salesforce-body1
- name: Body11
  property_count: 3
  slug: salesforce-body11
- name: Body12
  property_count: 1
  slug: salesforce-body12
- name: Body14
  property_count: 3
  slug: salesforce-body14
- name: Body15
  property_count: 3
  slug: salesforce-body15
- name: Body16
  property_count: 1
  slug: salesforce-body16
- name: Body17
  property_count: 1
  slug: salesforce-body17
- name: Body18
  property_count: 1
  slug: salesforce-body18
- name: Body19
  property_count: 1
  slug: salesforce-body19
- name: Body2
  property_count: 2
  slug: salesforce-body2
- name: Body20
  property_count: 1
  slug: salesforce-body20
- name: Body21
  property_count: 1
  slug: salesforce-body21
- name: Body22
  property_count: 1
  slug: salesforce-body22
- name: Body23
  property_count: 1
  slug: salesforce-body23
- name: Body24
  property_count: 16
  slug: salesforce-body24
- name: Body25
  property_count: 23
  slug: salesforce-body25
- name: Body26
  property_count: 21
  slug: salesforce-body26
- name: Body4
  property_count: 3
  slug: salesforce-body4
- name: Body5
  property_count: 1
  slug: salesforce-body5
- name: Body6
  property_count: 3
  slug: salesforce-body6
- name: Body7
  property_count: 1
  slug: salesforce-body7
- name: Bookmarks
  property_count: 1
  slug: salesforce-bookmarks
- name: BrandImage
  property_count: 3
  slug: salesforce-brand-image
- name: Error
  property_count: 3
  slug: salesforce-bulk-2-error
- name: IngestJobInfo
  property_count: 17
  slug: salesforce-bulk-2-ingest-job-info
- name: IngestJobRequest
  property_count: 7
  slug: salesforce-bulk-2-ingest-job-request
- name: JobState
  property_count: 0
  slug: salesforce-bulk-2-job-state
- name: QueryJobInfo
  property_count: 15
  slug: salesforce-bulk-2-query-job-info
- name: QueryJobRequest
  property_count: 5
  slug: salesforce-bulk-2-query-job-request
- name: BulkCloseJobRequest
  property_count: 1
  slug: salesforce-bulk-close-job-request
- name: BulkCreateJobRequest
  property_count: 3
  slug: salesforce-bulk-create-job-request
- name: Salesforce Bulk API 2.0 Job
  property_count: 19
  slug: salesforce-bulk-job
- name: BusinessBrand
  property_count: 6
  slug: salesforce-business-brand
- name: BusinessHours
  property_count: 6
  slug: salesforce-business-hours
- name: CalculatePriceNewSaleBundlesRequest
  property_count: 4
  slug: salesforce-calculate-price-new-sale-bundles-request
- name: CalculatePriceNewSaleRequest
  property_count: 3
  slug: salesforce-calculate-price-new-sale-request
- name: CalculatePriceNewSalewithDiscountsRequest
  property_count: 3
  slug: salesforce-calculate-price-new-salewith-discounts-request
- name: CallCenterId
  property_count: 31
  slug: salesforce-call-center-id
- name: CalloutOptions
  property_count: 3
  slug: salesforce-callout-options
- name: CampaignHistory
  property_count: 6
  slug: salesforce-campaign-history
- name: CampaignMember
  property_count: 6
  slug: salesforce-campaign-member
- name: CampaignMemberStatus
  property_count: 6
  slug: salesforce-campaign-member-status
- name: Campaign
  property_count: 1
  slug: salesforce-campaign
- name: Campaign4
  property_count: 6
  slug: salesforce-campaign4
- name: CancelaVoucherRequest
  property_count: 1
  slug: salesforce-cancela-voucher-request
- name: Capabilities
  property_count: 12
  slug: salesforce-capabilities
- name: Capabilities1
  property_count: 1
  slug: salesforce-capabilities1
- name: Capabilities6
  property_count: 4
  slug: salesforce-capabilities6
- name: Capabilities8
  property_count: 4
  slug: salesforce-capabilities8
- name: CardPaymentMethod
  property_count: 11
  slug: salesforce-card-payment-method
- name: CartDetail
  property_count: 5
  slug: salesforce-cart-detail
- name: CartLineDetail
  property_count: 4
  slug: salesforce-cart-line-detail
- name: Cart
  property_count: 1
  slug: salesforce-cart
- name: CaseComment
  property_count: 6
  slug: salesforce-case-comment
- name: CaseContactRole
  property_count: 6
  slug: salesforce-case-contact-role
- name: CaseHistory
  property_count: 6
  slug: salesforce-case-history
- name: Case
  property_count: 6
  slug: salesforce-case
- name: ChangeeventrelaystateRequest
  property_count: 1
  slug: salesforce-changeeventrelaystate-request
- name: ChannelProgramHistory
  property_count: 6
  slug: salesforce-channel-program-history
- name: ChannelProgramLevelHistory
  property_count: 6
  slug: salesforce-channel-program-level-history
- name: ChannelProgramLevelName
  property_count: 2
  slug: salesforce-channel-program-level-name
- name: ChannelProgramLevelName1
  property_count: 31
  slug: salesforce-channel-program-level-name1
- name: ChannelProgramLevel
  property_count: 6
  slug: salesforce-channel-program-level
- name: ChannelProgramMemberHistory
  property_count: 6
  slug: salesforce-channel-program-member-history
- name: ChannelProgramMember
  property_count: 6
  slug: salesforce-channel-program-member
- name: ChannelProgramName
  property_count: 2
  slug: salesforce-channel-program-name
- name: ChannelProgramName1
  property_count: 31
  slug: salesforce-channel-program-name1
- name: ChannelProgram
  property_count: 6
  slug: salesforce-channel-program
- name: ChatterLikes
  property_count: 4
  slug: salesforce-chatter-likes
- name: ChildAccounts
  property_count: 1
  slug: salesforce-child-accounts
- name: ChildRelationship
  property_count: 8
  slug: salesforce-child-relationship
- name: ChildRelationship2
  property_count: 5
  slug: salesforce-child-relationship2
- name: City
  property_count: 31
  slug: salesforce-city
- name: City2
  property_count: 2
  slug: salesforce-city2
- name: City3
  property_count: 2
  slug: salesforce-city3
- name: CleanStatus
  property_count: 2
  slug: salesforce-clean-status
- name: CleanStatus2
  property_count: 31
  slug: salesforce-clean-status2
- name: CleanStatus4
  property_count: 5
  slug: salesforce-clean-status4
- name: ClientInfo
  property_count: 2
  slug: salesforce-client-info
- name: CloneSourceId
  property_count: 31
  slug: salesforce-clone-source-id
- name: CloneSourceId3
  property_count: 2
  slug: salesforce-clone-source-id3
- name: CloseDate
  property_count: 2
  slug: salesforce-close-date
- name: Close
  property_count: 2
  slug: salesforce-close
- name: CloseorAbortaJobRequest
  property_count: 1
  slug: salesforce-closeor-aborta-job-request
- name: CodeCoverage
  property_count: 7
  slug: salesforce-code-coverage
- name: CodeCoverageWarning
  property_count: 4
  slug: salesforce-code-coverage-warning
- name: Color
  property_count: 3
  slug: salesforce-color
- name: ColumnWidths
  property_count: 6
  slug: salesforce-column-widths
- name: ColumnWrap
  property_count: 6
  slug: salesforce-column-wrap
- name: CommSubscriptionChannelTypeHistory
  property_count: 6
  slug: salesforce-comm-subscription-channel-type-history
- name: CommSubscriptionChannelType
  property_count: 6
  slug: salesforce-comm-subscription-channel-type
- name: CommSubscriptionHistory
  property_count: 6
  slug: salesforce-comm-subscription-history
- name: CommSubscription
  property_count: 6
  slug: salesforce-comm-subscription
- name: Comment-EditRequest
  property_count: 1
  slug: salesforce-comment-edit-request
- name: Comments
  property_count: 1
  slug: salesforce-comments
- name: Commitment
  property_count: 15
  slug: salesforce-commitment
- name: Commitment1
  property_count: 12
  slug: salesforce-commitment1
- name: CommunityNickname
  property_count: 31
  slug: salesforce-community-nickname
- name: CompanyDunsNumber
  property_count: 31
  slug: salesforce-company-duns-number
- name: CompanyName
  property_count: 31
  slug: salesforce-company-name
- name: Company
  property_count: 31
  slug: salesforce-company
- name: Company1
  property_count: 2
  slug: salesforce-company1
- name: Components
  property_count: 2
  slug: salesforce-components
- name: CompositeBatchRequest
  property_count: 2
  slug: salesforce-composite-batch-request
- name: CompositeGraphRequest
  property_count: 1
  slug: salesforce-composite-graph-request
- name: CompositeRequest
  property_count: 1
  slug: salesforce-composite-request
- name: CompositeRequest1
  property_count: 4
  slug: salesforce-composite-request1
- name: CompositeRequest2
  property_count: 4
  slug: salesforce-composite-request2
- name: CompositeRequest3
  property_count: 4
  slug: salesforce-composite-request3
- name: CompositeRequest4
  property_count: 4
  slug: salesforce-composite-request4
- name: CompositeRequest5
  property_count: 4
  slug: salesforce-composite-request5
- name: CompositeRequest6
  property_count: 4
  slug: salesforce-composite-request6
- name: CompositeResponse
  property_count: 4
  slug: salesforce-composite-response
- name: ConcurrentAsyncGetReportInstances
  property_count: 2
  slug: salesforce-concurrent-async-get-report-instances
- name: ConcurrentEinsteinDataInsightsStoryCreation
  property_count: 2
  slug: salesforce-concurrent-einstein-data-insights-story-creation
- name: ConcurrentEinsteinDiscoveryStoryCreation
  property_count: 2
  slug: salesforce-concurrent-einstein-discovery-story-creation
- name: ConcurrentSyncReportRuns
  property_count: 2
  slug: salesforce-concurrent-sync-report-runs
- name: Condition
  property_count: 1
  slug: salesforce-condition
- name: ConditionsList
  property_count: 3
  slug: salesforce-conditions-list
- name: ConditionsList1
  property_count: 2
  slug: salesforce-conditions-list1
- name: Conditions
  property_count: 1
  slug: salesforce-conditions
- name: Constructor
  property_count: 7
  slug: salesforce-constructor
- name: ConsumptionRateHistory
  property_count: 6
  slug: salesforce-consumption-rate-history
- name: ConsumptionRate
  property_count: 6
  slug: salesforce-consumption-rate
- name: ConsumptionScheduleHistory
  property_count: 6
  slug: salesforce-consumption-schedule-history
- name: ConsumptionSchedule
  property_count: 6
  slug: salesforce-consumption-schedule
- name: ContactHistory
  property_count: 6
  slug: salesforce-contact-history
- name: ContactId
  property_count: 31
  slug: salesforce-contact-id
- name: ContactPointTypeConsentHistory
  property_count: 6
  slug: salesforce-contact-point-type-consent-history
- name: ContactPointTypeConsent
  property_count: 6
  slug: salesforce-contact-point-type-consent
- name: ContactRequest
  property_count: 6
  slug: salesforce-contact-request
- name: ContactSObject
  property_count: 3
  slug: salesforce-contact-s-object
- name: Contact
  property_count: 1
  slug: salesforce-contact
- name: Contact2
  property_count: 1
  slug: salesforce-contact2
- name: Contact3
  property_count: 6
  slug: salesforce-contact3
- name: ContactsOrdered
  property_count: 2
  slug: salesforce-contacts-ordered
- name: Contacts
  property_count: 1
  slug: salesforce-contacts
- name: Contacts1
  property_count: 2
  slug: salesforce-contacts1
- name: ContactswithAccountName
  property_count: 2
  slug: salesforce-contactswith-account-name
- name: ContentDocumentHistory
  property_count: 6
  slug: salesforce-content-document-history
- name: ContentDocumentLink
  property_count: 6
  slug: salesforce-content-document-link
- name: ContentDocument
  property_count: 6
  slug: salesforce-content-document
- name: Content
  property_count: 1
  slug: salesforce-content
- name: ContentVersionHistory
  property_count: 6
  slug: salesforce-content-version-history
- name: ContentVersion
  property_count: 6
  slug: salesforce-content-version
- name: ContentWorkspace
  property_count: 6
  slug: salesforce-content-workspace
- name: Content1
  property_count: 1
  slug: salesforce-content1
- name: Context
  property_count: 2
  slug: salesforce-context
- name: Context1
  property_count: 2
  slug: salesforce-context1
- name: Context2
  property_count: 2
  slug: salesforce-context2
- name: ContractContactRole
  property_count: 6
  slug: salesforce-contract-contact-role
- name: ContractHistory
  property_count: 6
  slug: salesforce-contract-history
- name: ContractRenewerAPIRequest
  property_count: 1
  slug: salesforce-contract-renewer-api-request
- name: Contract
  property_count: 6
  slug: salesforce-contract
- name: ConversationEntry
  property_count: 7
  slug: salesforce-conversation-entry
- name: ConvertedAccountId
  property_count: 31
  slug: salesforce-converted-account-id
- name: ConvertedContactId
  property_count: 31
  slug: salesforce-converted-contact-id
- name: ConvertedDate
  property_count: 31
  slug: salesforce-converted-date
- name: ConvertedOpportunityId
  property_count: 31
  slug: salesforce-converted-opportunity-id
- name: CorporateMemberEnrollmentsRequest
  property_count: 5
  slug: salesforce-corporate-member-enrollments-request
- name: CorporateMemberEnrollments
  property_count: 5
  slug: salesforce-corporate-member-enrollments
- name: Country
  property_count: 31
  slug: salesforce-country
- name: Country2
  property_count: 2
  slug: salesforce-country2
- name: CreateAccountSuccess
  property_count: 2
  slug: salesforce-create-account-success
- name: CreateAssetFromOrderRequest
  property_count: 1
  slug: salesforce-create-asset-from-order-request
- name: CreateCloneSandboxRequest
  property_count: 9
  slug: salesforce-create-clone-sandbox-request
- name: CreateCommitmentsRequest
  property_count: 2
  slug: salesforce-create-commitments-request
- name: CreateCredentialRequest
  property_count: 5
  slug: salesforce-create-credential-request
- name: CreateCustom
  property_count: 2
  slug: salesforce-create-custom
- name: CreateExternalCredentialRequest
  property_count: 5
  slug: salesforce-create-external-credential-request
- name: CreateGiftsRequest
  property_count: 2
  slug: salesforce-create-gifts-request
- name: CreateNamedCredentialRequest
  property_count: 7
  slug: salesforce-create-named-credential-request
- name: CreateOrderEvergreenTermedRequest
  property_count: 2
  slug: salesforce-create-order-evergreen-termed-request
- name: CreateOrderFromQuoteRequest
  property_count: 1
  slug: salesforce-create-order-from-quote-request
- name: CreateOrderOne-TimeRequest
  property_count: 2
  slug: salesforce-create-order-one-time-request
- name: CreateOrderWithBundleRequest
  property_count: 2
  slug: salesforce-create-order-with-bundle-request
- name: CreatePaymentMethodRequest
  property_count: 5
  slug: salesforce-create-payment-method-request
- name: CreatePledgeCommitmentsRequest
  property_count: 2
  slug: salesforce-create-pledge-commitments-request
- name: CreateSandbox
  property_count: 5
  slug: salesforce-create-sandbox
- name: create
  property_count: 1
  slug: salesforce-create
- name: CreateTableRequest
  property_count: 8
  slug: salesforce-create-table-request
- name: CreateaFavoriteRequest
  property_count: 4
  slug: salesforce-createa-favorite-request
- name: CreateaFavoritelistview
  property_count: 11
  slug: salesforce-createa-favoritelistview
- name: CreateaRecordRequest
  property_count: 3
  slug: salesforce-createa-record-request
- name: CreateaRecord
  property_count: 11
  slug: salesforce-createa-record
- name: Createable
  property_count: 1
  slug: salesforce-createable
- name: CreateandSaveQuoteProposalAPIRequest
  property_count: 2
  slug: salesforce-createand-save-quote-proposal-api-request
- name: CreatechannelRequest
  property_count: 2
  slug: salesforce-createchannel-request
- name: CreatechannelRequest1
  property_count: 2
  slug: salesforce-createchannel-request1
- name: CreatechannelmemberRequest
  property_count: 2
  slug: salesforce-createchannelmember-request
- name: CreatechannelmemberRequest1
  property_count: 2
  slug: salesforce-createchannelmember-request1
- name: CreatedById
  property_count: 1
  slug: salesforce-created-by-id
- name: CreatedById2
  property_count: 31
  slug: salesforce-created-by-id2
- name: CreatedById5
  property_count: 2
  slug: salesforce-created-by-id5
- name: CreatedBy
  property_count: 3
  slug: salesforce-created-by
- name: CreatedBy3
  property_count: 2
  slug: salesforce-created-by3
- name: CreatedDate
  property_count: 2
  slug: salesforce-created-date
- name: CreatedDate14
  property_count: 2
  slug: salesforce-created-date14
- name: CreatedDate2
  property_count: 31
  slug: salesforce-created-date2
- name: CreatedDate5
  property_count: 2
  slug: salesforce-created-date5
- name: CreateeventrelayRequest
  property_count: 2
  slug: salesforce-createeventrelay-request
- name: CreatejobRequest
  property_count: 2
  slug: salesforce-createjob-request
- name: CreatemanagedeventsubscriptionRequest
  property_count: 2
  slug: salesforce-createmanagedeventsubscription-request
- name: CreatenamedcredentialRequest1
  property_count: 2
  slug: salesforce-createnamedcredential-request1
- name: CreateorUpdateQuoteRequest
  property_count: 2
  slug: salesforce-createor-update-quote-request
- name: CredentialStuffingEventStore
  property_count: 6
  slug: salesforce-credential-stuffing-event-store
- name: Credentials
  property_count: 1
  slug: salesforce-credentials
- name: CreditPointstoMembersRequest
  property_count: 1
  slug: salesforce-credit-pointsto-members-request
- name: CreditPointstoMembers
  property_count: 4
  slug: salesforce-credit-pointsto-members
- name: CspTrustedSite
  property_count: 6
  slug: salesforce-csp-trusted-site
- name: CurrentGeneratorsC
  property_count: 31
  slug: salesforce-current-generators-c
- name: CurrentGeneratorsC1
  property_count: 2
  slug: salesforce-current-generators-c1
- name: CustomHeader
  property_count: 3
  slug: salesforce-custom-header
- name: CustomHeader1
  property_count: 4
  slug: salesforce-custom-header1
- name: Custom
  property_count: 1
  slug: salesforce-custom
- name: CustomSetting
  property_count: 1
  slug: salesforce-custom-setting
- name: Customdata
  property_count: 6
  slug: salesforce-customdata
- name: CustomerPriorityC
  property_count: 1
  slug: salesforce-customer-priority-c
- name: CustomerPriorityC1
  property_count: 31
  slug: salesforce-customer-priority-c1
- name: CustomerPriorityC2
  property_count: 2
  slug: salesforce-customer-priority-c2
- name: CustomerPriorityC4
  property_count: 2
  slug: salesforce-customer-priority-c4
- name: Customer
  property_count: 6
  slug: salesforce-customer
- name: DailyAnalyticsDataflowJobExecutions
  property_count: 2
  slug: salesforce-daily-analytics-dataflow-job-executions
- name: DailyAnalyticsUploadedFilesSizeMB
  property_count: 2
  slug: salesforce-daily-analytics-uploaded-files-size-mb
- name: DailyApiRequests
  property_count: 2
  slug: salesforce-daily-api-requests
- name: DailyAsyncApexExecutions
  property_count: 2
  slug: salesforce-daily-async-apex-executions
- name: DailyAsyncApexTests
  property_count: 2
  slug: salesforce-daily-async-apex-tests
- name: DailyBulkApiBatches
  property_count: 2
  slug: salesforce-daily-bulk-api-batches
- name: DailyBulkV2QueryFileStorageMB
  property_count: 2
  slug: salesforce-daily-bulk-v2-query-file-storage-mb
- name: DailyBulkV2QueryJobs
  property_count: 2
  slug: salesforce-daily-bulk-v2-query-jobs
- name: DailyDeliveredPlatformEvents
  property_count: 2
  slug: salesforce-daily-delivered-platform-events
- name: DailyDurableGenericStreamingApiEvents
  property_count: 2
  slug: salesforce-daily-durable-generic-streaming-api-events
- name: DailyDurableStreamingApiEvents
  property_count: 2
  slug: salesforce-daily-durable-streaming-api-events
- name: DailyEinsteinDataInsightsStoryCreation
  property_count: 2
  slug: salesforce-daily-einstein-data-insights-story-creation
- name: DailyEinsteinDiscoveryOptimizationJobRuns
  property_count: 2
  slug: salesforce-daily-einstein-discovery-optimization-job-runs
- name: DailyEinsteinDiscoveryPredictAPICalls
  property_count: 2
  slug: salesforce-daily-einstein-discovery-predict-api-calls
- name: DailyEinsteinDiscoveryPredictionsByCDC
  property_count: 2
  slug: salesforce-daily-einstein-discovery-predictions-by-cdc
- name: DailyEinsteinDiscoveryStoryCreation
  property_count: 2
  slug: salesforce-daily-einstein-discovery-story-creation
- name: DailyFunctionsApiCallLimit
  property_count: 2
  slug: salesforce-daily-functions-api-call-limit
- name: DailyGenericStreamingApiEvents
  property_count: 2
  slug: salesforce-daily-generic-streaming-api-events
- name: DailyScratchOrgs
  property_count: 2
  slug: salesforce-daily-scratch-orgs
- name: DailyStandardVolumePlatformEvents
  property_count: 2
  slug: salesforce-daily-standard-volume-platform-events
- name: DailyStreamingApiEvents
  property_count: 2
  slug: salesforce-daily-streaming-api-events
- name: DailyWorkflowEmails
  property_count: 2
  slug: salesforce-daily-workflow-emails
- name: DandBCompany
  property_count: 6
  slug: salesforce-dand-b-company
- name: DandbCompanyId
  property_count: 1
  slug: salesforce-dandb-company-id
- name: DandbCompanyId1
  property_count: 31
  slug: salesforce-dandb-company-id1
- name: Data
  property_count: 1
  slug: salesforce-data
- name: DataStorageMB
  property_count: 2
  slug: salesforce-data-storage-mb
- name: DataTranslationEnabled
  property_count: 1
  slug: salesforce-data-translation-enabled
- name: DataUseLegalBasisHistory
  property_count: 6
  slug: salesforce-data-use-legal-basis-history
- name: DataUseLegalBasis
  property_count: 6
  slug: salesforce-data-use-legal-basis
- name: DataUsePurposeHistory
  property_count: 6
  slug: salesforce-data-use-purpose-history
- name: DataUsePurpose
  property_count: 6
  slug: salesforce-data-use-purpose
- name: Data10
  property_count: 1
  slug: salesforce-data10
- name: Data11
  property_count: 1
  slug: salesforce-data11
- name: Data12
  property_count: 1
  slug: salesforce-data12
- name: Data13
  property_count: 1
  slug: salesforce-data13
- name: Data3
  property_count: 1
  slug: salesforce-data3
- name: Data4
  property_count: 1
  slug: salesforce-data4
- name: Data6
  property_count: 1
  slug: salesforce-data6
- name: Data7
  property_count: 1
  slug: salesforce-data7
- name: DataweaveKeyMappingMdt
  property_count: 6
  slug: salesforce-dataweave-key-mapping-mdt
- name: DataweaveMappingMdt
  property_count: 6
  slug: salesforce-dataweave-mapping-mdt
- name: DebitPointsfromMembersRequest
  property_count: 1
  slug: salesforce-debit-pointsfrom-members-request
- name: DebitPointsfromMembers
  property_count: 4
  slug: salesforce-debit-pointsfrom-members
- name: DecisionModelNotationExportRequest
  property_count: 1
  slug: salesforce-decision-model-notation-export-request
- name: DecisionTable
  property_count: 3
  slug: salesforce-decision-table
- name: DecisionTable1
  property_count: 9
  slug: salesforce-decision-table1
- name: DeepCloneable
  property_count: 1
  slug: salesforce-deep-cloneable
- name: DefaultGroupBanner
  property_count: 1
  slug: salesforce-default-group-banner
- name: DefaultGroupImage
  property_count: 3
  slug: salesforce-default-group-image
- name: DefaultGroupNotificationFrequency
  property_count: 31
  slug: salesforce-default-group-notification-frequency
- name: DefaultPageBanner
  property_count: 1
  slug: salesforce-default-page-banner
- name: DefaultUserBanner
  property_count: 1
  slug: salesforce-default-user-banner
- name: DefaultUserImage
  property_count: 3
  slug: salesforce-default-user-image
- name: DelegatedAccountHistory
  property_count: 6
  slug: salesforce-delegated-account-history
- name: DelegatedAccount
  property_count: 6
  slug: salesforce-delegated-account
- name: DelegatedApproverId
  property_count: 31
  slug: salesforce-delegated-approver-id
- name: Deletable
  property_count: 1
  slug: salesforce-deletable
- name: DeleteAccount
  property_count: 2
  slug: salesforce-delete-account
- name: DeleteCredentialRequest
  property_count: 3
  slug: salesforce-delete-credential-request
- name: DeleteEvent
  property_count: 6
  slug: salesforce-delete-event
- name: Department
  property_count: 2
  slug: salesforce-department
- name: Department1
  property_count: 31
  slug: salesforce-department1
- name: DeprecatedAndHidden
  property_count: 1
  slug: salesforce-deprecated-and-hidden
- name: describeMetadataResponse
  property_count: 1
  slug: salesforce-describe-metadata-response
- name: describeMetadata
  property_count: 1
  slug: salesforce-describe-metadata
- name: describeValueTypeResponse
  property_count: 1
  slug: salesforce-describe-value-type-response
- name: describeValueType
  property_count: 1
  slug: salesforce-describe-value-type
- name: Describeeventchannel
  property_count: 45
  slug: salesforce-describeeventchannel
- name: Description
  property_count: 1
  slug: salesforce-description
- name: Description3
  property_count: 2
  slug: salesforce-description3
- name: Description5
  property_count: 31
  slug: salesforce-description5
- name: Description6
  property_count: 2
  slug: salesforce-description6
- name: Designation
  property_count: 3
  slug: salesforce-designation
- name: Designation1
  property_count: 2
  slug: salesforce-designation1
- name: Detail
  property_count: 2
  slug: salesforce-detail
- name: Detail1
  property_count: 3
  slug: salesforce-detail1
- name: Detail10
  property_count: 2
  slug: salesforce-detail10
- name: Detail13
  property_count: 2
  slug: salesforce-detail13
- name: Detail14
  property_count: 3
  slug: salesforce-detail14
- name: Detail3
  property_count: 2
  slug: salesforce-detail3
- name: Detail4
  property_count: 3
  slug: salesforce-detail4
- name: Detail7
  property_count: 2
  slug: salesforce-detail7
- name: Detail8
  property_count: 2
  slug: salesforce-detail8
- name: DeveloperName
  property_count: 31
  slug: salesforce-developer-name
- name: DigestFrequency
  property_count: 31
  slug: salesforce-digest-frequency
- name: DisambiguationField
  property_count: 2
  slug: salesforce-disambiguation-field
- name: DisplayColumn
  property_count: 6
  slug: salesforce-display-column
- name: Division
  property_count: 31
  slug: salesforce-division
- name: DoesIncludeBosses
  property_count: 31
  slug: salesforce-does-include-bosses
- name: DoesSendEmailToMembers
  property_count: 31
  slug: salesforce-does-send-email-to-members
- name: DonorOptions
  property_count: 1
  slug: salesforce-donor-options
- name: Donor
  property_count: 9
  slug: salesforce-donor
- name: Donor1
  property_count: 8
  slug: salesforce-donor1
- name: Donor3
  property_count: 8
  slug: salesforce-donor3
- name: DunsNumber
  property_count: 2
  slug: salesforce-duns-number
- name: DunsNumber1
  property_count: 31
  slug: salesforce-duns-number1
- name: DuplicateRecordItem
  property_count: 6
  slug: salesforce-duplicate-record-item
- name: DuplicateRecordSet
  property_count: 6
  slug: salesforce-duplicate-record-set
- name: DurableStreamingApiConcurrentClients
  property_count: 2
  slug: salesforce-durable-streaming-api-concurrent-clients
- name: Edge
  property_count: 1
  slug: salesforce-edge
- name: Edge10
  property_count: 1
  slug: salesforce-edge10
- name: Edge6
  property_count: 1
  slug: salesforce-edge6
- name: Edge7
  property_count: 1
  slug: salesforce-edge7
- name: Edit
  property_count: 6
  slug: salesforce-edit
- name: Edit6
  property_count: 6
  slug: salesforce-edit6
- name: EligibleChannel
  property_count: 3
  slug: salesforce-eligible-channel
- name: EligibleCustomerEvents
  property_count: 2
  slug: salesforce-eligible-customer-events
- name: EligibleEnrollmentPeriod
  property_count: 3
  slug: salesforce-eligible-enrollment-period
- name: EligibleLoyaltyTier
  property_count: 2
  slug: salesforce-eligible-loyalty-tier
- name: EligibleProductCategory
  property_count: 1
  slug: salesforce-eligible-product-category
- name: EligibleProduct
  property_count: 1
  slug: salesforce-eligible-product
- name: EligiblePromotionsRequest
  property_count: 1
  slug: salesforce-eligible-promotions-request
- name: EmailBouncedDate
  property_count: 3
  slug: salesforce-email-bounced-date
- name: EmailBouncedDate1
  property_count: 31
  slug: salesforce-email-bounced-date1
- name: EmailBouncedReason
  property_count: 2
  slug: salesforce-email-bounced-reason
- name: EmailBouncedReason1
  property_count: 31
  slug: salesforce-email-bounced-reason1
- name: EmailEncodingKey
  property_count: 31
  slug: salesforce-email-encoding-key
- name: EmailMessageRelation
  property_count: 6
  slug: salesforce-email-message-relation
- name: EmailPreferencesAutoBcc
  property_count: 31
  slug: salesforce-email-preferences-auto-bcc
- name: EmailPreferencesAutoBccStayInTouch
  property_count: 31
  slug: salesforce-email-preferences-auto-bcc-stay-in-touch
- name: EmailPreferencesStayInTouchReminder
  property_count: 31
  slug: salesforce-email-preferences-stay-in-touch-reminder
- name: Email
  property_count: 2
  slug: salesforce-email
- name: Email1
  property_count: 31
  slug: salesforce-email1
- name: Email5
  property_count: 2
  slug: salesforce-email5
- name: EmployeeNumber
  property_count: 31
  slug: salesforce-employee-number
- name: EngagementChannelTypeHistory
  property_count: 6
  slug: salesforce-engagement-channel-type-history
- name: EngagementChannelType
  property_count: 6
  slug: salesforce-engagement-channel-type
- name: EnrichedField
  property_count: 1
  slug: salesforce-enriched-field
- name: EnrollforPromotionsRequest
  property_count: 1
  slug: salesforce-enrollfor-promotions-request
- name: EntityLabel
  property_count: 2
  slug: salesforce-entity-label
- name: Entity
  property_count: 19
  slug: salesforce-entity
- name: Envelope
  property_count: 2
  slug: salesforce-envelope
- name: Envelope1
  property_count: 2
  slug: salesforce-envelope1
- name: Envelope2
  property_count: 1
  slug: salesforce-envelope2
- name: Envelope3
  property_count: 2
  slug: salesforce-envelope3
- name: Envelope4
  property_count: 1
  slug: salesforce-envelope4
- name: Envelope5
  property_count: 2
  slug: salesforce-envelope5
- name: Envelope6
  property_count: 1
  slug: salesforce-envelope6
- name: Envelope7
  property_count: 2
  slug: salesforce-envelope7
- name: ErrorCode
  property_count: 1
  slug: salesforce-error-code
- name: ErrorInfo
  property_count: 2
  slug: salesforce-error-info
- name: Error
  property_count: 3
  slug: salesforce-error
- name: Errors
  property_count: 2
  slug: salesforce-errors
- name: Errors12
  property_count: 2
  slug: salesforce-errors12
- name: Errors5
  property_count: 1
  slug: salesforce-errors5
- name: Errors7
  property_count: 3
  slug: salesforce-errors7
- name: ExpressionSetCreationRequest
  property_count: 5
  slug: salesforce-expression-set-creation-request
- name: ExpressionSetInvocationRequest
  property_count: 2
  slug: salesforce-expression-set-invocation-request
- name: ExpressionSetUpdateRequest
  property_count: 5
  slug: salesforce-expression-set-update-request
- name: ExtendedDetails
  property_count: 2
  slug: salesforce-extended-details
- name: ExtendedErrorCode
  property_count: 1
  slug: salesforce-extended-error-code
- name: ExtendedErrorDetails
  property_count: 2
  slug: salesforce-extended-error-details
- name: ExtendedErrorDetails1
  property_count: 2
  slug: salesforce-extended-error-details1
- name: Extension
  property_count: 31
  slug: salesforce-extension
- name: ExternalCredential
  property_count: 11
  slug: salesforce-external-credential
- name: ExternalCredential1
  property_count: 4
  slug: salesforce-external-credential1
- name: ExternalCredential2
  property_count: 1
  slug: salesforce-external-credential2
- name: Favorite
  property_count: 11
  slug: salesforce-favorite
- name: Favorite1
  property_count: 2
  slug: salesforce-favorite1
- name: Fax
  property_count: 2
  slug: salesforce-fax
- name: Fax2
  property_count: 31
  slug: salesforce-fax2
- name: Fax4
  property_count: 2
  slug: salesforce-fax4
- name: Fax5
  property_count: 2
  slug: salesforce-fax5
- name: FederationIdentifier
  property_count: 31
  slug: salesforce-federation-identifier
- name: FeedElement
  property_count: 2
  slug: salesforce-feed-element
- name: FeedElementsBatchPostRequest
  property_count: 1
  slug: salesforce-feed-elements-batch-post-request
- name: FeedElementsCapabilityCommentsItems
  property_count: 18
  slug: salesforce-feed-elements-capability-comments-items
- name: FeedElementsPostandSearchRequest
  property_count: 4
  slug: salesforce-feed-elements-postand-search-request
- name: FeedEnabled
  property_count: 1
  slug: salesforce-feed-enabled
- name: FieldMappingList
  property_count: 1
  slug: salesforce-field-mapping-list
- name: Field
  property_count: 3
  slug: salesforce-field
- name: Field1
  property_count: 57
  slug: salesforce-field1
- name: Field2
  property_count: 2
  slug: salesforce-field2
- name: Field3
  property_count: 2
  slug: salesforce-field3
- name: Field4
  property_count: 4
  slug: salesforce-field4
- name: Field5
  property_count: 4
  slug: salesforce-field5
- name: Field9
  property_count: 57
  slug: salesforce-field9
- name: Fields
  property_count: 2
  slug: salesforce-fields
- name: Fields11
  property_count: 35
  slug: salesforce-fields11
- name: Fields15
  property_count: 70
  slug: salesforce-fields15
- name: Fields16
  property_count: 3
  slug: salesforce-fields16
- name: Fields17
  property_count: 2
  slug: salesforce-fields17
- name: Fields18
  property_count: 17
  slug: salesforce-fields18
- name: Fields2
  property_count: 57
  slug: salesforce-fields2
- name: Fields20
  property_count: 1
  slug: salesforce-fields20
- name: Fields21
  property_count: 42
  slug: salesforce-fields21
- name: Fields27
  property_count: 37
  slug: salesforce-fields27
- name: Fields3
  property_count: 14
  slug: salesforce-fields3
- name: Fields31
  property_count: 36
  slug: salesforce-fields31
- name: Fields38
  property_count: 3
  slug: salesforce-fields38
- name: Fields39
  property_count: 4
  slug: salesforce-fields39
- name: Fields4
  property_count: 60
  slug: salesforce-fields4
- name: Fields40
  property_count: 12
  slug: salesforce-fields40
- name: Fields41
  property_count: 7
  slug: salesforce-fields41
- name: Fields5
  property_count: 18
  slug: salesforce-fields5
- name: Fields6
  property_count: 196
  slug: salesforce-fields6
- name: Fields7
  property_count: 35
  slug: salesforce-fields7
- name: Fields8
  property_count: 2
  slug: salesforce-fields8
- name: FileInformation
  property_count: 48
  slug: salesforce-file-information
- name: FileStorageMB
  property_count: 2
  slug: salesforce-file-storage-mb
- name: Files
  property_count: 1
  slug: salesforce-files
- name: FirstName
  property_count: 2
  slug: salesforce-first-name
- name: FirstName1
  property_count: 31
  slug: salesforce-first-name1
- name: FirstName4
  property_count: 2
  slug: salesforce-first-name4
- name: FirstTransaction
  property_count: 11
  slug: salesforce-first-transaction
- name: FlowInterview
  property_count: 6
  slug: salesforce-flow-interview
- name: FlowOrchestrationInstance
  property_count: 6
  slug: salesforce-flow-orchestration-instance
- name: FlowOrchestrationStageInstance
  property_count: 6
  slug: salesforce-flow-orchestration-stage-instance
- name: FlowOrchestrationStepInstance
  property_count: 6
  slug: salesforce-flow-orchestration-step-instance
- name: FlowOrchestrationWorkItem
  property_count: 6
  slug: salesforce-flow-orchestration-work-item
- name: Flows
  property_count: 3
  slug: salesforce-flows
- name: ForecastEnabled
  property_count: 31
  slug: salesforce-forecast-enabled
- name: ForgotPassword-ChangePasswordRequest
  property_count: 3
  slug: salesforce-forgot-password-change-password-request
- name: ForgotPassword-InitializeRequest
  property_count: 2
  slug: salesforce-forgot-password-initialize-request
- name: FullPhotoUrl
  property_count: 31
  slug: salesforce-full-photo-url
- name: Full
  property_count: 1
  slug: salesforce-full
- name: GenerateOpenAPISchema
  property_count: 1
  slug: salesforce-generate-open-api-schema
- name: GenerateQuoteDocumentAPIRequest
  property_count: 2
  slug: salesforce-generate-quote-document-api-request
- name: GenerateResponseBasedonPromptTemplate
  property_count: 5
  slug: salesforce-generate-response-basedon-prompt-template
- name: GeneratedData
  property_count: 6
  slug: salesforce-generated-data
- name: Generation
  property_count: 3
  slug: salesforce-generation
- name: GeocodeAccuracy
  property_count: 31
  slug: salesforce-geocode-accuracy
- name: GetActiveTheme
  property_count: 11
  slug: salesforce-get-active-theme
- name: GetAllNavigationItems
  property_count: 4
  slug: salesforce-get-all-navigation-items
- name: GetAppointmentCandidatesRequest
  property_count: 9
  slug: salesforce-get-appointment-candidates-request
- name: GetAppointmentSlotsRequest
  property_count: 9
  slug: salesforce-get-appointment-slots-request
- name: GetApps
  property_count: 2
  slug: salesforce-get-apps
- name: GetChildRecords
  property_count: 8
  slug: salesforce-get-child-records
- name: GetDefaultValuestoCloneaRecord
  property_count: 3
  slug: salesforce-get-default-valuesto-clonea-record
- name: GetDefaultValuestoCreateaRecord
  property_count: 3
  slug: salesforce-get-default-valuesto-createa-record
- name: GetFavorites
  property_count: 1
  slug: salesforce-get-favorites
- name: GetGlobalActions
  property_count: 3
  slug: salesforce-get-global-actions
- name: GetLastSelectedApp
  property_count: 18
  slug: salesforce-get-last-selected-app
- name: GetLightningPageActions
  property_count: 3
  slug: salesforce-get-lightning-page-actions
- name: GetListViewChartActions
  property_count: 3
  slug: salesforce-get-list-view-chart-actions
- name: GetListViewHeaderActions
  property_count: 3
  slug: salesforce-get-list-view-header-actions
- name: GetListViewMetadatabyAPIName
  property_count: 18
  slug: salesforce-get-list-view-metadataby-api-name
- name: GetListViewMetadatabyID
  property_count: 19
  slug: salesforce-get-list-view-metadataby-id
- name: GetListViewRecordActions
  property_count: 3
  slug: salesforce-get-list-view-record-actions
- name: GetListViewRecordsRequest
  property_count: 5
  slug: salesforce-get-list-view-records-request
- name: GetListViewRecords
  property_count: 16
  slug: salesforce-get-list-view-records
- name: GetListViewRecordsbyID
  property_count: 16
  slug: salesforce-get-list-view-recordsby-id
- name: GetListViewRecordsperAPIName
  property_count: 16
  slug: salesforce-get-list-view-recordsper-api-name
- name: GetListViewsforanObject
  property_count: 12
  slug: salesforce-get-list-viewsforan-object
- name: GetLookupFieldActions
  property_count: 3
  slug: salesforce-get-lookup-field-actions
- name: GetLookupFieldSuggestions
  property_count: 2
  slug: salesforce-get-lookup-field-suggestions
- name: GetLookupFieldSuggestionsforaSpecifiedObject
  property_count: 8
  slug: salesforce-get-lookup-field-suggestionsfora-specified-object
- name: GetMemberPromotionsRequest
  property_count: 1
  slug: salesforce-get-member-promotions-request
- name: GetMRUListViewActions
  property_count: 3
  slug: salesforce-get-mru-list-view-actions
- name: GetObjectMetadata
  property_count: 23
  slug: salesforce-get-object-metadata
- name: GetParallelResultsforaQueryJob
  property_count: 3
  slug: salesforce-get-parallel-resultsfora-query-job
- name: GetPhotoActions
  property_count: 3
  slug: salesforce-get-photo-actions
- name: GetRecordDataandObjectMetadata
  property_count: 5
  slug: salesforce-get-record-dataand-object-metadata
- name: GetRecordDetailPageActions
  property_count: 3
  slug: salesforce-get-record-detail-page-actions
- name: GetRecordEditPageActions
  property_count: 3
  slug: salesforce-get-record-edit-page-actions
- name: GetRecordLayoutMetadata
  property_count: 8
  slug: salesforce-get-record-layout-metadata
- name: GetRelatedListActions
  property_count: 3
  slug: salesforce-get-related-list-actions
- name: GetRelatedListRecordActions
  property_count: 3
  slug: salesforce-get-related-list-record-actions
- name: GetSandbox
  property_count: 17
  slug: salesforce-get-sandbox
- name: GetSandboxStatus
  property_count: 6
  slug: salesforce-get-sandbox-status
- name: Get
  property_count: 1
  slug: salesforce-get
- name: GetToolingDescribeSObject
  property_count: 45
  slug: salesforce-get-tooling-describe-s-object
- name: GetToolingDescribe
  property_count: 3
  slug: salesforce-get-tooling-describe
- name: GetToolingMetadataSObject
  property_count: 2
  slug: salesforce-get-tooling-metadata-s-object
- name: GetValuesforAllPicklistFieldsofaRecordType
  property_count: 2
  slug: salesforce-get-valuesfor-all-picklist-fieldsofa-record-type
- name: GetValuesforaPicklistField
  property_count: 5
  slug: salesforce-get-valuesfora-picklist-field
- name: GetaBatchofRecords
  property_count: 2
  slug: salesforce-geta-batchof-records
- name: GetaDirectoryofSupportedObjects
  property_count: 1
  slug: salesforce-geta-directoryof-supported-objects
- name: GetaFavorite
  property_count: 11
  slug: salesforce-geta-favorite
- name: GetaRecord
  property_count: 11
  slug: salesforce-geta-record
- name: Getallmanagedeventsubscriptions
  property_count: 6
  slug: salesforce-getallmanagedeventsubscriptions
- name: GetanApp
  property_count: 18
  slug: salesforce-getan-app
- name: Getchannelmember
  property_count: 18
  slug: salesforce-getchannelmember
- name: Getconversationentries
  property_count: 1
  slug: salesforce-getconversationentries
- name: Geteventchannel
  property_count: 16
  slug: salesforce-geteventchannel
- name: Gettestresults
  property_count: 5
  slug: salesforce-gettestresults
- name: Getteststatus
  property_count: 2
  slug: salesforce-getteststatus
- name: GiftCommitmentCustomField
  property_count: 2
  slug: salesforce-gift-commitment-custom-field
- name: GiftCommitmentScheduleCustomField
  property_count: 2
  slug: salesforce-gift-commitment-schedule-custom-field
- name: Gift
  property_count: 20
  slug: salesforce-gift
- name: GiftTransactionCustomField
  property_count: 2
  slug: salesforce-gift-transaction-custom-field
- name: Giftcommitment
  property_count: 2
  slug: salesforce-giftcommitment
- name: Giftcommitmentschedule
  property_count: 2
  slug: salesforce-giftcommitmentschedule
- name: Giftdefaultdesignation
  property_count: 2
  slug: salesforce-giftdefaultdesignation
- name: Gifttransaction
  property_count: 2
  slug: salesforce-gifttransaction
- name: Gifttransactiondesignation
  property_count: 2
  slug: salesforce-gifttransactiondesignation
- name: Global
  property_count: 3
  slug: salesforce-global
- name: GraphResponse
  property_count: 1
  slug: salesforce-graph-response
- name: Graph
  property_count: 2
  slug: salesforce-graph
- name: Graph1
  property_count: 3
  slug: salesforce-graph1
- name: Graph2
  property_count: 2
  slug: salesforce-graph2
- name: Graph3
  property_count: 2
  slug: salesforce-graph3
- name: Graph4
  property_count: 2
  slug: salesforce-graph4
- name: Graph5
  property_count: 2
  slug: salesforce-graph5
- name: GroupInvitesRequest
  property_count: 2
  slug: salesforce-group-invites-request
- name: GroupMembersPrivate-POST
  property_count: 8
  slug: salesforce-group-members-private-post
- name: Group
  property_count: 25
  slug: salesforce-group
- name: Group1
  property_count: 23
  slug: salesforce-group1
- name: Group2
  property_count: 6
  slug: salesforce-group2
- name: HasSubtypes
  property_count: 1
  slug: salesforce-has-subtypes
- name: Header
  property_count: 3
  slug: salesforce-header
- name: Header4
  property_count: 1
  slug: salesforce-header4
- name: Header5
  property_count: 1
  slug: salesforce-header5
- name: Header8
  property_count: 1
  slug: salesforce-header8
- name: Holiday
  property_count: 6
  slug: salesforce-holiday
- name: HomePhone
  property_count: 2
  slug: salesforce-home-phone
- name: HourlyAsyncReportRuns
  property_count: 2
  slug: salesforce-hourly-async-report-runs
- name: HourlyDashboardRefreshes
  property_count: 2
  slug: salesforce-hourly-dashboard-refreshes
- name: HourlyDashboardResults
  property_count: 2
  slug: salesforce-hourly-dashboard-results
- name: HourlyDashboardStatuses
  property_count: 2
  slug: salesforce-hourly-dashboard-statuses
- name: HourlyLongTermIdMapping
  property_count: 2
  slug: salesforce-hourly-long-term-id-mapping
- name: HourlyManagedContentPublicRequests
  property_count: 2
  slug: salesforce-hourly-managed-content-public-requests
- name: HourlyODataCallout
  property_count: 2
  slug: salesforce-hourly-o-data-callout
- name: HourlyPublishedPlatformEvents
  property_count: 2
  slug: salesforce-hourly-published-platform-events
- name: HourlyPublishedStandardVolumePlatformEvents
  property_count: 2
  slug: salesforce-hourly-published-standard-volume-platform-events
- name: HourlyShortTermIdMapping
  property_count: 2
  slug: salesforce-hourly-short-term-id-mapping
- name: HourlySyncReportRuns
  property_count: 2
  slug: salesforce-hourly-sync-report-runs
- name: HourlyTimeBasedWorkflow
  property_count: 2
  slug: salesforce-hourly-time-based-workflow
- name: HttpHeaders
  property_count: 1
  slug: salesforce-http-headers
- name: Icon
  property_count: 5
  slug: salesforce-icon
- name: Id
  property_count: 1
  slug: salesforce-id
- name: Id4
  property_count: 31
  slug: salesforce-id4
- name: Id8
  property_count: 2
  slug: salesforce-id8
- name: ImageHistory
  property_count: 6
  slug: salesforce-image-history
- name: Image
  property_count: 6
  slug: salesforce-image
- name: Implicit
  property_count: 2
  slug: salesforce-implicit
- name: IndividualHistory
  property_count: 6
  slug: salesforce-individual-history
- name: IndividualId
  property_count: 2
  slug: salesforce-individual-id
- name: IndividualId1
  property_count: 31
  slug: salesforce-individual-id1
- name: IndividualMemberEnrollmentsRequest
  property_count: 11
  slug: salesforce-individual-member-enrollments-request
- name: IndividualMemberEnrollments
  property_count: 5
  slug: salesforce-individual-member-enrollments
- name: Individual
  property_count: 6
  slug: salesforce-individual
- name: Industry
  property_count: 2
  slug: salesforce-industry
- name: Industry1
  property_count: 31
  slug: salesforce-industry1
- name: Industry2
  property_count: 2
  slug: salesforce-industry2
- name: Industry3
  property_count: 2
  slug: salesforce-industry3
- name: Info
  property_count: 3
  slug: salesforce-info
- name: Information
  property_count: 2
  slug: salesforce-information
- name: Infos
  property_count: 2
  slug: salesforce-infos
- name: InitiateAmendQuantityRequest
  property_count: 4
  slug: salesforce-initiate-amend-quantity-request
- name: InitiateCancellationRequest
  property_count: 3
  slug: salesforce-initiate-cancellation-request
- name: InitiateRenewalRequest
  property_count: 1
  slug: salesforce-initiate-renewal-request
- name: Input
  property_count: 1
  slug: salesforce-input
- name: Input1
  property_count: 1
  slug: salesforce-input1
- name: Input2
  property_count: 2
  slug: salesforce-input2
- name: Inputs
  property_count: 3
  slug: salesforce-inputs
- name: Inputs1
  property_count: 1
  slug: salesforce-inputs1
- name: Inputs2
  property_count: 1
  slug: salesforce-inputs2
- name: Inputs3
  property_count: 1
  slug: salesforce-inputs3
- name: Interactions
  property_count: 1
  slug: salesforce-interactions
- name: Invitees
  property_count: 1
  slug: salesforce-invitees
- name: InvokeRequest
  property_count: 2
  slug: salesforce-invoke-request
- name: IPAddressRange
  property_count: 6
  slug: salesforce-ip-address-range
- name: IsActive
  property_count: 31
  slug: salesforce-is-active
- name: IsConverted
  property_count: 31
  slug: salesforce-is-converted
- name: IsCustomerPortal
  property_count: 2
  slug: salesforce-is-customer-portal
- name: IsCustomerPortal1
  property_count: 31
  slug: salesforce-is-customer-portal1
- name: IsDeleted
  property_count: 2
  slug: salesforce-is-deleted
- name: IsDeleted2
  property_count: 31
  slug: salesforce-is-deleted2
- name: IsEmailBounced
  property_count: 2
  slug: salesforce-is-email-bounced
- name: IsExtIndicatorVisible
  property_count: 31
  slug: salesforce-is-ext-indicator-visible
- name: IsInterface
  property_count: 1
  slug: salesforce-is-interface
- name: IsPartner
  property_count: 2
  slug: salesforce-is-partner
- name: IsPartner1
  property_count: 31
  slug: salesforce-is-partner1
- name: IsPortalEnabled
  property_count: 31
  slug: salesforce-is-portal-enabled
- name: IsProfilePhotoActive
  property_count: 31
  slug: salesforce-is-profile-photo-active
- name: IsSubtype
  property_count: 1
  slug: salesforce-is-subtype
- name: IsUnreadByOwner
  property_count: 31
  slug: salesforce-is-unread-by-owner
- name: IssueaVoucherRequest
  property_count: 1
  slug: salesforce-issuea-voucher-request
- name: Item
  property_count: 1
  slug: salesforce-item
- name: Items
  property_count: 1
  slug: salesforce-items
- name: Items17
  property_count: 2
  slug: salesforce-items17
- name: Items18
  property_count: 1
  slug: salesforce-items18
- name: Items19
  property_count: 2
  slug: salesforce-items19
- name: Items20
  property_count: 2
  slug: salesforce-items20
- name: Items22
  property_count: 2
  slug: salesforce-items22
- name: Items23
  property_count: 2
  slug: salesforce-items23
- name: JigsawCompanyId
  property_count: 1
  slug: salesforce-jigsaw-company-id
- name: JigsawCompanyId1
  property_count: 31
  slug: salesforce-jigsaw-company-id1
- name: JigsawContactId
  property_count: 1
  slug: salesforce-jigsaw-contact-id
- name: JigsawContactId1
  property_count: 31
  slug: salesforce-jigsaw-contact-id1
- name: JigsawImportLimitOverride
  property_count: 31
  slug: salesforce-jigsaw-import-limit-override
- name: Jigsaw
  property_count: 2
  slug: salesforce-jigsaw
- name: Jigsaw2
  property_count: 31
  slug: salesforce-jigsaw2
- name: json
  property_count: 3
  slug: salesforce-json
- name: KeyPrefix
  property_count: 1
  slug: salesforce-key-prefix
- name: Key
  property_count: 6
  slug: salesforce-key
- name: LabelPlural
  property_count: 1
  slug: salesforce-label-plural
- name: Label
  property_count: 1
  slug: salesforce-label
- name: LanguageLocaleKey
  property_count: 31
  slug: salesforce-language-locale-key
- name: LastActivityDate
  property_count: 3
  slug: salesforce-last-activity-date
- name: LastActivityDate2
  property_count: 31
  slug: salesforce-last-activity-date2
- name: LastCURequestDate
  property_count: 2
  slug: salesforce-last-cu-request-date
- name: LastCUUpdateDate
  property_count: 2
  slug: salesforce-last-cu-update-date
- name: LastEditedBy
  property_count: 19
  slug: salesforce-last-edited-by
- name: LastLoginDate
  property_count: 31
  slug: salesforce-last-login-date
- name: LastModifiedById
  property_count: 1
  slug: salesforce-last-modified-by-id
- name: LastModifiedById2
  property_count: 31
  slug: salesforce-last-modified-by-id2
- name: LastModifiedById5
  property_count: 2
  slug: salesforce-last-modified-by-id5
- name: LastModifiedBy
  property_count: 3
  slug: salesforce-last-modified-by
- name: LastModifiedBy3
  property_count: 2
  slug: salesforce-last-modified-by3
- name: LastModifiedDate
  property_count: 2
  slug: salesforce-last-modified-date
- name: LastModifiedDate14
  property_count: 2
  slug: salesforce-last-modified-date14
- name: LastModifiedDate2
  property_count: 31
  slug: salesforce-last-modified-date2
- name: LastModifiedDate5
  property_count: 2
  slug: salesforce-last-modified-date5
- name: LastName
  property_count: 2
  slug: salesforce-last-name
- name: LastName1
  property_count: 31
  slug: salesforce-last-name1
- name: LastName4
  property_count: 2
  slug: salesforce-last-name4
- name: LastPasswordChangeDate
  property_count: 31
  slug: salesforce-last-password-change-date
- name: LastReferencedDate
  property_count: 3
  slug: salesforce-last-referenced-date
- name: LastReferencedDate2
  property_count: 31
  slug: salesforce-last-referenced-date2
- name: LastViewedDate
  property_count: 3
  slug: salesforce-last-viewed-date
- name: LastViewedDate2
  property_count: 31
  slug: salesforce-last-viewed-date2
- name: Latitude
  property_count: 31
  slug: salesforce-latitude
- name: LaunchFlowRequest
  property_count: 1
  slug: salesforce-launch-flow-request
- name: LayoutComponent
  property_count: 3
  slug: salesforce-layout-component
- name: LayoutComponent1
  property_count: 5
  slug: salesforce-layout-component1
- name: LayoutItem
  property_count: 7
  slug: salesforce-layout-item
- name: LayoutItem1
  property_count: 7
  slug: salesforce-layout-item1
- name: LayoutRow
  property_count: 1
  slug: salesforce-layout-row
- name: LayoutRow1
  property_count: 1
  slug: salesforce-layout-row1
- name: Layout
  property_count: 8
  slug: salesforce-layout
- name: LayoutUserStates
  property_count: 1
  slug: salesforce-layout-user-states
- name: Layout1
  property_count: 8
  slug: salesforce-layout1
- name: Layoutable
  property_count: 1
  slug: salesforce-layoutable
- name: Layouts
  property_count: 1
  slug: salesforce-layouts
- name: LeadHistory
  property_count: 6
  slug: salesforce-lead-history
- name: Lead
  property_count: 1
  slug: salesforce-lead
- name: LeadSource
  property_count: 2
  slug: salesforce-lead-source
- name: LeadSource1
  property_count: 31
  slug: salesforce-lead-source1
- name: LeadSource2
  property_count: 2
  slug: salesforce-lead-source2
- name: LeadSource4
  property_count: 5
  slug: salesforce-lead-source4
- name: Lead1
  property_count: 23
  slug: salesforce-lead1
- name: Lead2
  property_count: 6
  slug: salesforce-lead2
- name: LevelC
  property_count: 5
  slug: salesforce-level-c
- name: Likes
  property_count: 8
  slug: salesforce-likes
- name: Limits
  property_count: 52
  slug: salesforce-limits
- name: Links
  property_count: 5
  slug: salesforce-links
- name: Links11
  property_count: 2
  slug: salesforce-links11
- name: Links13
  property_count: 2
  slug: salesforce-links13
- name: Links3
  property_count: 1
  slug: salesforce-links3
- name: Links7
  property_count: 6
  slug: salesforce-links7
- name: Links9
  property_count: 4
  slug: salesforce-links9
- name: ListEmail
  property_count: 6
  slug: salesforce-list-email
- name: listMetadataQuery
  property_count: 2
  slug: salesforce-list-metadata-query
- name: listMetadataResponse
  property_count: 1
  slug: salesforce-list-metadata-response
- name: listMetadata
  property_count: 2
  slug: salesforce-list-metadata
- name: ListReference
  property_count: 4
  slug: salesforce-list-reference
- name: ListSandboxes
  property_count: 6
  slug: salesforce-list-sandboxes
- name: List
  property_count: 4
  slug: salesforce-list
- name: ListViewChartInstance
  property_count: 3
  slug: salesforce-list-view-chart-instance
- name: Listchannelmembers
  property_count: 6
  slug: salesforce-listchannelmembers
- name: Listeventchannels
  property_count: 6
  slug: salesforce-listeventchannels
- name: Listnamedcredentials
  property_count: 6
  slug: salesforce-listnamedcredentials
- name: LocaleSidKey
  property_count: 31
  slug: salesforce-locale-sid-key
- name: Location
  property_count: 2
  slug: salesforce-location
- name: Longitude
  property_count: 31
  slug: salesforce-longitude
- name: LookupResults
  property_count: 1
  slug: salesforce-lookup-results
- name: LookupTableRequest
  property_count: 2
  slug: salesforce-lookup-table-request
- name: LookupTableRequest1
  property_count: 1
  slug: salesforce-lookup-table-request1
- name: LoyaltyProgramCurrency
  property_count: 1
  slug: salesforce-loyalty-program-currency
- name: LoyaltyProgram
  property_count: 1
  slug: salesforce-loyalty-program
- name: m200
  property_count: 2
  slug: salesforce-m200
- name: m304
  property_count: 2
  slug: salesforce-m304
- name: MacroHistory
  property_count: 6
  slug: salesforce-macro-history
- name: Macro
  property_count: 6
  slug: salesforce-macro
- name: MailingAddress
  property_count: 2
  slug: salesforce-mailing-address
- name: MailingCity
  property_count: 2
  slug: salesforce-mailing-city
- name: MailingCountry
  property_count: 2
  slug: salesforce-mailing-country
- name: MailingGeocodeAccuracy
  property_count: 2
  slug: salesforce-mailing-geocode-accuracy
- name: MailingGeocodeAccuracy1
  property_count: 5
  slug: salesforce-mailing-geocode-accuracy1
- name: MailingLatitude
  property_count: 2
  slug: salesforce-mailing-latitude
- name: MailingLongitude
  property_count: 2
  slug: salesforce-mailing-longitude
- name: MailingPostalCode
  property_count: 2
  slug: salesforce-mailing-postal-code
- name: MailingState
  property_count: 2
  slug: salesforce-mailing-state
- name: MailingStreet
  property_count: 2
  slug: salesforce-mailing-street
- name: ManagedContent
  property_count: 6
  slug: salesforce-managed-content
- name: ManagedContentVariant
  property_count: 6
  slug: salesforce-managed-content-variant
- name: ManagerId
  property_count: 31
  slug: salesforce-manager-id
- name: MassEmail
  property_count: 2
  slug: salesforce-mass-email
- name: MasterRecordId
  property_count: 2
  slug: salesforce-master-record-id
- name: MasterRecordId2
  property_count: 31
  slug: salesforce-master-record-id2
- name: MatchBillingAddressC
  property_count: 1
  slug: salesforce-match-billing-address-c
- name: MediumBannerPhotoUrl
  property_count: 31
  slug: salesforce-medium-banner-photo-url
- name: MediumPhotoUrl
  property_count: 31
  slug: salesforce-medium-photo-url
- name: MemberBenefits
  property_count: 1
  slug: salesforce-member-benefits
- name: MemberBenefits1
  property_count: 11
  slug: salesforce-member-benefits1
- name: MemberCurrency
  property_count: 20
  slug: salesforce-member-currency
- name: MemberProfile
  property_count: 24
  slug: salesforce-member-profile
- name: MemberTier
  property_count: 12
  slug: salesforce-member-tier
- name: MemberVouchers
  property_count: 2
  slug: salesforce-member-vouchers
- name: MerchandiseC
  property_count: 6
  slug: salesforce-merchandise-c
- name: MerchandisingMixC
  property_count: 6
  slug: salesforce-merchandising-mix-c
- name: Mergeable
  property_count: 1
  slug: salesforce-mergeable
- name: Message
  property_count: 1
  slug: salesforce-message
- name: MessageSegment
  property_count: 2
  slug: salesforce-message-segment
- name: MessageSegment1
  property_count: 4
  slug: salesforce-message-segment1
- name: MessageSegment11
  property_count: 6
  slug: salesforce-message-segment11
- name: MessageSegment2
  property_count: 4
  slug: salesforce-message-segment2
- name: MessageSegment3
  property_count: 9
  slug: salesforce-message-segment3
- name: MessageSegment5
  property_count: 4
  slug: salesforce-message-segment5
- name: metadataObjects
  property_count: 6
  slug: salesforce-metadata-objects
- name: Metadata
  property_count: 2
  slug: salesforce-metadata
- name: Metadata1
  property_count: 3
  slug: salesforce-metadata1
- name: Metadata10
  property_count: 4
  slug: salesforce-metadata10
- name: Metadata12
  property_count: 4
  slug: salesforce-metadata12
- name: Metadata13
  property_count: 1
  slug: salesforce-metadata13
- name: Metadata14
  property_count: 2
  slug: salesforce-metadata14
- name: Metadata15
  property_count: 5
  slug: salesforce-metadata15
- name: Metadata17
  property_count: 4
  slug: salesforce-metadata17
- name: Metadata18
  property_count: 1
  slug: salesforce-metadata18
- name: Metadata2
  property_count: 3
  slug: salesforce-metadata2
- name: Metadata3
  property_count: 2
  slug: salesforce-metadata3
- name: Metadata6
  property_count: 3
  slug: salesforce-metadata6
- name: Metadata7
  property_count: 4
  slug: salesforce-metadata7
- name: Metadata9
  property_count: 5
  slug: salesforce-metadata9
- name: Method
  property_count: 8
  slug: salesforce-method
- name: MixItemC
  property_count: 6
  slug: salesforce-mix-item-c
- name: MobilePhone
  property_count: 2
  slug: salesforce-mobile-phone
- name: MobilePhone1
  property_count: 31
  slug: salesforce-mobile-phone1
- name: MobilePhone3
  property_count: 2
  slug: salesforce-mobile-phone3
- name: MobileSDK
  property_count: 4
  slug: salesforce-mobile-sdk
- name: ModelField
  property_count: 3
  slug: salesforce-model-field
- name: Model
  property_count: 1
  slug: salesforce-model
- name: Model1
  property_count: 18
  slug: salesforce-model1
- name: Model3
  property_count: 6
  slug: salesforce-model3
- name: MonthlyEinsteinDiscoveryStoryCreation
  property_count: 2
  slug: salesforce-monthly-einstein-discovery-story-creation
- name: Motif
  property_count: 5
  slug: salesforce-motif
- name: MruEnabled
  property_count: 1
  slug: salesforce-mru-enabled
- name: Mute
  property_count: 1
  slug: salesforce-mute
- name: MySubscription
  property_count: 2
  slug: salesforce-my-subscription
- name: NaicsCode
  property_count: 2
  slug: salesforce-naics-code
- name: NaicsCode1
  property_count: 31
  slug: salesforce-naics-code1
- name: NaicsDesc
  property_count: 2
  slug: salesforce-naics-desc
- name: NaicsDesc1
  property_count: 31
  slug: salesforce-naics-desc1
- name: NameOrAlias
  property_count: 31
  slug: salesforce-name-or-alias
- name: Name
  property_count: 1
  slug: salesforce-name
- name: Name13
  property_count: 1
  slug: salesforce-name13
- name: Name14
  property_count: 2
  slug: salesforce-name14
- name: Name16
  property_count: 31
  slug: salesforce-name16
- name: Name17
  property_count: 31
  slug: salesforce-name17
- name: Name18
  property_count: 23
  slug: salesforce-name18
- name: Name19
  property_count: 31
  slug: salesforce-name19
- name: Name21
  property_count: 2
  slug: salesforce-name21
- name: Name42
  property_count: 2
  slug: salesforce-name42
- name: NamedCredential
  property_count: 6
  slug: salesforce-named-credential
- name: NamespaceRegistryHistory
  property_count: 6
  slug: salesforce-namespace-registry-history
- name: NamespaceRegistry
  property_count: 6
  slug: salesforce-namespace-registry
- name: NavItem
  property_count: 15
  slug: salesforce-nav-item
- name: NavItem2
  property_count: 15
  slug: salesforce-nav-item2
- name: NavItem3
  property_count: 15
  slug: salesforce-nav-item3
- name: NavItem5
  property_count: 15
  slug: salesforce-nav-item5
- name: NavItem6
  property_count: 15
  slug: salesforce-nav-item6
- name: Node
  property_count: 2
  slug: salesforce-node
- name: Node10
  property_count: 4
  slug: salesforce-node10
- name: Node6
  property_count: 3
  slug: salesforce-node6
- name: Node7
  property_count: 5
  slug: salesforce-node7
- name: Note
  property_count: 6
  slug: salesforce-note
- name: NumberOfContactsC
  property_count: 1
  slug: salesforce-number-of-contacts-c
- name: NumberOfEmployees
  property_count: 2
  slug: salesforce-number-of-employees
- name: NumberOfEmployees1
  property_count: 31
  slug: salesforce-number-of-employees1
- name: NumberOfEmployees2
  property_count: 2
  slug: salesforce-number-of-employees2
- name: NumberOfEmployees7
  property_count: 2
  slug: salesforce-number-of-employees7
- name: NumberOfFailedLogins
  property_count: 31
  slug: salesforce-number-of-failed-logins
- name: NumberofLocationsC
  property_count: 1
  slug: salesforce-numberof-locations-c
- name: NumberofLocationsC1
  property_count: 31
  slug: salesforce-numberof-locations-c1
- name: NumberofLocationsC2
  property_count: 2
  slug: salesforce-numberof-locations-c2
- name: NumberofLocationsC5
  property_count: 2
  slug: salesforce-numberof-locations-c5
- name: OAuth2
  property_count: 3
  slug: salesforce-o-auth2
- name: ObjectDescribe
  property_count: 2
  slug: salesforce-object-describe
- name: ObjectDescribe1
  property_count: 28
  slug: salesforce-object-describe1
- name: ObjectInfos
  property_count: 4
  slug: salesforce-object-infos
- name: ObjectInfos1
  property_count: 2
  slug: salesforce-object-infos1
- name: Objects
  property_count: 172
  slug: salesforce-objects
- name: OfflinePdaTrialExpirationDate
  property_count: 31
  slug: salesforce-offline-pda-trial-expiration-date
- name: OfflineTrialExpirationDate
  property_count: 31
  slug: salesforce-offline-trial-expiration-date
- name: OpenIDConnectDiscovery
  property_count: 2
  slug: salesforce-open-id-connect-discovery
- name: OpenIDConnectDynamicClientRegistrationEndpointRequest
  property_count: 6
  slug: salesforce-open-id-connect-dynamic-client-registration-endpoint-request
- name: OpportunitiesClosingSoonExplicitAND
  property_count: 2
  slug: salesforce-opportunities-closing-soon-explicit-and
- name: OpportunitiesClosingSoon
  property_count: 2
  slug: salesforce-opportunities-closing-soon
- name: OpportunitiesEarlyStage
  property_count: 2
  slug: salesforce-opportunities-early-stage
- name: OpportunitiesNotClosed
  property_count: 2
  slug: salesforce-opportunities-not-closed
- name: OpportunityContactRole
  property_count: 6
  slug: salesforce-opportunity-contact-role
- name: OpportunityFieldHistory
  property_count: 6
  slug: salesforce-opportunity-field-history
- name: OpportunityHistory
  property_count: 6
  slug: salesforce-opportunity-history
- name: OpportunityLineItem
  property_count: 6
  slug: salesforce-opportunity-line-item
- name: OpportunityPartner
  property_count: 6
  slug: salesforce-opportunity-partner
- name: Opportunity
  property_count: 1
  slug: salesforce-opportunity
- name: Opportunity3
  property_count: 1
  slug: salesforce-opportunity3
- name: Opportunity4
  property_count: 6
  slug: salesforce-opportunity4
- name: OptOutfromaPromotionRequest
  property_count: 1
  slug: salesforce-opt-outfroma-promotion-request
- name: OrderHistory
  property_count: 6
  slug: salesforce-order-history
- name: OrderItemHistory
  property_count: 6
  slug: salesforce-order-item-history
- name: OrderItem
  property_count: 6
  slug: salesforce-order-item
- name: Order
  property_count: 6
  slug: salesforce-order
- name: OrderedByInfo
  property_count: 3
  slug: salesforce-ordered-by-info
- name: OrgMetricScanResult
  property_count: 6
  slug: salesforce-org-metric-scan-result
- name: OrgMetricScanSummary
  property_count: 6
  slug: salesforce-org-metric-scan-summary
- name: OrgMetric
  property_count: 6
  slug: salesforce-org-metric
- name: Organization
  property_count: 6
  slug: salesforce-organization
- name: OtherAddress
  property_count: 2
  slug: salesforce-other-address
- name: OtherCity
  property_count: 2
  slug: salesforce-other-city
- name: OtherCountry
  property_count: 2
  slug: salesforce-other-country
- name: OtherGeocodeAccuracy
  property_count: 2
  slug: salesforce-other-geocode-accuracy
- name: OtherGeocodeAccuracy1
  property_count: 5
  slug: salesforce-other-geocode-accuracy1
- name: OtherLatitude
  property_count: 2
  slug: salesforce-other-latitude
- name: OtherLongitude
  property_count: 2
  slug: salesforce-other-longitude
- name: OtherPhone
  property_count: 2
  slug: salesforce-other-phone
- name: OtherPostalCode
  property_count: 2
  slug: salesforce-other-postal-code
- name: OtherState
  property_count: 2
  slug: salesforce-other-state
- name: OtherStreet
  property_count: 2
  slug: salesforce-other-street
- name: OutOfOfficeMessage
  property_count: 31
  slug: salesforce-out-of-office-message
- name: OutOfOffice
  property_count: 1
  slug: salesforce-out-of-office
- name: Outcome
  property_count: 3
  slug: salesforce-outcome
- name: OutputParameters
  property_count: 1
  slug: salesforce-output-parameters
- name: OutputParameters1
  property_count: 1
  slug: salesforce-output-parameters1
- name: OutputParameters2
  property_count: 1
  slug: salesforce-output-parameters2
- name: OutputParameters3
  property_count: 1
  slug: salesforce-output-parameters3
- name: Output
  property_count: 1
  slug: salesforce-output
- name: OutputValues
  property_count: 1
  slug: salesforce-output-values
- name: OutputValues1
  property_count: 1
  slug: salesforce-output-values1
- name: Output1
  property_count: 2
  slug: salesforce-output1
- name: Output2
  property_count: 1
  slug: salesforce-output2
- name: Output4
  property_count: 5
  slug: salesforce-output4
- name: OutreachSourceCode
  property_count: 2
  slug: salesforce-outreach-source-code
- name: OwnerId
  property_count: 2
  slug: salesforce-owner-id
- name: OwnerId2
  property_count: 31
  slug: salesforce-owner-id2
- name: OwnerId4
  property_count: 2
  slug: salesforce-owner-id4
- name: Owner
  property_count: 19
  slug: salesforce-owner
- name: Owner11
  property_count: 2
  slug: salesforce-owner11
- name: Owner4
  property_count: 2
  slug: salesforce-owner4
- name: Owner6
  property_count: 2
  slug: salesforce-owner6
- name: Ownership
  property_count: 2
  slug: salesforce-ownership
- name: Ownership1
  property_count: 31
  slug: salesforce-ownership1
- name: Ownership2
  property_count: 2
  slug: salesforce-ownership2
- name: Ownership4
  property_count: 2
  slug: salesforce-ownership4
- name: Package2VersionCreates
  property_count: 2
  slug: salesforce-package2-version-creates
- name: Package2VersionCreatesWithoutValidation
  property_count: 2
  slug: salesforce-package2-version-creates-without-validation
- name: PageInfo
  property_count: 4
  slug: salesforce-page-info
- name: PageReference
  property_count: 3
  slug: salesforce-page-reference
- name: PageReference6
  property_count: 3
  slug: salesforce-page-reference6
- name: Page
  property_count: 8
  slug: salesforce-page
- name: Page1
  property_count: 8
  slug: salesforce-page1
- name: Parameter
  property_count: 4
  slug: salesforce-parameter
- name: Parameter1
  property_count: 5
  slug: salesforce-parameter1
- name: Parameter4
  property_count: 5
  slug: salesforce-parameter4
- name: Parameter5
  property_count: 2
  slug: salesforce-parameter5
- name: ParentId
  property_count: 2
  slug: salesforce-parent-id
- name: ParentId1
  property_count: 31
  slug: salesforce-parent-id1
- name: ParentId2
  property_count: 2
  slug: salesforce-parent-id2
- name: Parent
  property_count: 7
  slug: salesforce-parent
- name: Parent2
  property_count: 20
  slug: salesforce-parent2
- name: Parent4
  property_count: 2
  slug: salesforce-parent4
- name: Parent7
  property_count: 2
  slug: salesforce-parent7
- name: PartnerFundAllocationHistory
  property_count: 6
  slug: salesforce-partner-fund-allocation-history
- name: PartnerFundAllocation
  property_count: 6
  slug: salesforce-partner-fund-allocation
- name: PartnerFundClaimHistory
  property_count: 6
  slug: salesforce-partner-fund-claim-history
- name: PartnerFundClaim
  property_count: 6
  slug: salesforce-partner-fund-claim
- name: PartnerFundRequestHistory
  property_count: 6
  slug: salesforce-partner-fund-request-history
- name: PartnerFundRequest
  property_count: 6
  slug: salesforce-partner-fund-request
- name: PartnerMarketingBudgetHistory
  property_count: 6
  slug: salesforce-partner-marketing-budget-history
- name: PartnerMarketingBudget
  property_count: 6
  slug: salesforce-partner-marketing-budget
- name: Partner
  property_count: 6
  slug: salesforce-partner
- name: PartyConsentHistory
  property_count: 6
  slug: salesforce-party-consent-history
- name: PartyConsent
  property_count: 6
  slug: salesforce-party-consent
- name: Password
  property_count: 2
  slug: salesforce-password
- name: PasswordlessLogin-InitializeRequest
  property_count: 3
  slug: salesforce-passwordless-login-initialize-request
- name: Paths
  property_count: 1
  slug: salesforce-paths
- name: PaymentInstrument
  property_count: 16
  slug: salesforce-payment-instrument
- name: Paymentinstrument1
  property_count: 2
  slug: salesforce-paymentinstrument1
- name: Period
  property_count: 6
  slug: salesforce-period
- name: PermissionSets
  property_count: 3
  slug: salesforce-permission-sets
- name: Phone
  property_count: 2
  slug: salesforce-phone
- name: Phone2
  property_count: 31
  slug: salesforce-phone2
- name: Phone5
  property_count: 2
  slug: salesforce-phone5
- name: Phone9
  property_count: 2
  slug: salesforce-phone9
- name: Photo
  property_count: 7
  slug: salesforce-photo
- name: PhotoUrl
  property_count: 2
  slug: salesforce-photo-url
- name: PhotoUrl2
  property_count: 31
  slug: salesforce-photo-url2
- name: PhotoUrl4
  property_count: 2
  slug: salesforce-photo-url4
- name: Photo15
  property_count: 7
  slug: salesforce-photo15
- name: Photos
  property_count: 2
  slug: salesforce-photos
- name: PicklistFieldValues
  property_count: 6
  slug: salesforce-picklist-field-values
- name: PicklistValue
  property_count: 5
  slug: salesforce-picklist-value
- name: PicklistValue1
  property_count: 5
  slug: salesforce-picklist-value1
- name: PicklistValue2
  property_count: 5
  slug: salesforce-picklist-value2
- name: PicklistValue31
  property_count: 5
  slug: salesforce-picklist-value31
- name: PlatformEventSchemabyEventName
  property_count: 4
  slug: salesforce-platform-event-schemaby-event-name
- name: PortalRole
  property_count: 31
  slug: salesforce-portal-role
- name: Post
  property_count: 3
  slug: salesforce-post
- name: PostToolingSObjectRequest
  property_count: 1
  slug: salesforce-post-tooling-s-object-request
- name: PostalCode
  property_count: 31
  slug: salesforce-postal-code
- name: PostalCode2
  property_count: 2
  slug: salesforce-postal-code2
- name: PostalCode3
  property_count: 2
  slug: salesforce-postal-code3
- name: PotentialValueC
  property_count: 1
  slug: salesforce-potential-value-c
- name: PredictRequest
  property_count: 4
  slug: salesforce-predict-request
- name: Predict
  property_count: 3
  slug: salesforce-predict
- name: PredictionDefinitions1
  property_count: 14
  slug: salesforce-prediction-definitions1
- name: Prediction
  property_count: 4
  slug: salesforce-prediction
- name: Prediction1
  property_count: 2
  slug: salesforce-prediction1
- name: Predictiondefinitionmetadata
  property_count: 14
  slug: salesforce-predictiondefinitionmetadata
- name: Predictiondefinitions
  property_count: 4
  slug: salesforce-predictiondefinitions
- name: Predictionmodels
  property_count: 3
  slug: salesforce-predictionmodels
- name: PrescribableField
  property_count: 2
  slug: salesforce-prescribable-field
- name: PricebookEntryHistory
  property_count: 6
  slug: salesforce-pricebook-entry-history
- name: PricebookEntry
  property_count: 6
  slug: salesforce-pricebook-entry
- name: Pricebook2History
  property_count: 6
  slug: salesforce-pricebook2-history
- name: Pricebook2
  property_count: 6
  slug: salesforce-pricebook2
- name: PrimaryC
  property_count: 31
  slug: salesforce-primary-c
- name: PrimaryC1
  property_count: 2
  slug: salesforce-primary-c1
- name: Principal
  property_count: 3
  slug: salesforce-principal
- name: Principal1
  property_count: 7
  slug: salesforce-principal1
- name: PrivateConnectOutboundCalloutHourlyLimitMB
  property_count: 2
  slug: salesforce-private-connect-outbound-callout-hourly-limit-mb
- name: ProcessApprovalsSubmitRequest
  property_count: 7
  slug: salesforce-process-approvals-submit-request
- name: ProcessDefinition
  property_count: 6
  slug: salesforce-process-definition
- name: ProcessInstance
  property_count: 6
  slug: salesforce-process-instance
- name: ProcessParameter
  property_count: 2
  slug: salesforce-process-parameter
- name: ProcessParameter1
  property_count: 2
  slug: salesforce-process-parameter1
- name: ProcessParameter2
  property_count: 2
  slug: salesforce-process-parameter2
- name: ProcessParameter3
  property_count: 2
  slug: salesforce-process-parameter3
- name: ProcessParameter4
  property_count: 1
  slug: salesforce-process-parameter4
- name: ProcessParameter5
  property_count: 4
  slug: salesforce-process-parameter5
- name: ProcessParameter7
  property_count: 2
  slug: salesforce-process-parameter7
- name: ProcessParameter8
  property_count: 5
  slug: salesforce-process-parameter8
- name: ProcessParameter9
  property_count: 3
  slug: salesforce-process-parameter9
- name: ProcessingOptions
  property_count: 1
  slug: salesforce-processing-options
- name: ProductConsumptionSchedule
  property_count: 6
  slug: salesforce-product-consumption-schedule
- name: ProductContext
  property_count: 2
  slug: salesforce-product-context
- name: ProductContext1
  property_count: 1
  slug: salesforce-product-context1
- name: ProductInterestC
  property_count: 31
  slug: salesforce-product-interest-c
- name: ProductInterestC1
  property_count: 2
  slug: salesforce-product-interest-c1
- name: Product2History
  property_count: 6
  slug: salesforce-product2-history
- name: Product2
  property_count: 6
  slug: salesforce-product2
- name: ProfileId
  property_count: 31
  slug: salesforce-profile-id
- name: ProfilePhotoId
  property_count: 31
  slug: salesforce-profile-photo-id
- name: ProfileSkillEndorsementHistory
  property_count: 6
  slug: salesforce-profile-skill-endorsement-history
- name: ProfileSkillEndorsement
  property_count: 6
  slug: salesforce-profile-skill-endorsement
- name: ProfileSkillHistory
  property_count: 6
  slug: salesforce-profile-skill-history
- name: ProfileSkill
  property_count: 6
  slug: salesforce-profile-skill
- name: ProfileSkillUserHistory
  property_count: 6
  slug: salesforce-profile-skill-user-history
- name: ProfileSkillUser
  property_count: 6
  slug: salesforce-profile-skill-user
- name: PromotionEligibility
  property_count: 6
  slug: salesforce-promotion-eligibility
- name: PromotionLimits
  property_count: 8
  slug: salesforce-promotion-limits
- name: PromotionsCreationRequest
  property_count: 11
  slug: salesforce-promotions-creation-request
- name: Properties
  property_count: 2
  slug: salesforce-properties
- name: Properties1
  property_count: 29
  slug: salesforce-properties1
- name: Properties10
  property_count: 3
  slug: salesforce-properties10
- name: Properties12
  property_count: 60
  slug: salesforce-properties12
- name: Properties2
  property_count: 1
  slug: salesforce-properties2
- name: Properties3
  property_count: 2
  slug: salesforce-properties3
- name: Properties4
  property_count: 74
  slug: salesforce-properties4
- name: Properties5
  property_count: 2
  slug: salesforce-properties5
- name: Properties6
  property_count: 4
  slug: salesforce-properties6
- name: Properties7
  property_count: 1
  slug: salesforce-properties7
- name: Properties8
  property_count: 5
  slug: salesforce-properties8
- name: Properties9
  property_count: 4
  slug: salesforce-properties9
- name: PublishCallbackUsageInApex
  property_count: 2
  slug: salesforce-publish-callback-usage-in-apex
- name: PublishmultipleeventsRequest
  property_count: 2
  slug: salesforce-publishmultipleevents-request
- name: PublishsingleeventRequest
  property_count: 3
  slug: salesforce-publishsingleevent-request
- name: Publishsingleevent
  property_count: 3
  slug: salesforce-publishsingleevent
- name: QueryAll
  property_count: 3
  slug: salesforce-query-all
- name: Salesforce SOQL Query Result
  property_count: 4
  slug: salesforce-query-result
- name: Query
  property_count: 1
  slug: salesforce-query
- name: Query10
  property_count: 1
  slug: salesforce-query10
- name: Query11
  property_count: 3
  slug: salesforce-query11
- name: Query3
  property_count: 1
  slug: salesforce-query3
- name: Query4
  property_count: 1
  slug: salesforce-query4
- name: Query6
  property_count: 1
  slug: salesforce-query6
- name: Query7
  property_count: 1
  slug: salesforce-query7
- name: Queryable
  property_count: 1
  slug: salesforce-queryable
- name: QuickTextHistory
  property_count: 6
  slug: salesforce-quick-text-history
- name: QuickText
  property_count: 6
  slug: salesforce-quick-text
- name: QuoteTermReaderAPIRequest
  property_count: 1
  slug: salesforce-quote-term-reader-api-request
- name: Rating
  property_count: 2
  slug: salesforce-rating
- name: Rating1
  property_count: 31
  slug: salesforce-rating1
- name: Rating2
  property_count: 2
  slug: salesforce-rating2
- name: Rating3
  property_count: 2
  slug: salesforce-rating3
- name: ReadBy
  property_count: 3
  slug: salesforce-read-by
- name: ReadProductAPIRequest
  property_count: 1
  slug: salesforce-read-product-api-request
- name: ReceivesAdminInfoEmails
  property_count: 31
  slug: salesforce-receives-admin-info-emails
- name: ReceivesInfoEmails
  property_count: 31
  slug: salesforce-receives-info-emails
- name: RecentItems
  property_count: 2
  slug: salesforce-recent-items
- name: Recipient
  property_count: 19
  slug: salesforce-recipient
- name: Recommendation
  property_count: 6
  slug: salesforce-recommendation
- name: RecordAction
  property_count: 6
  slug: salesforce-record-action
- name: RecordCount
  property_count: 1
  slug: salesforce-record-count
- name: Record
  property_count: 11
  slug: salesforce-record
- name: RecordTypeId
  property_count: 31
  slug: salesforce-record-type-id
- name: RecordTypeInfo
  property_count: 8
  slug: salesforce-record-type-info
- name: RecordTypeInfos
  property_count: 1
  slug: salesforce-record-type-infos
- name: RecordType
  property_count: 6
  slug: salesforce-record-type
- name: Record10
  property_count: 6
  slug: salesforce-record10
- name: Record11
  property_count: 20
  slug: salesforce-record11
- name: Record12
  property_count: 14
  slug: salesforce-record12
- name: Record13
  property_count: 2
  slug: salesforce-record13
- name: Record14
  property_count: 70
  slug: salesforce-record14
- name: Record15
  property_count: 2
  slug: salesforce-record15
- name: Record16
  property_count: 2
  slug: salesforce-record16
- name: Record17
  property_count: 9
  slug: salesforce-record17
- name: Record18
  property_count: 2
  slug: salesforce-record18
- name: Record19
  property_count: 13
  slug: salesforce-record19
- name: Record2
  property_count: 8
  slug: salesforce-record2
- name: Record20
  property_count: 2
  slug: salesforce-record20
- name: Record21
  property_count: 14
  slug: salesforce-record21
- name: Record22
  property_count: 2
  slug: salesforce-record22
- name: Record23
  property_count: 13
  slug: salesforce-record23
- name: Record24
  property_count: 5
  slug: salesforce-record24
- name: Record25
  property_count: 4
  slug: salesforce-record25
- name: Record27
  property_count: 11
  slug: salesforce-record27
- name: Record28
  property_count: 11
  slug: salesforce-record28
- name: Record3
  property_count: 4
  slug: salesforce-record3
- name: Record4
  property_count: 6
  slug: salesforce-record4
- name: Record5
  property_count: 5
  slug: salesforce-record5
- name: Record6
  property_count: 3
  slug: salesforce-record6
- name: Record7
  property_count: 3
  slug: salesforce-record7
- name: Record8
  property_count: 19
  slug: salesforce-record8
- name: Record9
  property_count: 5
  slug: salesforce-record9
- name: Records
  property_count: 2
  slug: salesforce-records
- name: Records1
  property_count: 11
  slug: salesforce-records1
- name: Records2
  property_count: 11
  slug: salesforce-records2
- name: Records3
  property_count: 11
  slug: salesforce-records3
- name: Records4
  property_count: 10
  slug: salesforce-records4
- name: RedeemVoucherRequest
  property_count: 2
  slug: salesforce-redeem-voucher-request
- name: RedeemVoucher
  property_count: 2
  slug: salesforce-redeem-voucher
- name: Reference
  property_count: 2
  slug: salesforce-reference
- name: ReferenceToInfo
  property_count: 2
  slug: salesforce-reference-to-info
- name: RefreshSandboxRequest
  property_count: 2
  slug: salesforce-refresh-sandbox-request
- name: RegionC
  property_count: 1
  slug: salesforce-region-c
- name: Registration-InitializeRequest
  property_count: 5
  slug: salesforce-registration-initialize-request
- name: RelatedId
  property_count: 31
  slug: salesforce-related-id
- name: RelatedNamedCredential
  property_count: 4
  slug: salesforce-related-named-credential
- name: RenewedContract
  property_count: 2
  slug: salesforce-renewed-contract
- name: Replicateable
  property_count: 1
  slug: salesforce-replicateable
- name: ReportAnomalyEventStore
  property_count: 6
  slug: salesforce-report-anomaly-event-store
- name: Report
  property_count: 6
  slug: salesforce-report
- name: ReportsToId
  property_count: 2
  slug: salesforce-reports-to-id
- name: RequestBody
  property_count: 1
  slug: salesforce-request-body
- name: RequestProductInformationBundledComponentsRequest
  property_count: 2
  slug: salesforce-request-product-information-bundled-components-request
- name: RequestProductInformationNoBundlesRequest
  property_count: 3
  slug: salesforce-request-product-information-no-bundles-request
- name: Request
  property_count: 8
  slug: salesforce-request
- name: RequestedGroup
  property_count: 2
  slug: salesforce-requested-group
- name: ResourcesbyVersion
  property_count: 48
  slug: salesforce-resourcesby-version
- name: RestApiError
  property_count: 2
  slug: salesforce-rest-api-error
- name: ApiVersion
  property_count: 3
  slug: salesforce-rest-api-version
- name: CompositeRequest
  property_count: 3
  slug: salesforce-rest-composite-request
- name: CompositeResponse
  property_count: 1
  slug: salesforce-rest-composite-response
- name: Error
  property_count: 3
  slug: salesforce-rest-error
- name: QueryResult
  property_count: 4
  slug: salesforce-rest-query-result
- name: SObjectDescribe
  property_count: 11
  slug: salesforce-rest-s-object-describe
- name: SObjectRecord
  property_count: 2
  slug: salesforce-rest-s-object-record
- name: SearchResult
  property_count: 1
  slug: salesforce-rest-search-result
- name: ResultPage
  property_count: 1
  slug: salesforce-result-page
- name: Result
  property_count: 2
  slug: salesforce-result
- name: Result1
  property_count: 2
  slug: salesforce-result1
- name: Result2
  property_count: 21
  slug: salesforce-result2
- name: Result21
  property_count: 2
  slug: salesforce-result21
- name: result3
  property_count: 4
  slug: salesforce-result3
- name: result4
  property_count: 4
  slug: salesforce-result4
- name: result5
  property_count: 11
  slug: salesforce-result5
- name: Result6
  property_count: 11
  slug: salesforce-result6
- name: Results
  property_count: 1
  slug: salesforce-results
- name: Results1
  property_count: 2
  slug: salesforce-results1
- name: Results2
  property_count: 1
  slug: salesforce-results2
- name: Results3
  property_count: 1
  slug: salesforce-results3
- name: Results4
  property_count: 2
  slug: salesforce-results4
- name: Resultwithdefaultnav
  property_count: 4
  slug: salesforce-resultwithdefaultnav
- name: Resultwithpersonalizednav
  property_count: 4
  slug: salesforce-resultwithpersonalizednav
- name: RetailLocationGroup
  property_count: 1
  slug: salesforce-retail-location-group
- name: RetrieveOpenAPISchema
  property_count: 6
  slug: salesforce-retrieve-open-api-schema
- name: Retrieveable
  property_count: 1
  slug: salesforce-retrieveable
- name: Reward
  property_count: 14
  slug: salesforce-reward
- name: RichInput
  property_count: 4
  slug: salesforce-rich-input
- name: runDecisionMatrixRequest
  property_count: 1
  slug: salesforce-run-decision-matrix-request
- name: runDecisionMatrix
  property_count: 5
  slug: salesforce-run-decision-matrix
- name: runExpressionSetRequest
  property_count: 1
  slug: salesforce-run-expression-set-request
- name: RunSetting
  property_count: 1
  slug: salesforce-run-setting
- name: RunagenttestRequest
  property_count: 1
  slug: salesforce-runagenttest-request
- name: Runagenttest
  property_count: 2
  slug: salesforce-runagenttest
- name: SObjectCollectionsCreateRequest
  property_count: 2
  slug: salesforce-s-object-collections-create-request
- name: SObjectCollectionsUpdateRequest
  property_count: 2
  slug: salesforce-s-object-collections-update-request
- name: SObjectCollectionsUpdate
  property_count: 3
  slug: salesforce-s-object-collections-update
- name: SObjectCollectionsUpsertRequest
  property_count: 2
  slug: salesforce-s-object-collections-upsert-request
- name: SObjectCreateRequest
  property_count: 1
  slug: salesforce-s-object-create-request
- name: SObjectCreate
  property_count: 3
  slug: salesforce-s-object-create
- name: SObjectDescribe
  property_count: 45
  slug: salesforce-s-object-describe
- name: SObjectRootInfo
  property_count: 2
  slug: salesforce-s-object-root-info
- name: SObjectRowsUpdateRequest
  property_count: 1
  slug: salesforce-s-object-rows-update-request
- name: SObjectTreeRequest
  property_count: 1
  slug: salesforce-s-object-tree-request
- name: sObjects
  property_count: 4
  slug: salesforce-s-objects
- name: SObjects1
  property_count: 2
  slug: salesforce-s-objects1
- name: Salutation
  property_count: 2
  slug: salesforce-salutation
- name: Salutation1
  property_count: 31
  slug: salesforce-salutation1
- name: Salutation2
  property_count: 2
  slug: salesforce-salutation2
- name: Salutation4
  property_count: 5
  slug: salesforce-salutation4
- name: SampleLightningPage
  property_count: 3
  slug: salesforce-sample-lightning-page
- name: SaveResult
  property_count: 2
  slug: salesforce-save-result
- name: Schema
  property_count: 1
  slug: salesforce-schema
- name: Schema1
  property_count: 2
  slug: salesforce-schema1
- name: Schema10
  property_count: 1
  slug: salesforce-schema10
- name: Schemas
  property_count: 6
  slug: salesforce-schemas
- name: Scopes
  property_count: 17
  slug: salesforce-scopes
- name: Scopes1
  property_count: 1
  slug: salesforce-scopes1
- name: ScorecardAssociation
  property_count: 6
  slug: salesforce-scorecard-association
- name: ScorecardMetric
  property_count: 6
  slug: salesforce-scorecard-metric
- name: Scorecard
  property_count: 6
  slug: salesforce-scorecard
- name: ScratchOrgInfoHistory
  property_count: 6
  slug: salesforce-scratch-org-info-history
- name: ScratchOrgInfo
  property_count: 6
  slug: salesforce-scratch-org-info
- name: SearchPromotionRule
  property_count: 6
  slug: salesforce-search-promotion-rule
- name: SearchRecord
  property_count: 2
  slug: salesforce-search-record
- name: Searchable
  property_count: 1
  slug: salesforce-searchable
- name: Section
  property_count: 7
  slug: salesforce-section
- name: SectionUserStates
  property_count: 5
  slug: salesforce-section-user-states
- name: Section1
  property_count: 7
  slug: salesforce-section1
- name: Security
  property_count: 3
  slug: salesforce-security
- name: SecuritySchemes
  property_count: 3
  slug: salesforce-security-schemes
- name: SellerHistory
  property_count: 6
  slug: salesforce-seller-history
- name: Seller
  property_count: 6
  slug: salesforce-seller
- name: SenderEmail
  property_count: 31
  slug: salesforce-sender-email
- name: SenderName
  property_count: 31
  slug: salesforce-sender-name
- name: Sender
  property_count: 19
  slug: salesforce-sender
- name: Sender1
  property_count: 3
  slug: salesforce-sender1
- name: Server
  property_count: 1
  slug: salesforce-server
- name: SessionHeader
  property_count: 1
  slug: salesforce-session-header
- name: SessionHeader1
  property_count: 1
  slug: salesforce-session-header1
- name: SessionHeader4
  property_count: 1
  slug: salesforce-session-header4
- name: SessionHijackingEventStore
  property_count: 6
  slug: salesforce-session-hijacking-event-store
- name: Settings
  property_count: 3
  slug: salesforce-settings
- name: SetupAssistantStep
  property_count: 6
  slug: salesforce-setup-assistant-step
- name: Share
  property_count: 2
  slug: salesforce-share
- name: ShippingAddress
  property_count: 2
  slug: salesforce-shipping-address
- name: ShippingAddress1
  property_count: 8
  slug: salesforce-shipping-address1
- name: ShippingAddress11
  property_count: 8
  slug: salesforce-shipping-address11
- name: ShippingAddress12
  property_count: 8
  slug: salesforce-shipping-address12
- name: ShippingAddress2
  property_count: 31
  slug: salesforce-shipping-address2
- name: ShippingCity
  property_count: 2
  slug: salesforce-shipping-city
- name: ShippingCity1
  property_count: 31
  slug: salesforce-shipping-city1
- name: ShippingCity2
  property_count: 2
  slug: salesforce-shipping-city2
- name: ShippingCity4
  property_count: 2
  slug: salesforce-shipping-city4
- name: ShippingCountry
  property_count: 2
  slug: salesforce-shipping-country
- name: ShippingCountry1
  property_count: 31
  slug: salesforce-shipping-country1
- name: ShippingCountry2
  property_count: 2
  slug: salesforce-shipping-country2
- name: ShippingCountry4
  property_count: 2
  slug: salesforce-shipping-country4
- name: ShippingGeocodeAccuracy
  property_count: 2
  slug: salesforce-shipping-geocode-accuracy
- name: ShippingGeocodeAccuracy1
  property_count: 31
  slug: salesforce-shipping-geocode-accuracy1
- name: ShippingLatitude
  property_count: 2
  slug: salesforce-shipping-latitude
- name: ShippingLatitude1
  property_count: 31
  slug: salesforce-shipping-latitude1
- name: ShippingLongitude
  property_count: 2
  slug: salesforce-shipping-longitude
- name: ShippingLongitude1
  property_count: 31
  slug: salesforce-shipping-longitude1
- name: ShippingPostalCode
  property_count: 2
  slug: salesforce-shipping-postal-code
- name: ShippingPostalCode1
  property_count: 31
  slug: salesforce-shipping-postal-code1
- name: ShippingPostalCode2
  property_count: 2
  slug: salesforce-shipping-postal-code2
- name: ShippingPostalCode4
  property_count: 2
  slug: salesforce-shipping-postal-code4
- name: ShippingState
  property_count: 2
  slug: salesforce-shipping-state
- name: ShippingState1
  property_count: 31
  slug: salesforce-shipping-state1
- name: ShippingState2
  property_count: 2
  slug: salesforce-shipping-state2
- name: ShippingState4
  property_count: 2
  slug: salesforce-shipping-state4
- name: ShippingStreet
  property_count: 2
  slug: salesforce-shipping-street
- name: ShippingStreet1
  property_count: 31
  slug: salesforce-shipping-street1
- name: ShippingStreet2
  property_count: 2
  slug: salesforce-shipping-street2
- name: ShippingStreet4
  property_count: 2
  slug: salesforce-shipping-street4
- name: SICCodeC
  property_count: 31
  slug: salesforce-sic-code-c
- name: SICCodeC1
  property_count: 2
  slug: salesforce-sic-code-c1
- name: SicDesc
  property_count: 2
  slug: salesforce-sic-desc
- name: SicDesc1
  property_count: 31
  slug: salesforce-sic-desc1
- name: Sic
  property_count: 2
  slug: salesforce-sic
- name: Sic1
  property_count: 31
  slug: salesforce-sic1
- name: Sic2
  property_count: 2
  slug: salesforce-sic2
- name: Sic4
  property_count: 2
  slug: salesforce-sic4
- name: Signature
  property_count: 31
  slug: salesforce-signature
- name: SingleEmail
  property_count: 2
  slug: salesforce-single-email
- name: SiteHistory
  property_count: 6
  slug: salesforce-site-history
- name: Site
  property_count: 2
  slug: salesforce-site
- name: Site1
  property_count: 31
  slug: salesforce-site1
- name: Site2
  property_count: 2
  slug: salesforce-site2
- name: SLAExpirationDateC
  property_count: 2
  slug: salesforce-sla-expiration-date-c
- name: SLAExpirationDateC1
  property_count: 31
  slug: salesforce-sla-expiration-date-c1
- name: SLAExpirationDateC2
  property_count: 2
  slug: salesforce-sla-expiration-date-c2
- name: SLAExpirationDateC4
  property_count: 2
  slug: salesforce-sla-expiration-date-c4
- name: SLASerialNumberC
  property_count: 1
  slug: salesforce-sla-serial-number-c
- name: SLASerialNumberC1
  property_count: 31
  slug: salesforce-sla-serial-number-c1
- name: SLASerialNumberC2
  property_count: 2
  slug: salesforce-sla-serial-number-c2
- name: SLASerialNumberC4
  property_count: 2
  slug: salesforce-sla-serial-number-c4
- name: SLAC
  property_count: 1
  slug: salesforce-slac
- name: SLAC1
  property_count: 31
  slug: salesforce-slac1
- name: SLAC2
  property_count: 2
  slug: salesforce-slac2
- name: SLAC4
  property_count: 2
  slug: salesforce-slac4
- name: SmallBannerPhotoUrl
  property_count: 31
  slug: salesforce-small-banner-photo-url
- name: SmallPhotoUrl
  property_count: 31
  slug: salesforce-small-photo-url
- name: Salesforce SObject Record
  property_count: 18
  slug: salesforce-sobject
- name: SobjectsContact
  property_count: 3
  slug: salesforce-sobjects-contact
- name: Sobjects2
  property_count: 28
  slug: salesforce-sobjects2
- name: SolutionHistory
  property_count: 6
  slug: salesforce-solution-history
- name: StageName
  property_count: 1
  slug: salesforce-stage-name
- name: State
  property_count: 31
  slug: salesforce-state
- name: State2
  property_count: 2
  slug: salesforce-state2
- name: StaticResource
  property_count: 6
  slug: salesforce-static-resource
- name: StatusCode
  property_count: 1
  slug: salesforce-status-code
- name: Status
  property_count: 2
  slug: salesforce-status
- name: Status1
  property_count: 2
  slug: salesforce-status1
- name: Status200-RecordFound
  property_count: 6
  slug: salesforce-status200-record-found
- name: Status200-Success
  property_count: 4
  slug: salesforce-status200-success
- name: Status200-Success2
  property_count: 3
  slug: salesforce-status200-success2
- name: Status200-Successfull
  property_count: 5
  slug: salesforce-status200-successfull
- name: Status200-SuccessfullyUpdated
  property_count: 6
  slug: salesforce-status200-successfully-updated
- name: Status200-UpdateCommitmentDatabaseFailure
  property_count: 2
  slug: salesforce-status200-update-commitment-database-failure
- name: Status200-UpdateCommitmentRequestValidationFailure
  property_count: 2
  slug: salesforce-status200-update-commitment-request-validation-failure
- name: Status200-UpdateCommitmentRequestValidationFailure1
  property_count: 4
  slug: salesforce-status200-update-commitment-request-validation-failure1
- name: Status200-UpdateCommitmentSuccess
  property_count: 2
  slug: salesforce-status200-update-commitment-success
- name: Status200-UpdateCommitmentSuccessWithExternalIds
  property_count: 2
  slug: salesforce-status200-update-commitment-success-with-external-ids
- name: Status201-AcceptedButWarning
  property_count: 1
  slug: salesforce-status201-accepted-but-warning
- name: Status201-BadRequest
  property_count: 3
  slug: salesforce-status201-bad-request
- name: Status201-CreateCommitmentRequestValidationFailure
  property_count: 4
  slug: salesforce-status201-create-commitment-request-validation-failure
- name: Status201-CreateCommitmentSuccess
  property_count: 4
  slug: salesforce-status201-create-commitment-success
- name: Status201-CreateCommitmentSuccessWithExternalIds
  property_count: 4
  slug: salesforce-status201-create-commitment-success-with-external-ids
- name: Status201-CreateCommitmentSuccessWithExternalIds1
  property_count: 4
  slug: salesforce-status201-create-commitment-success-with-external-ids1
- name: Status201-CreateCommitmentSuccess1
  property_count: 4
  slug: salesforce-status201-create-commitment-success1
- name: Status201-CreateGiftRequestValidationFailure
  property_count: 4
  slug: salesforce-status201-create-gift-request-validation-failure
- name: Status201-CreateGiftSuccess
  property_count: 4
  slug: salesforce-status201-create-gift-success
- name: Status201-CreateGiftSuccessWithExternalIds
  property_count: 4
  slug: salesforce-status201-create-gift-success-with-external-ids
- name: Status201-Error
  property_count: 1
  slug: salesforce-status201-error
- name: Status201-KeyPairNotFound
  property_count: 1
  slug: salesforce-status201-key-pair-not-found
- name: Status201-SuccessCreatedOnlyMandatoryFields
  property_count: 6
  slug: salesforce-status201-success-created-only-mandatory-fields
- name: Status201-Success
  property_count: 3
  slug: salesforce-status201-success
- name: Status201-Success1
  property_count: 1
  slug: salesforce-status201-success1
- name: Status201-Success2
  property_count: 1
  slug: salesforce-status201-success2
- name: Status201-Success3
  property_count: 3
  slug: salesforce-status201-success3
- name: Status201-Success4
  property_count: 4
  slug: salesforce-status201-success4
- name: Status201-Success5
  property_count: 5
  slug: salesforce-status201-success5
- name: Status201-UpdateCommitmentExternalIds
  property_count: 4
  slug: salesforce-status201-update-commitment-external-ids
- name: Status201-UpdateCommitmentSuccess
  property_count: 4
  slug: salesforce-status201-update-commitment-success
- name: Status201-UpdateTransactionPaymentRequestValidationFailed
  property_count: 4
  slug: salesforce-status201-update-transaction-payment-request-validation-failed
- name: Status201-UpdateTransactionPaymentSuccess
  property_count: 4
  slug: salesforce-status201-update-transaction-payment-success
- name: Status201-UpdateTransactionPaymentWithExternalIds1
  property_count: 4
  slug: salesforce-status201-update-transaction-payment-with-external-ids1
- name: Status400-ActiveExpressionCanNotBeDeleted1
  property_count: 2
  slug: salesforce-status400-active-expression-can-not-be-deleted1
- name: Status400-BadRequest1
  property_count: 2
  slug: salesforce-status400-bad-request1
- name: Status400-Duplicate1
  property_count: 2
  slug: salesforce-status400-duplicate1
- name: Status400-EmptyExpressionSetAPIName1
  property_count: 5
  slug: salesforce-status400-empty-expression-set-api-name1
- name: Status400-ErrorInvalidInput1
  property_count: 2
  slug: salesforce-status400-error-invalid-input1
- name: Status400-ExpressionNotFound1
  property_count: 5
  slug: salesforce-status400-expression-not-found1
- name: Status400-InstanceNotFound1
  property_count: 2
  slug: salesforce-status400-instance-not-found1
- name: Status400-InvalidBody1
  property_count: 2
  slug: salesforce-status400-invalid-body1
- name: Status400-InvalidEnum1
  property_count: 2
  slug: salesforce-status400-invalid-enum1
- name: Status400-InvalidExpressionSetName1
  property_count: 2
  slug: salesforce-status400-invalid-expression-set-name1
- name: Status400-InvalidIdentifierOfVersion1
  property_count: 2
  slug: salesforce-status400-invalid-identifier-of-version1
- name: Status400-InvalidOperation1
  property_count: 2
  slug: salesforce-status400-invalid-operation1
- name: Status400-MatrixNotFound1
  property_count: 2
  slug: salesforce-status400-matrix-not-found1
- name: Status400-MissingMandatoryBodyField1
  property_count: 2
  slug: salesforce-status400-missing-mandatory-body-field1
- name: Status400-PreviouslyDeletedRecord1
  property_count: 2
  slug: salesforce-status400-previously-deleted-record1
- name: Status400-TryToDeletePreviouslyDeleted1
  property_count: 2
  slug: salesforce-status400-try-to-delete-previously-deleted1
- name: Status400-UnknownException1
  property_count: 2
  slug: salesforce-status400-unknown-exception1
- name: Status400-UnrecognizedBodyField1
  property_count: 2
  slug: salesforce-status400-unrecognized-body-field1
- name: Status401-Unauthorized1
  property_count: 2
  slug: salesforce-status401-unauthorized1
- name: Status404-NotFound1
  property_count: 2
  slug: salesforce-status404-not-found1
- name: Status404-RecordNotFound1
  property_count: 2
  slug: salesforce-status404-record-not-found1
- name: Status500-EmptyBodyButRecordExist1
  property_count: 2
  slug: salesforce-status500-empty-body-but-record-exist1
- name: Status500-EmptyBody1
  property_count: 2
  slug: salesforce-status500-empty-body1
- name: Status500-ErrorNoBody1
  property_count: 2
  slug: salesforce-status500-error-no-body1
- name: Status500-UnexpectedError1
  property_count: 2
  slug: salesforce-status500-unexpected-error1
- name: Status500-UnknownException1
  property_count: 2
  slug: salesforce-status500-unknown-exception1
- name: Status8
  property_count: 31
  slug: salesforce-status8
- name: Status9
  property_count: 2
  slug: salesforce-status9
- name: StayInTouchNote
  property_count: 31
  slug: salesforce-stay-in-touch-note
- name: StayInTouchSignature
  property_count: 31
  slug: salesforce-stay-in-touch-signature
- name: StayInTouchSubject
  property_count: 31
  slug: salesforce-stay-in-touch-subject
- name: Step
  property_count: 10
  slug: salesforce-step
- name: Store
  property_count: 1
  slug: salesforce-store
- name: StreamingApiConcurrentClients
  property_count: 2
  slug: salesforce-streaming-api-concurrent-clients
- name: StreamingChannel
  property_count: 6
  slug: salesforce-streaming-channel
- name: Street
  property_count: 31
  slug: salesforce-street
- name: Street2
  property_count: 2
  slug: salesforce-street2
- name: Street3
  property_count: 2
  slug: salesforce-street3
- name: Subject
  property_count: 7
  slug: salesforce-subject
- name: Subscriber
  property_count: 19
  slug: salesforce-subscriber
- name: SuccesfulUserPhoto
  property_count: 7
  slug: salesforce-succesful-user-photo
- name: Success
  property_count: 1
  slug: salesforce-success
- name: Success1
  property_count: 6
  slug: salesforce-success1
- name: SuccessfulAssetTokenFlow
  property_count: 4
  slug: salesforce-successful-asset-token-flow
- name: SuccessfulAuthenticationConfigurationEndpoint
  property_count: 9
  slug: salesforce-successful-authentication-configuration-endpoint
- name: SuccessfulBulkCloseJob
  property_count: 24
  slug: salesforce-successful-bulk-close-job
- name: SuccessfulBulkCreateJob
  property_count: 24
  slug: salesforce-successful-bulk-create-job
- name: SuccessfulClientCredentialsFlow-basicauthorizationheader
  property_count: 8
  slug: salesforce-successful-client-credentials-flow-basicauthorizationheader
- name: SuccessfulClientCredentialsFlow
  property_count: 8
  slug: salesforce-successful-client-credentials-flow
- name: SuccessfulCloseorAbortaJob
  property_count: 10
  slug: salesforce-successful-closeor-aborta-job
- name: SuccessfulComment-Edit
  property_count: 18
  slug: salesforce-successful-comment-edit
- name: SuccessfulComment
  property_count: 18
  slug: salesforce-successful-comment
- name: SuccessfulCompositeGraph
  property_count: 1
  slug: salesforce-successful-composite-graph
- name: SuccessfulComposite
  property_count: 1
  slug: salesforce-successful-composite
- name: successfulCreateCredential
  property_count: 6
  slug: salesforce-successful-create-credential
- name: SuccessfulCreateExternalCredential
  property_count: 10
  slug: salesforce-successful-create-external-credential
- name: SuccessfulCreateNamedCredential
  property_count: 10
  slug: salesforce-successful-create-named-credential
- name: SuccessfulCreatejobQueryRequest
  property_count: 5
  slug: salesforce-successful-createjob-query-request
- name: SuccessfulCreatejobQuery
  property_count: 12
  slug: salesforce-successful-createjob-query
- name: SuccessfulCreatejob
  property_count: 13
  slug: salesforce-successful-createjob
- name: SuccessfulDeviceFlow2
  property_count: 9
  slug: salesforce-successful-device-flow2
- name: SuccessfulFeedElementsBatchPost
  property_count: 2
  slug: salesforce-successful-feed-elements-batch-post
- name: SuccessfulFeedElementsPostandSearch
  property_count: 21
  slug: salesforce-successful-feed-elements-postand-search
- name: SuccessfulFeedElementsPostandSearch1
  property_count: 21
  slug: salesforce-successful-feed-elements-postand-search1
- name: SuccessfulFileShares
  property_count: 5
  slug: salesforce-successful-file-shares
- name: SuccessfulFilesSharesLink
  property_count: 5
  slug: salesforce-successful-files-shares-link
- name: SuccessfulFollowing-POST
  property_count: 5
  slug: salesforce-successful-following-post
- name: SuccessfulFollowing
  property_count: 5
  slug: salesforce-successful-following
- name: SuccessfulGetAllQueryJobs
  property_count: 3
  slug: salesforce-successful-get-all-query-jobs
- name: SuccessfulGetCredential
  property_count: 7
  slug: salesforce-successful-get-credential
- name: SuccessfulGetExternalCredentialsbyDeveloperName
  property_count: 11
  slug: salesforce-successful-get-external-credentialsby-developer-name
- name: SuccessfulGetJobInfoQuery
  property_count: 15
  slug: salesforce-successful-get-job-info-query
- name: SuccessfulGetJobInfoQuery1
  property_count: 16
  slug: salesforce-successful-get-job-info-query1
- name: SuccessfulGetJobInfo
  property_count: 19
  slug: salesforce-successful-get-job-info
- name: SuccessfulGetNamedCredentialbyDeveloperName
  property_count: 10
  slug: salesforce-successful-get-named-credentialby-developer-name
- name: SuccessfulGroupMembersPrivate
  property_count: 2
  slug: salesforce-successful-group-members-private
- name: SuccessfulGroupMembers
  property_count: 5
  slug: salesforce-successful-group-members
- name: SuccessfulGroupMembershipRequestsPrivate
  property_count: 8
  slug: salesforce-successful-group-membership-requests-private
- name: SuccessfulIDToken
  property_count: 30
  slug: salesforce-successful-id-token
- name: SuccessfulJWTBearerTokenFlow
  property_count: 5
  slug: salesforce-successful-jwt-bearer-token-flow
- name: SuccessfulListExternalCredentials
  property_count: 1
  slug: salesforce-successful-list-external-credentials
- name: SuccessfulListNamedCredentials
  property_count: 1
  slug: salesforce-successful-list-named-credentials
- name: SuccessfulListofGroups-POST
  property_count: 25
  slug: salesforce-successful-listof-groups-post
- name: SuccessfulListofGroups
  property_count: 4
  slug: salesforce-successful-listof-groups
- name: SuccessfulNewsFeedElements
  property_count: 9
  slug: salesforce-successful-news-feed-elements
- name: SuccessfulOAuthUsernamePasswordLogin
  property_count: 6
  slug: salesforce-successful-o-auth-username-password-login
- name: SuccessfulOpenIDConnectDiscoveryEndpoint
  property_count: 18
  slug: salesforce-successful-open-id-connect-discovery-endpoint
- name: SuccessfulRecordFeedElements
  property_count: 9
  slug: salesforce-successful-record-feed-elements
- name: SuccessfulRefreshToken
  property_count: 8
  slug: salesforce-successful-refresh-token
- name: SuccessfulSObjectCollectionsCreate
  property_count: 3
  slug: salesforce-successful-s-object-collections-create
- name: SuccessfulSObjectCollectionsDelete
  property_count: 3
  slug: salesforce-successful-s-object-collections-delete
- name: SuccessfulSObjectCollectionsRetrieve
  property_count: 3
  slug: salesforce-successful-s-object-collections-retrieve
- name: SuccessfulSObjectCollectionsUpsert
  property_count: 4
  slug: salesforce-successful-s-object-collections-upsert
- name: SuccessfulSObjectTree
  property_count: 2
  slug: salesforce-successful-s-object-tree
- name: SuccessfulSalesforceKeys
  property_count: 1
  slug: salesforce-successful-salesforce-keys
- name: SuccessfulUpdateExternalCredential
  property_count: 10
  slug: salesforce-successful-update-external-credential
- name: SuccessfulUpdateNamedCredential
  property_count: 10
  slug: salesforce-successful-update-named-credential
- name: SuccessfulUserInfo
  property_count: 24
  slug: salesforce-successful-user-info
- name: SuccessfulUserMessagesGeneral
  property_count: 9
  slug: salesforce-successful-user-messages-general
- name: SuccessfulUserProfileFeedElements
  property_count: 9
  slug: salesforce-successful-user-profile-feed-elements
- name: SuccessfulUsersFilesGeneral
  property_count: 49
  slug: salesforce-successful-users-files-general
- name: SuccessfulWebServerFlow2
  property_count: 9
  slug: salesforce-successful-web-server-flow2
- name: SuccessfullGetAllJobs
  property_count: 3
  slug: salesforce-successfull-get-all-jobs
- name: SupportedScope
  property_count: 2
  slug: salesforce-supported-scope
- name: SymbolTable
  property_count: 13
  slug: salesforce-symbol-table
- name: SystemModstamp
  property_count: 2
  slug: salesforce-system-modstamp
- name: SystemModstamp10
  property_count: 2
  slug: salesforce-system-modstamp10
- name: SystemModstamp2
  property_count: 31
  slug: salesforce-system-modstamp2
- name: Tab
  property_count: 9
  slug: salesforce-tab
- name: TableDeclaration
  property_count: 6
  slug: salesforce-table-declaration
- name: TestCase
  property_count: 7
  slug: salesforce-test-case
- name: TestCredential
  property_count: 2
  slug: salesforce-test-credential
- name: TestResult
  property_count: 11
  slug: salesforce-test-result
- name: ThemeInfo
  property_count: 2
  slug: salesforce-theme-info
- name: ThemeItem
  property_count: 3
  slug: salesforce-theme-item
- name: Themes
  property_count: 1
  slug: salesforce-themes
- name: ThreatDetectionFeedback
  property_count: 6
  slug: salesforce-threat-detection-feedback
- name: TickerSymbol
  property_count: 2
  slug: salesforce-ticker-symbol
- name: TickerSymbol1
  property_count: 31
  slug: salesforce-ticker-symbol1
- name: TickerSymbol2
  property_count: 2
  slug: salesforce-ticker-symbol2
- name: TierGroup
  property_count: 2
  slug: salesforce-tier-group
- name: Tier
  property_count: 2
  slug: salesforce-tier
- name: TimeZoneSidKey
  property_count: 31
  slug: salesforce-time-zone-sid-key
- name: Title
  property_count: 2
  slug: salesforce-title
- name: Title1
  property_count: 31
  slug: salesforce-title1
- name: Title4
  property_count: 2
  slug: salesforce-title4
- name: ToolingExecuteAnonymous
  property_count: 7
  slug: salesforce-tooling-execute-anonymous
- name: ToolingQuery
  property_count: 6
  slug: salesforce-tooling-query
- name: ToolingRunTestsSync
  property_count: 10
  slug: salesforce-tooling-run-tests-sync
- name: ToolingSearch
  property_count: 1
  slug: salesforce-tooling-search
- name: TopicAssignment
  property_count: 6
  slug: salesforce-topic-assignment
- name: Topic
  property_count: 6
  slug: salesforce-topic
- name: Topics
  property_count: 3
  slug: salesforce-topics
- name: Topics2
  property_count: 2
  slug: salesforce-topics2
- name: Tradestyle
  property_count: 2
  slug: salesforce-tradestyle
- name: Tradestyle1
  property_count: 31
  slug: salesforce-tradestyle1
- name: TransactionHistoryRequest
  property_count: 5
  slug: salesforce-transaction-history-request
- name: TransactionHistory
  property_count: 4
  slug: salesforce-transaction-history
- name: TransactionJournal
  property_count: 8
  slug: salesforce-transaction-journal
- name: TransactionJournal2
  property_count: 7
  slug: salesforce-transaction-journal2
- name: TransactionJournal3
  property_count: 6
  slug: salesforce-transaction-journal3
- name: TransactionJournal4
  property_count: 17
  slug: salesforce-transaction-journal4
- name: TransactionJournal5
  property_count: 8
  slug: salesforce-transaction-journal5
- name: TransactionJournalsExecutionRequest
  property_count: 1
  slug: salesforce-transaction-journals-execution-request
- name: TransactionJournalsSimulationRequest
  property_count: 2
  slug: salesforce-transaction-journals-simulation-request
- name: TransactionLedgerSummary
  property_count: 4
  slug: salesforce-transaction-ledger-summary
- name: Translation
  property_count: 6
  slug: salesforce-translation
- name: Triggerable
  property_count: 1
  slug: salesforce-triggerable
- name: Type
  property_count: 4
  slug: salesforce-type
- name: Type1
  property_count: 4
  slug: salesforce-type1
- name: Type10
  property_count: 2
  slug: salesforce-type10
- name: Type11
  property_count: 4
  slug: salesforce-type11
- name: Type12
  property_count: 4
  slug: salesforce-type12
- name: Type13
  property_count: 2
  slug: salesforce-type13
- name: Type4
  property_count: 2
  slug: salesforce-type4
- name: Type5
  property_count: 1
  slug: salesforce-type5
- name: Type7
  property_count: 31
  slug: salesforce-type7
- name: ErrorResponse
  property_count: 2
  slug: salesforce-ui-error-response
- name: FieldRepresentation
  property_count: 8
  slug: salesforce-ui-field-representation
- name: FieldValueRepresentation
  property_count: 2
  slug: salesforce-ui-field-value-representation
- name: ListViewCollection
  property_count: 5
  slug: salesforce-ui-list-view-collection
- name: ListViewResult
  property_count: 4
  slug: salesforce-ui-list-view-result
- name: ListViewSummary
  property_count: 4
  slug: salesforce-ui-list-view-summary
- name: LookupRecordsCollection
  property_count: 2
  slug: salesforce-ui-lookup-records-collection
- name: ObjectInfoRepresentation
  property_count: 11
  slug: salesforce-ui-object-info-representation
- name: PicklistValue
  property_count: 4
  slug: salesforce-ui-picklist-value
- name: PicklistValuesCollection
  property_count: 1
  slug: salesforce-ui-picklist-values-collection
- name: RecordInput
  property_count: 2
  slug: salesforce-ui-record-input
- name: RecordRepresentation
  property_count: 12
  slug: salesforce-ui-record-representation
- name: Uiapi
  property_count: 1
  slug: salesforce-uiapi
- name: Uiapi10
  property_count: 1
  slug: salesforce-uiapi10
- name: Uiapi11
  property_count: 1
  slug: salesforce-uiapi11
- name: Uiapi12
  property_count: 1
  slug: salesforce-uiapi12
- name: Uiapi13
  property_count: 1
  slug: salesforce-uiapi13
- name: Uiapi3
  property_count: 1
  slug: salesforce-uiapi3
- name: Uiapi4
  property_count: 1
  slug: salesforce-uiapi4
- name: Uiapi6
  property_count: 1
  slug: salesforce-uiapi6
- name: Uiapi7
  property_count: 1
  slug: salesforce-uiapi7
- name: Undeletable
  property_count: 1
  slug: salesforce-undeletable
- name: undelete
  property_count: 1
  slug: salesforce-undelete
- name: UnenrollaMemberRequest
  property_count: 1
  slug: salesforce-unenrolla-member-request
- name: UpDownVote
  property_count: 3
  slug: salesforce-up-down-vote
- name: UpateAccountSuccess
  property_count: 2
  slug: salesforce-upate-account-success
- name: UpdateCommitmentPaymentsRequest
  property_count: 1
  slug: salesforce-update-commitment-payments-request
- name: UpdateCommitmentsRequest
  property_count: 12
  slug: salesforce-update-commitments-request
- name: UpdateCredentialRequest
  property_count: 5
  slug: salesforce-update-credential-request
- name: UpdateExternalCredentialRequest
  property_count: 4
  slug: salesforce-update-external-credential-request
- name: UpdateGiftTransactionPaymentsRequest
  property_count: 1
  slug: salesforce-update-gift-transaction-payments-request
- name: UpdateLastSelectedApp
  property_count: 18
  slug: salesforce-update-last-selected-app
- name: UpdateMemberDetailsRequest
  property_count: 1
  slug: salesforce-update-member-details-request
- name: UpdateMemberTierRequest
  property_count: 1
  slug: salesforce-update-member-tier-request
- name: UpdateNamedCredentialRequest
  property_count: 6
  slug: salesforce-update-named-credential-request
- name: Update
  property_count: 10
  slug: salesforce-update
- name: UpdateTableRequest
  property_count: 12
  slug: salesforce-update-table-request
- name: UpdateUsageofaFavorite
  property_count: 11
  slug: salesforce-update-usageofa-favorite
- name: Update1
  property_count: 2
  slug: salesforce-update1
- name: UpdateaBatchofFavoritesRequest
  property_count: 1
  slug: salesforce-updatea-batchof-favorites-request
- name: UpdateaBatchofFavorites
  property_count: 1
  slug: salesforce-updatea-batchof-favorites
- name: UpdateaFavoriteRequest
  property_count: 2
  slug: salesforce-updatea-favorite-request
- name: UpdateaFavorite
  property_count: 11
  slug: salesforce-updatea-favorite
- name: UpdateaRecordRequest
  property_count: 2
  slug: salesforce-updatea-record-request
- name: UpdateaRecord
  property_count: 11
  slug: salesforce-updatea-record
- name: Updateable
  property_count: 1
  slug: salesforce-updateable
- name: UpdatechannelRequest
  property_count: 2
  slug: salesforce-updatechannel-request
- name: UpdateeventrelayRequest
  property_count: 2
  slug: salesforce-updateeventrelay-request
- name: UpdatemanagedeventsubscriptionRequest
  property_count: 2
  slug: salesforce-updatemanagedeventsubscription-request
- name: UpdatenamedcredentialRequest1
  property_count: 2
  slug: salesforce-updatenamedcredential-request1
- name: UpsellOpportunityC
  property_count: 1
  slug: salesforce-upsell-opportunity-c
- name: UpsellOpportunityC1
  property_count: 31
  slug: salesforce-upsell-opportunity-c1
- name: UpsellOpportunityC2
  property_count: 2
  slug: salesforce-upsell-opportunity-c2
- name: UpsellOpportunityC4
  property_count: 2
  slug: salesforce-upsell-opportunity-c4
- name: Url
  property_count: 1
  slug: salesforce-url
- name: Urls
  property_count: 17
  slug: salesforce-urls
- name: Urls2
  property_count: 3
  slug: salesforce-urls2
- name: Urls3
  property_count: 1
  slug: salesforce-urls3
- name: Urls4
  property_count: 11
  slug: salesforce-urls4
- name: Urls5
  property_count: 2
  slug: salesforce-urls5
- name: Urls7
  property_count: 5
  slug: salesforce-urls7
- name: Urls8
  property_count: 8
  slug: salesforce-urls8
- name: UserPermissionsCallCenterAutoLogin
  property_count: 31
  slug: salesforce-user-permissions-call-center-auto-login
- name: UserPermissionsInteractionUser
  property_count: 31
  slug: salesforce-user-permissions-interaction-user
- name: UserPermissionsJigsawProspectingUser
  property_count: 31
  slug: salesforce-user-permissions-jigsaw-prospecting-user
- name: UserPermissionsKnowledgeUser
  property_count: 31
  slug: salesforce-user-permissions-knowledge-user
- name: UserPermissionsMarketingUser
  property_count: 31
  slug: salesforce-user-permissions-marketing-user
- name: UserPermissionsOfflineUser
  property_count: 31
  slug: salesforce-user-permissions-offline-user
- name: UserPermissionsSFContentUser
  property_count: 31
  slug: salesforce-user-permissions-sf-content-user
- name: UserPermissionsSiteforceContributorUser
  property_count: 31
  slug: salesforce-user-permissions-siteforce-contributor-user
- name: UserPermissionsSiteforcePublisherUser
  property_count: 31
  slug: salesforce-user-permissions-siteforce-publisher-user
- name: UserPermissionsSupportUser
  property_count: 31
  slug: salesforce-user-permissions-support-user
- name: UserPermissionsWorkDotComUserFeature
  property_count: 31
  slug: salesforce-user-permissions-work-dot-com-user-feature
- name: UserPreferencesActivityRemindersPopup
  property_count: 31
  slug: salesforce-user-preferences-activity-reminders-popup
- name: UserPreferencesApexPagesDeveloperMode
  property_count: 31
  slug: salesforce-user-preferences-apex-pages-developer-mode
- name: UserPreferencesCacheDiagnostics
  property_count: 31
  slug: salesforce-user-preferences-cache-diagnostics
- name: UserPreferencesContentEmailAsAndWhen
  property_count: 31
  slug: salesforce-user-preferences-content-email-as-and-when
- name: UserPreferencesContentNoEmail
  property_count: 31
  slug: salesforce-user-preferences-content-no-email
- name: UserPreferencesCreateLEXAppsWTShown
  property_count: 31
  slug: salesforce-user-preferences-create-lex-apps-wt-shown
- name: UserPreferencesDedupeStorageMigrationComplete
  property_count: 31
  slug: salesforce-user-preferences-dedupe-storage-migration-complete
- name: UserPreferencesDisCommentAfterLikeEmail
  property_count: 31
  slug: salesforce-user-preferences-dis-comment-after-like-email
- name: UserPreferencesDisMentionsCommentEmail
  property_count: 31
  slug: salesforce-user-preferences-dis-mentions-comment-email
- name: UserPreferencesDisProfPostCommentEmail
  property_count: 31
  slug: salesforce-user-preferences-dis-prof-post-comment-email
- name: UserPreferencesDisableAllFeedsEmail
  property_count: 31
  slug: salesforce-user-preferences-disable-all-feeds-email
- name: UserPreferencesDisableBookmarkEmail
  property_count: 31
  slug: salesforce-user-preferences-disable-bookmark-email
- name: UserPreferencesDisableChangeCommentEmail
  property_count: 31
  slug: salesforce-user-preferences-disable-change-comment-email
- name: UserPreferencesDisableEndorsementEmail
  property_count: 31
  slug: salesforce-user-preferences-disable-endorsement-email
- name: UserPreferencesDisableFileShareNotificationsForApi
  property_count: 31
  slug: salesforce-user-preferences-disable-file-share-notifications-for-api
- name: UserPreferencesDisableFollowersEmail
  property_count: 31
  slug: salesforce-user-preferences-disable-followers-email
- name: UserPreferencesDisableLaterCommentEmail
  property_count: 31
  slug: salesforce-user-preferences-disable-later-comment-email
- name: UserPreferencesDisableLikeEmail
  property_count: 31
  slug: salesforce-user-preferences-disable-like-email
- name: UserPreferencesDisableMentionsPostEmail
  property_count: 31
  slug: salesforce-user-preferences-disable-mentions-post-email
- name: UserPreferencesDisableMessageEmail
  property_count: 31
  slug: salesforce-user-preferences-disable-message-email
- name: UserPreferencesDisableProfilePostEmail
  property_count: 31
  slug: salesforce-user-preferences-disable-profile-post-email
- name: UserPreferencesDisableSharePostEmail
  property_count: 31
  slug: salesforce-user-preferences-disable-share-post-email
- name: UserPreferencesEnableAutoSubForFeeds
  property_count: 31
  slug: salesforce-user-preferences-enable-auto-sub-for-feeds
- name: UserPreferencesEventRemindersCheckboxDefault
  property_count: 31
  slug: salesforce-user-preferences-event-reminders-checkbox-default
- name: UserPreferencesExcludeMailAppAttachments
  property_count: 31
  slug: salesforce-user-preferences-exclude-mail-app-attachments
- name: UserPreferencesFavoritesShowTopFavorites
  property_count: 31
  slug: salesforce-user-preferences-favorites-show-top-favorites
- name: UserPreferencesFavoritesWTShown
  property_count: 31
  slug: salesforce-user-preferences-favorites-wt-shown
- name: UserPreferencesFirstTimeInLightning
  property_count: 31
  slug: salesforce-user-preferences-first-time-in-lightning
- name: UserPreferencesGlobalNavBarWTShown
  property_count: 31
  slug: salesforce-user-preferences-global-nav-bar-wt-shown
- name: UserPreferencesGlobalNavGridMenuWTShown
  property_count: 31
  slug: salesforce-user-preferences-global-nav-grid-menu-wt-shown
- name: UserPreferencesHasCelebrationBadge
  property_count: 31
  slug: salesforce-user-preferences-has-celebration-badge
- name: UserPreferencesHasSentWarningEmail
  property_count: 31
  slug: salesforce-user-preferences-has-sent-warning-email
- name: UserPreferencesHeavyPagePromptEnabled
  property_count: 31
  slug: salesforce-user-preferences-heavy-page-prompt-enabled
- name: UserPreferencesHideBiggerPhotoCallout
  property_count: 31
  slug: salesforce-user-preferences-hide-bigger-photo-callout
- name: UserPreferencesHideChatterOnboardingSplash
  property_count: 31
  slug: salesforce-user-preferences-hide-chatter-onboarding-splash
- name: UserPreferencesHideCSNDesktopTask
  property_count: 31
  slug: salesforce-user-preferences-hide-csn-desktop-task
- name: UserPreferencesHideCSNGetChatterMobileTask
  property_count: 31
  slug: salesforce-user-preferences-hide-csn-get-chatter-mobile-task
- name: UserPreferencesHideEndUserOnboardingAssistantModal
  property_count: 31
  slug: salesforce-user-preferences-hide-end-user-onboarding-assistant-modal
- name: UserPreferencesHideEventCalendar
  property_count: 31
  slug: salesforce-user-preferences-hide-event-calendar
- name: UserPreferencesHideLearningPathModal
  property_count: 31
  slug: salesforce-user-preferences-hide-learning-path-modal
- name: UserPreferencesHideLightningMigrationModal
  property_count: 31
  slug: salesforce-user-preferences-hide-lightning-migration-modal
- name: UserPreferencesHideMailAppEAPUserGuidance
  property_count: 31
  slug: salesforce-user-preferences-hide-mail-app-eap-user-guidance
- name: UserPreferencesHideMailAppWelcomeMat
  property_count: 31
  slug: salesforce-user-preferences-hide-mail-app-welcome-mat
- name: UserPreferencesHideS1BrowserUI
  property_count: 31
  slug: salesforce-user-preferences-hide-s1-browser-ui
- name: UserPreferencesHideSecondChatterOnboardingSplash
  property_count: 31
  slug: salesforce-user-preferences-hide-second-chatter-onboarding-splash
- name: UserPreferencesHideSfxWelcomeMat
  property_count: 31
  slug: salesforce-user-preferences-hide-sfx-welcome-mat
- name: UserPreferencesHideTaskListViewsPopover
  property_count: 31
  slug: salesforce-user-preferences-hide-task-list-views-popover
- name: UserPreferencesHideTrialsCelebration
  property_count: 31
  slug: salesforce-user-preferences-hide-trials-celebration
- name: UserPreferencesHideTrialsWelcomeMat
  property_count: 31
  slug: salesforce-user-preferences-hide-trials-welcome-mat
- name: UserPreferencesJigsawListUser
  property_count: 31
  slug: salesforce-user-preferences-jigsaw-list-user
- name: UserPreferencesLightningExperiencePreferred
  property_count: 31
  slug: salesforce-user-preferences-lightning-experience-preferred
- name: UserPreferencesLtngPromoReserved10UserPref
  property_count: 31
  slug: salesforce-user-preferences-ltng-promo-reserved10-user-pref
- name: UserPreferencesLtngPromoReserved16UserPref
  property_count: 31
  slug: salesforce-user-preferences-ltng-promo-reserved16-user-pref
- name: UserPreferencesLtngPromoReserved19UserPref
  property_count: 31
  slug: salesforce-user-preferences-ltng-promo-reserved19-user-pref
- name: UserPreferencesNativeEmailClient
  property_count: 31
  slug: salesforce-user-preferences-native-email-client
- name: UserPreferencesNewLightningReportRunPageEnabled
  property_count: 31
  slug: salesforce-user-preferences-new-lightning-report-run-page-enabled
- name: UserPreferencesPathAssistantCollapsed
  property_count: 31
  slug: salesforce-user-preferences-path-assistant-collapsed
- name: UserPreferencesPreviewCustomTheme
  property_count: 31
  slug: salesforce-user-preferences-preview-custom-theme
- name: UserPreferencesPreviewLightning
  property_count: 31
  slug: salesforce-user-preferences-preview-lightning
- name: UserPreferencesReadReceiptLastToggleValue
  property_count: 31
  slug: salesforce-user-preferences-read-receipt-last-toggle-value
- name: UserPreferencesReceiveNoNotificationsAsApprover
  property_count: 31
  slug: salesforce-user-preferences-receive-no-notifications-as-approver
- name: UserPreferencesReceiveNotificationsAsDelegatedApprover
  property_count: 31
  slug: salesforce-user-preferences-receive-notifications-as-delegated-approver
- name: UserPreferencesRecordHomeReservedWTShown
  property_count: 31
  slug: salesforce-user-preferences-record-home-reserved-wt-shown
- name: UserPreferencesRecordHomeSectionCollapseWTShown
  property_count: 31
  slug: salesforce-user-preferences-record-home-section-collapse-wt-shown
- name: UserPreferencesReminderSoundOff
  property_count: 31
  slug: salesforce-user-preferences-reminder-sound-off
- name: UserPreferencesReverseOpenActivitiesView
  property_count: 31
  slug: salesforce-user-preferences-reverse-open-activities-view
- name: UserPreferencesSalesEssentialsSetupAssistantCompleted
  property_count: 31
  slug: salesforce-user-preferences-sales-essentials-setup-assistant-completed
- name: UserPreferences
  property_count: 2
  slug: salesforce-user-preferences
- name: UserPreferencesSetupAssistantUserPref1
  property_count: 31
  slug: salesforce-user-preferences-setup-assistant-user-pref1
- name: UserPreferencesShowCityToExternalUsers
  property_count: 31
  slug: salesforce-user-preferences-show-city-to-external-users
- name: UserPreferencesShowCityToGuestUsers
  property_count: 31
  slug: salesforce-user-preferences-show-city-to-guest-users
- name: UserPreferencesShowCountryToExternalUsers
  property_count: 31
  slug: salesforce-user-preferences-show-country-to-external-users
- name: UserPreferencesShowCountryToGuestUsers
  property_count: 31
  slug: salesforce-user-preferences-show-country-to-guest-users
- name: UserPreferencesShowEmailToExternalUsers
  property_count: 31
  slug: salesforce-user-preferences-show-email-to-external-users
- name: UserPreferencesShowEmailToGuestUsers
  property_count: 31
  slug: salesforce-user-preferences-show-email-to-guest-users
- name: UserPreferencesShowFaxToExternalUsers
  property_count: 31
  slug: salesforce-user-preferences-show-fax-to-external-users
- name: UserPreferencesShowFaxToGuestUsers
  property_count: 31
  slug: salesforce-user-preferences-show-fax-to-guest-users
- name: UserPreferencesShowForecastingChangeSignals
  property_count: 31
  slug: salesforce-user-preferences-show-forecasting-change-signals
- name: UserPreferencesShowManagerToExternalUsers
  property_count: 31
  slug: salesforce-user-preferences-show-manager-to-external-users
- name: UserPreferencesShowManagerToGuestUsers
  property_count: 31
  slug: salesforce-user-preferences-show-manager-to-guest-users
- name: UserPreferencesShowMobilePhoneToExternalUsers
  property_count: 31
  slug: salesforce-user-preferences-show-mobile-phone-to-external-users
- name: UserPreferencesShowMobilePhoneToGuestUsers
  property_count: 31
  slug: salesforce-user-preferences-show-mobile-phone-to-guest-users
- name: UserPreferencesShowPostalCodeToExternalUsers
  property_count: 31
  slug: salesforce-user-preferences-show-postal-code-to-external-users
- name: UserPreferencesShowPostalCodeToGuestUsers
  property_count: 31
  slug: salesforce-user-preferences-show-postal-code-to-guest-users
- name: UserPreferencesShowProfilePicToGuestUsers
  property_count: 31
  slug: salesforce-user-preferences-show-profile-pic-to-guest-users
- name: UserPreferencesShowStateToExternalUsers
  property_count: 31
  slug: salesforce-user-preferences-show-state-to-external-users
- name: UserPreferencesShowStateToGuestUsers
  property_count: 31
  slug: salesforce-user-preferences-show-state-to-guest-users
- name: UserPreferencesShowStreetAddressToExternalUsers
  property_count: 31
  slug: salesforce-user-preferences-show-street-address-to-external-users
- name: UserPreferencesShowStreetAddressToGuestUsers
  property_count: 31
  slug: salesforce-user-preferences-show-street-address-to-guest-users
- name: UserPreferencesShowTitleToExternalUsers
  property_count: 31
  slug: salesforce-user-preferences-show-title-to-external-users
- name: UserPreferencesShowTitleToGuestUsers
  property_count: 31
  slug: salesforce-user-preferences-show-title-to-guest-users
- name: UserPreferencesShowWorkPhoneToExternalUsers
  property_count: 31
  slug: salesforce-user-preferences-show-work-phone-to-external-users
- name: UserPreferencesShowWorkPhoneToGuestUsers
  property_count: 31
  slug: salesforce-user-preferences-show-work-phone-to-guest-users
- name: UserPreferencesSortFeedByComment
  property_count: 31
  slug: salesforce-user-preferences-sort-feed-by-comment
- name: UserPreferencesSRHOverrideActivities
  property_count: 31
  slug: salesforce-user-preferences-srh-override-activities
- name: UserPreferencesSuppressEventSFXReminders
  property_count: 31
  slug: salesforce-user-preferences-suppress-event-sfx-reminders
- name: UserPreferencesSuppressTaskSFXReminders
  property_count: 31
  slug: salesforce-user-preferences-suppress-task-sfx-reminders
- name: UserPreferencesTaskRemindersCheckboxDefault
  property_count: 31
  slug: salesforce-user-preferences-task-reminders-checkbox-default
- name: UserPreferencesTodayGettingStarted
  property_count: 31
  slug: salesforce-user-preferences-today-getting-started
- name: UserPreferencesTrailheadBadgeCreated
  property_count: 31
  slug: salesforce-user-preferences-trailhead-badge-created
- name: UserPreferencesUserDebugModePref
  property_count: 31
  slug: salesforce-user-preferences-user-debug-mode-pref
- name: UserRoleId
  property_count: 31
  slug: salesforce-user-role-id
- name: UserRole
  property_count: 6
  slug: salesforce-user-role
- name: User
  property_count: 19
  slug: salesforce-user
- name: UserType
  property_count: 31
  slug: salesforce-user-type
- name: User3
  property_count: 19
  slug: salesforce-user3
- name: User4
  property_count: 19
  slug: salesforce-user4
- name: User7
  property_count: 23
  slug: salesforce-user7
- name: User8
  property_count: 6
  slug: salesforce-user8
- name: Userdata
  property_count: 4
  slug: salesforce-userdata
- name: Username
  property_count: 31
  slug: salesforce-username
- name: Value
  property_count: 11
  slug: salesforce-value
- name: Value2
  property_count: 11
  slug: salesforce-value2
- name: Value22
  property_count: 10
  slug: salesforce-value22
- name: Value6
  property_count: 4
  slug: salesforce-value6
- name: Variable
  property_count: 8
  slug: salesforce-variable
- name: Verified
  property_count: 5
  slug: salesforce-verified
- name: Version
  property_count: 9
  slug: salesforce-version
- name: Version2
  property_count: 11
  slug: salesforce-version2
- name: Version5
  property_count: 3
  slug: salesforce-version5
- name: View
  property_count: 8
  slug: salesforce-view
- name: Warnings
  property_count: 2
  slug: salesforce-warnings
- name: Website
  property_count: 2
  slug: salesforce-website
- name: Website1
  property_count: 31
  slug: salesforce-website1
- name: Website2
  property_count: 2
  slug: salesforce-website2
- name: Website5
  property_count: 2
  slug: salesforce-website5
- name: WorkBadgeDefinitionHistory
  property_count: 6
  slug: salesforce-work-badge-definition-history
- name: YearStarted
  property_count: 2
  slug: salesforce-year-started
- name: YearStarted1
  property_count: 31
  slug: salesforce-year-started1
json_structures:
- name: Salesforce 0 F94 H000000 Uf2X Sag Structure
  property_count: 3
  slug: salesforce-0-f94-h000000-uf2x-sag-structure
- name: Salesforce 00 B58000002Ssin Eaa Structure
  property_count: 3
  slug: salesforce-00-b58000002ssin-eaa-structure
- name: Salesforce 00 Qb0000003P O Qs Mam Structure
  property_count: 11
  slug: salesforce-00-qb0000003p-o-qs-mam-structure
- name: Salesforce 00 Qb0000003P Ordma2 Structure
  property_count: 11
  slug: salesforce-00-qb0000003p-ordma2-structure
- name: Salesforce 0014 H00002 Lb R7 Qqav Structure
  property_count: 3
  slug: salesforce-0014-h00002-lb-r7-qqav-structure
- name: Salesforce 0014 H00002 Lb R7 Qqav1 Structure
  property_count: 3
  slug: salesforce-0014-h00002-lb-r7-qqav1-structure
- name: Salesforce 00158000006 Qb Oh Aao Structure
  property_count: 3
  slug: salesforce-00158000006-qb-oh-aao-structure
- name: Salesforce 00158000006 Qb Oh Aao1 Structure
  property_count: 3
  slug: salesforce-00158000006-qb-oh-aao1-structure
- name: Salesforce 00158000006 Qb Oh Aao2 Structure
  property_count: 3
  slug: salesforce-00158000006-qb-oh-aao2-structure
- name: Salesforce 00358000006Woxw Aaa Structure
  property_count: 3
  slug: salesforce-00358000006woxw-aaa-structure
- name: Salesforce 00H B0000000 Jr Bria0 Structure
  property_count: 2
  slug: salesforce-00h-b0000000-jr-bria0-structure
- name: Salesforce 01 Bb0000002R P3 Imau Structure
  property_count: 2
  slug: salesforce-01-bb0000002r-p3-imau-structure
- name: Salesforce 01 Bb0000002R P3 Jmau Structure
  property_count: 2
  slug: salesforce-01-bb0000002r-p3-jmau-structure
- name: Salesforce 01 Bb0000002R P3 Lmau Structure
  property_count: 2
  slug: salesforce-01-bb0000002r-p3-lmau-structure
- name: Salesforce 01 Bb0000002R P3 Mmau Structure
  property_count: 2
  slug: salesforce-01-bb0000002r-p3-mmau-structure
- name: Salesforce 01 Bb0000002R P3 Nmau Structure
  property_count: 2
  slug: salesforce-01-bb0000002r-p3-nmau-structure
- name: Salesforce 012000000000000 Aaa Structure
  property_count: 1
  slug: salesforce-012000000000000-aaa-structure
- name: Salesforce 012000000000000 Aaa1 Structure
  property_count: 5
  slug: salesforce-012000000000000-aaa1-structure
- name: Salesforce 404 Because Version59.0 Not Present In Target Org1 Structure
  property_count: 2
  slug: salesforce-404-because-version59.0-not-present-in-target-org1-structure
- name: Salesforce Aborta Job Query Request Structure
  property_count: 1
  slug: salesforce-aborta-job-query-request-structure
- name: Salesforce Aborta Job Query Structure
  property_count: 10
  slug: salesforce-aborta-job-query-structure
- name: Salesforce About Me Structure
  property_count: 31
  slug: salesforce-about-me-structure
- name: Salesforce Access Records Structure
  property_count: 19
  slug: salesforce-access-records-structure
- name: Salesforce Account Brand Structure
  property_count: 6
  slug: salesforce-account-brand-structure
- name: Salesforce Account Create Structure
  property_count: 1
  slug: salesforce-account-create-structure
- name: Salesforce Account Custom Field Structure
  property_count: 2
  slug: salesforce-account-custom-field-structure
- name: Salesforce Account Delete Structure
  property_count: 1
  slug: salesforce-account-delete-structure
- name: Salesforce Account History Structure
  property_count: 6
  slug: salesforce-account-history-structure
- name: Salesforce Account Id Structure
  property_count: 2
  slug: salesforce-account-id-structure
- name: Salesforce Account Id1 Structure
  property_count: 31
  slug: salesforce-account-id1-structure
- name: Salesforce Account Id2 Structure
  property_count: 2
  slug: salesforce-account-id2-structure
- name: Salesforce Account Number Structure
  property_count: 2
  slug: salesforce-account-number-structure
- name: Salesforce Account Number1 Structure
  property_count: 31
  slug: salesforce-account-number1-structure
- name: Salesforce Account Number2 Structure
  property_count: 2
  slug: salesforce-account-number2-structure
- name: Salesforce Account Number4 Structure
  property_count: 2
  slug: salesforce-account-number4-structure
- name: Salesforce Account Partner Structure
  property_count: 6
  slug: salesforce-account-partner-structure
- name: Salesforce Account S Object Structure
  property_count: 3
  slug: salesforce-account-s-object-structure
- name: Salesforce Account Source Structure
  property_count: 2
  slug: salesforce-account-source-structure
- name: Salesforce Account Source1 Structure
  property_count: 31
  slug: salesforce-account-source1-structure
- name: Salesforce Account Structure
  property_count: 2
  slug: salesforce-account-structure
- name: Salesforce Account Update Structure
  property_count: 1
  slug: salesforce-account-update-structure
- name: Salesforce Account10 Structure
  property_count: 3
  slug: salesforce-account10-structure
- name: Salesforce Account11 Structure
  property_count: 1
  slug: salesforce-account11-structure
- name: Salesforce Account12 Structure
  property_count: 6
  slug: salesforce-account12-structure
- name: Salesforce Account13 Structure
  property_count: 23
  slug: salesforce-account13-structure
- name: Salesforce Account15 Structure
  property_count: 8
  slug: salesforce-account15-structure
- name: Salesforce Account16 Structure
  property_count: 4
  slug: salesforce-account16-structure
- name: Salesforce Account17 Structure
  property_count: 3
  slug: salesforce-account17-structure
- name: Salesforce Account18 Structure
  property_count: 3
  slug: salesforce-account18-structure
- name: Salesforce Account7 Structure
  property_count: 1
  slug: salesforce-account7-structure
- name: Salesforce Accountby Id Structure
  property_count: 2
  slug: salesforce-accountby-id-structure
- name: Salesforce Accounts Structure
  property_count: 2
  slug: salesforce-accounts-structure
- name: Salesforce Accountswith Cursors Pagination Structure
  property_count: 2
  slug: salesforce-accountswith-cursors-pagination-structure
- name: Salesforce Accountswith Filter Structure
  property_count: 2
  slug: salesforce-accountswith-filter-structure
- name: Salesforce Action Override Structure
  property_count: 5
  slug: salesforce-action-override-structure
- name: Salesforce Actions Structure
  property_count: 1
  slug: salesforce-actions-structure
- name: Salesforce Actions1 Structure
  property_count: 19
  slug: salesforce-actions1-structure
- name: Salesforce Actions10 Structure
  property_count: 19
  slug: salesforce-actions10-structure
- name: Salesforce Actions11 Structure
  property_count: 1
  slug: salesforce-actions11-structure
- name: Salesforce Actions12 Structure
  property_count: 19
  slug: salesforce-actions12-structure
- name: Salesforce Actions13 Structure
  property_count: 1
  slug: salesforce-actions13-structure
- name: Salesforce Actions14 Structure
  property_count: 19
  slug: salesforce-actions14-structure
- name: Salesforce Actions15 Structure
  property_count: 1
  slug: salesforce-actions15-structure
- name: Salesforce Actions17 Structure
  property_count: 1
  slug: salesforce-actions17-structure
- name: Salesforce Actions18 Structure
  property_count: 19
  slug: salesforce-actions18-structure
- name: Salesforce Actions19 Structure
  property_count: 1
  slug: salesforce-actions19-structure
- name: Salesforce Actions2 Structure
  property_count: 2
  slug: salesforce-actions2-structure
- name: Salesforce Actions21 Structure
  property_count: 1
  slug: salesforce-actions21-structure
- name: Salesforce Actions22 Structure
  property_count: 19
  slug: salesforce-actions22-structure
- name: Salesforce Actions23 Structure
  property_count: 1
  slug: salesforce-actions23-structure
- name: Salesforce Actions24 Structure
  property_count: 19
  slug: salesforce-actions24-structure
- name: Salesforce Actions3 Structure
  property_count: 19
  slug: salesforce-actions3-structure
- name: Salesforce Actions5 Structure
  property_count: 1
  slug: salesforce-actions5-structure
- name: Salesforce Actions6 Structure
  property_count: 19
  slug: salesforce-actions6-structure
- name: Salesforce Actions7 Structure
  property_count: 1
  slug: salesforce-actions7-structure
- name: Salesforce Actions8 Structure
  property_count: 19
  slug: salesforce-actions8-structure
- name: Salesforce Actions9 Structure
  property_count: 1
  slug: salesforce-actions9-structure
- name: Salesforce Activateable Structure
  property_count: 1
  slug: salesforce-activateable-structure
- name: Salesforce Active C Structure
  property_count: 1
  slug: salesforce-active-c-structure
- name: Salesforce Active C1 Structure
  property_count: 31
  slug: salesforce-active-c1-structure
- name: Salesforce Active C2 Structure
  property_count: 2
  slug: salesforce-active-c2-structure
- name: Salesforce Active C4 Structure
  property_count: 2
  slug: salesforce-active-c4-structure
- name: Salesforce Active Scratch Org History Structure
  property_count: 6
  slug: salesforce-active-scratch-org-history-structure
- name: Salesforce Active Scratch Org Structure
  property_count: 6
  slug: salesforce-active-scratch-org-structure
- name: Salesforce Active Scratch Orgs Structure
  property_count: 2
  slug: salesforce-active-scratch-orgs-structure
- name: Salesforce Actor Structure
  property_count: 19
  slug: salesforce-actor-structure
- name: Salesforce Addanitemtoacart Request Structure
  property_count: 3
  slug: salesforce-addanitemtoacart-request-structure
- name: Salesforce Addenrichedfieldstochannelmember Request Structure
  property_count: 2
  slug: salesforce-addenrichedfieldstochannelmember-request-structure
- name: Salesforce Addfilterexpressioninchannelmember Request Structure
  property_count: 2
  slug: salesforce-addfilterexpressioninchannelmember-request-structure
- name: Salesforce Additional Data Structure
  property_count: 2
  slug: salesforce-additional-data-structure
- name: Salesforce Additional Field Values Structure
  property_count: 1
  slug: salesforce-additional-field-values-structure
- name: Salesforce Additional Loyalty Member Currency Fields Structure
  property_count: 1
  slug: salesforce-additional-loyalty-member-currency-fields-structure
- name: Salesforce Additional Properties Structure
  property_count: 1
  slug: salesforce-additional-properties-structure
- name: Salesforce Address Structure
  property_count: 1
  slug: salesforce-address-structure
- name: Salesforce Address1 Structure
  property_count: 6
  slug: salesforce-address1-structure
- name: Salesforce Address5 Structure
  property_count: 31
  slug: salesforce-address5-structure
- name: Salesforce Aggregation Results Structure
  property_count: 1
  slug: salesforce-aggregation-results-structure
- name: Salesforce Alias Structure
  property_count: 31
  slug: salesforce-alias-structure
- name: Salesforce Alias4 Structure
  property_count: 2
  slug: salesforce-alias4-structure
- name: Salesforce Analytics External Data Size Mb Structure
  property_count: 2
  slug: salesforce-analytics-external-data-size-mb-structure
- name: Salesforce Annotation Structure
  property_count: 1
  slug: salesforce-annotation-structure
- name: Salesforce Annual Revenue Structure
  property_count: 2
  slug: salesforce-annual-revenue-structure
- name: Salesforce Annual Revenue1 Structure
  property_count: 31
  slug: salesforce-annual-revenue1-structure
- name: Salesforce Annual Revenue2 Structure
  property_count: 2
  slug: salesforce-annual-revenue2-structure
- name: Salesforce Annual Revenue3 Structure
  property_count: 2
  slug: salesforce-annual-revenue3-structure
- name: Salesforce Api Anomaly Event Store Structure
  property_count: 6
  slug: salesforce-api-anomaly-event-store-structure
- name: Salesforce App Analytics Query Request Structure
  property_count: 6
  slug: salesforce-app-analytics-query-request-structure
- name: Salesforce App Menu Item Structure
  property_count: 6
  slug: salesforce-app-menu-item-structure
- name: Salesforce App Menu Structure
  property_count: 3
  slug: salesforce-app-menu-structure
- name: Salesforce App Structure
  property_count: 18
  slug: salesforce-app-structure
- name: Salesforce Application Json Structure
  property_count: 1
  slug: salesforce-application-json-structure
- name: Salesforce Application Json1 Structure
  property_count: 1
  slug: salesforce-application-json1-structure
- name: Salesforce Applied Promotion Structure
  property_count: 2
  slug: salesforce-applied-promotion-structure
- name: Salesforce Asset History Structure
  property_count: 6
  slug: salesforce-asset-history-structure
- name: Salesforce Asset Ids Structure
  property_count: 1
  slug: salesforce-asset-ids-structure
- name: Salesforce Asset Relationship History Structure
  property_count: 6
  slug: salesforce-asset-relationship-history-structure
- name: Salesforce Asset Relationship Structure
  property_count: 6
  slug: salesforce-asset-relationship-structure
- name: Salesforce Asset Structure
  property_count: 6
  slug: salesforce-asset-structure
- name: Salesforce Assignment Structure
  property_count: 2
  slug: salesforce-assignment-structure
- name: Salesforce Assistant Name Structure
  property_count: 2
  slug: salesforce-assistant-name-structure
- name: Salesforce Assistant Phone Structure
  property_count: 2
  slug: salesforce-assistant-phone-structure
- name: Salesforce Associate Entity Type Structure
  property_count: 1
  slug: salesforce-associate-entity-type-structure
- name: Salesforce Associate Parent Entity Structure
  property_count: 1
  slug: salesforce-associate-parent-entity-structure
- name: Salesforce Associated Account Details Structure
  property_count: 4
  slug: salesforce-associated-account-details-structure
- name: Salesforce Associated Actions Structure
  property_count: 1
  slug: salesforce-associated-actions-structure
- name: Salesforce Associated Contact Details Structure
  property_count: 4
  slug: salesforce-associated-contact-details-structure
- name: Salesforce Associated Contact Structure
  property_count: 4
  slug: salesforce-associated-contact-structure
- name: Salesforce Attributes Structure
  property_count: 2
  slug: salesforce-attributes-structure
- name: Salesforce Attributes14 Structure
  property_count: 1
  slug: salesforce-attributes14-structure
- name: Salesforce Attributes15 Structure
  property_count: 2
  slug: salesforce-attributes15-structure
- name: Salesforce Attributes22 Structure
  property_count: 2
  slug: salesforce-attributes22-structure
- name: Salesforce Attributes29 Structure
  property_count: 3
  slug: salesforce-attributes29-structure
- name: Salesforce Attributes3 Structure
  property_count: 1
  slug: salesforce-attributes3-structure
- name: Salesforce Attributes35 Structure
  property_count: 2
  slug: salesforce-attributes35-structure
- name: Salesforce Attributes4 Structure
  property_count: 2
  slug: salesforce-attributes4-structure
- name: Salesforce Authorization Code Structure
  property_count: 3
  slug: salesforce-authorization-code-structure
- name: Salesforce Authorization Form Consent History Structure
  property_count: 6
  slug: salesforce-authorization-form-consent-history-structure
- name: Salesforce Authorization Form Consent Structure
  property_count: 6
  slug: salesforce-authorization-form-consent-structure
- name: Salesforce Authorization Form Data Use History Structure
  property_count: 6
  slug: salesforce-authorization-form-data-use-history-structure
- name: Salesforce Authorization Form Data Use Structure
  property_count: 6
  slug: salesforce-authorization-form-data-use-structure
- name: Salesforce Authorization Form History Structure
  property_count: 6
  slug: salesforce-authorization-form-history-structure
- name: Salesforce Authorization Form Structure
  property_count: 6
  slug: salesforce-authorization-form-structure
- name: Salesforce Authorization Form Text History Structure
  property_count: 6
  slug: salesforce-authorization-form-text-history-structure
- name: Salesforce Authorization Form Text Structure
  property_count: 6
  slug: salesforce-authorization-form-text-structure
- name: Salesforce Background Operation Structure
  property_count: 6
  slug: salesforce-background-operation-structure
- name: Salesforce Badge Text Structure
  property_count: 31
  slug: salesforce-badge-text-structure
- name: Salesforce Banner Photo Id Structure
  property_count: 31
  slug: salesforce-banner-photo-id-structure
- name: Salesforce Banner Photo Structure
  property_count: 3
  slug: salesforce-banner-photo-structure
- name: Salesforce Banner Photo Url Structure
  property_count: 31
  slug: salesforce-banner-photo-url-structure
- name: Salesforce Batch Info List Structure
  property_count: 1
  slug: salesforce-batch-info-list-structure
- name: Salesforce Batch Info Structure
  property_count: 10
  slug: salesforce-batch-info-structure
- name: Salesforce Batch Request Structure
  property_count: 2
  slug: salesforce-batch-request-structure
- name: Salesforce Bearer Auth Structure
  property_count: 3
  slug: salesforce-bearer-auth-structure
- name: Salesforce Billing Address Structure
  property_count: 2
  slug: salesforce-billing-address-structure
- name: Salesforce Billing Address1 Structure
  property_count: 8
  slug: salesforce-billing-address1-structure
- name: Salesforce Billing Address2 Structure
  property_count: 31
  slug: salesforce-billing-address2-structure
- name: Salesforce Billing City Structure
  property_count: 2
  slug: salesforce-billing-city-structure
- name: Salesforce Billing City1 Structure
  property_count: 31
  slug: salesforce-billing-city1-structure
- name: Salesforce Billing City2 Structure
  property_count: 2
  slug: salesforce-billing-city2-structure
- name: Salesforce Billing City3 Structure
  property_count: 2
  slug: salesforce-billing-city3-structure
- name: Salesforce Billing Country Structure
  property_count: 2
  slug: salesforce-billing-country-structure
- name: Salesforce Billing Country1 Structure
  property_count: 31
  slug: salesforce-billing-country1-structure
- name: Salesforce Billing Country2 Structure
  property_count: 2
  slug: salesforce-billing-country2-structure
- name: Salesforce Billing Country3 Structure
  property_count: 2
  slug: salesforce-billing-country3-structure
- name: Salesforce Billing Geocode Accuracy Structure
  property_count: 2
  slug: salesforce-billing-geocode-accuracy-structure
- name: Salesforce Billing Geocode Accuracy1 Structure
  property_count: 31
  slug: salesforce-billing-geocode-accuracy1-structure
- name: Salesforce Billing Latitude Structure
  property_count: 2
  slug: salesforce-billing-latitude-structure
- name: Salesforce Billing Latitude1 Structure
  property_count: 31
  slug: salesforce-billing-latitude1-structure
- name: Salesforce Billing Longitude Structure
  property_count: 2
  slug: salesforce-billing-longitude-structure
- name: Salesforce Billing Longitude1 Structure
  property_count: 31
  slug: salesforce-billing-longitude1-structure
- name: Salesforce Billing Postal Code Structure
  property_count: 2
  slug: salesforce-billing-postal-code-structure
- name: Salesforce Billing Postal Code1 Structure
  property_count: 31
  slug: salesforce-billing-postal-code1-structure
- name: Salesforce Billing Postal Code2 Structure
  property_count: 2
  slug: salesforce-billing-postal-code2-structure
- name: Salesforce Billing Postal Code3 Structure
  property_count: 2
  slug: salesforce-billing-postal-code3-structure
- name: Salesforce Billing State Structure
  property_count: 2
  slug: salesforce-billing-state-structure
- name: Salesforce Billing State1 Structure
  property_count: 31
  slug: salesforce-billing-state1-structure
- name: Salesforce Billing State2 Structure
  property_count: 2
  slug: salesforce-billing-state2-structure
- name: Salesforce Billing State3 Structure
  property_count: 2
  slug: salesforce-billing-state3-structure
- name: Salesforce Billing Street Structure
  property_count: 2
  slug: salesforce-billing-street-structure
- name: Salesforce Billing Street1 Structure
  property_count: 31
  slug: salesforce-billing-street1-structure
- name: Salesforce Billing Street2 Structure
  property_count: 2
  slug: salesforce-billing-street2-structure
- name: Salesforce Billing Street3 Structure
  property_count: 2
  slug: salesforce-billing-street3-structure
- name: Salesforce Birthdate Structure
  property_count: 3
  slug: salesforce-birthdate-structure
- name: Salesforce Body Structure
  property_count: 3
  slug: salesforce-body-structure
- name: Salesforce Body1 Structure
  property_count: 3
  slug: salesforce-body1-structure
- name: Salesforce Body11 Structure
  property_count: 3
  slug: salesforce-body11-structure
- name: Salesforce Body12 Structure
  property_count: 1
  slug: salesforce-body12-structure
- name: Salesforce Body14 Structure
  property_count: 3
  slug: salesforce-body14-structure
- name: Salesforce Body15 Structure
  property_count: 3
  slug: salesforce-body15-structure
- name: Salesforce Body16 Structure
  property_count: 1
  slug: salesforce-body16-structure
- name: Salesforce Body17 Structure
  property_count: 1
  slug: salesforce-body17-structure
- name: Salesforce Body18 Structure
  property_count: 1
  slug: salesforce-body18-structure
- name: Salesforce Body19 Structure
  property_count: 1
  slug: salesforce-body19-structure
- name: Salesforce Body2 Structure
  property_count: 2
  slug: salesforce-body2-structure
- name: Salesforce Body20 Structure
  property_count: 1
  slug: salesforce-body20-structure
- name: Salesforce Body21 Structure
  property_count: 1
  slug: salesforce-body21-structure
- name: Salesforce Body22 Structure
  property_count: 1
  slug: salesforce-body22-structure
- name: Salesforce Body23 Structure
  property_count: 1
  slug: salesforce-body23-structure
- name: Salesforce Body24 Structure
  property_count: 16
  slug: salesforce-body24-structure
- name: Salesforce Body25 Structure
  property_count: 23
  slug: salesforce-body25-structure
- name: Salesforce Body26 Structure
  property_count: 21
  slug: salesforce-body26-structure
- name: Salesforce Body4 Structure
  property_count: 3
  slug: salesforce-body4-structure
- name: Salesforce Body5 Structure
  property_count: 1
  slug: salesforce-body5-structure
- name: Salesforce Body6 Structure
  property_count: 3
  slug: salesforce-body6-structure
- name: Salesforce Body7 Structure
  property_count: 1
  slug: salesforce-body7-structure
- name: Salesforce Bookmarks Structure
  property_count: 1
  slug: salesforce-bookmarks-structure
- name: Salesforce Brand Image Structure
  property_count: 3
  slug: salesforce-brand-image-structure
- name: Salesforce Bulk 2 Error Structure
  property_count: 3
  slug: salesforce-bulk-2-error-structure
- name: Salesforce Bulk 2 Ingest Job Info Structure
  property_count: 17
  slug: salesforce-bulk-2-ingest-job-info-structure
- name: Salesforce Bulk 2 Ingest Job Request Structure
  property_count: 7
  slug: salesforce-bulk-2-ingest-job-request-structure
- name: Salesforce Bulk 2 Job State Structure
  property_count: 0
  slug: salesforce-bulk-2-job-state-structure
- name: Salesforce Bulk 2 Query Job Info Structure
  property_count: 15
  slug: salesforce-bulk-2-query-job-info-structure
- name: Salesforce Bulk 2 Query Job Request Structure
  property_count: 5
  slug: salesforce-bulk-2-query-job-request-structure
- name: Salesforce Bulk Close Job Request Structure
  property_count: 1
  slug: salesforce-bulk-close-job-request-structure
- name: Salesforce Bulk Create Job Request Structure
  property_count: 3
  slug: salesforce-bulk-create-job-request-structure
- name: Salesforce Business Brand Structure
  property_count: 6
  slug: salesforce-business-brand-structure
- name: Salesforce Business Hours Structure
  property_count: 6
  slug: salesforce-business-hours-structure
- name: Salesforce Calculate Price New Sale Bundles Request Structure
  property_count: 4
  slug: salesforce-calculate-price-new-sale-bundles-request-structure
- name: Salesforce Calculate Price New Sale Request Structure
  property_count: 3
  slug: salesforce-calculate-price-new-sale-request-structure
- name: Salesforce Calculate Price New Salewith Discounts Request Structure
  property_count: 3
  slug: salesforce-calculate-price-new-salewith-discounts-request-structure
- name: Salesforce Call Center Id Structure
  property_count: 31
  slug: salesforce-call-center-id-structure
- name: Salesforce Callout Options Structure
  property_count: 3
  slug: salesforce-callout-options-structure
- name: Salesforce Campaign History Structure
  property_count: 6
  slug: salesforce-campaign-history-structure
- name: Salesforce Campaign Member Status Structure
  property_count: 6
  slug: salesforce-campaign-member-status-structure
- name: Salesforce Campaign Member Structure
  property_count: 6
  slug: salesforce-campaign-member-structure
- name: Salesforce Campaign Structure
  property_count: 1
  slug: salesforce-campaign-structure
- name: Salesforce Campaign4 Structure
  property_count: 6
  slug: salesforce-campaign4-structure
- name: Salesforce Cancela Voucher Request Structure
  property_count: 1
  slug: salesforce-cancela-voucher-request-structure
- name: Salesforce Capabilities Structure
  property_count: 12
  slug: salesforce-capabilities-structure
- name: Salesforce Capabilities1 Structure
  property_count: 1
  slug: salesforce-capabilities1-structure
- name: Salesforce Capabilities6 Structure
  property_count: 4
  slug: salesforce-capabilities6-structure
- name: Salesforce Capabilities8 Structure
  property_count: 4
  slug: salesforce-capabilities8-structure
- name: Salesforce Card Payment Method Structure
  property_count: 11
  slug: salesforce-card-payment-method-structure
- name: Salesforce Cart Detail Structure
  property_count: 5
  slug: salesforce-cart-detail-structure
- name: Salesforce Cart Line Detail Structure
  property_count: 4
  slug: salesforce-cart-line-detail-structure
- name: Salesforce Cart Structure
  property_count: 1
  slug: salesforce-cart-structure
- name: Salesforce Case Comment Structure
  property_count: 6
  slug: salesforce-case-comment-structure
- name: Salesforce Case Contact Role Structure
  property_count: 6
  slug: salesforce-case-contact-role-structure
- name: Salesforce Case History Structure
  property_count: 6
  slug: salesforce-case-history-structure
- name: Salesforce Case Structure
  property_count: 6
  slug: salesforce-case-structure
- name: Salesforce Changeeventrelaystate Request Structure
  property_count: 1
  slug: salesforce-changeeventrelaystate-request-structure
- name: Salesforce Channel Program History Structure
  property_count: 6
  slug: salesforce-channel-program-history-structure
- name: Salesforce Channel Program Level History Structure
  property_count: 6
  slug: salesforce-channel-program-level-history-structure
- name: Salesforce Channel Program Level Name Structure
  property_count: 2
  slug: salesforce-channel-program-level-name-structure
- name: Salesforce Channel Program Level Name1 Structure
  property_count: 31
  slug: salesforce-channel-program-level-name1-structure
- name: Salesforce Channel Program Level Structure
  property_count: 6
  slug: salesforce-channel-program-level-structure
- name: Salesforce Channel Program Member History Structure
  property_count: 6
  slug: salesforce-channel-program-member-history-structure
- name: Salesforce Channel Program Member Structure
  property_count: 6
  slug: salesforce-channel-program-member-structure
- name: Salesforce Channel Program Name Structure
  property_count: 2
  slug: salesforce-channel-program-name-structure
- name: Salesforce Channel Program Name1 Structure
  property_count: 31
  slug: salesforce-channel-program-name1-structure
- name: Salesforce Channel Program Structure
  property_count: 6
  slug: salesforce-channel-program-structure
- name: Salesforce Chatter Likes Structure
  property_count: 4
  slug: salesforce-chatter-likes-structure
- name: Salesforce Child Accounts Structure
  property_count: 1
  slug: salesforce-child-accounts-structure
- name: Salesforce Child Relationship Structure
  property_count: 8
  slug: salesforce-child-relationship-structure
- name: Salesforce Child Relationship2 Structure
  property_count: 5
  slug: salesforce-child-relationship2-structure
- name: Salesforce City Structure
  property_count: 31
  slug: salesforce-city-structure
- name: Salesforce City2 Structure
  property_count: 2
  slug: salesforce-city2-structure
- name: Salesforce City3 Structure
  property_count: 2
  slug: salesforce-city3-structure
- name: Salesforce Clean Status Structure
  property_count: 2
  slug: salesforce-clean-status-structure
- name: Salesforce Clean Status2 Structure
  property_count: 31
  slug: salesforce-clean-status2-structure
- name: Salesforce Clean Status4 Structure
  property_count: 5
  slug: salesforce-clean-status4-structure
- name: Salesforce Client Info Structure
  property_count: 2
  slug: salesforce-client-info-structure
- name: Salesforce Clone Source Id Structure
  property_count: 31
  slug: salesforce-clone-source-id-structure
- name: Salesforce Clone Source Id3 Structure
  property_count: 2
  slug: salesforce-clone-source-id3-structure
- name: Salesforce Close Date Structure
  property_count: 2
  slug: salesforce-close-date-structure
- name: Salesforce Close Structure
  property_count: 2
  slug: salesforce-close-structure
- name: Salesforce Closeor Aborta Job Request Structure
  property_count: 1
  slug: salesforce-closeor-aborta-job-request-structure
- name: Salesforce Code Coverage Structure
  property_count: 7
  slug: salesforce-code-coverage-structure
- name: Salesforce Code Coverage Warning Structure
  property_count: 4
  slug: salesforce-code-coverage-warning-structure
- name: Salesforce Color Structure
  property_count: 3
  slug: salesforce-color-structure
- name: Salesforce Column Widths Structure
  property_count: 6
  slug: salesforce-column-widths-structure
- name: Salesforce Column Wrap Structure
  property_count: 6
  slug: salesforce-column-wrap-structure
- name: Salesforce Comm Subscription Channel Type History Structure
  property_count: 6
  slug: salesforce-comm-subscription-channel-type-history-structure
- name: Salesforce Comm Subscription Channel Type Structure
  property_count: 6
  slug: salesforce-comm-subscription-channel-type-structure
- name: Salesforce Comm Subscription History Structure
  property_count: 6
  slug: salesforce-comm-subscription-history-structure
- name: Salesforce Comm Subscription Structure
  property_count: 6
  slug: salesforce-comm-subscription-structure
- name: Salesforce Comment Edit Request Structure
  property_count: 1
  slug: salesforce-comment-edit-request-structure
- name: Salesforce Comments Structure
  property_count: 1
  slug: salesforce-comments-structure
- name: Salesforce Commitment Structure
  property_count: 15
  slug: salesforce-commitment-structure
- name: Salesforce Commitment1 Structure
  property_count: 12
  slug: salesforce-commitment1-structure
- name: Salesforce Community Nickname Structure
  property_count: 31
  slug: salesforce-community-nickname-structure
- name: Salesforce Company Duns Number Structure
  property_count: 31
  slug: salesforce-company-duns-number-structure
- name: Salesforce Company Name Structure
  property_count: 31
  slug: salesforce-company-name-structure
- name: Salesforce Company Structure
  property_count: 31
  slug: salesforce-company-structure
- name: Salesforce Company1 Structure
  property_count: 2
  slug: salesforce-company1-structure
- name: Salesforce Components Structure
  property_count: 2
  slug: salesforce-components-structure
- name: Salesforce Composite Batch Request Structure
  property_count: 2
  slug: salesforce-composite-batch-request-structure
- name: Salesforce Composite Graph Request Structure
  property_count: 1
  slug: salesforce-composite-graph-request-structure
- name: Salesforce Composite Request Structure
  property_count: 1
  slug: salesforce-composite-request-structure
- name: Salesforce Composite Request1 Structure
  property_count: 4
  slug: salesforce-composite-request1-structure
- name: Salesforce Composite Request2 Structure
  property_count: 4
  slug: salesforce-composite-request2-structure
- name: Salesforce Composite Request3 Structure
  property_count: 4
  slug: salesforce-composite-request3-structure
- name: Salesforce Composite Request4 Structure
  property_count: 4
  slug: salesforce-composite-request4-structure
- name: Salesforce Composite Request5 Structure
  property_count: 4
  slug: salesforce-composite-request5-structure
- name: Salesforce Composite Request6 Structure
  property_count: 4
  slug: salesforce-composite-request6-structure
- name: Salesforce Composite Response Structure
  property_count: 4
  slug: salesforce-composite-response-structure
- name: Salesforce Concurrent Async Get Report Instances Structure
  property_count: 2
  slug: salesforce-concurrent-async-get-report-instances-structure
- name: Salesforce Concurrent Einstein Data Insights Story Creation Structure
  property_count: 2
  slug: salesforce-concurrent-einstein-data-insights-story-creation-structure
- name: Salesforce Concurrent Einstein Discovery Story Creation Structure
  property_count: 2
  slug: salesforce-concurrent-einstein-discovery-story-creation-structure
- name: Salesforce Concurrent Sync Report Runs Structure
  property_count: 2
  slug: salesforce-concurrent-sync-report-runs-structure
- name: Salesforce Condition Structure
  property_count: 1
  slug: salesforce-condition-structure
- name: Salesforce Conditions List Structure
  property_count: 3
  slug: salesforce-conditions-list-structure
- name: Salesforce Conditions List1 Structure
  property_count: 2
  slug: salesforce-conditions-list1-structure
- name: Salesforce Conditions Structure
  property_count: 1
  slug: salesforce-conditions-structure
- name: Salesforce Constructor Structure
  property_count: 7
  slug: salesforce-constructor-structure
- name: Salesforce Consumption Rate History Structure
  property_count: 6
  slug: salesforce-consumption-rate-history-structure
- name: Salesforce Consumption Rate Structure
  property_count: 6
  slug: salesforce-consumption-rate-structure
- name: Salesforce Consumption Schedule History Structure
  property_count: 6
  slug: salesforce-consumption-schedule-history-structure
- name: Salesforce Consumption Schedule Structure
  property_count: 6
  slug: salesforce-consumption-schedule-structure
- name: Salesforce Contact History Structure
  property_count: 6
  slug: salesforce-contact-history-structure
- name: Salesforce Contact Id Structure
  property_count: 31
  slug: salesforce-contact-id-structure
- name: Salesforce Contact Point Type Consent History Structure
  property_count: 6
  slug: salesforce-contact-point-type-consent-history-structure
- name: Salesforce Contact Point Type Consent Structure
  property_count: 6
  slug: salesforce-contact-point-type-consent-structure
- name: Salesforce Contact Request Structure
  property_count: 6
  slug: salesforce-contact-request-structure
- name: Salesforce Contact S Object Structure
  property_count: 3
  slug: salesforce-contact-s-object-structure
- name: Salesforce Contact Structure
  property_count: 1
  slug: salesforce-contact-structure
- name: Salesforce Contact2 Structure
  property_count: 1
  slug: salesforce-contact2-structure
- name: Salesforce Contact3 Structure
  property_count: 6
  slug: salesforce-contact3-structure
- name: Salesforce Contacts Ordered Structure
  property_count: 2
  slug: salesforce-contacts-ordered-structure
- name: Salesforce Contacts Structure
  property_count: 1
  slug: salesforce-contacts-structure
- name: Salesforce Contacts1 Structure
  property_count: 2
  slug: salesforce-contacts1-structure
- name: Salesforce Contactswith Account Name Structure
  property_count: 2
  slug: salesforce-contactswith-account-name-structure
- name: Salesforce Content Document History Structure
  property_count: 6
  slug: salesforce-content-document-history-structure
- name: Salesforce Content Document Link Structure
  property_count: 6
  slug: salesforce-content-document-link-structure
- name: Salesforce Content Document Structure
  property_count: 6
  slug: salesforce-content-document-structure
- name: Salesforce Content Structure
  property_count: 1
  slug: salesforce-content-structure
- name: Salesforce Content Version History Structure
  property_count: 6
  slug: salesforce-content-version-history-structure
- name: Salesforce Content Version Structure
  property_count: 6
  slug: salesforce-content-version-structure
- name: Salesforce Content Workspace Structure
  property_count: 6
  slug: salesforce-content-workspace-structure
- name: Salesforce Content1 Structure
  property_count: 1
  slug: salesforce-content1-structure
- name: Salesforce Context Structure
  property_count: 2
  slug: salesforce-context-structure
- name: Salesforce Context1 Structure
  property_count: 2
  slug: salesforce-context1-structure
- name: Salesforce Context2 Structure
  property_count: 2
  slug: salesforce-context2-structure
- name: Salesforce Contract Contact Role Structure
  property_count: 6
  slug: salesforce-contract-contact-role-structure
- name: Salesforce Contract History Structure
  property_count: 6
  slug: salesforce-contract-history-structure
- name: Salesforce Contract Renewer Api Request Structure
  property_count: 1
  slug: salesforce-contract-renewer-api-request-structure
- name: Salesforce Contract Structure
  property_count: 6
  slug: salesforce-contract-structure
- name: Salesforce Conversation Entry Structure
  property_count: 7
  slug: salesforce-conversation-entry-structure
- name: Salesforce Converted Account Id Structure
  property_count: 31
  slug: salesforce-converted-account-id-structure
- name: Salesforce Converted Contact Id Structure
  property_count: 31
  slug: salesforce-converted-contact-id-structure
- name: Salesforce Converted Date Structure
  property_count: 31
  slug: salesforce-converted-date-structure
- name: Salesforce Converted Opportunity Id Structure
  property_count: 31
  slug: salesforce-converted-opportunity-id-structure
- name: Salesforce Corporate Member Enrollments Request Structure
  property_count: 5
  slug: salesforce-corporate-member-enrollments-request-structure
- name: Salesforce Corporate Member Enrollments Structure
  property_count: 5
  slug: salesforce-corporate-member-enrollments-structure
- name: Salesforce Country Structure
  property_count: 31
  slug: salesforce-country-structure
- name: Salesforce Country2 Structure
  property_count: 2
  slug: salesforce-country2-structure
- name: Salesforce Create Account Success Structure
  property_count: 2
  slug: salesforce-create-account-success-structure
- name: Salesforce Create Asset From Order Request Structure
  property_count: 1
  slug: salesforce-create-asset-from-order-request-structure
- name: Salesforce Create Clone Sandbox Request Structure
  property_count: 9
  slug: salesforce-create-clone-sandbox-request-structure
- name: Salesforce Create Commitments Request Structure
  property_count: 2
  slug: salesforce-create-commitments-request-structure
- name: Salesforce Create Credential Request Structure
  property_count: 5
  slug: salesforce-create-credential-request-structure
- name: Salesforce Create Custom Structure
  property_count: 2
  slug: salesforce-create-custom-structure
- name: Salesforce Create External Credential Request Structure
  property_count: 5
  slug: salesforce-create-external-credential-request-structure
- name: Salesforce Create Gifts Request Structure
  property_count: 2
  slug: salesforce-create-gifts-request-structure
- name: Salesforce Create Named Credential Request Structure
  property_count: 7
  slug: salesforce-create-named-credential-request-structure
- name: Salesforce Create Order Evergreen Termed Request Structure
  property_count: 2
  slug: salesforce-create-order-evergreen-termed-request-structure
- name: Salesforce Create Order From Quote Request Structure
  property_count: 1
  slug: salesforce-create-order-from-quote-request-structure
- name: Salesforce Create Order One Time Request Structure
  property_count: 2
  slug: salesforce-create-order-one-time-request-structure
- name: Salesforce Create Order With Bundle Request Structure
  property_count: 2
  slug: salesforce-create-order-with-bundle-request-structure
- name: Salesforce Create Payment Method Request Structure
  property_count: 5
  slug: salesforce-create-payment-method-request-structure
- name: Salesforce Create Pledge Commitments Request Structure
  property_count: 2
  slug: salesforce-create-pledge-commitments-request-structure
- name: Salesforce Create Sandbox Structure
  property_count: 5
  slug: salesforce-create-sandbox-structure
- name: Salesforce Create Structure
  property_count: 1
  slug: salesforce-create-structure
- name: Salesforce Create Table Request Structure
  property_count: 8
  slug: salesforce-create-table-request-structure
- name: Salesforce Createa Favorite Request Structure
  property_count: 4
  slug: salesforce-createa-favorite-request-structure
- name: Salesforce Createa Favoritelistview Structure
  property_count: 11
  slug: salesforce-createa-favoritelistview-structure
- name: Salesforce Createa Record Request Structure
  property_count: 3
  slug: salesforce-createa-record-request-structure
- name: Salesforce Createa Record Structure
  property_count: 11
  slug: salesforce-createa-record-structure
- name: Salesforce Createable Structure
  property_count: 1
  slug: salesforce-createable-structure
- name: Salesforce Createand Save Quote Proposal Api Request Structure
  property_count: 2
  slug: salesforce-createand-save-quote-proposal-api-request-structure
- name: Salesforce Createchannel Request Structure
  property_count: 2
  slug: salesforce-createchannel-request-structure
- name: Salesforce Createchannel Request1 Structure
  property_count: 2
  slug: salesforce-createchannel-request1-structure
- name: Salesforce Createchannelmember Request Structure
  property_count: 2
  slug: salesforce-createchannelmember-request-structure
- name: Salesforce Createchannelmember Request1 Structure
  property_count: 2
  slug: salesforce-createchannelmember-request1-structure
- name: Salesforce Created By Id Structure
  property_count: 1
  slug: salesforce-created-by-id-structure
- name: Salesforce Created By Id2 Structure
  property_count: 31
  slug: salesforce-created-by-id2-structure
- name: Salesforce Created By Id5 Structure
  property_count: 2
  slug: salesforce-created-by-id5-structure
- name: Salesforce Created By Structure
  property_count: 3
  slug: salesforce-created-by-structure
- name: Salesforce Created By3 Structure
  property_count: 2
  slug: salesforce-created-by3-structure
- name: Salesforce Created Date Structure
  property_count: 2
  slug: salesforce-created-date-structure
- name: Salesforce Created Date14 Structure
  property_count: 2
  slug: salesforce-created-date14-structure
- name: Salesforce Created Date2 Structure
  property_count: 31
  slug: salesforce-created-date2-structure
- name: Salesforce Created Date5 Structure
  property_count: 2
  slug: salesforce-created-date5-structure
- name: Salesforce Createeventrelay Request Structure
  property_count: 2
  slug: salesforce-createeventrelay-request-structure
- name: Salesforce Createjob Request Structure
  property_count: 2
  slug: salesforce-createjob-request-structure
- name: Salesforce Createmanagedeventsubscription Request Structure
  property_count: 2
  slug: salesforce-createmanagedeventsubscription-request-structure
- name: Salesforce Createnamedcredential Request1 Structure
  property_count: 2
  slug: salesforce-createnamedcredential-request1-structure
- name: Salesforce Createor Update Quote Request Structure
  property_count: 2
  slug: salesforce-createor-update-quote-request-structure
- name: Salesforce Credential Stuffing Event Store Structure
  property_count: 6
  slug: salesforce-credential-stuffing-event-store-structure
- name: Salesforce Credentials Structure
  property_count: 1
  slug: salesforce-credentials-structure
- name: Salesforce Credit Pointsto Members Request Structure
  property_count: 1
  slug: salesforce-credit-pointsto-members-request-structure
- name: Salesforce Credit Pointsto Members Structure
  property_count: 4
  slug: salesforce-credit-pointsto-members-structure
- name: Salesforce Csp Trusted Site Structure
  property_count: 6
  slug: salesforce-csp-trusted-site-structure
- name: Salesforce Current Generators C Structure
  property_count: 31
  slug: salesforce-current-generators-c-structure
- name: Salesforce Current Generators C1 Structure
  property_count: 2
  slug: salesforce-current-generators-c1-structure
- name: Salesforce Custom Header Structure
  property_count: 3
  slug: salesforce-custom-header-structure
- name: Salesforce Custom Header1 Structure
  property_count: 4
  slug: salesforce-custom-header1-structure
- name: Salesforce Custom Setting Structure
  property_count: 1
  slug: salesforce-custom-setting-structure
- name: Salesforce Custom Structure
  property_count: 1
  slug: salesforce-custom-structure
- name: Salesforce Customdata Structure
  property_count: 6
  slug: salesforce-customdata-structure
- name: Salesforce Customer Priority C Structure
  property_count: 1
  slug: salesforce-customer-priority-c-structure
- name: Salesforce Customer Priority C1 Structure
  property_count: 31
  slug: salesforce-customer-priority-c1-structure
- name: Salesforce Customer Priority C2 Structure
  property_count: 2
  slug: salesforce-customer-priority-c2-structure
- name: Salesforce Customer Priority C4 Structure
  property_count: 2
  slug: salesforce-customer-priority-c4-structure
- name: Salesforce Customer Structure
  property_count: 6
  slug: salesforce-customer-structure
- name: Salesforce Daily Analytics Dataflow Job Executions Structure
  property_count: 2
  slug: salesforce-daily-analytics-dataflow-job-executions-structure
- name: Salesforce Daily Analytics Uploaded Files Size Mb Structure
  property_count: 2
  slug: salesforce-daily-analytics-uploaded-files-size-mb-structure
- name: Salesforce Daily Api Requests Structure
  property_count: 2
  slug: salesforce-daily-api-requests-structure
- name: Salesforce Daily Async Apex Executions Structure
  property_count: 2
  slug: salesforce-daily-async-apex-executions-structure
- name: Salesforce Daily Async Apex Tests Structure
  property_count: 2
  slug: salesforce-daily-async-apex-tests-structure
- name: Salesforce Daily Bulk Api Batches Structure
  property_count: 2
  slug: salesforce-daily-bulk-api-batches-structure
- name: Salesforce Daily Bulk V2 Query File Storage Mb Structure
  property_count: 2
  slug: salesforce-daily-bulk-v2-query-file-storage-mb-structure
- name: Salesforce Daily Bulk V2 Query Jobs Structure
  property_count: 2
  slug: salesforce-daily-bulk-v2-query-jobs-structure
- name: Salesforce Daily Delivered Platform Events Structure
  property_count: 2
  slug: salesforce-daily-delivered-platform-events-structure
- name: Salesforce Daily Durable Generic Streaming Api Events Structure
  property_count: 2
  slug: salesforce-daily-durable-generic-streaming-api-events-structure
- name: Salesforce Daily Durable Streaming Api Events Structure
  property_count: 2
  slug: salesforce-daily-durable-streaming-api-events-structure
- name: Salesforce Daily Einstein Data Insights Story Creation Structure
  property_count: 2
  slug: salesforce-daily-einstein-data-insights-story-creation-structure
- name: Salesforce Daily Einstein Discovery Optimization Job Runs Structure
  property_count: 2
  slug: salesforce-daily-einstein-discovery-optimization-job-runs-structure
- name: Salesforce Daily Einstein Discovery Predict Api Calls Structure
  property_count: 2
  slug: salesforce-daily-einstein-discovery-predict-api-calls-structure
- name: Salesforce Daily Einstein Discovery Predictions By Cdc Structure
  property_count: 2
  slug: salesforce-daily-einstein-discovery-predictions-by-cdc-structure
- name: Salesforce Daily Einstein Discovery Story Creation Structure
  property_count: 2
  slug: salesforce-daily-einstein-discovery-story-creation-structure
- name: Salesforce Daily Functions Api Call Limit Structure
  property_count: 2
  slug: salesforce-daily-functions-api-call-limit-structure
- name: Salesforce Daily Generic Streaming Api Events Structure
  property_count: 2
  slug: salesforce-daily-generic-streaming-api-events-structure
- name: Salesforce Daily Scratch Orgs Structure
  property_count: 2
  slug: salesforce-daily-scratch-orgs-structure
- name: Salesforce Daily Standard Volume Platform Events Structure
  property_count: 2
  slug: salesforce-daily-standard-volume-platform-events-structure
- name: Salesforce Daily Streaming Api Events Structure
  property_count: 2
  slug: salesforce-daily-streaming-api-events-structure
- name: Salesforce Daily Workflow Emails Structure
  property_count: 2
  slug: salesforce-daily-workflow-emails-structure
- name: Salesforce Dand B Company Structure
  property_count: 6
  slug: salesforce-dand-b-company-structure
- name: Salesforce Dandb Company Id Structure
  property_count: 1
  slug: salesforce-dandb-company-id-structure
- name: Salesforce Dandb Company Id1 Structure
  property_count: 31
  slug: salesforce-dandb-company-id1-structure
- name: Salesforce Data Storage Mb Structure
  property_count: 2
  slug: salesforce-data-storage-mb-structure
- name: Salesforce Data Structure
  property_count: 1
  slug: salesforce-data-structure
- name: Salesforce Data Translation Enabled Structure
  property_count: 1
  slug: salesforce-data-translation-enabled-structure
- name: Salesforce Data Use Legal Basis History Structure
  property_count: 6
  slug: salesforce-data-use-legal-basis-history-structure
- name: Salesforce Data Use Legal Basis Structure
  property_count: 6
  slug: salesforce-data-use-legal-basis-structure
- name: Salesforce Data Use Purpose History Structure
  property_count: 6
  slug: salesforce-data-use-purpose-history-structure
- name: Salesforce Data Use Purpose Structure
  property_count: 6
  slug: salesforce-data-use-purpose-structure
- name: Salesforce Data10 Structure
  property_count: 1
  slug: salesforce-data10-structure
- name: Salesforce Data11 Structure
  property_count: 1
  slug: salesforce-data11-structure
- name: Salesforce Data12 Structure
  property_count: 1
  slug: salesforce-data12-structure
- name: Salesforce Data13 Structure
  property_count: 1
  slug: salesforce-data13-structure
- name: Salesforce Data3 Structure
  property_count: 1
  slug: salesforce-data3-structure
- name: Salesforce Data4 Structure
  property_count: 1
  slug: salesforce-data4-structure
- name: Salesforce Data6 Structure
  property_count: 1
  slug: salesforce-data6-structure
- name: Salesforce Data7 Structure
  property_count: 1
  slug: salesforce-data7-structure
- name: Salesforce Dataweave Key Mapping Mdt Structure
  property_count: 6
  slug: salesforce-dataweave-key-mapping-mdt-structure
- name: Salesforce Dataweave Mapping Mdt Structure
  property_count: 6
  slug: salesforce-dataweave-mapping-mdt-structure
- name: Salesforce Debit Pointsfrom Members Request Structure
  property_count: 1
  slug: salesforce-debit-pointsfrom-members-request-structure
- name: Salesforce Debit Pointsfrom Members Structure
  property_count: 4
  slug: salesforce-debit-pointsfrom-members-structure
- name: Salesforce Decision Model Notation Export Request Structure
  property_count: 1
  slug: salesforce-decision-model-notation-export-request-structure
- name: Salesforce Decision Table Structure
  property_count: 3
  slug: salesforce-decision-table-structure
- name: Salesforce Decision Table1 Structure
  property_count: 9
  slug: salesforce-decision-table1-structure
- name: Salesforce Deep Cloneable Structure
  property_count: 1
  slug: salesforce-deep-cloneable-structure
- name: Salesforce Default Group Banner Structure
  property_count: 1
  slug: salesforce-default-group-banner-structure
- name: Salesforce Default Group Image Structure
  property_count: 3
  slug: salesforce-default-group-image-structure
- name: Salesforce Default Group Notification Frequency Structure
  property_count: 31
  slug: salesforce-default-group-notification-frequency-structure
- name: Salesforce Default Page Banner Structure
  property_count: 1
  slug: salesforce-default-page-banner-structure
- name: Salesforce Default User Banner Structure
  property_count: 1
  slug: salesforce-default-user-banner-structure
- name: Salesforce Default User Image Structure
  property_count: 3
  slug: salesforce-default-user-image-structure
- name: Salesforce Delegated Account History Structure
  property_count: 6
  slug: salesforce-delegated-account-history-structure
- name: Salesforce Delegated Account Structure
  property_count: 6
  slug: salesforce-delegated-account-structure
- name: Salesforce Delegated Approver Id Structure
  property_count: 31
  slug: salesforce-delegated-approver-id-structure
- name: Salesforce Deletable Structure
  property_count: 1
  slug: salesforce-deletable-structure
- name: Salesforce Delete Account Structure
  property_count: 2
  slug: salesforce-delete-account-structure
- name: Salesforce Delete Credential Request Structure
  property_count: 3
  slug: salesforce-delete-credential-request-structure
- name: Salesforce Delete Event Structure
  property_count: 6
  slug: salesforce-delete-event-structure
- name: Salesforce Department Structure
  property_count: 2
  slug: salesforce-department-structure
- name: Salesforce Department1 Structure
  property_count: 31
  slug: salesforce-department1-structure
- name: Salesforce Deprecated And Hidden Structure
  property_count: 1
  slug: salesforce-deprecated-and-hidden-structure
- name: Salesforce Describe Metadata Response Structure
  property_count: 1
  slug: salesforce-describe-metadata-response-structure
- name: Salesforce Describe Metadata Structure
  property_count: 1
  slug: salesforce-describe-metadata-structure
- name: Salesforce Describe Value Type Response Structure
  property_count: 1
  slug: salesforce-describe-value-type-response-structure
- name: Salesforce Describe Value Type Structure
  property_count: 1
  slug: salesforce-describe-value-type-structure
- name: Salesforce Describeeventchannel Structure
  property_count: 45
  slug: salesforce-describeeventchannel-structure
- name: Salesforce Description Structure
  property_count: 1
  slug: salesforce-description-structure
- name: Salesforce Description3 Structure
  property_count: 2
  slug: salesforce-description3-structure
- name: Salesforce Description5 Structure
  property_count: 31
  slug: salesforce-description5-structure
- name: Salesforce Description6 Structure
  property_count: 2
  slug: salesforce-description6-structure
- name: Salesforce Designation Structure
  property_count: 3
  slug: salesforce-designation-structure
- name: Salesforce Designation1 Structure
  property_count: 2
  slug: salesforce-designation1-structure
- name: Salesforce Detail Structure
  property_count: 2
  slug: salesforce-detail-structure
- name: Salesforce Detail1 Structure
  property_count: 3
  slug: salesforce-detail1-structure
- name: Salesforce Detail10 Structure
  property_count: 2
  slug: salesforce-detail10-structure
- name: Salesforce Detail13 Structure
  property_count: 2
  slug: salesforce-detail13-structure
- name: Salesforce Detail14 Structure
  property_count: 3
  slug: salesforce-detail14-structure
- name: Salesforce Detail3 Structure
  property_count: 2
  slug: salesforce-detail3-structure
- name: Salesforce Detail4 Structure
  property_count: 3
  slug: salesforce-detail4-structure
- name: Salesforce Detail7 Structure
  property_count: 2
  slug: salesforce-detail7-structure
- name: Salesforce Detail8 Structure
  property_count: 2
  slug: salesforce-detail8-structure
- name: Salesforce Developer Name Structure
  property_count: 31
  slug: salesforce-developer-name-structure
- name: Salesforce Digest Frequency Structure
  property_count: 31
  slug: salesforce-digest-frequency-structure
- name: Salesforce Disambiguation Field Structure
  property_count: 2
  slug: salesforce-disambiguation-field-structure
- name: Salesforce Display Column Structure
  property_count: 6
  slug: salesforce-display-column-structure
- name: Salesforce Division Structure
  property_count: 31
  slug: salesforce-division-structure
- name: Salesforce Does Include Bosses Structure
  property_count: 31
  slug: salesforce-does-include-bosses-structure
- name: Salesforce Does Send Email To Members Structure
  property_count: 31
  slug: salesforce-does-send-email-to-members-structure
- name: Salesforce Donor Options Structure
  property_count: 1
  slug: salesforce-donor-options-structure
- name: Salesforce Donor Structure
  property_count: 9
  slug: salesforce-donor-structure
- name: Salesforce Donor1 Structure
  property_count: 8
  slug: salesforce-donor1-structure
- name: Salesforce Donor3 Structure
  property_count: 8
  slug: salesforce-donor3-structure
- name: Salesforce Duns Number Structure
  property_count: 2
  slug: salesforce-duns-number-structure
- name: Salesforce Duns Number1 Structure
  property_count: 31
  slug: salesforce-duns-number1-structure
- name: Salesforce Duplicate Record Item Structure
  property_count: 6
  slug: salesforce-duplicate-record-item-structure
- name: Salesforce Duplicate Record Set Structure
  property_count: 6
  slug: salesforce-duplicate-record-set-structure
- name: Salesforce Durable Streaming Api Concurrent Clients Structure
  property_count: 2
  slug: salesforce-durable-streaming-api-concurrent-clients-structure
- name: Salesforce Edge Structure
  property_count: 1
  slug: salesforce-edge-structure
- name: Salesforce Edge10 Structure
  property_count: 1
  slug: salesforce-edge10-structure
- name: Salesforce Edge6 Structure
  property_count: 1
  slug: salesforce-edge6-structure
- name: Salesforce Edge7 Structure
  property_count: 1
  slug: salesforce-edge7-structure
- name: Salesforce Edit Structure
  property_count: 6
  slug: salesforce-edit-structure
- name: Salesforce Edit6 Structure
  property_count: 6
  slug: salesforce-edit6-structure
- name: Salesforce Eligible Channel Structure
  property_count: 3
  slug: salesforce-eligible-channel-structure
- name: Salesforce Eligible Customer Events Structure
  property_count: 2
  slug: salesforce-eligible-customer-events-structure
- name: Salesforce Eligible Enrollment Period Structure
  property_count: 3
  slug: salesforce-eligible-enrollment-period-structure
- name: Salesforce Eligible Loyalty Tier Structure
  property_count: 2
  slug: salesforce-eligible-loyalty-tier-structure
- name: Salesforce Eligible Product Category Structure
  property_count: 1
  slug: salesforce-eligible-product-category-structure
- name: Salesforce Eligible Product Structure
  property_count: 1
  slug: salesforce-eligible-product-structure
- name: Salesforce Eligible Promotions Request Structure
  property_count: 1
  slug: salesforce-eligible-promotions-request-structure
- name: Salesforce Email Bounced Date Structure
  property_count: 3
  slug: salesforce-email-bounced-date-structure
- name: Salesforce Email Bounced Date1 Structure
  property_count: 31
  slug: salesforce-email-bounced-date1-structure
- name: Salesforce Email Bounced Reason Structure
  property_count: 2
  slug: salesforce-email-bounced-reason-structure
- name: Salesforce Email Bounced Reason1 Structure
  property_count: 31
  slug: salesforce-email-bounced-reason1-structure
- name: Salesforce Email Encoding Key Structure
  property_count: 31
  slug: salesforce-email-encoding-key-structure
- name: Salesforce Email Message Relation Structure
  property_count: 6
  slug: salesforce-email-message-relation-structure
- name: Salesforce Email Preferences Auto Bcc Stay In Touch Structure
  property_count: 31
  slug: salesforce-email-preferences-auto-bcc-stay-in-touch-structure
- name: Salesforce Email Preferences Auto Bcc Structure
  property_count: 31
  slug: salesforce-email-preferences-auto-bcc-structure
- name: Salesforce Email Preferences Stay In Touch Reminder Structure
  property_count: 31
  slug: salesforce-email-preferences-stay-in-touch-reminder-structure
- name: Salesforce Email Structure
  property_count: 2
  slug: salesforce-email-structure
- name: Salesforce Email1 Structure
  property_count: 31
  slug: salesforce-email1-structure
- name: Salesforce Email5 Structure
  property_count: 2
  slug: salesforce-email5-structure
- name: Salesforce Employee Number Structure
  property_count: 31
  slug: salesforce-employee-number-structure
- name: Salesforce Engagement Channel Type History Structure
  property_count: 6
  slug: salesforce-engagement-channel-type-history-structure
- name: Salesforce Engagement Channel Type Structure
  property_count: 6
  slug: salesforce-engagement-channel-type-structure
- name: Salesforce Enriched Field Structure
  property_count: 1
  slug: salesforce-enriched-field-structure
- name: Salesforce Enrollfor Promotions Request Structure
  property_count: 1
  slug: salesforce-enrollfor-promotions-request-structure
- name: Salesforce Entity Label Structure
  property_count: 2
  slug: salesforce-entity-label-structure
- name: Salesforce Entity Structure
  property_count: 19
  slug: salesforce-entity-structure
- name: Salesforce Envelope Structure
  property_count: 2
  slug: salesforce-envelope-structure
- name: Salesforce Envelope1 Structure
  property_count: 2
  slug: salesforce-envelope1-structure
- name: Salesforce Envelope2 Structure
  property_count: 1
  slug: salesforce-envelope2-structure
- name: Salesforce Envelope3 Structure
  property_count: 2
  slug: salesforce-envelope3-structure
- name: Salesforce Envelope4 Structure
  property_count: 1
  slug: salesforce-envelope4-structure
- name: Salesforce Envelope5 Structure
  property_count: 2
  slug: salesforce-envelope5-structure
- name: Salesforce Envelope6 Structure
  property_count: 1
  slug: salesforce-envelope6-structure
- name: Salesforce Envelope7 Structure
  property_count: 2
  slug: salesforce-envelope7-structure
- name: Salesforce Error Code Structure
  property_count: 1
  slug: salesforce-error-code-structure
- name: Salesforce Error Info Structure
  property_count: 2
  slug: salesforce-error-info-structure
- name: Salesforce Error Structure
  property_count: 3
  slug: salesforce-error-structure
- name: Salesforce Errors Structure
  property_count: 2
  slug: salesforce-errors-structure
- name: Salesforce Errors12 Structure
  property_count: 2
  slug: salesforce-errors12-structure
- name: Salesforce Errors5 Structure
  property_count: 1
  slug: salesforce-errors5-structure
- name: Salesforce Errors7 Structure
  property_count: 3
  slug: salesforce-errors7-structure
- name: Salesforce Expression Set Creation Request Structure
  property_count: 5
  slug: salesforce-expression-set-creation-request-structure
- name: Salesforce Expression Set Invocation Request Structure
  property_count: 2
  slug: salesforce-expression-set-invocation-request-structure
- name: Salesforce Expression Set Update Request Structure
  property_count: 5
  slug: salesforce-expression-set-update-request-structure
- name: Salesforce Extended Details Structure
  property_count: 2
  slug: salesforce-extended-details-structure
- name: Salesforce Extended Error Code Structure
  property_count: 1
  slug: salesforce-extended-error-code-structure
- name: Salesforce Extended Error Details Structure
  property_count: 2
  slug: salesforce-extended-error-details-structure
- name: Salesforce Extended Error Details1 Structure
  property_count: 2
  slug: salesforce-extended-error-details1-structure
- name: Salesforce Extension Structure
  property_count: 31
  slug: salesforce-extension-structure
- name: Salesforce External Credential Structure
  property_count: 11
  slug: salesforce-external-credential-structure
- name: Salesforce External Credential1 Structure
  property_count: 4
  slug: salesforce-external-credential1-structure
- name: Salesforce External Credential2 Structure
  property_count: 1
  slug: salesforce-external-credential2-structure
- name: Salesforce Favorite Structure
  property_count: 11
  slug: salesforce-favorite-structure
- name: Salesforce Favorite1 Structure
  property_count: 2
  slug: salesforce-favorite1-structure
- name: Salesforce Fax Structure
  property_count: 2
  slug: salesforce-fax-structure
- name: Salesforce Fax2 Structure
  property_count: 31
  slug: salesforce-fax2-structure
- name: Salesforce Fax4 Structure
  property_count: 2
  slug: salesforce-fax4-structure
- name: Salesforce Fax5 Structure
  property_count: 2
  slug: salesforce-fax5-structure
- name: Salesforce Federation Identifier Structure
  property_count: 31
  slug: salesforce-federation-identifier-structure
- name: Salesforce Feed Element Structure
  property_count: 2
  slug: salesforce-feed-element-structure
- name: Salesforce Feed Elements Batch Post Request Structure
  property_count: 1
  slug: salesforce-feed-elements-batch-post-request-structure
- name: Salesforce Feed Elements Capability Comments Items Structure
  property_count: 18
  slug: salesforce-feed-elements-capability-comments-items-structure
- name: Salesforce Feed Elements Postand Search Request Structure
  property_count: 4
  slug: salesforce-feed-elements-postand-search-request-structure
- name: Salesforce Feed Enabled Structure
  property_count: 1
  slug: salesforce-feed-enabled-structure
- name: Salesforce Field Mapping List Structure
  property_count: 1
  slug: salesforce-field-mapping-list-structure
- name: Salesforce Field Structure
  property_count: 3
  slug: salesforce-field-structure
- name: Salesforce Field1 Structure
  property_count: 57
  slug: salesforce-field1-structure
- name: Salesforce Field2 Structure
  property_count: 2
  slug: salesforce-field2-structure
- name: Salesforce Field3 Structure
  property_count: 2
  slug: salesforce-field3-structure
- name: Salesforce Field4 Structure
  property_count: 4
  slug: salesforce-field4-structure
- name: Salesforce Field5 Structure
  property_count: 4
  slug: salesforce-field5-structure
- name: Salesforce Field9 Structure
  property_count: 57
  slug: salesforce-field9-structure
- name: Salesforce Fields Structure
  property_count: 2
  slug: salesforce-fields-structure
- name: Salesforce Fields11 Structure
  property_count: 35
  slug: salesforce-fields11-structure
- name: Salesforce Fields15 Structure
  property_count: 70
  slug: salesforce-fields15-structure
- name: Salesforce Fields16 Structure
  property_count: 3
  slug: salesforce-fields16-structure
- name: Salesforce Fields17 Structure
  property_count: 2
  slug: salesforce-fields17-structure
- name: Salesforce Fields18 Structure
  property_count: 17
  slug: salesforce-fields18-structure
- name: Salesforce Fields2 Structure
  property_count: 57
  slug: salesforce-fields2-structure
- name: Salesforce Fields20 Structure
  property_count: 1
  slug: salesforce-fields20-structure
- name: Salesforce Fields21 Structure
  property_count: 42
  slug: salesforce-fields21-structure
- name: Salesforce Fields27 Structure
  property_count: 37
  slug: salesforce-fields27-structure
- name: Salesforce Fields3 Structure
  property_count: 14
  slug: salesforce-fields3-structure
- name: Salesforce Fields31 Structure
  property_count: 36
  slug: salesforce-fields31-structure
- name: Salesforce Fields38 Structure
  property_count: 3
  slug: salesforce-fields38-structure
- name: Salesforce Fields39 Structure
  property_count: 4
  slug: salesforce-fields39-structure
- name: Salesforce Fields4 Structure
  property_count: 60
  slug: salesforce-fields4-structure
- name: Salesforce Fields40 Structure
  property_count: 12
  slug: salesforce-fields40-structure
- name: Salesforce Fields41 Structure
  property_count: 7
  slug: salesforce-fields41-structure
- name: Salesforce Fields5 Structure
  property_count: 18
  slug: salesforce-fields5-structure
- name: Salesforce Fields6 Structure
  property_count: 196
  slug: salesforce-fields6-structure
- name: Salesforce Fields7 Structure
  property_count: 35
  slug: salesforce-fields7-structure
- name: Salesforce Fields8 Structure
  property_count: 2
  slug: salesforce-fields8-structure
- name: Salesforce File Information Structure
  property_count: 48
  slug: salesforce-file-information-structure
- name: Salesforce File Storage Mb Structure
  property_count: 2
  slug: salesforce-file-storage-mb-structure
- name: Salesforce Files Structure
  property_count: 1
  slug: salesforce-files-structure
- name: Salesforce First Name Structure
  property_count: 2
  slug: salesforce-first-name-structure
- name: Salesforce First Name1 Structure
  property_count: 31
  slug: salesforce-first-name1-structure
- name: Salesforce First Name4 Structure
  property_count: 2
  slug: salesforce-first-name4-structure
- name: Salesforce First Transaction Structure
  property_count: 11
  slug: salesforce-first-transaction-structure
- name: Salesforce Flow Interview Structure
  property_count: 6
  slug: salesforce-flow-interview-structure
- name: Salesforce Flow Orchestration Instance Structure
  property_count: 6
  slug: salesforce-flow-orchestration-instance-structure
- name: Salesforce Flow Orchestration Stage Instance Structure
  property_count: 6
  slug: salesforce-flow-orchestration-stage-instance-structure
- name: Salesforce Flow Orchestration Step Instance Structure
  property_count: 6
  slug: salesforce-flow-orchestration-step-instance-structure
- name: Salesforce Flow Orchestration Work Item Structure
  property_count: 6
  slug: salesforce-flow-orchestration-work-item-structure
- name: Salesforce Flows Structure
  property_count: 3
  slug: salesforce-flows-structure
- name: Salesforce Forecast Enabled Structure
  property_count: 31
  slug: salesforce-forecast-enabled-structure
- name: Salesforce Forgot Password Change Password Request Structure
  property_count: 3
  slug: salesforce-forgot-password-change-password-request-structure
- name: Salesforce Forgot Password Initialize Request Structure
  property_count: 2
  slug: salesforce-forgot-password-initialize-request-structure
- name: Salesforce Full Photo Url Structure
  property_count: 31
  slug: salesforce-full-photo-url-structure
- name: Salesforce Full Structure
  property_count: 1
  slug: salesforce-full-structure
- name: Salesforce Generate Open Api Schema Structure
  property_count: 1
  slug: salesforce-generate-open-api-schema-structure
- name: Salesforce Generate Quote Document Api Request Structure
  property_count: 2
  slug: salesforce-generate-quote-document-api-request-structure
- name: Salesforce Generate Response Basedon Prompt Template Structure
  property_count: 5
  slug: salesforce-generate-response-basedon-prompt-template-structure
- name: Salesforce Generated Data Structure
  property_count: 6
  slug: salesforce-generated-data-structure
- name: Salesforce Generation Structure
  property_count: 3
  slug: salesforce-generation-structure
- name: Salesforce Geocode Accuracy Structure
  property_count: 31
  slug: salesforce-geocode-accuracy-structure
- name: Salesforce Get Active Theme Structure
  property_count: 11
  slug: salesforce-get-active-theme-structure
- name: Salesforce Get All Navigation Items Structure
  property_count: 4
  slug: salesforce-get-all-navigation-items-structure
- name: Salesforce Get Appointment Candidates Request Structure
  property_count: 9
  slug: salesforce-get-appointment-candidates-request-structure
- name: Salesforce Get Appointment Slots Request Structure
  property_count: 9
  slug: salesforce-get-appointment-slots-request-structure
- name: Salesforce Get Apps Structure
  property_count: 2
  slug: salesforce-get-apps-structure
- name: Salesforce Get Child Records Structure
  property_count: 8
  slug: salesforce-get-child-records-structure
- name: Salesforce Get Default Valuesto Clonea Record Structure
  property_count: 3
  slug: salesforce-get-default-valuesto-clonea-record-structure
- name: Salesforce Get Default Valuesto Createa Record Structure
  property_count: 3
  slug: salesforce-get-default-valuesto-createa-record-structure
- name: Salesforce Get Favorites Structure
  property_count: 1
  slug: salesforce-get-favorites-structure
- name: Salesforce Get Global Actions Structure
  property_count: 3
  slug: salesforce-get-global-actions-structure
- name: Salesforce Get Last Selected App Structure
  property_count: 18
  slug: salesforce-get-last-selected-app-structure
- name: Salesforce Get Lightning Page Actions Structure
  property_count: 3
  slug: salesforce-get-lightning-page-actions-structure
- name: Salesforce Get List View Chart Actions Structure
  property_count: 3
  slug: salesforce-get-list-view-chart-actions-structure
- name: Salesforce Get List View Header Actions Structure
  property_count: 3
  slug: salesforce-get-list-view-header-actions-structure
- name: Salesforce Get List View Metadataby Api Name Structure
  property_count: 18
  slug: salesforce-get-list-view-metadataby-api-name-structure
- name: Salesforce Get List View Metadataby Id Structure
  property_count: 19
  slug: salesforce-get-list-view-metadataby-id-structure
- name: Salesforce Get List View Record Actions Structure
  property_count: 3
  slug: salesforce-get-list-view-record-actions-structure
- name: Salesforce Get List View Records Request Structure
  property_count: 5
  slug: salesforce-get-list-view-records-request-structure
- name: Salesforce Get List View Records Structure
  property_count: 16
  slug: salesforce-get-list-view-records-structure
- name: Salesforce Get List View Recordsby Id Structure
  property_count: 16
  slug: salesforce-get-list-view-recordsby-id-structure
- name: Salesforce Get List View Recordsper Api Name Structure
  property_count: 16
  slug: salesforce-get-list-view-recordsper-api-name-structure
- name: Salesforce Get List Viewsforan Object Structure
  property_count: 12
  slug: salesforce-get-list-viewsforan-object-structure
- name: Salesforce Get Lookup Field Actions Structure
  property_count: 3
  slug: salesforce-get-lookup-field-actions-structure
- name: Salesforce Get Lookup Field Suggestions Structure
  property_count: 2
  slug: salesforce-get-lookup-field-suggestions-structure
- name: Salesforce Get Lookup Field Suggestionsfora Specified Object Structure
  property_count: 8
  slug: salesforce-get-lookup-field-suggestionsfora-specified-object-structure
- name: Salesforce Get Member Promotions Request Structure
  property_count: 1
  slug: salesforce-get-member-promotions-request-structure
- name: Salesforce Get Mru List View Actions Structure
  property_count: 3
  slug: salesforce-get-mru-list-view-actions-structure
- name: Salesforce Get Object Metadata Structure
  property_count: 23
  slug: salesforce-get-object-metadata-structure
- name: Salesforce Get Parallel Resultsfora Query Job Structure
  property_count: 3
  slug: salesforce-get-parallel-resultsfora-query-job-structure
- name: Salesforce Get Photo Actions Structure
  property_count: 3
  slug: salesforce-get-photo-actions-structure
- name: Salesforce Get Record Dataand Object Metadata Structure
  property_count: 5
  slug: salesforce-get-record-dataand-object-metadata-structure
- name: Salesforce Get Record Detail Page Actions Structure
  property_count: 3
  slug: salesforce-get-record-detail-page-actions-structure
- name: Salesforce Get Record Edit Page Actions Structure
  property_count: 3
  slug: salesforce-get-record-edit-page-actions-structure
- name: Salesforce Get Record Layout Metadata Structure
  property_count: 8
  slug: salesforce-get-record-layout-metadata-structure
- name: Salesforce Get Related List Actions Structure
  property_count: 3
  slug: salesforce-get-related-list-actions-structure
- name: Salesforce Get Related List Record Actions Structure
  property_count: 3
  slug: salesforce-get-related-list-record-actions-structure
- name: Salesforce Get Sandbox Status Structure
  property_count: 6
  slug: salesforce-get-sandbox-status-structure
- name: Salesforce Get Sandbox Structure
  property_count: 17
  slug: salesforce-get-sandbox-structure
- name: Salesforce Get Structure
  property_count: 1
  slug: salesforce-get-structure
- name: Salesforce Get Tooling Describe S Object Structure
  property_count: 45
  slug: salesforce-get-tooling-describe-s-object-structure
- name: Salesforce Get Tooling Describe Structure
  property_count: 3
  slug: salesforce-get-tooling-describe-structure
- name: Salesforce Get Tooling Metadata S Object Structure
  property_count: 2
  slug: salesforce-get-tooling-metadata-s-object-structure
- name: Salesforce Get Valuesfor All Picklist Fieldsofa Record Type Structure
  property_count: 2
  slug: salesforce-get-valuesfor-all-picklist-fieldsofa-record-type-structure
- name: Salesforce Get Valuesfora Picklist Field Structure
  property_count: 5
  slug: salesforce-get-valuesfora-picklist-field-structure
- name: Salesforce Geta Batchof Records Structure
  property_count: 2
  slug: salesforce-geta-batchof-records-structure
- name: Salesforce Geta Directoryof Supported Objects Structure
  property_count: 1
  slug: salesforce-geta-directoryof-supported-objects-structure
- name: Salesforce Geta Favorite Structure
  property_count: 11
  slug: salesforce-geta-favorite-structure
- name: Salesforce Geta Record Structure
  property_count: 11
  slug: salesforce-geta-record-structure
- name: Salesforce Getallmanagedeventsubscriptions Structure
  property_count: 6
  slug: salesforce-getallmanagedeventsubscriptions-structure
- name: Salesforce Getan App Structure
  property_count: 18
  slug: salesforce-getan-app-structure
- name: Salesforce Getchannelmember Structure
  property_count: 18
  slug: salesforce-getchannelmember-structure
- name: Salesforce Getconversationentries Structure
  property_count: 1
  slug: salesforce-getconversationentries-structure
- name: Salesforce Geteventchannel Structure
  property_count: 16
  slug: salesforce-geteventchannel-structure
- name: Salesforce Gettestresults Structure
  property_count: 5
  slug: salesforce-gettestresults-structure
- name: Salesforce Getteststatus Structure
  property_count: 2
  slug: salesforce-getteststatus-structure
- name: Salesforce Gift Commitment Custom Field Structure
  property_count: 2
  slug: salesforce-gift-commitment-custom-field-structure
- name: Salesforce Gift Commitment Schedule Custom Field Structure
  property_count: 2
  slug: salesforce-gift-commitment-schedule-custom-field-structure
- name: Salesforce Gift Structure
  property_count: 20
  slug: salesforce-gift-structure
- name: Salesforce Gift Transaction Custom Field Structure
  property_count: 2
  slug: salesforce-gift-transaction-custom-field-structure
- name: Salesforce Giftcommitment Structure
  property_count: 2
  slug: salesforce-giftcommitment-structure
- name: Salesforce Giftcommitmentschedule Structure
  property_count: 2
  slug: salesforce-giftcommitmentschedule-structure
- name: Salesforce Giftdefaultdesignation Structure
  property_count: 2
  slug: salesforce-giftdefaultdesignation-structure
- name: Salesforce Gifttransaction Structure
  property_count: 2
  slug: salesforce-gifttransaction-structure
- name: Salesforce Gifttransactiondesignation Structure
  property_count: 2
  slug: salesforce-gifttransactiondesignation-structure
- name: Salesforce Global Structure
  property_count: 3
  slug: salesforce-global-structure
- name: Salesforce Graph Response Structure
  property_count: 1
  slug: salesforce-graph-response-structure
- name: Salesforce Graph Structure
  property_count: 2
  slug: salesforce-graph-structure
- name: Salesforce Graph1 Structure
  property_count: 3
  slug: salesforce-graph1-structure
- name: Salesforce Graph2 Structure
  property_count: 2
  slug: salesforce-graph2-structure
- name: Salesforce Graph3 Structure
  property_count: 2
  slug: salesforce-graph3-structure
- name: Salesforce Graph4 Structure
  property_count: 2
  slug: salesforce-graph4-structure
- name: Salesforce Graph5 Structure
  property_count: 2
  slug: salesforce-graph5-structure
- name: Salesforce Group Invites Request Structure
  property_count: 2
  slug: salesforce-group-invites-request-structure
- name: Salesforce Group Members Private Post Structure
  property_count: 8
  slug: salesforce-group-members-private-post-structure
- name: Salesforce Group Structure
  property_count: 25
  slug: salesforce-group-structure
- name: Salesforce Group1 Structure
  property_count: 23
  slug: salesforce-group1-structure
- name: Salesforce Group2 Structure
  property_count: 6
  slug: salesforce-group2-structure
- name: Salesforce Has Subtypes Structure
  property_count: 1
  slug: salesforce-has-subtypes-structure
- name: Salesforce Header Structure
  property_count: 3
  slug: salesforce-header-structure
- name: Salesforce Header4 Structure
  property_count: 1
  slug: salesforce-header4-structure
- name: Salesforce Header5 Structure
  property_count: 1
  slug: salesforce-header5-structure
- name: Salesforce Header8 Structure
  property_count: 1
  slug: salesforce-header8-structure
- name: Salesforce Holiday Structure
  property_count: 6
  slug: salesforce-holiday-structure
- name: Salesforce Home Phone Structure
  property_count: 2
  slug: salesforce-home-phone-structure
- name: Salesforce Hourly Async Report Runs Structure
  property_count: 2
  slug: salesforce-hourly-async-report-runs-structure
- name: Salesforce Hourly Dashboard Refreshes Structure
  property_count: 2
  slug: salesforce-hourly-dashboard-refreshes-structure
- name: Salesforce Hourly Dashboard Results Structure
  property_count: 2
  slug: salesforce-hourly-dashboard-results-structure
- name: Salesforce Hourly Dashboard Statuses Structure
  property_count: 2
  slug: salesforce-hourly-dashboard-statuses-structure
- name: Salesforce Hourly Long Term Id Mapping Structure
  property_count: 2
  slug: salesforce-hourly-long-term-id-mapping-structure
- name: Salesforce Hourly Managed Content Public Requests Structure
  property_count: 2
  slug: salesforce-hourly-managed-content-public-requests-structure
- name: Salesforce Hourly O Data Callout Structure
  property_count: 2
  slug: salesforce-hourly-o-data-callout-structure
- name: Salesforce Hourly Published Platform Events Structure
  property_count: 2
  slug: salesforce-hourly-published-platform-events-structure
- name: Salesforce Hourly Published Standard Volume Platform Events Structure
  property_count: 2
  slug: salesforce-hourly-published-standard-volume-platform-events-structure
- name: Salesforce Hourly Short Term Id Mapping Structure
  property_count: 2
  slug: salesforce-hourly-short-term-id-mapping-structure
- name: Salesforce Hourly Sync Report Runs Structure
  property_count: 2
  slug: salesforce-hourly-sync-report-runs-structure
- name: Salesforce Hourly Time Based Workflow Structure
  property_count: 2
  slug: salesforce-hourly-time-based-workflow-structure
- name: Salesforce Http Headers Structure
  property_count: 1
  slug: salesforce-http-headers-structure
- name: Salesforce Icon Structure
  property_count: 5
  slug: salesforce-icon-structure
- name: Salesforce Id Structure
  property_count: 1
  slug: salesforce-id-structure
- name: Salesforce Id4 Structure
  property_count: 31
  slug: salesforce-id4-structure
- name: Salesforce Id8 Structure
  property_count: 2
  slug: salesforce-id8-structure
- name: Salesforce Image History Structure
  property_count: 6
  slug: salesforce-image-history-structure
- name: Salesforce Image Structure
  property_count: 6
  slug: salesforce-image-structure
- name: Salesforce Implicit Structure
  property_count: 2
  slug: salesforce-implicit-structure
- name: Salesforce Individual History Structure
  property_count: 6
  slug: salesforce-individual-history-structure
- name: Salesforce Individual Id Structure
  property_count: 2
  slug: salesforce-individual-id-structure
- name: Salesforce Individual Id1 Structure
  property_count: 31
  slug: salesforce-individual-id1-structure
- name: Salesforce Individual Member Enrollments Request Structure
  property_count: 11
  slug: salesforce-individual-member-enrollments-request-structure
- name: Salesforce Individual Member Enrollments Structure
  property_count: 5
  slug: salesforce-individual-member-enrollments-structure
- name: Salesforce Individual Structure
  property_count: 6
  slug: salesforce-individual-structure
- name: Salesforce Industry Structure
  property_count: 2
  slug: salesforce-industry-structure
- name: Salesforce Industry1 Structure
  property_count: 31
  slug: salesforce-industry1-structure
- name: Salesforce Industry2 Structure
  property_count: 2
  slug: salesforce-industry2-structure
- name: Salesforce Industry3 Structure
  property_count: 2
  slug: salesforce-industry3-structure
- name: Salesforce Info Structure
  property_count: 3
  slug: salesforce-info-structure
- name: Salesforce Information Structure
  property_count: 2
  slug: salesforce-information-structure
- name: Salesforce Infos Structure
  property_count: 2
  slug: salesforce-infos-structure
- name: Salesforce Initiate Amend Quantity Request Structure
  property_count: 4
  slug: salesforce-initiate-amend-quantity-request-structure
- name: Salesforce Initiate Cancellation Request Structure
  property_count: 3
  slug: salesforce-initiate-cancellation-request-structure
- name: Salesforce Initiate Renewal Request Structure
  property_count: 1
  slug: salesforce-initiate-renewal-request-structure
- name: Salesforce Input Structure
  property_count: 1
  slug: salesforce-input-structure
- name: Salesforce Input1 Structure
  property_count: 1
  slug: salesforce-input1-structure
- name: Salesforce Input2 Structure
  property_count: 2
  slug: salesforce-input2-structure
- name: Salesforce Inputs Structure
  property_count: 3
  slug: salesforce-inputs-structure
- name: Salesforce Inputs1 Structure
  property_count: 1
  slug: salesforce-inputs1-structure
- name: Salesforce Inputs2 Structure
  property_count: 1
  slug: salesforce-inputs2-structure
- name: Salesforce Inputs3 Structure
  property_count: 1
  slug: salesforce-inputs3-structure
- name: Salesforce Interactions Structure
  property_count: 1
  slug: salesforce-interactions-structure
- name: Salesforce Invitees Structure
  property_count: 1
  slug: salesforce-invitees-structure
- name: Salesforce Invoke Request Structure
  property_count: 2
  slug: salesforce-invoke-request-structure
- name: Salesforce Ip Address Range Structure
  property_count: 6
  slug: salesforce-ip-address-range-structure
- name: Salesforce Is Active Structure
  property_count: 31
  slug: salesforce-is-active-structure
- name: Salesforce Is Converted Structure
  property_count: 31
  slug: salesforce-is-converted-structure
- name: Salesforce Is Customer Portal Structure
  property_count: 2
  slug: salesforce-is-customer-portal-structure
- name: Salesforce Is Customer Portal1 Structure
  property_count: 31
  slug: salesforce-is-customer-portal1-structure
- name: Salesforce Is Deleted Structure
  property_count: 2
  slug: salesforce-is-deleted-structure
- name: Salesforce Is Deleted2 Structure
  property_count: 31
  slug: salesforce-is-deleted2-structure
- name: Salesforce Is Email Bounced Structure
  property_count: 2
  slug: salesforce-is-email-bounced-structure
- name: Salesforce Is Ext Indicator Visible Structure
  property_count: 31
  slug: salesforce-is-ext-indicator-visible-structure
- name: Salesforce Is Interface Structure
  property_count: 1
  slug: salesforce-is-interface-structure
- name: Salesforce Is Partner Structure
  property_count: 2
  slug: salesforce-is-partner-structure
- name: Salesforce Is Partner1 Structure
  property_count: 31
  slug: salesforce-is-partner1-structure
- name: Salesforce Is Portal Enabled Structure
  property_count: 31
  slug: salesforce-is-portal-enabled-structure
- name: Salesforce Is Profile Photo Active Structure
  property_count: 31
  slug: salesforce-is-profile-photo-active-structure
- name: Salesforce Is Subtype Structure
  property_count: 1
  slug: salesforce-is-subtype-structure
- name: Salesforce Is Unread By Owner Structure
  property_count: 31
  slug: salesforce-is-unread-by-owner-structure
- name: Salesforce Issuea Voucher Request Structure
  property_count: 1
  slug: salesforce-issuea-voucher-request-structure
- name: Salesforce Item Structure
  property_count: 1
  slug: salesforce-item-structure
- name: Salesforce Items Structure
  property_count: 1
  slug: salesforce-items-structure
- name: Salesforce Items17 Structure
  property_count: 2
  slug: salesforce-items17-structure
- name: Salesforce Items18 Structure
  property_count: 1
  slug: salesforce-items18-structure
- name: Salesforce Items19 Structure
  property_count: 2
  slug: salesforce-items19-structure
- name: Salesforce Items20 Structure
  property_count: 2
  slug: salesforce-items20-structure
- name: Salesforce Items22 Structure
  property_count: 2
  slug: salesforce-items22-structure
- name: Salesforce Items23 Structure
  property_count: 2
  slug: salesforce-items23-structure
- name: Salesforce Jigsaw Company Id Structure
  property_count: 1
  slug: salesforce-jigsaw-company-id-structure
- name: Salesforce Jigsaw Company Id1 Structure
  property_count: 31
  slug: salesforce-jigsaw-company-id1-structure
- name: Salesforce Jigsaw Contact Id Structure
  property_count: 1
  slug: salesforce-jigsaw-contact-id-structure
- name: Salesforce Jigsaw Contact Id1 Structure
  property_count: 31
  slug: salesforce-jigsaw-contact-id1-structure
- name: Salesforce Jigsaw Import Limit Override Structure
  property_count: 31
  slug: salesforce-jigsaw-import-limit-override-structure
- name: Salesforce Jigsaw Structure
  property_count: 2
  slug: salesforce-jigsaw-structure
- name: Salesforce Jigsaw2 Structure
  property_count: 31
  slug: salesforce-jigsaw2-structure
- name: Salesforce Json Structure
  property_count: 3
  slug: salesforce-json-structure
- name: Salesforce Key Prefix Structure
  property_count: 1
  slug: salesforce-key-prefix-structure
- name: Salesforce Key Structure
  property_count: 6
  slug: salesforce-key-structure
- name: Salesforce Label Plural Structure
  property_count: 1
  slug: salesforce-label-plural-structure
- name: Salesforce Label Structure
  property_count: 1
  slug: salesforce-label-structure
- name: Salesforce Language Locale Key Structure
  property_count: 31
  slug: salesforce-language-locale-key-structure
- name: Salesforce Last Activity Date Structure
  property_count: 3
  slug: salesforce-last-activity-date-structure
- name: Salesforce Last Activity Date2 Structure
  property_count: 31
  slug: salesforce-last-activity-date2-structure
- name: Salesforce Last Cu Request Date Structure
  property_count: 2
  slug: salesforce-last-cu-request-date-structure
- name: Salesforce Last Cu Update Date Structure
  property_count: 2
  slug: salesforce-last-cu-update-date-structure
- name: Salesforce Last Edited By Structure
  property_count: 19
  slug: salesforce-last-edited-by-structure
- name: Salesforce Last Login Date Structure
  property_count: 31
  slug: salesforce-last-login-date-structure
- name: Salesforce Last Modified By Id Structure
  property_count: 1
  slug: salesforce-last-modified-by-id-structure
- name: Salesforce Last Modified By Id2 Structure
  property_count: 31
  slug: salesforce-last-modified-by-id2-structure
- name: Salesforce Last Modified By Id5 Structure
  property_count: 2
  slug: salesforce-last-modified-by-id5-structure
- name: Salesforce Last Modified By Structure
  property_count: 3
  slug: salesforce-last-modified-by-structure
- name: Salesforce Last Modified By3 Structure
  property_count: 2
  slug: salesforce-last-modified-by3-structure
- name: Salesforce Last Modified Date Structure
  property_count: 2
  slug: salesforce-last-modified-date-structure
- name: Salesforce Last Modified Date14 Structure
  property_count: 2
  slug: salesforce-last-modified-date14-structure
- name: Salesforce Last Modified Date2 Structure
  property_count: 31
  slug: salesforce-last-modified-date2-structure
- name: Salesforce Last Modified Date5 Structure
  property_count: 2
  slug: salesforce-last-modified-date5-structure
- name: Salesforce Last Name Structure
  property_count: 2
  slug: salesforce-last-name-structure
- name: Salesforce Last Name1 Structure
  property_count: 31
  slug: salesforce-last-name1-structure
- name: Salesforce Last Name4 Structure
  property_count: 2
  slug: salesforce-last-name4-structure
- name: Salesforce Last Password Change Date Structure
  property_count: 31
  slug: salesforce-last-password-change-date-structure
- name: Salesforce Last Referenced Date Structure
  property_count: 3
  slug: salesforce-last-referenced-date-structure
- name: Salesforce Last Referenced Date2 Structure
  property_count: 31
  slug: salesforce-last-referenced-date2-structure
- name: Salesforce Last Viewed Date Structure
  property_count: 3
  slug: salesforce-last-viewed-date-structure
- name: Salesforce Last Viewed Date2 Structure
  property_count: 31
  slug: salesforce-last-viewed-date2-structure
- name: Salesforce Latitude Structure
  property_count: 31
  slug: salesforce-latitude-structure
- name: Salesforce Launch Flow Request Structure
  property_count: 1
  slug: salesforce-launch-flow-request-structure
- name: Salesforce Layout Component Structure
  property_count: 3
  slug: salesforce-layout-component-structure
- name: Salesforce Layout Component1 Structure
  property_count: 5
  slug: salesforce-layout-component1-structure
- name: Salesforce Layout Item Structure
  property_count: 7
  slug: salesforce-layout-item-structure
- name: Salesforce Layout Item1 Structure
  property_count: 7
  slug: salesforce-layout-item1-structure
- name: Salesforce Layout Row Structure
  property_count: 1
  slug: salesforce-layout-row-structure
- name: Salesforce Layout Row1 Structure
  property_count: 1
  slug: salesforce-layout-row1-structure
- name: Salesforce Layout Structure
  property_count: 8
  slug: salesforce-layout-structure
- name: Salesforce Layout User States Structure
  property_count: 1
  slug: salesforce-layout-user-states-structure
- name: Salesforce Layout1 Structure
  property_count: 8
  slug: salesforce-layout1-structure
- name: Salesforce Layoutable Structure
  property_count: 1
  slug: salesforce-layoutable-structure
- name: Salesforce Layouts Structure
  property_count: 1
  slug: salesforce-layouts-structure
- name: Salesforce Lead History Structure
  property_count: 6
  slug: salesforce-lead-history-structure
- name: Salesforce Lead Source Structure
  property_count: 2
  slug: salesforce-lead-source-structure
- name: Salesforce Lead Source1 Structure
  property_count: 31
  slug: salesforce-lead-source1-structure
- name: Salesforce Lead Source2 Structure
  property_count: 2
  slug: salesforce-lead-source2-structure
- name: Salesforce Lead Source4 Structure
  property_count: 5
  slug: salesforce-lead-source4-structure
- name: Salesforce Lead Structure
  property_count: 1
  slug: salesforce-lead-structure
- name: Salesforce Lead1 Structure
  property_count: 23
  slug: salesforce-lead1-structure
- name: Salesforce Lead2 Structure
  property_count: 6
  slug: salesforce-lead2-structure
- name: Salesforce Level C Structure
  property_count: 5
  slug: salesforce-level-c-structure
- name: Salesforce Likes Structure
  property_count: 8
  slug: salesforce-likes-structure
- name: Salesforce Limits Structure
  property_count: 52
  slug: salesforce-limits-structure
- name: Salesforce Links Structure
  property_count: 5
  slug: salesforce-links-structure
- name: Salesforce Links11 Structure
  property_count: 2
  slug: salesforce-links11-structure
- name: Salesforce Links13 Structure
  property_count: 2
  slug: salesforce-links13-structure
- name: Salesforce Links3 Structure
  property_count: 1
  slug: salesforce-links3-structure
- name: Salesforce Links7 Structure
  property_count: 6
  slug: salesforce-links7-structure
- name: Salesforce Links9 Structure
  property_count: 4
  slug: salesforce-links9-structure
- name: Salesforce List Email Structure
  property_count: 6
  slug: salesforce-list-email-structure
- name: Salesforce List Metadata Query Structure
  property_count: 2
  slug: salesforce-list-metadata-query-structure
- name: Salesforce List Metadata Response Structure
  property_count: 1
  slug: salesforce-list-metadata-response-structure
- name: Salesforce List Metadata Structure
  property_count: 2
  slug: salesforce-list-metadata-structure
- name: Salesforce List Reference Structure
  property_count: 4
  slug: salesforce-list-reference-structure
- name: Salesforce List Sandboxes Structure
  property_count: 6
  slug: salesforce-list-sandboxes-structure
- name: Salesforce List Structure
  property_count: 4
  slug: salesforce-list-structure
- name: Salesforce List View Chart Instance Structure
  property_count: 3
  slug: salesforce-list-view-chart-instance-structure
- name: Salesforce Listchannelmembers Structure
  property_count: 6
  slug: salesforce-listchannelmembers-structure
- name: Salesforce Listeventchannels Structure
  property_count: 6
  slug: salesforce-listeventchannels-structure
- name: Salesforce Listnamedcredentials Structure
  property_count: 6
  slug: salesforce-listnamedcredentials-structure
- name: Salesforce Locale Sid Key Structure
  property_count: 31
  slug: salesforce-locale-sid-key-structure
- name: Salesforce Location Structure
  property_count: 2
  slug: salesforce-location-structure
- name: Salesforce Longitude Structure
  property_count: 31
  slug: salesforce-longitude-structure
- name: Salesforce Lookup Results Structure
  property_count: 1
  slug: salesforce-lookup-results-structure
- name: Salesforce Lookup Table Request Structure
  property_count: 2
  slug: salesforce-lookup-table-request-structure
- name: Salesforce Lookup Table Request1 Structure
  property_count: 1
  slug: salesforce-lookup-table-request1-structure
- name: Salesforce Loyalty Program Currency Structure
  property_count: 1
  slug: salesforce-loyalty-program-currency-structure
- name: Salesforce Loyalty Program Structure
  property_count: 1
  slug: salesforce-loyalty-program-structure
- name: Salesforce M200 Structure
  property_count: 2
  slug: salesforce-m200-structure
- name: Salesforce M304 Structure
  property_count: 2
  slug: salesforce-m304-structure
- name: Salesforce Macro History Structure
  property_count: 6
  slug: salesforce-macro-history-structure
- name: Salesforce Macro Structure
  property_count: 6
  slug: salesforce-macro-structure
- name: Salesforce Mailing Address Structure
  property_count: 2
  slug: salesforce-mailing-address-structure
- name: Salesforce Mailing City Structure
  property_count: 2
  slug: salesforce-mailing-city-structure
- name: Salesforce Mailing Country Structure
  property_count: 2
  slug: salesforce-mailing-country-structure
- name: Salesforce Mailing Geocode Accuracy Structure
  property_count: 2
  slug: salesforce-mailing-geocode-accuracy-structure
- name: Salesforce Mailing Geocode Accuracy1 Structure
  property_count: 5
  slug: salesforce-mailing-geocode-accuracy1-structure
- name: Salesforce Mailing Latitude Structure
  property_count: 2
  slug: salesforce-mailing-latitude-structure
- name: Salesforce Mailing Longitude Structure
  property_count: 2
  slug: salesforce-mailing-longitude-structure
- name: Salesforce Mailing Postal Code Structure
  property_count: 2
  slug: salesforce-mailing-postal-code-structure
- name: Salesforce Mailing State Structure
  property_count: 2
  slug: salesforce-mailing-state-structure
- name: Salesforce Mailing Street Structure
  property_count: 2
  slug: salesforce-mailing-street-structure
- name: Salesforce Managed Content Structure
  property_count: 6
  slug: salesforce-managed-content-structure
- name: Salesforce Managed Content Variant Structure
  property_count: 6
  slug: salesforce-managed-content-variant-structure
- name: Salesforce Manager Id Structure
  property_count: 31
  slug: salesforce-manager-id-structure
- name: Salesforce Mass Email Structure
  property_count: 2
  slug: salesforce-mass-email-structure
- name: Salesforce Master Record Id Structure
  property_count: 2
  slug: salesforce-master-record-id-structure
- name: Salesforce Master Record Id2 Structure
  property_count: 31
  slug: salesforce-master-record-id2-structure
- name: Salesforce Match Billing Address C Structure
  property_count: 1
  slug: salesforce-match-billing-address-c-structure
- name: Salesforce Medium Banner Photo Url Structure
  property_count: 31
  slug: salesforce-medium-banner-photo-url-structure
- name: Salesforce Medium Photo Url Structure
  property_count: 31
  slug: salesforce-medium-photo-url-structure
- name: Salesforce Member Benefits Structure
  property_count: 1
  slug: salesforce-member-benefits-structure
- name: Salesforce Member Benefits1 Structure
  property_count: 11
  slug: salesforce-member-benefits1-structure
- name: Salesforce Member Currency Structure
  property_count: 20
  slug: salesforce-member-currency-structure
- name: Salesforce Member Profile Structure
  property_count: 24
  slug: salesforce-member-profile-structure
- name: Salesforce Member Tier Structure
  property_count: 12
  slug: salesforce-member-tier-structure
- name: Salesforce Member Vouchers Structure
  property_count: 2
  slug: salesforce-member-vouchers-structure
- name: Salesforce Merchandise C Structure
  property_count: 6
  slug: salesforce-merchandise-c-structure
- name: Salesforce Merchandising Mix C Structure
  property_count: 6
  slug: salesforce-merchandising-mix-c-structure
- name: Salesforce Mergeable Structure
  property_count: 1
  slug: salesforce-mergeable-structure
- name: Salesforce Message Segment Structure
  property_count: 2
  slug: salesforce-message-segment-structure
- name: Salesforce Message Segment1 Structure
  property_count: 4
  slug: salesforce-message-segment1-structure
- name: Salesforce Message Segment11 Structure
  property_count: 6
  slug: salesforce-message-segment11-structure
- name: Salesforce Message Segment2 Structure
  property_count: 4
  slug: salesforce-message-segment2-structure
- name: Salesforce Message Segment3 Structure
  property_count: 9
  slug: salesforce-message-segment3-structure
- name: Salesforce Message Segment5 Structure
  property_count: 4
  slug: salesforce-message-segment5-structure
- name: Salesforce Message Structure
  property_count: 1
  slug: salesforce-message-structure
- name: Salesforce Metadata Objects Structure
  property_count: 6
  slug: salesforce-metadata-objects-structure
- name: Salesforce Metadata Structure
  property_count: 2
  slug: salesforce-metadata-structure
- name: Salesforce Metadata1 Structure
  property_count: 3
  slug: salesforce-metadata1-structure
- name: Salesforce Metadata10 Structure
  property_count: 4
  slug: salesforce-metadata10-structure
- name: Salesforce Metadata12 Structure
  property_count: 4
  slug: salesforce-metadata12-structure
- name: Salesforce Metadata13 Structure
  property_count: 1
  slug: salesforce-metadata13-structure
- name: Salesforce Metadata14 Structure
  property_count: 2
  slug: salesforce-metadata14-structure
- name: Salesforce Metadata15 Structure
  property_count: 5
  slug: salesforce-metadata15-structure
- name: Salesforce Metadata17 Structure
  property_count: 4
  slug: salesforce-metadata17-structure
- name: Salesforce Metadata18 Structure
  property_count: 1
  slug: salesforce-metadata18-structure
- name: Salesforce Metadata2 Structure
  property_count: 3
  slug: salesforce-metadata2-structure
- name: Salesforce Metadata3 Structure
  property_count: 2
  slug: salesforce-metadata3-structure
- name: Salesforce Metadata6 Structure
  property_count: 3
  slug: salesforce-metadata6-structure
- name: Salesforce Metadata7 Structure
  property_count: 4
  slug: salesforce-metadata7-structure
- name: Salesforce Metadata9 Structure
  property_count: 5
  slug: salesforce-metadata9-structure
- name: Salesforce Method Structure
  property_count: 8
  slug: salesforce-method-structure
- name: Salesforce Mix Item C Structure
  property_count: 6
  slug: salesforce-mix-item-c-structure
- name: Salesforce Mobile Phone Structure
  property_count: 2
  slug: salesforce-mobile-phone-structure
- name: Salesforce Mobile Phone1 Structure
  property_count: 31
  slug: salesforce-mobile-phone1-structure
- name: Salesforce Mobile Phone3 Structure
  property_count: 2
  slug: salesforce-mobile-phone3-structure
- name: Salesforce Mobile Sdk Structure
  property_count: 4
  slug: salesforce-mobile-sdk-structure
- name: Salesforce Model Field Structure
  property_count: 3
  slug: salesforce-model-field-structure
- name: Salesforce Model Structure
  property_count: 1
  slug: salesforce-model-structure
- name: Salesforce Model1 Structure
  property_count: 18
  slug: salesforce-model1-structure
- name: Salesforce Model3 Structure
  property_count: 6
  slug: salesforce-model3-structure
- name: Salesforce Monthly Einstein Discovery Story Creation Structure
  property_count: 2
  slug: salesforce-monthly-einstein-discovery-story-creation-structure
- name: Salesforce Motif Structure
  property_count: 5
  slug: salesforce-motif-structure
- name: Salesforce Mru Enabled Structure
  property_count: 1
  slug: salesforce-mru-enabled-structure
- name: Salesforce Mute Structure
  property_count: 1
  slug: salesforce-mute-structure
- name: Salesforce My Subscription Structure
  property_count: 2
  slug: salesforce-my-subscription-structure
- name: Salesforce Naics Code Structure
  property_count: 2
  slug: salesforce-naics-code-structure
- name: Salesforce Naics Code1 Structure
  property_count: 31
  slug: salesforce-naics-code1-structure
- name: Salesforce Naics Desc Structure
  property_count: 2
  slug: salesforce-naics-desc-structure
- name: Salesforce Naics Desc1 Structure
  property_count: 31
  slug: salesforce-naics-desc1-structure
- name: Salesforce Name Or Alias Structure
  property_count: 31
  slug: salesforce-name-or-alias-structure
- name: Salesforce Name Structure
  property_count: 1
  slug: salesforce-name-structure
- name: Salesforce Name13 Structure
  property_count: 1
  slug: salesforce-name13-structure
- name: Salesforce Name14 Structure
  property_count: 2
  slug: salesforce-name14-structure
- name: Salesforce Name16 Structure
  property_count: 31
  slug: salesforce-name16-structure
- name: Salesforce Name17 Structure
  property_count: 31
  slug: salesforce-name17-structure
- name: Salesforce Name18 Structure
  property_count: 23
  slug: salesforce-name18-structure
- name: Salesforce Name19 Structure
  property_count: 31
  slug: salesforce-name19-structure
- name: Salesforce Name21 Structure
  property_count: 2
  slug: salesforce-name21-structure
- name: Salesforce Name42 Structure
  property_count: 2
  slug: salesforce-name42-structure
- name: Salesforce Named Credential Structure
  property_count: 6
  slug: salesforce-named-credential-structure
- name: Salesforce Namespace Registry History Structure
  property_count: 6
  slug: salesforce-namespace-registry-history-structure
- name: Salesforce Namespace Registry Structure
  property_count: 6
  slug: salesforce-namespace-registry-structure
- name: Salesforce Nav Item Structure
  property_count: 15
  slug: salesforce-nav-item-structure
- name: Salesforce Nav Item2 Structure
  property_count: 15
  slug: salesforce-nav-item2-structure
- name: Salesforce Nav Item3 Structure
  property_count: 15
  slug: salesforce-nav-item3-structure
- name: Salesforce Nav Item5 Structure
  property_count: 15
  slug: salesforce-nav-item5-structure
- name: Salesforce Nav Item6 Structure
  property_count: 15
  slug: salesforce-nav-item6-structure
- name: Salesforce Node Structure
  property_count: 2
  slug: salesforce-node-structure
- name: Salesforce Node10 Structure
  property_count: 4
  slug: salesforce-node10-structure
- name: Salesforce Node6 Structure
  property_count: 3
  slug: salesforce-node6-structure
- name: Salesforce Node7 Structure
  property_count: 5
  slug: salesforce-node7-structure
- name: Salesforce Note Structure
  property_count: 6
  slug: salesforce-note-structure
- name: Salesforce Number Of Contacts C Structure
  property_count: 1
  slug: salesforce-number-of-contacts-c-structure
- name: Salesforce Number Of Employees Structure
  property_count: 2
  slug: salesforce-number-of-employees-structure
- name: Salesforce Number Of Employees1 Structure
  property_count: 31
  slug: salesforce-number-of-employees1-structure
- name: Salesforce Number Of Employees2 Structure
  property_count: 2
  slug: salesforce-number-of-employees2-structure
- name: Salesforce Number Of Employees7 Structure
  property_count: 2
  slug: salesforce-number-of-employees7-structure
- name: Salesforce Number Of Failed Logins Structure
  property_count: 31
  slug: salesforce-number-of-failed-logins-structure
- name: Salesforce Numberof Locations C Structure
  property_count: 1
  slug: salesforce-numberof-locations-c-structure
- name: Salesforce Numberof Locations C1 Structure
  property_count: 31
  slug: salesforce-numberof-locations-c1-structure
- name: Salesforce Numberof Locations C2 Structure
  property_count: 2
  slug: salesforce-numberof-locations-c2-structure
- name: Salesforce Numberof Locations C5 Structure
  property_count: 2
  slug: salesforce-numberof-locations-c5-structure
- name: Salesforce O Auth2 Structure
  property_count: 3
  slug: salesforce-o-auth2-structure
- name: Salesforce Object Describe Structure
  property_count: 2
  slug: salesforce-object-describe-structure
- name: Salesforce Object Describe1 Structure
  property_count: 28
  slug: salesforce-object-describe1-structure
- name: Salesforce Object Infos Structure
  property_count: 4
  slug: salesforce-object-infos-structure
- name: Salesforce Object Infos1 Structure
  property_count: 2
  slug: salesforce-object-infos1-structure
- name: Salesforce Objects Structure
  property_count: 172
  slug: salesforce-objects-structure
- name: Salesforce Offline Pda Trial Expiration Date Structure
  property_count: 31
  slug: salesforce-offline-pda-trial-expiration-date-structure
- name: Salesforce Offline Trial Expiration Date Structure
  property_count: 31
  slug: salesforce-offline-trial-expiration-date-structure
- name: Salesforce Open Id Connect Discovery Structure
  property_count: 2
  slug: salesforce-open-id-connect-discovery-structure
- name: Salesforce Open Id Connect Dynamic Client Registration Endpoint Request Structure
  property_count: 6
  slug: salesforce-open-id-connect-dynamic-client-registration-endpoint-request-structure
- name: Salesforce Opportunities Closing Soon Explicit And Structure
  property_count: 2
  slug: salesforce-opportunities-closing-soon-explicit-and-structure
- name: Salesforce Opportunities Closing Soon Structure
  property_count: 2
  slug: salesforce-opportunities-closing-soon-structure
- name: Salesforce Opportunities Early Stage Structure
  property_count: 2
  slug: salesforce-opportunities-early-stage-structure
- name: Salesforce Opportunities Not Closed Structure
  property_count: 2
  slug: salesforce-opportunities-not-closed-structure
- name: Salesforce Opportunity Contact Role Structure
  property_count: 6
  slug: salesforce-opportunity-contact-role-structure
- name: Salesforce Opportunity Field History Structure
  property_count: 6
  slug: salesforce-opportunity-field-history-structure
- name: Salesforce Opportunity History Structure
  property_count: 6
  slug: salesforce-opportunity-history-structure
- name: Salesforce Opportunity Line Item Structure
  property_count: 6
  slug: salesforce-opportunity-line-item-structure
- name: Salesforce Opportunity Partner Structure
  property_count: 6
  slug: salesforce-opportunity-partner-structure
- name: Salesforce Opportunity Structure
  property_count: 1
  slug: salesforce-opportunity-structure
- name: Salesforce Opportunity3 Structure
  property_count: 1
  slug: salesforce-opportunity3-structure
- name: Salesforce Opportunity4 Structure
  property_count: 6
  slug: salesforce-opportunity4-structure
- name: Salesforce Opt Outfroma Promotion Request Structure
  property_count: 1
  slug: salesforce-opt-outfroma-promotion-request-structure
- name: Salesforce Order History Structure
  property_count: 6
  slug: salesforce-order-history-structure
- name: Salesforce Order Item History Structure
  property_count: 6
  slug: salesforce-order-item-history-structure
- name: Salesforce Order Item Structure
  property_count: 6
  slug: salesforce-order-item-structure
- name: Salesforce Order Structure
  property_count: 6
  slug: salesforce-order-structure
- name: Salesforce Ordered By Info Structure
  property_count: 3
  slug: salesforce-ordered-by-info-structure
- name: Salesforce Org Metric Scan Result Structure
  property_count: 6
  slug: salesforce-org-metric-scan-result-structure
- name: Salesforce Org Metric Scan Summary Structure
  property_count: 6
  slug: salesforce-org-metric-scan-summary-structure
- name: Salesforce Org Metric Structure
  property_count: 6
  slug: salesforce-org-metric-structure
- name: Salesforce Organization Structure
  property_count: 6
  slug: salesforce-organization-structure
- name: Salesforce Other Address Structure
  property_count: 2
  slug: salesforce-other-address-structure
- name: Salesforce Other City Structure
  property_count: 2
  slug: salesforce-other-city-structure
- name: Salesforce Other Country Structure
  property_count: 2
  slug: salesforce-other-country-structure
- name: Salesforce Other Geocode Accuracy Structure
  property_count: 2
  slug: salesforce-other-geocode-accuracy-structure
- name: Salesforce Other Geocode Accuracy1 Structure
  property_count: 5
  slug: salesforce-other-geocode-accuracy1-structure
- name: Salesforce Other Latitude Structure
  property_count: 2
  slug: salesforce-other-latitude-structure
- name: Salesforce Other Longitude Structure
  property_count: 2
  slug: salesforce-other-longitude-structure
- name: Salesforce Other Phone Structure
  property_count: 2
  slug: salesforce-other-phone-structure
- name: Salesforce Other Postal Code Structure
  property_count: 2
  slug: salesforce-other-postal-code-structure
- name: Salesforce Other State Structure
  property_count: 2
  slug: salesforce-other-state-structure
- name: Salesforce Other Street Structure
  property_count: 2
  slug: salesforce-other-street-structure
- name: Salesforce Out Of Office Message Structure
  property_count: 31
  slug: salesforce-out-of-office-message-structure
- name: Salesforce Out Of Office Structure
  property_count: 1
  slug: salesforce-out-of-office-structure
- name: Salesforce Outcome Structure
  property_count: 3
  slug: salesforce-outcome-structure
- name: Salesforce Output Parameters Structure
  property_count: 1
  slug: salesforce-output-parameters-structure
- name: Salesforce Output Parameters1 Structure
  property_count: 1
  slug: salesforce-output-parameters1-structure
- name: Salesforce Output Parameters2 Structure
  property_count: 1
  slug: salesforce-output-parameters2-structure
- name: Salesforce Output Parameters3 Structure
  property_count: 1
  slug: salesforce-output-parameters3-structure
- name: Salesforce Output Structure
  property_count: 1
  slug: salesforce-output-structure
- name: Salesforce Output Values Structure
  property_count: 1
  slug: salesforce-output-values-structure
- name: Salesforce Output Values1 Structure
  property_count: 1
  slug: salesforce-output-values1-structure
- name: Salesforce Output1 Structure
  property_count: 2
  slug: salesforce-output1-structure
- name: Salesforce Output2 Structure
  property_count: 1
  slug: salesforce-output2-structure
- name: Salesforce Output4 Structure
  property_count: 5
  slug: salesforce-output4-structure
- name: Salesforce Outreach Source Code Structure
  property_count: 2
  slug: salesforce-outreach-source-code-structure
- name: Salesforce Owner Id Structure
  property_count: 2
  slug: salesforce-owner-id-structure
- name: Salesforce Owner Id2 Structure
  property_count: 31
  slug: salesforce-owner-id2-structure
- name: Salesforce Owner Id4 Structure
  property_count: 2
  slug: salesforce-owner-id4-structure
- name: Salesforce Owner Structure
  property_count: 19
  slug: salesforce-owner-structure
- name: Salesforce Owner11 Structure
  property_count: 2
  slug: salesforce-owner11-structure
- name: Salesforce Owner4 Structure
  property_count: 2
  slug: salesforce-owner4-structure
- name: Salesforce Owner6 Structure
  property_count: 2
  slug: salesforce-owner6-structure
- name: Salesforce Ownership Structure
  property_count: 2
  slug: salesforce-ownership-structure
- name: Salesforce Ownership1 Structure
  property_count: 31
  slug: salesforce-ownership1-structure
- name: Salesforce Ownership2 Structure
  property_count: 2
  slug: salesforce-ownership2-structure
- name: Salesforce Ownership4 Structure
  property_count: 2
  slug: salesforce-ownership4-structure
- name: Salesforce Package2 Version Creates Structure
  property_count: 2
  slug: salesforce-package2-version-creates-structure
- name: Salesforce Package2 Version Creates Without Validation Structure
  property_count: 2
  slug: salesforce-package2-version-creates-without-validation-structure
- name: Salesforce Page Info Structure
  property_count: 4
  slug: salesforce-page-info-structure
- name: Salesforce Page Reference Structure
  property_count: 3
  slug: salesforce-page-reference-structure
- name: Salesforce Page Reference6 Structure
  property_count: 3
  slug: salesforce-page-reference6-structure
- name: Salesforce Page Structure
  property_count: 8
  slug: salesforce-page-structure
- name: Salesforce Page1 Structure
  property_count: 8
  slug: salesforce-page1-structure
- name: Salesforce Parameter Structure
  property_count: 4
  slug: salesforce-parameter-structure
- name: Salesforce Parameter1 Structure
  property_count: 5
  slug: salesforce-parameter1-structure
- name: Salesforce Parameter4 Structure
  property_count: 5
  slug: salesforce-parameter4-structure
- name: Salesforce Parameter5 Structure
  property_count: 2
  slug: salesforce-parameter5-structure
- name: Salesforce Parent Id Structure
  property_count: 2
  slug: salesforce-parent-id-structure
- name: Salesforce Parent Id1 Structure
  property_count: 31
  slug: salesforce-parent-id1-structure
- name: Salesforce Parent Id2 Structure
  property_count: 2
  slug: salesforce-parent-id2-structure
- name: Salesforce Parent Structure
  property_count: 7
  slug: salesforce-parent-structure
- name: Salesforce Parent2 Structure
  property_count: 20
  slug: salesforce-parent2-structure
- name: Salesforce Parent4 Structure
  property_count: 2
  slug: salesforce-parent4-structure
- name: Salesforce Parent7 Structure
  property_count: 2
  slug: salesforce-parent7-structure
- name: Salesforce Partner Fund Allocation History Structure
  property_count: 6
  slug: salesforce-partner-fund-allocation-history-structure
- name: Salesforce Partner Fund Allocation Structure
  property_count: 6
  slug: salesforce-partner-fund-allocation-structure
- name: Salesforce Partner Fund Claim History Structure
  property_count: 6
  slug: salesforce-partner-fund-claim-history-structure
- name: Salesforce Partner Fund Claim Structure
  property_count: 6
  slug: salesforce-partner-fund-claim-structure
- name: Salesforce Partner Fund Request History Structure
  property_count: 6
  slug: salesforce-partner-fund-request-history-structure
- name: Salesforce Partner Fund Request Structure
  property_count: 6
  slug: salesforce-partner-fund-request-structure
- name: Salesforce Partner Marketing Budget History Structure
  property_count: 6
  slug: salesforce-partner-marketing-budget-history-structure
- name: Salesforce Partner Marketing Budget Structure
  property_count: 6
  slug: salesforce-partner-marketing-budget-structure
- name: Salesforce Partner Structure
  property_count: 6
  slug: salesforce-partner-structure
- name: Salesforce Party Consent History Structure
  property_count: 6
  slug: salesforce-party-consent-history-structure
- name: Salesforce Party Consent Structure
  property_count: 6
  slug: salesforce-party-consent-structure
- name: Salesforce Password Structure
  property_count: 2
  slug: salesforce-password-structure
- name: Salesforce Passwordless Login Initialize Request Structure
  property_count: 3
  slug: salesforce-passwordless-login-initialize-request-structure
- name: Salesforce Paths Structure
  property_count: 1
  slug: salesforce-paths-structure
- name: Salesforce Payment Instrument Structure
  property_count: 16
  slug: salesforce-payment-instrument-structure
- name: Salesforce Paymentinstrument1 Structure
  property_count: 2
  slug: salesforce-paymentinstrument1-structure
- name: Salesforce Period Structure
  property_count: 6
  slug: salesforce-period-structure
- name: Salesforce Permission Sets Structure
  property_count: 3
  slug: salesforce-permission-sets-structure
- name: Salesforce Phone Structure
  property_count: 2
  slug: salesforce-phone-structure
- name: Salesforce Phone2 Structure
  property_count: 31
  slug: salesforce-phone2-structure
- name: Salesforce Phone5 Structure
  property_count: 2
  slug: salesforce-phone5-structure
- name: Salesforce Phone9 Structure
  property_count: 2
  slug: salesforce-phone9-structure
- name: Salesforce Photo Structure
  property_count: 7
  slug: salesforce-photo-structure
- name: Salesforce Photo Url Structure
  property_count: 2
  slug: salesforce-photo-url-structure
- name: Salesforce Photo Url2 Structure
  property_count: 31
  slug: salesforce-photo-url2-structure
- name: Salesforce Photo Url4 Structure
  property_count: 2
  slug: salesforce-photo-url4-structure
- name: Salesforce Photo15 Structure
  property_count: 7
  slug: salesforce-photo15-structure
- name: Salesforce Photos Structure
  property_count: 2
  slug: salesforce-photos-structure
- name: Salesforce Picklist Field Values Structure
  property_count: 6
  slug: salesforce-picklist-field-values-structure
- name: Salesforce Picklist Value Structure
  property_count: 5
  slug: salesforce-picklist-value-structure
- name: Salesforce Picklist Value1 Structure
  property_count: 5
  slug: salesforce-picklist-value1-structure
- name: Salesforce Picklist Value2 Structure
  property_count: 5
  slug: salesforce-picklist-value2-structure
- name: Salesforce Picklist Value31 Structure
  property_count: 5
  slug: salesforce-picklist-value31-structure
- name: Salesforce Platform Event Schemaby Event Name Structure
  property_count: 4
  slug: salesforce-platform-event-schemaby-event-name-structure
- name: Salesforce Portal Role Structure
  property_count: 31
  slug: salesforce-portal-role-structure
- name: Salesforce Post Structure
  property_count: 3
  slug: salesforce-post-structure
- name: Salesforce Post Tooling S Object Request Structure
  property_count: 1
  slug: salesforce-post-tooling-s-object-request-structure
- name: Salesforce Postal Code Structure
  property_count: 31
  slug: salesforce-postal-code-structure
- name: Salesforce Postal Code2 Structure
  property_count: 2
  slug: salesforce-postal-code2-structure
- name: Salesforce Postal Code3 Structure
  property_count: 2
  slug: salesforce-postal-code3-structure
- name: Salesforce Potential Value C Structure
  property_count: 1
  slug: salesforce-potential-value-c-structure
- name: Salesforce Predict Request Structure
  property_count: 4
  slug: salesforce-predict-request-structure
- name: Salesforce Predict Structure
  property_count: 3
  slug: salesforce-predict-structure
- name: Salesforce Prediction Definitions1 Structure
  property_count: 14
  slug: salesforce-prediction-definitions1-structure
- name: Salesforce Prediction Structure
  property_count: 4
  slug: salesforce-prediction-structure
- name: Salesforce Prediction1 Structure
  property_count: 2
  slug: salesforce-prediction1-structure
- name: Salesforce Predictiondefinitionmetadata Structure
  property_count: 14
  slug: salesforce-predictiondefinitionmetadata-structure
- name: Salesforce Predictiondefinitions Structure
  property_count: 4
  slug: salesforce-predictiondefinitions-structure
- name: Salesforce Predictionmodels Structure
  property_count: 3
  slug: salesforce-predictionmodels-structure
- name: Salesforce Prescribable Field Structure
  property_count: 2
  slug: salesforce-prescribable-field-structure
- name: Salesforce Pricebook Entry History Structure
  property_count: 6
  slug: salesforce-pricebook-entry-history-structure
- name: Salesforce Pricebook Entry Structure
  property_count: 6
  slug: salesforce-pricebook-entry-structure
- name: Salesforce Pricebook2 History Structure
  property_count: 6
  slug: salesforce-pricebook2-history-structure
- name: Salesforce Pricebook2 Structure
  property_count: 6
  slug: salesforce-pricebook2-structure
- name: Salesforce Primary C Structure
  property_count: 31
  slug: salesforce-primary-c-structure
- name: Salesforce Primary C1 Structure
  property_count: 2
  slug: salesforce-primary-c1-structure
- name: Salesforce Principal Structure
  property_count: 3
  slug: salesforce-principal-structure
- name: Salesforce Principal1 Structure
  property_count: 7
  slug: salesforce-principal1-structure
- name: Salesforce Private Connect Outbound Callout Hourly Limit Mb Structure
  property_count: 2
  slug: salesforce-private-connect-outbound-callout-hourly-limit-mb-structure
- name: Salesforce Process Approvals Submit Request Structure
  property_count: 7
  slug: salesforce-process-approvals-submit-request-structure
- name: Salesforce Process Definition Structure
  property_count: 6
  slug: salesforce-process-definition-structure
- name: Salesforce Process Instance Structure
  property_count: 6
  slug: salesforce-process-instance-structure
- name: Salesforce Process Parameter Structure
  property_count: 2
  slug: salesforce-process-parameter-structure
- name: Salesforce Process Parameter1 Structure
  property_count: 2
  slug: salesforce-process-parameter1-structure
- name: Salesforce Process Parameter2 Structure
  property_count: 2
  slug: salesforce-process-parameter2-structure
- name: Salesforce Process Parameter3 Structure
  property_count: 2
  slug: salesforce-process-parameter3-structure
- name: Salesforce Process Parameter4 Structure
  property_count: 1
  slug: salesforce-process-parameter4-structure
- name: Salesforce Process Parameter5 Structure
  property_count: 4
  slug: salesforce-process-parameter5-structure
- name: Salesforce Process Parameter7 Structure
  property_count: 2
  slug: salesforce-process-parameter7-structure
- name: Salesforce Process Parameter8 Structure
  property_count: 5
  slug: salesforce-process-parameter8-structure
- name: Salesforce Process Parameter9 Structure
  property_count: 3
  slug: salesforce-process-parameter9-structure
- name: Salesforce Processing Options Structure
  property_count: 1
  slug: salesforce-processing-options-structure
- name: Salesforce Product Consumption Schedule Structure
  property_count: 6
  slug: salesforce-product-consumption-schedule-structure
- name: Salesforce Product Context Structure
  property_count: 2
  slug: salesforce-product-context-structure
- name: Salesforce Product Context1 Structure
  property_count: 1
  slug: salesforce-product-context1-structure
- name: Salesforce Product Interest C Structure
  property_count: 31
  slug: salesforce-product-interest-c-structure
- name: Salesforce Product Interest C1 Structure
  property_count: 2
  slug: salesforce-product-interest-c1-structure
- name: Salesforce Product2 History Structure
  property_count: 6
  slug: salesforce-product2-history-structure
- name: Salesforce Product2 Structure
  property_count: 6
  slug: salesforce-product2-structure
- name: Salesforce Profile Id Structure
  property_count: 31
  slug: salesforce-profile-id-structure
- name: Salesforce Profile Photo Id Structure
  property_count: 31
  slug: salesforce-profile-photo-id-structure
- name: Salesforce Profile Skill Endorsement History Structure
  property_count: 6
  slug: salesforce-profile-skill-endorsement-history-structure
- name: Salesforce Profile Skill Endorsement Structure
  property_count: 6
  slug: salesforce-profile-skill-endorsement-structure
- name: Salesforce Profile Skill History Structure
  property_count: 6
  slug: salesforce-profile-skill-history-structure
- name: Salesforce Profile Skill Structure
  property_count: 6
  slug: salesforce-profile-skill-structure
- name: Salesforce Profile Skill User History Structure
  property_count: 6
  slug: salesforce-profile-skill-user-history-structure
- name: Salesforce Profile Skill User Structure
  property_count: 6
  slug: salesforce-profile-skill-user-structure
- name: Salesforce Promotion Eligibility Structure
  property_count: 6
  slug: salesforce-promotion-eligibility-structure
- name: Salesforce Promotion Limits Structure
  property_count: 8
  slug: salesforce-promotion-limits-structure
- name: Salesforce Promotions Creation Request Structure
  property_count: 11
  slug: salesforce-promotions-creation-request-structure
- name: Salesforce Properties Structure
  property_count: 2
  slug: salesforce-properties-structure
- name: Salesforce Properties1 Structure
  property_count: 29
  slug: salesforce-properties1-structure
- name: Salesforce Properties10 Structure
  property_count: 3
  slug: salesforce-properties10-structure
- name: Salesforce Properties12 Structure
  property_count: 60
  slug: salesforce-properties12-structure
- name: Salesforce Properties2 Structure
  property_count: 1
  slug: salesforce-properties2-structure
- name: Salesforce Properties3 Structure
  property_count: 2
  slug: salesforce-properties3-structure
- name: Salesforce Properties4 Structure
  property_count: 74
  slug: salesforce-properties4-structure
- name: Salesforce Properties5 Structure
  property_count: 2
  slug: salesforce-properties5-structure
- name: Salesforce Properties6 Structure
  property_count: 4
  slug: salesforce-properties6-structure
- name: Salesforce Properties7 Structure
  property_count: 1
  slug: salesforce-properties7-structure
- name: Salesforce Properties8 Structure
  property_count: 5
  slug: salesforce-properties8-structure
- name: Salesforce Properties9 Structure
  property_count: 4
  slug: salesforce-properties9-structure
- name: Salesforce Publish Callback Usage In Apex Structure
  property_count: 2
  slug: salesforce-publish-callback-usage-in-apex-structure
- name: Salesforce Publishmultipleevents Request Structure
  property_count: 2
  slug: salesforce-publishmultipleevents-request-structure
- name: Salesforce Publishsingleevent Request Structure
  property_count: 3
  slug: salesforce-publishsingleevent-request-structure
- name: Salesforce Publishsingleevent Structure
  property_count: 3
  slug: salesforce-publishsingleevent-structure
- name: Salesforce Query All Structure
  property_count: 3
  slug: salesforce-query-all-structure
- name: Salesforce Query Structure
  property_count: 1
  slug: salesforce-query-structure
- name: Salesforce Query10 Structure
  property_count: 1
  slug: salesforce-query10-structure
- name: Salesforce Query11 Structure
  property_count: 3
  slug: salesforce-query11-structure
- name: Salesforce Query3 Structure
  property_count: 1
  slug: salesforce-query3-structure
- name: Salesforce Query4 Structure
  property_count: 1
  slug: salesforce-query4-structure
- name: Salesforce Query6 Structure
  property_count: 1
  slug: salesforce-query6-structure
- name: Salesforce Query7 Structure
  property_count: 1
  slug: salesforce-query7-structure
- name: Salesforce Queryable Structure
  property_count: 1
  slug: salesforce-queryable-structure
- name: Salesforce Quick Text History Structure
  property_count: 6
  slug: salesforce-quick-text-history-structure
- name: Salesforce Quick Text Structure
  property_count: 6
  slug: salesforce-quick-text-structure
- name: Salesforce Quote Term Reader Api Request Structure
  property_count: 1
  slug: salesforce-quote-term-reader-api-request-structure
- name: Salesforce Rating Structure
  property_count: 2
  slug: salesforce-rating-structure
- name: Salesforce Rating1 Structure
  property_count: 31
  slug: salesforce-rating1-structure
- name: Salesforce Rating2 Structure
  property_count: 2
  slug: salesforce-rating2-structure
- name: Salesforce Rating3 Structure
  property_count: 2
  slug: salesforce-rating3-structure
- name: Salesforce Read By Structure
  property_count: 3
  slug: salesforce-read-by-structure
- name: Salesforce Read Product Api Request Structure
  property_count: 1
  slug: salesforce-read-product-api-request-structure
- name: Salesforce Receives Admin Info Emails Structure
  property_count: 31
  slug: salesforce-receives-admin-info-emails-structure
- name: Salesforce Receives Info Emails Structure
  property_count: 31
  slug: salesforce-receives-info-emails-structure
- name: Salesforce Recent Items Structure
  property_count: 2
  slug: salesforce-recent-items-structure
- name: Salesforce Recipient Structure
  property_count: 19
  slug: salesforce-recipient-structure
- name: Salesforce Recommendation Structure
  property_count: 6
  slug: salesforce-recommendation-structure
- name: Salesforce Record Action Structure
  property_count: 6
  slug: salesforce-record-action-structure
- name: Salesforce Record Count Structure
  property_count: 1
  slug: salesforce-record-count-structure
- name: Salesforce Record Structure
  property_count: 11
  slug: salesforce-record-structure
- name: Salesforce Record Type Id Structure
  property_count: 31
  slug: salesforce-record-type-id-structure
- name: Salesforce Record Type Info Structure
  property_count: 8
  slug: salesforce-record-type-info-structure
- name: Salesforce Record Type Infos Structure
  property_count: 1
  slug: salesforce-record-type-infos-structure
- name: Salesforce Record Type Structure
  property_count: 6
  slug: salesforce-record-type-structure
- name: Salesforce Record10 Structure
  property_count: 6
  slug: salesforce-record10-structure
- name: Salesforce Record11 Structure
  property_count: 20
  slug: salesforce-record11-structure
- name: Salesforce Record12 Structure
  property_count: 14
  slug: salesforce-record12-structure
- name: Salesforce Record13 Structure
  property_count: 2
  slug: salesforce-record13-structure
- name: Salesforce Record14 Structure
  property_count: 70
  slug: salesforce-record14-structure
- name: Salesforce Record15 Structure
  property_count: 2
  slug: salesforce-record15-structure
- name: Salesforce Record16 Structure
  property_count: 2
  slug: salesforce-record16-structure
- name: Salesforce Record17 Structure
  property_count: 9
  slug: salesforce-record17-structure
- name: Salesforce Record18 Structure
  property_count: 2
  slug: salesforce-record18-structure
- name: Salesforce Record19 Structure
  property_count: 13
  slug: salesforce-record19-structure
- name: Salesforce Record2 Structure
  property_count: 8
  slug: salesforce-record2-structure
- name: Salesforce Record20 Structure
  property_count: 2
  slug: salesforce-record20-structure
- name: Salesforce Record21 Structure
  property_count: 14
  slug: salesforce-record21-structure
- name: Salesforce Record22 Structure
  property_count: 2
  slug: salesforce-record22-structure
- name: Salesforce Record23 Structure
  property_count: 13
  slug: salesforce-record23-structure
- name: Salesforce Record24 Structure
  property_count: 5
  slug: salesforce-record24-structure
- name: Salesforce Record25 Structure
  property_count: 4
  slug: salesforce-record25-structure
- name: Salesforce Record27 Structure
  property_count: 11
  slug: salesforce-record27-structure
- name: Salesforce Record28 Structure
  property_count: 11
  slug: salesforce-record28-structure
- name: Salesforce Record3 Structure
  property_count: 4
  slug: salesforce-record3-structure
- name: Salesforce Record4 Structure
  property_count: 6
  slug: salesforce-record4-structure
- name: Salesforce Record5 Structure
  property_count: 5
  slug: salesforce-record5-structure
- name: Salesforce Record6 Structure
  property_count: 3
  slug: salesforce-record6-structure
- name: Salesforce Record7 Structure
  property_count: 3
  slug: salesforce-record7-structure
- name: Salesforce Record8 Structure
  property_count: 19
  slug: salesforce-record8-structure
- name: Salesforce Record9 Structure
  property_count: 5
  slug: salesforce-record9-structure
- name: Salesforce Records Structure
  property_count: 2
  slug: salesforce-records-structure
- name: Salesforce Records1 Structure
  property_count: 11
  slug: salesforce-records1-structure
- name: Salesforce Records2 Structure
  property_count: 11
  slug: salesforce-records2-structure
- name: Salesforce Records3 Structure
  property_count: 11
  slug: salesforce-records3-structure
- name: Salesforce Records4 Structure
  property_count: 10
  slug: salesforce-records4-structure
- name: Salesforce Redeem Voucher Request Structure
  property_count: 2
  slug: salesforce-redeem-voucher-request-structure
- name: Salesforce Redeem Voucher Structure
  property_count: 2
  slug: salesforce-redeem-voucher-structure
- name: Salesforce Reference Structure
  property_count: 2
  slug: salesforce-reference-structure
- name: Salesforce Reference To Info Structure
  property_count: 2
  slug: salesforce-reference-to-info-structure
- name: Salesforce Refresh Sandbox Request Structure
  property_count: 2
  slug: salesforce-refresh-sandbox-request-structure
- name: Salesforce Region C Structure
  property_count: 1
  slug: salesforce-region-c-structure
- name: Salesforce Registration Initialize Request Structure
  property_count: 5
  slug: salesforce-registration-initialize-request-structure
- name: Salesforce Related Id Structure
  property_count: 31
  slug: salesforce-related-id-structure
- name: Salesforce Related Named Credential Structure
  property_count: 4
  slug: salesforce-related-named-credential-structure
- name: Salesforce Renewed Contract Structure
  property_count: 2
  slug: salesforce-renewed-contract-structure
- name: Salesforce Replicateable Structure
  property_count: 1
  slug: salesforce-replicateable-structure
- name: Salesforce Report Anomaly Event Store Structure
  property_count: 6
  slug: salesforce-report-anomaly-event-store-structure
- name: Salesforce Report Structure
  property_count: 6
  slug: salesforce-report-structure
- name: Salesforce Reports To Id Structure
  property_count: 2
  slug: salesforce-reports-to-id-structure
- name: Salesforce Request Body Structure
  property_count: 1
  slug: salesforce-request-body-structure
- name: Salesforce Request Product Information Bundled Components Request Structure
  property_count: 2
  slug: salesforce-request-product-information-bundled-components-request-structure
- name: Salesforce Request Product Information No Bundles Request Structure
  property_count: 3
  slug: salesforce-request-product-information-no-bundles-request-structure
- name: Salesforce Request Structure
  property_count: 8
  slug: salesforce-request-structure
- name: Salesforce Requested Group Structure
  property_count: 2
  slug: salesforce-requested-group-structure
- name: Salesforce Resourcesby Version Structure
  property_count: 48
  slug: salesforce-resourcesby-version-structure
- name: Salesforce Rest Api Error Structure
  property_count: 2
  slug: salesforce-rest-api-error-structure
- name: Salesforce Rest Api Version Structure
  property_count: 3
  slug: salesforce-rest-api-version-structure
- name: Salesforce Rest Composite Request Structure
  property_count: 3
  slug: salesforce-rest-composite-request-structure
- name: Salesforce Rest Composite Response Structure
  property_count: 1
  slug: salesforce-rest-composite-response-structure
- name: Salesforce Rest Error Structure
  property_count: 3
  slug: salesforce-rest-error-structure
- name: Salesforce Rest Query Result Structure
  property_count: 4
  slug: salesforce-rest-query-result-structure
- name: Salesforce Rest S Object Describe Structure
  property_count: 11
  slug: salesforce-rest-s-object-describe-structure
- name: Salesforce Rest S Object Record Structure
  property_count: 2
  slug: salesforce-rest-s-object-record-structure
- name: Salesforce Rest Search Result Structure
  property_count: 1
  slug: salesforce-rest-search-result-structure
- name: Salesforce Result Page Structure
  property_count: 1
  slug: salesforce-result-page-structure
- name: Salesforce Result Structure
  property_count: 2
  slug: salesforce-result-structure
- name: Salesforce Result1 Structure
  property_count: 2
  slug: salesforce-result1-structure
- name: Salesforce Result2 Structure
  property_count: 21
  slug: salesforce-result2-structure
- name: Salesforce Result21 Structure
  property_count: 2
  slug: salesforce-result21-structure
- name: Salesforce Result3 Structure
  property_count: 4
  slug: salesforce-result3-structure
- name: Salesforce Result4 Structure
  property_count: 4
  slug: salesforce-result4-structure
- name: Salesforce Result5 Structure
  property_count: 11
  slug: salesforce-result5-structure
- name: Salesforce Result6 Structure
  property_count: 11
  slug: salesforce-result6-structure
- name: Salesforce Results Structure
  property_count: 1
  slug: salesforce-results-structure
- name: Salesforce Results1 Structure
  property_count: 2
  slug: salesforce-results1-structure
- name: Salesforce Results2 Structure
  property_count: 1
  slug: salesforce-results2-structure
- name: Salesforce Results3 Structure
  property_count: 1
  slug: salesforce-results3-structure
- name: Salesforce Results4 Structure
  property_count: 2
  slug: salesforce-results4-structure
- name: Salesforce Resultwithdefaultnav Structure
  property_count: 4
  slug: salesforce-resultwithdefaultnav-structure
- name: Salesforce Resultwithpersonalizednav Structure
  property_count: 4
  slug: salesforce-resultwithpersonalizednav-structure
- name: Salesforce Retail Location Group Structure
  property_count: 1
  slug: salesforce-retail-location-group-structure
- name: Salesforce Retrieve Open Api Schema Structure
  property_count: 6
  slug: salesforce-retrieve-open-api-schema-structure
- name: Salesforce Retrieveable Structure
  property_count: 1
  slug: salesforce-retrieveable-structure
- name: Salesforce Reward Structure
  property_count: 14
  slug: salesforce-reward-structure
- name: Salesforce Rich Input Structure
  property_count: 4
  slug: salesforce-rich-input-structure
- name: Salesforce Run Decision Matrix Request Structure
  property_count: 1
  slug: salesforce-run-decision-matrix-request-structure
- name: Salesforce Run Decision Matrix Structure
  property_count: 5
  slug: salesforce-run-decision-matrix-structure
- name: Salesforce Run Expression Set Request Structure
  property_count: 1
  slug: salesforce-run-expression-set-request-structure
- name: Salesforce Run Setting Structure
  property_count: 1
  slug: salesforce-run-setting-structure
- name: Salesforce Runagenttest Request Structure
  property_count: 1
  slug: salesforce-runagenttest-request-structure
- name: Salesforce Runagenttest Structure
  property_count: 2
  slug: salesforce-runagenttest-structure
- name: Salesforce S Object Collections Create Request Structure
  property_count: 2
  slug: salesforce-s-object-collections-create-request-structure
- name: Salesforce S Object Collections Update Request Structure
  property_count: 2
  slug: salesforce-s-object-collections-update-request-structure
- name: Salesforce S Object Collections Update Structure
  property_count: 3
  slug: salesforce-s-object-collections-update-structure
- name: Salesforce S Object Collections Upsert Request Structure
  property_count: 2
  slug: salesforce-s-object-collections-upsert-request-structure
- name: Salesforce S Object Create Request Structure
  property_count: 1
  slug: salesforce-s-object-create-request-structure
- name: Salesforce S Object Create Structure
  property_count: 3
  slug: salesforce-s-object-create-structure
- name: Salesforce S Object Describe Structure
  property_count: 45
  slug: salesforce-s-object-describe-structure
- name: Salesforce S Object Root Info Structure
  property_count: 2
  slug: salesforce-s-object-root-info-structure
- name: Salesforce S Object Rows Update Request Structure
  property_count: 1
  slug: salesforce-s-object-rows-update-request-structure
- name: Salesforce S Object Tree Request Structure
  property_count: 1
  slug: salesforce-s-object-tree-request-structure
- name: Salesforce S Objects Structure
  property_count: 4
  slug: salesforce-s-objects-structure
- name: Salesforce S Objects1 Structure
  property_count: 2
  slug: salesforce-s-objects1-structure
- name: Salesforce Salutation Structure
  property_count: 2
  slug: salesforce-salutation-structure
- name: Salesforce Salutation1 Structure
  property_count: 31
  slug: salesforce-salutation1-structure
- name: Salesforce Salutation2 Structure
  property_count: 2
  slug: salesforce-salutation2-structure
- name: Salesforce Salutation4 Structure
  property_count: 5
  slug: salesforce-salutation4-structure
- name: Salesforce Sample Lightning Page Structure
  property_count: 3
  slug: salesforce-sample-lightning-page-structure
- name: Salesforce Save Result Structure
  property_count: 2
  slug: salesforce-save-result-structure
- name: Salesforce Schema Structure
  property_count: 1
  slug: salesforce-schema-structure
- name: Salesforce Schema1 Structure
  property_count: 2
  slug: salesforce-schema1-structure
- name: Salesforce Schema10 Structure
  property_count: 1
  slug: salesforce-schema10-structure
- name: Salesforce Schemas Structure
  property_count: 6
  slug: salesforce-schemas-structure
- name: Salesforce Scopes Structure
  property_count: 17
  slug: salesforce-scopes-structure
- name: Salesforce Scopes1 Structure
  property_count: 1
  slug: salesforce-scopes1-structure
- name: Salesforce Scorecard Association Structure
  property_count: 6
  slug: salesforce-scorecard-association-structure
- name: Salesforce Scorecard Metric Structure
  property_count: 6
  slug: salesforce-scorecard-metric-structure
- name: Salesforce Scorecard Structure
  property_count: 6
  slug: salesforce-scorecard-structure
- name: Salesforce Scratch Org Info History Structure
  property_count: 6
  slug: salesforce-scratch-org-info-history-structure
- name: Salesforce Scratch Org Info Structure
  property_count: 6
  slug: salesforce-scratch-org-info-structure
- name: Salesforce Search Promotion Rule Structure
  property_count: 6
  slug: salesforce-search-promotion-rule-structure
- name: Salesforce Search Record Structure
  property_count: 2
  slug: salesforce-search-record-structure
- name: Salesforce Searchable Structure
  property_count: 1
  slug: salesforce-searchable-structure
- name: Salesforce Section Structure
  property_count: 7
  slug: salesforce-section-structure
- name: Salesforce Section User States Structure
  property_count: 5
  slug: salesforce-section-user-states-structure
- name: Salesforce Section1 Structure
  property_count: 7
  slug: salesforce-section1-structure
- name: Salesforce Security Schemes Structure
  property_count: 3
  slug: salesforce-security-schemes-structure
- name: Salesforce Security Structure
  property_count: 3
  slug: salesforce-security-structure
- name: Salesforce Seller History Structure
  property_count: 6
  slug: salesforce-seller-history-structure
- name: Salesforce Seller Structure
  property_count: 6
  slug: salesforce-seller-structure
- name: Salesforce Sender Email Structure
  property_count: 31
  slug: salesforce-sender-email-structure
- name: Salesforce Sender Name Structure
  property_count: 31
  slug: salesforce-sender-name-structure
- name: Salesforce Sender Structure
  property_count: 19
  slug: salesforce-sender-structure
- name: Salesforce Sender1 Structure
  property_count: 3
  slug: salesforce-sender1-structure
- name: Salesforce Server Structure
  property_count: 1
  slug: salesforce-server-structure
- name: Salesforce Session Header Structure
  property_count: 1
  slug: salesforce-session-header-structure
- name: Salesforce Session Header1 Structure
  property_count: 1
  slug: salesforce-session-header1-structure
- name: Salesforce Session Header4 Structure
  property_count: 1
  slug: salesforce-session-header4-structure
- name: Salesforce Session Hijacking Event Store Structure
  property_count: 6
  slug: salesforce-session-hijacking-event-store-structure
- name: Salesforce Settings Structure
  property_count: 3
  slug: salesforce-settings-structure
- name: Salesforce Setup Assistant Step Structure
  property_count: 6
  slug: salesforce-setup-assistant-step-structure
- name: Salesforce Share Structure
  property_count: 2
  slug: salesforce-share-structure
- name: Salesforce Shipping Address Structure
  property_count: 2
  slug: salesforce-shipping-address-structure
- name: Salesforce Shipping Address1 Structure
  property_count: 8
  slug: salesforce-shipping-address1-structure
- name: Salesforce Shipping Address11 Structure
  property_count: 8
  slug: salesforce-shipping-address11-structure
- name: Salesforce Shipping Address12 Structure
  property_count: 8
  slug: salesforce-shipping-address12-structure
- name: Salesforce Shipping Address2 Structure
  property_count: 31
  slug: salesforce-shipping-address2-structure
- name: Salesforce Shipping City Structure
  property_count: 2
  slug: salesforce-shipping-city-structure
- name: Salesforce Shipping City1 Structure
  property_count: 31
  slug: salesforce-shipping-city1-structure
- name: Salesforce Shipping City2 Structure
  property_count: 2
  slug: salesforce-shipping-city2-structure
- name: Salesforce Shipping City4 Structure
  property_count: 2
  slug: salesforce-shipping-city4-structure
- name: Salesforce Shipping Country Structure
  property_count: 2
  slug: salesforce-shipping-country-structure
- name: Salesforce Shipping Country1 Structure
  property_count: 31
  slug: salesforce-shipping-country1-structure
- name: Salesforce Shipping Country2 Structure
  property_count: 2
  slug: salesforce-shipping-country2-structure
- name: Salesforce Shipping Country4 Structure
  property_count: 2
  slug: salesforce-shipping-country4-structure
- name: Salesforce Shipping Geocode Accuracy Structure
  property_count: 2
  slug: salesforce-shipping-geocode-accuracy-structure
- name: Salesforce Shipping Geocode Accuracy1 Structure
  property_count: 31
  slug: salesforce-shipping-geocode-accuracy1-structure
- name: Salesforce Shipping Latitude Structure
  property_count: 2
  slug: salesforce-shipping-latitude-structure
- name: Salesforce Shipping Latitude1 Structure
  property_count: 31
  slug: salesforce-shipping-latitude1-structure
- name: Salesforce Shipping Longitude Structure
  property_count: 2
  slug: salesforce-shipping-longitude-structure
- name: Salesforce Shipping Longitude1 Structure
  property_count: 31
  slug: salesforce-shipping-longitude1-structure
- name: Salesforce Shipping Postal Code Structure
  property_count: 2
  slug: salesforce-shipping-postal-code-structure
- name: Salesforce Shipping Postal Code1 Structure
  property_count: 31
  slug: salesforce-shipping-postal-code1-structure
- name: Salesforce Shipping Postal Code2 Structure
  property_count: 2
  slug: salesforce-shipping-postal-code2-structure
- name: Salesforce Shipping Postal Code4 Structure
  property_count: 2
  slug: salesforce-shipping-postal-code4-structure
- name: Salesforce Shipping State Structure
  property_count: 2
  slug: salesforce-shipping-state-structure
- name: Salesforce Shipping State1 Structure
  property_count: 31
  slug: salesforce-shipping-state1-structure
- name: Salesforce Shipping State2 Structure
  property_count: 2
  slug: salesforce-shipping-state2-structure
- name: Salesforce Shipping State4 Structure
  property_count: 2
  slug: salesforce-shipping-state4-structure
- name: Salesforce Shipping Street Structure
  property_count: 2
  slug: salesforce-shipping-street-structure
- name: Salesforce Shipping Street1 Structure
  property_count: 31
  slug: salesforce-shipping-street1-structure
- name: Salesforce Shipping Street2 Structure
  property_count: 2
  slug: salesforce-shipping-street2-structure
- name: Salesforce Shipping Street4 Structure
  property_count: 2
  slug: salesforce-shipping-street4-structure
- name: Salesforce Sic Code C Structure
  property_count: 31
  slug: salesforce-sic-code-c-structure
- name: Salesforce Sic Code C1 Structure
  property_count: 2
  slug: salesforce-sic-code-c1-structure
- name: Salesforce Sic Desc Structure
  property_count: 2
  slug: salesforce-sic-desc-structure
- name: Salesforce Sic Desc1 Structure
  property_count: 31
  slug: salesforce-sic-desc1-structure
- name: Salesforce Sic Structure
  property_count: 2
  slug: salesforce-sic-structure
- name: Salesforce Sic1 Structure
  property_count: 31
  slug: salesforce-sic1-structure
- name: Salesforce Sic2 Structure
  property_count: 2
  slug: salesforce-sic2-structure
- name: Salesforce Sic4 Structure
  property_count: 2
  slug: salesforce-sic4-structure
- name: Salesforce Signature Structure
  property_count: 31
  slug: salesforce-signature-structure
- name: Salesforce Single Email Structure
  property_count: 2
  slug: salesforce-single-email-structure
- name: Salesforce Site History Structure
  property_count: 6
  slug: salesforce-site-history-structure
- name: Salesforce Site Structure
  property_count: 2
  slug: salesforce-site-structure
- name: Salesforce Site1 Structure
  property_count: 31
  slug: salesforce-site1-structure
- name: Salesforce Site2 Structure
  property_count: 2
  slug: salesforce-site2-structure
- name: Salesforce Sla Expiration Date C Structure
  property_count: 2
  slug: salesforce-sla-expiration-date-c-structure
- name: Salesforce Sla Expiration Date C1 Structure
  property_count: 31
  slug: salesforce-sla-expiration-date-c1-structure
- name: Salesforce Sla Expiration Date C2 Structure
  property_count: 2
  slug: salesforce-sla-expiration-date-c2-structure
- name: Salesforce Sla Expiration Date C4 Structure
  property_count: 2
  slug: salesforce-sla-expiration-date-c4-structure
- name: Salesforce Sla Serial Number C Structure
  property_count: 1
  slug: salesforce-sla-serial-number-c-structure
- name: Salesforce Sla Serial Number C1 Structure
  property_count: 31
  slug: salesforce-sla-serial-number-c1-structure
- name: Salesforce Sla Serial Number C2 Structure
  property_count: 2
  slug: salesforce-sla-serial-number-c2-structure
- name: Salesforce Sla Serial Number C4 Structure
  property_count: 2
  slug: salesforce-sla-serial-number-c4-structure
- name: Salesforce Slac Structure
  property_count: 1
  slug: salesforce-slac-structure
- name: Salesforce Slac1 Structure
  property_count: 31
  slug: salesforce-slac1-structure
- name: Salesforce Slac2 Structure
  property_count: 2
  slug: salesforce-slac2-structure
- name: Salesforce Slac4 Structure
  property_count: 2
  slug: salesforce-slac4-structure
- name: Salesforce Small Banner Photo Url Structure
  property_count: 31
  slug: salesforce-small-banner-photo-url-structure
- name: Salesforce Small Photo Url Structure
  property_count: 31
  slug: salesforce-small-photo-url-structure
- name: Salesforce Sobjects Contact Structure
  property_count: 3
  slug: salesforce-sobjects-contact-structure
- name: Salesforce Sobjects2 Structure
  property_count: 28
  slug: salesforce-sobjects2-structure
- name: Salesforce Solution History Structure
  property_count: 6
  slug: salesforce-solution-history-structure
- name: Salesforce Stage Name Structure
  property_count: 1
  slug: salesforce-stage-name-structure
- name: Salesforce State Structure
  property_count: 31
  slug: salesforce-state-structure
- name: Salesforce State2 Structure
  property_count: 2
  slug: salesforce-state2-structure
- name: Salesforce Static Resource Structure
  property_count: 6
  slug: salesforce-static-resource-structure
- name: Salesforce Status Code Structure
  property_count: 1
  slug: salesforce-status-code-structure
- name: Salesforce Status Structure
  property_count: 2
  slug: salesforce-status-structure
- name: Salesforce Status1 Structure
  property_count: 2
  slug: salesforce-status1-structure
- name: Salesforce Status200 Record Found Structure
  property_count: 6
  slug: salesforce-status200-record-found-structure
- name: Salesforce Status200 Success Structure
  property_count: 4
  slug: salesforce-status200-success-structure
- name: Salesforce Status200 Success2 Structure
  property_count: 3
  slug: salesforce-status200-success2-structure
- name: Salesforce Status200 Successfull Structure
  property_count: 5
  slug: salesforce-status200-successfull-structure
- name: Salesforce Status200 Successfully Updated Structure
  property_count: 6
  slug: salesforce-status200-successfully-updated-structure
- name: Salesforce Status200 Update Commitment Database Failure Structure
  property_count: 2
  slug: salesforce-status200-update-commitment-database-failure-structure
- name: Salesforce Status200 Update Commitment Request Validation Failure Structure
  property_count: 2
  slug: salesforce-status200-update-commitment-request-validation-failure-structure
- name: Salesforce Status200 Update Commitment Request Validation Failure1 Structure
  property_count: 4
  slug: salesforce-status200-update-commitment-request-validation-failure1-structure
- name: Salesforce Status200 Update Commitment Success Structure
  property_count: 2
  slug: salesforce-status200-update-commitment-success-structure
- name: Salesforce Status200 Update Commitment Success With External Ids Structure
  property_count: 2
  slug: salesforce-status200-update-commitment-success-with-external-ids-structure
- name: Salesforce Status201 Accepted But Warning Structure
  property_count: 1
  slug: salesforce-status201-accepted-but-warning-structure
- name: Salesforce Status201 Bad Request Structure
  property_count: 3
  slug: salesforce-status201-bad-request-structure
- name: Salesforce Status201 Create Commitment Request Validation Failure Structure
  property_count: 4
  slug: salesforce-status201-create-commitment-request-validation-failure-structure
- name: Salesforce Status201 Create Commitment Success Structure
  property_count: 4
  slug: salesforce-status201-create-commitment-success-structure
- name: Salesforce Status201 Create Commitment Success With External Ids Structure
  property_count: 4
  slug: salesforce-status201-create-commitment-success-with-external-ids-structure
- name: Salesforce Status201 Create Commitment Success With External Ids1 Structure
  property_count: 4
  slug: salesforce-status201-create-commitment-success-with-external-ids1-structure
- name: Salesforce Status201 Create Commitment Success1 Structure
  property_count: 4
  slug: salesforce-status201-create-commitment-success1-structure
- name: Salesforce Status201 Create Gift Request Validation Failure Structure
  property_count: 4
  slug: salesforce-status201-create-gift-request-validation-failure-structure
- name: Salesforce Status201 Create Gift Success Structure
  property_count: 4
  slug: salesforce-status201-create-gift-success-structure
- name: Salesforce Status201 Create Gift Success With External Ids Structure
  property_count: 4
  slug: salesforce-status201-create-gift-success-with-external-ids-structure
- name: Salesforce Status201 Error Structure
  property_count: 1
  slug: salesforce-status201-error-structure
- name: Salesforce Status201 Key Pair Not Found Structure
  property_count: 1
  slug: salesforce-status201-key-pair-not-found-structure
- name: Salesforce Status201 Success Created Only Mandatory Fields Structure
  property_count: 6
  slug: salesforce-status201-success-created-only-mandatory-fields-structure
- name: Salesforce Status201 Success Structure
  property_count: 3
  slug: salesforce-status201-success-structure
- name: Salesforce Status201 Success1 Structure
  property_count: 1
  slug: salesforce-status201-success1-structure
- name: Salesforce Status201 Success2 Structure
  property_count: 1
  slug: salesforce-status201-success2-structure
- name: Salesforce Status201 Success3 Structure
  property_count: 3
  slug: salesforce-status201-success3-structure
- name: Salesforce Status201 Success4 Structure
  property_count: 4
  slug: salesforce-status201-success4-structure
- name: Salesforce Status201 Success5 Structure
  property_count: 5
  slug: salesforce-status201-success5-structure
- name: Salesforce Status201 Update Commitment External Ids Structure
  property_count: 4
  slug: salesforce-status201-update-commitment-external-ids-structure
- name: Salesforce Status201 Update Commitment Success Structure
  property_count: 4
  slug: salesforce-status201-update-commitment-success-structure
- name: Salesforce Status201 Update Transaction Payment Request Validation Failed Structure
  property_count: 4
  slug: salesforce-status201-update-transaction-payment-request-validation-failed-structure
- name: Salesforce Status201 Update Transaction Payment Success Structure
  property_count: 4
  slug: salesforce-status201-update-transaction-payment-success-structure
- name: Salesforce Status201 Update Transaction Payment With External Ids1 Structure
  property_count: 4
  slug: salesforce-status201-update-transaction-payment-with-external-ids1-structure
- name: Salesforce Status400 Active Expression Can Not Be Deleted1 Structure
  property_count: 2
  slug: salesforce-status400-active-expression-can-not-be-deleted1-structure
- name: Salesforce Status400 Bad Request1 Structure
  property_count: 2
  slug: salesforce-status400-bad-request1-structure
- name: Salesforce Status400 Duplicate1 Structure
  property_count: 2
  slug: salesforce-status400-duplicate1-structure
- name: Salesforce Status400 Empty Expression Set Api Name1 Structure
  property_count: 5
  slug: salesforce-status400-empty-expression-set-api-name1-structure
- name: Salesforce Status400 Error Invalid Input1 Structure
  property_count: 2
  slug: salesforce-status400-error-invalid-input1-structure
- name: Salesforce Status400 Expression Not Found1 Structure
  property_count: 5
  slug: salesforce-status400-expression-not-found1-structure
- name: Salesforce Status400 Instance Not Found1 Structure
  property_count: 2
  slug: salesforce-status400-instance-not-found1-structure
- name: Salesforce Status400 Invalid Body1 Structure
  property_count: 2
  slug: salesforce-status400-invalid-body1-structure
- name: Salesforce Status400 Invalid Enum1 Structure
  property_count: 2
  slug: salesforce-status400-invalid-enum1-structure
- name: Salesforce Status400 Invalid Expression Set Name1 Structure
  property_count: 2
  slug: salesforce-status400-invalid-expression-set-name1-structure
- name: Salesforce Status400 Invalid Identifier Of Version1 Structure
  property_count: 2
  slug: salesforce-status400-invalid-identifier-of-version1-structure
- name: Salesforce Status400 Invalid Operation1 Structure
  property_count: 2
  slug: salesforce-status400-invalid-operation1-structure
- name: Salesforce Status400 Matrix Not Found1 Structure
  property_count: 2
  slug: salesforce-status400-matrix-not-found1-structure
- name: Salesforce Status400 Missing Mandatory Body Field1 Structure
  property_count: 2
  slug: salesforce-status400-missing-mandatory-body-field1-structure
- name: Salesforce Status400 Previously Deleted Record1 Structure
  property_count: 2
  slug: salesforce-status400-previously-deleted-record1-structure
- name: Salesforce Status400 Try To Delete Previously Deleted1 Structure
  property_count: 2
  slug: salesforce-status400-try-to-delete-previously-deleted1-structure
- name: Salesforce Status400 Unknown Exception1 Structure
  property_count: 2
  slug: salesforce-status400-unknown-exception1-structure
- name: Salesforce Status400 Unrecognized Body Field1 Structure
  property_count: 2
  slug: salesforce-status400-unrecognized-body-field1-structure
- name: Salesforce Status401 Unauthorized1 Structure
  property_count: 2
  slug: salesforce-status401-unauthorized1-structure
- name: Salesforce Status404 Not Found1 Structure
  property_count: 2
  slug: salesforce-status404-not-found1-structure
- name: Salesforce Status404 Record Not Found1 Structure
  property_count: 2
  slug: salesforce-status404-record-not-found1-structure
- name: Salesforce Status500 Empty Body But Record Exist1 Structure
  property_count: 2
  slug: salesforce-status500-empty-body-but-record-exist1-structure
- name: Salesforce Status500 Empty Body1 Structure
  property_count: 2
  slug: salesforce-status500-empty-body1-structure
- name: Salesforce Status500 Error No Body1 Structure
  property_count: 2
  slug: salesforce-status500-error-no-body1-structure
- name: Salesforce Status500 Unexpected Error1 Structure
  property_count: 2
  slug: salesforce-status500-unexpected-error1-structure
- name: Salesforce Status500 Unknown Exception1 Structure
  property_count: 2
  slug: salesforce-status500-unknown-exception1-structure
- name: Salesforce Status8 Structure
  property_count: 31
  slug: salesforce-status8-structure
- name: Salesforce Status9 Structure
  property_count: 2
  slug: salesforce-status9-structure
- name: Salesforce Stay In Touch Note Structure
  property_count: 31
  slug: salesforce-stay-in-touch-note-structure
- name: Salesforce Stay In Touch Signature Structure
  property_count: 31
  slug: salesforce-stay-in-touch-signature-structure
- name: Salesforce Stay In Touch Subject Structure
  property_count: 31
  slug: salesforce-stay-in-touch-subject-structure
- name: Salesforce Step Structure
  property_count: 10
  slug: salesforce-step-structure
- name: Salesforce Store Structure
  property_count: 1
  slug: salesforce-store-structure
- name: Salesforce Streaming Api Concurrent Clients Structure
  property_count: 2
  slug: salesforce-streaming-api-concurrent-clients-structure
- name: Salesforce Streaming Channel Structure
  property_count: 6
  slug: salesforce-streaming-channel-structure
- name: Salesforce Street Structure
  property_count: 31
  slug: salesforce-street-structure
- name: Salesforce Street2 Structure
  property_count: 2
  slug: salesforce-street2-structure
- name: Salesforce Street3 Structure
  property_count: 2
  slug: salesforce-street3-structure
- name: Salesforce Subject Structure
  property_count: 7
  slug: salesforce-subject-structure
- name: Salesforce Subscriber Structure
  property_count: 19
  slug: salesforce-subscriber-structure
- name: Salesforce Succesful User Photo Structure
  property_count: 7
  slug: salesforce-succesful-user-photo-structure
- name: Salesforce Success Structure
  property_count: 1
  slug: salesforce-success-structure
- name: Salesforce Success1 Structure
  property_count: 6
  slug: salesforce-success1-structure
- name: Salesforce Successful Asset Token Flow Structure
  property_count: 4
  slug: salesforce-successful-asset-token-flow-structure
- name: Salesforce Successful Authentication Configuration Endpoint Structure
  property_count: 9
  slug: salesforce-successful-authentication-configuration-endpoint-structure
- name: Salesforce Successful Bulk Close Job Structure
  property_count: 24
  slug: salesforce-successful-bulk-close-job-structure
- name: Salesforce Successful Bulk Create Job Structure
  property_count: 24
  slug: salesforce-successful-bulk-create-job-structure
- name: Salesforce Successful Client Credentials Flow Basicauthorizationheader Structure
  property_count: 8
  slug: salesforce-successful-client-credentials-flow-basicauthorizationheader-structure
- name: Salesforce Successful Client Credentials Flow Structure
  property_count: 8
  slug: salesforce-successful-client-credentials-flow-structure
- name: Salesforce Successful Closeor Aborta Job Structure
  property_count: 10
  slug: salesforce-successful-closeor-aborta-job-structure
- name: Salesforce Successful Comment Edit Structure
  property_count: 18
  slug: salesforce-successful-comment-edit-structure
- name: Salesforce Successful Comment Structure
  property_count: 18
  slug: salesforce-successful-comment-structure
- name: Salesforce Successful Composite Graph Structure
  property_count: 1
  slug: salesforce-successful-composite-graph-structure
- name: Salesforce Successful Composite Structure
  property_count: 1
  slug: salesforce-successful-composite-structure
- name: Salesforce Successful Create Credential Structure
  property_count: 6
  slug: salesforce-successful-create-credential-structure
- name: Salesforce Successful Create External Credential Structure
  property_count: 10
  slug: salesforce-successful-create-external-credential-structure
- name: Salesforce Successful Create Named Credential Structure
  property_count: 10
  slug: salesforce-successful-create-named-credential-structure
- name: Salesforce Successful Createjob Query Request Structure
  property_count: 5
  slug: salesforce-successful-createjob-query-request-structure
- name: Salesforce Successful Createjob Query Structure
  property_count: 12
  slug: salesforce-successful-createjob-query-structure
- name: Salesforce Successful Createjob Structure
  property_count: 13
  slug: salesforce-successful-createjob-structure
- name: Salesforce Successful Device Flow2 Structure
  property_count: 9
  slug: salesforce-successful-device-flow2-structure
- name: Salesforce Successful Feed Elements Batch Post Structure
  property_count: 2
  slug: salesforce-successful-feed-elements-batch-post-structure
- name: Salesforce Successful Feed Elements Postand Search Structure
  property_count: 21
  slug: salesforce-successful-feed-elements-postand-search-structure
- name: Salesforce Successful Feed Elements Postand Search1 Structure
  property_count: 21
  slug: salesforce-successful-feed-elements-postand-search1-structure
- name: Salesforce Successful File Shares Structure
  property_count: 5
  slug: salesforce-successful-file-shares-structure
- name: Salesforce Successful Files Shares Link Structure
  property_count: 5
  slug: salesforce-successful-files-shares-link-structure
- name: Salesforce Successful Following Post Structure
  property_count: 5
  slug: salesforce-successful-following-post-structure
- name: Salesforce Successful Following Structure
  property_count: 5
  slug: salesforce-successful-following-structure
- name: Salesforce Successful Get All Query Jobs Structure
  property_count: 3
  slug: salesforce-successful-get-all-query-jobs-structure
- name: Salesforce Successful Get Credential Structure
  property_count: 7
  slug: salesforce-successful-get-credential-structure
- name: Salesforce Successful Get External Credentialsby Developer Name Structure
  property_count: 11
  slug: salesforce-successful-get-external-credentialsby-developer-name-structure
- name: Salesforce Successful Get Job Info Query Structure
  property_count: 15
  slug: salesforce-successful-get-job-info-query-structure
- name: Salesforce Successful Get Job Info Query1 Structure
  property_count: 16
  slug: salesforce-successful-get-job-info-query1-structure
- name: Salesforce Successful Get Job Info Structure
  property_count: 19
  slug: salesforce-successful-get-job-info-structure
- name: Salesforce Successful Get Named Credentialby Developer Name Structure
  property_count: 10
  slug: salesforce-successful-get-named-credentialby-developer-name-structure
- name: Salesforce Successful Group Members Private Structure
  property_count: 2
  slug: salesforce-successful-group-members-private-structure
- name: Salesforce Successful Group Members Structure
  property_count: 5
  slug: salesforce-successful-group-members-structure
- name: Salesforce Successful Group Membership Requests Private Structure
  property_count: 8
  slug: salesforce-successful-group-membership-requests-private-structure
- name: Salesforce Successful Id Token Structure
  property_count: 30
  slug: salesforce-successful-id-token-structure
- name: Salesforce Successful Jwt Bearer Token Flow Structure
  property_count: 5
  slug: salesforce-successful-jwt-bearer-token-flow-structure
- name: Salesforce Successful List External Credentials Structure
  property_count: 1
  slug: salesforce-successful-list-external-credentials-structure
- name: Salesforce Successful List Named Credentials Structure
  property_count: 1
  slug: salesforce-successful-list-named-credentials-structure
- name: Salesforce Successful Listof Groups Post Structure
  property_count: 25
  slug: salesforce-successful-listof-groups-post-structure
- name: Salesforce Successful Listof Groups Structure
  property_count: 4
  slug: salesforce-successful-listof-groups-structure
- name: Salesforce Successful News Feed Elements Structure
  property_count: 9
  slug: salesforce-successful-news-feed-elements-structure
- name: Salesforce Successful O Auth Username Password Login Structure
  property_count: 6
  slug: salesforce-successful-o-auth-username-password-login-structure
- name: Salesforce Successful Open Id Connect Discovery Endpoint Structure
  property_count: 18
  slug: salesforce-successful-open-id-connect-discovery-endpoint-structure
- name: Salesforce Successful Record Feed Elements Structure
  property_count: 9
  slug: salesforce-successful-record-feed-elements-structure
- name: Salesforce Successful Refresh Token Structure
  property_count: 8
  slug: salesforce-successful-refresh-token-structure
- name: Salesforce Successful S Object Collections Create Structure
  property_count: 3
  slug: salesforce-successful-s-object-collections-create-structure
- name: Salesforce Successful S Object Collections Delete Structure
  property_count: 3
  slug: salesforce-successful-s-object-collections-delete-structure
- name: Salesforce Successful S Object Collections Retrieve Structure
  property_count: 3
  slug: salesforce-successful-s-object-collections-retrieve-structure
- name: Salesforce Successful S Object Collections Upsert Structure
  property_count: 4
  slug: salesforce-successful-s-object-collections-upsert-structure
- name: Salesforce Successful S Object Tree Structure
  property_count: 2
  slug: salesforce-successful-s-object-tree-structure
- name: Salesforce Successful Salesforce Keys Structure
  property_count: 1
  slug: salesforce-successful-salesforce-keys-structure
- name: Salesforce Successful Update External Credential Structure
  property_count: 10
  slug: salesforce-successful-update-external-credential-structure
- name: Salesforce Successful Update Named Credential Structure
  property_count: 10
  slug: salesforce-successful-update-named-credential-structure
- name: Salesforce Successful User Info Structure
  property_count: 24
  slug: salesforce-successful-user-info-structure
- name: Salesforce Successful User Messages General Structure
  property_count: 9
  slug: salesforce-successful-user-messages-general-structure
- name: Salesforce Successful User Profile Feed Elements Structure
  property_count: 9
  slug: salesforce-successful-user-profile-feed-elements-structure
- name: Salesforce Successful Users Files General Structure
  property_count: 49
  slug: salesforce-successful-users-files-general-structure
- name: Salesforce Successful Web Server Flow2 Structure
  property_count: 9
  slug: salesforce-successful-web-server-flow2-structure
- name: Salesforce Successfull Get All Jobs Structure
  property_count: 3
  slug: salesforce-successfull-get-all-jobs-structure
- name: Salesforce Supported Scope Structure
  property_count: 2
  slug: salesforce-supported-scope-structure
- name: Salesforce Symbol Table Structure
  property_count: 13
  slug: salesforce-symbol-table-structure
- name: Salesforce System Modstamp Structure
  property_count: 2
  slug: salesforce-system-modstamp-structure
- name: Salesforce System Modstamp10 Structure
  property_count: 2
  slug: salesforce-system-modstamp10-structure
- name: Salesforce System Modstamp2 Structure
  property_count: 31
  slug: salesforce-system-modstamp2-structure
- name: Salesforce Tab Structure
  property_count: 9
  slug: salesforce-tab-structure
- name: Salesforce Table Declaration Structure
  property_count: 6
  slug: salesforce-table-declaration-structure
- name: Salesforce Test Case Structure
  property_count: 7
  slug: salesforce-test-case-structure
- name: Salesforce Test Credential Structure
  property_count: 2
  slug: salesforce-test-credential-structure
- name: Salesforce Test Result Structure
  property_count: 11
  slug: salesforce-test-result-structure
- name: Salesforce Theme Info Structure
  property_count: 2
  slug: salesforce-theme-info-structure
- name: Salesforce Theme Item Structure
  property_count: 3
  slug: salesforce-theme-item-structure
- name: Salesforce Themes Structure
  property_count: 1
  slug: salesforce-themes-structure
- name: Salesforce Threat Detection Feedback Structure
  property_count: 6
  slug: salesforce-threat-detection-feedback-structure
- name: Salesforce Ticker Symbol Structure
  property_count: 2
  slug: salesforce-ticker-symbol-structure
- name: Salesforce Ticker Symbol1 Structure
  property_count: 31
  slug: salesforce-ticker-symbol1-structure
- name: Salesforce Ticker Symbol2 Structure
  property_count: 2
  slug: salesforce-ticker-symbol2-structure
- name: Salesforce Tier Group Structure
  property_count: 2
  slug: salesforce-tier-group-structure
- name: Salesforce Tier Structure
  property_count: 2
  slug: salesforce-tier-structure
- name: Salesforce Time Zone Sid Key Structure
  property_count: 31
  slug: salesforce-time-zone-sid-key-structure
- name: Salesforce Title Structure
  property_count: 2
  slug: salesforce-title-structure
- name: Salesforce Title1 Structure
  property_count: 31
  slug: salesforce-title1-structure
- name: Salesforce Title4 Structure
  property_count: 2
  slug: salesforce-title4-structure
- name: Salesforce Tooling Execute Anonymous Structure
  property_count: 7
  slug: salesforce-tooling-execute-anonymous-structure
- name: Salesforce Tooling Query Structure
  property_count: 6
  slug: salesforce-tooling-query-structure
- name: Salesforce Tooling Run Tests Sync Structure
  property_count: 10
  slug: salesforce-tooling-run-tests-sync-structure
- name: Salesforce Tooling Search Structure
  property_count: 1
  slug: salesforce-tooling-search-structure
- name: Salesforce Topic Assignment Structure
  property_count: 6
  slug: salesforce-topic-assignment-structure
- name: Salesforce Topic Structure
  property_count: 6
  slug: salesforce-topic-structure
- name: Salesforce Topics Structure
  property_count: 3
  slug: salesforce-topics-structure
- name: Salesforce Topics2 Structure
  property_count: 2
  slug: salesforce-topics2-structure
- name: Salesforce Tradestyle Structure
  property_count: 2
  slug: salesforce-tradestyle-structure
- name: Salesforce Tradestyle1 Structure
  property_count: 31
  slug: salesforce-tradestyle1-structure
- name: Salesforce Transaction History Request Structure
  property_count: 5
  slug: salesforce-transaction-history-request-structure
- name: Salesforce Transaction History Structure
  property_count: 4
  slug: salesforce-transaction-history-structure
- name: Salesforce Transaction Journal Structure
  property_count: 8
  slug: salesforce-transaction-journal-structure
- name: Salesforce Transaction Journal2 Structure
  property_count: 7
  slug: salesforce-transaction-journal2-structure
- name: Salesforce Transaction Journal3 Structure
  property_count: 6
  slug: salesforce-transaction-journal3-structure
- name: Salesforce Transaction Journal4 Structure
  property_count: 17
  slug: salesforce-transaction-journal4-structure
- name: Salesforce Transaction Journal5 Structure
  property_count: 8
  slug: salesforce-transaction-journal5-structure
- name: Salesforce Transaction Journals Execution Request Structure
  property_count: 1
  slug: salesforce-transaction-journals-execution-request-structure
- name: Salesforce Transaction Journals Simulation Request Structure
  property_count: 2
  slug: salesforce-transaction-journals-simulation-request-structure
- name: Salesforce Transaction Ledger Summary Structure
  property_count: 4
  slug: salesforce-transaction-ledger-summary-structure
- name: Salesforce Translation Structure
  property_count: 6
  slug: salesforce-translation-structure
- name: Salesforce Triggerable Structure
  property_count: 1
  slug: salesforce-triggerable-structure
- name: Salesforce Type Structure
  property_count: 4
  slug: salesforce-type-structure
- name: Salesforce Type1 Structure
  property_count: 4
  slug: salesforce-type1-structure
- name: Salesforce Type10 Structure
  property_count: 2
  slug: salesforce-type10-structure
- name: Salesforce Type11 Structure
  property_count: 4
  slug: salesforce-type11-structure
- name: Salesforce Type12 Structure
  property_count: 4
  slug: salesforce-type12-structure
- name: Salesforce Type13 Structure
  property_count: 2
  slug: salesforce-type13-structure
- name: Salesforce Type4 Structure
  property_count: 2
  slug: salesforce-type4-structure
- name: Salesforce Type5 Structure
  property_count: 1
  slug: salesforce-type5-structure
- name: Salesforce Type7 Structure
  property_count: 31
  slug: salesforce-type7-structure
- name: Salesforce Ui Error Response Structure
  property_count: 2
  slug: salesforce-ui-error-response-structure
- name: Salesforce Ui Field Representation Structure
  property_count: 8
  slug: salesforce-ui-field-representation-structure
- name: Salesforce Ui Field Value Representation Structure
  property_count: 2
  slug: salesforce-ui-field-value-representation-structure
- name: Salesforce Ui List View Collection Structure
  property_count: 5
  slug: salesforce-ui-list-view-collection-structure
- name: Salesforce Ui List View Result Structure
  property_count: 4
  slug: salesforce-ui-list-view-result-structure
- name: Salesforce Ui List View Summary Structure
  property_count: 4
  slug: salesforce-ui-list-view-summary-structure
- name: Salesforce Ui Lookup Records Collection Structure
  property_count: 2
  slug: salesforce-ui-lookup-records-collection-structure
- name: Salesforce Ui Object Info Representation Structure
  property_count: 11
  slug: salesforce-ui-object-info-representation-structure
- name: Salesforce Ui Picklist Value Structure
  property_count: 4
  slug: salesforce-ui-picklist-value-structure
- name: Salesforce Ui Picklist Values Collection Structure
  property_count: 1
  slug: salesforce-ui-picklist-values-collection-structure
- name: Salesforce Ui Record Input Structure
  property_count: 2
  slug: salesforce-ui-record-input-structure
- name: Salesforce Ui Record Representation Structure
  property_count: 12
  slug: salesforce-ui-record-representation-structure
- name: Salesforce Uiapi Structure
  property_count: 1
  slug: salesforce-uiapi-structure
- name: Salesforce Uiapi10 Structure
  property_count: 1
  slug: salesforce-uiapi10-structure
- name: Salesforce Uiapi11 Structure
  property_count: 1
  slug: salesforce-uiapi11-structure
- name: Salesforce Uiapi12 Structure
  property_count: 1
  slug: salesforce-uiapi12-structure
- name: Salesforce Uiapi13 Structure
  property_count: 1
  slug: salesforce-uiapi13-structure
- name: Salesforce Uiapi3 Structure
  property_count: 1
  slug: salesforce-uiapi3-structure
- name: Salesforce Uiapi4 Structure
  property_count: 1
  slug: salesforce-uiapi4-structure
- name: Salesforce Uiapi6 Structure
  property_count: 1
  slug: salesforce-uiapi6-structure
- name: Salesforce Uiapi7 Structure
  property_count: 1
  slug: salesforce-uiapi7-structure
- name: Salesforce Undeletable Structure
  property_count: 1
  slug: salesforce-undeletable-structure
- name: Salesforce Undelete Structure
  property_count: 1
  slug: salesforce-undelete-structure
- name: Salesforce Unenrolla Member Request Structure
  property_count: 1
  slug: salesforce-unenrolla-member-request-structure
- name: Salesforce Up Down Vote Structure
  property_count: 3
  slug: salesforce-up-down-vote-structure
- name: Salesforce Upate Account Success Structure
  property_count: 2
  slug: salesforce-upate-account-success-structure
- name: Salesforce Update Commitment Payments Request Structure
  property_count: 1
  slug: salesforce-update-commitment-payments-request-structure
- name: Salesforce Update Commitments Request Structure
  property_count: 12
  slug: salesforce-update-commitments-request-structure
- name: Salesforce Update Credential Request Structure
  property_count: 5
  slug: salesforce-update-credential-request-structure
- name: Salesforce Update External Credential Request Structure
  property_count: 4
  slug: salesforce-update-external-credential-request-structure
- name: Salesforce Update Gift Transaction Payments Request Structure
  property_count: 1
  slug: salesforce-update-gift-transaction-payments-request-structure
- name: Salesforce Update Last Selected App Structure
  property_count: 18
  slug: salesforce-update-last-selected-app-structure
- name: Salesforce Update Member Details Request Structure
  property_count: 1
  slug: salesforce-update-member-details-request-structure
- name: Salesforce Update Member Tier Request Structure
  property_count: 1
  slug: salesforce-update-member-tier-request-structure
- name: Salesforce Update Named Credential Request Structure
  property_count: 6
  slug: salesforce-update-named-credential-request-structure
- name: Salesforce Update Structure
  property_count: 10
  slug: salesforce-update-structure
- name: Salesforce Update Table Request Structure
  property_count: 12
  slug: salesforce-update-table-request-structure
- name: Salesforce Update Usageofa Favorite Structure
  property_count: 11
  slug: salesforce-update-usageofa-favorite-structure
- name: Salesforce Update1 Structure
  property_count: 2
  slug: salesforce-update1-structure
- name: Salesforce Updatea Batchof Favorites Request Structure
  property_count: 1
  slug: salesforce-updatea-batchof-favorites-request-structure
- name: Salesforce Updatea Batchof Favorites Structure
  property_count: 1
  slug: salesforce-updatea-batchof-favorites-structure
- name: Salesforce Updatea Favorite Request Structure
  property_count: 2
  slug: salesforce-updatea-favorite-request-structure
- name: Salesforce Updatea Favorite Structure
  property_count: 11
  slug: salesforce-updatea-favorite-structure
- name: Salesforce Updatea Record Request Structure
  property_count: 2
  slug: salesforce-updatea-record-request-structure
- name: Salesforce Updatea Record Structure
  property_count: 11
  slug: salesforce-updatea-record-structure
- name: Salesforce Updateable Structure
  property_count: 1
  slug: salesforce-updateable-structure
- name: Salesforce Updatechannel Request Structure
  property_count: 2
  slug: salesforce-updatechannel-request-structure
- name: Salesforce Updateeventrelay Request Structure
  property_count: 2
  slug: salesforce-updateeventrelay-request-structure
- name: Salesforce Updatemanagedeventsubscription Request Structure
  property_count: 2
  slug: salesforce-updatemanagedeventsubscription-request-structure
- name: Salesforce Updatenamedcredential Request1 Structure
  property_count: 2
  slug: salesforce-updatenamedcredential-request1-structure
- name: Salesforce Upsell Opportunity C Structure
  property_count: 1
  slug: salesforce-upsell-opportunity-c-structure
- name: Salesforce Upsell Opportunity C1 Structure
  property_count: 31
  slug: salesforce-upsell-opportunity-c1-structure
- name: Salesforce Upsell Opportunity C2 Structure
  property_count: 2
  slug: salesforce-upsell-opportunity-c2-structure
- name: Salesforce Upsell Opportunity C4 Structure
  property_count: 2
  slug: salesforce-upsell-opportunity-c4-structure
- name: Salesforce Url Structure
  property_count: 1
  slug: salesforce-url-structure
- name: Salesforce Urls Structure
  property_count: 17
  slug: salesforce-urls-structure
- name: Salesforce Urls2 Structure
  property_count: 3
  slug: salesforce-urls2-structure
- name: Salesforce Urls3 Structure
  property_count: 1
  slug: salesforce-urls3-structure
- name: Salesforce Urls4 Structure
  property_count: 11
  slug: salesforce-urls4-structure
- name: Salesforce Urls5 Structure
  property_count: 2
  slug: salesforce-urls5-structure
- name: Salesforce Urls7 Structure
  property_count: 5
  slug: salesforce-urls7-structure
- name: Salesforce Urls8 Structure
  property_count: 8
  slug: salesforce-urls8-structure
- name: Salesforce User Permissions Call Center Auto Login Structure
  property_count: 31
  slug: salesforce-user-permissions-call-center-auto-login-structure
- name: Salesforce User Permissions Interaction User Structure
  property_count: 31
  slug: salesforce-user-permissions-interaction-user-structure
- name: Salesforce User Permissions Jigsaw Prospecting User Structure
  property_count: 31
  slug: salesforce-user-permissions-jigsaw-prospecting-user-structure
- name: Salesforce User Permissions Knowledge User Structure
  property_count: 31
  slug: salesforce-user-permissions-knowledge-user-structure
- name: Salesforce User Permissions Marketing User Structure
  property_count: 31
  slug: salesforce-user-permissions-marketing-user-structure
- name: Salesforce User Permissions Offline User Structure
  property_count: 31
  slug: salesforce-user-permissions-offline-user-structure
- name: Salesforce User Permissions Sf Content User Structure
  property_count: 31
  slug: salesforce-user-permissions-sf-content-user-structure
- name: Salesforce User Permissions Siteforce Contributor User Structure
  property_count: 31
  slug: salesforce-user-permissions-siteforce-contributor-user-structure
- name: Salesforce User Permissions Siteforce Publisher User Structure
  property_count: 31
  slug: salesforce-user-permissions-siteforce-publisher-user-structure
- name: Salesforce User Permissions Support User Structure
  property_count: 31
  slug: salesforce-user-permissions-support-user-structure
- name: Salesforce User Permissions Work Dot Com User Feature Structure
  property_count: 31
  slug: salesforce-user-permissions-work-dot-com-user-feature-structure
- name: Salesforce User Preferences Activity Reminders Popup Structure
  property_count: 31
  slug: salesforce-user-preferences-activity-reminders-popup-structure
- name: Salesforce User Preferences Apex Pages Developer Mode Structure
  property_count: 31
  slug: salesforce-user-preferences-apex-pages-developer-mode-structure
- name: Salesforce User Preferences Cache Diagnostics Structure
  property_count: 31
  slug: salesforce-user-preferences-cache-diagnostics-structure
- name: Salesforce User Preferences Content Email As And When Structure
  property_count: 31
  slug: salesforce-user-preferences-content-email-as-and-when-structure
- name: Salesforce User Preferences Content No Email Structure
  property_count: 31
  slug: salesforce-user-preferences-content-no-email-structure
- name: Salesforce User Preferences Create Lex Apps Wt Shown Structure
  property_count: 31
  slug: salesforce-user-preferences-create-lex-apps-wt-shown-structure
- name: Salesforce User Preferences Dedupe Storage Migration Complete Structure
  property_count: 31
  slug: salesforce-user-preferences-dedupe-storage-migration-complete-structure
- name: Salesforce User Preferences Dis Comment After Like Email Structure
  property_count: 31
  slug: salesforce-user-preferences-dis-comment-after-like-email-structure
- name: Salesforce User Preferences Dis Mentions Comment Email Structure
  property_count: 31
  slug: salesforce-user-preferences-dis-mentions-comment-email-structure
- name: Salesforce User Preferences Dis Prof Post Comment Email Structure
  property_count: 31
  slug: salesforce-user-preferences-dis-prof-post-comment-email-structure
- name: Salesforce User Preferences Disable All Feeds Email Structure
  property_count: 31
  slug: salesforce-user-preferences-disable-all-feeds-email-structure
- name: Salesforce User Preferences Disable Bookmark Email Structure
  property_count: 31
  slug: salesforce-user-preferences-disable-bookmark-email-structure
- name: Salesforce User Preferences Disable Change Comment Email Structure
  property_count: 31
  slug: salesforce-user-preferences-disable-change-comment-email-structure
- name: Salesforce User Preferences Disable Endorsement Email Structure
  property_count: 31
  slug: salesforce-user-preferences-disable-endorsement-email-structure
- name: Salesforce User Preferences Disable File Share Notifications For Api Structure
  property_count: 31
  slug: salesforce-user-preferences-disable-file-share-notifications-for-api-structure
- name: Salesforce User Preferences Disable Followers Email Structure
  property_count: 31
  slug: salesforce-user-preferences-disable-followers-email-structure
- name: Salesforce User Preferences Disable Later Comment Email Structure
  property_count: 31
  slug: salesforce-user-preferences-disable-later-comment-email-structure
- name: Salesforce User Preferences Disable Like Email Structure
  property_count: 31
  slug: salesforce-user-preferences-disable-like-email-structure
- name: Salesforce User Preferences Disable Mentions Post Email Structure
  property_count: 31
  slug: salesforce-user-preferences-disable-mentions-post-email-structure
- name: Salesforce User Preferences Disable Message Email Structure
  property_count: 31
  slug: salesforce-user-preferences-disable-message-email-structure
- name: Salesforce User Preferences Disable Profile Post Email Structure
  property_count: 31
  slug: salesforce-user-preferences-disable-profile-post-email-structure
- name: Salesforce User Preferences Disable Share Post Email Structure
  property_count: 31
  slug: salesforce-user-preferences-disable-share-post-email-structure
- name: Salesforce User Preferences Enable Auto Sub For Feeds Structure
  property_count: 31
  slug: salesforce-user-preferences-enable-auto-sub-for-feeds-structure
- name: Salesforce User Preferences Event Reminders Checkbox Default Structure
  property_count: 31
  slug: salesforce-user-preferences-event-reminders-checkbox-default-structure
- name: Salesforce User Preferences Exclude Mail App Attachments Structure
  property_count: 31
  slug: salesforce-user-preferences-exclude-mail-app-attachments-structure
- name: Salesforce User Preferences Favorites Show Top Favorites Structure
  property_count: 31
  slug: salesforce-user-preferences-favorites-show-top-favorites-structure
- name: Salesforce User Preferences Favorites Wt Shown Structure
  property_count: 31
  slug: salesforce-user-preferences-favorites-wt-shown-structure
- name: Salesforce User Preferences First Time In Lightning Structure
  property_count: 31
  slug: salesforce-user-preferences-first-time-in-lightning-structure
- name: Salesforce User Preferences Global Nav Bar Wt Shown Structure
  property_count: 31
  slug: salesforce-user-preferences-global-nav-bar-wt-shown-structure
- name: Salesforce User Preferences Global Nav Grid Menu Wt Shown Structure
  property_count: 31
  slug: salesforce-user-preferences-global-nav-grid-menu-wt-shown-structure
- name: Salesforce User Preferences Has Celebration Badge Structure
  property_count: 31
  slug: salesforce-user-preferences-has-celebration-badge-structure
- name: Salesforce User Preferences Has Sent Warning Email Structure
  property_count: 31
  slug: salesforce-user-preferences-has-sent-warning-email-structure
- name: Salesforce User Preferences Heavy Page Prompt Enabled Structure
  property_count: 31
  slug: salesforce-user-preferences-heavy-page-prompt-enabled-structure
- name: Salesforce User Preferences Hide Bigger Photo Callout Structure
  property_count: 31
  slug: salesforce-user-preferences-hide-bigger-photo-callout-structure
- name: Salesforce User Preferences Hide Chatter Onboarding Splash Structure
  property_count: 31
  slug: salesforce-user-preferences-hide-chatter-onboarding-splash-structure
- name: Salesforce User Preferences Hide Csn Desktop Task Structure
  property_count: 31
  slug: salesforce-user-preferences-hide-csn-desktop-task-structure
- name: Salesforce User Preferences Hide Csn Get Chatter Mobile Task Structure
  property_count: 31
  slug: salesforce-user-preferences-hide-csn-get-chatter-mobile-task-structure
- name: Salesforce User Preferences Hide End User Onboarding Assistant Modal Structure
  property_count: 31
  slug: salesforce-user-preferences-hide-end-user-onboarding-assistant-modal-structure
- name: Salesforce User Preferences Hide Event Calendar Structure
  property_count: 31
  slug: salesforce-user-preferences-hide-event-calendar-structure
- name: Salesforce User Preferences Hide Learning Path Modal Structure
  property_count: 31
  slug: salesforce-user-preferences-hide-learning-path-modal-structure
- name: Salesforce User Preferences Hide Lightning Migration Modal Structure
  property_count: 31
  slug: salesforce-user-preferences-hide-lightning-migration-modal-structure
- name: Salesforce User Preferences Hide Mail App Eap User Guidance Structure
  property_count: 31
  slug: salesforce-user-preferences-hide-mail-app-eap-user-guidance-structure
- name: Salesforce User Preferences Hide Mail App Welcome Mat Structure
  property_count: 31
  slug: salesforce-user-preferences-hide-mail-app-welcome-mat-structure
- name: Salesforce User Preferences Hide S1 Browser Ui Structure
  property_count: 31
  slug: salesforce-user-preferences-hide-s1-browser-ui-structure
- name: Salesforce User Preferences Hide Second Chatter Onboarding Splash Structure
  property_count: 31
  slug: salesforce-user-preferences-hide-second-chatter-onboarding-splash-structure
- name: Salesforce User Preferences Hide Sfx Welcome Mat Structure
  property_count: 31
  slug: salesforce-user-preferences-hide-sfx-welcome-mat-structure
- name: Salesforce User Preferences Hide Task List Views Popover Structure
  property_count: 31
  slug: salesforce-user-preferences-hide-task-list-views-popover-structure
- name: Salesforce User Preferences Hide Trials Celebration Structure
  property_count: 31
  slug: salesforce-user-preferences-hide-trials-celebration-structure
- name: Salesforce User Preferences Hide Trials Welcome Mat Structure
  property_count: 31
  slug: salesforce-user-preferences-hide-trials-welcome-mat-structure
- name: Salesforce User Preferences Jigsaw List User Structure
  property_count: 31
  slug: salesforce-user-preferences-jigsaw-list-user-structure
- name: Salesforce User Preferences Lightning Experience Preferred Structure
  property_count: 31
  slug: salesforce-user-preferences-lightning-experience-preferred-structure
- name: Salesforce User Preferences Ltng Promo Reserved10 User Pref Structure
  property_count: 31
  slug: salesforce-user-preferences-ltng-promo-reserved10-user-pref-structure
- name: Salesforce User Preferences Ltng Promo Reserved16 User Pref Structure
  property_count: 31
  slug: salesforce-user-preferences-ltng-promo-reserved16-user-pref-structure
- name: Salesforce User Preferences Ltng Promo Reserved19 User Pref Structure
  property_count: 31
  slug: salesforce-user-preferences-ltng-promo-reserved19-user-pref-structure
- name: Salesforce User Preferences Native Email Client Structure
  property_count: 31
  slug: salesforce-user-preferences-native-email-client-structure
- name: Salesforce User Preferences New Lightning Report Run Page Enabled Structure
  property_count: 31
  slug: salesforce-user-preferences-new-lightning-report-run-page-enabled-structure
- name: Salesforce User Preferences Path Assistant Collapsed Structure
  property_count: 31
  slug: salesforce-user-preferences-path-assistant-collapsed-structure
- name: Salesforce User Preferences Preview Custom Theme Structure
  property_count: 31
  slug: salesforce-user-preferences-preview-custom-theme-structure
- name: Salesforce User Preferences Preview Lightning Structure
  property_count: 31
  slug: salesforce-user-preferences-preview-lightning-structure
- name: Salesforce User Preferences Read Receipt Last Toggle Value Structure
  property_count: 31
  slug: salesforce-user-preferences-read-receipt-last-toggle-value-structure
- name: Salesforce User Preferences Receive No Notifications As Approver Structure
  property_count: 31
  slug: salesforce-user-preferences-receive-no-notifications-as-approver-structure
- name: Salesforce User Preferences Receive Notifications As Delegated Approver Structure
  property_count: 31
  slug: salesforce-user-preferences-receive-notifications-as-delegated-approver-structure
- name: Salesforce User Preferences Record Home Reserved Wt Shown Structure
  property_count: 31
  slug: salesforce-user-preferences-record-home-reserved-wt-shown-structure
- name: Salesforce User Preferences Record Home Section Collapse Wt Shown Structure
  property_count: 31
  slug: salesforce-user-preferences-record-home-section-collapse-wt-shown-structure
- name: Salesforce User Preferences Reminder Sound Off Structure
  property_count: 31
  slug: salesforce-user-preferences-reminder-sound-off-structure
- name: Salesforce User Preferences Reverse Open Activities View Structure
  property_count: 31
  slug: salesforce-user-preferences-reverse-open-activities-view-structure
- name: Salesforce User Preferences Sales Essentials Setup Assistant Completed Structure
  property_count: 31
  slug: salesforce-user-preferences-sales-essentials-setup-assistant-completed-structure
- name: Salesforce User Preferences Setup Assistant User Pref1 Structure
  property_count: 31
  slug: salesforce-user-preferences-setup-assistant-user-pref1-structure
- name: Salesforce User Preferences Show City To External Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-city-to-external-users-structure
- name: Salesforce User Preferences Show City To Guest Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-city-to-guest-users-structure
- name: Salesforce User Preferences Show Country To External Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-country-to-external-users-structure
- name: Salesforce User Preferences Show Country To Guest Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-country-to-guest-users-structure
- name: Salesforce User Preferences Show Email To External Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-email-to-external-users-structure
- name: Salesforce User Preferences Show Email To Guest Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-email-to-guest-users-structure
- name: Salesforce User Preferences Show Fax To External Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-fax-to-external-users-structure
- name: Salesforce User Preferences Show Fax To Guest Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-fax-to-guest-users-structure
- name: Salesforce User Preferences Show Forecasting Change Signals Structure
  property_count: 31
  slug: salesforce-user-preferences-show-forecasting-change-signals-structure
- name: Salesforce User Preferences Show Manager To External Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-manager-to-external-users-structure
- name: Salesforce User Preferences Show Manager To Guest Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-manager-to-guest-users-structure
- name: Salesforce User Preferences Show Mobile Phone To External Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-mobile-phone-to-external-users-structure
- name: Salesforce User Preferences Show Mobile Phone To Guest Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-mobile-phone-to-guest-users-structure
- name: Salesforce User Preferences Show Postal Code To External Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-postal-code-to-external-users-structure
- name: Salesforce User Preferences Show Postal Code To Guest Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-postal-code-to-guest-users-structure
- name: Salesforce User Preferences Show Profile Pic To Guest Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-profile-pic-to-guest-users-structure
- name: Salesforce User Preferences Show State To External Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-state-to-external-users-structure
- name: Salesforce User Preferences Show State To Guest Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-state-to-guest-users-structure
- name: Salesforce User Preferences Show Street Address To External Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-street-address-to-external-users-structure
- name: Salesforce User Preferences Show Street Address To Guest Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-street-address-to-guest-users-structure
- name: Salesforce User Preferences Show Title To External Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-title-to-external-users-structure
- name: Salesforce User Preferences Show Title To Guest Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-title-to-guest-users-structure
- name: Salesforce User Preferences Show Work Phone To External Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-work-phone-to-external-users-structure
- name: Salesforce User Preferences Show Work Phone To Guest Users Structure
  property_count: 31
  slug: salesforce-user-preferences-show-work-phone-to-guest-users-structure
- name: Salesforce User Preferences Sort Feed By Comment Structure
  property_count: 31
  slug: salesforce-user-preferences-sort-feed-by-comment-structure
- name: Salesforce User Preferences Srh Override Activities Structure
  property_count: 31
  slug: salesforce-user-preferences-srh-override-activities-structure
- name: Salesforce User Preferences Structure
  property_count: 2
  slug: salesforce-user-preferences-structure
- name: Salesforce User Preferences Suppress Event Sfx Reminders Structure
  property_count: 31
  slug: salesforce-user-preferences-suppress-event-sfx-reminders-structure
- name: Salesforce User Preferences Suppress Task Sfx Reminders Structure
  property_count: 31
  slug: salesforce-user-preferences-suppress-task-sfx-reminders-structure
- name: Salesforce User Preferences Task Reminders Checkbox Default Structure
  property_count: 31
  slug: salesforce-user-preferences-task-reminders-checkbox-default-structure
- name: Salesforce User Preferences Today Getting Started Structure
  property_count: 31
  slug: salesforce-user-preferences-today-getting-started-structure
- name: Salesforce User Preferences Trailhead Badge Created Structure
  property_count: 31
  slug: salesforce-user-preferences-trailhead-badge-created-structure
- name: Salesforce User Preferences User Debug Mode Pref Structure
  property_count: 31
  slug: salesforce-user-preferences-user-debug-mode-pref-structure
- name: Salesforce User Role Id Structure
  property_count: 31
  slug: salesforce-user-role-id-structure
- name: Salesforce User Role Structure
  property_count: 6
  slug: salesforce-user-role-structure
- name: Salesforce User Structure
  property_count: 19
  slug: salesforce-user-structure
- name: Salesforce User Type Structure
  property_count: 31
  slug: salesforce-user-type-structure
- name: Salesforce User3 Structure
  property_count: 19
  slug: salesforce-user3-structure
- name: Salesforce User4 Structure
  property_count: 19
  slug: salesforce-user4-structure
- name: Salesforce User7 Structure
  property_count: 23
  slug: salesforce-user7-structure
- name: Salesforce User8 Structure
  property_count: 6
  slug: salesforce-user8-structure
- name: Salesforce Userdata Structure
  property_count: 4
  slug: salesforce-userdata-structure
- name: Salesforce Username Structure
  property_count: 31
  slug: salesforce-username-structure
- name: Salesforce Value Structure
  property_count: 11
  slug: salesforce-value-structure
- name: Salesforce Value2 Structure
  property_count: 11
  slug: salesforce-value2-structure
- name: Salesforce Value22 Structure
  property_count: 10
  slug: salesforce-value22-structure
- name: Salesforce Value6 Structure
  property_count: 4
  slug: salesforce-value6-structure
- name: Salesforce Variable Structure
  property_count: 8
  slug: salesforce-variable-structure
- name: Salesforce Verified Structure
  property_count: 5
  slug: salesforce-verified-structure
- name: Salesforce Version Structure
  property_count: 9
  slug: salesforce-version-structure
- name: Salesforce Version2 Structure
  property_count: 11
  slug: salesforce-version2-structure
- name: Salesforce Version5 Structure
  property_count: 3
  slug: salesforce-version5-structure
- name: Salesforce View Structure
  property_count: 8
  slug: salesforce-view-structure
- name: Salesforce Warnings Structure
  property_count: 2
  slug: salesforce-warnings-structure
- name: Salesforce Website Structure
  property_count: 2
  slug: salesforce-website-structure
- name: Salesforce Website1 Structure
  property_count: 31
  slug: salesforce-website1-structure
- name: Salesforce Website2 Structure
  property_count: 2
  slug: salesforce-website2-structure
- name: Salesforce Website5 Structure
  property_count: 2
  slug: salesforce-website5-structure
- name: Salesforce Work Badge Definition History Structure
  property_count: 6
  slug: salesforce-work-badge-definition-history-structure
- name: Salesforce Year Started Structure
  property_count: 2
  slug: salesforce-year-started-structure
- name: Salesforce Year Started1 Structure
  property_count: 31
  slug: salesforce-year-started1-structure
jsonld:
- class_count: 0
  name: Salesforce Bulk 2 Context
  property_count: 5
  slug: salesforce-bulk-2-context
- class_count: 0
  name: Salesforce Context
  property_count: 1770
  slug: salesforce-context
- class_count: 0
  name: Salesforce Rest Context
  property_count: 8
  slug: salesforce-rest-context
- class_count: 0
  name: Salesforce Ui Context
  property_count: 12
  slug: salesforce-ui-context
layout: provider
mcp_servers:
- description: ''
  name: Salesforce MCP Server
  slug: salesforce-mcp-server
modified: '2026-08-30'
name: Salesforce
nav: Providers
network: true
overview: 'Salesforce publishes 152 APIs on the [APIs.io](https://apis.io/) network, including REST API, SOAP API, Bulk API, and 149 more. Tagged areas include Fortune 500, Artificial Intelligence, Analytics, Cloud, and Commerce.


  The Salesforce catalog on APIs.io includes 3 event-driven AsyncAPI specifications, 4 JSON-LD contexts, and 3 Spectral governance rulesets.


  Salesforce''s developer surface includes authentication, sandbox, changelog, CLI, developer portal, documentation, getting-started guide, and 120 more developer resources.'
plans:
- name: Salesforce Plans Pricing
  plan_count: 6
  slug: salesforce-plans-pricing
press:
- date: '2026-05-25'
  title: Salesforce Newsroom
  url: https://www.salesforce.com/news/
- date: '2026-05-25'
  title: 'Salesforce Investor Relations: Salesforce.com, Inc.'
  url: https://investor.salesforce.com/overview/default.aspx
- date: '2026-05-25'
  title: Press Releases Archives
  url: https://www.salesforce.com/news/content-types/press-releases/
- date: '2026-05-25'
  title: Introducing Salesforce Headless 360. No Browser Required.
  url: https://www.salesforce.com/news/stories/salesforce-headless-360-announcement/
- date: '2026-05-25'
  title: Artificial Intelligence (AI) at Salesforce
  url: https://www.salesforce.com/artificial-intelligence/
- date: '2026-05-21'
  title: How Salesforce Is Scaling Accessibility in the Age of AI
  url: https://www.salesforce.com/news/stories/salesforce-scaling-accessibility-age-of-ai/
- date: '2026-05-21'
  title: 'When AI Becomes Invisible: The Rise of Ambient Intelligence'
  url: https://www.salesforce.com/news/linked-content/when-ai-becomes-invisible-the-rise-of-ambient-intelligence/
- date: '2026-05-21'
  title: 'More than 50,000 Hours Back: What a Year of Manager Agent Taught Us'
  url: https://www.salesforce.com/news/stories/lessons-from-one-year-of-manager-agent/
random_paper: 13
rate_limits:
- limit_count: 9
  name: Salesforce Rate Limits
  slug: salesforce-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Salesforce API Rules
  rule_count: 8
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 7
  slug: salesforce-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Salesforce API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: salesforce-jsonschema-spectral-rules
- effective_rule_count: 69
  extends:
  - spectral:oas
  name: Salesforce API Rules
  rule_count: 28
  severity_counts:
    error: 19
    hint: 0
    info: 3
    warn: 6
  slug: salesforce-spectral-rules
scopes:
- name: Salesforce Scopes
  scope_count: 36
  slug: salesforce-scopes
  summary_line: 36 scopes · authorizationCode
score:
  band: exemplar
  composite: 82.5
  coverage:
    artifact_dirs: 43
    catalog_gap: 23.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 47.0
    contract_quality: 76.2
    developer_ergonomics: 94.6
    discoverability: 75.9
    governance: 47.0
    operational_transparency: 86.8
  previous_composite: 82.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 256
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/salesforce/refs/heads/main/screenshots/salesforce-2026-06-20T193352.png
security:
- kind: authentication
  name: Salesforce Authentication
  slug: salesforce-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Salesforce Domain Security
  slug: salesforce-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Salesforce Vulnerability Disclosure
  slug: salesforce-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Salesforce Trust Center
  slug: salesforce-trust-center
  summary_line: SOC 1 (SSAE 18 / ISAE 3402), SOC 2, SOC 3, ISO 27001, ISO 27017, ISO 27018, ISO 42001 (AI management system), PCI DSS, HIPAA, HITRUST, FedRAMP, TX-RAMP, CSA STAR, NIST, GDPR
slug: salesforce
tags:
- Fortune 500
- Artificial Intelligence
- Analytics
- Cloud
- Commerce
- CRM
- Customer Service
- Enterprise
- Marketing
- Platform
- Sales
use_cases:
- description: Synchronize customer, lead, and opportunity data between Salesforce and external systems.
  name: CRM Data Integration
- description: Load and extract large volumes of records for data warehouse synchronization and ETL workflows.
  name: Bulk Data Migration
- description: Build reactive integrations using platform events and change data capture for real-time data replication.
  name: Event-Driven Architecture
- description: Automate multi-channel marketing journeys and manage subscriber engagement via Marketing Cloud APIs.
  name: Marketing Campaign Orchestration
- description: Deploy Einstein predictions and Agentforce agents for intelligent lead scoring and customer service automation.
  name: AI-Powered Customer Insights
- description: Build Lightning Web Components and custom Apex REST APIs to extend the Salesforce platform.
  name: Custom Application Development
- description: Power headless commerce experiences with shopper APIs for products, baskets, and orders.
  name: Commerce Storefront Integration
- description: Automate metadata deployments and manage org configurations using Metadata and Tooling APIs.
  name: DevOps And CI/CD Automation
website: https://developer.salesforce.com/
---
