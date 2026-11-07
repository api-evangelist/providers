---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 347
  human_in_the_loop: 32
  name: Microsoft Azure Functions Agentic Access
  operation_count: 693
  slug: microsoft-azure-functions-agentic-access
  summary_line: 693 operations · 347 acting · 32 human-in-the-loop
api_count: 1
apis:
- description: The Azure Functions host runtime provides HTTP endpoints for function invocation, admin operations, host status, function management, and key management. Includes endpoints for listing functions, gett
  name: Azure Functions Runtime API
  slug: azure-functions-runtime-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The AppServiceEnvironments API from Microsoft Azure Functions — 36 operation(s) for appserviceenvironments.
  name: Microsoft Azure Functions AppServiceEnvironments API
  phrasing_intents:
  - id: AppServiceEnvironments_List
    intent: List all App Service Environments in a subscription
    question: Which App Service Environments exist across my whole Azure subscription?
  - id: AppServiceEnvironments_ListByResourceGroup
    intent: List App Service Environments in a resource group
    question: What App Service Environments live in this particular resource group?
  - id: AppServiceEnvironments_Get
    intent: Get an App Service Environment's properties
    question: What are the current settings and status of one App Service Environment?
  - id: AppServiceEnvironments_CreateOrUpdate
    intent: Create or replace an App Service Environment
    question: How do I provision a brand-new App Service Environment?
  - id: AppServiceEnvironments_Update
    intent: Patch an existing App Service Environment
    question: Can I change just a few settings on an existing ASE without resending everything?
  - id: AppServiceEnvironments_Delete
    intent: Delete an App Service Environment
    question: How do I tear down an App Service Environment I no longer need?
  - id: AppServiceEnvironments_ListCapacities
    intent: Get worker compute capacity of an ASE
    question: How much worker capacity is used versus available in my App Service Environment?
  - id: AppServiceEnvironments_GetVipInfo
    intent: Get IP addresses assigned to an ASE
    question: Which virtual IP addresses are assigned to my App Service Environment?
  phrasing_ops: 48
  slug: microsoft-azure-functions-appserviceenvironments-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The AppServicePlans API from Microsoft Azure Functions — 22 operation(s) for appserviceplans.
  name: Microsoft Azure Functions AppServicePlans API
  phrasing_intents:
  - id: AppServicePlans_List
    intent: List App Service plans across a subscription
    question: What App Service plans exist across my whole Azure subscription?
  - id: AppServicePlans_ListByResourceGroup
    intent: List App Service plans in a resource group
    question: Which App Service plans live in one particular resource group?
  - id: AppServicePlans_Get
    intent: Get an App Service plan
    question: How do I look up the details of one App Service plan by name?
  - id: AppServicePlans_CreateOrUpdate
    intent: Create or replace an App Service plan
    question: How do I create a new App Service plan with a chosen SKU?
  - id: AppServicePlans_Update
    intent: Patch properties of an existing App Service plan
    question: Can I change a few settings on an existing App Service plan without resending everything?
  - id: AppServicePlans_Delete
    intent: Delete an App Service plan
    question: How do I remove an App Service plan I no longer need?
  - id: AppServicePlans_ListCapabilities
    intent: List capabilities of an App Service plan
    question: What features and capabilities does my App Service plan support?
  - id: AppServicePlans_GetServerFarmRdpPassword
    intent: Get the RDP password for a custom-mode plan
    question: How do I get the remote desktop password for a custom-mode server farm?
  phrasing_ops: 30
  slug: microsoft-azure-functions-appserviceplans-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Certificates API from Microsoft Azure Functions — 3 operation(s) for certificates.
  name: Microsoft Azure Functions Certificates API
  phrasing_intents:
  - id: Certificates_List
    intent: List certificates in a subscription
    question: Which App Service certificates exist across my whole Azure subscription?
  - id: Certificates_ListByResourceGroup
    intent: List certificates in a resource group
    question: What certificates are stored in one particular resource group?
  - id: Certificates_Get
    intent: Get a certificate
    question: When does one of my App Service certificates expire, and what hostnames does it cover?
  - id: Certificates_CreateOrUpdate
    intent: Upload or replace a certificate
    question: How do I upload a TLS certificate for my function apps and web apps?
  - id: Certificates_Update
    intent: Patch an existing certificate
    question: Can I change just some properties of an existing certificate without re-uploading it?
  - id: Certificates_Delete
    intent: Delete a certificate
    question: Can I remove an expired certificate I no longer use?
  phrasing_ops: 6
  slug: microsoft-azure-functions-certificates-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The DeletedWebApps API from Microsoft Azure Functions — 3 operation(s) for deletedwebapps.
  name: Microsoft Azure Functions DeletedWebApps API
  phrasing_intents:
  - id: DeletedWebApps_List
    intent: List deleted apps in a subscription
    question: Which web and function apps have been deleted across my whole subscription?
  - id: DeletedWebApps_ListByLocation
    intent: List deleted apps in one region
    question: What apps were deleted in a specific Azure region?
  - id: DeletedWebApps_GetDeletedWebAppByLocation
    intent: Get a deleted app by ID
    question: Can I look up the details of one deleted app using its numeric ID?
  phrasing_ops: 3
  slug: microsoft-azure-functions-deletedwebapps-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Diagnostics API from Microsoft Azure Functions — 22 operation(s) for diagnostics.
  name: Microsoft Azure Functions Diagnostics API
  phrasing_intents:
  - id: Diagnostics_ListHostingEnvironmentDetectorResponses
    intent: List detector responses for an App Service Environment
    question: What diagnostic detectors report on my App Service Environment?
  - id: Diagnostics_GetHostingEnvironmentDetectorResponse
    intent: Get one detector response for an App Service Environment
    question: Can I run a single detector against my App Service Environment for a specific time window?
  - id: Diagnostics_ListSiteDetectorResponses
    intent: List detector responses for a web app
    question: Which diagnostic detectors have results for my production web app?
  - id: Diagnostics_GetSiteDetectorResponse
    intent: Get one detector response for a web app
    question: What did a particular detector find on my app during an outage window?
  - id: Diagnostics_ListSiteDiagnosticCategories
    intent: List diagnostic categories for a web app
    question: What diagnostic categories are available for troubleshooting my site?
  - id: Diagnostics_GetSiteDiagnosticCategory
    intent: Get a diagnostic category for a web app
    question: How do I look up one diagnostic category on my production site?
  - id: Diagnostics_ListSiteAnalyses
    intent: List analyses in a site diagnostic category
    question: Which analyses can I run within a diagnostic category for my app?
  - id: Diagnostics_GetSiteAnalysis
    intent: Get a site analysis definition
    question: How do I look up the definition of one analysis for my site?
  phrasing_ops: 22
  slug: microsoft-azure-functions-diagnostics-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Global API from Microsoft Azure Functions — 3 operation(s) for global.
  name: Microsoft Azure Functions Global API
  phrasing_intents:
  - id: Global_GetDeletedWebApp
    intent: Get a deleted app in a subscription
    question: Can I look up the details of an app I deleted from my subscription?
  - id: Global_GetDeletedWebAppSnapshots
    intent: List restore snapshots of a deleted app
    question: Which snapshots are available to restore an app I deleted?
  - id: Global_GetSubscriptionOperationWithAsyncResponse
    intent: Check an async operation in a region
    question: How do I check the status of a long-running App Service operation in a region?
  phrasing_ops: 3
  slug: microsoft-azure-functions-global-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The KubeEnvironments API from Microsoft Azure Functions — 3 operation(s) for kubeenvironments.
  name: Microsoft Azure Functions KubeEnvironments API
  phrasing_intents:
  - id: KubeEnvironments_ListBySubscription
    intent: List Kubernetes Environments in a subscription
    question: What Kubernetes Environments exist across my whole subscription?
  - id: KubeEnvironments_ListByResourceGroup
    intent: List Kubernetes Environments in a resource group
    question: Which Kubernetes Environments are in one resource group?
  - id: KubeEnvironments_Get
    intent: Get a Kubernetes Environment
    question: How do I view the properties of one Kubernetes Environment?
  - id: KubeEnvironments_CreateOrUpdate
    intent: Create or replace a Kubernetes Environment
    question: How do I create a new Kubernetes Environment for App Service?
  - id: KubeEnvironments_Update
    intent: Patch an existing Kubernetes Environment
    question: Can I change settings on an existing Kubernetes Environment without recreating it?
  - id: KubeEnvironments_Delete
    intent: Delete a Kubernetes Environment
    question: How do I remove a Kubernetes Environment I no longer use?
  phrasing_ops: 6
  slug: microsoft-azure-functions-kubeenvironments-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Operations API from Microsoft Azure Functions — 1 operation(s) for operations.
  name: Microsoft Azure Functions Operations API
  phrasing_intents:
  - id: Provider_ListOperations
    intent: List operations of the Microsoft.Web resource provider
    question: What operations does the Microsoft.Web resource provider expose?
  phrasing_ops: 1
  slug: microsoft-azure-functions-operations-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Provider API from Microsoft Azure Functions — 7 operation(s) for provider.
  name: Microsoft Azure Functions Provider API
  phrasing_intents:
  - id: Provider_GetAvailableStacks
    intent: List available application frameworks
    question: Which application frameworks and versions does App Service support?
  - id: Provider_GetFunctionAppStacks
    intent: List Function app runtime stacks
    question: What runtimes and versions can I use for an Azure Functions app?
  - id: Provider_GetFunctionAppStacksForLocation
    intent: List Function app stacks in a region
    question: Which Function app runtimes are supported in a specific Azure region?
  - id: Provider_GetWebAppStacksForLocation
    intent: List Web app stacks in a region
    question: Which web app runtimes and versions are offered in a particular region?
  - id: Provider_ListOperations
    intent: List Microsoft.Web provider operations
    question: What operations does the Microsoft.Web resource provider expose?
  - id: Provider_GetWebAppStacks
    intent: List Web app runtime stacks
    question: What runtimes and versions can I pick for a web app across all regions?
  - id: Provider_GetAvailableStacksOnPrem
    intent: List application frameworks for my subscription
    question: Which application frameworks are available to my own subscription, including on-premises stacks?
  phrasing_ops: 7
  slug: microsoft-azure-functions-provider-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Providers API from Microsoft Azure Functions — 3 operation(s) for providers.
  name: Microsoft Azure Functions Providers API
  phrasing_intents:
  - id: GetPublishingUser
    intent: Get the publishing user
    question: What deployment credentials username is set for my account's FTP and local Git publishing?
  - id: UpdatePublishingUser
    intent: Update the publishing user
    question: How do I change my deployment username and password for FTP or local Git?
  - id: ListSourceControls
    intent: List available source control providers
    question: Which source control services can I connect my Azure websites and function apps to?
  - id: GetSourceControl
    intent: Get a source control token
    question: Is a token stored for a particular source control type on my account?
  - id: UpdateSourceControl
    intent: Update a source control token
    question: How do I refresh the token used for deployments from a source control type?
  phrasing_ops: 5
  slug: microsoft-azure-functions-providers-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Recommendations API from Microsoft Azure Functions — 15 operation(s) for recommendations.
  name: Microsoft Azure Functions Recommendations API
  phrasing_intents:
  - id: Recommendations_List
    intent: List recommendations for a subscription
    question: What App Service recommendations does Azure have for my whole subscription?
  - id: Recommendations_DisableRecommendationForSubscription
    intent: Turn off a recommendation rule subscription-wide
    question: How do I stop a specific recommendation rule from applying to my entire subscription?
  - id: Recommendations_ResetAllFilters
    intent: Reset recommendation opt-outs for a subscription
    question: How do I undo every recommendation opt-out across my subscription?
  - id: Recommendations_ListHistoryForHostingEnvironment
    intent: Get past recommendations for an ASE
    question: What recommendations did my App Service Environment receive in the past?
  - id: Recommendations_ListRecommendedRulesForHostingEnvironment
    intent: List current recommendations for an ASE
    question: Which recommendations currently apply to my App Service Environment?
  - id: Recommendations_GetRuleDetailsByHostingEnvironment
    intent: Get a recommendation rule's details for an ASE
    question: What does a particular recommendation rule say about my hosting environment?
  - id: Recommendations_DisableRecommendationForHostingEnvironment
    intent: Permanently disable one recommendation for an ASE
    question: How do I permanently silence a single recommendation rule on my App Service Environment?
  - id: Recommendations_DisableAllForHostingEnvironment
    intent: Disable all recommendations for an ASE
    question: How do I switch off every recommendation for one App Service Environment?
  phrasing_ops: 15
  slug: microsoft-azure-functions-recommendations-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ResourceHealthMetadata API from Microsoft Azure Functions — 6 operation(s) for resourcehealthmetadata.
  name: Microsoft Azure Functions ResourceHealthMetadata API
  phrasing_intents:
  - id: ResourceHealthMetadata_List
    intent: List resource health metadata for a subscription
    question: What resource health categories are set for all the sites in my subscription?
  - id: ResourceHealthMetadata_ListByResourceGroup
    intent: List resource health metadata in a resource group
    question: Which health metadata categories apply to the sites in one resource group?
  - id: ResourceHealthMetadata_ListBySite
    intent: List resource health metadata for an app
    question: What resource health metadata entries exist for my app as a collection?
  - id: ResourceHealthMetadata_GetBySite
    intent: Get the resource health category of an app
    question: Which resource health category does my app use?
  - id: ResourceHealthMetadata_ListBySiteSlot
    intent: List resource health metadata for a slot
    question: What resource health metadata entries exist for a deployment slot?
  - id: ResourceHealthMetadata_GetBySiteSlot
    intent: Get the resource health category of a slot
    question: Which resource health category does a deployment slot use?
  phrasing_ops: 6
  slug: microsoft-azure-functions-resourcehealthmetadata-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The SiteCertificates API from Microsoft Azure Functions — 4 operation(s) for sitecertificates.
  name: Microsoft Azure Functions SiteCertificates API
  phrasing_intents:
  - id: SiteCertificates_List
    intent: List certificates on an app
    question: Which certificates are attached to my app?
  - id: SiteCertificates_Get
    intent: Get a certificate on an app
    question: What are the details of one certificate on my app, like its thumbprint or expiry?
  - id: SiteCertificates_CreateOrUpdate
    intent: Create or replace a certificate on an app
    question: How do I upload a new certificate to my app?
  - id: SiteCertificates_Update
    intent: Patch an existing certificate on an app
    question: Can I change a few fields on a certificate already attached to my app?
  - id: SiteCertificates_Delete
    intent: Delete a certificate from an app
    question: How do I remove a certificate from my app?
  - id: SiteCertificates_ListSlot
    intent: List certificates on a deployment slot
    question: Which certificates are attached to a deployment slot of my app?
  - id: SiteCertificates_GetSlot
    intent: Get a certificate on a deployment slot
    question: What are the details of one certificate on a deployment slot?
  - id: SiteCertificates_CreateOrUpdateSlot
    intent: Create or replace a certificate on a slot
    question: How do I add a certificate to a staging deployment slot?
  phrasing_ops: 10
  slug: microsoft-azure-functions-sitecertificates-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Subscriptions API from Microsoft Azure Functions — 15 operation(s) for subscriptions.
  name: Microsoft Azure Functions Subscriptions API
  phrasing_intents:
  - id: ListAseRegions
    intent: List regions available for App Service Environments
    question: Which regions can I deploy an App Service Environment into?
  - id: ListBillingMeters
    intent: List App Service billing meters for a location
    question: What billing meters apply to App Service in a given region?
  - id: CheckNameAvailability
    intent: Check if an App Service resource name is free
    question: Is the name I want for my web app already taken?
  - id: ListCustomHostNameSites
    intent: List custom hostnames in a subscription
    question: Which custom hostnames are bound to sites in my subscription?
  - id: GetSubscriptionDeploymentLocations
    intent: List deployment locations including ministamps
    question: What geo regions and ministamps can my subscription deploy to?
  - id: ListGeoRegions
    intent: List geographical regions for App Service
    question: Which Azure regions support Linux workers for App Service?
  - id: ListSiteIdentifiersAssignedToHostName
    intent: List apps assigned to a hostname
    question: Which apps are assigned to a particular hostname?
  - id: RegionalCheckNameAvailability
    intent: Check name availability for DNL sites in a region
    question: Is a site name available with a domain name label in a specific region?
  phrasing_ops: 15
  slug: microsoft-azure-functions-subscriptions-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The WorkflowRunActions API from Microsoft Azure Functions — 10 operation(s) for workflowrunactions.
  name: Microsoft Azure Functions WorkflowRunActions API
  phrasing_intents:
  - id: WorkflowRunActions_List
    intent: List the actions of a workflow run
    question: Which actions executed in a particular Logic Apps workflow run?
  - id: WorkflowRunActions_Get
    intent: Get one action from a workflow run
    question: How do I see the status and outputs of one action in a workflow run?
  - id: WorkflowRunActions_ListExpressionTraces
    intent: List expression traces for a run action
    question: How can I see how expressions were evaluated in a workflow action?
  - id: WorkflowRunActionRepetitions_List
    intent: List repetitions of a looping workflow action
    question: How do I see every iteration of a for-each action in a workflow run?
  - id: WorkflowRunActionRepetitions_Get
    intent: Get one repetition of a workflow action
    question: What happened in one specific iteration of a looping action?
  - id: WorkflowRunActionRepetitions_ListExpressionTraces
    intent: List expression traces for an action repetition
    question: Can I see expression evaluation for one loop iteration rather than the whole action?
  - id: WorkflowRunActionRepetitionsRequestHistories_List
    intent: List request histories for an action repetition
    question: What HTTP requests did one loop iteration of an action send?
  - id: WorkflowRunActionRepetitionsRequestHistories_Get
    intent: Get one request history for an action repetition
    question: How do I see the exact request and response for one call made during a repetition?
  phrasing_ops: 10
  slug: microsoft-azure-functions-workflowrunactions-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Workflows API from Microsoft Azure Functions — 2 operation(s) for workflows.
  name: Microsoft Azure Functions Workflows API
  phrasing_intents:
  - id: Workflows_RegenerateAccessKey
    intent: Regenerate a workflow's callback URL access key
    question: How do I rotate the access key used in a Logic Apps workflow's request trigger callback URL?
  - id: Workflows_Validate
    intent: Validate a workflow definition
    question: Can I check whether a workflow definition is valid before saving it?
  phrasing_ops: 2
  slug: microsoft-azure-functions-workflows-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The WorkflowTriggerHistories API from Microsoft Azure Functions — 3 operation(s) for workflowtriggerhistories.
  name: Microsoft Azure Functions WorkflowTriggerHistories API
  phrasing_intents:
  - id: WorkflowTriggerHistories_List
    intent: List a workflow trigger's history
    question: When did a trigger in my Logic Apps Standard workflow last fire, and did it succeed?
  - id: WorkflowTriggerHistories_Get
    intent: Get one workflow trigger history entry
    question: What inputs and outputs did one specific trigger firing record?
  - id: WorkflowTriggerHistories_Resubmit
    intent: Resubmit a workflow run from trigger history
    question: Can I rerun a workflow using the same trigger event that fired before?
  phrasing_ops: 3
  slug: microsoft-azure-functions-workflowtriggerhistories-api
