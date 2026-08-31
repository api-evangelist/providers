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
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 353
  human_in_the_loop: 32
  name: Microsoft Azure Functions Agentic Access
  operation_count: 692
  slug: microsoft-azure-functions-agentic-access
  summary_line: 692 operations · 353 acting · 32 human-in-the-loop
api_count: 1
apis:
- description: The Azure Functions host runtime provides HTTP endpoints for function invocation, admin operations, host status, function management, and key management. Includes endpoints for listing functions, gett
  name: Azure Functions Runtime API
  slug: azure-functions-runtime-api
- description: The AppServiceEnvironments API from Microsoft Azure Functions — 36 operation(s) for appserviceenvironments.
  name: Microsoft Azure Functions AppServiceEnvironments API
  slug: microsoft-azure-functions-appserviceenvironments-api
- description: The AppServicePlans API from Microsoft Azure Functions — 22 operation(s) for appserviceplans.
  name: Microsoft Azure Functions AppServicePlans API
  slug: microsoft-azure-functions-appserviceplans-api
- description: The Certificates API from Microsoft Azure Functions — 3 operation(s) for certificates.
  name: Microsoft Azure Functions Certificates API
  slug: microsoft-azure-functions-certificates-api
- description: The DeletedWebApps API from Microsoft Azure Functions — 3 operation(s) for deletedwebapps.
  name: Microsoft Azure Functions DeletedWebApps API
  slug: microsoft-azure-functions-deletedwebapps-api
- description: The Diagnostics API from Microsoft Azure Functions — 22 operation(s) for diagnostics.
  name: Microsoft Azure Functions Diagnostics API
  slug: microsoft-azure-functions-diagnostics-api
- description: The Global API from Microsoft Azure Functions — 3 operation(s) for global.
  name: Microsoft Azure Functions Global API
  slug: microsoft-azure-functions-global-api
- description: The KubeEnvironments API from Microsoft Azure Functions — 3 operation(s) for kubeenvironments.
  name: Microsoft Azure Functions KubeEnvironments API
  slug: microsoft-azure-functions-kubeenvironments-api
- description: The Operations API from Microsoft Azure Functions — 1 operation(s) for operations.
  name: Microsoft Azure Functions Operations API
  slug: microsoft-azure-functions-operations-api
- description: The Provider API from Microsoft Azure Functions — 7 operation(s) for provider.
  name: Microsoft Azure Functions Provider API
  slug: microsoft-azure-functions-provider-api
- description: The Providers API from Microsoft Azure Functions — 3 operation(s) for providers.
  name: Microsoft Azure Functions Providers API
  slug: microsoft-azure-functions-providers-api
- description: The Recommendations API from Microsoft Azure Functions — 15 operation(s) for recommendations.
  name: Microsoft Azure Functions Recommendations API
  slug: microsoft-azure-functions-recommendations-api
- description: The ResourceHealthMetadata API from Microsoft Azure Functions — 6 operation(s) for resourcehealthmetadata.
  name: Microsoft Azure Functions ResourceHealthMetadata API
  slug: microsoft-azure-functions-resourcehealthmetadata-api
- description: The SiteCertificates API from Microsoft Azure Functions — 4 operation(s) for sitecertificates.
  name: Microsoft Azure Functions SiteCertificates API
  slug: microsoft-azure-functions-sitecertificates-api
- description: The StaticSites API from Microsoft Azure Functions — 51 operation(s) for staticsites.
  name: Microsoft Azure Functions StaticSites API
  slug: microsoft-azure-functions-staticsites-api
- description: The Subscriptions API from Microsoft Azure Functions — 15 operation(s) for subscriptions.
  name: Microsoft Azure Functions Subscriptions API
  slug: microsoft-azure-functions-subscriptions-api
- description: The WebApps API from Microsoft Azure Functions — 300 operation(s) for webapps.
  name: Microsoft Azure Functions WebApps API
  slug: microsoft-azure-functions-webapps-api
- description: The WorkflowRunActions API from Microsoft Azure Functions — 10 operation(s) for workflowrunactions.
  name: Microsoft Azure Functions WorkflowRunActions API
  slug: microsoft-azure-functions-workflowrunactions-api
