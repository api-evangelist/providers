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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Workday Studio Agentic Access
  operation_count: 22
  slug: workday-studio-agentic-access
  summary_line: 22 operations · 11 acting
api_count: 2
apis:
- description: RESTful API providing modern JSON-based access to Workday data and services. Uses OAuth 2.0 authentication and standard HTTP methods for operations across HCM, financial management, recruiting, payrol
  name: Workday REST API
  slug: workday-rest-api
- description: API for creating and executing custom reports built in Workday Studio. Exposes custom reports as RESTful web services through Report-as-a-Service (RaaS), enabling programmatic access to report data wi
  name: Workday Custom Reports API
  slug: workday-custom-reports-api
- description: Low-code integration and automation platform for building event-driven and batch integrations using a visual drag-and-drop builder. Enables developers to create workflows that connect Workday with ext
  name: Workday Orchestrate API
  slug: workday-orchestrate-api
- baseURL_template: https://{baseUrl}/ccx/service/{tenant}
  baseurl_source: spec_template
  description: Web service operations for managing time-off requests, leave balances, absence plans, and return-to-work processes.
  name: Workday Studio Absence Management API
  slug: workday-studio-absence-management-api
- baseURL_template: https://{baseUrl}/ccx/service/{tenant}
  baseurl_source: spec_template
  description: Web service operations for benefits enrollment, plan management, coverage administration, and life events processing.
  name: Workday Studio Benefits Administration API
  slug: workday-studio-benefits-administration-api
- baseURL_template: https://{baseUrl}/ccx/service/{tenant}
  baseurl_source: spec_template
  description: Web service operations for compensation plans, pay grades, salary structures, and bonus configurations.
  name: Workday Studio Compensation API
  slug: workday-studio-compensation-api
- baseURL_template: https://{baseUrl}/ccx/service/{tenant}
  baseurl_source: spec_template
  description: Web service operations for financial accounting, expense management, revenue management, and financial reporting.
  name: Workday Studio Financial Management API
  slug: workday-studio-financial-management-api
- baseURL_template: https://{baseUrl}/ccx/service/{tenant}
  baseurl_source: spec_template
  description: Web service operations for managing employee data, worker records, organizational structures, and HR transactions.
  name: Workday Studio Human Resources API
  slug: workday-studio-human-resources-api
- baseURL_template: https://{baseUrl}/ccx/service/{tenant}
  baseurl_source: spec_template
  description: Manage Studio integration assemblies, which are the graphical representations of integration logic composed of configurable components.
  name: Workday Studio Integration Assemblies API
  slug: workday-studio-integration-assemblies-api
- baseURL_template: https://{baseUrl}/ccx/service/{tenant}
  baseurl_source: spec_template
  description: Monitor and retrieve integration execution events including run status, processing statistics, and error details.
  name: Workday Studio Integration Events API
  slug: workday-studio-integration-events-api
- baseURL_template: https://{baseUrl}/ccx/service/{tenant}
  baseurl_source: spec_template
  description: Manage integration systems configured in the Workday tenant, including Studio-built integrations and core connector configurations.
  name: Workday Studio Integration Systems API
  slug: workday-studio-integration-systems-api
- baseURL_template: https://{baseUrl}/ccx/service/{tenant}
  baseurl_source: spec_template
  description: Access available integration templates and core connectors that serve as starting points for building new integrations.
  name: Workday Studio Integration Templates API
  slug: workday-studio-integration-templates-api
- baseURL_template: https://{baseUrl}/ccx/service/{tenant}
  baseurl_source: spec_template
  description: Configure and retrieve launch parameters used to control integration execution behavior at runtime.
  name: Workday Studio Launch Parameters API
  slug: workday-studio-launch-parameters-api
- baseURL_template: https://{baseUrl}/ccx/service/{tenant}
  baseurl_source: spec_template
  description: Web service operations for payroll processing, tax management, compensation calculations, and pay component configurations.
  name: Workday Studio Payroll API
  slug: workday-studio-payroll-api
- baseURL_template: https://{baseUrl}/ccx/service/{tenant}
  baseurl_source: spec_template
  description: Web service operations for job postings, candidate management, application tracking, and offer management.
  name: Workday Studio Recruiting API
  slug: workday-studio-recruiting-api
