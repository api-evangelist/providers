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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.4
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 21
  human_in_the_loop: 1
  name: Servicenow Agentic Access
  operation_count: 44
  slug: servicenow-agentic-access
  summary_line: 44 operations · 21 acting · 1 human-in-the-loop
api_count: 63
apis:
- description: The ServiceNow Batch API enables sending multiple REST API requests in a single HTTP call, reducing network overhead and improving integration performance. Each request in the batch is executed indepe
  name: ServiceNow Batch API
  slug: servicenow-batch-api
- description: The ServiceNow Knowledge Management REST API provides endpoints for searching and retrieving knowledge articles, including most-viewed and featured articles. It supports public and authenticated acces
  name: ServiceNow Knowledge Management API
  slug: servicenow-knowledge-management-api
- description: The ServiceNow Identification and Reconciliation API provides a REST endpoint for creating or updating configuration items (CIs) in the CMDB using the platform's identification and reconciliation engi
  name: ServiceNow Identification and Reconciliation API
  slug: servicenow-identification-reconciliation-api
- description: The ServiceNow Performance Analytics API provides REST endpoints for retrieving performance analytics data including scores, breakdowns, and widget data. It enables integration with external dashboard
  name: ServiceNow Performance Analytics API
  slug: servicenow-performance-analytics-api
- description: ServiceNow Scripted REST APIs allow developers to create custom REST API endpoints on the Now Platform using server-side JavaScript. They support custom request processing logic, authentication, and r
  name: ServiceNow Scripted REST APIs
  slug: servicenow-scripted-rest-apis
- description: The ServiceNow GraphQL API framework allows developers to create custom GraphQL API schemas on the Now Platform for querying record data from components or external systems. It supports defining resol
  name: ServiceNow GraphQL API
  slug: servicenow-graphql-api
- description: The ServiceNow Application Service API provides REST endpoints to create, modify, and update application services in the CMDB. It requires users to have the app_service_admin role and enables programm
  name: ServiceNow Application Service API
  slug: servicenow-application-service-api
- description: The ServiceNow Case API provides REST endpoints for creating, retrieving, and updating Customer Service Management (CSM) case records. It supports the full case lifecycle including case creation, assi
  name: ServiceNow Case API
  slug: servicenow-case-api
- description: The ServiceNow Account API provides REST endpoints for retrieving and managing customer account records within Customer Service Management (CSM). It enables external systems to query and update accoun
  name: ServiceNow Account API
  slug: servicenow-account-api
- description: The ServiceNow Consumer API provides REST endpoints for retrieving and updating CSM consumer records. It supports managing individual consumer profiles and can generate new social media profile record
  name: ServiceNow Consumer API
  slug: servicenow-consumer-api
- description: The ServiceNow CSM Attachment API provides REST endpoints for uploading and managing file attachments on Customer Service Management records such as cases and interactions. It extends the base Attachm
  name: ServiceNow CSM Attachment API
  slug: servicenow-csm-attachment-api
- description: The ServiceNow Email API provides REST endpoints for sending email messages from the Now Platform. It allows external systems and integrations to trigger email notifications and communications through
  name: ServiceNow Email API
  slug: servicenow-email-api
- description: The ServiceNow CI/CD API provides REST endpoints for integrating ServiceNow application development with continuous integration and continuous delivery pipelines. It supports operations such as applyi
  name: ServiceNow CI/CD API
  slug: servicenow-cicd-api
- description: The ServiceNow CI/CD Update Set API provides REST methods to create, retrieve, preview, commit, and back out update sets. It enables automated deployment workflows by allowing CI/CD pipelines to manag
  name: ServiceNow CI/CD Update Set API
  slug: servicenow-cicd-update-set-api
- description: The ServiceNow DevOps API provides REST endpoints for integrating external DevOps toolchains with ServiceNow's DevOps Change Velocity product. It enables automated change request creation, artifact an
  name: ServiceNow DevOps API
  slug: servicenow-devops-api
- description: The ServiceNow DevOps Config API provides REST endpoints for managing DevOps configuration data and policies. It supports configuration validation and compliance checks as part of the DevOps change ac
  name: ServiceNow DevOps Config API
  slug: servicenow-devops-config-api
- description: The ServiceNow CMDB Meta API provides REST endpoints for retrieving metadata about CMDB classes, including their attributes, relationships, and hierarchy. It enables developers to programmatically dis
  name: ServiceNow CMDB Meta API
  slug: servicenow-cmdb-meta-api
- description: The ServiceNow CMDB Data Ingestion API provides REST endpoints for bulk ingesting configuration item data into the CMDB from external data sources. It supports high-volume CI data loading with built-i
  name: ServiceNow CMDB Data Ingestion API
  slug: servicenow-cmdb-data-ingestion-api
- description: The ServiceNow MetricBase Time Series API (formerly Clotho) provides REST endpoints for storing, retrieving, and transforming time series metric data on the Now Platform. It is used by IT Operations M
  name: ServiceNow MetricBase Time Series API
  slug: servicenow-metricbase-time-series-api
- description: The ServiceNow Interaction Management API provides REST endpoints for creating and managing customer interactions across multiple channels. It supports omnichannel routing and enables external contact
  name: ServiceNow Interaction Management API
  slug: servicenow-interaction-management-api
- description: The ServiceNow Voice Interaction Resource API provides REST endpoints for integrating telephony and voice systems with ServiceNow. It enables Contact Center as a Service (CCaaS) providers to manage vo
  name: ServiceNow Voice Interaction Resource API
  slug: servicenow-voice-interaction-resource-api
- description: The ServiceNow User Role Inheritance API provides REST endpoints for querying the role inheritance hierarchy for users and groups. It enables external systems to determine effective roles and permissi
  name: ServiceNow User Role Inheritance API
  slug: servicenow-user-role-inheritance-api
- description: The ServiceNow HR API provides REST endpoints for managing Human Resources Service Delivery (HRSD) data including employee cases, lifecycle events, and HR service requests. It enables integration with
  name: ServiceNow HR API
  slug: servicenow-hr-api