- description: The WorkflowRuns API from Microsoft Azure Functions — 3 operation(s) for workflowruns.
  name: Microsoft Azure Functions WorkflowRuns API
  slug: microsoft-azure-functions-workflowruns-api
- description: The Workflows API from Microsoft Azure Functions — 2 operation(s) for workflows.
  name: Microsoft Azure Functions Workflows API
  slug: microsoft-azure-functions-workflows-api
- description: The WorkflowTriggerHistories API from Microsoft Azure Functions — 3 operation(s) for workflowtriggerhistories.
  name: Microsoft Azure Functions WorkflowTriggerHistories API
  slug: microsoft-azure-functions-workflowtriggerhistories-api
- description: The WorkflowTriggers API from Microsoft Azure Functions — 5 operation(s) for workflowtriggers.
  name: Microsoft Azure Functions WorkflowTriggers API
  slug: microsoft-azure-functions-workflowtriggers-api
- description: The WorkflowVersions API from Microsoft Azure Functions — 2 operation(s) for workflowversions.
  name: Microsoft Azure Functions WorkflowVersions API
  slug: microsoft-azure-functions-workflowversions-api
arazzos:
- description: Create a single function inside an existing function app, then read it back to confirm it exists.
  name: Create a Function in a Function App and Verify It
  slug: microsoft-azure-functions-create-function-and-verify-workflow
- description: Create a function, sync the function app's triggers, and list the resulting trigger status.
  name: Deploy a Function and Sync Its Triggers
  slug: microsoft-azure-functions-deploy-function-and-sync-triggers-workflow
- description: Read a function app, list its functions, and issue a Functions admin token for the runtime API.
  name: Inspect a Function App and Issue an Admin Token
  slug: microsoft-azure-functions-inspect-app-and-issue-admin-token-workflow
- description: Create a function app, poll until it reports a running state, then list its functions.
  name: Provision an Azure Function App and Confirm It Is Running
  slug: microsoft-azure-functions-provision-function-app-workflow
- description: Create a deployment slot on a function app, poll it until running, and ensure it is started.
  name: Provision a Staging Deployment Slot
  slug: microsoft-azure-functions-provision-staging-slot-workflow
- description: Create a deployment record on a function app, read it back, and list all deployments.
  name: Record a Deployment and Verify the Deployment Log
  slug: microsoft-azure-functions-record-deployment-workflow
- description: Create or update a named function key, then list the function keys to confirm the new value is in place.
  name: Rotate a Function Key and Confirm It
  slug: microsoft-azure-functions-rotate-function-key-workflow
- description: Create or update a host key (function or system) of a function app, then list all host keys to confirm.
  name: Rotate a Host-Level Key and List All Host Keys
  slug: microsoft-azure-functions-rotate-host-key-workflow
- description: Diff a staging slot against a target, swap it in, and confirm the app is running.
  name: Preview and Swap a Slot Into Production
  slug: microsoft-azure-functions-swap-slot-to-production-workflow
- description: Read the current app settings, write a merged set, and list them back to confirm.
  name: Update Function App Settings and Confirm Them
  slug: microsoft-azure-functions-update-app-settings-workflow
- description: Read the web site configuration, apply changes, then restart the app to pick them up.
  name: Update Function App Site Configuration and Restart
  slug: microsoft-azure-functions-update-site-config-workflow
artifact_total: 189
collections:
- collection_type: postman
  name: WebApps API Client
  slug: postman-azure-functions-management-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WebApps API Client
  slug: open-azure-functions-management-api
- collection_type: open
  name: WebApps API Client AppServiceEnvironments API
  slug: open-microsoft-azure-functions-appserviceenvironments-api
- collection_type: open
  name: WebApps API Client AppServiceEnvironments AppServicePlans API
  slug: open-microsoft-azure-functions-appserviceplans-api
- collection_type: open
  name: WebApps API Client AppServiceEnvironments Certificates API
  slug: open-microsoft-azure-functions-certificates-api
