---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Power Platform Agentic Access
  operation_count: 40
  slug: power-platform-agentic-access
  summary_line: 40 operations · 16 acting
api_count: 2
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
- baseURL: https://api.powerapps.com
  baseurl_source: declared
  description: Operations for managing application packages within Power Platform environments, including listing available packages, installing applications, and checking installation status.
  name: Microsoft Power Platform APIs Applications API
  phrasing_intents:
  - id: getEnvironmentApplicationPackages
    intent: List application packages for an environment
    question: Which app packages can I install in a particular Power Platform environment?
  - id: installApplicationPackage
    intent: Install an application package in an environment
    question: How do I install a Microsoft app package into one of my environments?
  - id: getApplicationPackageInstallStatus
    intent: Check an application package install's status
    question: Has my application package install finished or failed?
  - id: getTenantApplicationPackages
    intent: List installable packages for the tenant
    question: What Microsoft-provided application packages are available to my whole tenant?
  phrasing_ops: 4
  slug: power-platform-applications-api
- baseURL: https://api.powerapps.com
  baseurl_source: declared
  description: Operations for listing, creating, and managing Power Platform environments. Environments are containers that store apps, flows, data, and other resources.
  name: Microsoft Power Platform APIs Environments API
  phrasing_intents:
  - id: listEnvironments
    intent: List all environments in the tenant
    question: Which Power Platform environments exist in my tenant?
  - id: getEnvironment
    intent: Get details of one environment
    question: What region, SKU and Dataverse details does a particular environment have?
  - id: deleteEnvironment
    intent: Delete an environment permanently
    question: How do I delete a Power Platform environment?
  phrasing_ops: 3
  slug: power-platform-environments-api
- baseURL: https://api.powerapps.com
  baseurl_source: declared
  description: Operations for monitoring and retrieving Power Automate flow run history within environments.
  name: Microsoft Power Platform APIs Flow Runs API
  phrasing_intents:
  - id: listFlowRuns
    intent: List runs of a Power Automate flow
    question: How do I see the run history of a Power Automate flow?
  phrasing_ops: 1
  slug: power-platform-flow-runs-api
- baseURL: https://api.powerapps.com
  baseurl_source: declared
  description: Operations for managing billing policies and licensing across the Power Platform tenant.
  name: Microsoft Power Platform APIs Licensing API
  phrasing_intents:
  - id: listBillingPolicies
    intent: List the tenant's billing policies
    question: Which pay-as-you-go billing policies are configured for my tenant?
  - id: createBillingPolicy
    intent: Create a pay-as-you-go billing policy
    question: How do I set up pay-as-you-go billing for Power Platform against an Azure subscription?
  - id: getBillingPolicy
    intent: Get a billing policy
    question: What are the details of one specific billing policy?
  - id: updateBillingPolicy
    intent: Update an existing billing policy
    question: Can I rename an existing billing policy?
  - id: deleteBillingPolicy
    intent: Delete a billing policy
    question: How do I remove a pay-as-you-go billing policy?
  phrasing_ops: 5
  slug: power-platform-licensing-api
- description: The Microsoft Dataverse Web API provides OData v4 RESTful access to the Dataverse data platform that underpins Power Platform. Developers can perform CRUD operations on tables, execute actions and fun
  name: Microsoft Dataverse Web API
  slug: dataverse-api
- description: Power Platform Connectors provide pre-built integrations with hundreds of external services and enable developers to create custom connectors using OpenAPI definitions. Connectors abstract API authent
  name: Power Platform Connectors
  slug: connectors-api
- baseURL: https://{org}.api.crm.dynamics.com/api/data/v9.2/
  baseurl_source: declared
  description: The Metadata API from Microsoft Power Platform — 3 operation(s) for metadata.
  name: Microsoft Power Platform Metadata API
  phrasing_intents:
  - id: listEntityDefinitions
    intent: List all Dataverse table definitions
    question: What tables exist in my Dataverse environment?
  - id: getEntityDefinition
    intent: Get metadata for one Dataverse table
    question: How do I read the schema of a single Dataverse table?
  - id: whoAmI
    intent: Identify the signed-in Dataverse user
    question: Which user am I authenticated as against Dataverse?
  phrasing_ops: 3
  slug: microsoft-power-platform-metadata-api