- baseURL_template: https://{baseUrl}/ccx/service/{tenant}
  baseurl_source: spec_template
  description: Operations for discovering available web services, their versions, and WSDL definitions.
  name: Workday Studio Service Directory API
  slug: workday-studio-service-directory-api
- baseURL_template: https://{baseUrl}/ccx/service/{tenant}
  baseurl_source: spec_template
  description: Web service operations for position management, job requisitions, hiring actions, and organizational staffing.
  name: Workday Studio Staffing API
  slug: workday-studio-staffing-api
- baseURL_template: https://{baseUrl}/ccx/service/{tenant}
  baseurl_source: spec_template
  description: Web service operations for time entry, timesheet management, time calculations, and clock-in/clock-out records.
  name: Workday Studio Time Tracking API
  slug: workday-studio-time-tracking-api
artifact_total: 133
collections:
- collection_type: postman
  name: Workday Studio Integration Absence Management API
  slug: postman-workday-studio-absence-management-api
- collection_type: postman
  name: Workday Studio Integration Absence Management Benefits Administration API
  slug: postman-workday-studio-benefits-administration-api
- collection_type: postman
  name: Workday Studio Integration Absence Management Compensation API
  slug: postman-workday-studio-compensation-api
- collection_type: postman
  name: Workday Studio Integration Absence Management Financial Management API
  slug: postman-workday-studio-financial-management-api
- collection_type: postman
  name: Workday Studio Integration Absence Management Human Resources API
  slug: postman-workday-studio-human-resources-api
- collection_type: postman
  name: Workday Studio Integration Absence Management Integration Assemblies API
  slug: postman-workday-studio-integration-assemblies-api
- collection_type: postman
  name: Workday Studio Integration Absence Management Integration Events API
  slug: postman-workday-studio-integration-events-api
- collection_type: postman
  name: Workday Studio Integration Absence Management Integration Systems API
  slug: postman-workday-studio-integration-systems-api
- collection_type: postman
  name: Workday Studio Integration Absence Management Integration Templates API
  slug: postman-workday-studio-integration-templates-api
- collection_type: postman
  name: Workday Studio Integration Absence Management Launch Parameters API
  slug: postman-workday-studio-launch-parameters-api
- collection_type: postman
  name: Workday Studio Integration Absence Management Payroll API
  slug: postman-workday-studio-payroll-api
- collection_type: postman
  name: Workday Studio Integration Absence Management Recruiting API
  slug: postman-workday-studio-recruiting-api
- collection_type: postman
  name: Workday Studio Integration Absence Management Service Directory API
  slug: postman-workday-studio-service-directory-api
- collection_type: postman
  name: Workday Studio Integration Absence Management Staffing API
  slug: postman-workday-studio-staffing-api
- collection_type: postman
  name: Workday Studio Integration Absence Management Time Tracking API
  slug: postman-workday-studio-time-tracking-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Workday Studio Integration Absence Management API
  slug: open-workday-studio-absence-management-api
- collection_type: open
  name: Workday Studio Integration Absence Management Benefits Administration API
  slug: open-workday-studio-benefits-administration-api
- collection_type: open
  name: Workday Studio Integration Absence Management Compensation API
  slug: open-workday-studio-compensation-api
- collection_type: open
  name: Workday Studio Integration Absence Management Financial Management API
  slug: open-workday-studio-financial-management-api
- collection_type: open
  name: Workday Studio Integration Absence Management Human Resources API
  slug: open-workday-studio-human-resources-api
- collection_type: open
  name: Workday Studio Integration Absence Management Integration Assemblies API
  slug: open-workday-studio-integration-assemblies-api
- collection_type: open
  name: Workday Studio Integration Absence Management Integration Events API
  slug: open-workday-studio-integration-events-api
- collection_type: open
  name: Workday Studio Integration Absence Management Integration Systems API
  slug: open-workday-studio-integration-systems-api
- collection_type: open
  name: Workday Studio Integration Absence Management Integration Templates API
  slug: open-workday-studio-integration-templates-api
- collection_type: open
  name: Workday Studio Integration API
  slug: open-workday-studio-integration
