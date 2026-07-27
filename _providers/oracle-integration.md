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
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 45
  human_in_the_loop: 1
  name: Oracle Integration Agentic Access
  operation_count: 104
  slug: oracle-integration-agentic-access
  summary_line: 104 operations · 45 acting · 1 human-in-the-loop
api_count: 25
apis:
- description: REST API for configuring and administering the Oracle Integration File Server, an SFTP-compliant file repository for managing file-based integrations.
  name: Oracle Integration File Server API
  slug: oracle-integration-file-server-api
- description: OCI control plane API for provisioning and managing Oracle Integration instances, custom endpoints, and data retention configuration.
  name: Oracle Integration Administrative API
  slug: oracle-integration-administrative-api
- description: Rapid Adapter Builder for custom adapters.
  name: Oracle Integration Adapters API
  slug: oracle-integration-adapters-api
- description: Process analytics queries and data.
  name: Oracle Integration Analytics API
  slug: oracle-integration-analytics-api
- description: B2B document customization and schema management.
  name: Oracle Integration B2B Documents API
  slug: oracle-integration-b2b-documents-api
- description: Monitor B2B business and wire messages.
  name: Oracle Integration B2B Monitoring API
  slug: oracle-integration-b2b-monitoring-api
- description: Manage SSL certificates for secure connections.
  name: Oracle Integration Certificates API
  slug: oracle-integration-certificates-api
- description: Manage connections that define integration endpoints.
  name: Oracle Integration Connections API
  slug: oracle-integration-connections-api
- description: Manage DMN decision models and services.
  name: Oracle Integration Decision Models API
  slug: oracle-integration-decision-models-api
- description: Manage deployed BPM projects.
  name: Oracle Integration Deployed Projects API
  slug: oracle-integration-deployed-projects-api
- description: Manage dynamic process definitions and instances.
  name: Oracle Integration Dynamic Processes API
  slug: oracle-integration-dynamic-processes-api
- description: Configure CORS and environment settings.
  name: Oracle Integration Environment API
  slug: oracle-integration-environment-api
- description: Manage users, groups, and roles.
  name: Oracle Integration Identities API
  slug: oracle-integration-identities-api
- description: Create, manage, and deploy integrations.
  name: Oracle Integration Integrations API
  slug: oracle-integration-integrations-api
- description: Manage JavaScript libraries for use in integrations.
  name: Oracle Integration Libraries API
  slug: oracle-integration-libraries-api
- description: Manage lookup tables for data mapping.
  name: Oracle Integration Lookups API
  slug: oracle-integration-lookups-api
- description: Monitor and manage integration instances.
  name: Oracle Integration Monitoring API
  slug: oracle-integration-monitoring-api
- description: Manage packages for grouping integrations.
  name: Oracle Integration Packages API
  slug: oracle-integration-packages-api
- description: Retrieve process definition metadata and configurations.
  name: Oracle Integration Process Definitions API
  slug: oracle-integration-process-definitions-api
- description: Manage process instances and related data.
  name: Oracle Integration Process Instances API
  slug: oracle-integration-process-instances-api
- description: Manage integration projects and deployments.
  name: Oracle Integration Projects API
  slug: oracle-integration-projects-api
- description: Manage scheduled integration execution.
  name: Oracle Integration Scheduled Integrations API
  slug: oracle-integration-scheduled-integrations-api
- description: Manage workspace spaces.
  name: Oracle Integration Spaces API
  slug: oracle-integration-spaces-api
- description: Manage user tasks and task actions.
  name: Oracle Integration Tasks API
  slug: oracle-integration-tasks-api
- description: Manage B2B trading partners and agreements.
  name: Oracle Integration Trading Partners API
  slug: oracle-integration-trading-partners-api
arazzos:
- description: Record an explanatory comment on a process instance, then abort it when it is still open.
  name: Oracle Integration Abort a Process with an Audit Comment
  slug: oracle-integration-abort-process-with-comment-workflow
- description: Find a monitored instance, confirm it is in progress, and abort it.
  name: Oracle Integration Abort a Running Instance
  slug: oracle-integration-abort-running-instance-workflow
- description: Locate an integration, confirm it is ready, activate it, and poll until the activation completes.
  name: Oracle Integration Activate an Integration
  slug: oracle-integration-activate-integration-workflow
