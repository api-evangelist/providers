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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Mulesoft Agentic Access
  operation_count: 15
  slug: mulesoft-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 1
apis:
- description: MuleSoft Anypoint Platform unifies API management with integration, providing a complete solution to connect any application, data source, or device with reusable APIs and integrations.
  name: MuleSoft Anypoint Platform
  slug: mulesoft
- description: The Anypoint Exchange API provides programmatic access to MuleSoft's asset marketplace, enabling discovery, publishing, and management of reusable integration assets including APIs, connectors, templa
  name: MuleSoft Anypoint Exchange API
  slug: mulesoft-anypoint-exchange-api
- description: The Anypoint Runtime Manager API provides programmatic control over Mule application deployments across CloudHub, Runtime Fabric, and hybrid deployment targets. It enables CI/CD automation for deployi
  name: MuleSoft Anypoint Runtime Manager API
  slug: mulesoft-anypoint-runtime-manager-api
- description: The Anypoint MQ API provides a cloud messaging service built on the Anypoint Platform for asynchronous messaging between Mule applications and other systems. It supports queues, exchanges, and dead-le
  name: MuleSoft Anypoint MQ API
  slug: mulesoft-anypoint-mq-api
- description: The Anypoint Design Center API provides access to the MuleSoft web-based API design environment for creating and editing API specifications in RAML and OAS formats. It supports project management, fil
  name: MuleSoft Anypoint Design Center API
  slug: mulesoft-anypoint-design-center-api
- baseURL: https://anypoint.mulesoft.com
  baseurl_source: declared
  description: Manage Mule applications deployed to CloudHub, Runtime Fabric, or hybrid targets. Includes operations for deploying, starting, stopping, and monitoring application instances.
  name: MuleSoft Applications API
  slug: mulesoft-applications-api
- baseURL: https://anypoint.mulesoft.com
  baseurl_source: declared
  description: Manage deployment environments within an organization. Environments provide isolated contexts for deploying and running Mule applications, such as Design, Sandbox, and Production.
  name: MuleSoft Environments API
  slug: mulesoft-environments-api
- baseURL: https://anypoint.mulesoft.com
  baseurl_source: declared
  description: Manage organizations and business groups within the Anypoint Platform. Organizations are the top-level containers for all platform resources including environments, users, and applications.
  name: MuleSoft Organizations API
  slug: mulesoft-organizations-api
arazzos:
- description: Walk from organization to environment to the applications running in it.
  name: MuleSoft Audit Application Inventory
  slug: mulesoft-audit-application-inventory-workflow
- description: Confirm an application exists, delete it, then verify it is gone.
  name: MuleSoft Decommission Application
  slug: mulesoft-decommission-app-workflow
- description: Deploy a CloudHub application and poll its status until it reaches STARTED.
  name: MuleSoft Deploy Application and Poll Until Started
  slug: mulesoft-deploy-app-and-poll-status-workflow
- description: Read an organization, apply MFA and session-timeout settings, then confirm.
  name: MuleSoft Harden Organization Security
  slug: mulesoft-harden-organization-security-workflow
- description: Read an application's config in one environment and deploy a copy into another.
  name: MuleSoft Promote Application Between Environments
  slug: mulesoft-promote-app-between-environments-workflow
- description: Create a new Anypoint environment and deploy a CloudHub application into it.
  name: MuleSoft Provision Environment and Deploy Application
  slug: mulesoft-provision-environment-and-deploy-app-workflow
- description: Find an organization by name, fetch its details, and list its environments.
  name: MuleSoft Resolve Organization and List Environments
  slug: mulesoft-resolve-org-and-list-environments-workflow
- description: Delete an application from an environment, then delete the environment itself.
  name: MuleSoft Tear Down Environment
  slug: mulesoft-teardown-environment-workflow
- description: Update a CloudHub application's runtime version then verify it redeploys.
  name: MuleSoft Update Application Runtime and Verify
  slug: mulesoft-update-app-runtime-and-verify-workflow
- description: Find an environment by name and update it if it exists, otherwise create it.
  name: MuleSoft Upsert Environment
  slug: mulesoft-upsert-environment-workflow
