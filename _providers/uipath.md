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
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 33
  human_in_the_loop: 1
  name: Uipath Agentic Access
  operation_count: 79
  slug: uipath-agentic-access
  summary_line: 79 operations · 33 acting · 1 human-in-the-loop
api_count: 32
apis:
- description: Retrieve and manage system and automation alerts
  name: UiPath Alerts API
  slug: uipath-alerts-api
- description: Manage the application inventory used in automation assessments
  name: UiPath AppInventory API
  slug: uipath-appinventory-api
- description: Manage shared assets such as credentials, text values, integers, and boolean values
  name: UiPath Assets API
  slug: uipath-assets-api
- description: Retrieve and download organization and tenant audit event logs
  name: UiPath AuditLogs API
  slug: uipath-auditlogs-api
- description: Manage automation ideas and projects in the pipeline
  name: UiPath Automations API
  slug: uipath-automations-api
- description: Classify documents into predefined document types
  name: UiPath Classification API
  slug: uipath-classification-api
- description: Convert documents into a digitized format for downstream processing
  name: UiPath Digitization API
  slug: uipath-digitization-api
- description: Discover available projects, classifiers, and extractors
  name: UiPath Discovery API
  slug: uipath-discovery-api
- description: Perform CRUD operations on custom data entity records
  name: UiPath Entities API
  slug: uipath-entities-api
- description: Extract structured data fields from documents
  name: UiPath Extraction API
  slug: uipath-extraction-api
- description: Manage organizational folders for grouping automation resources
  name: UiPath Folders API
  slug: uipath-folders-api
- description: Manage user groups and group memberships
  name: UiPath Groups API
  slug: uipath-groups-api
- description: Manage automation job execution, including starting, stopping, and querying job state
  name: UiPath Jobs API
  slug: uipath-jobs-api
- description: Manage license allocations across user groups and services
  name: UiPath Licenses API
  slug: uipath-licenses-api
- description: Manage machine templates and registered physical or virtual machines
  name: UiPath Machines API
  slug: uipath-machines-api
- description: Manage automation package uploads and versions
  name: UiPath Packages API
  slug: uipath-packages-api
- description: Retrieve automation pipeline data and status views
  name: UiPath Pipeline API
  slug: uipath-pipeline-api
- description: Manage automation processes (published packages deployed to folders)
  name: UiPath Processes API
  slug: uipath-processes-api
- description: Manage test projects within Test Manager
  name: UiPath Projects API
  slug: uipath-projects-api
- description: Manage individual queue transaction items and their processing state
  name: UiPath QueueItems API
  slug: uipath-queueitems-api
- description: Manage transaction queues for distributing work items to robots
  name: UiPath Queues API
  slug: uipath-queues-api
- description: Manage requirements and their traceability links to test cases
  name: UiPath Requirements API
  slug: uipath-requirements-api
- description: Manage software robots registered with Orchestrator
  name: UiPath Robots API
  slug: uipath-robots-api
- description: Manage roles and their associated permissions
  name: UiPath Roles API
  slug: uipath-roles-api
- description: Manage time-based and recurring triggers for automation processes
  name: UiPath Schedules API
  slug: uipath-schedules-api
- description: Manage cloud storage buckets for storing automation artifacts
  name: UiPath StorageBuckets API
  slug: uipath-storagebuckets-api
- description: Manage test cases and their definitions
  name: UiPath TestCases API
  slug: uipath-testcases-api
- description: Retrieve test execution results and logs
  name: UiPath TestExecutions API
  slug: uipath-testexecutions-api
- description: Manage test sets that group test cases for execution
  name: UiPath TestSets API
  slug: uipath-testsets-api
- description: Manage users and their roles within Automation Hub
  name: UiPath Users API
  slug: uipath-users-api
- description: Validate and correct digitization, classification, and extraction results
  name: UiPath Validation API
  slug: uipath-validation-api
- description: Manage webhook subscriptions for Orchestrator event notifications
  name: UiPath Webhooks API
  slug: uipath-webhooks-api
arazzos:
- description: Resolve an existing queue, add a transaction item, and read back its status.
  name: UiPath Add and Track a Queue Item
  slug: uipath-add-and-track-queue-item-workflow
- description: Create, read, update, and delete a shared asset end to end.
  name: UiPath Asset Lifecycle
  slug: uipath-asset-lifecycle-workflow
- description: Create a test project, seed a test case and a test set, then read back the project.
  name: UiPath Bootstrap a Test Project
  slug: uipath-bootstrap-test-project-workflow
- description: Locate a webhook by its target URL and delete the subscription.
  name: UiPath Find and Remove a Webhook
  slug: uipath-cleanup-webhook-workflow
- description: Run the full document understanding pipeline with polling for async results.
  name: UiPath Digitize, Classify, and Extract a Document
  slug: uipath-digitize-classify-extract-workflow
- description: Resolve a project, discover its extractors, digitize a document, and extract data with polling.
  name: UiPath Discover Extractors and Extract a Document
  slug: uipath-discover-and-extract-document-workflow
- description: Create, read, update, and delete a custom entity record end to end.
  name: UiPath Data Service Entity Record Lifecycle
  slug: uipath-entity-record-lifecycle-workflow
- description: Resolve a folder, then inventory its machines, robots, and recent jobs.
  name: UiPath Fleet Readiness Audit
  slug: uipath-fleet-readiness-audit-workflow
- description: Create a credential asset and confirm it by reading it back.
  name: UiPath Provision a Credential Asset
  slug: uipath-provision-credential-asset-workflow
- description: Create a transaction queue and seed it with its first work item.
  name: UiPath Provision a Queue and Add an Item
  slug: uipath-provision-queue-and-add-item-workflow
- description: Discover available event types, create a webhook, and confirm its registration.
  name: UiPath Register a Job Event Webhook
  slug: uipath-register-job-webhook-workflow
- description: Resolve a test project, create a requirement and a covering test case, then list test cases.
  name: UiPath Establish Requirement Traceability
  slug: uipath-requirement-traceability-workflow