- description: The ServiceNow Event Management Topic Open API provides REST endpoints for managing event topics and subscriptions within IT Operations Management. It enables external monitoring tools to publish even
  name: ServiceNow Event Management Topic Open API
  slug: servicenow-event-management-topic-api
- description: The ServiceNow Predictive Intelligence API provides REST endpoints for accessing machine learning prediction models on the Now Platform. It supports classification, similarity matching, and regression
  name: ServiceNow Predictive Intelligence API
  slug: servicenow-predictive-intelligence-api
- description: The ServiceNow AWA Agent API provides REST endpoints for managing agent availability, presence, and capacity within Advanced Work Assignment (AWA). It enables external systems to query and update agen
  name: ServiceNow AWA Agent API
  slug: servicenow-awa-agent-api
- description: 'The ServiceNow AWA Offer Work API provides REST endpoints to assign or transfer work items to agents through the Advanced Work Assignment engine. It enables programmatic distribution of tasks, cases, '
  name: ServiceNow AWA Offer Work API
  slug: servicenow-awa-offer-work-api
- description: The ServiceNow Virtual Agent Bot Integration API provides REST endpoints for integrating external messaging platforms and chatbot frameworks with ServiceNow Virtual Agent. It enables sending and recei
  name: ServiceNow Virtual Agent Bot Integration API
  slug: servicenow-virtual-agent-bot-integration-api
- description: The ServiceNow Openframe API provides REST endpoints that enable Contact Center as a Service (CCaaS) providers to create and update interaction records without using the Operation Handler. It supports
  name: ServiceNow Openframe API
  slug: servicenow-openframe-api
- description: The ServiceNow AI Assets API provides REST endpoints to retrieve, update, and create AI assets such as systems, data sets, prompts, and models. It supports AI governance and inventory management by en
  name: ServiceNow AI Assets API
  slug: servicenow-ai-assets-api
- description: 'The ServiceNow Lead API provides REST endpoints to create, update, and retrieve marketing leads and their associated lead line items. It enables integration with external marketing automation and CRM '
  name: ServiceNow Lead API
  slug: servicenow-lead-api
- description: The ServiceNow Sales Agreement API provides REST methods for creating new sales agreements and retrieving existing sales agreements by sys_id. It supports contract management workflows within ServiceN
  name: ServiceNow Sales Agreement API
  slug: servicenow-sales-agreement-api
- description: The ServiceNow Agent Client Collector (ACC) API provides REST endpoints for managing agent client collectors used in IT Operations Management. It enables programmatic interaction with ACC agents for d
  name: ServiceNow Agent Client Collector API
  slug: servicenow-agent-client-collector-api
- description: The ServiceNow Agent Mapping API provides REST endpoints for managing agent mapping configurations. It enables external systems to create and manage mappings between external agent identifiers and Ser
  name: ServiceNow Agent Mapping API
  slug: servicenow-agent-mapping-api
- description: The ServiceNow Automation Center API provides REST endpoints for managing and executing automation workflows on the Now Platform. It supports programmatic control of automation tasks, enabling externa
  name: ServiceNow Automation Center API
  slug: servicenow-automation-center-api
- description: The ServiceNow AP Invoice API provides REST endpoints for managing accounts payable invoice records on the Now Platform. It enables external financial systems to create, retrieve, and update invoice d
  name: ServiceNow AP Invoice API
  slug: servicenow-ap-invoice-api
- description: The ServiceNow CSM Order API provides REST endpoints for managing order records within Customer Service Management. It enables external systems to create, retrieve, and update customer orders and asso
  name: ServiceNow CSM Order API
  slug: servicenow-csm-order-api
- description: The ServiceNow CI Lifecycle Management API provides REST endpoints for managing the lifecycle states of configuration items (CIs) in the CMDB. It enables programmatic tracking and transition of CI sta
  name: ServiceNow CI Lifecycle Management API
  slug: servicenow-ci-lifecycle-management-api
- description: The ServiceNow Alarm Management Open API provides REST endpoints for managing alarm records within IT Operations Management. It supports creating, retrieving, and updating alarm data from external mon
  name: ServiceNow Alarm Management Open API
  slug: servicenow-alarm-management-open-api
- description: The ServiceNow SAM Software Usage Data Integration API provides REST endpoints for importing software usage and metering data into Software Asset Management. It enables third-party software usage trac
  name: ServiceNow SAM Software Usage Data Integration API
  slug: servicenow-sam-software-usage-api
- description: The ServiceNow Product Catalog Open API provides REST endpoints for managing product catalog data based on the TM Forum TMF620 specification. It enables querying and managing product specifications, o
  name: ServiceNow Product Catalog Open API
  slug: servicenow-product-catalog-open-api
- description: The ServiceNow Service Catalog Open API provides REST endpoints for managing service catalog data based on the TM Forum TMF633 specification. It supports querying and managing service specifications a
  name: ServiceNow Service Catalog Open API
  slug: servicenow-service-catalog-open-api
- description: The ServiceNow Product Order Open API provides REST endpoints for managing product orders based on the TM Forum TMF622 specification. It enables creating, retrieving, and updating product orders for t
  name: ServiceNow Product Order Open API
  slug: servicenow-product-order-open-api
- description: The ServiceNow Service Order Open API provides REST endpoints for managing service orders based on the TM Forum TMF641 specification. It enables creating, retrieving, and updating service orders for t
  name: ServiceNow Service Order Open API
  slug: servicenow-service-order-open-api
- description: The ServiceNow Resource Inventory Open API provides REST endpoints for managing resource inventory data based on TM Forum specifications. It supports querying and managing physical and logical resourc
  name: ServiceNow Resource Inventory Open API
  slug: servicenow-resource-inventory-open-api
- description: The ServiceNow Product Inventory Open API provides REST endpoints for managing product inventory data based on TM Forum specifications. It supports querying and managing product instances and their li
  name: ServiceNow Product Inventory Open API
  slug: servicenow-product-inventory-open-api
- description: The ServiceNow Service Test Management Open API provides REST endpoints for managing service test records based on TM Forum specifications. It supports creating and managing service test definitions a
  name: ServiceNow Service Test Management Open API
  slug: servicenow-service-test-management-open-api
