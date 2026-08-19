---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Power Platform Agentic Access
  operation_count: 13
  slug: power-platform-agentic-access
  summary_line: 13 operations · 5 acting
api_count: 9
apis:
- description: OData v4.0 compliant Web API for Microsoft Dataverse, providing RESTful data storage, business logic, and entity management capabilities across the Power Platform.
  name: Dataverse API (Common Data Service)
  slug: dataverse-api-common-data-service
- description: API for building, managing, and deploying AI agents and conversational chatbots. Power Virtual Agents has been rebranded to Microsoft Copilot Studio with expanded AI agent capabilities.
  name: Microsoft Copilot Studio API (formerly Power Virtual Agents)
  slug: microsoft-copilot-studio-api-formerly-power-virtual-agents
- description: API for administrative operations across Power Platform environments including environment management, governance, capacity, and licensing via the BAP (Business Application Platform) endpoint.
  name: Power Platform Admin API
  slug: power-platform-admin-api
- description: API for custom and certified connectors that extend Power Platform capabilities across Power Apps, Power Automate, Logic Apps, and Copilot Studio.
  name: Power Platform Connectors API
  slug: power-platform-connectors-api
- description: Web API for Power Pages (formerly Power Apps Portals) enabling CRUD operations on Microsoft Dataverse tables from portal webpages for richer user experiences.
  name: Power Pages Web API
  slug: power-pages-web-api
- description: Operations for managing application packages within Power Platform environments, including listing available packages, installing applications, and checking installation status.
  name: Microsoft Power Platform APIs Applications API
  slug: power-platform-applications-api
- description: Operations for listing, creating, and managing Power Platform environments. Environments are containers that store apps, flows, data, and other resources.
  name: Microsoft Power Platform APIs Environments API
  slug: power-platform-environments-api
- description: Operations for monitoring and retrieving Power Automate flow run history within environments.
  name: Microsoft Power Platform APIs Flow Runs API
  slug: power-platform-flow-runs-api
- description: Operations for managing billing policies and licensing across the Power Platform tenant.
  name: Microsoft Power Platform APIs Licensing API
  slug: power-platform-licensing-api
artifact_total: 149
collections:
- collection_type: postman
  name: Microsoft Power Platform REST Applications API
  slug: postman-power-platform-applications-api
- collection_type: postman
  name: Microsoft Power Platform REST Applications Environments API
  slug: postman-power-platform-environments-api
- collection_type: postman
  name: Microsoft Power Platform REST Applications Flow Runs API
  slug: postman-power-platform-flow-runs-api
- collection_type: postman
  name: Microsoft Power Platform REST Applications Licensing API
  slug: postman-power-platform-licensing-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Power Platform REST API
  slug: open-power-platform-api
- collection_type: open
  name: Microsoft Power Platform REST Applications API
  slug: open-power-platform-applications-api
- collection_type: open
  name: Microsoft Power Platform REST Applications Environments API
  slug: open-power-platform-environments-api
- collection_type: open
  name: Microsoft Power Platform REST Applications Flow Runs API
  slug: open-power-platform-flow-runs-api
- collection_type: open
  name: Microsoft Power Platform REST Applications Licensing API
  slug: open-power-platform-licensing-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/microsoft/PowerPlatformConnectors/blob/dev/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-power-platform-apis/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/power-platform-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/power-platform-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/power-platform-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/power-platform-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/power-platform-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-power-platform
- group: start
  title: ''
  type: DeveloperPortal
  url: https://learn.microsoft.com/en-us/power-platform/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/power-platform/
- group: company
  title: ''
  type: Blog
  url: https://www.microsoft.com/en-us/power-platform/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft/powerplatform
- group: learn
  title: ''
  type: Training
  url: https://learn.microsoft.com/en-us/training/powerplatform/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.microsoft/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/privacystatement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/licensing/terms/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/power-platform/
- group: operate
  title: ''
  type: Support
  url: https://admin.powerplatform.microsoft.com/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/microsoft/powerbi-modeling-mcp
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/microsoft/power-platform-skills
created: '2024-01-15'
description: Collection of APIs for Microsoft Power Platform services including Power Apps, Power Automate, Power BI, Copilot Studio, Power Pages, and Dataverse.
examples:
- key_count: 3
  name: Power Platform Addon Info Example
  slug: power-platform-addon-info-example