- description: Resolve a folder context, pick a deployed process, and start a job in it.
  name: UiPath Resolve Folder and Start a Job
  slug: uipath-resolve-folder-start-job-workflow
- description: Read an existing asset, write an updated value, and verify the change.
  name: UiPath Rotate an Asset Value
  slug: uipath-rotate-asset-value-workflow
- description: Start a job for a process and poll its state until it reaches a terminal outcome.
  name: UiPath Start and Monitor a Job
  slug: uipath-start-and-monitor-job-workflow
- description: Locate a currently running job and send it a stop signal.
  name: UiPath Find and Stop a Running Job
  slug: uipath-stop-running-job-workflow
- description: Find a configured schedule, resolve its process, and run it immediately.
  name: UiPath Trigger a Scheduled Process On Demand
  slug: uipath-trigger-scheduled-process-now-workflow
- description: Query an entity by a key field and update the match or create a new record.
  name: UiPath Upsert a Data Service Entity Record
  slug: uipath-upsert-entity-record-workflow
artifact_total: 409
asyncapis:
- description: The UiPath Orchestrator webhook system delivers real-time event notifications to registered HTTP endpoints when automation events occur within the platform. Webhooks cover events for jobs, robots, que
  name: UiPath Orchestrator Webhook Events
  slug: uipath-orchestrator-webhooks-asyncapi
collections:
- collection_type: postman
  name: UiPath Automation Hub API
  slug: postman-uipath-automation-hub
- collection_type: postman
  name: UiPath Data Service API
  slug: postman-uipath-data-service
- collection_type: postman
  name: UiPath Document Understanding API
  slug: postman-uipath-document-understanding
- collection_type: postman
  name: UiPath Orchestrator API
  slug: postman-uipath-orchestrator
- collection_type: postman
  name: UiPath Platform Management API
  slug: postman-uipath-platform-management
- collection_type: postman
  name: UiPath Test Manager API
  slug: postman-uipath-test-manager
- collection_type: open
  name: UiPath Automation Hub API
  slug: open-uipath-automation-hub
- collection_type: open
  name: UiPath Data Service API
  slug: open-uipath-data-service
- collection_type: open
  name: UiPath Document Understanding API
  slug: open-uipath-document-understanding
- collection_type: open
  name: UiPath Orchestrator API
  slug: open-uipath-orchestrator
- collection_type: open
  name: UiPath Platform Management API
  slug: open-uipath-platform-management
- collection_type: open
  name: UiPath Test Manager API
  slug: open-uipath-test-manager
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uipath-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/uipath-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/uipath-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uipath-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uipath-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/uipath/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/uipath-add-and-track-queue-item-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/uipath-asset-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/uipath-bootstrap-test-project-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/uipath-cleanup-webhook-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/uipath-digitize-classify-extract-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/uipath-discover-and-extract-document-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/uipath-entity-record-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/uipath-fleet-readiness-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/uipath-provision-credential-asset-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/uipath-provision-queue-and-add-item-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/uipath-register-job-webhook-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/uipath-requirement-traceability-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/uipath-resolve-folder-start-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/uipath-rotate-asset-value-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/uipath-start-and-monitor-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/uipath-stop-running-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/uipath-trigger-scheduled-process-now-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/uipath-upsert-entity-record-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uipath
- group: company
  title: ''
  type: Website
  url: https://www.uipath.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.uipath.com
- group: start
  title: ''
  type: Portal
  url: https://cloud.uipath.com
- group: company
  title: ''
  type: Blog
  url: https://www.uipath.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.uipath.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uipath.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uipath.com/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://support.uipath.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.uipath.com
- group: learn
  title: ''
  type: Academy
  url: https://academy.uipath.com
- group: operate
  title: ''
  type: Forums
  url: https://forum.uipath.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UiPath
- group: build
  title: Python SDK
  type: SDKs
  url: https://pypi.org/project/uipath/
- group: build
  title: Python SDK GitHub
  type: SDKs
  url: https://github.com/UiPath/uipath-python
- group: build
  title: LangChain Python SDK
  type: SDKs
  url: https://github.com/UiPath/uipath-langchain-python
- group: build
  title: TypeScript SDK
  type: SDKs
  url: https://github.com/UiPath/uipath-typescript
- group: build
  title: Python Integrations SDK
  type: SDKs
  url: https://github.com/UiPath/uipath-integrations-python
- group: build
  title: MCP Server
  type: Tools
  url: https://github.com/UiPath/uipath-mcp-python
- group: build
  title: UiPath CLI
  type: CLI
  url: https://github.com/UiPath/uipathcli
- group: build
  title: ''
  type: CLI
  url: https://docs.uipath.com/automation-cloud/docs/uipath-cli
- group: start
  title: ''
  type: Signup
  url: https://cloud.uipath.com/portal_/cloudrpa
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.uipath.com/automation-cloud/docs/introduction
- group: auth
  title: ''
  type: Authentication
  url: https://docs.uipath.com/automation-cloud/automation-cloud/latest/api-guide/accessing-uipath-resources-using-external-apps
- group: design
  title: ''
  type: SpectralRules
  url: rules/uipath-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/uipath-vocabulary.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/UiPath/uipath-mcp-python
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/UiPath/skills
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.uipath.com/llms.txt
created: '2025-01-01'
description: UiPath is an enterprise automation platform offering robotic process automation (RPA), AI-powered automation, and agentic automation capabilities. The platform includes Orchestrator for managing robots and automation jobs, Studio for developing automation workflows, Document Understanding for intelligent document processing, Data Service for structured data storage, Automation Hub for pipeline management and governance, Test Manager for automated testing, and Platform Management for organization and tenant administration. UiPath provides Python SDKs, REST APIs, and a rich integration ecosystem supporting enterprise automation at scale.
examples:
- key_count: 2
  name: Automation Hub Add User Request Example
  slug: automation-hub-add-user-request-example
- key_count: 2
  name: Automation Hub App Inventory List Response Example
  slug: automation-hub-app-inventory-list-response-example