- baseURL: https://{functionapp}.azurewebsites.net
  baseurl_source: declared
  description: The Static Sites API from Microsoft Azure Functions — 51 operation(s) for static sites.
  name: Microsoft Azure Functions Static Sites API
  phrasing_intents:
  - id: StaticSites_PreviewWorkflow
    intent: Preview the generated workflow file for a static site
    question: Can I see what build workflow file Azure would generate for my static site before I create it?
  - id: StaticSites_List
    intent: List all static sites in a subscription
    question: Which static web apps exist across my whole Azure subscription?
  - id: StaticSites_GetStaticSitesByResourceGroup
    intent: List static sites in a resource group
    question: What static web apps are deployed in one particular resource group?
  - id: StaticSites_GetStaticSite
    intent: Get the details of a static site
    question: What are the settings, SKU and default hostname of one of my static web apps?
  - id: StaticSites_CreateOrUpdateStaticSite
    intent: Create or replace a static site
    question: How do I create a new Azure Static Web App in an existing resource group?
  - id: StaticSites_UpdateStaticSite
    intent: Patch properties of an existing static site
    question: Can I change just a few properties of a static web app without resending the whole definition?
  - id: StaticSites_DeleteStaticSite
    intent: Delete a static site
    question: Can I permanently remove a static web app I no longer need?
  - id: StaticSites_ListBasicAuth
    intent: List basic auth settings for a static site
    question: Is password protection turned on for my static web app?
  phrasing_ops: 75
  slug: microsoft-azure-functions-static-sites-api