- description: The ServiceNow Project Portfolio Management API provides REST endpoints for managing projects, demands, and resource plans within Strategic Portfolio Management (SPM). It enables external systems to c
  name: ServiceNow Project Portfolio Management API
  slug: servicenow-project-portfolio-management-api
- description: Operations for computing aggregate statistics on ServiceNow table records including count, sum, average, minimum, and maximum values.
  name: ServiceNow Aggregate Statistics API
  slug: servicenow-aggregate-statistics-api
- description: Operations for uploading, retrieving, listing, and deleting file attachments on ServiceNow records.
  name: ServiceNow Attachments API
  slug: servicenow-attachments-api
- description: Operations for managing the shopping cart and submitting orders.
  name: ServiceNow Cart API
  slug: servicenow-cart-api
- description: Operations for retrieving catalog item details and variables.
  name: ServiceNow Catalog Items API
  slug: servicenow-catalog-items-api
- description: Operations for browsing and retrieving service catalogs.
  name: ServiceNow Catalogs API
  slug: servicenow-catalogs-api
- description: Operations for browsing catalog categories.
  name: ServiceNow Categories API
  slug: servicenow-categories-api
- description: Operations for managing tasks associated with change requests.
  name: ServiceNow Change Tasks API
  slug: servicenow-change-tasks-api
- description: Operations for retrieving configuration item instances from the CMDB by class name.
  name: ServiceNow CMDB Instances API
  slug: servicenow-cmdb-instances-api
- description: Operations for managing Customer Service Management contacts
  name: ServiceNow Contact API
  slug: servicenow-contact-api
- description: Operations for managing emergency change requests that require expedited processing.
  name: ServiceNow Emergency Changes API
  slug: servicenow-emergency-changes-api
- description: Operations for inserting records into import set staging tables and triggering transform map processing.
  name: ServiceNow Import Sets API
  slug: servicenow-import-sets-api
- description: Operations for managing normal change requests that require full review and approval before implementation.
  name: ServiceNow Normal Changes API
  slug: servicenow-normal-changes-api
- description: Operations for managing standard change requests based on pre-approved templates.
  name: ServiceNow Standard Changes API
  slug: servicenow-standard-changes-api
- description: Operations for creating, reading, updating, and deleting records in ServiceNow tables.
  name: ServiceNow Table Records API
  slug: servicenow-table-records-api
- description: Operations for managing trouble tickets (Cases, Incidents, and Service Problem Cases)
  name: ServiceNow Trouble Ticket API
  slug: servicenow-trouble-ticket-api
arazzos:
- description: Find an incident by number, read it, then append a work note and reassign it.
  name: ServiceNow Add Incident Work Note
  slug: servicenow-add-incident-worknote-workflow
- description: Find the oldest unassigned task on a table, claim it, then mark it work in progress.
  name: ServiceNow Assign Open Task
  slug: servicenow-assign-open-tasks-workflow
- description: Insert multiple records into an import set staging table, then verify the first transformed row.
  name: ServiceNow Bulk Import Records
  slug: servicenow-bulk-import-records-workflow
- description: Add a catalog item to the cart, review the cart contents, then submit the order.
  name: ServiceNow Cart Checkout
  slug: servicenow-cart-checkout-workflow
- description: Create a change task on a change, list the change's tasks, then update the task.
  name: ServiceNow Add Task to Change Request
  slug: servicenow-change-add-task-workflow
- description: Find a problem by number, read it, then close it with a resolution code and notes.
  name: ServiceNow Close Problem
  slug: servicenow-close-problem-workflow
- description: Create a normal change request, read it back, then move it through approval.
  name: ServiceNow Create and Approve Normal Change
  slug: servicenow-create-change-request-then-approve-workflow
- description: Create an emergency change request, read it back, then attach an implementation task.
  name: ServiceNow Create Emergency Change With Task
  slug: servicenow-create-emergency-change-workflow
- description: Create an incident via the Table API, read it back, then update its state and assignment.
  name: ServiceNow Create Incident Then Triage
  slug: servicenow-create-incident-then-update-workflow
- description: Read a source incident, open a problem record from it, then link the incident to the problem.
  name: ServiceNow Create Problem From Incident
  slug: servicenow-create-problem-from-incident-workflow
- description: Create a trouble ticket, read it back by id, then update its status and severity.
  name: ServiceNow Create Trouble Ticket Then Update
  slug: servicenow-create-trouble-ticket-then-update-workflow
- description: Find an open trouble ticket by type, read it, then raise its severity to escalate.
  name: ServiceNow Escalate Trouble Ticket
  slug: servicenow-escalate-trouble-ticket-workflow
- description: Insert a record into an import set staging table, then read the transformed target record.
  name: ServiceNow Import Set Load and Verify
  slug: servicenow-import-set-load-workflow
- description: Count open incidents grouped by priority, then list the matching backlog records.
  name: ServiceNow Incident Backlog Report
  slug: servicenow-incident-backlog-report-workflow
- description: Create an incident, attach a file to it via multipart upload, then confirm the attachment.
  name: ServiceNow Incident With Attachment
  slug: servicenow-incident-with-attachment-workflow
- description: Find a CI by name in a CMDB class, fetch its full record, then attach it to an incident.
  name: ServiceNow Link Configuration Item to Incident
  slug: servicenow-link-ci-to-incident-workflow
- description: Create a CSM contact, fetch it by its new sys_id, then open a welcome incident for it.
  name: ServiceNow Onboard Contact
  slug: servicenow-onboard-contact-workflow
- description: Look up a catalog item, read its details, then order it immediately.
  name: ServiceNow Order Catalog Item
  slug: servicenow-order-catalog-item-workflow
- description: Create a knowledge article draft on the kb_knowledge table, read it, then publish it.
  name: ServiceNow Publish Knowledge Article
  slug: servicenow-publish-knowledge-article-workflow
- description: Find an open incident by number, read it, then resolve it with a close code and notes.
  name: ServiceNow Resolve Incident
  slug: servicenow-resolve-incident-workflow