- key_count: 5
  name: Automation Hub Application Example
  slug: automation-hub-application-example
- key_count: 10
  name: Automation Hub Automation Example
  slug: automation-hub-automation-example
- key_count: 4
  name: Automation Hub Automation List Response Example
  slug: automation-hub-automation-list-response-example
- key_count: 3
  name: Automation Hub Benefit Data Example
  slug: automation-hub-benefit-data-example
- key_count: 4
  name: Automation Hub Collaborator Example
  slug: automation-hub-collaborator-example
- key_count: 4
  name: Automation Hub Create Automation Idea Request Example
  slug: automation-hub-create-automation-idea-request-example
- key_count: 3
  name: Automation Hub Edit User Request Example
  slug: automation-hub-edit-user-request-example
- key_count: 2
  name: Automation Hub Phase Count Example
  slug: automation-hub-phase-count-example
- key_count: 1
  name: Automation Hub Pipeline Data Example
  slug: automation-hub-pipeline-data-example
- key_count: 3
  name: Automation Hub Role Example
  slug: automation-hub-role-example
- key_count: 4
  name: Automation Hub Update Automation Request Example
  slug: automation-hub-update-automation-request-example
- key_count: 5
  name: Automation Hub User Example
  slug: automation-hub-user-example
- key_count: 2
  name: Automation Hub User List Response Example
  slug: automation-hub-user-list-response-example
- key_count: 5
  name: Data Service Entity Query Request Example
  slug: data-service-entity-query-request-example
- key_count: 3
  name: Data Service Entity Record Collection Example
  slug: data-service-entity-record-collection-example
- key_count: 5
  name: Data Service Entity Record Example
  slug: data-service-entity-record-example
- key_count: 0
  name: Data Service Entity Record Input Example
  slug: data-service-entity-record-input-example
- key_count: 3
  name: Data Service Filter Group Example
  slug: data-service-filter-group-example
- key_count: 2
  name: Data Service Order By Clause Example
  slug: data-service-order-by-clause-example
- key_count: 3
  name: Data Service Query Filter Example
  slug: data-service-query-filter-example
- key_count: 2
  name: Document Understanding Async Job Start Response Example
  slug: document-understanding-async-job-start-response-example
- key_count: 2
  name: Document Understanding Classification Request Example
  slug: document-understanding-classification-request-example
- key_count: 3
  name: Document Understanding Classification Result Example
  slug: document-understanding-classification-result-example
- key_count: 5
  name: Document Understanding Classification Result Item Example
  slug: document-understanding-classification-result-item-example
- key_count: 4
  name: Document Understanding Classifier Example
  slug: document-understanding-classifier-example
- key_count: 1
  name: Document Understanding Classifier Option Example
  slug: document-understanding-classifier-option-example
- key_count: 3
  name: Document Understanding Digitization Request Example
  slug: document-understanding-digitization-request-example
- key_count: 3
  name: Document Understanding Digitization Result Example
  slug: document-understanding-digitization-result-example
- key_count: 4
  name: Document Understanding Extracted Field Example
  slug: document-understanding-extracted-field-example
- key_count: 3
  name: Document Understanding Extraction Request Example
  slug: document-understanding-extraction-request-example
- key_count: 3
  name: Document Understanding Extraction Result Data Example
  slug: document-understanding-extraction-result-data-example
- key_count: 3
  name: Document Understanding Extraction Result Example
  slug: document-understanding-extraction-result-example
- key_count: 4
  name: Document Understanding Extractor Example
  slug: document-understanding-extractor-example
- key_count: 1
  name: Document Understanding Extractor Option Example
  slug: document-understanding-extractor-option-example
- key_count: 4
  name: Document Understanding Field Value Example
  slug: document-understanding-field-value-example
- key_count: 5
  name: Document Understanding Project Example
  slug: document-understanding-project-example
- key_count: 3
  name: Document Understanding Validation Request Example
  slug: document-understanding-validation-request-example
- key_count: 1
  name: Orchestrator Add Queue Item Request Example
  slug: orchestrator-add-queue-item-request-example
- key_count: 10
  name: Orchestrator Asset Example
  slug: orchestrator-asset-example
- key_count: 15
  name: Orchestrator Job Example
  slug: orchestrator-job-example
- key_count: 1
  name: Orchestrator O Data Alert Collection Example
  slug: orchestrator-o-data-alert-collection-example
- key_count: 1
  name: Orchestrator O Data Asset Collection Example
  slug: orchestrator-o-data-asset-collection-example
- key_count: 1
  name: Orchestrator O Data Folder Collection Example
  slug: orchestrator-o-data-folder-collection-example
- key_count: 3
  name: Orchestrator O Data Job Collection Example
  slug: orchestrator-o-data-job-collection-example
- key_count: 1
  name: Orchestrator O Data Machine Collection Example
  slug: orchestrator-o-data-machine-collection-example
- key_count: 1
  name: Orchestrator O Data Package Collection Example
  slug: orchestrator-o-data-package-collection-example
- key_count: 1
  name: Orchestrator O Data Process Collection Example
  slug: orchestrator-o-data-process-collection-example
- key_count: 1
  name: Orchestrator O Data Queue Definition Collection Example
  slug: orchestrator-o-data-queue-definition-collection-example
- key_count: 1
  name: Orchestrator O Data Queue Item Collection Example
  slug: orchestrator-o-data-queue-item-collection-example
- key_count: 1
  name: Orchestrator O Data Robot Collection Example
  slug: orchestrator-o-data-robot-collection-example
- key_count: 1
  name: Orchestrator O Data Role Collection Example
  slug: orchestrator-o-data-role-collection-example
- key_count: 1
  name: Orchestrator O Data Schedule Collection Example
  slug: orchestrator-o-data-schedule-collection-example
- key_count: 1
  name: Orchestrator O Data Storage Bucket Collection Example
  slug: orchestrator-o-data-storage-bucket-collection-example
- key_count: 1
  name: Orchestrator O Data User Collection Example
  slug: orchestrator-o-data-user-collection-example