artifact_total: 128
collections:
- collection_type: postman
  name: MuleSoft Anypoint Platform API
  slug: postman-mulesoft-anypoint-platform
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MuleSoft Anypoint Platform API
  slug: open-mulesoft-anypoint-platform
- collection_type: open
  name: MuleSoft Anypoint Platform Applications API
  slug: open-mulesoft-applications-api
- collection_type: open
  name: MuleSoft Anypoint Platform Applications Environments API
  slug: open-mulesoft-environments-api
- collection_type: open
  name: MuleSoft Anypoint Platform Applications Organizations API
  slug: open-mulesoft-organizations-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/salesforce/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mulesoft-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mulesoft-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mulesoft-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/mulesoft/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mulesoft-audit-application-inventory-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mulesoft-decommission-app-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mulesoft-deploy-app-and-poll-status-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mulesoft-harden-organization-security-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mulesoft-promote-app-between-environments-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mulesoft-provision-environment-and-deploy-app-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mulesoft-resolve-org-and-list-environments-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mulesoft-teardown-environment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mulesoft-update-app-runtime-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mulesoft-upsert-environment-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mulesoft
- group: start
  title: ''
  type: Portal
  url: https://www.mulesoft.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mulesoft.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mulesoft.com/general/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.mulesoft.com/access-management/connected-apps-overview
- group: start
  title: ''
  type: Console
  url: https://anypoint.mulesoft.com/
- group: company
  title: ''
  type: Blog
  url: https://blogs.mulesoft.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.mulesoft.com/release-notes/
- group: operate
  title: ''
  type: StatusPage
  url: https://trust.mulesoft.com/
- group: operate
  title: ''
  type: Support
  url: https://help.mulesoft.com/s/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mulesoft.com/platform/mule-esb-open-source-esb/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mulesoft.com/legal/terms/EULA
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mulesoft.com/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mulesoft
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/mulesoft/anypoint-examples
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/mule
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/mulesofttv
- group: build
  title: ''
  type: SDKs
  url: https://docs.mulesoft.com/mule-sdk/latest/
- group: other
  title: ''
  type: Glossary
  url: https://docs.mulesoft.com/general/glossary
- group: start
  title: ''
  type: Signup
  url: https://anypoint.mulesoft.com/login/signup?apintent=generic
- group: start
  title: ''
  type: Login
  url: https://anypoint.mulesoft.com/login/signin?apintent=generic
- group: company
  title: ''
  type: Partners
  url: https://www.mulesoft.com/integration-partner/partnermax-retirement
- group: design
  title: ''
  type: SpectralRules
  url: rules/mulesoft-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/mulesoft-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.mulesoft.com/llms.txt
created: '2026-03-18'
description: MuleSoft Anypoint Platform is an enterprise integration and API management platform offering an API gateway, design center, exchange marketplace, and monitoring for hybrid deployments connecting applications and data.
examples:
- key_count: 8
  name: Mulesoft Anypoint Platform Application Create Example
  slug: mulesoft-anypoint-platform-application-create-example
- key_count: 19
  name: Mulesoft Anypoint Platform Application Example
  slug: mulesoft-anypoint-platform-application-example
- key_count: 4
  name: Mulesoft Anypoint Platform Application Status Example
  slug: mulesoft-anypoint-platform-application-status-example
- key_count: 7
  name: Mulesoft Anypoint Platform Application Update Example
  slug: mulesoft-anypoint-platform-application-update-example
- key_count: 3
  name: Mulesoft Anypoint Platform Entitlements Example
  slug: mulesoft-anypoint-platform-entitlements-example
- key_count: 2
  name: Mulesoft Anypoint Platform Environment Create Example
  slug: mulesoft-anypoint-platform-environment-create-example
- key_count: 8
  name: Mulesoft Anypoint Platform Environment Example
  slug: mulesoft-anypoint-platform-environment-example
- key_count: 2
  name: Mulesoft Anypoint Platform Environment Update Example
  slug: mulesoft-anypoint-platform-environment-update-example