- key_count: 8
  name: Power Platform Application Package Example
  slug: power-platform-application-package-example
- key_count: 2
  name: Power Platform Application Package List Response Example
  slug: power-platform-application-package-list-response-example
- key_count: 3
  name: Power Platform Billing Instrument Example
  slug: power-platform-billing-instrument-example
- key_count: 3
  name: Power Platform Billing Policy Create Request Example
  slug: power-platform-billing-policy-create-request-example
- key_count: 6
  name: Power Platform Billing Policy Example
  slug: power-platform-billing-policy-example
- key_count: 2
  name: Power Platform Billing Policy List Response Example
  slug: power-platform-billing-policy-list-response-example
- key_count: 2
  name: Power Platform Billing Policy Update Request Example
  slug: power-platform-billing-policy-update-request-example
- key_count: 5
  name: Power Platform Capacity Info Example
  slug: power-platform-capacity-info-example
- key_count: 4
  name: Power Platform Environment Example
  slug: power-platform-environment-example
- key_count: 1
  name: Power Platform Environment List Response Example
  slug: power-platform-environment-list-response-example
- key_count: 18
  name: Power Platform Environment Properties Example
  slug: power-platform-environment-properties-example
- key_count: 1
  name: Power Platform Error Response Example
  slug: power-platform-error-response-example
- key_count: 3
  name: Power Platform Flow Run Example
  slug: power-platform-flow-run-example
- key_count: 2
  name: Power Platform Flow Run List Response Example
  slug: power-platform-flow-run-list-response-example
- key_count: 5
  name: Power Platform Flow Run Properties Example
  slug: power-platform-flow-run-properties-example
- key_count: 13
  name: Power Platform Linked Environment Metadata Example
  slug: power-platform-linked-environment-metadata-example
- key_count: 5
  name: Power Platform Operation Status Example
  slug: power-platform-operation-status-example
- key_count: 4
  name: Power Platform Principal Example
  slug: power-platform-principal-example
features:
- description: Build custom business applications with drag-and-drop canvas and model-driven app builders without writing code.
  name: Low-Code App Development
- description: Automate repetitive business processes with cloud flows, desktop flows, and AI-powered process mining.
  name: Workflow Automation
- description: Create interactive dashboards and reports with Power BI for data-driven decision making across the organization.
  name: Business Intelligence
- description: Build conversational AI agents with Copilot Studio that integrate with Teams, websites, and other channels.
  name: AI-Powered Chatbots
- description: Extend platform capabilities by creating custom connectors to any REST API or third-party service.
  name: Custom Connectors
- description: Store and manage business data in a secure, scalable cloud database with built-in business logic and security.
  name: Dataverse Data Platform
- description: Manage isolated environments for development, testing, and production with governance policies and access controls.
  name: Environment Management
- description: Embed Power BI reports and dashboards directly into custom applications and portals.
  name: Embedded Analytics
finops:
- name: Power Platform Finops
  service_category: Business Applications
  slug: power-platform-finops
image: https://powerplatform.microsoft.com/images/power-platform-logo.png
integrations:
- description: Deep integration with Outlook, Teams, SharePoint, OneDrive, and Excel for seamless productivity workflows.
  name: Microsoft 365
- description: Connect to Azure services including Azure Active Directory, Azure SQL, Azure Functions, and Cognitive Services.
  name: Microsoft Azure
- description: Extend Dynamics 365 CRM and ERP applications with custom Power Apps and automated workflows.
  name: Dynamics 365
- description: Connect to SAP ERP and S/4HANA through certified connectors for enterprise data integration.
  name: SAP
- description: Integrate with Salesforce CRM data and workflows through the Salesforce connector.
  name: Salesforce
- description: Connect Power Platform workflows with ServiceNow ITSM and service management processes.
  name: ServiceNow
json_schemas:
- name: AddonInfo
  property_count: 3
  slug: power-platform-addon-info
- name: AddonInfo
  property_count: 3
  slug: power-platform-addoninfo
- name: ApplicationPackageListResponse
  property_count: 2
  slug: power-platform-application-package-list-response
- name: ApplicationPackage
  property_count: 8
  slug: power-platform-application-package
- name: ApplicationPackage
  property_count: 8
  slug: power-platform-applicationpackage
- name: ApplicationPackageListResponse
  property_count: 2
  slug: power-platform-applicationpackagelistresponse