- key_count: 1
  name: Orchestrator O Data Webhook Collection Example
  slug: orchestrator-o-data-webhook-collection-example
- key_count: 7
  name: Orchestrator Queue Definition Example
  slug: orchestrator-queue-definition-example
- key_count: 6
  name: Orchestrator Queue Item Data Example
  slug: orchestrator-queue-item-data-example
- key_count: 14
  name: Orchestrator Queue Item Example
  slug: orchestrator-queue-item-example
- key_count: 6
  name: Orchestrator Robot Ref Example
  slug: orchestrator-robot-ref-example
- key_count: 7
  name: Orchestrator Start Info Example
  slug: orchestrator-start-info-example
- key_count: 1
  name: Orchestrator Start Jobs Request Example
  slug: orchestrator-start-jobs-request-example
- key_count: 2
  name: Orchestrator Stop Job Request Example
  slug: orchestrator-stop-job-request-example
- key_count: 2
  name: Orchestrator Webhook Event Type Example
  slug: orchestrator-webhook-event-type-example
- key_count: 7
  name: Orchestrator Webhook Example
  slug: orchestrator-webhook-example
- key_count: 3
  name: Platform Management Audit Event Collection Example
  slug: platform-management-audit-event-collection-example
- key_count: 12
  name: Platform Management Audit Event Example
  slug: platform-management-audit-event-example
- key_count: 2
  name: Platform Management Audit Source Example
  slug: platform-management-audit-source-example
- key_count: 1
  name: Platform Management Audit Sources Example
  slug: platform-management-audit-sources-example
- key_count: 2
  name: Platform Management Client Info Example
  slug: platform-management-client-info-example
- key_count: 2
  name: Platform Management Create Group Request Example
  slug: platform-management-create-group-request-example
- key_count: 3
  name: Platform Management Create User Request Example
  slug: platform-management-create-user-request-example
- key_count: 4
  name: Platform Management Group Example
  slug: platform-management-group-example
- key_count: 2
  name: Platform Management Group License Allocation Example
  slug: platform-management-group-license-allocation-example
- key_count: 3
  name: Platform Management License Allocation Entry Example
  slug: platform-management-license-allocation-entry-example
- key_count: 1
  name: Platform Management Update Group License Allocation Request Example
  slug: platform-management-update-group-license-allocation-request-example
- key_count: 6
  name: Platform Management User Example
  slug: platform-management-user-example
- key_count: 2
  name: Test Manager Create Project Request Example
  slug: test-manager-create-project-request-example
- key_count: 3
  name: Test Manager Create Requirement Request Example
  slug: test-manager-create-requirement-request-example
- key_count: 3
  name: Test Manager Create Test Case Request Example
  slug: test-manager-create-test-case-request-example
- key_count: 2
  name: Test Manager Create Test Set Request Example
  slug: test-manager-create-test-set-request-example
- key_count: 7
  name: Test Manager Project Example
  slug: test-manager-project-example
- key_count: 4
  name: Test Manager Project List Response Example
  slug: test-manager-project-list-response-example
- key_count: 7
  name: Test Manager Requirement Example
  slug: test-manager-requirement-example
- key_count: 2
  name: Test Manager Requirement List Response Example
  slug: test-manager-requirement-list-response-example
- key_count: 7
  name: Test Manager Test Case Example
  slug: test-manager-test-case-example
- key_count: 2
  name: Test Manager Test Case List Response Example
  slug: test-manager-test-case-list-response-example
- key_count: 10
  name: Test Manager Test Execution Example
  slug: test-manager-test-execution-example
- key_count: 2
  name: Test Manager Test Execution List Response Example
  slug: test-manager-test-execution-list-response-example
- key_count: 5
  name: Test Manager Test Set Example
  slug: test-manager-test-set-example
- key_count: 2
  name: Test Manager Test Set List Response Example
  slug: test-manager-test-set-list-response-example
- key_count: 0
  name: Uipath Document Understanding Example
  slug: uipath-document-understanding-example
- key_count: 3
  name: Uipath Orchestrator Example
  slug: uipath-orchestrator-example
features:
- description: Automate repetitive tasks across any application using software robots with no-code, low-code, and coded automation options.
  name: Robotic Process Automation
- description: Integrate AI capabilities including document understanding, computer vision, and natural language processing into automation workflows.
  name: AI-Powered Automation
- description: Build and deploy intelligent agents using Python, LangGraph, or LlamaIndex frameworks on the UiPath Agent Cloud.
  name: Agentic Automation
- description: Extract structured data from unstructured documents using ML models for OCR, classification, and field extraction.
  name: Document Understanding
- description: Centrally manage and monitor automation robots, jobs, queues, schedules, and assets across the enterprise.
  name: Orchestration
- description: Discover and analyze business processes to identify automation opportunities and measure impact.
  name: Process Mining
- description: Create, manage, and execute automated tests for RPA and application testing with enterprise CI/CD integration.
  name: Test Automation
- description: Connect to 1,000+ applications and services through pre-built connectors for enterprise integration.
  name: Integration Service
finops:
- name: Uipath Finops
  service_category: Automation / RPA
  slug: uipath-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uipath.png
integrations:
- description: Automate CRM operations, data sync, and customer workflows with native Salesforce integration.
  name: Salesforce
- description: Connect with SAP ERP and S/4HANA for automated finance, HR, and supply chain processes.
  name: SAP
- description: Automate Office applications, SharePoint, Teams, and Azure services through Microsoft 365 integration.
  name: Microsoft 365
- description: Integrate with ServiceNow for ITSM automation, ticket management, and service catalog workflows.
  name: ServiceNow
- description: Connect with Workday HCM for HR automation, payroll processing, and workforce management.
  name: Workday
- description: Build and deploy AI agents using LangChain and LangGraph frameworks on the UiPath platform.
  name: LangChain and LangGraph
json_schemas:
- name: AddUserRequest
  property_count: 2
  slug: automation-hub-add-user-request
- name: AppInventoryListResponse
  property_count: 2
  slug: automation-hub-app-inventory-list-response