- collection_type: open
  name: WebApps API Client AppServiceEnvironments DeletedWebApps API
  slug: open-microsoft-azure-functions-deletedwebapps-api
- collection_type: open
  name: WebApps API Client AppServiceEnvironments Diagnostics API
  slug: open-microsoft-azure-functions-diagnostics-api
- collection_type: open
  name: WebApps API Client AppServiceEnvironments Global API
  slug: open-microsoft-azure-functions-global-api
- collection_type: open
  name: WebApps API Client AppServiceEnvironments KubeEnvironments API
  slug: open-microsoft-azure-functions-kubeenvironments-api
- collection_type: open
  name: WebApps API Client AppServiceEnvironments Operations API
  slug: open-microsoft-azure-functions-operations-api
- collection_type: open
  name: WebApps API Client AppServiceEnvironments Provider API
  slug: open-microsoft-azure-functions-provider-api
- collection_type: open
  name: WebApps API Client AppServiceEnvironments Providers API
  slug: open-microsoft-azure-functions-providers-api
- collection_type: open
  name: WebApps API Client AppServiceEnvironments Recommendations API
  slug: open-microsoft-azure-functions-recommendations-api
- collection_type: open
  name: WebApps API Client AppServiceEnvironments ResourceHealthMetadata API
  slug: open-microsoft-azure-functions-resourcehealthmetadata-api
- collection_type: open
  name: WebApps API Client AppServiceEnvironments SiteCertificates API
  slug: open-microsoft-azure-functions-sitecertificates-api
- collection_type: open
  name: WebApps API Client AppServiceEnvironments StaticSites API
  slug: open-microsoft-azure-functions-staticsites-api
- collection_type: open
  name: WebApps API Client AppServiceEnvironments Subscriptions API
  slug: open-microsoft-azure-functions-subscriptions-api
- collection_type: open
  name: API Client AppServiceEnvironments WebApps API
  slug: open-microsoft-azure-functions-webapps-api
- collection_type: open
  name: WebApps API Client AppServiceEnvironments WorkflowRunActions API
  slug: open-microsoft-azure-functions-workflowrunactions-api
- collection_type: open
  name: WebApps API Client AppServiceEnvironments WorkflowRuns API
  slug: open-microsoft-azure-functions-workflowruns-api
- collection_type: open
  name: WebApps API Client AppServiceEnvironments Workflows API
  slug: open-microsoft-azure-functions-workflows-api
- collection_type: open
  name: WebApps API Client AppServiceEnvironments WorkflowTriggerHistories API
  slug: open-microsoft-azure-functions-workflowtriggerhistories-api
- collection_type: open
  name: WebApps API Client AppServiceEnvironments WorkflowTriggers API
  slug: open-microsoft-azure-functions-workflowtriggers-api
- collection_type: open
  name: WebApps API Client AppServiceEnvironments WorkflowVersions API
  slug: open-microsoft-azure-functions-workflowversions-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Azure/azure-functions-host/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Azure/azure-functions-host/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Azure/azure-functions-host/blob/dev/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Azure/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Azure/azure-functions-host/blob/dev/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Azure/azure-functions-host/blob/dev/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-functions-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-functions-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-functions-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-functions-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-azure-functions/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-functions-create-function-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-functions-deploy-function-and-sync-triggers-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-functions-inspect-app-and-issue-admin-token-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-functions-provision-function-app-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-functions-provision-staging-slot-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-functions-record-deployment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-functions-rotate-function-key-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-functions-rotate-host-key-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-functions-swap-slot-to-production-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-functions-update-app-settings-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-functions-update-site-config-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/azure-functions/functions-get-started
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/azure-functions/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/functions/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/azure/azure-functions/functions-versions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Azure/azure-functions-host
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Azure/azure-functions-core-tools
- group: build
  title: .NET SDK
  type: SDKs
  url: https://www.nuget.org/packages/Microsoft.Azure.Functions.Worker
- group: build
  title: Python SDK
  type: SDKs
  url: https://pypi.org/project/azure-functions/
- group: build
  title: Node.js SDK
  type: SDKs
  url: https://www.npmjs.com/package/@azure/functions