- collection_type: open
  name: Workday Studio Integration Absence Management Launch Parameters API
  slug: open-workday-studio-launch-parameters-api
- collection_type: open
  name: Workday Studio Integration Absence Management Payroll API
  slug: open-workday-studio-payroll-api
- collection_type: open
  name: Workday Studio Integration Absence Management Recruiting API
  slug: open-workday-studio-recruiting-api
- collection_type: open
  name: Workday Studio Integration Absence Management Service Directory API
  slug: open-workday-studio-service-directory-api
- collection_type: open
  name: Workday Studio Integration Absence Management Staffing API
  slug: open-workday-studio-staffing-api
- collection_type: open
  name: Workday Studio Integration Absence Management Time Tracking API
  slug: open-workday-studio-time-tracking-api
- collection_type: open
  name: Workday Studio Workday Web Services API
  slug: open-workday-studio-web-services
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/workday-studio/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workday-studio-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/workday-studio-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workday-studio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workday-studio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/workday-studio-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.workday.com/
- group: start
  title: ''
  type: Portal
  url: https://community.workday.com/
- group: start
  title: ''
  type: Console
  url: https://developer.workday.com/about
- group: start
  title: ''
  type: Login
  url: https://www.myworkday.com/
- group: start
  title: ''
  type: Signup
  url: https://community.workday.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.workday.com/en-us/guides.html
- group: start
  title: ''
  type: GettingStarted
  url: https://community.workday.com/node/97816
- group: auth
  title: ''
  type: Authentication
  url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html#authentication
- group: docs
  title: ''
  type: APIReference
  url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
- group: operate
  title: ''
  type: Support
  url: https://www.workday.com/en-us/customer-experience/support.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workday.com/en-us/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workday.com/en-us/privacy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.workday.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.workday.com/
- group: company
  title: ''
  type: DeveloperBlog
  url: https://workday.github.io/
- group: operate
  title: ''
  type: Contact
  url: https://www.workday.com/en-us/company/about-workday/contact-us.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Workday
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.workday.com/en-US/home
- group: learn
  title: ''
  type: Training
  url: https://www.workday.com/en-us/services/training-certifications.html
- group: other
  title: ''
  type: StudioDownload
  url: https://community.workday.com/studio-download
- group: design
  title: ''
  type: SpectralRules
  url: rules/workday-studio-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/workday-studio-vocabulary.yaml
created: '2024-01-01'
description: Workday Studio is an integrated development environment (IDE) for building custom integrations and applications on the Workday platform. It provides tools for creating web services, custom reports, and integration solutions.
features:
- description: Workday Studio is an Eclipse-based development environment with a graphical, drag-and-drop interface for designing custom integrations.
  name: Eclipse-based IDE
- description: Provides a library of reusable integration components for transports, transformations, splitters, and routing logic that accelerate integration development.
  name: Reusable Components
- description: Includes constructs for branching, looping, retries, and structured error handling to build resilient integrations.
  name: Flow Control and Error Handling
- description: Supports XSLT, XPath, and scripting for mapping and transforming data between Workday and external systems.
  name: Data Transformation
- description: Exposes custom Workday reports as RESTful web services through Report-as-a-Service (RaaS) for downstream consumption.
  name: Custom Report-as-a-Service
- description: Provides SOAP and REST access to 55+ Workday service areas including HCM, Financial Management, Payroll, and Benefits.
  name: Workday Web Services
- description: Offers OAuth 2.0-secured JSON REST endpoints for accessing Workday data and triggering business actions.
  name: Modern REST API
- description: Workday Orchestrate enables building event-driven and batch integrations through a visual workflow builder without writing code.
  name: Orchestrate Low-Code Integrations
- description: Integrations are deployed against tenant-specific endpoints with environment isolation between sandbox and production tenants.
  name: Tenant-Based Deployment
finops:
- name: Workday Studio Finops
  service_category: HR / Finance SaaS
  slug: workday-studio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workday-studio.png
integrations:
- description: Workday Studio runs as an Eclipse-based plug-in providing the development surface for building integrations.
  name: Eclipse IDE
- description: Common integration target for syncing customer, opportunity, and worker data between Workday and Salesforce.
  name: Salesforce
- description: Connect Workday to ServiceNow for IT service management and HR case management workflows.
  name: ServiceNow