- baseURL: https://{functionapp}.azurewebsites.net
  baseurl_source: declared
  description: The Web Apps API from Microsoft Azure Functions — 300 operation(s) for web apps.
  name: Microsoft Azure Functions Web Apps API
  phrasing_intents:
  - id: WebApps_List
    intent: List every app in my subscription
    question: Which App Service and Function apps exist across my whole Azure subscription?
  - id: WebApps_ListByResourceGroup
    intent: List the apps in a resource group
    question: What web and function apps live in a particular resource group?
  - id: WebApps_Get
    intent: Get the details of an app
    question: What are the current properties and state of one of my Azure web apps?
  - id: WebApps_CreateOrUpdate
    intent: Create or replace an app
    question: How do I create a new function app or web app in an existing resource group?
  - id: WebApps_Update
    intent: Patch an existing app's properties
    question: Can I change only a few properties of an existing web app without resending the whole definition?
  - id: WebApps_Delete
    intent: Delete an app
    question: What happens to the App Service plan when I delete the last app in it?
  - id: WebApps_AnalyzeCustomHostname
    intent: Check if a custom hostname can be added
    question: Will my custom domain work with my production web app before I bind it?
  - id: WebApps_ApplySlotConfigToProduction
    intent: Apply a slot's config to production before swap
    question: Can I stage a slot's configuration onto production before doing a swap?
  phrasing_ops: 416
  slug: microsoft-azure-functions-web-apps-api