- key_count: 2
  name: Mulesoft Anypoint Platform Error Example
  slug: mulesoft-anypoint-platform-error-example
- key_count: 16
  name: Mulesoft Anypoint Platform Organization Example
  slug: mulesoft-anypoint-platform-organization-example
- key_count: 4
  name: Mulesoft Anypoint Platform Organization Update Example
  slug: mulesoft-anypoint-platform-organization-update-example
- key_count: 2
  name: Mulesoft Anypoint Platform Resource Allocation Example
  slug: mulesoft-anypoint-platform-resource-allocation-example
- key_count: 3
  name: Mulesoft Anypoint Platform Subscription Example
  slug: mulesoft-anypoint-platform-subscription-example
- key_count: 2
  name: Mulesoft Anypoint Platform Worker Config Example
  slug: mulesoft-anypoint-platform-worker-config-example
- key_count: 6
  name: Mulesoft Createapplication Example
  slug: mulesoft-createapplication-example
- key_count: 6
  name: Mulesoft Createenvironment Example
  slug: mulesoft-createenvironment-example
- key_count: 6
  name: Mulesoft Getapplication Example
  slug: mulesoft-getapplication-example
- key_count: 6
  name: Mulesoft Getapplicationstatus Example
  slug: mulesoft-getapplicationstatus-example
- key_count: 6
  name: Mulesoft Getenvironment Example
  slug: mulesoft-getenvironment-example
- key_count: 6
  name: Mulesoft Getorganization Example
  slug: mulesoft-getorganization-example
- key_count: 6
  name: Mulesoft Listapplications Example
  slug: mulesoft-listapplications-example
- key_count: 6
  name: Mulesoft Listenvironments Example
  slug: mulesoft-listenvironments-example
- key_count: 6
  name: Mulesoft Listorganizations Example
  slug: mulesoft-listorganizations-example
- key_count: 6
  name: Mulesoft Updateapplication Example
  slug: mulesoft-updateapplication-example
- key_count: 6
  name: Mulesoft Updateenvironment Example
  slug: mulesoft-updateenvironment-example
- key_count: 6
  name: Mulesoft Updateorganization Example
  slug: mulesoft-updateorganization-example
features:
- description: Enterprise-grade API gateway for securing, governing, and managing API traffic across cloud and on-premises environments.
  name: API Gateway
- description: Centralized marketplace for discovering, sharing, and reusing APIs, connectors, templates, and integration assets across the organization.
  name: Anypoint Exchange
- description: Web-based API design environment for creating and editing API specifications in RAML and OAS formats with real-time collaboration.
  name: Design Center
- description: Unified management console for deploying, monitoring, and managing Mule applications across CloudHub, Runtime Fabric, and hybrid targets.
  name: Runtime Manager
- description: Cloud-native messaging service supporting queues, exchanges, and dead-letter queues for reliable asynchronous integration patterns.
  name: Anypoint MQ
- description: Powerful data transformation language for mapping and converting data between formats within Mule integration flows.
  name: DataWeave
- description: Eclipse-based IDE for building Mule applications with visual flow design and integrated debugging capabilities.
  name: Anypoint Studio
- description: Browser-based low-code tool for building simple integrations and automations without needing Anypoint Studio.
  name: Flow Designer
- description: Policy enforcement and governance framework for ensuring API consistency, security, and compliance across the platform.
  name: API Governance
- description: Real-time visibility into API and integration performance with dashboards, alerts, and log management.
  name: Anypoint Monitoring
finops:
- name: Mulesoft Finops
  service_category: Integration Platform / API Management
  slug: mulesoft-finops
graphqls:
- description: MuleSoft is an integration and API management platform. The Anypoint Platform API covers API design and publishing, CloudHub deployment, API analytics, access management, exchange artifacts, and Runti
  name: MuleSoft GraphQL API
  slug: mulesoft-graphql
image: /assets/icons/mulesoft.png
integrations:
- description: Native integration with Salesforce CRM, Service Cloud, and Marketing Cloud for bidirectional data sync and event-driven workflows.
  name: Salesforce