- group: build
  title: Java SDK
  type: SDKs
  url: https://central.sonatype.com/artifact/com.microsoft.azure.functions/azure-functions-java-library
- group: build
  title: Azure Functions Core Tools
  type: CLI
  url: https://github.com/Azure/azure-functions-core-tools
- group: build
  title: Azure CLI (az functionapp)
  type: CLI
  url: https://learn.microsoft.com/en-us/cli/azure/functionapp
- group: learn
  title: ''
  type: Training
  url: https://learn.microsoft.com/en-us/training/paths/create-serverless-applications/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-functions
- group: other
  title: ''
  type: X
  url: https://x.com/AzureFunctions
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Azure/azure-functions-mcp-extension
created: '2024-01-01'
description: Azure Functions is a serverless compute platform from Microsoft Azure enabling event-driven code execution triggered by HTTP requests, timers, queues, blobs, and other Azure services. The Azure Functions management API provides programmatic access to function app lifecycle management, deployment, configuration, scaling, and monitoring through Azure Resource Manager.
examples:
- key_count: 5
  name: Azure Functions App Service Plan Example
  slug: azure-functions-app-service-plan-example
- key_count: 2
  name: Azure Functions Backup Item Example
  slug: azure-functions-backup-item-example
- key_count: 1
  name: Azure Functions Backup Request Example
  slug: azure-functions-backup-request-example
- key_count: 2
  name: Azure Functions Certificate Example
  slug: azure-functions-certificate-example
- key_count: 1
  name: Azure Functions Connection String Dictionary Example
  slug: azure-functions-connection-string-dictionary-example
- key_count: 2
  name: Azure Functions Csm Publishing Credentials Policies Entity Example
  slug: azure-functions-csm-publishing-credentials-policies-entity-example
- key_count: 1
  name: Azure Functions Custom Hostname Analysis Result Example
  slug: azure-functions-custom-hostname-analysis-result-example
- key_count: 9
  name: Azure Functions Deployment Properties Example
  slug: azure-functions-deployment-properties-example
- key_count: 2
  name: Azure Functions Function Envelope Example
  slug: azure-functions-function-envelope-example
- key_count: 10
  name: Azure Functions Function Envelope Properties Example
  slug: azure-functions-function-envelope-properties-example
- key_count: 3
  name: Azure Functions Host Keys Example
  slug: azure-functions-host-keys-example
- key_count: 2
  name: Azure Functions Host Name Binding Example
  slug: azure-functions-host-name-binding-example
- key_count: 2
  name: Azure Functions Hybrid Connection Example
  slug: azure-functions-hybrid-connection-example
- key_count: 2
  name: Azure Functions Key Info Example
  slug: azure-functions-key-info-example
- key_count: 1
  name: Azure Functions Migrate My Sql Request Example
  slug: azure-functions-migrate-my-sql-request-example
- key_count: 2
  name: Azure Functions Premier Add On Example
  slug: azure-functions-premier-add-on-example
- key_count: 2
  name: Azure Functions Public Certificate Example
  slug: azure-functions-public-certificate-example
- key_count: 1
  name: Azure Functions Restore Request Example
  slug: azure-functions-restore-request-example
- key_count: 1
  name: Azure Functions Site Auth Settings Example
  slug: azure-functions-site-auth-settings-example
- key_count: 10
  name: Azure Functions Site Config Example
  slug: azure-functions-site-config-example
- key_count: 4
  name: Azure Functions Site Example
  slug: azure-functions-site-example
- key_count: 2
  name: Azure Functions Site Extension Info Example
  slug: azure-functions-site-extension-info-example
- key_count: 2
  name: Azure Functions Site Logs Config Example
  slug: azure-functions-site-logs-config-example
- key_count: 10
  name: Azure Functions Site Properties Example
  slug: azure-functions-site-properties-example
- key_count: 2
  name: Azure Functions Slot Config Names Resource Example
  slug: azure-functions-slot-config-names-resource-example
- key_count: 1
  name: Azure Functions Storage Migration Options Example
  slug: azure-functions-storage-migration-options-example