- description: List standard change models, create a change from a template, then read it back.
  name: ServiceNow Standard Change From Template
  slug: servicenow-standard-change-from-template-workflow
- description: Exercise the full Table API CRUD lifecycle — create, read, update, then delete a record.
  name: ServiceNow Table Record Lifecycle
  slug: servicenow-table-record-crud-workflow
- description: List CIs in a class, fetch one's full record, then update its attributes via the Table API.
  name: ServiceNow Update Configuration Item Attributes
  slug: servicenow-update-ci-attributes-workflow
- description: Find a CSM contact by email and update it if it exists, otherwise create it.
  name: ServiceNow Upsert Contact
  slug: servicenow-upsert-contact-workflow
artifact_total: 303
asyncapis:
- description: ServiceNow supports outbound event-driven integrations through business rules, event management, and outbound REST messages. When records are created, updated, or deleted in ServiceNow tables, busines
  name: ServiceNow Events and Notifications
  slug: servicenow-events-asyncapi
collections:
- collection_type: postman
  name: ServiceNow Contact API
  slug: postman-contact-api
- collection_type: postman
  name: ServiceNow Aggregate API
  slug: postman-servicenow-aggregate-api
- collection_type: postman
  name: ServiceNow Attachment API
  slug: postman-servicenow-attachment-api
- collection_type: postman
  name: ServiceNow Change Management API
  slug: postman-servicenow-change-management-api
- collection_type: postman
  name: ServiceNow CMDB Instance API
  slug: postman-servicenow-cmdb-instance-api
- collection_type: postman
  name: ServiceNow Import Set API
  slug: postman-servicenow-import-set-api
- collection_type: postman
  name: ServiceNow Service Catalog API
  slug: postman-servicenow-service-catalog-api
- collection_type: postman
  name: ServiceNow Table API
  slug: postman-servicenow-table-api
- collection_type: postman
  name: ServiceNow Trouble Ticket Open API
  slug: postman-trouble-ticket
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ServiceNow Aggregate API
  slug: open-servicenow-aggregate-api
- collection_type: open
  name: ServiceNow Aggregate Statistics API
  slug: open-servicenow-aggregate-statistics-api
- collection_type: open
  name: ServiceNow Attachment API
  slug: open-servicenow-attachment-api
- collection_type: open
  name: ServiceNow Attachments API
  slug: open-servicenow-attachments-api
- collection_type: open
  name: ServiceNow Cart API
  slug: open-servicenow-cart-api
- collection_type: open
  name: ServiceNow Catalog Items API
  slug: open-servicenow-catalog-items-api
- collection_type: open
  name: ServiceNow Catalogs API
  slug: open-servicenow-catalogs-api
- collection_type: open
  name: ServiceNow Categories API
  slug: open-servicenow-categories-api
- collection_type: open
  name: ServiceNow Change Management API
  slug: open-servicenow-change-management-api
- collection_type: open
  name: ServiceNow Change Tasks API
  slug: open-servicenow-change-tasks-api
- collection_type: open
  name: ServiceNow CMDB Instance API
  slug: open-servicenow-cmdb-instance-api
- collection_type: open
  name: ServiceNow CMDB Instances API
  slug: open-servicenow-cmdb-instances-api
- collection_type: open
  name: ServiceNow Contact API
  slug: open-servicenow-contact-api
- collection_type: open
  name: ServiceNow Emergency Changes API
  slug: open-servicenow-emergency-changes-api
- collection_type: open
  name: ServiceNow Import Set API
  slug: open-servicenow-import-set-api
- collection_type: open
  name: ServiceNow Import Sets API
  slug: open-servicenow-import-sets-api
- collection_type: open
  name: ServiceNow Normal Changes API
  slug: open-servicenow-normal-changes-api
- collection_type: open
  name: ServiceNow Service Catalog API
  slug: open-servicenow-service-catalog-api
- collection_type: open
  name: ServiceNow Standard Changes API
  slug: open-servicenow-standard-changes-api
- collection_type: open
  name: ServiceNow Table API
  slug: open-servicenow-table-api
- collection_type: open
  name: ServiceNow Table Records API
  slug: open-servicenow-table-records-api
- collection_type: open
  name: ServiceNow Trouble Ticket API
  slug: open-servicenow-trouble-ticket-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/servicenow-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/servicenow-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/servicenow-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/servicenow-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/servicenow-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/servicenow-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/servicenow-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/servicenow-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/servicenow-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/servicenow-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/servicenow-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/servicenow-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/servicenow-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/servicenow-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/servicenow-sandbox.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/servicenow-trust-center.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/servicenow-table-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/servicenow-aggregate-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/servicenow-attachment-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/servicenow-change-management-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/servicenow-cmdb-instance-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/servicenow-import-set-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/servicenow-service-catalog-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/servicenow-contact-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/servicenow-trouble-ticket-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/servicenow/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-add-incident-worknote-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-assign-open-tasks-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-bulk-import-records-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-cart-checkout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-change-add-task-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-close-problem-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-create-change-request-then-approve-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-create-emergency-change-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-create-incident-then-update-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-create-problem-from-incident-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-create-trouble-ticket-then-update-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-escalate-trouble-ticket-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-import-set-load-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-incident-backlog-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-incident-with-attachment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-link-ci-to-incident-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-onboard-contact-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-order-catalog-item-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-publish-knowledge-article-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-resolve-incident-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-standard-change-from-template-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-table-record-crud-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-update-ci-attributes-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/servicenow-upsert-contact-workflow.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/servicenow-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/servicenow-incident-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/servicenow-change-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/servicenow-configuration-item-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/servicenow-catalog-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/servicenow-user-schema.json
- group: company
  title: ''
  type: Website
  url: https://www.servicenow.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.servicenow.com
- group: company
  title: ''
  type: Blog
  url: https://www.servicenow.com/community/developer-blog/bg-p/developer-blog
- group: other
  title: ''
  type: Events
  url: https://www.servicenow.com/community/events/ct-p/TopLevel_Events