- description: Pre-built connector for SAP ERP, S/4HANA, and BTP enabling real-time data exchange with SAP systems.
  name: SAP
- description: Connector for syncing HR, finance, and planning data between Workday and other enterprise applications.
  name: Workday
- description: Integration with ServiceNow ITSM and ITOM for automated ticket creation, incident management, and CMDB sync.
  name: ServiceNow
- description: Connectors for Amazon S3, SQS, SNS, Lambda, and other AWS services for hybrid cloud integration.
  name: AWS
- description: Integration with Azure Service Bus, Blob Storage, SQL Database, and Active Directory services.
  name: Microsoft Azure
- description: Connector for sending notifications, creating channels, and automating workflows within Slack workspaces.
  name: Slack
- description: Pre-built connector for Oracle NetSuite ERP enabling financial, inventory, and order management integration.
  name: NetSuite
json_schemas:
- name: ApplicationCreate
  property_count: 8
  slug: mulesoft-anypoint-platform-application-create
- name: Application
  property_count: 19
  slug: mulesoft-anypoint-platform-application
- name: ApplicationStatus
  property_count: 4
  slug: mulesoft-anypoint-platform-application-status
- name: ApplicationUpdate
  property_count: 7
  slug: mulesoft-anypoint-platform-application-update
- name: Entitlements
  property_count: 3
  slug: mulesoft-anypoint-platform-entitlements
- name: EnvironmentCreate
  property_count: 2
  slug: mulesoft-anypoint-platform-environment-create
- name: Environment
  property_count: 8
  slug: mulesoft-anypoint-platform-environment
- name: EnvironmentUpdate
  property_count: 2
  slug: mulesoft-anypoint-platform-environment-update
- name: Error
  property_count: 2
  slug: mulesoft-anypoint-platform-error
- name: Organization
  property_count: 16
  slug: mulesoft-anypoint-platform-organization
- name: OrganizationUpdate
  property_count: 4
  slug: mulesoft-anypoint-platform-organization-update
- name: ResourceAllocation
  property_count: 2
  slug: mulesoft-anypoint-platform-resource-allocation
- name: Subscription
  property_count: 3
  slug: mulesoft-anypoint-platform-subscription
- name: WorkerConfig
  property_count: 2
  slug: mulesoft-anypoint-platform-worker-config
- name: MuleSoft Anypoint Application
  property_count: 27
  slug: mulesoft-application
- name: ApplicationCreate
  property_count: 9
  slug: mulesoft-applicationcreate
- name: ApplicationStatus
  property_count: 4
  slug: mulesoft-applicationstatus
- name: ApplicationUpdate
  property_count: 8
  slug: mulesoft-applicationupdate
- name: Entitlements
  property_count: 9
  slug: mulesoft-entitlements
- name: Environment
  property_count: 8
  slug: mulesoft-environment
- name: EnvironmentCreate
  property_count: 2
  slug: mulesoft-environmentcreate
- name: EnvironmentUpdate
  property_count: 2
  slug: mulesoft-environmentupdate
- name: Error
  property_count: 2
  slug: mulesoft-error
- name: Organization
  property_count: 18
  slug: mulesoft-organization
- name: OrganizationUpdate
  property_count: 4
  slug: mulesoft-organizationupdate
- name: ResourceAllocation
  property_count: 2
  slug: mulesoft-resourceallocation
- name: Subscription
  property_count: 3
  slug: mulesoft-subscription
- name: WorkerConfig
  property_count: 2
  slug: mulesoft-workerconfig
json_structures:
- name: Mulesoft Anypoint Platform Application Create Structure
  property_count: 8
  slug: mulesoft-anypoint-platform-application-create-structure
- name: Mulesoft Anypoint Platform Application Status Structure
  property_count: 4
  slug: mulesoft-anypoint-platform-application-status-structure
- name: Mulesoft Anypoint Platform Application Structure
  property_count: 19
  slug: mulesoft-anypoint-platform-application-structure