- description: Clone an existing integration to a new code, then activate the clone.
  name: Oracle Integration Clone and Activate an Integration
  slug: oracle-integration-clone-and-activate-integration-workflow
- description: Confirm an integration is active and deactivate it back to a configured state.
  name: Oracle Integration Deactivate an Integration
  slug: oracle-integration-deactivate-integration-workflow
- description: Update a connection's properties, test connectivity, and refresh its metadata on success.
  name: Oracle Integration Configure and Test a Connection
  slug: oracle-integration-provision-connection-workflow
- description: Create a workspace space, create an empty decision model inside its DMN space, and read the model back.
  name: Oracle Integration Provision a Decision Model
  slug: oracle-integration-provision-decision-model-workflow
- description: Find errored integration instances, inspect the activity stream of one, and resubmit it for reprocessing.
  name: Oracle Integration Triage and Resubmit an Errored Instance
  slug: oracle-integration-resubmit-errored-instance-workflow
- description: Pull a user task, read its payload, and approve or reject it based on the assignee's review.
  name: Oracle Integration Review and Action a User Task
  slug: oracle-integration-review-and-action-task-workflow
- description: Confirm a scheduled integration is active, start its schedule, and trigger an immediate run.
  name: Oracle Integration Start Schedule and Run Now
  slug: oracle-integration-run-scheduled-integration-workflow
- description: Start a structured process instance, locate the user task it generates, and act on that task.
  name: Oracle Integration Start a Process and Handle Its Task
  slug: oracle-integration-start-process-and-handle-task-workflow
- description: Detect whether a lookup exists, then update it if present or create it if missing, and read the result back.
  name: Oracle Integration Upsert a Lookup Table
  slug: oracle-integration-upsert-lookup-workflow
artifact_total: 106
collections:
- collection_type: postman
  name: Oracle Integration Developer API
  slug: postman-oracle-integration-developer-api
- collection_type: postman
  name: Oracle Integration Process Automation API
  slug: postman-oracle-integration-process-automation-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oracle-integration-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-integration-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oracle-integration-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/oracle-integration-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/oracle-integration/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-integration-abort-process-with-comment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-integration-abort-running-instance-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-integration-activate-integration-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-integration-clone-and-activate-integration-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-integration-deactivate-integration-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-integration-provision-connection-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-integration-provision-decision-model-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-integration-resubmit-errored-instance-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-integration-review-and-action-task-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-integration-run-scheduled-integration-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-integration-start-process-and-handle-task-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-integration-upsert-lookup-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://cloud.oracle.com/integration
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en/cloud/paas/application-integration/oracle-integration-oci/explore-oracle-integration-apis.html
- group: learn
  title: ''
  type: Tutorials
  url: https://docs.oracle.com/en/cloud/paas/integration-cloud/tutorials.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/cloud/paas/application-integration/index.html
- group: company
  title: ''
  type: Blog
  url: https://blogs.oracle.com/integration/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.oracle.com/en/cloud/paas/integration-cloud/whats-new/
- group: operate
  title: ''
  type: Support
  url: https://www.oracle.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://ocistatus.oraclecloud.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oracle.com/integration/pricing/
- group: start
  title: ''
  type: Console
  url: https://cloud.oracle.com/integration
- group: build
  title: OCI SDKs
  type: SDKs
  url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdks.htm
- group: build
  title: OCI CLI
  type: CLI
  url: https://github.com/oracle/oci-cli
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: build
  title: OCI CLI Repository
  type: GitHubRepository
  url: https://github.com/oracle/oci-cli
- group: build
  title: Python SDK Repository
  type: GitHubRepository
  url: https://github.com/oracle/oci-python-sdk
- group: build
  title: Go SDK Repository
  type: GitHubRepository
  url: https://github.com/oracle/oci-go-sdk
- group: learn
  title: ''
  type: Training
  url: https://education.oracle.com/
- group: other
  title: ''
  type: Marketplace
  url: https://cloudmarketplace.oracle.com/marketplace/en_US/homeLinkPage
- group: design
  title: ''
  type: SpectralRules
  url: rules/oracle-integration-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/oracle-integration-vocabulary.yaml