- baseURL: https://{functionapp}.azurewebsites.net
  baseurl_source: declared
  description: The Workflow Runs API from Microsoft Azure Functions — 3 operation(s) for workflow runs.
  name: Microsoft Azure Functions Workflow Runs API
  phrasing_intents:
  - id: WorkflowRuns_List
    intent: List the runs of a workflow
    question: How do I see the run history of a Logic Apps Standard workflow?
  - id: WorkflowRuns_Get
    intent: Get a workflow run
    question: What is the status of one specific workflow run?
  - id: WorkflowRuns_Cancel
    intent: Cancel a running workflow run
    question: How do I stop a workflow run that is stuck or running too long?
  phrasing_ops: 3
  slug: microsoft-azure-functions-workflow-runs-api
- baseURL: https://{functionapp}.azurewebsites.net
  baseurl_source: declared
  description: The Workflow Triggers API from Microsoft Azure Functions — 5 operation(s) for workflow triggers.
  name: Microsoft Azure Functions Workflow Triggers API
  phrasing_intents:
  - id: WorkflowTriggers_List
    intent: List the triggers of a workflow
    question: What triggers are defined on a Logic Apps Standard workflow?
  - id: WorkflowTriggers_Get
    intent: Get a workflow trigger
    question: How do I look up the state of one trigger on a workflow?
  - id: WorkflowTriggers_ListCallbackUrl
    intent: Get the callback URL for a workflow trigger
    question: Where do I find the URL to call a request-based workflow trigger?
  - id: WorkflowTriggers_Run
    intent: Run a workflow trigger manually
    question: Can I fire a workflow trigger manually instead of waiting for its schedule?
  - id: WorkflowTriggers_GetSchemaJson
    intent: Get a workflow trigger's JSON schema
    question: What payload shape does a workflow trigger expect?
  phrasing_ops: 5
  slug: microsoft-azure-functions-workflow-triggers-api