- key_count: 1
  name: Azure Functions String Dictionary Example
  slug: azure-functions-string-dictionary-example
- key_count: 2
  name: Azure Functions Triggered Web Job Example
  slug: azure-functions-triggered-web-job-example
- key_count: 2
  name: Azure Functions Web Job Example
  slug: azure-functions-web-job-example
features:
- description: Execute functions via HTTP requests with RESTful endpoint support and built-in authentication.
  name: HTTP Triggers
- description: Schedule function execution using CRON expressions for recurring tasks.
  name: Timer Triggers
- description: Process messages from Azure Storage Queues and Service Bus for async workloads.
  name: Queue Triggers
- description: React to blob storage changes for file processing and data pipeline automation.
  name: Blob Triggers
- description: Handle events from Azure Event Grid for event-driven architectures.
  name: Event Grid Triggers
- description: Process database changes in Azure Cosmos DB using the change feed.
  name: Cosmos DB Triggers
- description: Orchestrate complex stateful workflows with function chaining, fan-out/fan-in, and human interaction patterns.
  name: Durable Functions
- description: Manage staging and production slots for zero-downtime deployments and traffic splitting.
  name: Deployment Slots
- description: Run functions in any language by implementing a lightweight HTTP server.
  name: Custom Handlers
- description: Authenticate to Azure services without managing credentials using system or user-assigned identities.
  name: Managed Identity
- description: Automatic scaling from zero to thousands of instances based on event load.
  name: Scaling
- description: Pre-warmed instances, VNET integration, and unlimited execution duration for enterprise workloads.
  name: Premium Plan
finops:
- name: Microsoft Azure Functions Finops
  service_category: API
  slug: microsoft-azure-functions-finops
image: /assets/icons/microsoft-azure-functions.png
integrations:
- description: Front Azure Functions with API Management for rate limiting, authentication, and developer portal.
  name: Azure API Management
- description: CI/CD pipeline integration for automated function deployment and testing.
  name: Azure DevOps
- description: Deploy Azure Functions directly from GitHub repositories with Actions workflows.
  name: GitHub Actions
- description: Full development experience with the Azure Functions VS Code extension.
  name: Visual Studio Code
- description: Application Insights integration for function monitoring, logging, and diagnostics.
  name: Azure Monitor
- description: Secure secrets management with Key Vault references in application settings.
  name: Azure Key Vault
- description: Infrastructure-as-code management of function apps with the AzureRM Terraform provider.
  name: Terraform
json_schemas:
- name: AppServicePlan
  property_count: 5
  slug: azure-functions-app-service-plan
- name: BackupItem
  property_count: 2
  slug: azure-functions-backup-item
- name: BackupRequest
  property_count: 1
  slug: azure-functions-backup-request
- name: Certificate
  property_count: 2
  slug: azure-functions-certificate
- name: ConnectionStringDictionary
  property_count: 1
  slug: azure-functions-connection-string-dictionary
- name: CsmPublishingCredentialsPoliciesEntity
  property_count: 2
  slug: azure-functions-csm-publishing-credentials-policies-entity
- name: CustomHostnameAnalysisResult
  property_count: 1
  slug: azure-functions-custom-hostname-analysis-result
- name: DeploymentProperties
  property_count: 9
  slug: azure-functions-deployment-properties
- name: FunctionEnvelopeProperties
  property_count: 13
  slug: azure-functions-function-envelope-properties
- name: FunctionEnvelope
  property_count: 2
  slug: azure-functions-function-envelope
- name: HostKeys
  property_count: 3
  slug: azure-functions-host-keys
- name: HostNameBinding
  property_count: 2
  slug: azure-functions-host-name-binding
- name: HybridConnection
  property_count: 2
  slug: azure-functions-hybrid-connection
- name: KeyInfo
  property_count: 2
  slug: azure-functions-key-info
- name: MigrateMySqlRequest
  property_count: 1
  slug: azure-functions-migrate-my-sql-request
- name: PremierAddOn
  property_count: 2
  slug: azure-functions-premier-add-on
- name: PublicCertificate
  property_count: 2
  slug: azure-functions-public-certificate