created: '2024-01-15'
description: Oracle Integration provides native connectivity to Oracle and non-Oracle Software as a Service (SaaS) and on-premises applications, such as Oracle ERP Cloud, Oracle Service Cloud, HCM Cloud, Salesforce, Workday, EBS, SAP, NetSuite and others. It combines application integration, process automation, visual application building, and integration analytics into a single unified cloud service.
examples:
- key_count: 10
  name: Developer Api Connection Example
  slug: developer-api-connection-example
- key_count: 12
  name: Developer Api Integration Example
  slug: developer-api-integration-example
- key_count: 6
  name: Developer Api Monitoring Instance Example
  slug: developer-api-monitoring-instance-example
- key_count: 6
  name: Developer Api Trading Partner Example
  slug: developer-api-trading-partner-example
- key_count: 8
  name: Process Automation Api Process Instance Example
  slug: process-automation-api-process-instance-example
- key_count: 10
  name: Process Automation Api Task Example
  slug: process-automation-api-task-example
features:
- description: Library of prebuilt integration recipes and adapters for rapid deployment of common integration patterns.
  name: Prebuilt Integrations
- description: Native connectivity to Oracle SaaS, on-premises applications, and third-party services including Salesforce, SAP, Workday, and ServiceNow.
  name: Application Adapters
- description: Low-code drag-and-drop integration designer for building integration flows without extensive coding.
  name: Visual Integration Designer
- description: EDI and B2B document processing with support for trading partner management, document standards, and agreement lifecycle.
  name: B2B Document Exchange
- description: Business process management with structured and unstructured workflows, case management, and task management.
  name: Process Automation
- description: DMN-based decision model management for business rules execution and deployment.
  name: Decision Modeling
- description: Time-based scheduling of integration flows with pause, resume, start, and stop controls.
  name: Scheduled Integrations
- description: Real-time monitoring of integration instances, error tracking, activity streams, and audit records.
  name: Integration Monitoring
- description: SFTP-compliant embedded file server for file-based integration scenarios.
  name: File Server
- description: Custom adapter development framework for building reusable connectivity to proprietary or niche systems.
  name: Rapid Adapter Builder
- description: AI agent capabilities within integration projects for intelligent automation patterns and prompt templates.
  name: AI Agents
- description: ML-based guidance and recommendations for building and optimizing integrations.
  name: Machine Learning Recommendations
- description: Built-in analytics and process analytics with custom query builders and data visualization.
  name: Integration Analytics
- description: Native Fast Healthcare Interoperability Resources support for healthcare integration workflows.
  name: FHIR Support
finops:
- name: Oracle Integration Finops
  service_category: Integration / iPaaS
  slug: oracle-integration-finops
image: /assets/icons/oracle-integration.png
integrations:
- description: Native adapter for Oracle Enterprise Resource Planning Cloud including financials, procurement, and supply chain.
  name: Oracle ERP Cloud
- description: Native adapter for Oracle Human Capital Management Cloud for HR, payroll, and talent management.
  name: Oracle HCM Cloud
- description: Native adapter for Oracle Customer Experience Cloud including sales, service, and marketing.
  name: Oracle CX Cloud
- description: Native adapter for Oracle NetSuite ERP and CRM cloud services.
  name: Oracle NetSuite
- description: Prebuilt adapter for Salesforce CRM integration with Oracle cloud and on-premises applications.
  name: Salesforce
- description: Adapter for SAP ERP and S/4HANA integration via IDoc, BAPI, and RFC protocols.
  name: SAP
- description: Prebuilt adapter for Workday HCM and financial management integration.
  name: Workday
- description: Adapter for ServiceNow ITSM and ITOM integration with Oracle applications.
  name: ServiceNow
- description: Adapter for Shopify e-commerce platform integration with order management and inventory systems.
  name: Shopify
- description: Adapter for Snowflake data warehouse integration for analytics and data pipelines.
  name: Snowflake
- description: Connectivity to Microsoft Azure services and applications for multi-cloud integration.
  name: Microsoft Azure
- description: Connectivity to Amazon Web Services for multi-cloud integration scenarios.
  name: AWS
- description: Adapter for Slack messaging integration with workflow notifications and approvals.
  name: Slack
- description: Adapter for Atlassian JIRA project management and issue tracking integration.
  name: JIRA
json_schemas:
- name: Connection
  property_count: 10
  slug: developer-api-connection