- baseURL: https://{functionapp}.azurewebsites.net
  baseurl_source: declared
  description: The Workflow Versions API from Microsoft Azure Functions — 2 operation(s) for workflow versions.
  name: Microsoft Azure Functions Workflow Versions API
  phrasing_intents:
  - id: WorkflowVersions_List
    intent: List versions of a workflow
    question: What versions of my workflow have been saved?
  - id: WorkflowVersions_Get
    intent: Get a specific workflow version
    question: What did a particular earlier version of my workflow look like?
  phrasing_ops: 2
  slug: microsoft-azure-functions-workflow-versions-api
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
artifact_total: 188
collections:
- collection_type: postman
  name: WebApps API Client
  slug: postman-azure-functions-management-api
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
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-functions/plans/microsoft-azure-functions-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-functions-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-functions/rate-limits/microsoft-azure-functions-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-functions-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-functions/finops/microsoft-azure-functions-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-functions-finops.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-functions/capabilities/microsoft-azure-functions-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-azure-functions-capability-edges.yml
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/azure-functions/refs/heads/main/rules/azure-functions-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/azure-functions/refs/heads/main/vocabulary/azure-functions-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/azure-functions/refs/heads/main/json-ld/azure-functions-context.jsonld
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
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
  href: https://artifacts.apis.io/microsoft-azure-functions/agentic-access/microsoft-azure-functions-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-functions-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-functions/security/microsoft-azure-functions-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-functions-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-functions/authentication/microsoft-azure-functions-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-functions-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-functions/scopes/microsoft-azure-functions-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-functions-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-azure-functions/overview