- name: Application
  property_count: 5
  slug: automation-hub-application
- name: AutomationListResponse
  property_count: 4
  slug: automation-hub-automation-list-response
- name: Automation
  property_count: 10
  slug: automation-hub-automation
- name: BenefitData
  property_count: 3
  slug: automation-hub-benefit-data
- name: Collaborator
  property_count: 4
  slug: automation-hub-collaborator
- name: CreateAutomationIdeaRequest
  property_count: 4
  slug: automation-hub-create-automation-idea-request
- name: EditUserRequest
  property_count: 3
  slug: automation-hub-edit-user-request
- name: PhaseCount
  property_count: 2
  slug: automation-hub-phase-count
- name: PipelineData
  property_count: 1
  slug: automation-hub-pipeline-data
- name: Role
  property_count: 3
  slug: automation-hub-role
- name: UpdateAutomationRequest
  property_count: 4
  slug: automation-hub-update-automation-request
- name: UserListResponse
  property_count: 2
  slug: automation-hub-user-list-response
- name: User
  property_count: 5
  slug: automation-hub-user
- name: EntityQueryRequest
  property_count: 5
  slug: data-service-entity-query-request
- name: EntityRecordCollection
  property_count: 3
  slug: data-service-entity-record-collection
- name: EntityRecordInput
  property_count: 0
  slug: data-service-entity-record-input
- name: EntityRecord
  property_count: 5
  slug: data-service-entity-record
- name: FilterGroup
  property_count: 3
  slug: data-service-filter-group
- name: OrderByClause
  property_count: 2
  slug: data-service-order-by-clause
- name: QueryFilter
  property_count: 3
  slug: data-service-query-filter
- name: AsyncJobStartResponse
  property_count: 2
  slug: document-understanding-async-job-start-response
- name: ClassificationRequest
  property_count: 2
  slug: document-understanding-classification-request
- name: ClassificationResultItem
  property_count: 5
  slug: document-understanding-classification-result-item
- name: ClassificationResult
  property_count: 3
  slug: document-understanding-classification-result
- name: ClassifierOption
  property_count: 1
  slug: document-understanding-classifier-option
- name: Classifier
  property_count: 4
  slug: document-understanding-classifier
- name: DigitizationRequest
  property_count: 3
  slug: document-understanding-digitization-request
- name: DigitizationResult
  property_count: 3
  slug: document-understanding-digitization-result
- name: ExtractedField
  property_count: 4
  slug: document-understanding-extracted-field
- name: ExtractionRequest
  property_count: 3
  slug: document-understanding-extraction-request
- name: ExtractionResultData
  property_count: 3
  slug: document-understanding-extraction-result-data
- name: ExtractionResult
  property_count: 3
  slug: document-understanding-extraction-result
- name: ExtractorOption
  property_count: 1
  slug: document-understanding-extractor-option
- name: Extractor
  property_count: 4
  slug: document-understanding-extractor
- name: FieldValue
  property_count: 4
  slug: document-understanding-field-value
- name: Project
  property_count: 5
  slug: document-understanding-project
- name: ValidationRequest
  property_count: 3
  slug: document-understanding-validation-request
- name: AddQueueItemRequest
  property_count: 1
  slug: orchestrator-add-queue-item-request
- name: Asset
  property_count: 10
  slug: orchestrator-asset
- name: Job
  property_count: 15
  slug: orchestrator-job
- name: ODataAlertCollection
  property_count: 1
  slug: orchestrator-o-data-alert-collection
- name: ODataAssetCollection
  property_count: 1
  slug: orchestrator-o-data-asset-collection
- name: ODataFolderCollection
  property_count: 1
  slug: orchestrator-o-data-folder-collection
- name: ODataJobCollection
  property_count: 3
  slug: orchestrator-o-data-job-collection
- name: ODataMachineCollection
  property_count: 1
  slug: orchestrator-o-data-machine-collection
- name: ODataPackageCollection
  property_count: 1
  slug: orchestrator-o-data-package-collection
- name: ODataProcessCollection
  property_count: 1
  slug: orchestrator-o-data-process-collection
- name: ODataQueueDefinitionCollection
  property_count: 1
  slug: orchestrator-o-data-queue-definition-collection
- name: ODataQueueItemCollection
  property_count: 1
  slug: orchestrator-o-data-queue-item-collection
- name: ODataRobotCollection
  property_count: 1
  slug: orchestrator-o-data-robot-collection
- name: ODataRoleCollection
  property_count: 1
  slug: orchestrator-o-data-role-collection
- name: ODataScheduleCollection
  property_count: 1
  slug: orchestrator-o-data-schedule-collection
- name: ODataStorageBucketCollection
  property_count: 1
  slug: orchestrator-o-data-storage-bucket-collection
- name: ODataUserCollection
  property_count: 1
  slug: orchestrator-o-data-user-collection
- name: ODataWebhookCollection
  property_count: 1
  slug: orchestrator-o-data-webhook-collection
- name: QueueDefinition
  property_count: 7
  slug: orchestrator-queue-definition
- name: QueueItemData
  property_count: 6
  slug: orchestrator-queue-item-data
- name: QueueItem
  property_count: 14
  slug: orchestrator-queue-item
- name: RobotRef
  property_count: 6
  slug: orchestrator-robot-ref
- name: StartInfo
  property_count: 7
  slug: orchestrator-start-info
- name: StartJobsRequest
  property_count: 1
  slug: orchestrator-start-jobs-request
- name: StopJobRequest
  property_count: 2
  slug: orchestrator-stop-job-request
- name: WebhookEventType
  property_count: 2
  slug: orchestrator-webhook-event-type
- name: Webhook
  property_count: 7
  slug: orchestrator-webhook
- name: AuditEventCollection
  property_count: 3
  slug: platform-management-audit-event-collection
- name: AuditEvent
  property_count: 12
  slug: platform-management-audit-event
- name: AuditSource
  property_count: 2
  slug: platform-management-audit-source
- name: AuditSources
  property_count: 1
  slug: platform-management-audit-sources