- name: BillingInstrument
  property_count: 3
  slug: power-platform-billing-instrument
- name: BillingPolicyCreateRequest
  property_count: 3
  slug: power-platform-billing-policy-create-request
- name: BillingPolicyListResponse
  property_count: 2
  slug: power-platform-billing-policy-list-response
- name: BillingPolicy
  property_count: 6
  slug: power-platform-billing-policy
- name: BillingPolicyUpdateRequest
  property_count: 2
  slug: power-platform-billing-policy-update-request
- name: BillingInstrument
  property_count: 3
  slug: power-platform-billinginstrument
- name: BillingPolicy
  property_count: 9
  slug: power-platform-billingpolicy
- name: BillingPolicyCreateRequest
  property_count: 4
  slug: power-platform-billingpolicycreaterequest
- name: BillingPolicyListResponse
  property_count: 2
  slug: power-platform-billingpolicylistresponse
- name: BillingPolicyUpdateRequest
  property_count: 3
  slug: power-platform-billingpolicyupdaterequest
- name: CapacityInfo
  property_count: 5
  slug: power-platform-capacity-info
- name: CapacityInfo
  property_count: 5
  slug: power-platform-capacityinfo
- name: EnvironmentListResponse
  property_count: 1
  slug: power-platform-environment-list-response
- name: EnvironmentProperties
  property_count: 18
  slug: power-platform-environment-properties
- name: Environment
  property_count: 4
  slug: power-platform-environment
- name: EnvironmentListResponse
  property_count: 1
  slug: power-platform-environmentlistresponse
- name: EnvironmentProperties
  property_count: 20
  slug: power-platform-environmentproperties
- name: ErrorResponse
  property_count: 1
  slug: power-platform-error-response
- name: ErrorResponse
  property_count: 1
  slug: power-platform-errorresponse
- name: FlowRunListResponse
  property_count: 2
  slug: power-platform-flow-run-list-response
- name: FlowRunProperties
  property_count: 5
  slug: power-platform-flow-run-properties
- name: FlowRun
  property_count: 3
  slug: power-platform-flow-run
- name: FlowRun
  property_count: 4
  slug: power-platform-flowrun
- name: FlowRunListResponse
  property_count: 2
  slug: power-platform-flowrunlistresponse
- name: FlowRunProperties
  property_count: 5
  slug: power-platform-flowrunproperties
- name: LinkedEnvironmentMetadata
  property_count: 13
  slug: power-platform-linked-environment-metadata
- name: LinkedEnvironmentMetadata
  property_count: 13
  slug: power-platform-linkedenvironmentmetadata
- name: OperationStatus
  property_count: 5
  slug: power-platform-operation-status
- name: OperationStatus
  property_count: 5
  slug: power-platform-operationstatus
- name: Principal
  property_count: 4
  slug: power-platform-principal
json_structures:
- name: Power Platform Addon Info Structure
  property_count: 3
  slug: power-platform-addon-info-structure
- name: Power Platform Application Package List Response Structure
  property_count: 2
  slug: power-platform-application-package-list-response-structure
- name: Power Platform Application Package Structure
  property_count: 8
  slug: power-platform-application-package-structure
- name: Power Platform Billing Instrument Structure
  property_count: 3
  slug: power-platform-billing-instrument-structure
- name: Power Platform Billing Policy Create Request Structure
  property_count: 3
  slug: power-platform-billing-policy-create-request-structure
- name: Power Platform Billing Policy List Response Structure
  property_count: 2
  slug: power-platform-billing-policy-list-response-structure
- name: Power Platform Billing Policy Structure
  property_count: 6
  slug: power-platform-billing-policy-structure
- name: Power Platform Billing Policy Update Request Structure
  property_count: 2
  slug: power-platform-billing-policy-update-request-structure
- name: Power Platform Capacity Info Structure
  property_count: 5
  slug: power-platform-capacity-info-structure
- name: Power Platform Environment List Response Structure
  property_count: 1
  slug: power-platform-environment-list-response-structure
- name: Power Platform Environment Properties Structure
  property_count: 18
  slug: power-platform-environment-properties-structure
- name: Power Platform Environment Structure
  property_count: 4
  slug: power-platform-environment-structure
- name: Power Platform Error Response Structure
  property_count: 1
  slug: power-platform-error-response-structure
- name: Power Platform Flow Run List Response Structure
  property_count: 2
  slug: power-platform-flow-run-list-response-structure