- name: RestoreRequest
  property_count: 1
  slug: azure-functions-restore-request
- name: SiteAuthSettings
  property_count: 1
  slug: azure-functions-site-auth-settings
- name: SiteConfig
  property_count: 73
  slug: azure-functions-site-config
- name: SiteExtensionInfo
  property_count: 2
  slug: azure-functions-site-extension-info
- name: SiteLogsConfig
  property_count: 2
  slug: azure-functions-site-logs-config
- name: SiteProperties
  property_count: 56
  slug: azure-functions-site-properties
- name: Site
  property_count: 4
  slug: azure-functions-site
- name: SlotConfigNamesResource
  property_count: 2
  slug: azure-functions-slot-config-names-resource
- name: StorageMigrationOptions
  property_count: 1
  slug: azure-functions-storage-migration-options
- name: StringDictionary
  property_count: 1
  slug: azure-functions-string-dictionary
- name: TriggeredWebJob
  property_count: 2
  slug: azure-functions-triggered-web-job
- name: WebJob
  property_count: 2
  slug: azure-functions-web-job
json_structures:
- name: Azure Functions App Service Plan Structure
  property_count: 5
  slug: azure-functions-app-service-plan-structure
- name: Azure Functions Backup Item Structure
  property_count: 2
  slug: azure-functions-backup-item-structure
- name: Azure Functions Backup Request Structure
  property_count: 1
  slug: azure-functions-backup-request-structure
- name: Azure Functions Certificate Structure
  property_count: 2
  slug: azure-functions-certificate-structure
- name: Azure Functions Connection String Dictionary Structure
  property_count: 1
  slug: azure-functions-connection-string-dictionary-structure
- name: Azure Functions Csm Publishing Credentials Policies Entity Structure
  property_count: 2
  slug: azure-functions-csm-publishing-credentials-policies-entity-structure
- name: Azure Functions Custom Hostname Analysis Result Structure
  property_count: 1
  slug: azure-functions-custom-hostname-analysis-result-structure
- name: Azure Functions Deployment Properties Structure
  property_count: 9
  slug: azure-functions-deployment-properties-structure
- name: Azure Functions Function Envelope Properties Structure
  property_count: 13
  slug: azure-functions-function-envelope-properties-structure
- name: Azure Functions Function Envelope Structure
  property_count: 2
  slug: azure-functions-function-envelope-structure
- name: Azure Functions Host Keys Structure
  property_count: 3
  slug: azure-functions-host-keys-structure
- name: Azure Functions Host Name Binding Structure
  property_count: 2
  slug: azure-functions-host-name-binding-structure
- name: Azure Functions Hybrid Connection Structure
  property_count: 2
  slug: azure-functions-hybrid-connection-structure
- name: Azure Functions Key Info Structure
  property_count: 2
  slug: azure-functions-key-info-structure
- name: Azure Functions Migrate My Sql Request Structure
  property_count: 1
  slug: azure-functions-migrate-my-sql-request-structure
- name: Azure Functions Premier Add On Structure
  property_count: 2
  slug: azure-functions-premier-add-on-structure
- name: Azure Functions Public Certificate Structure
  property_count: 2
  slug: azure-functions-public-certificate-structure
- name: Azure Functions Restore Request Structure
  property_count: 1
  slug: azure-functions-restore-request-structure
- name: Azure Functions Site Auth Settings Structure
  property_count: 1
  slug: azure-functions-site-auth-settings-structure
- name: Azure Functions Site Config Structure
  property_count: 73
  slug: azure-functions-site-config-structure
- name: Azure Functions Site Extension Info Structure
  property_count: 2
  slug: azure-functions-site-extension-info-structure
- name: Azure Functions Site Logs Config Structure
  property_count: 2
  slug: azure-functions-site-logs-config-structure
- name: Azure Functions Site Properties Structure
  property_count: 56
  slug: azure-functions-site-properties-structure
- name: Azure Functions Site Structure
  property_count: 4
  slug: azure-functions-site-structure
- name: Azure Functions Slot Config Names Resource Structure
  property_count: 2
  slug: azure-functions-slot-config-names-resource-structure