- name: ClientInfo
  property_count: 2
  slug: platform-management-client-info
- name: CreateGroupRequest
  property_count: 2
  slug: platform-management-create-group-request
- name: CreateUserRequest
  property_count: 3
  slug: platform-management-create-user-request
- name: GroupLicenseAllocation
  property_count: 2
  slug: platform-management-group-license-allocation
- name: Group
  property_count: 4
  slug: platform-management-group
- name: LicenseAllocationEntry
  property_count: 3
  slug: platform-management-license-allocation-entry
- name: UpdateGroupLicenseAllocationRequest
  property_count: 1
  slug: platform-management-update-group-license-allocation-request
- name: User
  property_count: 6
  slug: platform-management-user
- name: CreateProjectRequest
  property_count: 2
  slug: test-manager-create-project-request
- name: CreateRequirementRequest
  property_count: 3
  slug: test-manager-create-requirement-request
- name: CreateTestCaseRequest
  property_count: 3
  slug: test-manager-create-test-case-request
- name: CreateTestSetRequest
  property_count: 2
  slug: test-manager-create-test-set-request
- name: ProjectListResponse
  property_count: 4
  slug: test-manager-project-list-response
- name: Project
  property_count: 7
  slug: test-manager-project
- name: RequirementListResponse
  property_count: 2
  slug: test-manager-requirement-list-response
- name: Requirement
  property_count: 7
  slug: test-manager-requirement
- name: TestCaseListResponse
  property_count: 2
  slug: test-manager-test-case-list-response
- name: TestCase
  property_count: 7
  slug: test-manager-test-case
- name: TestExecutionListResponse
  property_count: 2
  slug: test-manager-test-execution-list-response
- name: TestExecution
  property_count: 10
  slug: test-manager-test-execution
- name: TestSetListResponse
  property_count: 2
  slug: test-manager-test-set-list-response
- name: TestSet
  property_count: 5
  slug: test-manager-test-set
- name: UiPath Document Understanding Entities
  property_count: 0
  slug: uipath-document-understanding
- name: UiPath Orchestrator Entities
  property_count: 3
  slug: uipath-orchestrator
json_structures:
- name: Automation Hub Add User Request Structure
  property_count: 2
  slug: automation-hub-add-user-request-structure
- name: Automation Hub App Inventory List Response Structure
  property_count: 2
  slug: automation-hub-app-inventory-list-response-structure
- name: Automation Hub Application Structure
  property_count: 5
  slug: automation-hub-application-structure
- name: Automation Hub Automation List Response Structure
  property_count: 4
  slug: automation-hub-automation-list-response-structure
- name: Automation Hub Automation Structure
  property_count: 10
  slug: automation-hub-automation-structure
- name: Automation Hub Benefit Data Structure
  property_count: 3
  slug: automation-hub-benefit-data-structure
- name: Automation Hub Collaborator Structure
  property_count: 4
  slug: automation-hub-collaborator-structure
- name: Automation Hub Create Automation Idea Request Structure
  property_count: 4
  slug: automation-hub-create-automation-idea-request-structure
- name: Automation Hub Edit User Request Structure
  property_count: 3
  slug: automation-hub-edit-user-request-structure
- name: Automation Hub Phase Count Structure
  property_count: 2
  slug: automation-hub-phase-count-structure
- name: Automation Hub Pipeline Data Structure
  property_count: 1
  slug: automation-hub-pipeline-data-structure
- name: Automation Hub Role Structure
  property_count: 3
  slug: automation-hub-role-structure
- name: Automation Hub Update Automation Request Structure
  property_count: 4
  slug: automation-hub-update-automation-request-structure
- name: Automation Hub User List Response Structure
  property_count: 2
  slug: automation-hub-user-list-response-structure
- name: Automation Hub User Structure
  property_count: 5
  slug: automation-hub-user-structure
- name: Data Service Entity Query Request Structure
  property_count: 5
  slug: data-service-entity-query-request-structure
- name: Data Service Entity Record Collection Structure
  property_count: 3
  slug: data-service-entity-record-collection-structure
- name: Data Service Entity Record Input Structure
  property_count: 0
  slug: data-service-entity-record-input-structure
- name: Data Service Entity Record Structure
  property_count: 5
  slug: data-service-entity-record-structure
- name: Data Service Filter Group Structure
  property_count: 3
  slug: data-service-filter-group-structure
- name: Data Service Order By Clause Structure
  property_count: 2
  slug: data-service-order-by-clause-structure
- name: Data Service Query Filter Structure
  property_count: 3
  slug: data-service-query-filter-structure
- name: Document Understanding Async Job Start Response Structure
  property_count: 2
  slug: document-understanding-async-job-start-response-structure
- name: Document Understanding Classification Request Structure
  property_count: 2
  slug: document-understanding-classification-request-structure
- name: Document Understanding Classification Result Item Structure
  property_count: 5
  slug: document-understanding-classification-result-item-structure
- name: Document Understanding Classification Result Structure
  property_count: 3
  slug: document-understanding-classification-result-structure
- name: Document Understanding Classifier Option Structure
  property_count: 1
  slug: document-understanding-classifier-option-structure
- name: Document Understanding Classifier Structure
  property_count: 4
  slug: document-understanding-classifier-structure
- name: Document Understanding Digitization Request Structure
  property_count: 3
  slug: document-understanding-digitization-request-structure
- name: Document Understanding Digitization Result Structure
  property_count: 3
  slug: document-understanding-digitization-result-structure
- name: Document Understanding Extracted Field Structure
  property_count: 4
  slug: document-understanding-extracted-field-structure
- name: Document Understanding Extraction Request Structure
  property_count: 3
  slug: document-understanding-extraction-request-structure
- name: Document Understanding Extraction Result Data Structure
  property_count: 3
  slug: document-understanding-extraction-result-data-structure
- name: Document Understanding Extraction Result Structure
  property_count: 3
  slug: document-understanding-extraction-result-structure
- name: Document Understanding Extractor Option Structure
  property_count: 1
  slug: document-understanding-extractor-option-structure