- group: operate
  title: ''
  type: Forums
  url: https://www.servicenow.com/community/developer-forum/bd-p/developer-forum
- group: operate
  title: ''
  type: Community
  url: https://www.servicenow.com/community/
- group: docs
  title: ''
  type: Documentation
  url: https://www.servicenow.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_RESTAPI.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.servicenow.com/dev.do#!/learn/learning-plans/tokyo/new_to_servicenow/app_store_learnv2_rest_tokyo_rest_api_explorer
- group: auth
  title: ''
  type: Authentication
  url: https://www.servicenow.com/docs/bundle/yokohama-platform-security/page/administer/security/concept/c_OAuthApplications.html
- group: operate
  title: ''
  type: RateLimits
  url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_RESTAPI.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.servicenow.com
- group: operate
  title: ''
  type: Support
  url: https://support.servicenow.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.servicenow.com/products/pricing.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.servicenow.com/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.servicenow.com/privacy-statement.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.servicenow.com/docs/bundle/yokohama-release-notes/page/release-notes/family-release-notes.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ServiceNow
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ServiceNowDevProgram
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/ServiceNow/sdk
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@servicenow/sdk
- group: docs
  title: ''
  type: Documentation
  url: https://www.servicenow.com/docs/bundle/yokohama-application-development/page/build/servicenow-sdk/concept/servicenow-sdk-landing.html
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/servicenow
- group: start
  title: ''
  type: Signup
  url: https://developer.servicenow.com/dev.do
- group: start
  title: ''
  type: Login
  url: https://developer.servicenow.com/dev.do
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/serviceaborad
- group: operate
  title: ''
  type: RateLimits
  url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/inbound-REST-API-rate-limiting.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/use-REST-API-Explorer.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/task/export-openapi-specification.html
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/ServiceNow/PySNC
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/pysnc/
- group: docs
  title: ''
  type: Documentation
  url: https://servicenow.github.io/PySNC/
- group: auth
  title: ''
  type: Authentication
  url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/task/t_EnableOAuthWithREST.html
- group: other
  title: ''
  type: X
  url: https://x.com/ServiceNow
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/servicenow
- group: start
  title: ''
  type: GettingStarted
  url: https://www.servicenow.com/university/training-and-certification.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.servicenow.com/products/api-integrations.html
- group: docs
  title: ''
  type: APIReference
  url: https://developer.servicenow.com/dev.do#!/reference/api/yokohama/rest/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/contact-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/servicenow-aggregate-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/servicenow-attachment-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/servicenow-change-management-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/servicenow-cmdb-instance-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/servicenow-import-set-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/servicenow-service-catalog-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/servicenow-table-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/trouble-ticket-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/servicenow-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/servicenow-vocabulary.yaml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/ServiceNow/saai-skill-feedback
created: '2025-01-08'
description: ServiceNow provides cloud-based platform services that automate enterprise IT operations.
examples:
- key_count: 56
  name: Contact Contact Create Example
  slug: contact-contact-create-example
- key_count: 65
  name: Contact Contact Example
  slug: contact-contact-example
- key_count: 1
  name: Contact Error Example
  slug: contact-error-example
- key_count: 2
  name: Servicenow Aggregate Aggregate Result Example
  slug: servicenow-aggregate-aggregate-result-example
- key_count: 1
  name: Servicenow Aggregate Error Example
  slug: servicenow-aggregate-error-example
- key_count: 16
  name: Servicenow Attachment Attachment Example
  slug: servicenow-attachment-attachment-example
- key_count: 1
  name: Servicenow Attachment Error Example
  slug: servicenow-attachment-error-example
- key_count: 21
  name: Servicenow Change Management Change Request Example
  slug: servicenow-change-management-change-request-example
- key_count: 16
  name: Servicenow Change Management Change Request Input Example
  slug: servicenow-change-management-change-request-input-example
- key_count: 8
  name: Servicenow Change Management Change Task Example
  slug: servicenow-change-management-change-task-example
- key_count: 6
  name: Servicenow Change Management Change Task Input Example
  slug: servicenow-change-management-change-task-input-example
- key_count: 1
  name: Servicenow Change Management Error Example
  slug: servicenow-change-management-error-example
- key_count: 26
  name: Servicenow Cmdb Instance Cmdb Instance Example
  slug: servicenow-cmdb-instance-cmdb-instance-example
- key_count: 2
  name: Servicenow Cmdb Instance Cmdb Instance Summary Example
  slug: servicenow-cmdb-instance-cmdb-instance-summary-example
- key_count: 1
  name: Servicenow Cmdb Instance Error Example
  slug: servicenow-cmdb-instance-error-example
- key_count: 1
  name: Servicenow Import Set Error Example
  slug: servicenow-import-set-error-example
- key_count: 0
  name: Servicenow Import Set Import Set Input Example
  slug: servicenow-import-set-import-set-input-example
- key_count: 10
  name: Servicenow Import Set Import Set Result Example
  slug: servicenow-import-set-import-set-result-example
- key_count: 2
  name: Servicenow Service Catalog Cart Example
  slug: servicenow-service-catalog-cart-example
- key_count: 4
  name: Servicenow Service Catalog Cart Item Example
  slug: servicenow-service-catalog-cart-item-example
- key_count: 2
  name: Servicenow Service Catalog Cart Item Input Example
  slug: servicenow-service-catalog-cart-item-input-example
- key_count: 5
  name: Servicenow Service Catalog Catalog Example
  slug: servicenow-service-catalog-catalog-example
- key_count: 10
  name: Servicenow Service Catalog Catalog Item Detail Example
  slug: servicenow-service-catalog-catalog-item-detail-example
- key_count: 6
  name: Servicenow Service Catalog Catalog Item Example
  slug: servicenow-service-catalog-catalog-item-example
- key_count: 6
  name: Servicenow Service Catalog Catalog Variable Example
  slug: servicenow-service-catalog-catalog-variable-example
- key_count: 5
  name: Servicenow Service Catalog Category Example
  slug: servicenow-service-catalog-category-example