- name: Azure Functions Storage Migration Options Structure
  property_count: 1
  slug: azure-functions-storage-migration-options-structure
- name: Azure Functions String Dictionary Structure
  property_count: 1
  slug: azure-functions-string-dictionary-structure
- name: Azure Functions Triggered Web Job Structure
  property_count: 2
  slug: azure-functions-triggered-web-job-structure
- name: Azure Functions Web Job Structure
  property_count: 2
  slug: azure-functions-web-job-structure
jsonld:
- class_count: 29
  name: Azure Functions Context
  property_count: 158
  slug: azure-functions-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Microsoft Azure Functions
nav: Providers
network: true
overview: 'Microsoft Azure Functions publishes 22 APIs on the [APIs.io](https://apis.io/) network, including AppServiceEnvironments API, AppServicePlans API, Certificates API, and 19 more. Tagged areas include Azure, Cloud, Compute, Event-Driven, and Microsoft.


  The Microsoft Azure Functions catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Microsoft Azure Functions'' developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, engineering blog, and 38 more developer resources.'
plans:
- name: Microsoft Azure Functions Plans Pricing
  plan_count: 3
  slug: microsoft-azure-functions-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Microsoft Azure Functions Rate Limits
  slug: microsoft-azure-functions-rate-limits
rules:
- effective_rule_count: 19
  extends: []
  name: Microsoft Azure Functions API Rules
  rule_count: 19
  severity_counts:
    error: 14
    hint: 0
    info: 3
    warn: 2
  slug: azure-functions-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Microsoft Azure Functions API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-azure-functions-jsonschema-spectral-rules
- effective_rule_count: 44
  extends:
  - spectral:oas
  name: Microsoft Azure Functions API Rules
  rule_count: 3
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 3
  slug: microsoft-azure-functions-spectral-rules
scopes:
- name: Microsoft Azure Functions Scopes
  scope_count: 1
  slug: microsoft-azure-functions-scopes
  summary_line: 1 scope · implicit
score:
  band: strong
  composite: 64.3
  coverage:
    artifact_dirs: 19
    catalog_gap: 40.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 3.4
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 54.5
    contract_quality: 54.0
    developer_ergonomics: 85.7
    discoverability: 68.5
    governance: 54.5
    operational_transparency: 52.6
  open_source:
    applies: true
    score: 100.0
  previous_composite: 60.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-functions/refs/heads/main/screenshots/microsoft-azure-functions-2026-06-20T185418.png
security:
- kind: authentication
  name: Microsoft Azure Functions Authentication
  slug: microsoft-azure-functions-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Functions Domain Security
  slug: microsoft-azure-functions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-functions
solutions:
- description: Pay-per-execution pricing with automatic scaling and 5-minute execution timeout.
  name: Consumption Plan
- description: Pre-warmed instances, VNET integration, unlimited duration, and larger instance sizes.
  name: Premium Plan
- description: Run functions on dedicated App Service plans for predictable pricing and always-on execution.
  name: Dedicated Plan
- description: Run containerized functions on Azure Container Apps for Kubernetes-based hosting.
  name: Container Apps
tags:
- Azure
- Cloud
- Compute
- Event-Driven
- Microsoft
- Serverless
use_cases:
- description: Build serverless REST APIs with HTTP-triggered functions and Azure API Management integration.
  name: API Backend
- description: Process events from queues, topics, Event Grid, and IoT Hub for real-time data pipelines.
  name: Event Processing
- description: Run scheduled jobs for data cleanup, report generation, and system maintenance.
  name: Scheduled Tasks
- description: Transform, validate, and process files uploaded to blob storage.
  name: File Processing
- description: Receive and process webhooks from third-party services and SaaS platforms.
  name: Webhook Handling
- description: Build lightweight microservices with independent scaling and deployment.
  name: Microservices
- description: ETL workloads for transforming and loading data between Azure services.
  name: Data Transformation
- description: Process IoT device telemetry and events with Event Hub and IoT Hub triggers.
  name: IoT Backend
website: https://portal.azure.com/
---