- name: Document Understanding Extractor Structure
  property_count: 4
  slug: document-understanding-extractor-structure
- name: Document Understanding Field Value Structure
  property_count: 4
  slug: document-understanding-field-value-structure
- name: Document Understanding Project Structure
  property_count: 5
  slug: document-understanding-project-structure
- name: Document Understanding Validation Request Structure
  property_count: 3
  slug: document-understanding-validation-request-structure
- name: Orchestrator Add Queue Item Request Structure
  property_count: 1
  slug: orchestrator-add-queue-item-request-structure
- name: Orchestrator Asset Structure
  property_count: 10
  slug: orchestrator-asset-structure
- name: Orchestrator Job Structure
  property_count: 15
  slug: orchestrator-job-structure
- name: Orchestrator O Data Alert Collection Structure
  property_count: 1
  slug: orchestrator-o-data-alert-collection-structure
- name: Orchestrator O Data Asset Collection Structure
  property_count: 1
  slug: orchestrator-o-data-asset-collection-structure
- name: Orchestrator O Data Folder Collection Structure
  property_count: 1
  slug: orchestrator-o-data-folder-collection-structure
- name: Orchestrator O Data Job Collection Structure
  property_count: 3
  slug: orchestrator-o-data-job-collection-structure
- name: Orchestrator O Data Machine Collection Structure
  property_count: 1
  slug: orchestrator-o-data-machine-collection-structure
- name: Orchestrator O Data Package Collection Structure
  property_count: 1
  slug: orchestrator-o-data-package-collection-structure
- name: Orchestrator O Data Process Collection Structure
  property_count: 1
  slug: orchestrator-o-data-process-collection-structure
- name: Orchestrator O Data Queue Definition Collection Structure
  property_count: 1
  slug: orchestrator-o-data-queue-definition-collection-structure
- name: Orchestrator O Data Queue Item Collection Structure
  property_count: 1
  slug: orchestrator-o-data-queue-item-collection-structure
- name: Orchestrator O Data Robot Collection Structure
  property_count: 1
  slug: orchestrator-o-data-robot-collection-structure
- name: Orchestrator O Data Role Collection Structure
  property_count: 1
  slug: orchestrator-o-data-role-collection-structure
- name: Orchestrator O Data Schedule Collection Structure
  property_count: 1
  slug: orchestrator-o-data-schedule-collection-structure
- name: Orchestrator O Data Storage Bucket Collection Structure
  property_count: 1
  slug: orchestrator-o-data-storage-bucket-collection-structure
- name: Orchestrator O Data User Collection Structure
  property_count: 1
  slug: orchestrator-o-data-user-collection-structure
- name: Orchestrator O Data Webhook Collection Structure
  property_count: 1
  slug: orchestrator-o-data-webhook-collection-structure
- name: Orchestrator Queue Definition Structure
  property_count: 7
  slug: orchestrator-queue-definition-structure
- name: Orchestrator Queue Item Data Structure
  property_count: 6
  slug: orchestrator-queue-item-data-structure
- name: Orchestrator Queue Item Structure
  property_count: 14
  slug: orchestrator-queue-item-structure
- name: Orchestrator Robot Ref Structure
  property_count: 6
  slug: orchestrator-robot-ref-structure
- name: Orchestrator Start Info Structure
  property_count: 7
  slug: orchestrator-start-info-structure
- name: Orchestrator Start Jobs Request Structure
  property_count: 1
  slug: orchestrator-start-jobs-request-structure
- name: Orchestrator Stop Job Request Structure
  property_count: 2
  slug: orchestrator-stop-job-request-structure
- name: Orchestrator Webhook Event Type Structure
  property_count: 2
  slug: orchestrator-webhook-event-type-structure
- name: Orchestrator Webhook Structure
  property_count: 7
  slug: orchestrator-webhook-structure
- name: Platform Management Audit Event Collection Structure
  property_count: 3
  slug: platform-management-audit-event-collection-structure
- name: Platform Management Audit Event Structure
  property_count: 12
  slug: platform-management-audit-event-structure
- name: Platform Management Audit Source Structure
  property_count: 2
  slug: platform-management-audit-source-structure
- name: Platform Management Audit Sources Structure
  property_count: 1
  slug: platform-management-audit-sources-structure
- name: Platform Management Client Info Structure
  property_count: 2
  slug: platform-management-client-info-structure
- name: Platform Management Create Group Request Structure
  property_count: 2
  slug: platform-management-create-group-request-structure
- name: Platform Management Create User Request Structure
  property_count: 3
  slug: platform-management-create-user-request-structure
- name: Platform Management Group License Allocation Structure
  property_count: 2
  slug: platform-management-group-license-allocation-structure
- name: Platform Management Group Structure
  property_count: 4
  slug: platform-management-group-structure
- name: Platform Management License Allocation Entry Structure
  property_count: 3
  slug: platform-management-license-allocation-entry-structure
- name: Platform Management Update Group License Allocation Request Structure
  property_count: 1
  slug: platform-management-update-group-license-allocation-request-structure
- name: Platform Management User Structure
  property_count: 6
  slug: platform-management-user-structure
- name: Test Manager Create Project Request Structure
  property_count: 2
  slug: test-manager-create-project-request-structure
- name: Test Manager Create Requirement Request Structure
  property_count: 3
  slug: test-manager-create-requirement-request-structure
- name: Test Manager Create Test Case Request Structure
  property_count: 3
  slug: test-manager-create-test-case-request-structure
- name: Test Manager Create Test Set Request Structure
  property_count: 2
  slug: test-manager-create-test-set-request-structure
- name: Test Manager Project List Response Structure
  property_count: 4
  slug: test-manager-project-list-response-structure
- name: Test Manager Project Structure
  property_count: 7
  slug: test-manager-project-structure
- name: Test Manager Requirement List Response Structure
  property_count: 2
  slug: test-manager-requirement-list-response-structure
- name: Test Manager Requirement Structure
  property_count: 7
  slug: test-manager-requirement-structure