- description: Integrate Workday HCM with ADP and other third-party payroll providers for payroll data exchange.
  name: ADP
- description: Sync worker data with Microsoft 365 and Azure Active Directory for identity provisioning and collaboration tooling.
  name: Microsoft 365 and Azure AD
- description: Bridge Workday financial and HR data with SAP ERP systems for organizations running mixed environments.
  name: SAP
- description: Use Workday integrations to push and pull data from cloud storage, messaging, and data warehouses.
  name: AWS, Azure, and Google Cloud
- description: Stream Workday data into Snowflake, BigQuery, and other warehouses for analytics and reporting.
  name: Snowflake and Data Warehouses
json_schemas:
- name: AbsenceInputsResponse
  property_count: 2
  slug: workday-studio-absenceinputsresponse
- name: AssemblyComponent
  property_count: 4
  slug: workday-studio-assemblycomponent
- name: BenefitPlansResponse
  property_count: 2
  slug: workday-studio-benefitplansresponse
- name: CandidatesResponse
  property_count: 2
  slug: workday-studio-candidatesresponse
- name: CompensationPlansResponse
  property_count: 2
  slug: workday-studio-compensationplansresponse
- name: ErrorResponse
  property_count: 2
  slug: workday-studio-errorresponse
- name: GetAbsenceInputsRequest
  property_count: 2
  slug: workday-studio-getabsenceinputsrequest
- name: GetBenefitPlansRequest
  property_count: 2
  slug: workday-studio-getbenefitplansrequest
- name: GetCandidatesRequest
  property_count: 2
  slug: workday-studio-getcandidatesrequest
- name: GetCompensationPlansRequest
  property_count: 2
  slug: workday-studio-getcompensationplansrequest
- name: GetJobPostingsRequest
  property_count: 2
  slug: workday-studio-getjobpostingsrequest
- name: GetJournalEntriesRequest
  property_count: 2
  slug: workday-studio-getjournalentriesrequest
- name: GetOrganizationsRequest
  property_count: 2
  slug: workday-studio-getorganizationsrequest
- name: GetPayrollResultsRequest
  property_count: 2
  slug: workday-studio-getpayrollresultsrequest
- name: GetTimeClockEventsRequest
  property_count: 2
  slug: workday-studio-gettimeclockeventsrequest
- name: GetWorkersRequest
  property_count: 3
  slug: workday-studio-getworkersrequest
- name: IntegrationAssembliesResponse
  property_count: 2
  slug: workday-studio-integrationassembliesresponse
- name: IntegrationAssembly
  property_count: 7
  slug: workday-studio-integrationassembly
- name: IntegrationEvent
  property_count: 10
  slug: workday-studio-integrationevent
- name: IntegrationEventsResponse
  property_count: 2
  slug: workday-studio-integrationeventsresponse
- name: IntegrationLaunchRequest
  property_count: 1
  slug: workday-studio-integrationlaunchrequest
- name: IntegrationLogEntry
  property_count: 4
  slug: workday-studio-integrationlogentry
- name: IntegrationLogsResponse
  property_count: 2
  slug: workday-studio-integrationlogsresponse
- name: IntegrationSystem
  property_count: 9
  slug: workday-studio-integrationsystem
- name: IntegrationSystemsResponse
  property_count: 2
  slug: workday-studio-integrationsystemsresponse
- name: IntegrationTemplate
  property_count: 5
  slug: workday-studio-integrationtemplate
- name: IntegrationTemplatesResponse
  property_count: 2
  slug: workday-studio-integrationtemplatesresponse
- name: JobPostingsResponse
  property_count: 2
  slug: workday-studio-jobpostingsresponse
- name: JournalEntriesResponse
  property_count: 2
  slug: workday-studio-journalentriesresponse
- name: LaunchParameter
  property_count: 6
  slug: workday-studio-launchparameter
- name: LaunchParametersResponse
  property_count: 2
  slug: workday-studio-launchparametersresponse
- name: Organization
  property_count: 7
  slug: workday-studio-organization
- name: OrganizationsResponse
  property_count: 2
  slug: workday-studio-organizationsresponse
- name: PayrollResultsResponse
  property_count: 2
  slug: workday-studio-payrollresultsresponse