- key_count: 1
  name: Servicenow Service Catalog Error Example
  slug: servicenow-service-catalog-error-example
- key_count: 3
  name: Servicenow Service Catalog Order Result Example
  slug: servicenow-service-catalog-order-result-example
- key_count: 1
  name: Servicenow Table Error Example
  slug: servicenow-table-error-example
- key_count: 8
  name: Servicenow Table Record Example
  slug: servicenow-table-record-example
- key_count: 0
  name: Servicenow Table Record Input Example
  slug: servicenow-table-record-input-example
- key_count: 1
  name: Trouble Ticket Channel Example
  slug: trouble-ticket-channel-example
- key_count: 1
  name: Trouble Ticket Channel Input Example
  slug: trouble-ticket-channel-input-example
- key_count: 1
  name: Trouble Ticket Error Example
  slug: trouble-ticket-error-example
- key_count: 4
  name: Trouble Ticket Note Example
  slug: trouble-ticket-note-example
- key_count: 2
  name: Trouble Ticket Note Input Example
  slug: trouble-ticket-note-input-example
- key_count: 6
  name: Trouble Ticket Related Entity Example
  slug: trouble-ticket-related-entity-example
- key_count: 2
  name: Trouble Ticket Related Entity Input Example
  slug: trouble-ticket-related-entity-input-example
- key_count: 3
  name: Trouble Ticket Related Party Example
  slug: trouble-ticket-related-party-example
- key_count: 2
  name: Trouble Ticket Related Party Input Example
  slug: trouble-ticket-related-party-input-example
- key_count: 9
  name: Trouble Ticket Trouble Ticket Create Example
  slug: trouble-ticket-trouble-ticket-create-example
- key_count: 14
  name: Trouble Ticket Trouble Ticket Example
  slug: trouble-ticket-trouble-ticket-example
- key_count: 8
  name: Trouble Ticket Trouble Ticket Update Example
  slug: trouble-ticket-trouble-ticket-update-example
features:
- description: Universal Table API for CRUD operations on any ServiceNow table including incidents, changes, and custom tables.
  name: Table-Driven Architecture
- description: Complete ITSM capabilities with dedicated APIs for incident, change, problem, and knowledge management.
  name: IT Service Management
- description: CMDB APIs for managing configuration items, relationships, and service mappings with identification and reconciliation.
  name: Configuration Management Database
- description: Service Catalog APIs for browsing items, submitting requests, and managing cart operations.
  name: Service Catalog And Self-Service
- description: CSM APIs for cases, contacts, accounts, and consumer management with omnichannel routing.
  name: Customer Service Management
- description: AWA APIs for intelligent work routing, agent management, and capacity-based assignment.
  name: Advanced Work Assignment
- description: Bot Integration APIs for connecting external messaging platforms with ServiceNow conversational AI.
  name: Virtual Agent Integration
- description: CI/CD and DevOps APIs for automated application deployment, testing, and change velocity management.
  name: CI/CD And DevOps
- description: Event Management APIs for ingesting alerts and events from external monitoring systems.
  name: Event Management
- description: ML-powered APIs for automated classification, assignment, and prioritization of records.
  name: Predictive Intelligence
finops:
- name: Servicenow Finops
  service_category: Enterprise Workflow / Now Platform
  slug: servicenow-finops
graphqls:
- description: The ServiceNow GraphQL API framework allows developers to create custom GraphQL API schemas on the Now Platform for querying record data from components or external systems. It supports defining resol
  name: ServiceNow GraphQL API
  slug: servicenow-graphql
image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
integrations:
- description: Bidirectional synchronization of incidents and issues between ServiceNow and Atlassian Jira.
  name: Jira
- description: Virtual Agent and notification integration for managing IT requests directly from Microsoft Teams.
  name: Microsoft Teams
- description: Conversational IT support and incident management through Slack channel integrations.
  name: Slack
- description: CI/CD pipeline integration for automated change request creation and deployment tracking.
  name: Jenkins
- description: DevOps pipeline integration for change velocity and automated deployment workflows.
  name: Azure DevOps
- description: Event and alert ingestion from Splunk for centralized IT operations monitoring.
  name: Splunk
- description: Incident alerting and on-call management integration for streamlined incident response.
  name: PagerDuty
- description: Cloud resource discovery and CMDB synchronization for AWS infrastructure management.
  name: AWS
json_schemas:
- name: ContactCreate
  property_count: 56
  slug: contact-contact-create
- name: Contact
  property_count: 65
  slug: contact-contact
- name: Error
  property_count: 1
  slug: contact-error
- name: AggregateResult
  property_count: 2
  slug: servicenow-aggregate-aggregate-result
- name: Error
  property_count: 1
  slug: servicenow-aggregate-error
- name: Attachment
  property_count: 16
  slug: servicenow-attachment-attachment
- name: Error
  property_count: 1
  slug: servicenow-attachment-error
- name: ServiceNow Catalog Request
  property_count: 17
  slug: servicenow-catalog-request
- name: ChangeRequestInput
  property_count: 16
  slug: servicenow-change-management-change-request-input
- name: ChangeRequest
  property_count: 21
  slug: servicenow-change-management-change-request
- name: ChangeTaskInput
  property_count: 6
  slug: servicenow-change-management-change-task-input
- name: ChangeTask
  property_count: 8
  slug: servicenow-change-management-change-task
- name: Error
  property_count: 1
  slug: servicenow-change-management-error
- name: ServiceNow Change Request
  property_count: 39
  slug: servicenow-change-request
- name: CmdbInstance
  property_count: 26
  slug: servicenow-cmdb-instance-cmdb-instance
- name: CmdbInstanceSummary
  property_count: 2
  slug: servicenow-cmdb-instance-cmdb-instance-summary
- name: Error
  property_count: 1
  slug: servicenow-cmdb-instance-error
- name: ServiceNow Configuration Item
  property_count: 44
  slug: servicenow-configuration-item
- name: Error
  property_count: 1
  slug: servicenow-import-set-error
- name: ImportSetInput
  property_count: 0
  slug: servicenow-import-set-import-set-input