- baseURL: https://{org}.api.crm.dynamics.com/api/data/v9.2/
  baseurl_source: declared
  description: The Records API from Microsoft Power Platform — 2 operation(s) for records.
  name: Microsoft Power Platform Records API
  phrasing_intents:
  - id: listRecords
    intent: Query records from a Dataverse table
    question: How do I pull rows out of a Dataverse table?
  - id: createRecord
    intent: Create a record in a Dataverse table
    question: How do I add a new row to a Dataverse table?
  - id: getRecord
    intent: Retrieve a single Dataverse record by id
    question: How do I fetch one Dataverse row when I know its GUID?
  - id: updateRecord
    intent: Update or upsert a Dataverse record
    question: How do I change fields on an existing Dataverse row?
  - id: deleteRecord
    intent: Delete a Dataverse record
    question: How do I remove a row from a Dataverse table?
  phrasing_ops: 5
  slug: microsoft-power-platform-records-api
- description: The unified REST API for Power Platform administration, at https://api.powerplatform.com/{namespace}/{resource}?api-version={version}. Namespaces include licensing, appmanagement, environmentmanagemen
  name: Power Platform API
  slug: power-platform-api
- baseURL: https://[org].api.crm.dynamics.com/api/data/v9.2
  baseurl_source: declared
  description: The Accounts API from Microsoft Power Platform APIs — 3 operation(s) for accounts.
  name: Microsoft Power Platform APIs Accounts API
  phrasing_intents:
  - id: Accounts_ListBySubscription
    intent: List Power Platform accounts in a subscription
    question: Which Power Platform accounts exist across my whole Azure subscription?
  - id: Accounts_ListByResourceGroup
    intent: List Power Platform accounts in a resource group
    question: What Power Platform accounts live in a single resource group?
  - id: Accounts_Get
    intent: Get details of a Power Platform account
    question: What configuration does a specific Power Platform account have?
  - id: Accounts_CreateOrUpdate
    intent: Create a Power Platform account
    question: How do I create a new Power Platform account as an Azure resource?
  - id: Accounts_Update
    intent: Update an existing Power Platform account
    question: Can I change the tags on an account that already exists?
  - id: Accounts_Delete
    intent: Delete a Power Platform account
    question: How do I remove a Power Platform account I no longer need?
  phrasing_ops: 6
  slug: power-platform-accounts-api
- baseURL: https://[org].api.crm.dynamics.com/api/data/v9.2
  baseurl_source: declared
  description: The EnterprisePolicies API from Microsoft Power Platform APIs — 3 operation(s) for enterprisepolicies.
  name: Microsoft Power Platform APIs Enterprise Policies API
  phrasing_intents:
  - id: EnterprisePolicies_ListBySubscription
    intent: List enterprise policies in a subscription
    question: Which Power Platform enterprise policies exist across my Azure subscription?
  - id: EnterprisePolicies_ListByResourceGroup
    intent: List enterprise policies in a resource group
    question: What enterprise policies are deployed in one resource group?
  - id: EnterprisePolicies_Get
    intent: Get details of an enterprise policy
    question: What kind and identity does a particular enterprise policy have?
  - id: EnterprisePolicies_CreateOrUpdate
    intent: Create an enterprise policy
    question: How do I create a new enterprise policy for Power Platform?
  - id: EnterprisePolicies_Update
    intent: Update an existing enterprise policy
    question: Can I change the tags on an enterprise policy that already exists?
  - id: EnterprisePolicies_Delete
    intent: Delete an enterprise policy
    question: How do I remove an enterprise policy I no longer use?
  phrasing_ops: 6
  slug: power-platform-enterprisepolicies-api
- baseURL: https://[org].api.crm.dynamics.com/api/data/v9.2
  baseurl_source: declared
  description: The Operations API from Microsoft Power Platform APIs — 1 operation(s) for operations.
  name: Microsoft Power Platform APIs Operations API
  phrasing_intents:
  - id: Operations_List
    intent: List available Power Platform REST operations
    question: What REST operations does the Microsoft.PowerPlatform resource provider expose?
  phrasing_ops: 1
  slug: power-platform-operations-api