- name: RequestCriteria
  property_count: 5
  slug: workday-studio-requestcriteria
- name: ResourceReference
  property_count: 3
  slug: workday-studio-resourcereference
- name: ServiceMetadata
  property_count: 4
  slug: workday-studio-servicemetadata
- name: TimeClockEventsResponse
  property_count: 2
  slug: workday-studio-timeclockeventsresponse
- name: Worker
  property_count: 9
  slug: workday-studio-worker
- name: WorkersResponse
  property_count: 2
  slug: workday-studio-workersresponse
json_structures:
- name: Workday Studio Structure
  property_count: 0
  slug: workday-studio-structure
layout: provider
modified: '2026-05-19'
name: Workday Studio
nav: Providers
network: true
overview: 'Workday Studio publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Absence Management API, Benefits Administration API, Compensation API, and 12 more. Tagged areas include Cloud, Development, Enterprise, Finance, and HR.


  The Workday Studio catalog on APIs.io includes 2 Spectral governance rulesets.


  Workday Studio''s developer surface includes authentication, developer portal, developer console, signup flow, documentation, getting-started guide, API reference, and 21 more developer resources.'
plans:
- name: Workday Studio Plans Pricing
  plan_count: 1
  slug: workday-studio-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Workday Studio Rate Limits
  slug: workday-studio-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Workday Studio API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: workday-studio-jsonschema-spectral-rules
- effective_rule_count: 108
  extends:
  - spectral:oas
  name: Workday Studio API Rules
  rule_count: 67
  severity_counts:
    error: 25
    hint: 0
    info: 9
    warn: 33
  slug: workday-studio-spectral-rules
scopes:
- name: Workday Studio Scopes
  scope_count: 4
  slug: workday-studio-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 47.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 71.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 48.7
    commercial_clarity: 48.7
    contract_governance: 28.8
    contract_quality: 55.1
    developer_ergonomics: 69.0
    discoverability: 50.0
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 47.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/workday-studio/refs/heads/main/screenshots/workday-studio-2026-06-20T201611.png
security:
- kind: authentication
  name: Workday Studio Authentication
  slug: workday-studio-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Workday Studio Domain Security
  slug: workday-studio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Workday Studio Trust Center
  slug: workday-studio-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
slug: workday-studio
solutions:
- description: Cloud-based human capital management covering core HR, talent, learning, recruiting, and workforce planning.
  name: Workday HCM
- description: Cloud financial management for accounting, revenue, expenses, projects, and analytics.
  name: Workday Financial Management
- description: Native payroll for the United States, Canada, United Kingdom, and France integrated with Workday HCM.
  name: Workday Payroll
- description: Enterprise planning, budgeting, and forecasting platform that integrates with Workday Financials and HCM.
  name: Workday Adaptive Planning
- description: Platform for building custom apps that extend Workday functionality using the same data model and security.
  name: Workday Extend
- description: Low-code integration and automation platform for building workflows across Workday and external systems.
  name: Workday Orchestrate
- description: Curated catalog of partner-built integrations and apps that extend the Workday platform.
  name: Workday Marketplace
tags:
- Cloud
- Development
- Enterprise
- Finance
- HR
- IDE
- Integration
use_cases:
- description: Build bespoke integrations between Workday and external HR, payroll, benefits, and financial systems.
  name: Custom Integrations
- description: Connect Workday HCM and Payroll to third-party payroll providers, banks, and benefits carriers for data exchange.
  name: Payroll and Benefits Connectivity
- description: Keep worker records, organizational data, and position information in sync between Workday and downstream systems.
  name: Employee Data Synchronization
- description: Generate custom reports in Workday Studio and expose them through Report-as-a-Service for use in BI tools and dashboards.
  name: Custom Reporting
- description: Automate cross-system HR and finance business processes using Workday Orchestrate event-driven workflows.
  name: Business Process Automation
- description: Integrate Workday Financial Management with downstream ERPs, CRMs, and procurement systems for invoicing and revenue management.
  name: ERP and CRM Integration
- description: Synchronize worker lifecycle events from Workday into identity providers and downstream applications for user provisioning.
  name: Identity and Access Provisioning
website: https://www.workday.com/
---