- name: ImportSetResult
  property_count: 10
  slug: servicenow-import-set-import-set-result
- name: ServiceNow Incident
  property_count: 45
  slug: servicenow-incident
- name: CartItemInput
  property_count: 2
  slug: servicenow-service-catalog-cart-item-input
- name: CartItem
  property_count: 4
  slug: servicenow-service-catalog-cart-item
- name: Cart
  property_count: 2
  slug: servicenow-service-catalog-cart
- name: CatalogItemDetail
  property_count: 10
  slug: servicenow-service-catalog-catalog-item-detail
- name: CatalogItem
  property_count: 6
  slug: servicenow-service-catalog-catalog-item
- name: Catalog
  property_count: 5
  slug: servicenow-service-catalog-catalog
- name: CatalogVariable
  property_count: 6
  slug: servicenow-service-catalog-catalog-variable
- name: Category
  property_count: 5
  slug: servicenow-service-catalog-category
- name: Error
  property_count: 1
  slug: servicenow-service-catalog-error
- name: OrderResult
  property_count: 3
  slug: servicenow-service-catalog-order-result
- name: Error
  property_count: 1
  slug: servicenow-table-error
- name: RecordInput
  property_count: 0
  slug: servicenow-table-record-input
- name: Record
  property_count: 8
  slug: servicenow-table-record
- name: ServiceNow User
  property_count: 30
  slug: servicenow-user
- name: ChannelInput
  property_count: 1
  slug: trouble-ticket-channel-input
- name: Channel
  property_count: 1
  slug: trouble-ticket-channel
- name: Error
  property_count: 1
  slug: trouble-ticket-error
- name: NoteInput
  property_count: 2
  slug: trouble-ticket-note-input
- name: Note
  property_count: 4
  slug: trouble-ticket-note
- name: RelatedEntityInput
  property_count: 2
  slug: trouble-ticket-related-entity-input
- name: RelatedEntity
  property_count: 6
  slug: trouble-ticket-related-entity
- name: RelatedPartyInput
  property_count: 2
  slug: trouble-ticket-related-party-input
- name: RelatedParty
  property_count: 3
  slug: trouble-ticket-related-party
- name: TroubleTicketCreate
  property_count: 9
  slug: trouble-ticket-trouble-ticket-create
- name: TroubleTicket
  property_count: 14
  slug: trouble-ticket-trouble-ticket
- name: TroubleTicketUpdate
  property_count: 8
  slug: trouble-ticket-trouble-ticket-update
json_structures:
- name: Contact Contact Create Structure
  property_count: 56
  slug: contact-contact-create-structure
- name: Contact Contact Structure
  property_count: 65
  slug: contact-contact-structure
- name: Contact Error Structure
  property_count: 1
  slug: contact-error-structure
- name: Servicenow Aggregate Aggregate Result Structure
  property_count: 2
  slug: servicenow-aggregate-aggregate-result-structure
- name: Servicenow Aggregate Error Structure
  property_count: 1
  slug: servicenow-aggregate-error-structure
- name: Servicenow Attachment Attachment Structure
  property_count: 16
  slug: servicenow-attachment-attachment-structure
- name: Servicenow Attachment Error Structure
  property_count: 1
  slug: servicenow-attachment-error-structure
- name: Servicenow Change Management Change Request Input Structure
  property_count: 16
  slug: servicenow-change-management-change-request-input-structure
- name: Servicenow Change Management Change Request Structure
  property_count: 21
  slug: servicenow-change-management-change-request-structure
- name: Servicenow Change Management Change Task Input Structure
  property_count: 6
  slug: servicenow-change-management-change-task-input-structure
- name: Servicenow Change Management Change Task Structure
  property_count: 8
  slug: servicenow-change-management-change-task-structure
- name: Servicenow Change Management Error Structure
  property_count: 1
  slug: servicenow-change-management-error-structure
- name: Servicenow Cmdb Instance Cmdb Instance Structure
  property_count: 26
  slug: servicenow-cmdb-instance-cmdb-instance-structure
- name: Servicenow Cmdb Instance Cmdb Instance Summary Structure
  property_count: 2
  slug: servicenow-cmdb-instance-cmdb-instance-summary-structure
- name: Servicenow Cmdb Instance Error Structure
  property_count: 1
  slug: servicenow-cmdb-instance-error-structure
- name: Servicenow Import Set Error Structure
  property_count: 1
  slug: servicenow-import-set-error-structure
- name: Servicenow Import Set Import Set Input Structure
  property_count: 0
  slug: servicenow-import-set-import-set-input-structure
- name: Servicenow Import Set Import Set Result Structure
  property_count: 10
  slug: servicenow-import-set-import-set-result-structure
- name: Servicenow Service Catalog Cart Item Input Structure
  property_count: 2
  slug: servicenow-service-catalog-cart-item-input-structure
- name: Servicenow Service Catalog Cart Item Structure
  property_count: 4
  slug: servicenow-service-catalog-cart-item-structure
- name: Servicenow Service Catalog Cart Structure
  property_count: 2
  slug: servicenow-service-catalog-cart-structure
- name: Servicenow Service Catalog Catalog Item Detail Structure
  property_count: 10
  slug: servicenow-service-catalog-catalog-item-detail-structure
- name: Servicenow Service Catalog Catalog Item Structure
  property_count: 6
  slug: servicenow-service-catalog-catalog-item-structure
- name: Servicenow Service Catalog Catalog Structure
  property_count: 5
  slug: servicenow-service-catalog-catalog-structure
- name: Servicenow Service Catalog Catalog Variable Structure
  property_count: 6
  slug: servicenow-service-catalog-catalog-variable-structure
- name: Servicenow Service Catalog Category Structure
  property_count: 5
  slug: servicenow-service-catalog-category-structure
- name: Servicenow Service Catalog Error Structure
  property_count: 1
  slug: servicenow-service-catalog-error-structure
- name: Servicenow Service Catalog Order Result Structure
  property_count: 3
  slug: servicenow-service-catalog-order-result-structure
- name: Servicenow Table Error Structure
  property_count: 1
  slug: servicenow-table-error-structure