- name: Mulesoft Anypoint Platform Application Update Structure
  property_count: 7
  slug: mulesoft-anypoint-platform-application-update-structure
- name: Mulesoft Anypoint Platform Entitlements Structure
  property_count: 3
  slug: mulesoft-anypoint-platform-entitlements-structure
- name: Mulesoft Anypoint Platform Environment Create Structure
  property_count: 2
  slug: mulesoft-anypoint-platform-environment-create-structure
- name: Mulesoft Anypoint Platform Environment Structure
  property_count: 8
  slug: mulesoft-anypoint-platform-environment-structure
- name: Mulesoft Anypoint Platform Environment Update Structure
  property_count: 2
  slug: mulesoft-anypoint-platform-environment-update-structure
- name: Mulesoft Anypoint Platform Error Structure
  property_count: 2
  slug: mulesoft-anypoint-platform-error-structure
- name: Mulesoft Anypoint Platform Organization Structure
  property_count: 16
  slug: mulesoft-anypoint-platform-organization-structure
- name: Mulesoft Anypoint Platform Organization Update Structure
  property_count: 4
  slug: mulesoft-anypoint-platform-organization-update-structure
- name: Mulesoft Anypoint Platform Resource Allocation Structure
  property_count: 2
  slug: mulesoft-anypoint-platform-resource-allocation-structure
- name: Mulesoft Anypoint Platform Subscription Structure
  property_count: 3
  slug: mulesoft-anypoint-platform-subscription-structure
- name: Mulesoft Anypoint Platform Worker Config Structure
  property_count: 2
  slug: mulesoft-anypoint-platform-worker-config-structure
- name: Mulesoft Structure
  property_count: 0
  slug: mulesoft-structure
jsonld:
- class_count: 0
  name: Mulesoft Anypoint Platform Context
  property_count: 0
  slug: mulesoft-anypoint-platform-context
- class_count: 0
  name: Mulesoft Context
  property_count: 7
  slug: mulesoft-context
layout: provider
modified: '2026-08-30'
name: MuleSoft
nav: Providers
network: true
overview: 'MuleSoft publishes 3 APIs on the [APIs.io](https://apis.io/) network: Applications API, Environments API, and Organizations API. Tagged areas include API Gateway, API Management, Enterprise, and Integration.


  The MuleSoft catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  MuleSoft''s developer surface includes authentication, developer portal, documentation, getting-started guide, developer console, engineering blog, changelog, and 34 more developer resources.'
plans:
- name: Mulesoft Plans Pricing
  plan_count: 4
  slug: mulesoft-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Mulesoft Rate Limits
  slug: mulesoft-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: MuleSoft API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: mulesoft-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: MuleSoft API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 7
  slug: mulesoft-spectral-rules
score:
  band: developing
  composite: 52.7
  coverage:
    artifact_dirs: 22
    catalog_gap: 58.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 28.8
    contract_quality: 74.9
    developer_ergonomics: 69.0
    discoverability: 57.4
    governance: 28.8
    operational_transparency: 34.2
  previous_composite: 52.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mulesoft/refs/heads/main/screenshots/mulesoft-2026-06-20T185854.png
security:
- kind: authentication
  name: Mulesoft Authentication
  slug: mulesoft-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mulesoft Domain Security
  slug: mulesoft-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: mulesoft
tags:
- API Gateway
- API Management
- Enterprise
- Integration
use_cases:
- description: Connect SaaS and on-premises applications to create unified business processes and eliminate data silos.
  name: Application Integration
- description: Build reusable APIs organized in system, process, and experience layers to accelerate digital transformation.
  name: API-Led Connectivity
- description: Automate partner onboarding and EDI/AS2 data exchange with trading partners using pre-built connectors.
  name: B2B Integration
- description: Migrate on-premises integrations to the cloud while maintaining connectivity with legacy systems.
  name: Cloud Migration
- description: Unify customer data across CRM, ERP, and marketing systems to create a single view of the customer.
  name: Customer 360
- description: Connect AI agents to enterprise systems, models, and vector stores to orchestrate complex agentic workflows.
  name: AI Agent Integration
website: https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/
---