- name: Power Platform Flow Run Properties Structure
  property_count: 5
  slug: power-platform-flow-run-properties-structure
- name: Power Platform Flow Run Structure
  property_count: 3
  slug: power-platform-flow-run-structure
- name: Power Platform Linked Environment Metadata Structure
  property_count: 13
  slug: power-platform-linked-environment-metadata-structure
- name: Power Platform Operation Status Structure
  property_count: 5
  slug: power-platform-operation-status-structure
- name: Power Platform Principal Structure
  property_count: 4
  slug: power-platform-principal-structure
- name: Power Platform Structure
  property_count: 0
  slug: power-platform-structure
jsonld:
- class_count: 0
  name: Power Platform Context
  property_count: 0
  slug: power-platform-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Microsoft Power Platform APIs
nav: Providers
network: true
overview: 'Microsoft Power Platform APIs publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Environments API, Flow Runs API, and 1 more. Tagged areas include Business Applications, Copilot Studio, Dataverse, Low-Code, and Microsoft.


  The Microsoft Power Platform APIs catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Microsoft Power Platform APIs'' developer surface includes authentication, documentation, engineering blog, training material, API reference, support, and 14 more developer resources.'
plans:
- name: Power Platform Plans Pricing
  plan_count: 9
  slug: power-platform-plans-pricing
random_paper: 130
rate_limits:
- limit_count: 10
  name: Power Platform Rate Limits
  slug: power-platform-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Microsoft Power Platform APIs API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: power-platform-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Microsoft Power Platform APIs API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 8
  slug: power-platform-spectral-rules
scopes:
- name: Power Platform Scopes
  scope_count: 1
  slug: power-platform-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: developing
  composite: 52.8
  delta: -2.9
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 9.8
    contract_quality: 69.6
    developer_ergonomics: 57.1
    discoverability: 72.2
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 55.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 64.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/power-platform/refs/heads/main/screenshots/power-platform-2026-06-20T192023.png
security:
- kind: authentication
  name: Power Platform Authentication
  slug: power-platform-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Power Platform Domain Security
  slug: power-platform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Power Platform Vulnerability Disclosure
  slug: power-platform-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 52
skills:
- name: activate-site
  slug: activate-site
- name: add-azuredevops
  slug: add-azuredevops
- name: add-cloud-flow
  slug: add-cloud-flow
- name: add-connector
  slug: add-connector
- name: add-data-source
  slug: add-data-source
- name: add-datasource
  slug: add-datasource
- name: add-dataverse
  slug: add-dataverse
- name: add-excel
  slug: add-excel
- name: add-mcscopilot
  slug: add-mcscopilot
- name: add-office365
  slug: add-office365
- name: add-onedrive
  slug: add-onedrive
- name: add-sample-data
  slug: add-sample-data
- name: add-seo
  slug: add-seo
- name: add-server-logic
  slug: add-server-logic
- name: add-sharepoint
  slug: add-sharepoint
- name: add-teams
  slug: add-teams
- name: audit-permissions
  slug: audit-permissions
- name: canvas-app
  slug: canvas-app
- name: configure-canvas-mcp
  slug: configure-canvas-mcp
- name: configure-env-variables
  slug: configure-env-variables
- name: create-code-app
  slug: create-code-app
- name: create-site
  slug: create-site
- name: create-webroles
  slug: create-webroles
- name: deploy-pipeline
  slug: deploy-pipeline
slug: power-platform
tags:
- Business Applications
- Copilot Studio
- Dataverse
- Low-Code
- Microsoft
- No-Code
- Power Pages
- Power Platform
use_cases:
- description: Enable business users to build departmental applications without IT involvement using low-code tools.
  name: Citizen Developer Apps
- description: Automate approval workflows, data collection, notifications, and integrations across Microsoft 365 and third-party services.
  name: Process Automation
- description: Consolidate data from multiple sources into unified dashboards and self-service analytics for executive decision-making.
  name: Enterprise Reporting
- description: Deploy AI-powered virtual agents for customer support, HR inquiries, and IT helpdesk automation.
  name: Customer Service Bots
- description: Connect and synchronize data across SaaS applications, on-premises systems, and cloud databases using connectors and Dataverse.
  name: Data Integration
website: https://learn.microsoft.com/en-us/power-platform/developer/
---