- baseURL: https://[org].api.crm.dynamics.com/api/data/v9.2
  baseurl_source: declared
  description: The PrivateLinkResources API from Microsoft Power Platform APIs — 2 operation(s) for privatelinkresources.
  name: Microsoft Power Platform APIs Private Link Resources API
  phrasing_intents:
  - id: PrivateLinkResources_ListByEnterprisePolicy
    intent: List private link resources for a policy
    question: Which private link resources do I need to create for an enterprise policy?
  - id: PrivateLinkResources_Get
    intent: Get one private link resource for a policy
    question: What does a single named private link resource on my policy require?
  phrasing_ops: 2
  slug: power-platform-privatelinkresources-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Private Endpoint Connections API from Microsoft Power Platform APIs — 2 operation(s) for private endpoint connections.
  name: Microsoft Power Platform APIs Private Endpoint Connections API
  phrasing_intents:
  - id: PrivateEndpointConnections_ListByEnterprisePolicy
    intent: List private endpoint connections on a policy
    question: Which private endpoint connections are attached to an enterprise policy?
  - id: PrivateEndpointConnections_Get
    intent: Get a private endpoint connection
    question: What is the approval state of a specific private endpoint connection?
  - id: PrivateEndpointConnections_CreateOrUpdate
    intent: Approve or reject a private endpoint connection
    question: How do I approve a private endpoint request against my enterprise policy?
  - id: PrivateEndpointConnections_Delete
    intent: Delete a private endpoint connection
    question: How do I remove a private endpoint connection from an enterprise policy?
  phrasing_ops: 4
  slug: power-platform-private-endpoint-connections-api
artifact_total: 172
asyncapis:
- description: ''
  name: Power Platform Webhooks
  slug: power-platform-webhooks
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
- group: design
  href: https://artifacts.apis.io/power-platform/rules/power-platform-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/power-platform-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/power-platform/rules/power-platform-rules.yml
  title: ''
  type: Spectral
  url: rules/power-platform-rules.yml
- group: design
  href: https://artifacts.apis.io/power-platform/rules/power-platform-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/power-platform-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/power-platform/json-ld/power-platform-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/power-platform-context.jsonld
- group: design
  href: https://artifacts.apis.io/power-platform/vocabulary/power-platform-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/power-platform-vocabulary.yml
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: other
  href: https://artifacts.apis.io/power-platform/capabilities/power-platform-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/power-platform-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/power-platform/plans/power-platform-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/power-platform-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/power-platform/rate-limits/power-platform-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/power-platform-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/power-platform/finops/power-platform-finops.yml
  title: ''
  type: FinOps
  url: finops/power-platform-finops.yml
- group: agent
  href: https://artifacts.apis.io/power-platform/skills/power-platform-enterprise-policy-governance.md
  title: ''
  type: AgentSkill
  url: skills/power-platform-enterprise-policy-governance.md
- group: start
  title: ''
  type: Portal
  url: https://make.powerapps.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://powerapps.microsoft.com/en-us/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/power-platform/developer/get-started
- group: start
  title: ''
  type: SignUp
  url: https://www.microsoft.com/en-us/power-platform/products/power-apps/free
- group: operate
  title: ''
  type: Roadmap
  url: https://learn.microsoft.com/en-us/power-platform/release-plan/
- group: operate
  title: ''
  type: Community
  url: https://community.powerplatform.com/
- group: build
  href: https://artifacts.apis.io/power-platform/packages/power-platform-packages.yml
  title: ''
  type: Packages
  url: packages/power-platform-packages.yml
- group: build
  href: https://artifacts.apis.io/power-platform/packages/power-platform-packages.yml
  title: ''
  type: SDKs
  url: packages/power-platform-packages.yml
- group: build
  href: https://artifacts.apis.io/power-platform/cli/power-platform-cli.yml
  title: ''
  type: CLI
  url: cli/power-platform-cli.yml
- group: agent
  href: https://artifacts.apis.io/power-platform/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/power-platform/llms/power-platform-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/power-platform-llms.txt
- group: agent
  href: https://artifacts.apis.io/power-platform/well-known/power-platform-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/power-platform-well-known.yml
- group: auth
  href: https://artifacts.apis.io/power-platform/well-known/power-platform-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/power-platform-security.txt
- group: auth
  href: https://artifacts.apis.io/power-platform/security/power-platform-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/power-platform-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/power-platform/conformance/power-platform-conformance.yml
  title: ''
  type: Compliance
  url: conformance/power-platform-conformance.yml
- group: design
  href: https://artifacts.apis.io/power-platform/conformance/power-platform-conformance.yml
  title: ''
  type: Conformance
  url: conformance/power-platform-conformance.yml
- group: design
  href: https://artifacts.apis.io/power-platform/conventions/power-platform-conventions.yml
  title: ''
  type: Conventions
  url: conventions/power-platform-conventions.yml
- group: design
  href: https://artifacts.apis.io/power-platform/conventions/power-platform-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/power-platform-conventions.yml
- group: design
  href: https://artifacts.apis.io/power-platform/errors/power-platform-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/power-platform-problem-types.yml