- name: Integration
  property_count: 12
  slug: developer-api-integration
- name: MonitoringInstance
  property_count: 6
  slug: developer-api-monitoring-instance
- name: TradingPartner
  property_count: 6
  slug: developer-api-trading-partner
- name: ProcessInstance
  property_count: 8
  slug: process-automation-api-process-instance
- name: Task
  property_count: 10
  slug: process-automation-api-task
json_structures:
- name: Developer Api Connection Structure
  property_count: 10
  slug: developer-api-connection-structure
- name: Developer Api Integration Structure
  property_count: 12
  slug: developer-api-integration-structure
- name: Developer Api Monitoring Instance Structure
  property_count: 6
  slug: developer-api-monitoring-instance-structure
- name: Developer Api Trading Partner Structure
  property_count: 6
  slug: developer-api-trading-partner-structure
- name: Process Automation Api Process Instance Structure
  property_count: 8
  slug: process-automation-api-process-instance-structure
- name: Process Automation Api Task Structure
  property_count: 10
  slug: process-automation-api-task-structure
jsonld:
- class_count: 7
  name: Oracle Integration Developer Api Context
  property_count: 27
  slug: oracle-integration-developer-api-context
- class_count: 3
  name: Oracle Integration Process Automation Api Context
  property_count: 16
  slug: oracle-integration-process-automation-api-context
layout: provider
modified: '2026-05-19'
name: Oracle Integration
nav: Providers
network: true
overview: 'Oracle Integration publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Adapters API, Analytics API, B2B Documents API, and 20 more. Tagged areas include API Management, Automation, B2B Integration, Cloud Integration, and Enterprise Integration.


  The Oracle Integration catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Oracle Integration''s developer surface includes authentication, developer portal, getting-started guide, documentation, engineering blog, changelog, support, and 32 more developer resources.'
plans:
- name: Oracle Integration Plans Pricing
  plan_count: 4
  slug: oracle-integration-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 24
  name: Oracle Integration Rate Limits
  slug: oracle-integration-rate-limits
rules:
- name: Oracle Integration API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: oracle-integration-jsonschema-spectral-rules
- name: Oracle Integration API Rules
  rule_count: 42
  severity_counts:
    error: 18
    hint: 0
    info: 7
    warn: 17
  slug: oracle-integration-spectral-rules
scopes:
- name: Oracle Integration Scopes
  scope_count: 1
  slug: oracle-integration-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: exemplar
  composite: 76.8
  delta: 4.7
  facets:
    commercial_clarity: 71.1
    contract_quality: 80.5
    developer_ergonomics: 69.6
    discoverability: 92.5
    governance: 86.8
    operational_transparency: 68.4
  previous_composite: 72.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Oracle Integration Authentication
  slug: oracle-integration-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Oracle Integration Domain Security
  slug: oracle-integration-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oracle-integration
tags:
- API Management
- Automation
- B2B Integration
- Cloud Integration
- Enterprise Integration
- Integration
- iPaaS
- Process Automation
use_cases:
- description: Connect Oracle SaaS applications like ERP Cloud, HCM Cloud, and CX Cloud with third-party SaaS platforms.
  name: SaaS Application Integration
- description: Integrate Oracle ERP Cloud or on-premises EBS with procurement, supply chain, and financial systems.
  name: ERP Integration
- description: Synchronize human capital management data across Oracle HCM Cloud, Workday, and other HR systems.
  name: HCM Integration
- description: Automate EDI-based trading partner setup, agreement management, and document exchange.
  name: B2B Trading Partner Onboarding
- description: Automate business processes with approval workflows, case management, and task orchestration.
  name: Process Automation
- description: Build FHIR-compliant healthcare integration workflows for patient data exchange and interoperability.
  name: Healthcare Data Exchange
- description: Connect on-premises applications to Oracle Cloud and third-party cloud services via connectivity agents.
  name: Hybrid Cloud Integration
- description: Automate file transfers and processing with the embedded SFTP-compliant file server.
  name: File-Based Integration
- description: Manage integration lifecycle with export, import, and deployment APIs for DevOps automation.
  name: CI/CD For Integrations
- description: Process events and messages in real time using event-driven integration patterns and stream analytics.
  name: Real-Time Event Processing
website: https://cloud.oracle.com/integration
---