- name: Test Manager Test Case List Response Structure
  property_count: 2
  slug: test-manager-test-case-list-response-structure
- name: Test Manager Test Case Structure
  property_count: 7
  slug: test-manager-test-case-structure
- name: Test Manager Test Execution List Response Structure
  property_count: 2
  slug: test-manager-test-execution-list-response-structure
- name: Test Manager Test Execution Structure
  property_count: 10
  slug: test-manager-test-execution-structure
- name: Test Manager Test Set List Response Structure
  property_count: 2
  slug: test-manager-test-set-list-response-structure
- name: Test Manager Test Set Structure
  property_count: 5
  slug: test-manager-test-set-structure
- name: Uipath Document Understanding Structure
  property_count: 0
  slug: uipath-document-understanding-structure
- name: Uipath Orchestrator Structure
  property_count: 3
  slug: uipath-orchestrator-structure
jsonld:
- class_count: 18
  name: Uipath Automation Hub Context
  property_count: 24
  slug: uipath-automation-hub-context
- class_count: 0
  name: Uipath Context
  property_count: 15
  slug: uipath-context
- class_count: 7
  name: Uipath Data Service Context
  property_count: 19
  slug: uipath-data-service-context
- class_count: 19
  name: Uipath Document Understanding Context
  property_count: 35
  slug: uipath-document-understanding-context
- class_count: 2
  name: Uipath General Context
  property_count: 3
  slug: uipath-general-context
- class_count: 27
  name: Uipath Orchestrator Context
  property_count: 77
  slug: uipath-orchestrator-context
- class_count: 14
  name: Uipath Platform Management Context
  property_count: 29
  slug: uipath-platform-management-context
- class_count: 16
  name: Uipath Test Manager Context
  property_count: 26
  slug: uipath-test-manager-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: UiPath
nav: Providers
network: true
overview: 'UiPath publishes 32 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, AppInventory API, Assets API, and 29 more. Tagged areas include Automation, Robotic Process Automation, RPA, Artificial Intelligence, and Document Processing.


  The UiPath catalog on APIs.io includes 1 event-driven AsyncAPI specification, 8 JSON-LD contexts, and 3 Spectral governance rulesets.


  UiPath''s developer surface includes authentication, documentation, developer portal, engineering blog, pricing, support, academy / training, and 46 more developer resources.'
plans:
- name: Uipath Plans Pricing
  plan_count: 5
  slug: uipath-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 5
  name: Uipath Rate Limits
  slug: uipath-rate-limits
rules:
- name: UiPath API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: uipath-asyncapi-spectral-rules
- name: UiPath API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: uipath-jsonschema-spectral-rules
- name: UiPath API Rules
  rule_count: 45
  severity_counts:
    error: 15
    hint: 0
    info: 6
    warn: 24
  slug: uipath-spectral-rules
score:
  band: exemplar
  composite: 71.2
  delta: -4.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 90.2
    developer_ergonomics: 87.0
    discoverability: 75.9
    governance: 52.1
    operational_transparency: 28.9
  previous_composite: 75.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 32
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uipath/refs/heads/main/screenshots/uipath-2026-06-20T200001.png
security:
- kind: authentication
  name: Uipath Authentication
  slug: uipath-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Uipath Domain Security
  slug: uipath-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Uipath Vulnerability Disclosure
  slug: uipath-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Uipath Trust Center
  slug: uipath-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA
skill_count: 20
skills:
- name: uipath-admin
  slug: uipath-admin
- name: uipath-agents
  slug: uipath-agents
- name: uipath-api-workflow
  slug: uipath-api-workflow
- name: uipath-coded-apps
  slug: uipath-coded-apps
- name: uipath-data-fabric
  slug: uipath-data-fabric
- name: uipath-feedback
  slug: uipath-feedback
- name: uipath-governance
  slug: uipath-governance
- name: uipath-human-in-the-loop
  slug: uipath-human-in-the-loop
- name: uipath-ixp
  slug: uipath-ixp
- name: uipath-maestro-bpmn
  slug: uipath-maestro-bpmn
- name: uipath-maestro-case
  slug: uipath-maestro-case
- name: uipath-maestro-flow
  slug: uipath-maestro-flow
- name: uipath-planner
  slug: uipath-planner
- name: uipath-platform
  slug: uipath-platform
- name: uipath-review
  slug: uipath-review
- name: uipath-rpa
  slug: uipath-rpa
- name: uipath-solution
  slug: uipath-solution
- name: uipath-tasks
  slug: uipath-tasks
- name: uipath-test
  slug: uipath-test
- name: uipath-troubleshoot
  slug: uipath-troubleshoot
slug: uipath
solutions:
- description: Entry-level cloud automation for individuals and small teams with basic RPA and limited scale.
  name: Automation Cloud Basic
- description: Professional automation platform for businesses with unlimited users, robots, and enterprise data extraction.
  name: Automation Cloud Standard
- description: Strategic enterprise automation with full infrastructure control, BYOK, multi-region deployment, and advanced AI capabilities.
  name: Automation Cloud Enterprise
- description: FedRAMP Moderate authorized automation solution for U.S. government and public sector organizations.
  name: Automation Cloud Public Sector
tags:
- Automation
- Robotic Process Automation
- RPA
- Artificial Intelligence
- Document Processing
- Enterprise Automation
- Orchestration
- Testing
use_cases:
- description: Automate invoice processing, accounts payable/receivable, financial reporting, and compliance workflows.
  name: Finance and Accounting Automation
- description: Streamline employee onboarding, offboarding, payroll processing, and HR data management across systems.
  name: HR Onboarding Automation
- description: Automate customer inquiry routing, case management, data lookup, and response generation.
  name: Customer Service Automation
- description: Automate IT service desk tickets, provisioning, monitoring alerts, and infrastructure management tasks.
  name: IT Process Automation
- description: Automate patient data management, claims processing, prior authorization, and regulatory reporting.
  name: Healthcare Administration
- description: Automate procurement, order management, inventory tracking, and logistics workflows.
  name: Supply Chain Automation
website: https://www.uipath.com
---