- group: design
  href: https://artifacts.apis.io/microsoft-azure-functions/arazzo/microsoft-azure-functions-create-function-and-verify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-functions-create-function-and-verify-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-functions/arazzo/microsoft-azure-functions-deploy-function-and-sync-triggers-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-functions-deploy-function-and-sync-triggers-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-functions/arazzo/microsoft-azure-functions-inspect-app-and-issue-admin-token-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-functions-inspect-app-and-issue-admin-token-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-functions/arazzo/microsoft-azure-functions-provision-function-app-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-functions-provision-function-app-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-functions/arazzo/microsoft-azure-functions-provision-staging-slot-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-functions-provision-staging-slot-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-functions/arazzo/microsoft-azure-functions-record-deployment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-functions-record-deployment-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-functions/arazzo/microsoft-azure-functions-rotate-function-key-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-functions-rotate-function-key-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-functions/arazzo/microsoft-azure-functions-rotate-host-key-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-functions-rotate-host-key-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-functions/arazzo/microsoft-azure-functions-swap-slot-to-production-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-functions-swap-slot-to-production-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-functions/arazzo/microsoft-azure-functions-update-app-settings-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-functions-update-app-settings-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-functions/arazzo/microsoft-azure-functions-update-site-config-workflow.yml
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
- has_sources: true
  method: derived
  name: Microsoft Azure Functions Finops
  primary_unit: ''
  service_category: ''
  slug: microsoft-azure-functions-finops
  template: true
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
overview: 'Microsoft Azure Functions publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including AppServiceEnvironments API, AppServicePlans API, Certificates API, and 20 more. Tagged areas include Microsoft Azure, Cloud, Compute, Event-Driven, and Microsoft.


  The Microsoft Azure Functions catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Microsoft Azure Functions'' developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, engineering blog, and 46 more developer resources.'
plans:
- name: Microsoft Azure Functions Plans Pricing
  plan_count: 6
  slug: microsoft-azure-functions-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Microsoft Azure Functions Rate Limits
  slug: microsoft-azure-functions-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 19
  extends: []
  name: Microsoft Azure Functions — azure functions rules
  rule_count: 19
  severity_counts:
    error: 14
    hint: 0
    info: 3
    warn: 2
  slug: azure-functions-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Microsoft Azure Functions — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-azure-functions-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 44
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
  band: exemplar
  composite: 68.5
  coverage:
    artifact_dirs: 24
    catalog_earned: 72.0
    catalog_earned_first_party: 12.0
    catalog_gap: 43.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 27.3
    contract_quality: 50.2
    developer_ergonomics: 82.1
    discoverability: 71.7
    operational_transparency: 52.6
  open_source:
    applies: true
    score: 100.0
  previous_composite: 68.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/microsoft-azure-functions/microsoft-azure-functions-2026-06-20T185418.png
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
- Microsoft Azure
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
website: https://www.microsoft.com/
---