- name: Servicenow Table Record Input Structure
  property_count: 0
  slug: servicenow-table-record-input-structure
- name: Servicenow Table Record Structure
  property_count: 8
  slug: servicenow-table-record-structure
- name: Trouble Ticket Channel Input Structure
  property_count: 1
  slug: trouble-ticket-channel-input-structure
- name: Trouble Ticket Channel Structure
  property_count: 1
  slug: trouble-ticket-channel-structure
- name: Trouble Ticket Error Structure
  property_count: 1
  slug: trouble-ticket-error-structure
- name: Trouble Ticket Note Input Structure
  property_count: 2
  slug: trouble-ticket-note-input-structure
- name: Trouble Ticket Note Structure
  property_count: 4
  slug: trouble-ticket-note-structure
- name: Trouble Ticket Related Entity Input Structure
  property_count: 2
  slug: trouble-ticket-related-entity-input-structure
- name: Trouble Ticket Related Entity Structure
  property_count: 6
  slug: trouble-ticket-related-entity-structure
- name: Trouble Ticket Related Party Input Structure
  property_count: 2
  slug: trouble-ticket-related-party-input-structure
- name: Trouble Ticket Related Party Structure
  property_count: 3
  slug: trouble-ticket-related-party-structure
- name: Trouble Ticket Trouble Ticket Create Structure
  property_count: 9
  slug: trouble-ticket-trouble-ticket-create-structure
- name: Trouble Ticket Trouble Ticket Structure
  property_count: 14
  slug: trouble-ticket-trouble-ticket-structure
- name: Trouble Ticket Trouble Ticket Update Structure
  property_count: 8
  slug: trouble-ticket-trouble-ticket-update-structure
jsonld:
- class_count: 0
  name: Contact Context
  property_count: 3
  slug: contact-context
- class_count: 0
  name: Servicenow Aggregate Context
  property_count: 2
  slug: servicenow-aggregate-context
- class_count: 0
  name: Servicenow Attachment Context
  property_count: 2
  slug: servicenow-attachment-context
- class_count: 0
  name: Servicenow Change Management Context
  property_count: 5
  slug: servicenow-change-management-context
- class_count: 0
  name: Servicenow Cmdb Instance Context
  property_count: 3
  slug: servicenow-cmdb-instance-context
- class_count: 7
  name: Servicenow Context
  property_count: 8
  slug: servicenow-context
- class_count: 0
  name: Servicenow Import Set Context
  property_count: 2
  slug: servicenow-import-set-context
- class_count: 0
  name: Servicenow Service Catalog Context
  property_count: 10
  slug: servicenow-service-catalog-context
- class_count: 0
  name: Servicenow Table Context
  property_count: 2
  slug: servicenow-table-context
- class_count: 0
  name: Trouble Ticket Context
  property_count: 12
  slug: trouble-ticket-context
layout: provider
mcp_servers:
- description: ''
  name: servicenow-mcp.yml
  slug: servicenow-mcpyml
modified: '2026-06-20'
name: ServiceNow
nav: Providers
network: true
overview: 'ServiceNow publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Event Management Topic Open API, Aggregate Statistics API, Attachments API, and 13 more. Tagged areas include Automation, Cloud Services, Digital Workflows, Enterprise Platform, and IT Service Management.


  The ServiceNow catalog on APIs.io includes 1 event-driven AsyncAPI specification, 10 JSON-LD contexts, and 3 Spectral governance rulesets.


  ServiceNow''s developer surface includes authentication, CLI, changelog, sandbox, developer portal, engineering blog, documentation, and 99 more developer resources.'
plans:
- name: Servicenow Plans Pricing
  plan_count: 1
  slug: servicenow-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Servicenow Rate Limits
  slug: servicenow-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: ServiceNow API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: servicenow-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: ServiceNow API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: servicenow-jsonschema-spectral-rules
- effective_rule_count: 68
  extends:
  - spectral:oas
  name: ServiceNow API Rules
  rule_count: 27
  severity_counts:
    error: 19
    hint: 0
    info: 1
    warn: 7
  slug: servicenow-spectral-rules
scopes:
- name: Servicenow Scopes
  scope_count: 0
  slug: servicenow-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 66.9
  delta: -3.6
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 43.2
    contract_quality: 73.1
    developer_ergonomics: 90.5
    discoverability: 66.7
    governance: 43.2
    operational_transparency: 42.1
  previous_composite: 70.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/servicenow/refs/heads/main/screenshots/servicenow-2026-06-20T193735.png
security:
- kind: authentication
  name: Servicenow Authentication
  slug: servicenow-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Servicenow Domain Security
  slug: servicenow-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Servicenow Trust Center
  slug: servicenow-trust-center
  summary_line: SOC 2 Type II, ISO 27001:2022, ISO 27017, ISO 27018, FedRAMP (High P-ATO, first achieved 2019), IRAP
slug: servicenow
tags:
- Automation
- Cloud Services
- Digital Workflows
- Enterprise Platform
- IT Service Management
- ITSM
- Processes
- T1
- Workflow Automation
- Workflows
use_cases:
- description: Automate incident creation, assignment, escalation, and resolution through Table and Predictive Intelligence APIs.
  name: Incident Management Automation
- description: Integrate external CI/CD pipelines with ServiceNow change management for automated change request workflows.
  name: Change Management Integration
- description: Keep the CMDB in sync with external discovery and monitoring tools using Identification and Reconciliation APIs.
  name: CMDB Synchronization
- description: Build custom portals that browse service catalogs, submit requests, and track order status.
  name: Self-Service Portal Integration
- description: Manage customer cases, contacts, and interactions across channels with CSM and Virtual Agent APIs.
  name: Customer Service Orchestration
- description: Ingest events and metrics from monitoring tools for centralized alert management and correlation.
  name: IT Operations Monitoring
- description: Load data from external sources using Import Set APIs with transform maps for automated field mapping.
  name: Data Migration And ETL
- description: Manage agent availability and route work items based on skills and capacity using AWA APIs.
  name: Workforce Optimization
website: https://www.servicenow.com/
---