- group: design
  href: https://artifacts.apis.io/power-platform/lifecycle/power-platform-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/power-platform-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/power-platform/important-changes-coming
- group: operate
  href: https://artifacts.apis.io/power-platform/changelog/power-platform-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/power-platform-changelog.yml
- group: design
  href: https://artifacts.apis.io/power-platform/asyncapi/power-platform-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/power-platform-webhooks.yml
- group: start
  href: https://artifacts.apis.io/power-platform/sandbox/power-platform-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/power-platform-sandbox.yml
- group: design
  href: https://artifacts.apis.io/power-platform/components/power-platform-components.yml
  title: ''
  type: Components
  url: components/power-platform-components.yml
- group: design
  href: https://artifacts.apis.io/power-platform/data-model/power-platform-data-model.yml
  title: ''
  type: DataModel
  url: data-model/power-platform-data-model.yml
- group: other
  href: https://artifacts.apis.io/power-platform/overlays/power-platform-records-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/power-platform-records-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/microsoft/PowerPlatformConnectors/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/microsoft/PowerPlatformConnectors/blob/dev/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/microsoft/.github/blob/main/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/microsoft/PowerPlatformConnectors/blob/dev/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-power-platform-apis/overview
- group: agent
  href: https://artifacts.apis.io/power-platform/agentic-access/power-platform-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/power-platform-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/power-platform/security/power-platform-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/power-platform-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/power-platform/security/power-platform-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/power-platform-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/power-platform/authentication/power-platform-authentication.yml
  title: ''
  type: Authentication
  url: authentication/power-platform-authentication.yml
- group: auth
  href: https://artifacts.apis.io/power-platform/scopes/power-platform-scopes.yml
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
- has_sources: true
  method: derived
  name: Power Platform Finops
  primary_unit: ''
  service_category: ''
  slug: power-platform-finops
  template: true
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
- name: AccountList
  property_count: 2
  slug: power-platform-account-list
- name: Account
  property_count: 1
  slug: power-platform-account
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
- name: EnterprisePolicyList
  property_count: 2
  slug: power-platform-enterprise-policy-list
- name: EnterprisePolicy
  property_count: 3
  slug: power-platform-enterprise-policy
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
- name: PatchAccount
  property_count: 4
  slug: power-platform-patch-account
- name: PatchEnterprisePolicy
  property_count: 6
  slug: power-platform-patch-enterprise-policy
- name: Principal
  property_count: 4
  slug: power-platform-principal
- name: PrivateEndpointConnectionListResult
  property_count: 2
  slug: power-platform-private-endpoint-connection-list-result
- name: PrivateEndpointConnection
  property_count: 1
  slug: power-platform-private-endpoint-connection
- name: PrivateLinkResourceListResult
  property_count: 2
  slug: power-platform-private-link-resource-list-result
- name: PrivateLinkResource
  property_count: 1
  slug: power-platform-private-link-resource
- name: RecordCollection
  property_count: 3
  slug: power-platform-record-collection
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
overview: 'Microsoft Power Platform APIs publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Applications API, Environments API, Flow Runs API, and 16 more. Tagged areas include Business Applications, Copilot Studio, Dataverse, Low-Code, and Microsoft.


  The Microsoft Power Platform APIs catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Microsoft Power Platform APIs'' developer surface includes developer portal, pricing, getting-started guide, signup flow, CLI, changelog, sandbox, and 55 more developer resources.'
plans:
- name: Power Platform Plans Pricing
  plan_count: 2
  slug: power-platform-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 10
  name: Power Platform Rate Limits
  slug: power-platform-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Microsoft Power Platform APIs — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: power-platform-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Microsoft Power Platform APIs API Rules
  rule_count: 63
  severity_counts:
    error: 48
    hint: 0
    info: 6
    warn: 9
  slug: power-platform-rules
- authorship: generated
  effective_rule_count: 58
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
  band: exemplar
  composite: 75.1
  coverage:
    artifact_dirs: 39
    catalog_earned: 66.0
    catalog_earned_first_party: 8.0
    catalog_gap: 49.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.0
  facets:
    access_clarity: 81.6
    contract_governance: 45.5
    contract_quality: 70.1
    developer_ergonomics: 83.9
    discoverability: 65.0
    operational_transparency: 65.8
  open_source:
    applies: true
    score: 50.0
  previous_composite: 72.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 43.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/power-platform/power-platform-2026-06-20T192023.png
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
- kind: trust-center
  name: Power Platform Trust Center
  slug: power-platform-trust-center
  summary_line: trust center published
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
website: https://www.microsoft.com/
---
