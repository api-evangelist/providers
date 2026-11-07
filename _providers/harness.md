---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 63.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1382
  human_in_the_loop: 70
  name: Harness Agentic Access
  operation_count: 2889
  slug: harness-agentic-access
  summary_line: 2889 operations · 1382 acting · 70 human-in-the-loop
api_count: 1
apis:
- description: The Harness CI module helps build faster with features including code building, testing, dependency management, artifact uploads, and build monitoring with AI-powered Test Intelligence.
  name: Harness Continuous Integration API
  slug: ci-api
- description: The Harness CD and GitOps module automates all steps necessary to get changes into production with APIs for pipelines, execution, input sets, triggers, and approvals supporting multi-cloud deployments
  name: Harness Continuous Delivery and GitOps API
  slug: cd-api
- description: APIs to create and manage feature flags, targets, target groups, and tags for feature release management, performance monitoring, and A/B testing.
  name: Harness Feature Management and Experimentation API
  slug: feature-flags-api
- description: Cloud cost management APIs for cost recommendations, AutoStopping rules, commitment orchestration, cost categories, anomaly detection, asset governance, and BI dashboards.
  name: Harness Cloud Cost Management API
  slug: ccm-api
- description: APIs for chaos engineering, load testing, and disaster recovery testing including chaos experiments, probes, actions, faults, and resilience scoring.
  name: Harness Chaos Engineering API
  slug: chaos-api
- description: APIs for security vulnerability detection with over 40 scanner integrations for running scans, viewing results, and enforcing security policies across the software delivery lifecycle.
  name: Harness Security Testing Orchestration API
  slug: sto-api
- description: Backstage-powered Internal Developer Portal APIs for software catalog management, self-service workflows, scorecards, and developer experience.
  name: Harness Internal Developer Portal API
  slug: idp-api
- description: Source control management APIs for repositories, collaboration tools, pull requests, and pipeline integration.
  name: Harness Code Repository API
  slug: code-repo-api
- description: APIs for managing service level objectives, monitored services, and service dashboards for balancing feature velocity with reliability.
  name: Harness Service Reliability Management API
  slug: srm-api
- description: APIs for defining, deploying, and managing infrastructure across environments with Terraform and IaC tool integration.
  name: Harness Infrastructure as Code Management API
  slug: iacm-api
- description: APIs for SBOM generation, artifact integrity verification, and policy enforcement for software supply chain security and compliance.
  name: Harness Supply Chain Security API
  slug: ssca-api
- description: APIs for accessing engineering metrics and analytics data to improve engineering productivity, efficiency, and alignment.
  name: Harness Software Engineering Insights API
  slug: sei-api
- baseURL: https://app.harness.io/gateway
  baseurl_source: declared
  description: Manage organizations
  name: Harness Organizations API
  phrasing_intents:
  - id: listOrganizations
    intent: List organizations in the account
    question: Which organizations exist in my Harness account?
  phrasing_ops: 1
  slug: harness-organizations-api
- baseURL: https://app.harness.io/gateway
  baseurl_source: declared
  description: Execute pipelines
  name: Harness Pipeline Execution API
  phrasing_intents:
  - id: execute-pipeline
    intent: Run a pipeline with runtime inputs
    question: How do I trigger a pipeline run from a script?
  - id: rerun-pipeline
    intent: Rerun a previous pipeline execution
    question: Can I rerun a past pipeline execution from scratch?
  - id: retry-pipeline-with-inputset-pipeline-yaml
    intent: Retry a failed pipeline execution
    question: Can I retry only the failed stages of a pipeline run?
  - id: get-stages-execution-list
    intent: List a pipeline's stages and dependencies
    question: Which stages does a pipeline have, and how do they depend on each other?
  - id: rerun-stages-execution-of-pipeline
    intent: Rerun selected stages of a past execution
    question: Can I rerun just a couple of stages from an earlier pipeline execution?
  - id: runDynamicExecutionWithInputYaml
    intent: Run a pipeline with a dynamic YAML definition
    question: Can I execute a pipeline using YAML I generate at runtime?
  - id: execute-stages-with-input-yaml
    intent: Run only selected stages of a pipeline
    question: Can I start a new run that executes only certain stages of a pipeline?
  - id: executePipeline
    intent: Run a pipeline with input sets (legacy endpoint)
    question: Can I run a pipeline by referencing saved input sets?
  phrasing_ops: 8
  slug: harness-pipeline-execution-api
- baseURL: https://app.harness.io/gateway
  baseurl_source: declared
  description: Manage pipelines
  name: Harness Pipelines API
  phrasing_intents:
  - id: list-pipelines
    intent: List pipelines in a project
    question: What pipelines exist in my Harness project?
  - id: create-pipeline
    intent: Create a pipeline
    question: How do I create a new pipeline from YAML?
  - id: get-pipeline
    intent: Get a pipeline
    question: What does a specific pipeline's YAML look like?
  - id: update-pipeline
    intent: Replace a pipeline's full definition
    question: How do I overwrite a pipeline with a completely new YAML?
  - id: delete-pipeline
    intent: Delete a pipeline
    question: How do I delete a pipeline I no longer need?
  - id: patch-pipeline
    intent: Partially update a pipeline
    question: Can I change just a pipeline's name or tags without resending all the YAML?
  - id: start-pipeline-validation-event
    intent: Start validating a pipeline
    question: How do I kick off a validation check for a pipeline?
  - id: get-pipeline-validate-result
    intent: Get the result of a pipeline validation
    question: Did my pipeline validation pass?
  phrasing_ops: 13
  slug: harness-pipelines-api
- baseURL: https://app.harness.io/gateway
  baseurl_source: declared
  description: Manage projects
  name: Harness Projects API
  phrasing_intents:
  - id: AgentProjectService_List
    intent: List Argo CD projects on a GitOps agent
    question: Which Argo CD projects does a GitOps agent manage?
  - id: AgentProjectService_Create
    intent: Create an Argo CD project on a GitOps agent
    question: How do I create a new Argo CD project through a Harness GitOps agent?
  - id: AgentProjectService_Get
    intent: Get an Argo CD project by name
    question: How do I fetch one Argo project's definition from a GitOps agent?
  - id: AgentProjectService_Delete
    intent: Delete an Argo CD project
    question: How do I delete an Argo CD project from a GitOps agent?
  - id: AgentProjectService_Update
    intent: Update an Argo CD project
    question: How do I change an existing Argo project's allowed repos or destinations?
  - id: listProjects
    intent: List Harness projects in an account
    question: Which Harness projects exist in my account?
  phrasing_ops: 6
  slug: harness-projects-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains the APIs to perform access control checks
  name: Harness Access Control List API
  phrasing_intents:
  - id: getAccessControlList
    intent: Check a principal's permissions on resources
    question: Does a given user have permission to run a pipeline or edit a resource?
  - id: getAclCount
    intent: Count access control entries in a scope
    question: How many ACL entries exist for my account or project?
  phrasing_ops: 2
  slug: harness-access-control-list-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Account Banners.
  name: Harness Account Banner API
  phrasing_intents:
  - id: get-account-scoped-banners
    intent: List account banners
    question: What announcement banners have been set up for our Harness account?
  - id: create-account-scoped-banners
    intent: Create an account banner
    question: How do I post a banner message to everyone in our account?
  - id: validate-account-scoped-banner-identifier
    intent: Check a banner identifier is available
    question: Is a banner identifier already taken in my account?
  - id: banners-allowed
    intent: Check if more banners can be enabled
    question: Have we already hit the five enabled banner limit?
  - id: update-account-scoped-banner
    intent: Update an account banner
    question: How do I change the message on an existing banner?
  - id: delete-account-scoped-banner
    intent: Delete an account banner
    question: How do I remove a banner from the account for good?
  - id: get-account-scoped-active-banners
    intent: List currently active banners
    question: Which banners are users seeing right now?
  phrasing_ops: 7
  slug: harness-account-banner-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for account-scoped Certificates
  name: Harness Account Certificate API
  phrasing_intents:
  - id: get-account-scoped-certificate
    intent: Get an account-level certificate
    question: Can I view the details of a certificate stored at the account level?
  - id: update-account-scoped-certificate
    intent: Update an account-level certificate
    question: How do I replace the value of a certificate that's about to expire?
  - id: delete-account-scoped-certificate
    intent: Delete an account-level certificate
    question: Can I delete a certificate from the account even if something references it?
  - id: validate-account-scoped-certificate-identifier
    intent: Check a certificate identifier is available
    question: Is a certificate identifier already taken in my account?
  - id: get-account-scoped-certificates
    intent: List account-level certificates
    question: What certificates are stored in my Harness account?
  - id: create-account-scoped-certificates
    intent: Add a certificate at the account level
    question: How do I upload a certificate for use across the whole account?
  phrasing_ops: 6
  slug: harness-account-certificate-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Account-scoped Connectors.
  name: Harness Account Connector API
  phrasing_intents:
  - id: create-account-scoped-connector
    intent: Create an account-level connector
    question: How do I add a new connector to my account?
  - id: get-account-scoped-connectors
    intent: List account-level connectors
    question: Which connectors are set up at the account level?
  - id: get-account-scoped-connector
    intent: Get an account-level connector
    question: What is configured on a particular account connector?
  - id: update-account-scoped-connector
    intent: Update an account-level connector
    question: How do I change the settings of an existing account connector?
  - id: delete-account-scoped-connector
    intent: Delete an account-level connector
    question: How do I remove a connector from my account?
  - id: test-account-scoped-connector
    intent: Test an account connector's connection
    question: Is my account connector able to reach its target?
  phrasing_ops: 6
  slug: harness-account-connector-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Account Environments API from Harness — 2 operation(s) for account environments.
  name: Harness Account Environments API
  phrasing_intents:
  - id: create-account-scoped-environment
    intent: Create an account-level environment
    question: How do I create an environment shared across the whole account?
  - id: get-account-scoped-environments
    intent: List account-level environments
    question: Which account-level deployment environments can I see?
  - id: get-account-scoped-environment
    intent: Get an account-level environment
    question: What is configured on a specific account-level environment?
  - id: update-account-scoped-environment
    intent: Update an account-level environment
    question: How do I change the type or color of an account environment?
  - id: delete-account-scoped-environment
    intent: Delete an account-level environment
    question: How do I delete an environment at the account level?
  phrasing_ops: 5
  slug: harness-account-environments-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for account-scoped Favorites.
  name: Harness Account Favorites API
  phrasing_intents:
  - id: create-account-favorite
    intent: Mark a resource as a user's favorite
    question: How do I star a pipeline or project as a favorite for a user?
  - id: get-account-favorites
    intent: List a user's favorite resources
    question: Which resources has a user marked as favorites?
  - id: delete-account-favorite
    intent: Remove a resource from a user's favorites
    question: How do I unfavorite a resource for a user?
  phrasing_ops: 3
  slug: harness-account-favorites-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Account Infrastructures API from Harness — 2 operation(s) for account infrastructures.
  name: Harness Account Infrastructures API
  phrasing_intents:
  - id: create-account-scoped-infrastructure
    intent: Create an infrastructure in an account environment
    question: How do I add an infrastructure definition to an account-level environment?
  - id: get-account-scoped-infrastructures
    intent: List infrastructures in an account environment
    question: Which infrastructure definitions exist in an account-level environment?
  - id: get-account-scoped-infrastructure
    intent: Get an account-level infrastructure definition
    question: Can I see the YAML of one infrastructure in an account-level environment?
  - id: update-account-scoped-infrastructure
    intent: Update an account-level infrastructure definition
    question: Can I change the YAML of an account-level infrastructure?
  - id: delete-account-scoped-infrastructure
    intent: Delete an account-level infrastructure
    question: How do I delete an infrastructure from an account environment?
  phrasing_ops: 5
  slug: harness-account-infrastructures-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Account License Type API from Harness — 1 operation(s) for account license type.
  name: Harness Account License Type API
  phrasing_intents:
  - id: get-license-type
    intent: Get an account's license type
    question: What kind of Harness license does this account have?
  phrasing_ops: 1
  slug: harness-account-license-type-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Account Licensed Modules.
  name: Harness Account Licensed Modules API
  phrasing_intents:
  - id: get-account-licensed-modules
    intent: List the modules my account is licensed for
    question: Which modules is my account licensed to use?
  phrasing_ops: 1
  slug: harness-account-licensed-modules-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Rancher infra entities for account level.
  name: Harness Account Rancher Infrastructure API
  phrasing_intents:
  - id: list-account-scoped-rancher-clusters-using-connector
    intent: List Rancher clusters via an account connector
    question: Which Rancher clusters can my account-level Rancher connector see?
  - id: list-account-scoped-rancher-clusters-using-env-and-infra
    intent: List Rancher clusters for an environment and infra
    question: Which Rancher clusters are available to a given environment and infrastructure definition?
  phrasing_ops: 2
  slug: harness-account-rancher-infrastructure-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Account-scoped Resource Groups.
  name: Harness Account Resource Groups API
  phrasing_intents:
  - id: list-resource-groups-acc
    intent: List account-level resource groups
    question: Which resource groups are defined at my Harness account level?
  - id: create-resource-group-acc
    intent: Create an account-level resource group
    question: How do I create a custom resource group for access control at the account level?
  - id: get-resource-group-acc
    intent: Get an account-level resource group
    question: Which resources does a particular account resource group cover?
  - id: update-resource-group-acc
    intent: Update an account-level resource group
    question: How do I change the resources included in an account resource group?
  - id: delete-resource-group-acc
    intent: Delete an account-level resource group
    question: How do I delete a custom resource group at the account level?
  phrasing_ops: 5
  slug: harness-account-resource-groups-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Account-scoped Role Assignments.
  name: Harness Account Role Assignments API
  phrasing_intents:
  - id: get-account-scoped-role-assignments
    intent: List account-level role assignments
    question: Who has which roles at the account level in Harness?
  - id: create-account-scoped-role-assignments
    intent: Assign a role to a principal at account level
    question: How do I grant a user a role across the whole account?
  - id: get-account-scoped-role-assignment
    intent: Get an account-level role assignment
    question: Can I see which principal and resource group a specific role assignment covers?
  - id: delete-account-scoped-role-assignment
    intent: Revoke an account-level role assignment
    question: How do I take away a role someone was given at the account level?
  - id: get-role-assignments-count
    intent: Count the role assignments in an account
    question: How many role assignments does my account have in total?
  phrasing_ops: 5
  slug: harness-account-role-assignments-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Account-scoped Roles.
  name: Harness Account Roles API
  phrasing_intents:
  - id: list-roles-acc
    intent: List account-level roles
    question: What roles are defined at the account level in Harness?
  - id: create-role-acc
    intent: Create a custom account role
    question: How do I create a custom role with only certain permissions for my whole account?
  - id: get-role-acc
    intent: Get an account role
    question: Which permissions does a particular account role grant?
  - id: update-role-acc
    intent: Update an account role
    question: Can I add permissions to an existing account role?
  - id: delete-role-acc
    intent: Delete a custom account role
    question: Can I delete a custom role I no longer need?
  - id: get-roles-count
    intent: Count the roles in an account
    question: How many roles exist in my Harness account?
  phrasing_ops: 6
  slug: harness-account-roles-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for account-scoped secrets.
  name: Harness Account Secret API
  phrasing_intents:
  - id: create-account-scoped-secret
    intent: Create an account-level secret
    question: How do I store a new text or file secret at the account scope?
  - id: get-account-scoped-secrets
    intent: List account-level secrets
    question: Which secrets are stored at the account level in Harness?
  - id: validate-account-secret-ref
    intent: Check a secret manager path can be referenced
    question: Can I confirm a secret exists at a secret manager path before referencing it?
  - id: get-account-scoped-secret
    intent: Get an account-level secret
    question: What type and secret manager does an account secret use?
  - id: delete-account-scoped-secret
    intent: Delete an account-level secret
    question: How do I permanently remove a secret stored at the account level?
  - id: update-account-scoped-secret
    intent: Update an account-level secret
    question: How do I rotate the value of an existing account secret?
  phrasing_ops: 6
  slug: harness-account-secret-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for account-scoped services.
  name: Harness Account Services API
  phrasing_intents:
  - id: get-account-scoped-service
    intent: Get an account-level service
    question: Can I look up one account-scoped service by its identifier?
  - id: update-account-scoped-service
    intent: Update an account-level service
    question: How do I change the name or tags on an account-scoped service?
  - id: delete-account-scoped-service
    intent: Delete an account-level service
    question: Can I force-delete an account-level service?
  - id: get-account-scoped-services
    intent: List account-level services
    question: Which services are defined at my account level?
  - id: create-account-scoped-service
    intent: Create an account-level service
    question: How do I create a service that lives at the account level?
  - id: get-account-scoped-primary-manifests
    intent: List primary manifest options for a service
    question: Which manifests can be selected as primary for an account-level service?
  - id: post-account-scoped-primary-manifests
    intent: List primary manifests of a Git-stored service
    question: Can I list eligible primary manifests for a service whose YAML lives on a Git branch?
  phrasing_ops: 7
  slug: harness-account-services-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Account-scoped Templates.
  name: Harness Account Template API
  phrasing_intents:
  - id: create-templates-acc
    intent: Create an account-level template
    question: How do I publish a reusable pipeline or step template for the whole account?
  - id: get-templates-list-acc
    intent: List account-level templates
    question: What templates are defined at the account level?
  - id: update-git-metadata-details
    intent: Update Git details for a template's versions
    question: Can I update the Git metadata for all versions of a template at once?
  - id: get-template-stable-acc
    intent: Get the stable version of a template
    question: Which version of an account template is currently marked stable?
  - id: get-template-acc
    intent: Get a specific template version
    question: How do I retrieve a particular version label of an account template?
  - id: update-template-acc
    intent: Update a template version
    question: Can I edit the YAML of one existing template version?
  - id: delete-template-acc
    intent: Delete a template version
    question: How do I delete one version of an account template?
  - id: update-template-stable-acc
    intent: Mark a template version as stable
    question: How do I promote a template version to be the stable one?
  phrasing_ops: 10
  slug: harness-account-template-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Account Webhooks.
  name: Harness Account Webhooks API
  phrasing_intents:
  - id: list-account-webhooks
    intent: List account-level webhooks
    question: Which webhooks are configured at my account level?
  - id: create-account-webhooks
    intent: Create an account-level webhook
    question: How do I set up a webhook that applies across my whole account?
  - id: get-account-webhook
    intent: Get an account-level webhook
    question: How is one of my account webhooks configured?
  - id: update-account-webhook
    intent: Update an account-level webhook
    question: Can I disable an account webhook without deleting it?
  - id: delete-account-webhook
    intent: Delete an account-level webhook
    question: How do I delete a webhook defined at account level?
  phrasing_ops: 5
  slug: harness-account-webhooks-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The accountConfigs API from Harness — 1 operation(s) for accountconfigs.
  name: Harness Account Configs API
  phrasing_intents:
  - id: updatePipelineConfig
    intent: Update an account's pipeline config
    question: Can I change the pipeline configuration for my whole account?
  phrasing_ops: 1
  slug: harness-accountconfigs-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to accounts as defined in Harness
  name: Harness Accounts API
  phrasing_intents:
  - id: getAccountNG
    intent: Get a Harness account
    question: What company name, edition and status does my Harness account have?
  - id: enabledFeatureFlags
    intent: List feature flags enabled on an account
    question: Which feature flags are turned on for my Harness account?
  - id: isImmutableDelegateEnabled
    intent: Check if immutable delegates are enabled
    question: Does my account use immutable delegates?
  - id: licenseUpdateFromUING
    intent: Update an account's license status and type
    question: How do I change an account's license type and status?
  - id: updateAccountNameNG
    intent: Rename a Harness account
    question: Can I change the display name of my Harness account?
  - id: updateAccountDefaultExperienceNG
    intent: Change an account's default experience
    question: How do I switch the default experience users land in for my account?
  - id: Accounts#DeleteAccountData
    intent: Delete all security testing data for an account
    question: Can I wipe all Security Testing Orchestration data for an account?
  phrasing_ops: 7
  slug: harness-accounts-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Action Templates API from Harness — 5 operation(s) for action templates.
  name: Harness Action Templates API
  phrasing_intents:
  - id: listActionTemplate
    intent: List chaos action templates in a hub
    question: Which chaos action templates are available in my chaos hub?
  - id: createActionTemplate
    intent: Create a chaos action template
    question: How do I add a new reusable action template to a chaos hub?
  - id: getActionTemplate
    intent: Get a chaos action template
    question: What does a specific chaos action template do?
  - id: updateActionTemplate
    intent: Update a chaos action template
    question: How do I change the configuration of an existing chaos action template?
  - id: deleteActionTemplate
    intent: Delete a chaos action template
    question: How do I remove an action template from a chaos hub?
  - id: getActionTemplateRevisionDifference
    intent: Compare two action template revisions
    question: What changed between two revisions of a chaos action template?
  - id: listActionTemplateRevisions
    intent: List revisions of an action template
    question: How many revisions does a chaos action template have?
  - id: listVariablesInActionTemplate
    intent: List inputs of an action template revision
    question: What inputs does a chaos action template expect?
  phrasing_ops: 8
  slug: harness-action-templates-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Actions API from Harness — 5 operation(s) for actions.
  name: Harness Actions API
  phrasing_intents:
  - id: listActions
    intent: List chaos actions
    question: What chaos actions are available in my project?
  - id: createAction
    intent: Create a chaos action
    question: How do I define a new custom action for chaos experiments?
  - id: importAction
    intent: Import a chaos action from a hub
    question: Can I import an existing action from a chaos hub into my project?
  - id: getActionManifest
    intent: Get a chaos action's manifest
    question: Can I download the manifest behind a chaos action?
  - id: getAction
    intent: Get a chaos action
    question: What are the details and inputs of a specific chaos action?
  - id: updateAction
    intent: Update a chaos action
    question: Can I change the inputs or run properties of an existing action?
  - id: deleteAction
    intent: Delete a chaos action
    question: Can I delete a chaos action we don't use anymore?
  - id: listActionMetadata
    intent: List metadata for chaos actions
    question: Can I get lightweight metadata for a set of actions by their identifiers?
  phrasing_ops: 8
  slug: harness-actions-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Activities Service handles the API for workspace activities
  name: Harness Activities API
  phrasing_intents:
  - id: activities#list-activities
    intent: List IaCM activities in a project
    question: What infrastructure activities have run in my IaCM project recently?
  - id: activities#list-activity-resource-changes
    intent: List resource changes from an activity
    question: Which infrastructure resources did a particular activity change?
  phrasing_ops: 2
  slug: harness-activities-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Contains APIs related to Agent mTLS Endpoint management.
  name: Harness Agent mTLS Endpoint Management API
  phrasing_intents:
  - id: getAgentMtlsEndpointForAccount
    intent: Get the account's agent mTLS endpoint
    question: What mTLS endpoint do my delegates use to connect to Harness?
  - id: updateAgentMtlsEndpointForAccount
    intent: Replace the agent mTLS endpoint configuration
    question: How do I replace the whole agent mTLS endpoint config with new CA certificates and mode?
  - id: createAgentMtlsEndpointForAccount
    intent: Create an agent mTLS endpoint
    question: How do I set up mutual TLS for delegate connections to my Harness account?
  - id: deleteAgentMtlsEndpointForAccount
    intent: Remove the agent mTLS endpoint
    question: How do I turn off mutual TLS for delegates by deleting the endpoint?
  - id: patchAgentMtlsEndpointForAccount
    intent: Change selected mTLS endpoint settings
    question: Can I switch just the enforcement mode of my mTLS endpoint without resending the certificates?
  - id: checkAgentMtlsEndpointDomainPrefixAvailability
    intent: Check if an mTLS domain prefix is available
    question: Is the domain prefix I want for my agent mTLS endpoint already taken?
  phrasing_ops: 6
  slug: harness-agent-mtls-endpoint-management-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Agents API from Harness — 20 operation(s) for agents.
  name: Harness Agents API
  phrasing_intents:
  - id: AgentServiceForServer_List
    intent: List GitOps agents
    question: Which GitOps agents are registered in my Harness project?
  - id: AgentServiceForServer_Create
    intent: Register a new GitOps agent
    question: How do I register a new GitOps agent in Harness?
  - id: AgentServiceForServer_ListNamespaces
    intent: List namespaces GitOps agents run in
    question: Which Kubernetes namespaces are my GitOps agents installed in?
  - id: AgentServiceForServer_Search
    intent: Search GitOps agents with filters
    question: Can I search GitOps agents by a search term and filter by mapped projects?
  - id: AgentServiceForServer_ListTags
    intent: List tags used on GitOps agents
    question: What tags have been applied to my GitOps agents?
  - id: AgentServiceForServer_ListVersions
    intent: List versions of GitOps agents
    question: Which versions are my GitOps agents running?
  - id: AgentServiceForServer_Update
    intent: Update a GitOps agent's details
    question: Can I change the tags or metadata on an existing GitOps agent?
  - id: AgentServiceForServer_GetDeployYaml
    intent: Download an agent's install manifest YAML
    question: Where do I get the Kubernetes YAML manifest to install a GitOps agent?
  phrasing_ops: 25
  slug: harness-agents-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Aggregation Rules
  name: Harness Aggregation Rules API
  phrasing_intents:
  - id: get-aggregation-rules
    intent: List aggregation rules
    question: Which aggregation rules are defined in my developer portal?
  - id: create-aggregation-rule
    intent: Create an aggregation rule
    question: How do I create a rule that rolls up values across catalog entities?
  - id: get-aggregation-rule
    intent: Get an aggregation rule
    question: Where can I see how one aggregation rule is configured?
  - id: update-aggregation-rule
    intent: Update an aggregation rule
    question: Can I change the definition of an existing aggregation rule?
  - id: delete-aggregation-rule
    intent: Delete an aggregation rule
    question: How do I delete an aggregation rule?
  - id: review-aggregation-rules
    intent: Preview which entities will hold aggregated values
    question: Before saving a rule, which entities would its aggregated values land on?
  - id: trigger-aggregation-rule-computation
    intent: Run an aggregation rule's computation now
    question: How do I recompute an aggregation rule immediately?
  phrasing_ops: 7
  slug: harness-aggregationrules-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: AIDA API's for Harness OPA
  name: Harness Aida API
  phrasing_intents:
  - id: aida#accept
    intent: Record acceptance of an AI-generated policy
    question: How do I log that a user accepted the AI's suggested policy?
  - id: aida#analyze
    intent: Explain a Rego policy in plain language
    question: Can AI explain what a Rego policy does?
  - id: aida#generate
    intent: Generate a policy from a text description
    question: Can AI write a governance policy from a plain-language description?
  phrasing_ops: 3
  slug: harness-aida-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Backstage Allow List
  name: Harness Allow List API
  phrasing_intents:
  - id: get-allow-list
    intent: Get the backend URL allow list
    question: Which backend URLs are on my developer portal allow list?
  - id: save-allow-list
    intent: Save the backend URL allow list
    question: How do I add hosts to the backend URL allow list?
  phrasing_ops: 2
  slug: harness-allowlist-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Analyze Account Access Policy API from Harness — 1 operation(s) for analyze account access policy.
  name: Harness Analyze Account Access Policy API
  phrasing_intents:
  - id: analyze-account-access-policies
    intent: Analyze who has access in the account
    question: Which users or groups have a given permission across my Harness account?
  phrasing_ops: 1
  slug: harness-analyze-account-access-policy-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Analyze Organization Access Policy API from Harness — 1 operation(s) for analyze organization access policy.
  name: Harness Analyze Organization Access Policy API
  phrasing_intents:
  - id: analyze-org-access-policies
    intent: Analyze who has access to what in an organization
    question: Who in an organization has a given permission, and through which role?
  phrasing_ops: 1
  slug: harness-analyze-organization-access-policy-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Analyze Project Access Policy API from Harness — 1 operation(s) for analyze project access policy.
  name: Harness Analyze Project Access Policy API
  phrasing_intents:
  - id: analyze-project-access-policies
    intent: Analyze who has access in a project
    question: Who in this project has a particular permission?
  phrasing_ops: 1
  slug: harness-analyze-project-access-policy-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Get details about any anomalous spike in your cloud and AI costs
  name: Harness Anomalies API
  phrasing_intents:
  - id: getAnomaliesSummary
    intent: Summarize cloud cost anomalies
    question: What is the overall picture of cost anomalies across my clouds?
  - id: anomalyFilterValues
    intent: List distinct values for anomaly filters
    question: What values can I filter cost anomalies by?
  - id: listAnomalies
    intent: List detected cost anomalies
    question: Which unexpected cost spikes have been detected in my cloud spend?
  - id: listIgnoredAnomalies
    intent: List anomalies on the ignore list
    question: Which cost anomalies have we put on the ignore list?
  - id: listPerspectiveAnomalies
    intent: List anomalies for a perspective
    question: What cost anomalies show up in a particular perspective?
  - id: reportAnomalyFeedback
    intent: Mark an anomaly as true or false
    question: Can I tell the system that a flagged cost anomaly was a false alarm?
  - id: DismissAnomaly
    intent: Dismiss a CCM anomaly
    question: Can I acknowledge a CCM anomaly so it no longer needs attention?
  phrasing_ops: 7
  slug: harness-anomalies-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Anomalies Ignorelist Rule Management.
  name: Harness Anomalies Ignorelist Rule API
  phrasing_intents:
  - id: CreateNewAnomaliesIgnorelistRule
    intent: Create a cost anomaly ignore rule
    question: How do I stop certain cost anomalies from being flagged?
  - id: GetAnomaliesIgnorelistRule
    intent: Get an anomaly ignore rule
    question: What does a specific anomaly ignore rule match?
  - id: UpdateAnomaliesIgnorelistRule
    intent: Update an anomaly ignore rule
    question: Can I change what an existing anomaly ignore rule matches?
  - id: DeleteAnomaliesIgnorelistRule
    intent: Delete an anomaly ignore rule
    question: How do I delete an anomaly ignore rule so those anomalies show again?
  - id: listAzureSubscriptions
    intent: List Azure subscriptions for ignore rule filters
    question: Which Azure subscriptions can I scope an anomaly ignore rule to?
  - id: ListAnomaliesIgnorelistRule
    intent: List anomaly ignore rules
    question: What anomaly ignore rules are set up on my account?
  - id: ToggleAnomaliesIgnorelistRule
    intent: Enable or disable an anomaly ignore rule
    question: Can I pause an anomaly ignore rule without deleting it?
  phrasing_ops: 7
  slug: harness-anomalies-ignorelist-rule-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: APIs to manage anomaly comments
  name: Harness Anomaly Comments API
  phrasing_intents:
  - id: listAnomalyComments
    intent: List comments on a cost anomaly
    question: What has the team said about a particular cost anomaly?
  - id: saveAnomalyComment
    intent: Comment on a cost anomaly
    question: Can I annotate a cost anomaly with an explanation?
  phrasing_ops: 2
  slug: harness-anomaly-comments-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Ansible Service handles the API for ansible entities.
  name: Harness Ansible API
  phrasing_intents:
  - id: ansible#list-ansible-activities
    intent: List Ansible run activities in a project
    question: Which Ansible runs have happened recently in my Harness project?
  - id: ansible#show-ansible-activity
    intent: Get one Ansible activity record
    question: What happened in a specific Ansible activity I have the ID for?
  - id: ansible#list-data
    intent: List stored Ansible data files
    question: What data files has Ansible stored for an inventory or playbook?
  - id: ansible#create-data
    intent: Store binary data produced by an Ansible run
    question: How do I upload binary output generated by Ansible into Harness?
  - id: ansible#show-data
    intent: Download one stored Ansible data file
    question: Can I fetch a stored plan or state file the provisioner generated?
  - id: ansible#send-ansible-event
    intent: Send an Ansible event to Harness
    question: How do I report an Ansible event for a set of playbooks and inventories?
  - id: ansible#get-file
    intent: Fetch a playbook or inventory YAML from git
    question: Can I read the YAML of a playbook straight from its configured git repo?
  - id: ansible#list-hosts
    intent: List hosts across all Ansible inventories
    question: Which hosts does Ansible manage across every inventory in my project?
  phrasing_ops: 44
  slug: harness-ansible-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: APIs to create and manage Feature Flag SDK API Keys
  name: Harness API Keys API
  phrasing_intents:
  - id: GetAllAPIKeys
    intent: List feature flag SDK keys for an environment
    question: Which feature flag SDK keys exist for one of my environments?
  - id: AddAPIKey
    intent: Create a feature flag SDK key
    question: How do I create a new SDK key so my app can evaluate feature flags in an environment?
  - id: DeleteAPIKey
    intent: Delete a feature flag SDK key
    question: How do I revoke a feature flag SDK key that leaked?
  - id: GetAPIKey
    intent: Get a feature flag SDK key
    question: How do I look up one feature flag API key by its identifier?
  - id: UpdateAPIKey
    intent: Update a feature flag SDK key
    question: Can I rename an existing feature flag API key?
  phrasing_ops: 5
  slug: harness-api-keys-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Application API from Harness — 1 operation(s) for application.
  name: Harness Application API
  phrasing_intents:
  - id: ApplicationService_ListApps
    intent: List GitOps applications
    question: Which GitOps applications are deployed in my project?
  phrasing_ops: 1
  slug: harness-application-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Applications API from Harness — 30 operation(s) for applications.
  name: Harness Applications API
  phrasing_intents:
  - id: AgentApplicationService_List
    intent: List GitOps applications managed by an agent
    question: Which GitOps applications does a particular Harness GitOps agent manage?
  - id: AgentApplicationService_Create
    intent: Create a GitOps application on an agent
    question: How do I register a new Argo-style application with my GitOps agent?
  - id: AgentApplicationService_Parent
    intent: Find the parent app of a GitOps application
    question: Which app-of-apps or ApplicationSet owns this child GitOps application?
  - id: AgentApplicationService_ManagedResources
    intent: List resources managed by a GitOps application
    question: What Kubernetes resources does my GitOps application manage?
  - id: AgentApplicationService_ResourceTree
    intent: Get the resource tree of a GitOps application
    question: How are the resources in my GitOps application nested, from Deployment down to pods?
  - id: AgentApplicationService_Get
    intent: Get a GitOps application by name
    question: What is the current sync and health status of a specific GitOps application?
  - id: AgentApplicationService_ListResourceEvents
    intent: List Kubernetes events for a GitOps application
    question: What Kubernetes events has my GitOps application's resources emitted recently?
  - id: AgentApplicationStreamService_PodLogs2
    intent: Stream logs across an application's pods
    question: How can I tail logs from all the pods in a GitOps application without naming a pod?
  phrasing_ops: 35
  slug: harness-applications-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The ApplicationSet API from Harness — 8 operation(s) for applicationset.
  name: Harness Application Set API
  phrasing_intents:
  - id: ApplicationSetService_Create
    intent: Create a GitOps ApplicationSet
    question: How do I add a new ApplicationSet to a GitOps agent?
  - id: ApplicationSetService_Update
    intent: Update an existing GitOps ApplicationSet
    question: How do I change an ApplicationSet that's already deployed through my GitOps agent?
  - id: ApplicationSetService_Generate
    intent: Preview child applications an ApplicationSet generates
    question: Which child applications would my ApplicationSet produce?
  - id: ApplicationSetService_ListApplicationSetGenerators
    intent: List available ApplicationSet generator types
    question: What generator types can I use in an ApplicationSet?
  - id: ApplicationSetService_GetApplicationSetGenerator
    intent: Get details of one ApplicationSet generator
    question: What does a specific ApplicationSet generator look like and how is it configured?
  - id: ApplicationSetService_GetApplicationSetTemplate
    intent: Get an ApplicationSet starter template
    question: Is there a starter template for an ApplicationSet using a given generator?
  - id: ApplicationSetService_Get
    intent: Get an ApplicationSet
    question: How do I look up a single ApplicationSet by its identifier?
  - id: ApplicationSetService_Delete
    intent: Delete an ApplicationSet
    question: How can I remove an ApplicationSet from my GitOps setup?
  phrasing_ops: 10
  slug: harness-applicationset-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Approvals.
  name: Harness Approvals API
  phrasing_intents:
  - id: getApprovalInstancesByExecutionId
    intent: List approval steps in a pipeline run
    question: Which approval steps are waiting in a particular pipeline execution?
  - id: addHarnessApprovalActivityByPipelineExecutionId
    intent: Approve or reject a run by its execution ID
    question: Can I approve a waiting pipeline knowing only its execution ID?
  - id: addHarnessApprovalActivity
    intent: Approve or reject an approval instance
    question: How do I approve a Harness approval step from a script?
  - id: approvals#list-approvals
    intent: List IaC workspace approvals
    question: What infrastructure plan approvals are pending in my project?
  - id: approvals#create-approval
    intent: Create an IaC workspace approval
    question: How is an approval record created for an infrastructure workspace stage?
  - id: approvals#show-approval
    intent: Get one IaC workspace approval
    question: Who actioned a given infrastructure approval, and what is its status?
  - id: approvals#update-approval
    intent: Approve or reject an IaC workspace approval
    question: How do I mark an infrastructure plan approval as approved or rejected?
  phrasing_ops: 7
  slug: harness-approvals-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The ArgoProjects API from Harness — 4 operation(s) for argoprojects.
  name: Harness Argo Projects API
  phrasing_intents:
  - id: AgentArgoProjectService_ListForAgent
    intent: List ArgoCD AppProjects on an agent
    question: Which ArgoCD AppProjects are mapped to my GitOps agent?
  - id: AgentArgoProjectService_Create
    intent: Create an ArgoCD AppProject in the cluster
    question: How do I create an ArgoCD AppProject through Harness?
  - id: AgentArgoProjectService_Get
    intent: Get an ArgoCD AppProject by name
    question: Can I read the spec of one ArgoCD AppProject by its name?
  - id: AgentArgoProjectService_Delete
    intent: Delete an ArgoCD AppProject from the cluster
    question: Can I delete an ArgoCD AppProject from the cluster?
  - id: AgentArgoProjectService_ListEvents
    intent: List Kubernetes events for an AppProject
    question: What Kubernetes events has an ArgoCD AppProject produced?
  - id: AgentArgoProjectService_Update
    intent: Update an ArgoCD AppProject spec
    question: How do I change the spec of an existing ArgoCD AppProject?
  phrasing_ops: 6
  slug: harness-argoprojects-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The artifact API from Harness — 5 operation(s) for artifact.
  name: Harness Artifact API
  phrasing_intents:
  - id: listArtifacts
    intent: List all artifact versions in a project
    question: What artifacts has supply chain security tracked in my project?
  - id: listLatestArtifacts
    intent: List the latest version of each artifact
    question: What's the newest version of every artifact in my project?
  - id: getArtifactDetailComponentView
    intent: List the components inside an artifact tag
    question: Which open source components are inside this artifact version?
  - id: getArtifactDetailDeploymentView
    intent: List where an artifact tag is deployed
    question: Which environments is this artifact version deployed to?
  - id: getArtifactDetails
    intent: Get details of an artifact tag
    question: What are the details of a specific artifact version?
  phrasing_ops: 5
  slug: harness-artifact-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The artifactListing API from Harness — 7 operation(s) for artifactlisting.
  name: Harness Artifact Listing API
  phrasing_intents:
  - id: listArtifactSources
    intent: List artifact sources with artifact counts
    question: Which artifact registries feed my project and how many artifacts does each hold?
  - id: artifactListV2
    intent: List artifacts from one artifact source
    question: What artifacts come from a particular registry source?
  - id: getArtifactV2DetailComponentView
    intent: List the SBOM components of an artifact
    question: Which open source components and licenses are inside an artifact?
  - id: getArtifactV2DetailDeploymentView
    intent: See where an artifact is deployed
    question: Which environments is this artifact deployed to right now?
  - id: getArtifactV2Overview
    intent: Get an artifact's overview by source and artifact ID
    question: What is the security and compliance overview of an artifact?
  - id: getArtifactV2OverviewByName
    intent: Look up an artifact overview by image name and digest
    question: Can I find an artifact's overview using its image name, registry URL and digest?
  - id: getArtifactV2ChainOfCustody
    intent: Get an artifact's chain of custody
    question: What is the full history of events for an artifact from build to deploy?
  phrasing_ops: 7
  slug: harness-artifactlisting-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The artifactListingV2 API from Harness — 1 operation(s) for artifactlistingv2.
  name: Harness Artifact Listing V2 API
  phrasing_intents:
  - id: getArtifactChainOfCustodyV2
    intent: Get an artifact's chain of custody
    question: What is the chain of custody for a given artifact in my supply chain?
  phrasing_ops: 1
  slug: harness-artifactlistingv2-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: APIs to get, list artifacts
  name: Harness Artifacts API
  phrasing_intents:
  - id: RedirectHarnessArtifact
    intent: Open an artifact's page in the registry UI
    question: Is there a link that redirects straight to an artifact's page in Harness Artifact Registry?
  - id: DeleteArtifact
    intent: Delete an artifact and all its versions
    question: How do I delete an entire artifact from a Harness registry?
  - id: UpdateArtifactLabels
    intent: Set the labels on an artifact
    question: How do I add or change labels on an artifact in my registry?
  - id: GetArtifactStats
    intent: Get download and usage stats for one artifact
    question: How many downloads has a specific artifact had over a date range?
  - id: GetArtifactSummary
    intent: Get a summary of an artifact
    question: What's the overview of an artifact, like its type and latest version?
  - id: GetOciArtifactTags
    intent: List tags of an OCI image
    question: Which tags exist for a container image in my Harness registry?
  - id: DeleteArtifactVersion
    intent: Delete one version of an artifact
    question: How do I delete a single version of a package without removing the others?
  - id: CreateBulkDownloadRequestV1
    intent: Request a bulk download of an artifact version
    question: Can I download all the files of an artifact version in one bulk request?
  phrasing_ops: 16
  slug: harness-artifacts-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The ArtifactSigning API from Harness — 4 operation(s) for artifactsigning.
  name: Harness Artifact Signing API
  phrasing_intents:
  - id: saveSignature
    intent: Record an artifact signature
    question: How do I save the signature produced when an artifact was signed in a pipeline?
  - id: saveIntegrityVerification
    intent: Record an artifact integrity verification
    question: Where do I record whether an artifact passed signature verification?
  - id: uploadSignature
    intent: Upload an artifact signature
    question: How do I upload a signature and its signed payload for an artifact?
  - id: downloadSignature
    intent: Download an artifact's signature
    question: How do I fetch the signature for an image by its digest or tag?
  phrasing_ops: 4
  slug: harness-artifactsigning-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The artifactV2 API from Harness — 1 operation(s) for artifactv2.
  name: Harness Artifact V2 API
  phrasing_intents:
  - id: artifactList
    intent: List supply chain artifacts in a project
    question: Which artifacts has supply chain security tracked in my project?
  phrasing_ops: 1
  slug: harness-artifactv2-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: APIS to create and manage Target Group Attributes
  name: Harness Attributes API
  phrasing_intents:
  - id: GetAttributes
    intent: List custom target attributes in an environment
    question: Which custom attributes have feature flag targets reported in an environment?
  - id: CreateAttribute
    intent: Create a custom target attribute
    question: How do I add a new custom attribute for feature flag targeting?
  - id: DeleteAttribute
    intent: Delete a custom target attribute
    question: How do I remove a custom attribute from an environment?
  - id: GetAttribute
    intent: Get a custom target attribute
    question: What details are stored for a particular custom attribute?
  - id: PatchAttribute
    intent: Update a custom attribute via instructions
    question: How do I change a custom attribute's key details in an environment?
  phrasing_ops: 5
  slug: harness-attributes-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Audit as defined in Harness
  name: Harness Audit API
  phrasing_intents:
  - id: getAuditEventList
    intent: List audit events (v1)
    question: Who changed what in my Harness account, and when?
  - id: getAuditEventListV2
    intent: List audit events (v2)
    question: Is there a newer v2 endpoint for querying audit events?
  phrasing_ops: 2
  slug: harness-audit-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Filter of type Audit as defined in Harness
  name: Harness Audit Filters API
  phrasing_intents:
  - id: getAuditFilterList
    intent: List saved audit log filters
    question: Which saved audit trail filters do we have?
  - id: updateAuditFilter
    intent: Update a saved audit filter
    question: How do I change the criteria in a saved audit filter?
  - id: postAuditFilter
    intent: Save a new audit log filter
    question: Can I save an audit trail search as a reusable filter?
  - id: getAuditFilter
    intent: Get a saved audit filter
    question: What criteria does a given saved audit filter apply?
  - id: deleteAuditFilter
    intent: Delete a saved audit filter
    question: How do I remove a saved audit filter?
  phrasing_ops: 5
  slug: harness-auditfilters-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Audits API from Harness — 1 operation(s) for audits.
  name: Harness Audits API
  phrasing_intents:
  - id: post-audits
    intent: Search the audit trail
    question: Who changed what in my account last week?
  phrasing_ops: 1
  slug: harness-audits-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Audit Yaml as defined in Harness
  name: Harness Audit YAML API
  phrasing_intents:
  - id: getYamlDiff
    intent: Get the YAML diff of one audit event
    question: What changed in the YAML for a single audit trail entry?
  - id: getAuditYamlDiffs
    intent: Compute JSON Patch diffs for audit events
    question: Can I get field-level diffs for several audit events at once?
  phrasing_ops: 2
  slug: harness-audityaml-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Authentication settings as defined in Harness
  name: Harness Authentication Settings API
  phrasing_intents:
  - id: getLdapSettings
    intent: View the account's LDAP settings
    question: What LDAP connection and sync settings are configured on my Harness account?
  - id: updateLdapSettings
    intent: Change the account's existing LDAP settings
    question: Can I change the cron schedule of an LDAP sync that's already set up?
  - id: createLdapSettings
    intent: Set up LDAP authentication for the account
    question: What do I need to connect my account to an LDAP directory for the first time?
  - id: deleteLdapSettings
    intent: Remove the account's LDAP settings
    question: Can I remove the LDAP configuration from my account entirely?
  - id: deleteSamlMetaData
    intent: Delete the account-level SAML metadata
    question: How do I wipe the SAML metadata for my whole account?
  - id: deleteSamlMetaDataForSamlSSOId
    intent: Delete one SAML SSO configuration's metadata
    question: Can I remove the metadata for just one of several SAML identity providers?
  - id: enableDisableAuthenticationForSAMLSetting
    intent: Turn login on or off for one SAML setting
    question: Can I temporarily disable sign-in through one SAML provider without deleting it?
  - id: getAuthenticationSettings
    intent: Get the account's authentication settings
    question: Which login mechanisms and authentication settings does my account use?
  phrasing_ops: 23
  slug: harness-authentication-settings-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: IDP app Auth Information
  name: Harness Auth Info API
  phrasing_intents:
  - id: get-auth-info-auth-id
    intent: Get saved auth details for an auth id
    question: How do I read the auth details stored for a given auth id?
  - id: save-auth-info-auth-id
    intent: Save auth details for an auth id
    question: How do I store authentication environment variables for an auth id?
  phrasing_ops: 2
  slug: harness-authinfo-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs to create and manage alerts for AutoStopping events and notifications.
  name: Harness AutoStopping Alerts API
  phrasing_intents:
  - id: CreateAlert
    intent: Create an AutoStopping alert
    question: Can I get emailed or pinged in Slack when an AutoStopping warmup fails?
  - id: UpdateAlert
    intent: Update an AutoStopping alert
    question: How do I change who receives an existing AutoStopping alert?
  - id: ListAlerts
    intent: Search AutoStopping alerts
    question: Which AutoStopping alerts are set up in my account?
  - id: GetAlert
    intent: Get one AutoStopping alert
    question: What events and recipients does a specific AutoStopping alert have?
  - id: DeleteAlert
    intent: Delete an AutoStopping alert
    question: How do I stop an AutoStopping alert from sending notifications for good?
  phrasing_ops: 5
  slug: harness-autostopping-alerts-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs to manage fixed schedules for the AutoStopping Rules.
  name: Harness AutoStopping Fixed Schedules API
  phrasing_intents:
  - id: listAutoStoppingSchedules
    intent: List fixed schedules on an AutoStopping rule
    question: What fixed start and stop times are configured for my AutoStopping rule?
  - id: createAutoStoppingSchedules
    intent: Add a fixed schedule to an AutoStopping rule
    question: How do I keep resources running during business hours with an AutoStopping schedule?
  - id: deleteAutoStoppingSchedule
    intent: Delete an AutoStopping fixed schedule
    question: How do I remove a fixed schedule from an AutoStopping rule?
  phrasing_ops: 3
  slug: harness-autostopping-fixed-schedules-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs to create and manage load balancers used for AutoStopping.
  name: Harness AutoStopping Load Balancers API
  phrasing_intents:
  - id: ListLoadBalancers
    intent: List AutoStopping load balancers
    question: Which AutoStopping load balancers are set up in my cloud account?
  - id: EditLoadBalancer
    intent: Update an AutoStopping load balancer
    question: Can I change the security groups on an existing AutoStopping load balancer?
  - id: CreateLoadBalancer
    intent: Create an AutoStopping load balancer
    question: How do I set up a proxy entry point so AutoStopping can wake idle resources on traffic?
  - id: DeleteLoadBalancer
    intent: Delete AutoStopping load balancers
    question: Can I delete an AutoStopping load balancer along with the cloud resources it created?
  - id: DescribeLoadBalancer
    intent: Get an AutoStopping load balancer's details
    question: What's the configuration and status of one AutoStopping load balancer?
  - id: AccessPointRules
    intent: List AutoStopping Rules routed through a load balancer
    question: Which AutoStopping Rules send traffic through a given load balancer?
  - id: LoadBalancerActivity
    intent: Get when a load balancer last saw traffic
    question: When did an AutoStopping load balancer last receive traffic?
  phrasing_ops: 7
  slug: harness-autostopping-load-balancers-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs to create and manage AutoStopping Rules for your cloud resources.
  name: Harness AutoStopping Rules API
  phrasing_intents:
  - id: ListAutoStoppingRules
    intent: List AutoStopping rules
    question: Which AutoStopping rules do I have set up to shut down idle cloud resources?
  - id: UpdateAutoStoppingRule
    intent: Create an AutoStopping rule
    question: How do I create a rule that stops idle cloud VMs automatically?
  - id: AutoStoppingRuleDetails
    intent: Get an AutoStopping rule's configuration
    question: What idle time and resources are configured on a particular AutoStopping rule?
  - id: DeleteAutoStoppingRule
    intent: Delete an AutoStopping rule
    question: How do I permanently remove an AutoStopping rule?
  - id: HealthOfAutoStoppingRule
    intent: Check an AutoStopping rule's health
    question: Is my AutoStopping rule healthy and operating right now?
  - id: SavingsFromAutoStoppingRule
    intent: Get daily savings from one AutoStopping rule
    question: How much money has one AutoStopping rule saved each day?
  - id: AllAutoStoppingResources
    intent: List resources managed by an AutoStopping rule
    question: Which cloud resources does this AutoStopping rule control?
  - id: GetAutoStoppingDiagnostics
    intent: Run diagnostics on an AutoStopping rule
    question: Why isn't my AutoStopping rule stopping resources as expected?
  phrasing_ops: 13
  slug: harness-autostopping-rules-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains Autostopping v2 APIs that support the usage of Autostopping Proxy for managing cloud resources.
  name: Harness AutoStopping Rules V2 API
  phrasing_intents:
  - id: CreateAutoStoppingRuleV2
    intent: Create an AutoStopping rule
    question: How do I set up a rule that stops idle cloud resources automatically?
  - id: GetAutoStoppingRuleV2
    intent: Get an AutoStopping rule
    question: What proxy and idle settings does an AutoStopping rule use?
  - id: UpdateAutoStoppingRuleV2
    intent: Update an AutoStopping rule
    question: Can I change the idle behaviour of an existing AutoStopping rule?
  phrasing_ops: 3
  slug: harness-autostopping-rules-v2-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Backstage Environment Variable
  name: Harness Backstage Env Variable API
  phrasing_intents:
  - id: get-backstage-env-variables
    intent: List Backstage environment variables
    question: Which environment variables are mapped into my Harness IDP Backstage instance?
  - id: create-backstage-env-variable
    intent: Create a Backstage environment variable
    question: How do I add a new environment variable for Backstage to use, like a secret-backed token?
  - id: sync-backstage-env-variables
    intent: Sync all Backstage environment variables
    question: My Backstage env variable mappings look out of date; can I resynchronize them all?
  - id: get-backstage-env-variable
    intent: Get one Backstage environment variable
    question: What is a particular Backstage env variable mapped to?
  - id: update-backstage-env-variable
    intent: Update a Backstage environment variable
    question: Can I point an existing Backstage env variable at a different secret?
  - id: delete-backstage-env-variable
    intent: Delete a Backstage environment variable
    question: Can I remove one environment variable Backstage no longer needs?
  - id: create-backstage-env-variables
    intent: Create several Backstage env variables at once
    question: How do I add a whole set of environment variables to Backstage in one call?
  - id: update-backstage-env-variables
    intent: Update several Backstage env variables at once
    question: Can I update many Backstage environment variables in one request?
  phrasing_ops: 11
  slug: harness-backstageenvvariable-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Backstage Harness
  name: Harness Backstage Harness API
  phrasing_intents:
  - id: backstage-harness-sync-all-accounts
    intent: Sync Backstage entities for all IDP accounts
    question: Can I trigger a Backstage-to-platform entity sync across every IDP-enabled account at once?
  - id: backstage-harness-sync-for-account
    intent: Sync Backstage entities for my account
    question: How do I resync Backstage catalog entities for just my account?
  - id: backstage-harness-sync-for-account-entity
    intent: Sync one Backstage entity
    question: Can I sync a single Backstage entity instead of the whole catalog?
  phrasing_ops: 3
  slug: harness-backstageharness-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Backstage Permissions
  name: Harness Backstage Permissions API
  phrasing_intents:
  - id: get-backstage-permissions
    intent: Get Backstage permissions for the account
    question: Which Backstage permissions are set for my developer portal account?
  - id: create-backstage-permissions
    intent: Create Backstage permissions
    question: How do I set up Backstage permissions for the first time on my account?
  - id: update-backstage-permissions
    intent: Update Backstage permissions
    question: How do I change existing Backstage permissions in the developer portal?
  phrasing_ops: 3
  slug: harness-backstagepermissions-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The baseImage API from Harness — 1 operation(s) for baseimage.
  name: Harness Base Image API
  phrasing_intents:
  - id: getBaseImageDetails
    intent: Get base image details for an artifact
    question: Which base image is a container artifact built from?
  phrasing_ops: 1
  slug: harness-baseimage-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Baseline API from Harness — 1 operation(s) for baseline.
  name: Harness Baseline API
  phrasing_intents:
  - id: getBaselineForArtifact
    intent: Get an artifact's baseline
    question: Which tag is set as the baseline for comparing an artifact's security results?
  - id: setBaselineForArtifact
    intent: Set an artifact's baseline tag
    question: How do I choose which tag of an artifact becomes its baseline?
  phrasing_ops: 2
  slug: harness-baseline-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The BaselineV2 API from Harness — 1 operation(s) for baselinev2.
  name: Harness Baseline V2 API
  phrasing_intents:
  - id: setBaselineForArtifactV2
    intent: Set the baseline artifact for an artifact source
    question: How do I mark one artifact version as the baseline to compare others against?
  phrasing_ops: 1
  slug: harness-baselinev2-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Get details of BI-dashboards specific to CACM
  name: Harness BI Dashboards API
  phrasing_intents:
  - id: listBIDashboards
    intent: List cloud cost BI dashboards
    question: Which BI dashboards are available for cloud cost management?
  phrasing_ops: 1
  slug: harness-bi-dashboards-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: APIs for managing branch-scoped build sequence IDs
  name: Harness Branch Sequences API
  phrasing_intents:
  - id: deleteBranchSequence
    intent: Reset the build counter for one branch
    question: How do I reset the build number for just one branch of a pipeline?
  - id: listBranchSequences
    intent: List build counters for every branch of a pipeline
    question: What is the current build number for each branch of my pipeline?
  - id: deleteBranchSequences
    intent: Reset build counters for all branches of a pipeline
    question: How do I wipe every branch build counter on a pipeline?
  - id: getBranchSequence
    intent: Get the current build number for a branch
    question: What sequence ID is a specific branch of my pipeline on right now?
  - id: setBranchSequence
    intent: Set the build counter for a branch
    question: Can I set a branch's build number to a specific value?
  phrasing_ops: 5
  slug: harness-branch-sequences-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Manage Budget Groups and receive alerts when your costs exceed (or are forecasted to exceed) your configured budget group.
  name: Harness Budget Groups API
  phrasing_intents:
  - id: getBudgetGroup
    intent: Get a budget group's details
    question: What amount and alert thresholds are set on one of my budget groups?
  - id: updateBudgetGroup
    intent: Update a budget group
    question: How do I raise the amount on an existing budget group?
  - id: deleteBudgetGroup
    intent: Delete a budget group
    question: How do I remove a budget group I no longer track?
  - id: getAccessibleBudgetGroupSummaries
    intent: Filter budget groups into a hierarchy
    question: Can I filter my budget groups by amount range or budget status?
  - id: getLastPeriodCost
    intent: Get aggregated amounts for budgets or groups
    question: What is the combined amount across a set of budgets or budget groups?
  - id: getBudgetAndBudgetGroupsList
    intent: Summarize budgets and budget groups
    question: Can I see a summary of both budgets and budget groups together?
  - id: listBudgetGroups
    intent: List all budget groups
    question: Which budget groups exist in my Harness cloud cost account?
  - id: createBudgetGroup
    intent: Create a budget group with cost alerts
    question: How do I get alerted when a group of budgets exceeds a combined amount?
  phrasing_ops: 8
  slug: harness-budget-groups-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Manage Budgets in bulk
  name: Harness Budgets API
  phrasing_intents:
  - id: adjustBudgetAmountOperation
    intent: Adjust the amount of many budgets at once
    question: Can I raise several cloud cost budgets by a percentage in one request?
  - id: cloneBudgetsBulkOperation
    intent: Clone several budgets in bulk
    question: Can I duplicate a batch of budgets and decide how their alerts are copied?
  - id: createCostBucketBudgetsBulk
    intent: Create budgets for many cost buckets at once
    question: How do I create a budget for every cost bucket in a cost category in one call?
  - id: deleteBudgetsBulkOperation
    intent: Delete several budgets at once
    question: Can I delete a whole list of cost budgets in a single request?
  - id: checkBulkBudgetJobStatus
    intent: Check the status of a bulk budget job
    question: Has my bulk budget update job finished yet?
  - id: manageBudgetAlertsBulkOperation
    intent: Manage alerts on many budgets at once
    question: Can I add or remove alert recipients across many budgets in one go?
  - id: getBudget
    intent: Get a budget's details
    question: What amount, period and thresholds are set on one specific budget?
  - id: updateBudget
    intent: Update an existing budget
    question: How do I edit a budget I already created?
  phrasing_ops: 20
  slug: harness-budgets-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Get/set cost preferences for CACM features
  name: Harness CACM global cost settings API
  phrasing_intents:
  - id: getCostSettings
    intent: Get cost settings for a cost management feature
    question: Which AWS cost type, such as amortized or net, does a cloud cost feature use?
  - id: updateCostSettings
    intent: Change cost settings for a cost management feature
    question: How do I switch a cloud cost feature to show amortized AWS costs?
  phrasing_ops: 2
  slug: harness-cacm-global-cost-settings-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Get/set cost type settings for CACM governance
  name: Harness CACM governance cost settings API
  phrasing_intents:
  - id: getGovernanceCostSettings
    intent: Get cloud cost governance settings
    question: What cost settings does cloud asset governance use for my account?
  - id: updateGovernanceCostSettings
    intent: Update cloud cost governance settings
    question: How do I change the governance cost settings for one cloud?
  phrasing_ops: 2
  slug: harness-cacm-governance-cost-settings-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs required for the creation of Canny tickets
  name: Harness Canny API
  phrasing_intents:
  - id: createCannyPost
    intent: Submit feedback to a Canny board
    question: How do I post a feature request to a Canny feedback board on a user's behalf?
  - id: createCannyPostV2
    intent: Submit categorized feedback to a Canny board
    question: Can I file a Canny feedback post under a specific category?
  - id: getCannyBoards
    intent: List Canny feedback boards
    question: Which Canny feedback boards can I post ideas to?
  - id: getCannyBoards_1
    intent: List categories for Canny feedback boards
    question: What categories can I file a Canny post under?
  phrasing_ops: 4
  slug: harness-canny-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Catalog Custom Properties
  name: Harness Catalog Custom Properties API
  phrasing_intents:
  - id: ingest-catalog-custom-properties
    intent: Set a custom property on matching catalog entities
    question: How do I set a custom property across many catalog entities at once?
  - id: delete-catalog-custom-properties
    intent: Remove a custom property from matching entities
    question: Can I remove a custom property from every catalog entity that matches a filter?
  - id: get-catalog-custom-properties-by-entity
    intent: Get custom properties for a catalog entity
    question: What custom properties are set on a particular catalog entity?
  - id: ingest-catalog-custom-properties-by-entity
    intent: Set custom properties on one catalog entity
    question: How do I add a custom property to a single catalog entity?
  - id: delete-catalog-custom-properties-by-entity
    intent: Remove custom properties from one entity
    question: Can I delete a custom property from just one catalog entity?
  - id: get-entities-by-catalog-custom-property
    intent: Find entities that have a custom property
    question: Which catalog entities have a given custom property set?
  - id: ingest-entities-by-catalog-custom-property
    intent: Apply one custom property to a list of entities
    question: Can I set the same custom property on a specific list of entities?
  - id: delete-entities-by-catalog-custom-property
    intent: Remove a custom property from listed entities
    question: Can I unset a custom property on a specific list of entities?
  phrasing_ops: 8
  slug: harness-catalogcustomproperties-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: CCM Costs Service returns cloud cost management summaries for workspaces.
  name: Harness Ccm Costs API
  phrasing_intents:
  - id: ccm_costs#show
    intent: Show cloud cost summary for an IaC workspace
    question: How much do the resources managed by a Terraform workspace cost?
  phrasing_ops: 1
  slug: harness-ccm-costs-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Certificates API from Harness — 1 operation(s) for certificates.
  name: Harness Certificates API
  phrasing_intents:
  - id: CertificateService_ListCerts
    intent: List GitOps repository certificates
    question: Which TLS or SSH certificates are configured for GitOps?
  phrasing_ops: 1
  slug: harness-certificates-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Change Authoring API from Harness — 3 operation(s) for change authoring.
  name: Harness Change Authoring API
  phrasing_intents:
  - id: V1CreateChangeAuthoringEvent
    intent: Record a pipeline run from an AI change chat
    question: How is a pipeline run from the LLM change authoring chat recorded?
  - id: V1CheckChangesetExistence
    intent: Check which Liquibase changesets a schema already has
    question: Have these Liquibase changeset IDs already been applied to my database schema?
  - id: V1ExecuteLlmAuthoringPipeline
    intent: Run a validate-and-preview pipeline for a changeset
    question: Can I validate and preview a Liquibase changeset from the AI chat before applying it?
  phrasing_ops: 3
  slug: harness-change-authoring-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Changeset metadata API from Harness — 2 operation(s) for changeset metadata.
  name: Harness Changeset metadata API
  phrasing_intents:
  - id: V1ChangesetmetadataProjDbInstance
    intent: Get database changeset metadata for a pipeline stage
    question: Which database changesets did a pipeline stage apply to a schema instance?
  - id: V1StepFlywayMigrationScripts
    intent: Get the Flyway migration scripts a pipeline step ran
    question: Which Flyway migration scripts ran in a database pipeline step?
  phrasing_ops: 2
  slug: harness-changeset-metadata-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Chaos Components API from Harness — 2 operation(s) for chaos components.
  name: Harness Chaos Components API
  phrasing_intents:
  - id: getChaosComponentVariable
    intent: Get variables for a chaos fault, probe or action
    question: What inputs does a chaos fault or probe need before I run it?
  - id: runChaosComponent
    intent: Run a chaos fault, probe or action
    question: Can I run a single chaos fault on my infrastructure without a full experiment?
  phrasing_ops: 2
  slug: harness-chaos-components-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Chaos Hubs API from Harness — 3 operation(s) for chaos hubs.
  name: Harness Chaos Hubs API
  phrasing_intents:
  - id: listChaosHub
    intent: List chaos hubs in a project
    question: Which chaos hubs are connected to my Harness project?
  - id: createChaosHub
    intent: Create a chaos hub
    question: How do I add a chaos hub backed by my own Git repository?
  - id: getChaosHub
    intent: Get a chaos hub
    question: What repository and settings does a particular chaos hub use?
  - id: updateChaosHub
    intent: Rename or retag a chaos hub
    question: How do I rename a chaos hub or change its description?
  - id: deleteHub
    intent: Delete a chaos hub
    question: How do I remove a chaos hub from a project?
  - id: listHubMetadata
    intent: List chaos hub metadata
    question: Can I get lightweight metadata for many chaos hubs at once?
  phrasing_ops: 6
  slug: harness-chaos-hubs-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Chaos Infrastructure API from Harness — 27 operation(s) for chaos infrastructure.
  name: Harness Chaos Infrastructure API
  phrasing_intents:
  - id: getImageRegistry
    intent: Get the chaos image registry settings
    question: Which container image registry does Harness Chaos Engineering pull its chaos images from?
  - id: registerLegacyKubernetesInfra
    intent: Register a legacy Kubernetes chaos infrastructure
    question: How do I register a legacy Kubernetes chaos infrastructure in a project?
  - id: getLegacyKubernetesHelmInfraCommand
    intent: Get the Helm install command for a legacy chaos infra
    question: What Helm command do I run to install my legacy Kubernetes chaos infrastructure?
  - id: getLegacyKubernetesChaosInfraManifest
    intent: Download the manifest for a legacy chaos infra
    question: Where do I get the Kubernetes YAML manifest to apply for a legacy chaos infrastructure?
  - id: getLegacyKubernetesChaosInfraStats
    intent: Get statistics for legacy Kubernetes chaos infras
    question: How many legacy Kubernetes chaos infrastructures does my project have?
  - id: upgradeLegacyKubernetesChaosInfra
    intent: Upgrade a legacy Kubernetes chaos infrastructure
    question: How do I upgrade an outdated legacy Kubernetes chaos infrastructure to the latest version?
  - id: getLegacyKubernetesChaosInfraVersionDetails
    intent: Get version details for legacy Kubernetes chaos infras
    question: What versions are available for legacy Kubernetes chaos infrastructure?
  - id: getLegacyKubernetesChaosInfraDetails
    intent: Get details of a legacy Kubernetes chaos infra
    question: How can I see the configuration and status of one legacy Kubernetes chaos infra?
  phrasing_ops: 32
  slug: harness-chaos-infrastructure-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Chaos Recommendations API from Harness — 5 operation(s) for chaos recommendations.
  name: Harness Chaos Recommendations API
  phrasing_intents:
  - id: getRecommendation
    intent: Get a chaos experiment recommendation
    question: What does a specific chaos recommendation suggest testing?
  - id: listRecommendations1
    intent: List chaos experiment recommendations
    question: Which chaos experiments are recommended for my project?
  - id: deleteRecommendation
    intent: Delete a chaos recommendation
    question: Can I remove a chaos recommendation I don't want?
  - id: createRecommendation
    intent: Create an experiment from a recommendation
    question: Can I turn a chaos recommendation into a real experiment?
  - id: pipelineAddExperimentRecommendation
    intent: Add a recommended experiment to a pipeline
    question: Can I add a recommended chaos experiment to my pipeline?
  - id: runRecommendation
    intent: Run a recommended chaos experiment
    question: Can I run a recommended chaos experiment right away?
  - id: updateRecommendationStatus
    intent: Update a chaos recommendation's status
    question: Can I change the status of a single chaos recommendation?
  - id: bulkUpdateRecommendationStatus
    intent: Bulk update chaos recommendation statuses
    question: Can I update the status of many chaos recommendations at once?
  phrasing_ops: 8
  slug: harness-chaos-recommendations-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The ChaosGuard Conditions API from Harness — 3 operation(s) for chaosguard conditions.
  name: Harness ChaosGuard Conditions API
  phrasing_intents:
  - id: getSGPTemplateByGenAI
    intent: Generate a security governance condition template
    question: Can AI draft a security governance conditions template for chaos experiments?
  - id: listCondition
    intent: List ChaosGuard conditions
    question: What ChaosGuard conditions are set up in my project?
  - id: createCondition
    intent: Create a ChaosGuard condition
    question: How do I add a guard condition that restricts which faults can run?
  - id: getCondition
    intent: Get a ChaosGuard condition
    question: Can I see what faults and infrastructure a specific guard condition covers?
  - id: updateCondition
    intent: Update a ChaosGuard condition
    question: Can I change the faults an existing guard condition allows?
  - id: deleteCondition
    intent: Delete a ChaosGuard condition
    question: Can I remove a guard condition that's blocking experiments?
  phrasing_ops: 6
  slug: harness-chaosguard-conditions-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The ChaosGuard Rules API from Harness — 3 operation(s) for chaosguard rules.
  name: Harness ChaosGuard Rules API
  phrasing_intents:
  - id: listRule
    intent: List ChaosGuard rules
    question: What ChaosGuard rules are governing chaos experiments in my project?
  - id: createRule
    intent: Create a ChaosGuard rule
    question: How do I restrict who can run chaos experiments and when?
  - id: getRule
    intent: Get a ChaosGuard rule
    question: What conditions and user groups does one chaos guard rule cover?
  - id: updateRule1
    intent: Update a ChaosGuard rule
    question: Can I change the conditions or time windows on an existing chaos guard rule?
  - id: deleteRule1
    intent: Delete a ChaosGuard rule
    question: How do I delete a chaos guard rule entirely?
  - id: enableRule
    intent: Enable or disable a ChaosGuard rule
    question: Can I temporarily switch off a chaos guard rule without deleting it?
  phrasing_ops: 6
  slug: harness-chaosguard-rules-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Checks API from Harness — 4 operation(s) for checks.
  name: Harness Checks API
  phrasing_intents:
  - id: get-checks
    intent: List scorecard checks
    question: Which scorecard checks are available in my developer portal?
  - id: create-check
    intent: Create a custom scorecard check
    question: How do I add my own custom check to scorecards?
  - id: get-check
    intent: Get a scorecard check
    question: What rule does a particular scorecard check evaluate?
  - id: update-check
    intent: Update a scorecard check
    question: Can I change the rule on an existing custom check?
  - id: delete-check
    intent: Delete a scorecard check
    question: How do I remove a custom check I no longer want?
  - id: get-check-stats
    intent: Get pass/fail stats for a check
    question: How many catalog entities pass or fail a given check?
  - id: get-check-graph
    intent: Get trend graph data for a check
    question: How has a check's pass rate trended over time?
  phrasing_ops: 7
  slug: harness-checks-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The CICDWorkflows API from Harness — 6 operation(s) for cicdworkflows.
  name: Harness CICD Workflows API
  phrasing_intents:
  - id: getCICDWorkflowsList
    intent: List CI/CD workflows in a project
    question: Which CI/CD workflows has supply chain security discovered in my project?
  - id: getCICDWorkflowsSummary
    intent: Summarize CI/CD workflows and compliance
    question: How many CI/CD workflows do I have and how are they doing on compliance checks?
  - id: getCICDOverview
    intent: Get an overview of one CI/CD workflow
    question: What are the overview details of a single CI/CD workflow?
  - id: getCICDRulesEvaluationTrend
    intent: Get a workflow's rule evaluation trend
    question: How have compliance rule evaluations for a workflow trended over time?
  - id: getHarnessPipelineYaml
    intent: Get a Harness pipeline's workflow information
    question: Can I pull the pipeline details for a Harness pipeline tracked as a CI/CD workflow?
  - id: fetchPluginsForWorkflow
    intent: List plugins used by a CI/CD workflow
    question: Which plugins does a given CI/CD workflow use?
  phrasing_ops: 6
  slug: harness-cicdworkflows-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: APIs for listing cloud accounts across cloud providers.
  name: Harness Cloud Accounts API
  phrasing_intents:
  - id: listCloudAccounts
    intent: List cloud accounts for a cloud provider
    question: Which cloud accounts are connected for a given provider in cost management?
  phrasing_ops: 1
  slug: harness-cloud-accounts-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Get details about any anomalies in your cloud and AI costs
  name: Harness Cloud and AI cost anomalies v2 API
  phrasing_intents:
  - id: getAnomaliesList
    intent: List cloud cost anomalies
    question: Which unexpected cloud cost spikes has Harness detected in my account?
  - id: getAnomalyMetrics
    intent: Get metrics for each type of cost anomaly
    question: How many cost anomalies of each type do I have, and what's their cost impact?
  - id: getAnomalyMetricsSummary
    intent: Summarize cost anomaly metrics
    question: What's the headline summary of my cost anomalies right now?
  - id: getAnomalyMetricsTimeSeries
    intent: Chart cost anomaly metrics per day
    question: How have cost anomalies trended day by day?
  - id: getMeanResolutionTime
    intent: Get the mean time to resolve cost anomalies
    question: How long does my team take on average to resolve a cost anomaly?
  - id: updateAnomalyFeedback
    intent: Give feedback on a detected cost anomaly
    question: How do I tell Harness whether a flagged cost anomaly was real or a false alarm?
  - id: updateAnomalyStatus
    intent: Change the status of a cost anomaly
    question: How do I mark a cost anomaly as resolved or archived?
  phrasing_ops: 7
  slug: harness-cloud-and-ai-cost-anomalies-v2-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Get resource level insights into your cloud and AI cost anomalies
  name: Harness Cloud and AI cost anomaly details API
  phrasing_intents:
  - id: getAnomalyCostTimeSeriesData
    intent: Chart actual cost over time for an anomaly
    question: What did actual spend look like day by day around a cost anomaly?
  - id: getAnomalyDetails
    intent: Get details of a cost anomaly
    question: What caused a specific cloud or AI cost anomaly and how big was it?
  - id: getAnomalyResourceCostTimeSeriesData
    intent: Chart cost over time for one anomalous resource
    question: How did one resource's cost trend during an anomaly?
  - id: getAnomalyResourceList
    intent: List top resources behind a cost anomaly
    question: Which resources contributed most to this cost anomaly?
  phrasing_ops: 4
  slug: harness-cloud-and-ai-cost-anomaly-details-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs to onboard and manage Cluster Orchestrator for Kubernetes
  name: Harness Cluster Orchestrator API
  phrasing_intents:
  - id: listConnectedKubernetesClusters
    intent: List Kubernetes clusters connected to CCM
    question: Which Kubernetes clusters are connected to Harness cloud cost management?
  - id: onboardToClusterOrchestrator
    intent: Onboard a Kubernetes cluster to Cluster Orchestrator
    question: How do I enable Cluster Orchestrator on a cluster that already has a CCM Kubernetes connector?
  - id: getConnectedClusterDetails
    intent: Get details of an orchestrated cluster
    question: What region, VPC and status does an orchestrated cluster have?
  - id: updateClusterOrchestratorConfig
    intent: Update a Cluster Orchestrator's config
    question: How do I change the subnets or security groups a cluster orchestrator uses?
  phrasing_ops: 4
  slug: harness-cluster-orchestrator-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Gitops Clusters
  name: Harness Clusters API
  phrasing_intents:
  - id: getCluster
    intent: Get a GitOps cluster linked to an environment
    question: Which cluster is linked to a given Harness environment under a specific identifier?
  - id: deleteCluster
    intent: Unlink a cluster from an environment
    question: How do I detach one GitOps cluster from a Harness environment?
  - id: getClusterList
    intent: List clusters linked to an environment
    question: Which GitOps clusters are linked to my staging environment?
  - id: linkCluster
    intent: Link one GitOps cluster to an environment
    question: How do I attach a single GitOps cluster to a Harness environment?
  - id: linkClusters
    intent: Link several clusters to an environment at once
    question: Can I link many GitOps clusters to one environment in a single call?
  - id: unlinkClustersInBatch
    intent: Unlink several clusters from an environment
    question: How do I detach many clusters from an environment at once?
  - id: AgentClusterService_GetByName
    intent: Find an agent's cluster by name
    question: Can I look up a cluster a GitOps agent manages using its cluster name?
  - id: AgentClusterService_GetByUrl
    intent: Find an agent's cluster by server URL
    question: Which cluster on my GitOps agent points at a given Kubernetes API server URL?
  phrasing_ops: 17
  slug: harness-clusters-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The codeRepo API from Harness — 4 operation(s) for coderepo.
  name: Harness Code Repo API
  phrasing_intents:
  - id: codeRepositoriesList
    intent: List code repositories scanned for supply chain
    question: Which code repositories are tracked for supply chain security in a project?
  - id: getCodeRepositoryOverview
    intent: Get a scanned code repository's overview
    question: What's the supply chain overview for one code repository?
  - id: getRepoRulesEvaluationTrend
    intent: Get a repo's rule evaluation trend
    question: How have a repository's rule evaluations changed over time?
  - id: getAllRepositoriesSummary
    intent: Summarize all scanned repositories in a project
    question: What's the overall supply chain summary across a project's repositories?
  phrasing_ops: 4
  slug: harness-coderepo-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs specific to the Collection categories
  name: Harness Collection categories API
  phrasing_intents:
  - id: categories#listCategories
    intent: List collection categories
    question: Which collection categories are defined for my SEI workspace?
  - id: categories#createCategory
    intent: Create a collection category
    question: How do I add a new collection category to a workspace?
  - id: categories#deleteCategories
    intent: Delete several collection categories at once
    question: Can I delete multiple collection categories in a single request?
  - id: categories#updateCategory
    intent: Update a collection category
    question: How do I rename an existing collection category?
  - id: categories#deleteCategory
    intent: Delete one collection category
    question: How do I delete a single collection category by its ID?
  phrasing_ops: 5
  slug: harness-collection-categories-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs specific to Collections
  name: Harness Collections API
  phrasing_intents:
  - id: collections#listCollections
    intent: List collections
    question: Which collections (org units) are defined for my engineering insights?
  - id: collections#createCollection
    intent: Create a new collection
    question: How do I group teams or repositories into a new collection?
  - id: collections#editCollection
    intent: Edit an existing collection
    question: Can I change the definition of a collection that already exists?
  - id: collections#deleteCollection
    intent: Delete a collection
    question: How do I remove a collection I no longer need?
  phrasing_ops: 4
  slug: harness-collections-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Commitment Orchestrator APIs API from Harness — 1 operation(s) for commitment orchestrator apis.
  name: Harness Commitment Orchestrator APIs API
  phrasing_intents:
  - id: EventLogs
    intent: List commitment orchestration event logs
    question: What actions has Commitment Orchestrator taken on my cloud commitments?
  phrasing_ops: 1
  slug: harness-commitment-orchestrator-apis-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs to fetch commitment orchestrator events data.
  name: Harness Commitment Orchestrator Events APIs API
  phrasing_intents:
  - id: EventsChart
    intent: Chart commitment orchestrator events by date
    question: How many commitment events happened each day over a date range?
  - id: RenewalEvents
    intent: List RI and Savings Plan auto-renewal events
    question: Which reserved instance or savings plan renewals are coming up or already done?
  - id: RIRecommendationSchedule
    intent: Get the RI recommendation cooldown schedule
    question: When will the next reserved instance recommendation run become eligible?
  phrasing_ops: 3
  slug: harness-commitment-orchestrator-events-apis-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Commitment Orchestrator Landing Page API from Harness — 1 operation(s) for commitment orchestrator landing page.
  name: Harness Commitment Orchestrator Landing Page API
  phrasing_intents:
  - id: LandingPageHandler
    intent: Get commitment status and savings per cloud account
    question: Which of my cloud account connectors have commitments managed, and what are they saving?
  phrasing_ops: 1
  slug: harness-commitment-orchestrator-landing-page-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Commitment Orchestrator Setup APIs API from Harness — 9 operation(s) for commitment orchestrator setup apis.
  name: Harness Commitment Orchestrator Setup APIs API
  phrasing_intents:
  - id: SetupConfiguration
    intent: Set up commitment orchestration for a cloud account
    question: How do I turn on commitment orchestration for one of my cloud accounts?
  - id: SetupValidate
    intent: Validate a Savings Plans coverage target
    question: What are the maximum Savings Plans settings allowed for a target total coverage?
  - id: SetupInstanceTypes
    intent: List instance types in use for exclusions
    question: Which instance types are in use by region under my master account, so I can exclude some?
  - id: DeleteSetupConfiguration
    intent: Delete a commitment orchestration setup
    question: How do I turn off commitment orchestration completely for a cloud account?
  - id: GetSetupConfiguration
    intent: Get a commitment orchestration setup
    question: What commitment orchestration settings are saved for a cloud account?
  - id: UpdateSetupConfiguration
    intent: Update a commitment orchestration setup
    question: Can I switch an existing commitment orchestration setup out of dry-run mode?
  - id: GetEstimatedSavingsForSetup
    intent: Estimate savings for a target coverage
    question: How much would I save if I raised commitment coverage to a target percentage?
  - id: GetCostCoverageForSetup
    intent: Get EC2 cost and coverage breakdown
    question: How much of my EC2 spend is already covered by commitments, by instance type or region?
  phrasing_ops: 11
  slug: harness-commitment-orchestrator-setup-apis-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Commitment Orchestrator User Approval APIs API from Harness — 4 operation(s) for commitment orchestrator user approval apis.
  name: Harness Commitment Orchestrator User Approval APIs API
  phrasing_intents:
  - id: ApprovalsListV2
    intent: Search commitment transactions with filters
    question: Which Savings Plan or reserved instance transactions happened in a given date range and region?
  - id: ApprovalsList
    intent: List commitment transactions awaiting approval
    question: Which commitment purchases are waiting for me to approve?
  - id: ApprovalsUpdate
    intent: Approve or reject commitment transactions
    question: How do I approve a pending reserved instance purchase the orchestrator proposed?
  - id: ApprovalsOverview
    intent: Summarize commitment approvals and savings
    question: How much could I save if I approved the pending commitment events?
  phrasing_ops: 4
  slug: harness-commitment-orchestrator-user-approval-apis-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Commitment Utilization API from Harness — 1 operation(s) for commitment utilization.
  name: Harness Commitment Utilization API
  phrasing_intents:
  - id: GetCommitmentUtilizationDetails
    intent: Get savings plan and RI utilization
    question: How well are my savings plans and reserved instances being used?
  phrasing_ops: 1
  slug: harness-commitment-utilization-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The ComplianceResults API from Harness — 5 operation(s) for complianceresults.
  name: Harness Compliance Results API
  phrasing_intents:
  - id: fetchComplianceResults
    intent: List supply chain compliance results
    question: Which supply chain compliance checks failed in a project?
  - id: fetchComplianceResultsGroupById
    intent: Summarise compliance results per check
    question: How many artifacts pass or fail each compliance check?
  - id: fetchComplianceResultsByComplianceId
    intent: List artifacts evaluated by one compliance check
    question: Which artifacts were evaluated against a particular compliance check?
  - id: saveComplianceResult
    intent: Save compliance scan results
    question: How do I record compliance results from a repository scan in a pipeline?
  - id: fetchComplianceResultsByArtifact
    intent: List compliance results for an artifact
    question: Is a specific artifact compliant, and which checks did it fail?
  phrasing_ops: 5
  slug: harness-complianceresults-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The ComplianceResultsV2 API from Harness — 1 operation(s) for complianceresultsv2.
  name: Harness Compliance Results V2 API
  phrasing_intents:
  - id: saveComplianceResultV2
    intent: Save compliance scan results for a repository
    question: How do I submit supply chain compliance results for a repository scan?
  phrasing_ops: 1
  slug: harness-complianceresultsv2-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The ComplianceStandardsFilter API from Harness — 1 operation(s) for compliancestandardsfilter.
  name: Harness Compliance Standards Filter API
  phrasing_intents:
  - id: getComplianceStandardsFilters
    intent: Get compliance standards filter options
    question: Which compliance standards can I filter by?
  phrasing_ops: 1
  slug: harness-compliancestandardsfilter-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The ComplianceStats API from Harness — 4 operation(s) for compliancestats.
  name: Harness Compliance Stats API
  phrasing_intents:
  - id: postComplianceResultStatsOverview
    intent: Summarize compliance results by severity
    question: How many compliance findings do we have at each severity level?
  - id: getComplianceResultStatsByComplianceChecks
    intent: Get compliance stats per check
    question: Which individual compliance checks fail most often?
  - id: postComplianceResultStatsEvaluationBreakdownArtifactType
    intent: Break down compliance results by artifact
    question: Which artifact types account for our compliance evaluations?
  - id: get-compliance-evaluation-trends
    intent: Show compliance evaluation trends over time
    question: Is our compliance posture improving over the last few weeks?
  phrasing_ops: 4
  slug: harness-compliancestats-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The component API from Harness — 1 operation(s) for component.
  name: Harness Component API
  phrasing_intents:
  - id: getComponents
    intent: List components in a project
    question: Which components are tracked in my project?
  phrasing_ops: 1
  slug: harness-component-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Config API from Harness — 4 operation(s) for config.
  name: Harness Config API
  phrasing_intents:
  - id: getConfigForOrg
    intent: Get a supply chain config at org level
    question: What supply chain security config is set for an organization?
  - id: getConfigForAccount
    intent: Get a supply chain config at account level
    question: What supply chain security config applies account-wide?
  - id: listConfigs
    intent: List supply chain configs in a project
    question: Which supply chain security configs exist in a project?
  - id: saveConfig
    intent: Save a supply chain config in a project
    question: How do I save a supply chain security config for a project?
  - id: getConfigByNameAndType
    intent: Look up a supply chain config by name and type
    question: Can I find an SCS config by its name and type rather than its id?
  phrasing_ops: 5
  slug: harness-config-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The ConfigForProject API from Harness — 1 operation(s) for configforproject.
  name: Harness Config For Project API
  phrasing_intents:
  - id: getConfigById
    intent: Get a supply chain security config
    question: How do I view a supply chain security configuration in my project?
  - id: updateConfigById
    intent: Update a supply chain security config
    question: Can I rename or change the settings of a supply chain security config?
  phrasing_ops: 2
  slug: harness-configforproject-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Conflicts API from Harness — 1 operation(s) for conflicts.
  name: Harness Conflicts API
  phrasing_intents:
  - id: updateReleaseConflict
    intent: Resolve a release conflict
    question: Can I reassign a conflicting execution to a different release?
  phrasing_ops: 1
  slug: harness-conflicts-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Confluence Utils API from Harness — 1 operation(s) for confluence utils.
  name: Harness Confluence Utils API
  phrasing_intents:
  - id: confluenceOauthTokenGenerate
    intent: Generate a Confluence OAuth token
    question: How does Harness exchange a Confluence authorization code for an OAuth token?
  phrasing_ops: 1
  slug: harness-confluence-utils-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Connector Information
  name: Harness Connector Info API
  phrasing_intents:
  - id: get-connectors-info
    intent: List info for all connectors
    question: What connector info is stored for every provider type?
  - id: get-connector-info
    intent: Get the current connector info
    question: What connector is currently configured for this account?
  - id: save-connector-info
    intent: Create or update connector info
    question: How do I save connector details so they can be reused?
  - id: get-connector-info-by-providerType
    intent: Get connector info for a provider type
    question: What connector info is saved for a particular provider type?
  phrasing_ops: 4
  slug: harness-connectorinfo-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Connectors as defined in Harness
  name: Harness Connectors API
  phrasing_intents:
  - id: getCCMK8SConnectorList
    intent: List cloud cost Kubernetes connectors
    question: Which Kubernetes connectors are set up for cloud cost management in my account?
  - id: getConnectorList
    intent: List connectors with simple filters
    question: What connectors exist in my Harness project?
  - id: updateConnector
    intent: Update an existing connector
    question: How do I change the credentials or settings of a connector I already created?
  - id: createConnector
    intent: Create a new connector
    question: How do I create a connector so Harness can reach my cloud, Git or artifact repository?
  - id: getConnector
    intent: Get a connector's details
    question: How do I see the configuration of one connector by its ID?
  - id: deleteConnector
    intent: Delete a connector
    question: How do I delete a connector I no longer need?
  - id: getAllAllowedFieldValues
    intent: Get allowed field values for a connector type
    question: What values can I pick for fields when creating a connector of a given type?
  - id: getCEAwsTemplate
    intent: Get the AWS cost connector CloudFormation template URL
    question: Where is the AWS CloudFormation template I need to set up a cloud cost connector?
  phrasing_ops: 16
  slug: harness-connectors-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs specific to the Contributors
  name: Harness Contributors API
  phrasing_intents:
  - id: contributors#getActiveVersions
    intent: List active contributor data versions
    question: Which versions of our contributor list are currently active?
  - id: contributors#getSchema
    intent: Get the contributor data schema
    question: What fields, including custom ones, does a contributor record have?
  - id: users#listActiveUsers
    intent: List active licensed contributors
    question: Who counts as an active licensed contributor right now?
  - id: contributors#updateContributors
    intent: Update existing contributors
    question: How do I update details for contributors already in the system?
  - id: seiContributors#listContributors
    intent: List SEI contributors for the org
    question: Which licensed users does Software Engineering Insights count for our organization?
  phrasing_ops: 5
  slug: harness-contributors-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Allows you to categorize based on business requirements and get a contextual view of your expenses.
  name: Harness Cost Categories API
  phrasing_intents:
  - id: getBusinessMapping
    intent: Get a cost category
    question: What cost buckets and rules make up a particular cost category?
  - id: deleteBusinessMapping
    intent: Delete a cost category
    question: How do I delete a cost category?
  - id: getBusinessMappingForFilterPanel
    intent: Get cost categories for the recommendation filters
    question: Which cost categories and buckets can I filter recommendations by?
  - id: getBusinessMappingList
    intent: List cost categories
    question: What cost categories are set up in my account?
  - id: updateBusinessMapping
    intent: Update a cost category
    question: How do I change the buckets or rules on an existing cost category?
  - id: createBusinessMapping
    intent: Create a cost category
    question: How do I allocate cloud costs by team or business unit?
  phrasing_ops: 6
  slug: harness-cost-categories-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Cost Category Jira Project Mapping CRUD APIs.
  name: Harness Cost Category Jira Project Mapping API
  phrasing_intents:
  - id: bulkSyncCostCategoryJiraMappings
    intent: Bulk sync cost category Jira mappings
    question: Can I replace all my cost category to Jira project mappings in one call?
  - id: listCostCategoryJiraMapping
    intent: List cost category Jira mappings
    question: Which cost categories are mapped to which Jira projects?
  - id: createCostCategoryJiraMapping
    intent: Map a cost bucket to a Jira project
    question: How do I send recommendations for a cost bucket to a specific Jira project?
  - id: getCostCategoryJiraMapping
    intent: Get a cost category Jira mapping
    question: Which Jira project does a particular cost category mapping point to?
  - id: updateCostCategoryJiraMapping
    intent: Update a cost category Jira mapping
    question: How do I point an existing cost category mapping at a different Jira project?
  - id: deleteCostCategoryJiraMapping
    intent: Delete a cost category Jira mapping
    question: How do I stop routing a cost category's recommendations to Jira?
  phrasing_ops: 6
  slug: harness-cost-category-jira-project-mapping-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Fetch cloud and AI cost data for cost analysis
  name: Harness Cost Details API
  phrasing_intents:
  - id: iacmResourceCostOverview
    intent: Get cloud costs for Terraform-managed resources
    question: How much do the resources my Terraform workspace manages actually cost?
  - id: costdetailoverview
    intent: Get total cost and trend for a perspective
    question: What is my total cloud spend and trend for a perspective this month?
  - id: clusterData
    intent: Get Kubernetes cluster cost data as a table
    question: Which Kubernetes workloads cost the most in my clusters?
  - id: costdetailtabular
    intent: Get perspective cost details as a table
    question: Can I get a table of costs per service or account for a perspective?
  - id: costdetailttimeseries
    intent: Get perspective costs as a time series
    question: How has cost for a perspective changed day by day?
  phrasing_ops: 5
  slug: harness-cost-details-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Costs Service handles the API related with the costs attached to workspaces. This API is read only as all the cost are generated in the plugin side
  name: Harness Costs API
  phrasing_intents:
  - id: costs#list-costs
    intent: List monthly infrastructure cost per workspace
    question: What does each IaCM workspace in my project cost per month?
  - id: costs#list-costs-per-workspace
    intent: Get one workspace's cost by execution
    question: Which executions changed the cost of a particular workspace?
  phrasing_ops: 2
  slug: harness-costs-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Coverage Detail API from Harness — 1 operation(s) for coverage detail.
  name: Harness Coverage Detail API
  phrasing_intents:
  - id: CoverageDetail
    intent: Break down commitment coverage by dimension
    question: How much of my cloud usage is covered by commitments, broken down by region or instance family?
  phrasing_ops: 1
  slug: harness-coverage-detail-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Coverage Details API from Harness — 2 operation(s) for coverage details.
  name: Harness Coverage Details API
  phrasing_intents:
  - id: SPCoverageDetails
    intent: Get Savings Plans coverage details
    question: How much of my compute spend is covered by Savings Plans versus on-demand?
  - id: RICoverageDetails
    intent: Get Reserved Instances coverage details
    question: What percentage of my running hours are covered by Reserved Instances?
  phrasing_ops: 2
  slug: harness-coverage-details-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Coverage Overview API from Harness — 1 operation(s) for coverage overview.
  name: Harness Coverage Overview API
  phrasing_intents:
  - id: CoverageOverview
    intent: Get RI, Savings Plan and on-demand coverage
    question: How much of my compute spend is covered by reserved instances and savings plans versus on-demand?
  phrasing_ops: 1
  slug: harness-coverage-overview-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Credits allocation by account and moduleType API from Harness — 1 operation(s) for credits allocation by account and moduletype.
  name: Harness Credits allocation by account and moduleType API
  phrasing_intents:
  - id: credits-allocation-export-data
    intent: Export credit allocation data for a module
    question: How are Harness credits allocated in my account for a given module?
  phrasing_ops: 1
  slug: harness-credits-allocation-by-account-and-moduletype-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Credits OverUsage Data By Account API from Harness — 1 operation(s) for credits overusage data by account.
  name: Harness Credits OverUsage Data By Account API
  phrasing_intents:
  - id: credits-overusage
    intent: Get credit overuse count for an account
    question: How many credits has my account used beyond its allowance?
  phrasing_ops: 1
  slug: harness-credits-overusage-data-by-account-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Custom Deployment
  name: Harness Custom Deployment API
  phrasing_intents:
  - id: getCustomDeploymentEntityReferences
    intent: Find references in a custom deployment
    question: Which entities does my custom deployment template reference?
  - id: getCustomDeploymentExpressionVariables
    intent: List expression variables in a custom deployment
    question: What expression variables can I use in a custom deployment template?
  - id: getCustomDeploymentInfraVariables
    intent: Get infrastructure variables from a template
    question: What infrastructure variables does a custom deployment template define?
  - id: getUpdatedYamlForInfrastructure
    intent: Refresh infrastructure YAML from its template
    question: How do I bring an infrastructure definition in line with a changed deployment template?
  - id: validateInfrastructureForDeploymentTemplate
    intent: Validate infrastructure against its template
    question: Is my infrastructure definition still valid for its deployment template?
  phrasing_ops: 5
  slug: harness-customdeployment-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Custom Plugins V2.
  name: Harness Custom Plugins V2 API
  phrasing_intents:
  - id: get-custom-plugins-v2
    intent: List custom plugins
    question: What custom plugins are available in my Harness developer portal?
  - id: create-custom-plugins-v2
    intent: Create a custom plugin
    question: How do I register a new custom plugin in the portal?
  - id: get-custom-plugin-v2
    intent: Get a custom plugin's details
    question: How do I view the details of one custom plugin?
  - id: update-custom-plugin-v2
    intent: Update a custom plugin
    question: Can I rename a custom plugin or change its icon?
  - id: delete-custom-plugin-v2
    intent: Delete a custom plugin
    question: How do I delete a custom plugin from the portal?
  phrasing_ops: 5
  slug: harness-custompluginsv2-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Daily Module Account Access API from Harness — 1 operation(s) for daily module account access.
  name: Harness Daily Module Account Access API
  phrasing_intents:
  - id: get-v1-dailyModuleAccountAccess
    intent: Get daily module access records for a month
    question: Which days in a given month was a Harness module accessed on my account?
  phrasing_ops: 1
  slug: harness-daily-module-account-access-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Dashboard Aggregates API from Harness — 2 operation(s) for dashboard aggregates.
  name: Harness Dashboard Aggregates API
  phrasing_intents:
  - id: DashboardService_RecentDeployments
    intent: Get recent GitOps deployment statistics
    question: How many GitOps deployments succeeded or failed recently?
  - id: DashboardService_TopApplicationPhaseStats
    intent: List the five most deployed GitOps apps
    question: Which GitOps applications get deployed the most?
  phrasing_ops: 2
  slug: harness-dashboard-aggregates-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Aggregate summary of policies, policy sets and evaluations for display on the dashboard
  name: Harness Dashboard API
  phrasing_intents:
  - id: dashboard#metrics
    intent: Get policy governance metrics
    question: How many policies, policy sets and evaluations have run recently?
  phrasing_ops: 1
  slug: harness-dashboard-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Dashboards API from Harness — 13 operation(s) for dashboards.
  name: Harness Dashboards API
  phrasing_intents:
  - id: DashboardService_RecentlyCreatedCounts
    intent: Count recently created GitOps apps, clusters and repos
    question: How many GitOps applications, clusters and repositories were created in the last month?
  - id: DashboardService_GetDashboardOverview
    intent: Get the GitOps dashboard overview
    question: What are the key health and sync metrics on the GitOps dashboard?
  - id: get_dashboard_data
    intent: Download data from all tiles in a dashboard
    question: How do I export the data behind every tile on a custom dashboard?
  - id: get_dashboard_elements
    intent: List the elements of a dashboard
    question: Which tiles or elements make up a given dashboard?
  - id: get_dashboard_filters
    intent: List the filters on a dashboard
    question: What filters are defined on this dashboard and what are their defaults?
  - id: clone_dashboard
    intent: Clone a dashboard
    question: Can I copy an existing dashboard to use as a starting point for my own?
  - id: get_dashboard
    intent: Get a dashboard's details
    question: What are the name, folder and tags of a particular dashboard?
  - id: update_dashboard
    intent: Rename or move a dashboard
    question: How do I rename a dashboard or move it to another folder?
  phrasing_ops: 13
  slug: harness-dashboards-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Track and monitor the status of data ingestion and processing jobs across your cloud cost data pipeline.
  name: Harness Data Job Status API
  phrasing_intents:
  - id: getAllJobStatuses
    intent: List possible data job statuses
    question: What status values can a cloud cost data job have?
  - id: getDistinctBillingPeriods
    intent: List billing periods processed for a connector
    question: Which billing months have data jobs run for a given cost connector?
  - id: getDistinctExecutionMonths
    intent: List months a connector's data jobs ran
    question: In which months did data jobs actually execute for a connector?
  - id: getDistinctJobKinds
    intent: List data job kinds on the account
    question: What kinds of cost data jobs run on my account?
  - id: getDataJobHistoryDetails
    intent: Get a connector's data job execution history
    question: What happened in each run of a connector's data job during a month?
  - id: getDataJobDetails
    intent: Get a data job's latest run details
    question: What were the state transitions in the latest attempt of a data job?
  - id: getDataJobsDashboard
    intent: Get the data jobs dashboard summary
    question: How many cost data jobs are active or need attention right now?
  - id: listDataJobs
    intent: List data jobs with filters
    question: Which cost data jobs are currently failing?
  phrasing_ops: 8
  slug: harness-data-job-status-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for performing CRUD operations on Database Instance Entity
  name: Harness Database Instance API
  phrasing_intents:
  - id: V1GetDefaultAuthoringInstance
    intent: Get the default instance for authoring DB changes
    question: Which database instance should an LLM use to author schema changes?
  - id: V1CreateProjDbSchemaInstance
    intent: Create a database instance for a schema
    question: How do I add a database instance to a schema?
  - id: V1DeleteProjDbSchemaInstance
    intent: Delete a database instance
    question: How do I remove a database instance from a schema?
  - id: V1GetProjDbSchemaInstance
    intent: Get a database instance
    question: What is configured on a specific database instance?
  - id: V1ListProjDbSchemaInstance
    intent: List database instances of a schema
    question: What database instances belong to a schema?
  phrasing_ops: 5
  slug: harness-database-instance-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for performing CRUD operations on Database Schema Entity
  name: Harness Database Schema API
  phrasing_intents:
  - id: V1ListDatabaseSchema
    intent: List database schemas across an account
    question: Which database schemas exist across all projects in our account?
  - id: V1ListProjDbSchema
    intent: List database schemas in a project
    question: What database schemas are managed in this project?
  - id: V1CreateProjDbSchema
    intent: Create a database schema
    question: How do I register a new database schema for DB DevOps?
  - id: V1DeleteProjDbSchema
    intent: Delete a database schema
    question: How do I delete a database schema from a project?
  - id: V1GetProjDbSchema
    intent: Get a database schema
    question: What is configured on a specific database schema?
  - id: V1UpdateProjDbSchema
    intent: Update a database schema
    question: How do I change the changelog or service linked to a schema?
  - id: V1UpdateProjDbSchemaInstance
    intent: Update a database instance of a schema
    question: How do I change the branch or connector of a schema's database instance?
  phrasing_ops: 7
  slug: harness-database-schema-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for managing database snapshots and snapshot metadata
  name: Harness Database Snapshot API
  phrasing_intents:
  - id: V1GetSnapshotObjectNames
    intent: List object names in the latest DB snapshot
    question: Which tables or other objects of a given type are in my database instance's latest snapshot?
  - id: V1GetSnapshotObjectValues
    intent: Get object values from the latest DB snapshot
    question: What definitions were captured for specific objects in my database's latest snapshot?
  phrasing_ops: 2
  slug: harness-database-snapshot-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Dbops API from Harness — 3 operation(s) for dbops.
  name: Harness Dbops API
  phrasing_intents:
  - id: PostV1DbopsDbSnapshotMetadata
    intent: Record database snapshot metadata
    question: How does the DB DevOps plugin send snapshot metadata to capture a database's current state?
  - id: V1DeleteDbSchema
    intent: Delete database schemas for a scope
    question: Can I delete all database schemas under a parent in a project?
  - id: PostV1DbopsMetadataSnapshot
    intent: Upload a database snapshot file
    question: How does the plugin upload the actual snapshot file of a database?
  phrasing_ops: 3
  slug: harness-dbops-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Default Pipeline API from Harness — 1 operation(s) for default pipeline.
  name: Harness Default Pipeline API
  phrasing_intents:
  - id: V1DefaultLlmPipeline
    intent: Get the default LLM pipeline YAML for a database
    question: What default LLM pipeline YAML is generated for my database schema?
  phrasing_ops: 1
  slug: harness-default-pipeline-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Contains APIs related to Downloading Delegates
  name: Harness Delegate Download Resource API
  phrasing_intents:
  - id: downloadDockerDelegateYaml
    intent: Download a Docker delegate YAML
    question: How do I get the file to run a Harness delegate on Docker?
  - id: downloadKubernetesDelegateYaml
    intent: Download a Kubernetes delegate YAML
    question: How do I get the Kubernetes manifest to install a delegate in my cluster?
  phrasing_ops: 2
  slug: harness-delegate-download-resource-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Contains APIs related to Delegate Group Tags management
  name: Harness Delegate Group Tags Resource API
  phrasing_intents:
  - id: listTagsForDelegateGroup
    intent: List tags on a delegate group
    question: Which tags are attached to a delegate group?
  - id: updateTagsOfDelegateGroup
    intent: Replace all tags on a delegate group
    question: How do I overwrite a delegate group's tags with a new set?
  - id: addTagsToDelegateGroup
    intent: Add tags to a delegate group
    question: Can I add more tags to a delegate group without removing existing ones?
  - id: deleteTagsFromDelegateGroup
    intent: Remove all tags from a delegate group
    question: How do I strip every tag off a delegate group?
  - id: listDelegateGroupsUsingTags
    intent: Find delegate groups by tags
    question: Which delegate groups carry a particular tag?
  phrasing_ops: 5
  slug: harness-delegate-group-tags-resource-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Contains Delegate Setup APIs
  name: Harness Delegate Setup Resource API
  phrasing_intents:
  - id: deleteDelegate
    intent: Delete a delegate
    question: How do I remove a delegate we've decommissioned?
  - id: overrideDelegateImageTag
    intent: Remove a delegate image tag override
    question: Can I drop the pinned image tag so delegates go back to the default version?
  - id: generateTerraformModule
    intent: Get a Terraform example for installing delegates
    question: Is there a Terraform module example I can use to install a delegate?
  - id: generateNgHelmValuesYaml
    intent: Generate Helm values for a delegate install
    question: What Helm values file do I need to install a delegate on Kubernetes?
  - id: listOverrideDelegateImageTag
    intent: List delegate image tag overrides
    question: Are any delegate image versions pinned with overrides right now?
  - id: overrideDelegateImageTag_1
    intent: Pin delegates to a specific image tag
    question: How can I pin delegates to a particular image version for a while?
  - id: listDelegates
    intent: Search and filter delegates
    question: Which delegates are connected, and can I filter them by status or tag?
  - id: publishedDelegateVersion
    intent: Get the latest supported delegate version
    question: What is the newest delegate version I should be running?
  phrasing_ops: 8
  slug: harness-delegate-setup-resource-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Contains APIs related to Delegate Token management
  name: Harness Delegate Token Resource API
  phrasing_intents:
  - id: getCgDelegateTokens
    intent: List delegate tokens
    question: Which delegate tokens exist in my Harness project?
  - id: revokeCgDelegateToken
    intent: Revoke a delegate token
    question: How do I revoke a delegate token that may have leaked?
  - id: createDelegateToken
    intent: Create a delegate token
    question: How do I generate a new token for installing Harness delegates?
  - id: deleteNgDelegateToken
    intent: Delete a revoked delegate token
    question: How do I permanently delete a delegate token after revoking it?
  - id: getDelegateGroupsUsingToken
    intent: List delegate groups using a token
    question: Which delegate groups are still using a given token?
  phrasing_ops: 5
  slug: harness-delegate-token-resource-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Delete Repositories API from Harness — 2 operation(s) for delete repositories.
  name: Harness Delete Repositories API
  phrasing_intents:
  - id: deleteRepos
    intent: Remove repositories from an SCM integration
    question: How do I drop certain repositories from a supply chain SCM integration?
  - id: deleteRepositories
    intent: Delete repositories from the repo listing
    question: Can I delete repositories straight from the supply chain repository listing page?
  phrasing_ops: 2
  slug: harness-delete-repositories-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Delete Step Config API from Harness — 3 operation(s) for delete step config.
  name: Harness Delete Step Config API
  phrasing_intents:
  - id: deleteConfigByOrg
    intent: Delete an org-level supply chain step config
    question: How do I delete an SSCA step configuration defined at the organization level?
  - id: deleteConfigByAccount
    intent: Delete an account-level supply chain step config
    question: How do I delete an SSCA step configuration that applies to the whole account?
  - id: deleteConfigById
    intent: Delete a project-level supply chain step config
    question: How do I delete an SSCA step config scoped to a single project?
  phrasing_ops: 3
  slug: harness-delete-step-config-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for tracking changeSet deployment status
  name: Harness Deployed State API
  phrasing_intents:
  - id: V1GetDeployedState
    intent: Get deployed database changeset state
    question: Which database changesets did a pipeline execution deploy to a schema instance?
  phrasing_ops: 1
  slug: harness-deployed-state-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Devops Essentials License Data By Account API from Harness — 1 operation(s) for devops essentials license data by account.
  name: Harness Devops Essentials License Data By Account API
  phrasing_intents:
  - id: get-devops-essentials-license
    intent: Get DevOps Essentials subscription details
    question: What does my DevOps Essentials subscription include?
  phrasing_ops: 1
  slug: harness-devops-essentials-license-data-by-account-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: APIs to get details of docker artifacts
  name: Harness Docker Artifacts API
  phrasing_intents:
  - id: GetDockerArtifactDetails
    intent: Get details of a Docker image version
    question: What details are stored for a specific Docker image version in my artifact registry?
  - id: GetDockerArtifactIntegrationDetails
    intent: Get integration details for a Docker image
    question: Which pipelines and integrations have touched a given Docker image version?
  - id: GetDockerArtifactLayers
    intent: List the layers of a Docker image
    question: What layers make up a Docker image version and how big is each?
  - id: GetDockerArtifactManifest
    intent: Get the manifest for one Docker image digest
    question: Can I read the raw manifest of a Docker image for a specific digest?
  - id: GetDockerArtifactManifests
    intent: List all platform manifests for a Docker image
    question: Which platforms and architectures does a multi-arch Docker image version include?
  phrasing_ops: 5
  slug: harness-docker-artifacts-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs specific to the DORA reports
  name: Harness DORA API
  phrasing_intents:
  - id: dora#getLeadTime
    intent: Get DORA lead time for changes
    question: How long does it take our changes to get from commit to production?
  - id: dora#getDeploymentFrequency
    intent: Get DORA deployment frequency
    question: How often are we deploying to production?
  - id: dora#getChangeFailureRate
    intent: Get DORA change failure rate
    question: What percentage of our deployments cause failures?
  - id: dora#getMeanTimeToRestore
    intent: Get DORA mean time to restore
    question: How quickly do we recover from incidents on average?
  phrasing_ops: 4
  slug: harness-dora-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The downloads API from Harness — 2 operation(s) for downloads.
  name: Harness Downloads API
  phrasing_intents:
  - id: get_download_task_status
    intent: Check the status of a dashboard download task
    question: Is my dashboard tile export finished yet?
  - id: create_dashboard_element_download_task
    intent: Start a download task for one dashboard tile
    question: How do I export the data behind a single dashboard tile in the background?
  - id: get_dashboard_element_download_task_results
    intent: Fetch the results of a tile download task
    question: Once a tile export finishes, how do I retrieve the file?
  phrasing_ops: 3
  slug: harness-downloads-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to CRUD operations of Downtime
  name: Harness Downtime API
  phrasing_intents:
  - id: getDowntime
    intent: Get a scheduled downtime
    question: What window and services does a particular monitoring downtime cover?
  - id: updateDowntimeData
    intent: Edit a downtime's schedule and scope
    question: How do I change the schedule or affected services of an existing downtime?
  - id: deleteDowntimeData
    intent: Delete a downtime
    question: Can I delete a maintenance downtime that's no longer needed?
  - id: getAssociatedMonitoredServices
    intent: List services covered by one downtime
    question: Which monitored services are silenced by a specific downtime?
  - id: getDowntimeAssociatedMonitoredServices
    intent: List all services that have downtimes
    question: Which monitored services in this project have any downtime attached?
  - id: getHistory
    intent: Show past downtime occurrences
    question: When did downtimes last run for a service, and how long did they last?
  - id: listDowntimes
    intent: List configured downtimes
    question: What downtimes are currently configured in my project?
  - id: saveDowntime
    intent: Schedule a new downtime
    question: How do I schedule a maintenance window so alerts and SLOs pause for some services?
  phrasing_ops: 9
  slug: harness-downtime-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The DR Tests API from Harness — 1 operation(s) for dr tests.
  name: Harness DR Tests API
  phrasing_intents:
  - id: listDRTests
    intent: List disaster recovery tests
    question: Which disaster recovery tests have been set up in our pipelines?
  - id: createDRTest
    intent: Create a disaster recovery test pipeline
    question: Can I create a pipeline dedicated to disaster recovery testing?
  phrasing_ops: 2
  slug: harness-dr-tests-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: APIs to track drift between the last deployed manifest and the live cluster state
  name: Harness Drift Detection API
  phrasing_intents:
  - id: getDriftDetectionDetail
    intent: Get drift details for a deployed target
    question: Has a deployed service drifted from what Harness deployed?
  - id: listDriftDetectionTargets
    intent: List deployed targets tracked for drift
    question: Which service, environment and infrastructure combinations are tracked for drift in my project?
  phrasing_ops: 2
  slug: harness-drift-detection-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The enforcement API from Harness — 5 operation(s) for enforcement.
  name: Harness Enforcement API
  phrasing_intents:
  - id: getEnforcementSummary
    intent: Get an SBOM policy enforcement summary
    question: How many allow-list and deny-list violations did an SBOM enforcement run find?
  - id: getPolicyViolations
    intent: List policy violations from an enforcement
    question: Which components violated SBOM policy in a particular enforcement run?
  - id: getNormalisedSbomComponent
    intent: List normalized SBOM components for an artifact
    question: What components are in the normalized SBOM for an image?
  - id: saveEnforcementResult
    intent: Record a policy enforcement violation
    question: How does a pipeline record an individual component's policy violation?
  - id: saveEnforcementSummary
    intent: Record an enforcement run summary
    question: How is the overall result of an SBOM enforcement run stored?
  phrasing_ops: 5
  slug: harness-enforcement-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The enforcementV2 API from Harness — 1 operation(s) for enforcementv2.
  name: Harness Enforcement V2 API
  phrasing_intents:
  - id: enforceSbomV2
    intent: Enforce SBOM policies on an artifact
    question: Can I check an artifact's SBOM against my supply chain policies?
  phrasing_ops: 1
  slug: harness-enforcementv2-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: APIs for managing catalog Entities which represent the core components of your system. Entities can represent services, APIs, user groups, resources, and more. These endpoints allow you to create, ret
  name: Harness Entities API
  phrasing_intents:
  - id: create-entity
    intent: Create a catalog entity from YAML
    question: How do I register a new service in the catalog from its YAML definition?
  - id: get-entities
    intent: List catalog entities with filters
    question: Which catalog entities do I own across my projects?
  - id: submit-bulk-update-entity-field
    intent: Bulk-update one field across catalog entities
    question: Can I change the owner on many catalog entities at once?
  - id: get-bulk-update-entity-field-operation
    intent: Check a bulk field update's status
    question: Has my bulk owner change on the catalog finished yet?
  - id: get-entities-by-refs
    intent: Fetch catalog entities by their refs
    question: Can I look up several catalog entities at once from a list of entity references?
  - id: import-entity
    intent: Import a catalog entity from Git
    question: Can I import an existing entity YAML file from a Git repo into the catalog?
  - id: get-entities-groups
    intent: View catalog entities grouped by scope
    question: Can I see catalog entities organized by account, organization and project?
  - id: move-entity
    intent: Move an inline catalog entity to Git
    question: How do I move an inline catalog entity so it's stored in Git?
  phrasing_ops: 17
  slug: harness-entities-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The environment service for working with Environment-type infrastructures
  name: Harness Environment API
  phrasing_intents:
  - id: create-compile-and-execute-environment
    intent: Create, compile and run an IDP environment
    question: How do I spin up a new developer environment from an environment blueprint?
  - id: update-compile-and-execute-environment
    intent: Update and re-run an IDP environment
    question: How do I move an existing environment to a newer blueprint version?
  - id: delete-environment1
    intent: Delete an IDP environment
    question: How do I tear down a developer environment that's no longer active?
  - id: Environment#Compile
    intent: Compile an environment to infrastructure
    question: What infrastructure would my environment YAML compile to for a given target state?
  - id: Environment#Schemas
    intent: Get environment and blueprint schemas
    question: Where can I find the schema for writing environment and blueprint YAML?
  phrasing_ops: 5
  slug: harness-environment-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: APIs to create and manage Feature Flag Environment perspectives
  name: Harness Environment Perspectives API
  phrasing_intents:
  - id: DeletePerspective
    intent: Unlink the perspective from an environment
    question: How do I remove the perspective linked to an environment?
  - id: UpsertPerspective
    intent: Link a perspective to an environment
    question: How do I attach a perspective to a feature flag environment?
  phrasing_ops: 2
  slug: harness-environment-perspectives-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to EnvironmentGroup.
  name: Harness Environment Group API
  phrasing_intents:
  - id: postEnvironmentGroup
    intent: Create an environment group
    question: How do I group several environments together?
  - id: getEnvironmentGroup
    intent: Get an environment group
    question: Which environments are in a given environment group?
  - id: updateEnvironmentGroup
    intent: Update an environment group
    question: How do I change the YAML of an environment group?
  - id: deleteEnvironmentGroup
    intent: Delete an environment group
    question: How do I delete an environment group?
  - id: getEnvironmentGroupList
    intent: List environment groups
    question: What environment groups exist in my project?
  phrasing_ops: 5
  slug: harness-environmentgroup-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Environments
  name: Harness Environments API
  phrasing_intents:
  - id: checkAllowedValuesInEnvs
    intent: Check allowed-values usage in environments
    question: Do any of my Harness environments use allowed-values restrictions on their variables?
  - id: getEnvironmentList
    intent: List environments in a project
    question: Which deployment environments are defined in my Harness project?
  - id: updateEnvironmentV2
    intent: Update an existing environment
    question: How do I rename or re-describe an environment that already exists?
  - id: createEnvironmentV2
    intent: Create a new environment
    question: How do I add a new production or pre-production environment in Harness?
  - id: createEnvironmentsV2
    intent: Create many environments in one batch
    question: Can I create several environments at once and keep the ones that succeed?
  - id: getEnvironmentV2
    intent: Get one environment by identifier
    question: What is the configuration of a specific environment?
  - id: deleteEnvironmentV2
    intent: Delete an environment
    question: How do I delete an environment I no longer deploy to?
  - id: getServiceOverridesList
    intent: List service overrides for an environment
    question: Which service overrides are configured on a given environment?
  phrasing_ops: 15
  slug: harness-environments-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for EULA.
  name: Harness EULA API
  phrasing_intents:
  - id: sign-eula
    intent: Sign an end user license agreement
    question: How do I accept the Harness end user license agreement for a feature?
  - id: validate-eula-sign
    intent: Check whether a license agreement is signed
    question: Has our account already signed a given license agreement?
  phrasing_ops: 2
  slug: harness-eula-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Perform evaluations
  name: Harness Evaluate API
  phrasing_intents:
  - id: evaluate#evaluate
    intent: Evaluate a Rego policy against input
    question: Can I test an OPA Rego policy against sample JSON before saving it?
  phrasing_ops: 1
  slug: harness-evaluate-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Access evaluation results
  name: Harness Evaluations API
  phrasing_intents:
  - id: evaluations#list
    intent: List policy evaluations
    question: Which policy evaluations failed in my project recently?
  - id: evaluations#evaluation-input-signed-url
    intent: Get a download link for an evaluation's input
    question: How do I download the input that was evaluated when it was offloaded to storage?
  - id: evaluations#getYaml
    intent: Get an entity's YAML for policy evaluation
    question: Can I fetch the YAML of a pipeline or other entity that policies are evaluated against?
  - id: evaluations#find
    intent: Get a policy evaluation by ID
    question: Which policies passed or failed in one specific evaluation?
  phrasing_ops: 4
  slug: harness-evaluations-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Evidence Vault [Beta] API from Harness — 3 operation(s) for evidence vault [beta].
  name: Harness Evidence Vault [Beta] API
  phrasing_intents:
  - id: uploadAttestation
    intent: Upload a supply chain attestation
    question: How do I store a signed attestation in the evidence vault?
  - id: downloadAttestation
    intent: Download an attestation by digest
    question: How do I retrieve an attestation using its digest?
  - id: queryAttestationsGraphQL
    intent: Query attestations with GraphQL
    question: Can I search the evidence vault with a GraphQL query?
  phrasing_ops: 3
  slug: harness-evidence-vault-beta-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Example rego policies and corresponding input
  name: Harness Examples API
  phrasing_intents:
  - id: examples#list
    intent: List example policies
    question: Are there example policies I can start from?
  phrasing_ops: 1
  slug: harness-examples-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for execution config for image tags
  name: Harness Execution Config API
  phrasing_intents:
  - id: V1DeleteExecutionConfig
    intent: Delete my DB DevOps execution config overrides
    question: How do I drop all my custom DB DevOps image overrides?
  - id: V1GetCustomerConfig
    intent: Get my DB DevOps execution config
    question: Which DB DevOps images has my account overridden?
  - id: V1GetDefaultConfig
    intent: Get default DB DevOps images and tags
    question: What are the latest default DB DevOps image tags?
  - id: V1PinImage
    intent: Pin DB DevOps image versions
    question: How do I pin DB DevOps images to specific versions?
  - id: V1ResetExecutionConfig
    intent: Reset DB DevOps image tags to defaults
    question: Can I put overridden DB DevOps images back to their default tags?
  - id: V1UpdateExecutionConfig
    intent: Override DB DevOps image tags
    question: Can I override which image tag DB DevOps steps run with?
  phrasing_ops: 6
  slug: harness-execution-config-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: APIs for runtime execution input on pipeline steps and stages.
  name: Harness Execution Input API
  phrasing_intents:
  - id: getExecutionInputTemplate
    intent: Get the runtime input template for a step
    question: What inputs is a paused pipeline stage waiting for?
  - id: submitExecutionInput
    intent: Submit runtime inputs and resume a step
    question: How do I provide runtime inputs so a waiting pipeline continues?
  - id: createVariablesForPipelineExecution
    intent: List variables usable as expressions in a run
    question: Which variables can I reference as expressions during a pipeline run?
  phrasing_ops: 3
  slug: harness-execution-input-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The ExecutionLimits API from Harness — 1 operation(s) for executionlimits.
  name: Harness Execution Limits API
  phrasing_intents:
  - id: saveExecutionLimitsConfig
    intent: Save supply chain execution limits
    question: Can I update the execution limit configuration for supply chain security?
  phrasing_ops: 1
  slug: harness-executionlimits-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Executions Service handles the API for workflow executions. At this time it is a read-only API with no ability to directly create or edit executions. Instead these are triggered from the Workspaces Se
  name: Harness Executions API
  phrasing_intents:
  - id: executions#list-executions
    intent: List infrastructure executions in a project
    question: Which IaCM executions ran in a project for a given workspace?
  - id: executions#create-execution
    intent: Record a new infrastructure execution
    question: How do I register an execution for a workspace from a pipeline stage?
  - id: executions#show-execution
    intent: Show one infrastructure execution
    question: What happened in a specific pipeline stage's infrastructure execution?
  - id: executions#modify-execution
    intent: Add audit data to an execution
    question: Can I attach audit information to an existing infrastructure execution?
  - id: executions#list-cost-changes
    intent: List cost changes for an execution stage
    question: How much will this Terraform plan change my infrastructure cost?
  - id: executions#list-cost-changes-all-stages
    intent: List cost changes across all stages
    question: What's the total cost impact across every stage of a pipeline run?
  - id: executions#list-cost-changes-all-stages-by-modules
    intent: List cost changes per module across stages
    question: Which module is driving the cost increase in my execution?
  - id: executions#get-dependency-graph
    intent: Get an execution's dependency graph
    question: How are the modules in my infrastructure execution dependent on each other?
  phrasing_ops: 10
  slug: harness-executions-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Manage admin-defined rules that gate Exemption creation
  name: Harness Exemption Rules API
  phrasing_intents:
  - id: ExemptionRules#ListExemptionRules
    intent: List security exemption rules
    question: Which exemption rules are configured for security findings in my account?
  - id: ExemptionRules#CreateExemptionRule
    intent: Create a security exemption rule
    question: How do I set up a rule that governs how security issue exemptions are handled?
  - id: ExemptionRules#DeleteExemptionRule
    intent: Delete an exemption rule
    question: How do I remove an exemption rule entirely?
  - id: ExemptionRules#FindExemptionRuleById
    intent: Get one exemption rule
    question: What conditions and actions does a specific exemption rule have?
  - id: ExemptionRules#UpdateExemptionRule
    intent: Update an exemption rule
    question: How do I disable an existing exemption rule without deleting it?
  - id: ExemptionRules#GetExemptionConstraints
    intent: Get the strictest constraint for an exemption
    question: What constraints apply before I request an exemption for a security issue?
  phrasing_ops: 6
  slug: harness-exemptionrules-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Access and modify Exemptions to Security Issues
  name: Harness Exemptions API
  phrasing_intents:
  - id: Exemptions#ListExemptions
    intent: List security testing issue exemptions
    question: Which STO security issue exemptions exist in my Harness account?
  - id: Exemptions#CreateExemption
    intent: Request an exemption for a security issue
    question: How do I request an exemption for a vulnerability that STO flagged?
  - id: Exemptions#DeleteExemption
    intent: Delete a security issue exemption
    question: How do I remove an STO exemption so the issue blocks pipelines again?
  - id: Exemptions#FindExemptionById
    intent: Look up one security issue exemption
    question: What are the details and status of a single STO exemption by its ID?
  - id: Exemptions#UpdateExemption
    intent: Edit an existing security issue exemption
    question: Can I change the reason or expiration on an STO exemption I already requested?
  - id: Exemptions#ApproveExemption
    intent: Approve or reject a security issue exemption
    question: How do I approve a pending STO exemption request?
  - id: Exemptions#PromoteExemption
    intent: Promote an exemption to a higher scope
    question: Can I promote a project-level STO exemption so it applies across the org or account?
  - id: Exemptions#BulkCreateExemptions
    intent: Create many security issue exemptions at once
    question: Can I exempt many STO issues in a single request?
  phrasing_ops: 22
  slug: harness-exemptions-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Experiment Templates API from Harness — 7 operation(s) for experiment templates.
  name: Harness Experiment Templates API
  phrasing_intents:
  - id: listExperimentTemplate
    intent: List chaos experiment templates in a hub
    question: Which chaos experiment templates are available in my hub?
  - id: createExperimentTemplate
    intent: Create a chaos experiment template
    question: Can I add a new experiment template to a ChaosHub from a manifest?
  - id: getExperimentTemplate
    intent: Get a chaos experiment template
    question: What does a specific experiment template contain?
  - id: updateExperimentTemplate
    intent: Update a chaos experiment template
    question: How do I update an experiment template with a new manifest?
  - id: deleteExperimentTemplate
    intent: Delete a chaos experiment template
    question: How do I remove an experiment template from a hub?
  - id: compareExperimentTemplateRevisions
    intent: Compare two experiment template revisions
    question: What changed between two revisions of an experiment template?
  - id: createExperimentFromTemplate
    intent: Launch a chaos experiment from a template
    question: How do I create a runnable chaos experiment from a template?
  - id: getExperimentTemplateRevisions
    intent: List revisions of an experiment template
    question: What revisions exist for a given experiment template?
  phrasing_ops: 10
  slug: harness-experiment-templates-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Experiments API from Harness — 28 operation(s) for experiments.
  name: Harness Experiments API
  phrasing_intents:
  - id: GetChaosExperimentRunReport
    intent: Get the report for a Kubernetes chaos experiment run
    question: Can I pull a generated report for a finished kubernetesV1 chaos experiment run?
  - id: getExperimentRunsOverviewStats
    intent: Get chaos experiment run overview statistics
    question: How many chaos experiment runs passed or failed over the last month?
  - id: bulkExperimentDelete
    intent: Delete several chaos experiments at once
    question: Can I remove a batch of chaos experiments in one call instead of one by one?
  - id: bulkExperimentTagAdd
    intent: Add tags to several chaos experiments
    question: How do I tag many chaos experiments at the same time?
  - id: getChaosPipelineStepDetails
    intent: Get one step of a chaos pipeline execution
    question: What happened in a specific step of a chaos pipeline run?
  - id: getChaosPipelineExecution
    intent: Get the pipeline execution of a chaos experiment run
    question: Where can I see the whole pipeline execution behind a chaos experiment run?
  - id: listChaosV2Experiment
    intent: List chaos experiments in a project
    question: Which chaos experiments exist in my project?
  - id: saveChaosV2Experiment
    intent: Create or save a chaos experiment
    question: How do I create a new chaos experiment from a manifest?
  phrasing_ops: 34
  slug: harness-experiments-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Export and backup API from Harness — 1 operation(s) for export and backup.
  name: Harness Export and backup API
  phrasing_intents:
  - id: AgentServiceForServer_Export
    intent: Export a GitOps agent's setup
    question: Can I back up the applications, clusters and repositories behind a GitOps agent?
  phrasing_ops: 1
  slug: harness-export-and-backup-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Export License Usage Data By Account API from Harness — 1 operation(s) for export license usage data by account.
  name: Harness Export License Usage Data By Account API
  phrasing_intents:
  - id: export-license-usage-activity
    intent: Export license usage activity for an account
    question: Can I export license usage for my account over a date range?
  phrasing_ops: 1
  slug: harness-export-license-usage-data-by-account-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to External Data Provider Support for CACM
  name: Harness External Data Provider API
  phrasing_intents:
  - id: AddNewExternalDataFileMetadata
    intent: Register metadata for an external cost data file
    question: How do I record metadata for a cost file I uploaded from an external provider?
  - id: createExternalDataProvider
    intent: Create an external cost data provider
    question: How do I bring costs from a vendor that isn't a cloud provider into cloud cost management?
  - id: triggerDataIngestion
    intent: Start ingesting external cost data
    question: How do I kick off ingestion of an external provider's cost data for an invoice period?
  - id: CcmdeleteProvider
    intent: Delete an external data provider
    question: How do I remove an external cost data provider I no longer use?
  - id: updateFileMetaData
    intent: Update an external data file's metadata
    question: Can I correct the metadata on an external cost file I already registered?
  - id: deleteDatafileAndMetadata
    intent: Delete an external data file and its metadata
    question: How do I delete an uploaded external cost file along with its metadata?
  - id: getSignedUrl
    intent: Get a signed URL to upload external cost data
    question: Where do I upload an external provider's cost file for a given invoice period?
  - id: getProviders
    intent: List external data providers
    question: Which external cost data providers are set up in my account?
  phrasing_ops: 9
  slug: harness-external-data-provider-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Fault Templates API from Harness — 7 operation(s) for fault templates.
  name: Harness Fault Templates API
  phrasing_intents:
  - id: updateFault
    intent: Update a chaos fault
    question: How do I edit a chaos fault's inputs or spec after creating it?
  - id: deleteFault
    intent: Delete a chaos fault
    question: How do I remove a chaos fault I created?
  - id: listFaultTemplate
    intent: List fault templates in a ChaosHub
    question: Which chaos fault templates are available in a hub?
  - id: createFaultTemplate
    intent: Create a fault template in a hub
    question: How do I add a custom fault template to a ChaosHub?
  - id: getFaultTemplate
    intent: Get one fault template revision
    question: What does a specific fault template contain at a given revision?
  - id: updateFaultTemplate
    intent: Update a fault template in a hub
    question: Can I update a fault template that lives in a ChaosHub?
  - id: deleteFaultTemplate
    intent: Delete a fault template from a hub
    question: How do I remove a fault template from a ChaosHub?
  - id: compareFaultTemplateRevisions
    intent: Compare two revisions of a fault template
    question: What changed between two versions of a fault template?
  phrasing_ops: 11
  slug: harness-fault-templates-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Faults API from Harness — 7 operation(s) for faults.
  name: Harness Faults API
  phrasing_intents:
  - id: listFaultv2
    intent: List chaos faults in a project
    question: Which chaos faults are defined in my project?
  - id: createFault
    intent: Create a chaos fault
    question: How do I define a custom chaos fault?
  - id: getFault
    intent: Get a chaos fault from a project
    question: What does a particular chaos fault do and which infrastructures support it?
  - id: listExperimentRunsOfFault
    intent: List experiment runs that used a fault
    question: Which experiment runs have injected a given fault?
  - id: getFaultVariables
    intent: Get the inputs a chaos fault accepts
    question: What input variables can I tune on a chaos fault?
  - id: getFaultYaml
    intent: Get the YAML of a chaos fault
    question: Can I see the raw YAML definition of a fault?
  - id: listFault
    intent: List faults in a chaos hub
    question: Which faults are available in a chaos hub?
  - id: listFaultMetadata
    intent: List metadata for faults
    question: Can I get just the names and tags of faults, including all scopes?
  phrasing_ops: 8
  slug: harness-faults-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: APIs to create and manage Feature Flags
  name: Harness Feature Flags API
  phrasing_intents:
  - id: GetAllFeatures
    intent: List feature flags in a project
    question: What feature flags exist in my Harness project?
  - id: CreateFeatureFlag
    intent: Create a feature flag
    question: How do I create a new boolean feature flag with on and off variations?
  - id: DeleteFeatureFlag
    intent: Delete a feature flag
    question: Can I permanently delete a feature flag that's no longer used?
  - id: GetFeatureFlag
    intent: Get a feature flag
    question: What variations and default values does a specific feature flag have?
  - id: PatchFeature
    intent: Turn a feature flag on or off or change its rules
    question: How do I turn a feature flag on in production?
  - id: PutFeatureFlag
    intent: Replace a feature flag's definition
    question: Can I rewrite a flag's name, description and variations in one full update?
  - id: GetDependentFeatures
    intent: List flags that depend on a feature flag
    question: Which other flags use this flag as a prerequisite?
  - id: RestoreFeatureFlag
    intent: Restore an archived feature flag
    question: Can I bring back a feature flag that was archived?
  phrasing_ops: 8
  slug: harness-feature-flags-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to File Store in Harness
  name: Harness File Store API
  phrasing_intents:
  - id: listFilesAndFolders
    intent: List files and folders in the file store
    question: What files and folders are in my Harness file store?
  - id: create
    intent: Create a file or folder with content
    question: How do I upload a new config file into the file store?
  - id: createViaYAML
    intent: Create file or folder metadata from YAML
    question: Can I define a file store entry's metadata in YAML instead of a form?
  - id: getFile
    intent: Get a file or folder's metadata
    question: What metadata does the file store keep about one file?
  - id: update
    intent: Update a file or folder including content
    question: How do I replace the contents of a file already in the file store?
  - id: deleteFile
    intent: Delete a file or folder
    question: How do I delete a file from the file store?
  - id: downloadFile
    intent: Download a file from the file store
    question: How can I download a file I stored in Harness?
  - id: getCreatedByList
    intent: List users who created files
    question: Who has created files in our file store?
  phrasing_ops: 15
  slug: harness-file-store-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Filter as defined in Harness
  name: Harness Filter API
  phrasing_intents:
  - id: getFilterList
    intent: List saved platform filters
    question: Which saved filters exist in my Harness platform (NG) views for a given filter type?
  - id: updateFilter
    intent: Update a saved platform filter
    question: How do I change the criteria of a saved filter on the NG platform side?
  - id: postFilter
    intent: Save a new platform filter
    question: Can I save a reusable filter for the Harness platform list views?
  - id: getFilter
    intent: Get a saved platform filter's settings
    question: What criteria does a particular saved platform filter apply?
  - id: deleteFilter
    intent: Delete a saved platform filter
    question: How do I remove a saved filter I no longer use from the platform views?
  - id: PipelinegetFilterList
    intent: List saved pipeline filters
    question: Which saved filters do I have for pipeline and execution lists?
  - id: PipelineupdateFilter
    intent: Update a saved pipeline filter
    question: How do I edit the conditions of a saved filter on my pipelines list?
  - id: PipelinepostFilter
    intent: Save a new pipeline filter
    question: Can I save a filter so my pipeline executions list opens pre-filtered?
  phrasing_ops: 20
  slug: harness-filter-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Filter APIs API from Harness — 4 operation(s) for filter apis.
  name: Harness Filter APIs API
  phrasing_intents:
  - id: GetFilters
    intent: Get all commitment filter options
    question: What regions, instance families and provider accounts can I filter commitments by?
  - id: GetRegionFilters
    intent: List available regions for filtering
    question: Which AWS regions have usage I can filter on?
  - id: GetInstanceFamilyFilters
    intent: List available instance families
    question: Which instance families appear in my usage for filtering?
  - id: GetProviderAccountFilters
    intent: List cloud provider account IDs for filtering
    question: Which cloud provider account IDs can I filter by?
  phrasing_ops: 4
  slug: harness-filter-apis-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains the filter endpoint for Resource Groups.
  name: Harness Filter Resource Groups API
  phrasing_intents:
  - id: filter-resource-groups
    intent: Filter access-control resource groups
    question: Which resource groups exist in my org or project for access control?
  phrasing_ops: 1
  slug: harness-filter-resource-groups-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Filters API from Harness — 2 operation(s) for filters.
  name: Harness Filters API
  phrasing_intents:
  - id: FilterService_List
    intent: List saved GitOps filters
    question: Which saved filters do I have in GitOps?
  - id: FilterService_Create
    intent: Save a new GitOps filter
    question: Can I save a filter for my GitOps applications view?
  - id: FilterService_Update
    intent: Update a saved GitOps filter
    question: How do I change the conditions of a saved GitOps filter?
  - id: FilterService_Get
    intent: Get a saved GitOps filter
    question: What criteria does one of my GitOps filters hold?
  - id: FilterService_Delete
    intent: Delete a saved GitOps filter
    question: How do I remove a GitOps filter I don't use?
  phrasing_ops: 5
  slug: harness-filters-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The flyway API from Harness — 2 operation(s) for flyway.
  name: Harness Flyway API
  phrasing_intents:
  - id: V1FetchMigrationScriptSql
    intent: Fetch Flyway migration script SQL for a database
    question: Can I see the SQL of the Flyway migration scripts for a database instance?
  - id: V1GetFlywayDeployedState
    intent: Get the Flyway deployed state for an execution
    question: Which Flyway migrations were deployed in a pipeline run, compared with before?
  phrasing_ops: 2
  slug: harness-flyway-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The folders API from Harness — 2 operation(s) for folders.
  name: Harness Folders API
  phrasing_intents:
  - id: create_folder
    intent: Create a dashboard folder
    question: How do I create a folder to organise our custom dashboards?
  - id: get_folder
    intent: Get a dashboard folder
    question: What are the details of a particular dashboard folder?
  - id: update_folder
    intent: Rename a dashboard folder
    question: How do I rename a dashboard folder?
  - id: delete_folder
    intent: Delete a dashboard folder and its dashboards
    question: What happens to the dashboards inside a folder when I delete it?
  phrasing_ops: 4
  slug: harness-folders-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Agent ingest endpoints for the FP Triage agent's pre- and post-plugins
  name: Harness Fp Triage API
  phrasing_intents:
  - id: FpTriage#ListOccurrencesInScope
    intent: List security occurrences awaiting false-positive triage
    question: Which security issue occurrences in a project still need false-positive triage?
  - id: FpTriage#BatchUpsertVerdicts
    intent: Save a batch of false-positive triage verdicts
    question: How do I record false-positive verdicts for many security occurrences at once?
  phrasing_ops: 2
  slug: harness-fptriage-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Freeze API from Harness — 2 operation(s) for freeze.
  name: Harness Freeze API
  phrasing_intents:
  - id: RmgetFreezeList
    intent: List deployment freezes active in a time range
    question: Which deployment freezes are in effect during next week's release window?
  - id: getFreezeDetails
    intent: Get the details of a deployment freeze
    question: Which services and environments does a particular deployment freeze cover?
  phrasing_ops: 2
  slug: harness-freeze-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Freeze CRUD
  name: Harness Freeze CRUD API
  phrasing_intents:
  - id: createFreeze
    intent: Create a deployment freeze window
    question: How do I set up a deployment freeze so nothing ships during a release blackout?
  - id: getFreeze
    intent: Get a deployment freeze
    question: How do I view the configuration of a specific freeze window?
  - id: updateFreeze
    intent: Update a deployment freeze
    question: Can I change the window or scope of an existing freeze?
  - id: deleteFreeze
    intent: Delete a single deployment freeze
    question: How do I delete one freeze window?
  - id: deleteManyFreezes
    intent: Delete several deployment freezes at once
    question: Is there a bulk way to delete multiple freezes in one request?
  - id: getFreezeList
    intent: List deployment freezes
    question: Which deployment freezes are defined in my project?
  - id: getFrozenExecutionDetails
    intent: See which freezes blocked a pipeline execution
    question: My pipeline execution was frozen; which freeze stopped it?
  - id: getGlobalFreeze
    intent: Get the global freeze YAML
    question: Is there a global freeze in effect, and what does its YAML look like?
  phrasing_ops: 10
  slug: harness-freeze-crud-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Endpoints that power the STO micro-frontend
  name: Harness Frontend API
  phrasing_intents:
  - id: Frontend#AllIssuesFilters
    intent: List filter options for a project's security issues
    question: Which scanners, targets and severities can I filter a project's security issues by?
  - id: Frontend#AllIssuesList
    intent: List security issues from latest baseline scans
    question: What security issues were found in my project's latest baseline scans?
  - id: Frontend#AllIssuesDetails
    intent: Get a security issue's baseline scan details
    question: What are the full details of one security issue from the latest baseline scans?
  - id: Frontend#AllIssuesOccurrenceDetails
    intent: List an issue's occurrences on one target
    question: Where exactly does a security issue occur on a specific scan target?
  - id: Frontend#AllIssuesCountsV2
    intent: Count issues by severity and issue type
    question: How many security issues does my project have per severity level?
  - id: Frontend#AllIssuesTotalsV2
    intent: Get total issue and occurrence counts
    question: What is the overall number of issues and occurrences in a project, ignoring filters?
  - id: Frontend#AllIssuesListV2
    intent: List project issues from the summary table
    question: Is there a faster, pre-aggregated way to list all of a project's security issues?
  - id: Frontend#AllIssuesDetailsV2
    intent: Get issue details from the summary tables
    question: Can I fetch one issue's details from the pre-aggregated summary and detection data?
  phrasing_ops: 33
  slug: harness-frontend-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Get GenAI trace summaries and span waterfall data
  name: Harness GenAI Traces API
  phrasing_intents:
  - id: getGenAITraceSpans
    intent: Get the spans of a GenAI trace
    question: What individual spans make up a specific GenAI trace?
  - id: listGenAITraceServices
    intent: List GenAI services seen in traces
    question: Which GenAI services has Harness observed over the last year?
  - id: listGenAITraceSummaries
    intent: List GenAI trace summaries
    question: Can I browse summaries of recent GenAI traces for cost analysis?
  phrasing_ops: 3
  slug: harness-genai-traces-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Get Module Access API from Harness — 1 operation(s) for get module access.
  name: Harness Get Module Access API
  phrasing_intents:
  - id: get-v1-moduleAccess
    intent: Check a user's access to a module
    question: Does a given user have access to a particular Harness module?
  phrasing_ops: 1
  slug: harness-get-module-access-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Contains APIs related to Git Sync Branch
  name: Harness Git Branches API
  phrasing_intents:
  - id: syncGitBranch
    intent: Sync a new Git branch into Harness
    question: I created a new branch — how do I pull its content into Harness with old Git Sync?
  - id: getListOfBranchesWithStatus
    intent: List Git Sync branches and their sync status
    question: Which branches of my Git Sync repo are synced and which aren't?
  phrasing_ops: 2
  slug: harness-git-branches-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Contains APIs related to Git Full Sync
  name: Harness Git Full Sync API
  phrasing_intents:
  - id: getGitFullSyncConfig
    intent: Get the Git full sync configuration
    question: Which repo and branch is full Git sync configured to use?
  - id: updateGitFullSyncConfig
    intent: Update the Git full sync configuration
    question: How do I change the branch or folder full sync writes to?
  - id: createGitFullSyncConfig
    intent: Set up Git full sync for a scope
    question: How do I set up full sync of Harness entities to a Git repo for the first time?
  - id: listFullSyncFiles
    intent: List files in a Git full sync with status
    question: Which files failed during the last full Git sync?
  - id: triggerFullSync
    intent: Start a Git full sync
    question: How do I kick off a full sync of my entities to Git?
  phrasing_ops: 5
  slug: harness-git-full-sync-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Contains APIs for CRUD on Git Sync
  name: Harness Git Sync API
  phrasing_intents:
  - id: getGitSyncConfigList
    intent: List Git Sync configurations
    question: Which Git repositories are configured for Git Sync in my project?
  - id: updateGitSyncConfig
    intent: Update a Git Sync configuration
    question: Can I switch an existing Git Sync config to a different branch?
  - id: createGitSyncConfig
    intent: Create a Git Sync configuration
    question: How do I connect a Git repo so Harness entities sync to it?
  - id: isGitSyncEnabled
    intent: Check whether Git Sync is enabled
    question: Is Git Sync turned on for my project?
  - id: updateDefaultFolder
    intent: Set the default root folder for Git Sync
    question: Can I change which folder in the repo Git Sync uses by default?
  phrasing_ops: 5
  slug: harness-git-sync-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Contains APIs related to Git Sync Errors
  name: Harness Git Sync Errors API
  phrasing_intents:
  - id: getGitSyncErrorsCount
    intent: Count Git sync errors for a repo and branch
    question: How many Git sync errors do we have on a branch?
  - id: listGitSyncErrors
    intent: List Git sync errors by file or connectivity
    question: Which files failed to sync from Git into Harness?
  - id: listGitToHarnessErrorForCommit
    intent: List Git sync errors for a commit
    question: What sync errors did a specific commit cause?
  - id: listGitToHarnessErrorsGroupedByCommits
    intent: List Git sync errors grouped by commit
    question: Which commits have Git sync errors and how many each?
  phrasing_ops: 4
  slug: harness-git-sync-errors-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Contains APIs related to Git Sync Settings
  name: Harness Git Sync Settings API
  phrasing_intents:
  - id: getGitSyncSettings
    intent: Get Git Sync settings for a scope
    question: What Git Sync settings apply to my project?
  - id: updateGitSyncSetting
    intent: Change the Git Sync connectivity mode
    question: Can I switch Git Sync to connect through a delegate instead of the platform?
  - id: createGitSyncSetting
    intent: Create Git Sync settings for a scope
    question: How do I turn on Git Sync settings for a new project?
  phrasing_ops: 3
  slug: harness-git-sync-settings-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The GitX Events Resource API from Harness — 1 operation(s) for gitx events resource.
  name: Harness GitX Events Resource API
  phrasing_intents:
  - id: list-webhook-event-branches
    intent: List branches seen in GitX webhook events
    question: Which branches have GitX webhook events?
  phrasing_ops: 1
  slug: harness-gitx-events-resource-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The GitX Webhook Event API from Harness — 1 operation(s) for gitx webhook event.
  name: Harness GitX Webhook Event API
  phrasing_intents:
  - id: patch-gitx-webhook-events-gitx-webhook-event
    intent: Update a Git webhook event's status
    question: How do I change the status of a Git Experience webhook event?
  phrasing_ops: 1
  slug: harness-gitx-webhook-event-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Account GitX Webhooks.
  name: Harness GitX Webhooks API
  phrasing_intents:
  - id: create-gitx-webhook
    intent: Create an account-level GitX webhook
    question: How do I set up a GitX webhook so Harness syncs entities from my Git repo?
  - id: list-gitx-webhooks
    intent: List account-level GitX webhooks
    question: Which GitX webhooks are configured at the account level?
  - id: get-gitx-webhook
    intent: Get an account-level GitX webhook
    question: How do I see the repo and folders a GitX webhook is watching?
  - id: update-gitx-webhook
    intent: Update an account-level GitX webhook
    question: Can I disable a GitX webhook without deleting it?
  - id: delete-gitx-webhook
    intent: Delete an account-level GitX webhook
    question: How do I remove a GitX webhook from my account?
  - id: list-gitx-webhook-events
    intent: List account-level GitX webhook events
    question: What Git push events have my account's GitX webhooks received?
  phrasing_ops: 6
  slug: harness-gitx-webhooks-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The GitX Webhooks Event File Validation API from Harness — 1 operation(s) for gitx webhooks event file validation.
  name: Harness GitX Webhooks Event File Validation API
  phrasing_intents:
  - id: gitx-webhook-event-file-validation
    intent: Get file validations for a Git webhook event
    question: Which files failed validation when a Git webhook event was processed?
  phrasing_ops: 1
  slug: harness-gitx-webhooks-event-file-validation-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The GnuPGP Keys API from Harness — 2 operation(s) for gnupgp keys.
  name: Harness GnuPGP Keys API
  phrasing_intents:
  - id: AgentGPGKeyService_Create
    intent: Add GPG public keys to a GitOps agent
    question: How do I add a GPG public key so my GitOps agent can verify signed commits?
  - id: AgentGPGKeyService_Get
    intent: Get a GPG public key on a GitOps agent
    question: What information does the agent hold about a specific GPG key?
  - id: AgentGPGKeyService_Delete
    intent: Remove a GPG public key from a GitOps agent
    question: How do I remove a GPG key from my GitOps agent's configuration?
  phrasing_ops: 3
  slug: harness-gnupgp-keys-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs specific to Google Secret Manager Connector as defined in Harness
  name: Harness Google Secret Manager Connector API
  phrasing_intents:
  - id: getGcpRegions
    intent: List GCP regions for a Secret Manager connector
    question: Which GCP regions can I choose when setting up a Google Secret Manager connector?
  phrasing_ops: 1
  slug: harness-googlesecretmanagerconnector-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Governance Alert Management
  name: Harness Governance Alert API
  phrasing_intents:
  - id: CloneGovernanceAlertRule
    intent: Clone a governance alert rule
    question: Can I duplicate an existing cloud governance alert rule?
  - id: UpdateGovernanceAlertRule
    intent: Edit a governance alert rule
    question: How do I change who gets emailed by a governance alert rule?
  - id: CreateNewGovernanceAlertRule
    intent: Create a governance alert rule
    question: What's needed to get emailed when cloud governance flags resources?
  - id: DeleteGovernanceAlertRule
    intent: Delete a governance alert rule
    question: How do I permanently remove a governance alert rule?
  - id: GovernanceAlertRules
    intent: List governance alert rules
    question: Which governance alert rules are set up in my account?
  - id: GovernanceResourceTypes
    intent: List resource types governance supports
    question: Which resource types can governance alerts watch for a given cloud?
  - id: ToggleGovernanceAlertRule
    intent: Enable or disable a governance alert rule
    question: Can I pause a governance alert rule without deleting it?
  phrasing_ops: 7
  slug: harness-governance-alert-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to CACM Governance Enforcement Recommendations
  name: Harness Governance Enforcement Recommendation APIs API
  phrasing_intents:
  - id: acceptEnforcementRecommendations
    intent: Accept governance enforcement recommendations
    question: How do I accept suggested governance rule enforcements for my cloud accounts?
  - id: dismissEnforcementRecommendations
    intent: Dismiss governance enforcement recommendations
    question: How do I dismiss governance enforcement suggestions I don't want?
  - id: enforcementRecommendationDetails
    intent: Get an enforcement recommendation's details
    question: What rules, accounts and schedule does a governance enforcement recommendation propose?
  - id: ruleEnforcementRecommendations
    intent: List enforcement recommendations by search key
    question: Which governance enforcement recommendations are open for my account?
  - id: listRuleEnforcementRecommendations
    intent: Filter enforcement recommendations by rules and targets
    question: Can I filter enforcement recommendations by rule IDs, target accounts and regions?
  - id: updateEnforcementRecommendation
    intent: Edit an enforcement recommendation
    question: How do I adjust the schedule or target regions of an enforcement recommendation?
  phrasing_ops: 6
  slug: harness-governance-enforcement-recommendation-apis-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to CACM Governance Overview Page
  name: Harness Governance Overview API
  phrasing_intents:
  - id: dayWiseTotalEvaluations
    intent: Chart daily governance evaluations by status
    question: How many cloud governance evaluations ran each day, broken down by status?
  - id: totalNewEnforcementRecommendations
    intent: Count new enforcement recommendations
    question: How many new governance enforcement recommendations are waiting for us?
  - id: totalActiveEnforcements
    intent: Count active governance enforcements
    question: How many governance enforcements are currently active?
  - id: totalEvaluations
    intent: Count total governance evaluations
    question: What is the overall number of governance rule evaluations to date?
  - id: totalRealisedSavingsV2
    intent: Get total realised governance savings
    question: How much money has cloud asset governance saved us overall?
  - id: totalRealisedSavingsGrouped
    intent: Break down realised savings by cloud or resource type
    question: Which resource types contributed most to our governance savings?
  phrasing_ops: 6
  slug: harness-governance-overview-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to CACM Governance Recommendations
  name: Harness Governance Recommendation APIs API
  phrasing_intents:
  - id: recommendationHealth
    intent: Get recommendation health for a governance rule
    question: How healthy are the cost recommendations produced by one governance rule?
  - id: getRuleRecommendation
    intent: Get a governance recommendation
    question: What are the details of a specific cloud governance recommendation?
  - id: listGovernanceRecommendationHealth
    intent: List recommendation health across governance rules
    question: Which governance rules have unhealthy recommendations right now?
  phrasing_ops: 3
  slug: harness-governance-recommendation-apis-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The GPG Keys API from Harness — 1 operation(s) for gpg keys.
  name: Harness GPG Keys API
  phrasing_intents:
  - id: GnuPGKeyService_ListGPGKeys
    intent: List GitOps GPG public keys
    question: Which GPG public keys are registered for GitOps commit verification?
  phrasing_ops: 1
  slug: harness-gpg-keys-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Groups
  name: Harness Groups API
  phrasing_intents:
  - id: get-group-details
    intent: Get the details of one group
    question: What does a specific group in my Harness account contain?
  - id: delete-group
    intent: Delete a group
    question: How do I delete a group I no longer need?
  - id: get-all-groups-for-account
    intent: List all groups in the account
    question: Which groups exist across my whole account?
  - id: save-group
    intent: Save a new group
    question: How do I create a new group in my account?
  - id: update-groups
    intent: Update groups in bulk
    question: Can I update several groups in one request?
  - id: get-groups-yaml
    intent: Get the groups definition as YAML
    question: Can I export my groups configuration as YAML?
  - id: get-workflows-for-account
    intent: List workflows in the account
    question: Which workflows are available in my account to put into groups?
  phrasing_ops: 7
  slug: harness-groups-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs specific to the Harness Resource Group
  name: Harness Harness Resource Group API
  phrasing_intents:
  - id: getResourceGroupListV2
    intent: List resource groups
    question: Which resource groups exist in my account or project?
  - id: createResourceGroupV2
    intent: Create a resource group
    question: How do I create a resource group to scope access control?
  - id: getResourceGroupV2
    intent: Get a resource group
    question: What resources are included in a particular resource group?
  - id: updateResourceGroupV2
    intent: Update a resource group
    question: Can I add more resources to an existing resource group?
  - id: deleteResourceGroupV2
    intent: Delete a resource group
    question: How do I delete a resource group?
  - id: getFilterResourceGroupListV2
    intent: Filter resource groups by criteria
    question: Can I find resource groups that include a specific resource type?
  phrasing_ops: 6
  slug: harness-harness-resource-group-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Harness Resource Type
  name: Harness Harness Resource Type API
  phrasing_intents:
  - id: getResourceTypes
    intent: List resource types available for access control
    question: Which resource types can I use in roles and resource groups at this scope?
  phrasing_ops: 1
  slug: harness-harness-resource-type-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Harness DataPoints Information
  name: Harness Harness Data Points API
  phrasing_intents:
  - id: get-harness-data-point-values
    intent: Get values for Harness data source data points
    question: How do I fetch data point values from the Harness data source for scorecards?
  phrasing_ops: 1
  slug: harness-harnessdatapoints-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Health API from Harness — 2 operation(s) for health.
  name: Harness Health API
  phrasing_intents:
  - id: healthCheckV3
    intent: Check the health of the chaos service
    question: Is the chaos engineering service up and healthy?
  - id: getExperimentHelperImageVersion
    intent: Get the experiment helper image version
    question: Which helper image version do chaos experiments currently use?
  phrasing_ops: 2
  slug: harness-health-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to CV Health Sources
  name: Harness Healthsources API
  phrasing_intents:
  - id: listHealthSources
    intent: List health sources
    question: Which monitoring health sources are configured in my project?
  - id: updateHealthSource
    intent: Update a health source
    question: How do I change the queries a health source runs?
  - id: createHealthSource
    intent: Create a health source
    question: Can I add a new metrics or logs source for deployment verification?
  - id: getHealthSource
    intent: Get a health source
    question: What queries and connector does a given health source use?
  - id: deleteHealthSource
    intent: Delete a health source
    question: Is it possible to remove a health source we no longer monitor?
  - id: getHealthSourceRuntimeInputs
    intent: Get runtime inputs for a health source
    question: Which values in a health source have to be supplied at runtime?
  phrasing_ops: 6
  slug: harness-healthsources-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: APIs to get details of helm artifacts
  name: Harness Helm Artifacts API
  phrasing_intents:
  - id: GetHelmArtifactDetails
    intent: Get details of a Helm chart version
    question: What details are stored for a Helm chart version in my artifact registry?
  - id: GetHelmArtifactManifest
    intent: Get the manifest of a Helm chart version
    question: Can I view the manifest of a Helm chart in the registry?
  phrasing_ops: 2
  slug: harness-helm-artifacts-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Home Page Layout
  name: Harness Home Page Layout API
  phrasing_intents:
  - id: get-home-page-layout-info
    intent: Get the home page layout
    question: What cards and quick links are on my account's home page layout?
  - id: save-home-page-layout-info
    intent: Save the home page layout
    question: How do I customize the cards on my Harness home page?
  - id: get-yaml-for-home-page-layout
    intent: Export the home page layout as YAML
    question: Can I get the home page layout as YAML for version control?
  - id: delete-custom-link-card-quick-links
    intent: Delete a quick link icon on a custom card
    question: Can I remove the icon from a quick link inside a custom home page card?
  - id: delete-headers-quick-links-icon
    intent: Delete a header quick link icon
    question: Can I remove the icon from a quick link in the home page header?
  - id: delete-home-page-layout-cards-icon
    intent: Delete a home page card icon
    question: Can I remove the icon shown on a home page card?
  - id: delete-home-page-layout-icon
    intent: Delete the home page layout icon
    question: Can I delete the main icon used on my home page layout?
  phrasing_ops: 7
  slug: harness-homepagelayout-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Hosts as defined in Harness
  name: Harness Hosts API
  phrasing_intents:
  - id: filterHostsByConnector
    intent: List hosts behind an infrastructure connector
    question: Which hosts does a physical data center or cloud connector expose?
  - id: validateHosts_1
    intent: Validate connectivity credentials for hosts
    question: Can Harness reach my hosts with the credentials I configured?
  phrasing_ops: 2
  slug: harness-hosts-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Incident Response API from Harness — 1 operation(s) for incident response.
  name: Harness Incident Response API
  phrasing_intents:
  - id: sloNotificationTrigger
    intent: Trigger an incident notification for an SLO
    question: How do I raise an incident response notification when an SLO is breached?
  phrasing_ops: 1
  slug: harness-incident-response-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The infrastructure service for working with infrastructures
  name: Harness Infrastructure API
  phrasing_intents:
  - id: Infrastructure#List
    intent: List infrastructures
    question: What infrastructures have been defined in my account?
  - id: Infrastructure#Abort
    intent: Abort an infrastructure execution
    question: How do I stop an infrastructure execution that's still running?
  - id: Infrastructure#Delete
    intent: Delete an infrastructure
    question: How do I remove an infrastructure I no longer need?
  - id: Infrastructure#Get
    intent: Get an infrastructure
    question: What's the definition of one specific infrastructure?
  - id: Infrastructure#ListExecutions
    intent: List executions of an infrastructure
    question: What runs have been executed against a given infrastructure?
  - id: Infrastructure#ListSpecs
    intent: List specs of an infrastructure
    question: Which specs make up a particular infrastructure?
  - id: Infrastructure#ApprovePipelineExecution
    intent: Approve or reject a pipeline approval step
    question: How do I respond to an approval step that's blocking an infrastructure pipeline?
  - id: Infrastructure#Execute
    intent: Execute an infrastructure definition
    question: How do I run an infrastructure YAML to provision resources?
  phrasing_ops: 9
  slug: harness-infrastructure-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Infrastructure Definitions
  name: Harness Infrastructures API
  phrasing_intents:
  - id: getInfrastructureList
    intent: List infrastructure definitions in an environment
    question: Which infrastructure definitions exist in a given environment?
  - id: updateInfrastructure
    intent: Update an infrastructure definition
    question: Can I change an existing infrastructure definition's YAML or name?
  - id: createInfrastructure
    intent: Create an infrastructure in an environment
    question: How do I define where a service deploys inside an environment?
  - id: getInfrastructure
    intent: Get an infrastructure definition
    question: What is configured in one infrastructure definition?
  - id: deleteInfrastructure
    intent: Delete an infrastructure definition
    question: How do I remove an infrastructure definition from an environment?
  - id: importInfrastructure
    intent: Import an infrastructure from Git
    question: Can I create an infrastructure from a YAML file that already lives in my Git repo?
  - id: moveInfraConfigs
    intent: Move an infrastructure YAML to Git
    question: Can I move an inline infrastructure definition into a remote Git repository?
  - id: updateInfrastructureGitDetails
    intent: Update Git metadata of a remote infrastructure
    question: Can I point a remote infrastructure at a different repo or file path?
  phrasing_ops: 8
  slug: harness-infrastructures-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Input Sets.
  name: Harness Input Sets API
  phrasing_intents:
  - id: create-input-set
    intent: Create an input set for a pipeline
    question: How do I save a reusable set of runtime inputs for a pipeline?
  - id: list-input-sets
    intent: List a pipeline's input sets
    question: Which input sets are saved for one of my pipelines?
  - id: get-input-set
    intent: Retrieve an input set
    question: What runtime values does a particular input set supply to my pipeline?
  - id: update-input-set
    intent: Update an input set
    question: How do I change the values stored in an existing input set?
  - id: delete-input-set
    intent: Delete an input set
    question: How do I remove an input set I no longer need from a pipeline?
  - id: inputSetsMoveConfig
    intent: Move an inline input set to Git
    question: How do I move an input set stored inline in Harness into a Git repository?
  - id: importInputSetFromGit
    intent: Import an input set from a Git repository
    question: Can I import an input set YAML that already lives in my Git repo?
  - id: update-input-set-git-metadata
    intent: Update Git metadata of a remote input set
    question: How do I point a remote input set at a different repo or file path?
  phrasing_ops: 9
  slug: harness-input-sets-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Inputs API from Harness — 1 operation(s) for inputs.
  name: Harness Inputs API
  phrasing_intents:
  - id: get-pipeline-inputs
    intent: Get the runtime inputs a pipeline expects
    question: What runtime inputs do I need to supply before running this pipeline?
  phrasing_ops: 1
  slug: harness-inputs-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Insights Service lists insights for a workspace.
  name: Harness Insights API
  phrasing_intents:
  - id: insights#list-insights
    intent: List cost insights for a workspace
    question: Are there cost-optimization suggestions for my infrastructure workspace?
  phrasing_ops: 1
  slug: harness-insights-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The instance service for working with instances
  name: Harness Instance API
  phrasing_intents:
  - id: Instance#List
    intent: List infrastructure instances
    question: Which instances are running on my infrastructure?
  - id: Instance#Get
    intent: Get one infrastructure instance
    question: What state is a particular instance in?
  - id: Instance#ForceState
    intent: Force an instance into a given state
    question: Can I manually force an instance into a specific state?
  - id: Instance#ListEvents
    intent: List events for an instance
    question: What events have been recorded for a specific instance?
  - id: Instance#GetEvent
    intent: Get one instance event
    question: What happened in a specific instance event?
  phrasing_ops: 5
  slug: harness-instance-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The integration API from Harness — 6 operation(s) for integration.
  name: Harness Integration API
  phrasing_intents:
  - id: GetIntegration
    intent: Find an integration ID by GitHub org URL
    question: What's the integration ID for my GitHub organization?
  - id: listIntegrations
    intent: List supply chain integrations
    question: What source code integrations are set up in my project?
  - id: createIntegration
    intent: Create a supply chain integration
    question: How do I connect a GitHub app installation as an integration?
  - id: fetchReposInIntegration
    intent: Fetch all repos visible to a GitHub app integration
    question: Which repositories can the GitHub app see through this integration?
  - id: getIntegrationRepos
    intent: Get the repos configured in an integration
    question: Which repos have already been configured in an integration?
  - id: configureRepos
    intent: Set the repos an integration covers
    question: How do I choose exactly which repositories an integration covers?
  - id: addRepos
    intent: Add more repos to an integration
    question: Can I add repositories to an integration without replacing the existing ones?
  - id: deleteIntegration
    intent: Delete a supply chain integration
    question: How do I remove an integration from a project?
  phrasing_ops: 9
  slug: harness-integration-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Integration Step Config API from Harness — 3 operation(s) for integration step config.
  name: Harness Integration Step Config API
  phrasing_intents:
  - id: setIntegrationStepConfig
    intent: Set the integration step config for the account
    question: How do I set a supply chain integration step config for my whole account?
  - id: setIntegrationStepConfigForOrgProject
    intent: Set the integration step config for a project
    question: Can one project have its own integration step config?
  - id: setIntegrationStepConfigForOrg
    intent: Set the integration step config for an org
    question: Can I set integration step config at the organization level?
  phrasing_ops: 3
  slug: harness-integration-step-config-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The integrationConfig API from Harness — 1 operation(s) for integrationconfig.
  name: Harness Integration Config API
  phrasing_intents:
  - id: getIntegrationsConfig
    intent: Get the configuration for an integration type
    question: What settings does a given integration type use?
  phrasing_ops: 1
  slug: harness-integrationconfig-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Integrations
  name: Harness Integrations API
  phrasing_intents:
  - id: get-integrations
    intent: List integrations of a given type
    question: What integrations of a certain type are set up in my Harness account?
  - id: create-integration
    intent: Create a new integration
    question: How do I add a new integration of a particular type?
  - id: delete-integrations
    intent: Delete integrations of a given type
    question: How do I remove the integrations of a particular type from my account?
  - id: get-integration
    intent: Get one integration's details
    question: What is configured for a specific integration by its ID?
  - id: update-integration
    intent: Update an integration's configuration
    question: How do I change the settings of an existing integration?
  - id: discover-entities
    intent: List entities discovered by an integration
    question: What catalog entities has an integration discovered so far?
  - id: save-discover-entities
    intent: Import discovered entities from an integration
    question: How do I save the entities an integration discovered into my catalog?
  - id: unlinkIntegrationEntities
    intent: Unlink entities from an integration
    question: How do I detach catalog entities from the integration that imported them?
  phrasing_ops: 8
  slug: harness-integrations-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Invite as defined in Harness
  name: Harness Invite API
  phrasing_intents:
  - id: updateInvite
    intent: Resend a user invite email
    question: A teammate never got their Harness invite; can I resend it?
  - id: deleteInvite
    intent: Revoke a pending invite
    question: How do I cancel an invitation I sent by mistake?
  - id: getInvite
    intent: Look up an invite by id or token
    question: Can I look up an invite from the JWT token in the invite link?
  - id: getInvites
    intent: List invites for a project or organization
    question: Which invitations have been sent for my project?
  - id: getPendingUsersAggregated
    intent: List users with pending invites in a scope
    question: Who has been invited but hasn't accepted yet?
  phrasing_ops: 5
  slug: harness-invite-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for IP Allowlist.
  name: Harness IP Allowlist API
  phrasing_intents:
  - id: create-ip-allowlist-config
    intent: Create an IP allowlist configuration
    question: How do I restrict access to my Harness account to a set of IP ranges?
  - id: get-ip-allowlist-configs
    intent: List IP allowlist configurations
    question: Which IP allowlist configurations are set up on my Harness account?
  - id: get-ip-allowlist-config
    intent: Get one IP allowlist configuration
    question: What IP range and status does a specific allowlist config have?
  - id: update-ip-allowlist-config
    intent: Update an IP allowlist configuration
    question: How do I change the IP range on an existing allowlist config?
  - id: delete-ip-allowlist-config
    intent: Delete an IP allowlist configuration
    question: How do I remove an IP allowlist entry from my account?
  - id: validate-unique-ip-allowlist-config-identifier
    intent: Check an allowlist identifier is unique
    question: Is an IP allowlist identifier already taken before I create a new config?
  - id: validate-ip-address-allowlisted-or-not
    intent: Test an IP against allowlists or a custom block
    question: Does a given IP address fall inside a specific CIDR block I provide?
  - id: allowed-ip-address
    intent: Check if an IP address is allowed
    question: Will requests from this IP address be allowed into my Harness account?
  phrasing_ops: 8
  slug: harness-ip-allowlist-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Access and modify Security Issues
  name: Harness Issues API
  phrasing_intents:
  - id: Issues#ListIssues
    intent: List security issues
    question: Which security issues have scanners found in my account?
  - id: Issues#CreateIssue
    intent: Record a new security issue from a scan
    question: How do I record a vulnerability found by a scan as a security issue?
  - id: Issues#DeleteIssue
    intent: Delete a security issue
    question: How do I remove a security issue that was recorded by mistake?
  - id: Issues#FindIssueById
    intent: Get a security issue
    question: What are the details and severity of a specific security issue?
  - id: Issues#UpdateIssue
    intent: Update a security issue's occurrences
    question: How do I update the occurrences of an existing security issue after a new scan?
  - id: Issues#IssuesAugmentRemediation
    intent: Generate AI remediation steps for a security issue
    question: Can AI suggest remediation steps or a code fix for a security issue?
  phrasing_ops: 6
  slug: harness-issues-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Health related metadata for your k8S clusters having cost access enabled.
  name: Harness K8S Connectors Metadata API
  phrasing_intents:
  - id: ccmK8sMeta
    intent: Get cost metadata for Kubernetes connectors
    question: What cost management metadata exists for my Kubernetes connectors?
  phrasing_ops: 1
  slug: harness-k8s-connectors-metadata-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Fetching Release details regarding a pod.
  name: Harness K8s Release Service Mapping API
  phrasing_intents:
  - id: get-v1-releaseDetails
    intent: Look up services mapped to Kubernetes releases
    question: Which Harness service and environment does a pod's namespace and release name belong to?
  - id: post-v1-releaseDetails
    intent: Map namespaces and releases to services in bulk
    question: Can I post a batch of namespace and release names to resolve their services and environments?
  phrasing_ops: 2
  slug: harness-k8s-release-service-mapping-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Keys as defined in Harness
  name: Harness Keys API
  phrasing_intents:
  - id: ListAggregatedKeys
    intent: List SSH and PGP keys
    question: Which SSH and PGP keys are stored in my account?
  - id: createKey
    intent: Create an SSH or PGP key
    question: How do I add a PGP key instead of the default SSH key?
  - id: updateKey
    intent: Change a key's validity or revoke it
    question: How do I revoke a compromised PGP key?
  - id: deleteKey
    intent: Delete an SSH or PGP key
    question: Can I delete a key I no longer use?
  phrasing_ops: 4
  slug: harness-keys-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Kinds.
  name: Harness Kinds API
  phrasing_intents:
  - id: create-kind
    intent: Create a custom catalog kind
    question: How do I define a new kind of entity for the catalog?
  - id: get-kinds
    intent: List catalog entity kinds
    question: What entity kinds exist in my software catalog?
  - id: update-kind
    intent: Update a catalog kind
    question: Can I change the schema of a kind that's already in use?
  - id: delete-kind
    intent: Delete a catalog kind
    question: How do I remove a custom kind from the catalog?
  - id: get-kind
    intent: Get a catalog kind
    question: How is a specific entity kind defined?
  - id: get-kind-schema
    intent: Get the meta-schema for defining kinds
    question: What schema format do kind definitions have to follow?
  - id: kind-schema-validate
    intent: Validate a kind schema
    question: Can I check my kind schema is valid before I create the kind?
  phrasing_ops: 7
  slug: harness-kinds-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Kubernetes DataPoints Information
  name: Harness Kubernetes Data Points API
  phrasing_intents:
  - id: get-k8s-data-point-values
    intent: Get Kubernetes data point values for scorecards
    question: What values does the Kubernetes data source return for my scorecard checks?
  phrasing_ops: 1
  slug: harness-kubernetesdatapoints-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The labels API from Harness — 10 operation(s) for labels.
  name: Harness Labels API
  phrasing_intents:
  - id: listSpaceLabels
    intent: List labels defined for an account, org or project
    question: What labels are defined for my Harness Code project?
  - id: defineSpaceLabel
    intent: Create a new label at account, org or project level
    question: How do I create a new pull request label that every repo in my project can use?
  - id: saveSpaceLabel
    intent: Save a label and its values in one call at a scope
    question: Can I create or overwrite a project label together with all its values in a single request?
  - id: deleteSpaceLabel
    intent: Delete a label defined at account, org or project
    question: Can I remove a label that was defined for the whole project rather than one repo?
  - id: updateSpaceLabel
    intent: Update an account, org or project label
    question: Can I rename or recolor a label that's shared across my whole project?
  - id: listSpaceLabelValues
    intent: List the values of a project, org or account label
    question: What values are allowed for a label defined at the project level?
  - id: defineSpaceLabelValue
    intent: Add a value to an account, org or project label
    question: Can I add a new option to an existing project-wide label?
  - id: deleteSpaceLabelValue
    intent: Delete a value from an account, org or project label
    question: Can I remove one option from a project-wide label without deleting the label itself?
  phrasing_ops: 21
  slug: harness-labels-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Layout Proxy
  name: Harness Layout Proxy API
  phrasing_intents:
  - id: get-all-layouts
    intent: List portal layouts
    question: Which page layouts are configured in my developer portal?
  - id: create-layout
    intent: Create a portal layout
    question: Can I add a new page layout to the portal from YAML?
  - id: delete-layout
    intent: Delete a portal layout
    question: Can I remove a layout from the portal?
  - id: get-layout
    intent: Get a portal layout
    question: What does a particular layout's configuration look like?
  - id: get-layout-health
    intent: Check layout service health
    question: Is the layout service healthy?
  - id: layout-ingest
    intent: Ingest a plugin layout
    question: Can a plugin push its layout exports into the portal?
  phrasing_ops: 6
  slug: harness-layoutproxy-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for LayoutsV3.
  name: Harness Layouts V3 API
  phrasing_intents:
  - id: get-layouts-v3
    intent: List developer portal layouts
    question: Which page layouts are defined in my Harness developer portal?
  - id: create-layout-v3
    intent: Create a developer portal layout
    question: How do I add a new page layout to the developer portal?
  - id: delete-layout-v3
    intent: Delete a developer portal layout
    question: How do I remove a layout from the developer portal?
  - id: get-layout-v3
    intent: Get one developer portal layout
    question: What does a particular portal layout's YAML look like?
  - id: get-layout-health-v3
    intent: Check developer portal layout health
    question: Are my developer portal layouts healthy?
  - id: layout-ingest-v3
    intent: Ingest layout exports into the portal
    question: How do I bulk-load layout exports into the developer portal?
  phrasing_ops: 6
  slug: harness-layoutsv3-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for LayoutsV4.
  name: Harness Layouts V4 API
  phrasing_intents:
  - id: get-layouts-v4
    intent: Get page layouts (v4)
    question: What layouts are configured in my Harness account?
  phrasing_ops: 1
  slug: harness-layoutsv4-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Ldap Settings API from Harness — 16 operation(s) for ldap settings.
  name: Harness Ldap Settings API
  phrasing_intents:
  - id: create-ng-ldap-settings
    intent: Create LDAP settings for the account
    question: How do I set up LDAP authentication for my account from scratch?
  - id: get-account-ldap-settings
    intent: Get the account's LDAP settings
    question: What LDAP configuration is set up for my Harness account?
  - id: get-ldap-settings
    intent: Get LDAP settings by identifier
    question: Can I look up a specific LDAP configuration by its ID?
  - id: update-ldap-settings
    intent: Update existing LDAP settings
    question: How do I change the connection details of an existing LDAP configuration?
  - id: delete-ldap-settings
    intent: Delete LDAP settings
    question: How do I remove the LDAP configuration from my account?
  - id: validate-connection-settings
    intent: Test LDAP connection settings
    question: Can I check that Harness can reach my LDAP server before saving the config?
  - id: validate-user-settings
    intent: Test LDAP user query settings
    question: Does my LDAP user search base and filter actually find users?
  - id: validate-group-settings
    intent: Test LDAP group query settings
    question: Will my LDAP group search settings find the groups I expect?
  phrasing_ops: 19
  slug: harness-ldap-settings-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The License Usage Data By Account API from Harness — 1 operation(s) for license usage data by account.
  name: Harness License Usage Data By Account API
  phrasing_intents:
  - id: license-usage-activity
    intent: Get license usage activity for a time range
    question: How has our Harness license consumption trended over the last quarter?
  phrasing_ops: 1
  slug: harness-license-usage-data-by-account-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: License Usage Resource
  name: Harness License Usage Resource API
  phrasing_intents:
  - id: idp-license-usage-save
    intent: Record a user's Internal Developer Portal license usage
    question: How do I record that a developer accessed the Internal Developer Portal for license counting?
  - id: sscaLicenseUsage
    intent: Get supply chain security module license usage
    question: How much of our supply chain security license are we using?
  phrasing_ops: 2
  slug: harness-licenseusageresource-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for creating and retrieving database migration log information
  name: Harness Log Ingest API
  phrasing_intents:
  - id: V1IngestLogs
    intent: Ingest database migration logs
    question: How do I send migration logs so Harness updates a database's state?
  - id: V1GetDbinstanceLog
    intent: Get a database migration log event
    question: What does a specific migration log event for a database instance say?
  phrasing_ops: 2
  slug: harness-log-ingest-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs specific to the MCP Connector as defined in Harness
  name: Harness MCP Connector API
  phrasing_intents:
  - id: listMCPTools
    intent: List tools exposed by an MCP server connector
    question: What tools does a connected MCP server make available?
  phrasing_ops: 1
  slug: harness-mcpconnector-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Merged Plugins Configurations
  name: Harness Merged Plugins Config API
  phrasing_intents:
  - id: get-merged-plugins-config
    intent: Get merged config of enabled IDP plugins
    question: What is the combined configuration of all plugins enabled in my developer portal?
  - id: sync-app-config
    intent: Sync the merged app-config for an account
    question: How does a support user resync the developer portal app-config for an account?
  - id: update-configuration-entities
    intent: Update portal env variables and proxy settings
    question: How do I set environment variables and proxy entries on the portal configuration screen?
  phrasing_ops: 3
  slug: harness-mergedpluginsconfig-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Migration Service handles one-off connector and template migrations.
  name: Harness Migration API
  phrasing_intents:
  - id: migration#migrate-template-connectors
    intent: Add provider connectors to IaCM templates
    question: How do I add provider connectors to the IaCM templates we're using?
  - id: migration#migrate-workspace-connectors
    intent: Move workspace connectors to provider connectors
    question: Can I migrate connector data out of IaCM workspaces?
  phrasing_ops: 2
  slug: harness-migration-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for getting Migration State of Database Schema Entity
  name: Harness Migration State API
  phrasing_intents:
  - id: V1FetchDeployedChangesetSql
    intent: Get the SQL of changesets deployed to a DB instance
    question: What SQL actually ran when a changeset was deployed to my database instance?
  - id: V1ChangesetYamlProjDbInstance
    intent: Get the deployment YAML for a changeset on an instance
    question: Where can I get the YAML definition of a changeset as deployed to one database instance?
  - id: V1MigrationStateFlywayInstance
    intent: Get Flyway migration state of a DB instance
    question: Which Flyway migrations have been applied to one database instance?
  - id: V1MigrationStateProjDbInstance
    intent: Get migration state of a DB instance
    question: Which changesets have been deployed to a single database instance so far?
  - id: V1MigrationStateFlywaySchema
    intent: Get Flyway migration state across a schema
    question: How far along are Flyway migrations across all instances of one DB schema?
  - id: V1MigrationStateProjDbSchema
    intent: Get migration state across a DB schema
    question: Which changesets are deployed to which instances of my database schema?
  phrasing_ops: 6
  slug: harness-migration-state-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Module License Utilization API from Harness — 1 operation(s) for module license utilization.
  name: Harness Module License Utilization API
  phrasing_intents:
  - id: get-v1-moduleLicenseUtilization
    intent: Get module license utilization
    question: How much of my module licenses am I using?
  phrasing_ops: 1
  slug: harness-module-license-utilization-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The module-registry service is a private registry for Terraform/Opentofu modules
  name: Harness Module Registry API
  phrasing_intents:
  - id: module-registry#list_modules-by-account
    intent: List modules in the module registry
    question: What Terraform modules are published in our Harness module registry?
  - id: module-registry#create-module
    intent: Register a new module in the registry
    question: How do I add a new infrastructure module to the module registry?
  - id: module-registry#delete-module
    intent: Delete a module from the registry
    question: Is it possible to remove a whole module from the module registry?
  - id: module-registry#list-modules-by-id
    intent: Get one registry module by ID
    question: Where can I see the full details of a single module in the registry?
  - id: module-registry#update-module
    intent: Update a registry module's settings
    question: Can I change the repository or description of a module that's already registered?
  - id: module-registry#delete-module-lifecycle
    intent: Remove a module's lifecycle rule
    question: How do I drop the lifecycle rule so every version of a module counts as supported again?
  - id: module-registry#get-module-lifecycle
    intent: Get a module's lifecycle rule
    question: Which lifecycle rule controls when versions of a module become deprecated?
  - id: module-registry#put-module-lifecycle
    intent: Set a module's version lifecycle rule
    question: Can I define how many module versions stay supported before they are warned or deprecated?
  phrasing_ops: 35
  slug: harness-module-registry-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Module Versions API from Harness — 1 operation(s) for module versions.
  name: Harness Module Versions API
  phrasing_intents:
  - id: list-module-versions
    intent: List versions of Harness modules
    question: Which versions of each Harness module am I running?
  phrasing_ops: 1
  slug: harness-module-versions-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to CRUD operations of Monitored Services
  name: Harness Monitored Services API
  phrasing_intents:
  - id: createDefaultMonitoredService
    intent: Create a default monitored service
    question: Can Harness spin up a default monitored service for a service and environment pair automatically?
  - id: getMonitoredService
    intent: Get a monitored service's configuration
    question: How do I see the full configuration of one monitored service, including its health sources and dependencies?
  - id: updateMonitoredService
    intent: Update a monitored service's settings
    question: Can I rename a monitored service or change its tags and notification rules after it exists?
  - id: deleteMonitoredService
    intent: Delete a monitored service
    question: How do I remove a monitored service I no longer need?
  - id: detachMonitoredServiceFromTemplate
    intent: Detach a monitored service from its template
    question: Can I unlink a monitored service from the template it was created from so I can edit it freely?
  - id: getAllMonitoredServicesWithHealthSources
    intent: List monitored services with time-series health sources
    question: Which monitored services in my project have time-series health sources attached?
  - id: CvgetAnomaliesSummary
    intent: Count anomalies for a monitored service
    question: How many anomalies did a monitored service record over a given time window?
  - id: getCountOfServices
    intent: Count monitored services in a project
    question: How many monitored services does my project have in total?
  phrasing_ops: 37
  slug: harness-monitored-services-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The MS Teams Utils API from Harness — 1 operation(s) for ms teams utils.
  name: Harness MS Teams Utils API
  phrasing_intents:
  - id: msTeamsOauthTokenGenerate
    intent: Generate an OAuth token for Microsoft Teams
    question: How is the Microsoft Teams OAuth token created after authorizing the integration?
  phrasing_ops: 1
  slug: harness-ms-teams-utils-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Backstage Namespace
  name: Harness Namespace API
  phrasing_intents:
  - id: get-namespace-info
    intent: Get my account's customer namespace
    question: Which customer namespace is assigned to my Harness account?
  - id: create-namespace
    intent: Create a namespace for my account
    question: How do I provision a customer namespace for my account?
  phrasing_ops: 2
  slug: harness-namespace-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Network Maps API from Harness — 6 operation(s) for network maps.
  name: Harness Network Maps API
  phrasing_intents:
  - id: listTargetNetworkMaps
    intent: List network maps for chaos targeting
    question: Which application network maps are available to target with chaos experiments?
  - id: getTargetNetworkMap
    intent: Get a network map with chaos context
    question: What services and chaos details are in a particular application network map?
  - id: deleteTargetNetworkMap
    intent: Delete an application network map
    question: How do I delete an application network map I no longer target?
  - id: canRetryExperimentCreation
    intent: Check if experiment creation can be retried
    question: Can chaos experiment creation be retried for a network map where it failed?
  - id: retryExperimentCreation
    intent: Retry chaos experiment creation for a network map
    question: How do I rerun chaos experiment creation for a network map after it failed?
  - id: listService
    intent: List discovered services in a network map
    question: Which discovered services are part of a given network map?
  - id: getServiceResponse
    intent: Get one discovered service in a network map
    question: What chaos details are recorded for a single discovered service in my network map?
  phrasing_ops: 7
  slug: harness-network-maps-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Nextgen Ldap as defined in Harness
  name: Harness Nextgen Ldap API
  phrasing_intents:
  - id: getNgLdapSettings
    intent: Get the account's LDAP settings
    question: What LDAP configuration is set on my Harness account?
  - id: postLdapAuthenticationTest
    intent: Test an LDAP login
    question: Does LDAP authentication work with a test user's credentials?
  - id: searchLdapGroups
    intent: Search LDAP groups by name
    question: Which LDAP groups match a name I'm looking for?
  phrasing_ops: 3
  slug: harness-nextgen-ldap-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to CRUD operations of SLOs (simple & composite)
  name: Harness NG SLOs API
  phrasing_intents:
  - id: getServiceLevelObjectiveNg
    intent: Get an SLO's configuration
    question: What target and spec is defined on a particular SLO?
  - id: updateSLODataNg
    intent: Update an SLO
    question: How do I change the target on an existing SLO?
  - id: deleteSLODataNg
    intent: Delete an SLO
    question: How do I delete a service level objective?
  - id: getOnboardingGraphNg
    intent: Preview the onboarding graph for a composite SLO
    question: What will a composite SLO look like before I save it?
  - id: getSLOHealthListViewNg
    intent: Get the SLO health list view
    question: Which SLOs are at risk of exhausting their error budget?
  - id: getServiceLevelObjectivesNg
    intent: List all SLOs in a project
    question: What SLOs are defined in my project?
  - id: saveSLODataNg
    intent: Create an SLO
    question: How do I create a new service level objective?
  phrasing_ops: 7
  slug: harness-ng-slos-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Notification Attachments
  name: Harness Notification Attachments API
  phrasing_intents:
  - id: create-attachment
    intent: Save an attachment for notifications
    question: How do I attach a file so it can be sent along with a notification?
  phrasing_ops: 1
  slug: harness-notification-attachments-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Notification Channels
  name: Harness Notification Channels API
  phrasing_intents:
  - id: list-notification-channels
    intent: List a project's notification channels
    question: Which notification channels are set up in my project?
  - id: create-notification-channel
    intent: Create a project notification channel
    question: How do I add a new notification channel scoped to a single project?
  - id: get-notification-channel
    intent: Get a project notification channel
    question: How is a particular project notification channel configured?
  - id: delete-notification-channel
    intent: Delete a project notification channel
    question: How do I remove a notification channel from a project?
  - id: update-notification-channel
    intent: Update a project notification channel
    question: Can I change the destination of an existing project-level notification channel?
  - id: list-notification-channels-org
    intent: List an organization's notification channels
    question: What notification channels are defined at the organization level?
  - id: create-notification-channel-org
    intent: Create an organization notification channel
    question: How do I create a notification channel shared by every project in an org?
  - id: list-notification-channels-account
    intent: List account-level notification channels
    question: Which notification channels exist at the account level?
  phrasing_ops: 18
  slug: harness-notification-channels-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Notification Rules
  name: Harness Notification Rules API
  phrasing_intents:
  - id: list-notification-rules
    intent: List a project's notification rules
    question: Which notification rules are set up in my project?
  - id: create-notification-rule
    intent: Create a project notification rule
    question: How do I get alerted about events in a single project?
  - id: get-notification-rule
    intent: Get a project notification rule
    question: What conditions and channels does a particular project notification rule use?
  - id: delete-notification-rule
    intent: Delete a project notification rule
    question: How do I remove a notification rule from a project?
  - id: update-notification-rule
    intent: Update a project notification rule
    question: Can I change which conditions trigger a project's notification rule?
  - id: list-notification-rules-org
    intent: List an organization's notification rules
    question: What notification rules are defined at the org level?
  - id: create-notification-rule-org
    intent: Create an org-level notification rule
    question: How do I set up a notification rule that covers a whole organization?
  - id: list-notification-rules-account
    intent: List account-wide notification rules
    question: Which notification rules apply across my entire Harness account?
  phrasing_ops: 19
  slug: harness-notification-rules-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Set notification channels to get cloud and AI cost anomaly alerts
  name: Harness Notification Settings v2 API
  phrasing_intents:
  - id: listNotificationSettingsV2
    intent: List cost anomaly notification settings
    question: Which cost anomaly alert settings are configured in my account?
  - id: updateNotificationSettingV2
    intent: Update a cost anomaly notification setting
    question: How do I change the channels an existing cost anomaly alert is sent to?
  - id: createNotificationSettingV2
    intent: Set up cost anomaly alerts for a perspective
    question: How do I get alerted when cloud or AI costs spike unexpectedly on a perspective?
  - id: deleteNotificationSettingsV2
    intent: Delete a cost anomaly notification setting
    question: How do I stop cost anomaly alerts by removing their notification setting?
  phrasing_ops: 4
  slug: harness-notification-settings-v2-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to OIDC Access Token generation as defined in Harness
  name: Harness Oidc Access Token API
  phrasing_intents:
  - id: generateOidcIAMRoleCredentialForAws
    intent: Exchange an OIDC token for AWS IAM role credentials
    question: Can I get temporary AWS credentials for an IAM role using an OIDC token?
  - id: getOidcServiceAccountAccessTokenForGcp
    intent: Get a GCP service account token via OIDC
    question: Can I impersonate a GCP service account using an OIDC ID token?
  - id: exchangeOidcTokenForAzureCredentials
    intent: Exchange an OIDC token for Azure credentials
    question: Can I get Azure credentials from an OIDC token without a client secret?
  - id: OidcWorkloadAccessTokenResponse
    intent: Get a GCP workload identity access token
    question: Can I get a GCP workload identity federation token from an OIDC ID token?
  phrasing_ops: 4
  slug: harness-oidc-access-token-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to the Harness OIDC config
  name: Harness OIDC API
  phrasing_intents:
  - id: getHarnessOpenIdConfig
    intent: Get the JWKS signing keys for an account's OIDC
    question: Where are the public keys a cloud provider uses to verify Harness-issued OIDC tokens?
  - id: getHarnessOpenIdConfig_1
    intent: Get the OpenID discovery document for an account
    question: What is the issuer and discovery metadata for my account's OIDC provider?
  phrasing_ops: 2
  slug: harness-oidc-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to OIDC ID Token generation as defined in Harness
  name: Harness Oidc ID Token API
  phrasing_intents:
  - id: generateOidcIdTokenForAzure
    intent: Generate an OIDC ID token for Azure
    question: Can Harness issue an OIDC token so I can authenticate to Azure without a stored client secret?
  - id: generateOidcIdTokenForGcp
    intent: Generate an OIDC ID token for GCP (v1)
    question: How do I get a Harness OIDC token for GCP workload identity federation?
  - id: generateOidcIdTokenForGcp_1
    intent: Generate an OIDC ID token for GCP (v2)
    question: Is there a v2 endpoint for generating GCP OIDC ID tokens?
  - id: generateCustomOidcIdToken
    intent: Generate a custom OIDC ID token
    question: Can I mint an OIDC ID token with my own audience and subject for any relying party?
  - id: generateOidcIdTokenForAws
    intent: Generate an OIDC ID token for AWS
    question: How do I get a Harness OIDC token to assume an AWS role without long-lived keys?
  phrasing_ops: 5
  slug: harness-oidc-id-token-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Oidc Provider API from Harness — 3 operation(s) for oidc provider.
  name: Harness Oidc Provider API
  phrasing_intents:
  - id: create-oidc-provider
    intent: Add an OIDC identity provider
    question: How do I connect a new OIDC identity provider for single sign-on?
  - id: list-oidc-provider
    intent: List OIDC identity providers
    question: Which OIDC identity providers are configured for sign-in?
  - id: get-oidc-provider
    intent: Get an OIDC provider
    question: What issuer and scopes is an OIDC provider configured with?
  - id: update-oidc-provider
    intent: Update an OIDC provider
    question: Can I change the issuer or scopes of an existing OIDC provider?
  - id: delete-oidc-provider
    intent: Delete an OIDC provider
    question: How do I remove an OIDC identity provider from my account?
  - id: get-oidc-provider-internal
    intent: Get an OIDC provider with its decrypted secret
    question: Can I retrieve an OIDC provider including its decrypted client secret?
  phrasing_ops: 6
  slug: harness-oidc-provider-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to platform onboarding flows
  name: Harness Onboarding API
  phrasing_intents:
  - id: executeOnboarding
    intent: Provision a Kubernetes service setup in one call
    question: Can I create the secrets, connectors and Kubernetes service for onboarding in one request?
  - id: uploadKubeConfig
    intent: Upload a kubeconfig for onboarding
    question: Can I onboard my cluster by uploading a kubeconfig file?
  - id: listPipelineOnboarding
    intent: List pipelines onboarded to chaos
    question: Which of my pipelines have been onboarded to chaos engineering?
  - id: pipelineOnboardChaos
    intent: Onboard a pipeline to chaos engineering
    question: Can I add chaos experiments to an existing pipeline?
  - id: deletePipelineOnboarding
    intent: Delete a pipeline chaos onboarding entry
    question: Can I remove a pipeline's chaos onboarding record?
  - id: pipelineCanOnboardChaos
    intent: Check whether a pipeline can be onboarded
    question: Is my pipeline eligible to be onboarded to chaos?
  - id: pipelineOnboardChaosStatus
    intent: Get a pipeline's chaos onboarding status
    question: Has my pipeline finished onboarding to chaos?
  - id: listV2Onboarding
    intent: List chaos onboarding runs
    question: Which chaos onboarding runs exist in my project?
  phrasing_ops: 16
  slug: harness-onboarding-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Onboarding
  name: Harness Onboarding Resource API
  phrasing_intents:
  - id: get-harness-entities
    intent: List entities available to import into IDP
    question: Which services and entities from my account can be onboarded into the developer portal catalog?
  - id: get-harness-entities-count
    intent: Count entities available for onboarding
    question: How many entities are waiting to be onboarded into the portal?
  - id: import-harness-entities
    intent: Import entities into the developer portal
    question: How do I bulk-import my existing services into the IDP catalog?
  - id: onboarding-generate-yaml
    intent: Generate catalog YAML for entities
    question: Can I preview the catalog-info YAML that would be generated for my entities?
  phrasing_ops: 4
  slug: harness-onboardingresource-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Orchestration Activities API from Harness — 7 operation(s) for orchestration activities.
  name: Harness Orchestration Activities API
  phrasing_intents:
  - id: post-orchestrationActivity
    intent: Create a release orchestration activity
    question: How do I define a new orchestration activity for release management?
  - id: get-orchestration-activity-summary
    intent: List orchestration activities
    question: What orchestration activities exist in my project?
  - id: get-orchestrationActivity
    intent: Get an orchestration activity
    question: What is configured in a specific orchestration activity?
  - id: put-orchestration-activity
    intent: Update an orchestration activity
    question: How do I change the YAML of an existing orchestration activity?
  - id: delete-orchestration-activity
    intent: Delete an orchestration activity
    question: How do I remove an orchestration activity I no longer need?
  - id: get-orchestration-activity-inputs
    intent: Get input definitions for an activity
    question: What inputs does a given activity take within a process input configuration?
  - id: postOnHoldActivityAction
    intent: Retry or ignore an on-hold activity
    question: How do I resume an activity that is stuck on hold?
  - id: get-orchestration-activities-by-process-identifier
    intent: List activities in an orchestration process
    question: Which activities belong to a particular release process?
  phrasing_ops: 9
  slug: harness-orchestration-activities-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for SBOM.
  name: Harness Orchestration API
  phrasing_intents:
  - id: getOrchestrationSummary
    intent: Get a summary of an SBOM orchestration
    question: What happened in a particular SBOM orchestration run?
  phrasing_ops: 1
  slug: harness-orchestration-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Orchestration Executions API from Harness — 18 operation(s) for orchestration executions.
  name: Harness Orchestration Executions API
  phrasing_intents:
  - id: startReleaseExecution
    intent: Start executing a release
    question: How do I kick off a release in Harness release orchestration?
  - id: get-orchestration-execution-phases
    intent: Get the phases of a release
    question: What phases make up a release and what YAML configures each one?
  - id: get-orchestration-execution-activities
    intent: Get the activities in a release phase
    question: Which activities run inside a given phase of my release?
  - id: get-orchestration-execution-tasks
    intent: Get the tasks of a release activity
    question: What tasks sit under a particular activity in a release phase?
  - id: get-activity-retry-history-by-identifiers
    intent: Get the retry history of a release activity
    question: How many times was a release activity retried, and what happened each time?
  - id: get-orchestration-execution-activity-inputs
    intent: Get the input values of an activity execution
    question: What inputs were given to a specific activity execution?
  - id: get-orchestration-execution-activity
    intent: Get full details of a release activity execution
    question: Can I see the YAML and pipeline execution details behind one release activity?
  - id: get-orchestration-execution-phase-outputs
    intent: Get the outputs of a release phase
    question: What output values did a release phase produce?
  phrasing_ops: 19
  slug: harness-orchestration-executions-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Orchestration Processes API from Harness — 7 operation(s) for orchestration processes.
  name: Harness Orchestration Processes API
  phrasing_intents:
  - id: post-orchestrationProcess
    intent: Create a release orchestration process
    question: How do I define a new release orchestration process from YAML?
  - id: get-orchestrationProcess-summary
    intent: List orchestration processes
    question: Which release orchestration processes exist in my project?
  - id: get-orchestrationProcess
    intent: Get an orchestration process
    question: What does a particular orchestration process definition look like?
  - id: put-orchestration-process
    intent: Update an orchestration process
    question: How do I change the steps of an existing orchestration process?
  - id: delete-orchestration-process
    intent: Delete an orchestration process
    question: How do I remove an orchestration process I no longer need?
  - id: post-orchestrationProcessInput
    intent: Add an input set to an orchestration process
    question: How do I create an input set for an orchestration process?
  - id: get-orchestration-process-input
    intent: Get an orchestration process input
    question: What values are stored in a specific input of an orchestration process?
  - id: put-orchestration-process-input
    intent: Update an orchestration process input
    question: How do I edit the values in an existing process input set?
  phrasing_ops: 11
  slug: harness-orchestration-processes-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The OrchestrationV2 API from Harness — 4 operation(s) for orchestrationv2.
  name: Harness Orchestration V2 API
  phrasing_intents:
  - id: downloadSbom
    intent: Download the SBOM for an artifact
    question: How do I download the software bill of materials generated for an artifact?
  - id: calculateDriftForOrchestrationStep
    intent: Calculate SBOM drift for an orchestration step
    question: What components changed between this SBOM and a baseline?
  - id: uploadSbom
    intent: Upload an SBOM for an orchestration run
    question: Can I upload an SBOM I generated elsewhere and attach it to an orchestration run?
  - id: saveOrchestration
    intent: Save an SBOM orchestration record
    question: How do I record an orchestration with its artifact, SBOM metadata and attestation?
  phrasing_ops: 4
  slug: harness-orchestrationv2-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The orchestrationV3 API from Harness — 2 operation(s) for orchestrationv3.
  name: Harness Orchestration V3 API
  phrasing_intents:
  - id: uploadSbomV2
    intent: Upload an SBOM for an orchestration run
    question: How do I upload an SBOM file generated during a supply-chain orchestration run?
  - id: saveOrchestrationV2
    intent: Save an SBOM orchestration record
    question: How is an orchestration's artifact, SBOM metadata and attestation saved?
  phrasing_ops: 2
  slug: harness-orchestrationv3-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for organization-scoped Certificates
  name: Harness Org Certificate API
  phrasing_intents:
  - id: get-org-scoped-certificate
    intent: Get a certificate in an organization
    question: What are the details of a specific certificate stored at the org level?
  - id: update-org-scoped-certificate
    intent: Update a certificate in an organization
    question: How do I replace the value of a certificate stored at org scope?
  - id: delete-org-scoped-certificate
    intent: Delete a certificate from an organization
    question: How do I remove a certificate from my org?
  - id: validate-org-scoped-certificate-identifier
    intent: Check if a certificate identifier is free in an org
    question: Is a certificate identifier already taken in my organization?
  - id: get-org-scoped-certificates
    intent: List certificates in an organization
    question: What certificates are stored in my Harness organization?
  - id: create-org-scoped-certificates
    intent: Upload a new certificate to an organization
    question: How do I upload a new certificate file at the org level?
  phrasing_ops: 6
  slug: harness-org-certificate-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Organization-scoped Connectors.
  name: Harness Org Connector API
  phrasing_intents:
  - id: create-org-scoped-connector
    intent: Create an organization connector
    question: How do I add a new connector at the org level?
  - id: get-org-scoped-connectors
    intent: List connectors in an organization
    question: What connectors are set up at the organization level?
  - id: get-org-scoped-connector
    intent: Get an organization connector
    question: What is configured on a specific org-level connector?
  - id: update-org-scoped-connector
    intent: Update an organization connector
    question: How do I change the settings of an existing org connector?
  - id: delete-org-scoped-connector
    intent: Delete an organization connector
    question: How do I delete a connector from an organization?
  - id: test-org-scoped-connector
    intent: Test an organization connector's connection
    question: Is my org-level connector able to connect right now?
  phrasing_ops: 6
  slug: harness-org-connector-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Org Environments API from Harness — 2 operation(s) for org environments.
  name: Harness Org Environments API
  phrasing_intents:
  - id: create-org-scoped-environment
    intent: Create an environment in an organization
    question: How do I add a production or pre-production environment shared across an org?
  - id: get-org-scoped-environments
    intent: List environments in an organization
    question: What deployment environments are defined at the org level?
  - id: get-org-scoped-environment
    intent: Get an environment in an organization
    question: What is configured for a specific org-level environment?
  - id: update-org-scoped-environment
    intent: Update an environment in an organization
    question: How do I change an org environment from pre-production to production?
  - id: delete-org-scoped-environment
    intent: Delete an environment from an organization
    question: How do I remove an environment defined at the org level?
  phrasing_ops: 5
  slug: harness-org-environments-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for organization-scoped Favorites.
  name: Harness Org Favorites API
  phrasing_intents:
  - id: create-org-favorite
    intent: Add a favorite for a user in an organization
    question: Can I star a pipeline or other resource as a favorite at the organization level?
  - id: get-org-favorites
    intent: List a user's favorites in an organization
    question: What resources has a user starred as favorites in an organization?
  - id: delete-org-favorite
    intent: Remove a favorite for a user in an organization
    question: Can I unstar a resource from a user's organization favorites?
  phrasing_ops: 3
  slug: harness-org-favorites-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Org Gitx Webhooks API from Harness — 2 operation(s) for org gitx webhooks.
  name: Harness Org Gitx Webhooks API
  phrasing_intents:
  - id: list-org-gitx-webhooks
    intent: List org-level GitX webhooks
    question: Which GitX webhooks are configured at the organization level?
  - id: create-org-gitx-webhook
    intent: Create an org-level GitX webhook
    question: How do I set up a GitX webhook so Harness picks up changes from a Git repo for my org?
  - id: get-org-gitx-webhook
    intent: Get an org-level GitX webhook
    question: What repo and folders does a particular org GitX webhook watch?
  - id: update-org-gitx-webhook
    intent: Update an org-level GitX webhook
    question: How do I disable an org GitX webhook without deleting it?
  - id: delete-org-gitx-webhook
    intent: Delete an org-level GitX webhook
    question: How do I remove a GitX webhook from my organization?
  phrasing_ops: 5
  slug: harness-org-gitx-webhooks-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Org Gitx Webhooks Events.
  name: Harness Org Gitx Webhooks Events API
  phrasing_intents:
  - id: list-org-gitx-webhook-events
    intent: List GitX webhook events for an org
    question: What GitX webhook events has my organization received?
  phrasing_ops: 1
  slug: harness-org-gitx-webhooks-events-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Org Infrastructures API from Harness — 2 operation(s) for org infrastructures.
  name: Harness Org Infrastructures API
  phrasing_intents:
  - id: create-org-scoped-infrastructure
    intent: Create an org-level infrastructure definition
    question: How do I define a new deployment target infrastructure shared across an org?
  - id: get-org-scoped-infrastructures
    intent: List org-level infrastructure definitions
    question: Which infrastructure definitions exist in an org-level environment?
  - id: get-org-scoped-infrastructure
    intent: Get an org-level infrastructure definition
    question: What does an org-level infrastructure definition's YAML look like?
  - id: update-org-scoped-infrastructure
    intent: Update an org-level infrastructure definition
    question: How do I change the YAML of an existing org infrastructure definition?
  - id: delete-org-scoped-infrastructure
    intent: Delete an org-level infrastructure definition
    question: How do I delete an infrastructure definition from an org environment?
  phrasing_ops: 5
  slug: harness-org-infrastructures-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for projects.
  name: Harness Org Project API
  phrasing_intents:
  - id: create-org-scoped-project
    intent: Create a project in an organization
    question: How do I create a new project under an organization?
  - id: get-org-scoped-projects
    intent: List projects in an organization
    question: Which projects exist in a given organization?
  - id: get-org-scoped-project
    intent: Get a project
    question: Where can I see the details of one project?
  - id: update-org-scoped-project
    intent: Update a project
    question: Can I rename a project or change its description?
  - id: delete-org-scoped-project
    intent: Delete a project
    question: How do I delete a project from an organization?
  phrasing_ops: 5
  slug: harness-org-project-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Rancher infra entities for org level.
  name: Harness Org Rancher Infrastructure API
  phrasing_intents:
  - id: list-org-scoped-rancher-clusters-using-connector
    intent: List Rancher clusters via an org connector
    question: Which Rancher clusters can my organization-level Rancher connector see?
  - id: list-org-scoped-rancher-clusters-using-env-and-infra
    intent: List Rancher clusters via org environment and infra
    question: Which Rancher clusters belong to an org-level environment and infrastructure definition?
  phrasing_ops: 2
  slug: harness-org-rancher-infrastructure-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Organization-scoped Role Assignments.
  name: Harness Org Role Assignments API
  phrasing_intents:
  - id: get-org-scoped-role-assignments
    intent: List role assignments in an organization
    question: Who has which roles in my organization?
  - id: create-org-scoped-role-assignments
    intent: Assign a role in an organization
    question: How do I grant a user a role in an organization?
  - id: get-org-scoped-role-assignment
    intent: Get an organization role assignment
    question: What role and principal does a specific assignment grant?
  - id: delete-org-scoped-role-assignment
    intent: Delete an organization role assignment
    question: How do I revoke a role from someone in an organization?
  phrasing_ops: 4
  slug: harness-org-role-assignments-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for organization-scoped secrets.
  name: Harness Org Secret API
  phrasing_intents:
  - id: create-org-scoped-secret
    intent: Create a secret in an organization
    question: How do I add a new secret at the organization level?
  - id: get-org-scoped-secrets
    intent: List an organization's secrets
    question: Which secrets are defined in my organization?
  - id: validate-org-secret-ref
    intent: Check a secret manager path can be referenced
    question: Can I confirm a secret in my external secret manager is referenceable before saving it?
  - id: get-org-scoped-secret
    intent: Get one organization secret
    question: What are the details of one secret in my organization?
  - id: delete-org-scoped-secret
    intent: Delete an organization secret
    question: What's the way to remove a secret from my organization?
  - id: update-org-scoped-secret
    intent: Update an organization secret
    question: How do I rotate the value of an org-level secret?
  phrasing_ops: 6
  slug: harness-org-secret-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for organization-scoped services.
  name: Harness Org Services API
  phrasing_intents:
  - id: get-org-scoped-service
    intent: Get an org-level service
    question: What is configured on a service defined at organization scope?
  - id: update-org-scoped-service
    intent: Update an org-level service
    question: How do I change the YAML of a service shared across an organization?
  - id: delete-org-scoped-service
    intent: Delete an org-level service
    question: How do I delete a service defined at the organization level?
  - id: get-org-scoped-services
    intent: List an organization's services
    question: Which services are defined at my organization's scope?
  - id: create-org-scoped-service
    intent: Create an org-level service
    question: How do I create a service every project in an organization can use?
  - id: get-org-scoped-primary-manifests
    intent: List eligible primary manifests of an org service
    question: Which manifests on an org-scoped service can be picked as the primary one?
  - id: post-org-scoped-primary-manifests
    intent: List primary manifests from a Git branch
    question: Can I list primary manifest candidates of a Git-stored org service on a specific branch?
  phrasing_ops: 7
  slug: harness-org-services-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Organization-scoped Templates.
  name: Harness Org Template API
  phrasing_intents:
  - id: update-git-metadata-details-org
    intent: Update Git details of an org template
    question: Can I update the Git metadata for all versions of an org-level template?
  - id: create-templates-org
    intent: Create an organization-level template
    question: How do I create a new template shared across an organization?
  - id: get-templates-list-org
    intent: List templates in an organization
    question: Which pipeline templates exist at my organization level?
  - id: get-template-stable-org
    intent: Get the stable version of an org template
    question: What is the current stable version of an org template?
  - id: get-template-org
    intent: Get a specific version of an org template
    question: Can I retrieve an older version of an org-level template?
  - id: update-template-org
    intent: Update a version of an org template
    question: How do I edit a specific version of an org template?
  - id: delete-template-org
    intent: Delete a version of an org template
    question: Can I delete one version of an organization template?
  - id: update-template-stable-org
    intent: Set the stable version of an org template
    question: How do I promote a template version to stable at the org level?
  phrasing_ops: 10
  slug: harness-org-template-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Org Webhooks.
  name: Harness Org Webhooks API
  phrasing_intents:
  - id: list-org-webhooks
    intent: List webhooks in an organization
    question: What webhooks are configured at the organization level?
  - id: create-org-webhooks
    intent: Create an org-level webhook
    question: How do I set up a webhook that applies across a whole organization?
  - id: get-org-webhook
    intent: Get an org-level webhook
    question: Can I see how a specific organization webhook is configured?
  - id: update-org-webhook
    intent: Update or disable an org webhook
    question: How can I disable an org webhook without deleting it?
  - id: delete-org-webhook
    intent: Delete an org-level webhook
    question: Can I permanently remove a webhook from an organization?
  phrasing_ops: 5
  slug: harness-org-webhooks-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Create and manage organizations in your account. You use organizations to group together related projects. For example, you can use an organization to group together projects within a business unit or
  name: Harness Organization API
  phrasing_intents:
  - id: create-organization
    intent: Create an organization (v1)
    question: How do I create a new organization in Harness?
  - id: get-organizations
    intent: List organizations (v1)
    question: Which organizations exist in my Harness account?
  - id: get-organization
    intent: Get an organization (v1)
    question: Where can I see one organization's details by its identifier?
  - id: update-organization
    intent: Update an organization (v1)
    question: Can I rename an organization or change its description?
  - id: delete-organization
    intent: Delete an organization (v1)
    question: How do I delete an organization I no longer need?
  - id: getOrganizationList
    intent: List organizations by filter (NG)
    question: Can I filter organizations by a list of identifiers?
  - id: postOrganization
    intent: Create an organization (NG)
    question: Is there a legacy NG endpoint for creating an organization?
  - id: getOrganization
    intent: Get an organization's details (NG)
    question: Can I fetch an organization by identifier from the NG API?
  phrasing_ops: 10
  slug: harness-organization-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Organization-scoped Resource Groups.
  name: Harness Organization Resource Groups API
  phrasing_intents:
  - id: list-resource-groups-org
    intent: List resource groups in an organization
    question: Which resource groups exist in my organization?
  - id: create-resource-group-org
    intent: Create a resource group in an organization
    question: How do I create a custom resource group at the org level?
  - id: get-resource-group-org
    intent: Get an organization resource group
    question: Which resources does a particular org resource group cover?
  - id: update-resource-group-org
    intent: Update an organization resource group
    question: How do I change which resources an org resource group includes?
  - id: delete-resource-group-org
    intent: Delete an organization resource group
    question: How do I remove a custom resource group from an organization?
  phrasing_ops: 5
  slug: harness-organization-resource-groups-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Organization-scoped Roles.
  name: Harness Organization Roles API
  phrasing_intents:
  - id: list-roles-org
    intent: List roles in an organization
    question: Which roles are available in my organization?
  - id: create-role-org
    intent: Create a custom organization role
    question: Can I create a custom role with specific permissions for an organization?
  - id: get-role-org
    intent: Get an organization role
    question: What permissions does a particular organization role grant?
  - id: update-role-org
    intent: Update an organization role
    question: Can I change the permissions on an existing org role?
  - id: delete-role-org
    intent: Delete a custom organization role
    question: Can I delete a custom role from my organization?
  phrasing_ops: 5
  slug: harness-organization-roles-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Orgs API from Harness — 2 operation(s) for orgs.
  name: Harness Orgs API
  phrasing_intents:
  - id: V2ListProjDbInstances
    intent: List database instances in a project
    question: What database instances are managed in my project?
  - id: V2ListProjDbSchema
    intent: List database schemas in a project
    question: Which database schemas are defined in my project?
  phrasing_ops: 2
  slug: harness-orgs-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Overrides
  name: Harness Overrides API
  phrasing_intents:
  - id: updateOverride
    intent: Update a service or environment override
    question: How do I change the values in an existing environment or service override?
  - id: createOverride
    intent: Create a service or environment override
    question: How do I override variables or manifests for one service in a specific environment?
  - id: getOverridesViaIdentifier
    intent: Get a deployment override by identifier
    question: What values does a particular service or environment override set?
  - id: deleteOverride
    intent: Delete a deployment override
    question: How do I remove a service or environment override so defaults apply again?
  - id: OverrideMoveConfigs
    intent: Move an override between inline and Git storage
    question: Can I move an override's YAML out of Harness and into a Git repo?
  - id: updateOverrideGitDetails
    intent: Update Git metadata of a remote override
    question: If I moved an override's file in Git, how do I update the path Harness points to?
  - id: Overrides#ListOverrides
    intent: List security issue overrides
    question: Which security scan findings have had their severity or status overridden in STO?
  - id: Overrides#CreateOverride
    intent: Override a field on a security issue
    question: How do I change the severity of a security finding STO reported, with a reason?
  phrasing_ops: 11
  slug: harness-overrides-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Get overview of CACM features.
  name: Harness Overview API
  phrasing_intents:
  - id: getCCMOverview
    intent: Get a cloud cost overview for a period
    question: What's the high-level picture of my cloud spend over a time range?
  - id: V1GetDbOverview
    intent: Get a database DevOps overview for a project
    question: How many DB schemas and database instances does my project have?
  phrasing_ops: 2
  slug: harness-overview-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains the APIs related to permissions
  name: Harness Permissions API
  phrasing_intents:
  - id: getPermissionList
    intent: List available permissions
    question: What permissions can be granted in a Harness project?
  - id: getPermissionResourceTypesList
    intent: List resource types that have permissions
    question: Which resource types can permissions be applied to?
  phrasing_ops: 2
  slug: harness-permissions-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Manage cost reports created on Perspectives.
  name: Harness Perspective Reports API
  phrasing_intents:
  - id: getReportSetting
    intent: Get a cost perspective report schedule
    question: What scheduled cost reports are attached to a given perspective?
  - id: updateReportSetting
    intent: Update a scheduled cost report
    question: How do I change who receives a scheduled perspective cost report?
  - id: createReportSetting
    intent: Schedule a cost perspective report
    question: How do I email a cloud cost perspective report to my team every week?
  - id: deleteReportSetting
    intent: Delete a scheduled cost report
    question: How do I stop a scheduled perspective cost report?
  - id: getAllReports
    intent: List cost reports I can access
    question: Which scheduled cost reports am I able to see?
  - id: sendMail
    intent: Email a cost report now
    question: Can I send a cost report email immediately instead of waiting for its schedule?
  phrasing_ops: 6
  slug: harness-perspective-reports-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Group your resources using Perspectives in ways that are more meaningful to your business needs.
  name: Harness Perspectives API
  phrasing_intents:
  - id: getPerspective
    intent: Get a cloud cost perspective
    question: What rules and data sources make up a particular cost perspective?
  - id: updatePerspective
    intent: Update a cost perspective
    question: How do I change the rules or time range of an existing perspective?
  - id: createPerspective
    intent: Create or clone a cost perspective
    question: How do I build a new cloud cost perspective in Harness CCM?
  - id: deletePerspective
    intent: Delete a cost perspective
    question: How do I remove a cost perspective I no longer need?
  - id: getAllPerspectives
    intent: List all cost perspectives
    question: Which cost perspectives exist in my account?
  - id: getLastPeriodCost_1
    intent: Get a perspective's cost for the last period
    question: What did a perspective cost in the previous period?
  - id: getLastYearMonthlyCost
    intent: Get a perspective's last 12 months of cost
    question: What has a perspective cost month by month over the past year?
  phrasing_ops: 7
  slug: harness-perspectives-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Group your Perspectives using Folders in ways that are more meaningful to your business needs.
  name: Harness Perspectives Folders API
  phrasing_intents:
  - id: createPerspectiveFolder
    intent: Create a folder for cost perspectives
    question: How do I group my cloud cost perspectives into a folder?
  - id: deleteFolder
    intent: Delete a perspective folder
    question: Can I delete a perspective folder I no longer need?
  - id: getFolders
    intent: List perspective folders in an account
    question: What perspective folders exist in my cloud cost account?
  - id: updateFolder
    intent: Rename or pin a perspective folder
    question: Can I rename a perspective folder or pin it to the top?
  - id: getAllFolderPerspectives
    intent: List the perspectives inside a folder
    question: Which cost perspectives are stored in a particular folder?
  - id: movePerspectives
    intent: Move perspectives to another folder
    question: Can I move a perspective from one folder to another?
  phrasing_ops: 6
  slug: harness-perspectives-folders-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains pipeline APIs for files as provided as runtime input during pipeline execution
  name: Harness Pipeline API
  phrasing_intents:
  - id: downloadFileUsingFilePath
    intent: Download a pipeline input file by its storage path
    question: Can I download a file a pipeline stored in cloud storage if I know its file path?
  - id: PipelinegetFile
    intent: Get a file uploaded during a pipeline execution step
    question: How do I retrieve a file that was uploaded in one step of a pipeline execution?
  - id: createPipelineExecutionAnnotations
    intent: Add or update annotations on a pipeline execution
    question: Can I attach annotations to a pipeline execution after a step finishes?
  - id: convertPipelineToDAG
    intent: Convert a sequential pipeline to DAG format
    question: How do I turn an existing sequential pipeline into a DAG with stage dependencies?
  - id: postPipeline
    intent: Create a pipeline
    question: How do I create a new CI/CD pipeline in a project?
  - id: postPipelineV2
    intent: Create a pipeline with the v2 endpoint
    question: Which create endpoint lets me allow dynamic executions on a new pipeline?
  - id: getPipeline
    intent: Get a pipeline's YAML definition
    question: What does the full YAML of a pipeline look like?
  - id: updatePipeline
    intent: Update a pipeline
    question: How do I save changes to an existing pipeline?
  phrasing_ops: 16
  slug: harness-pipeline-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Pipeline Dashboard
  name: Harness Pipeline Dashboard API
  phrasing_intents:
  - id: getPipelineExecution
    intent: Get day-by-day execution stats for a pipeline
    question: How often did a pipeline run, succeed or fail each day over a period?
  phrasing_ops: 1
  slug: harness-pipeline-dashboard-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to retention of pipeline execution data
  name: Harness Pipeline data retention API
  phrasing_intents:
  - id: getRetentionPeriodInMonths
    intent: Get the pipeline execution retention period
    question: How long does Harness keep my pipeline execution history?
  phrasing_ops: 1
  slug: harness-pipeline-data-retention-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Executing a Pipeline
  name: Harness Pipeline Execute API
  phrasing_intents:
  - id: retryHistory
    intent: Get the retry history of an execution
    question: How many times has a pipeline execution been retried?
  - id: putHandleInterrupt
    intent: Abort, pause or resume a pipeline run
    question: How do I abort a running pipeline execution?
  - id: markManualExecution
    intent: Fail or resume a manual intervention step
    question: What do I do when a step is waiting on manual intervention?
  - id: handleStageInterrupt
    intent: Interrupt a single stage of a run
    question: Can I abort just one stage without stopping the rest of the pipeline?
  - id: retryPipeline
    intent: Retry a failed pipeline run
    question: How do I rerun a failed pipeline from the stages that failed?
  - id: retryPipelineV2
    intent: Retry a run with new runtime inputs (V2)
    question: Can I change the runtime inputs when retrying a failed execution?
  - id: postPipelineExecuteWithInputSetList
    intent: Run a pipeline using saved input sets
    question: Can I start a pipeline by referencing input sets I already saved?
  - id: postPipelineExecuteWithInputSetYaml
    intent: Run a pipeline with runtime input YAML
    question: How do I trigger a pipeline run through the Harness API?
  phrasing_ops: 9
  slug: harness-pipeline-execute-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for fetching Pipeline Execution Details
  name: Harness Pipeline Execution Details API
  phrasing_intents:
  - id: canRetryExecution
    intent: Check whether a pipeline execution can be retried
    question: Can this failed pipeline run be retried, or do I have to start a fresh execution?
  - id: getAnnotationFullContent
    intent: Fetch the full content of an execution annotation
    question: How do I read the complete text of an annotation that was truncated in the execution view?
  - id: getExecutionDetail
    intent: Get details of a pipeline execution
    question: What happened in a given pipeline run — status, stages and timings?
  - id: getExecutionDetailV2
    intent: Get execution details with child stage graph (v2)
    question: How do I get execution details that include child stages of a chained pipeline?
  - id: getExecutionGraph
    intent: Get the node graph of a pipeline execution
    question: Where can I get the full node-by-node execution graph for a pipeline run?
  - id: getExecutionSubGraphForNodeExecution
    intent: Get the subgraph of a retried step group
    question: How do I see what ran inside a step group that was retried?
  - id: getExecutionURL
    intent: Get the UI link to a pipeline execution
    question: How can I get a shareable link to a pipeline execution in the Harness UI?
  - id: getExecutionData
    intent: Get metadata of a pipeline execution
    question: What metadata is stored for a pipeline execution, like who triggered it?
  phrasing_ops: 17
  slug: harness-pipeline-execution-details-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Input Sets
  name: Harness Pipeline Input Set API
  phrasing_intents:
  - id: listInputSet
    intent: List a pipeline's input sets
    question: What input sets have been saved for a pipeline?
  - id: postInputSet
    intent: Create an input set for a pipeline
    question: How do I save a reusable set of runtime inputs for a pipeline?
  - id: postOverlayInputSet
    intent: Create an overlay input set
    question: Can I combine several input sets into one overlay input set?
  - id: getInputSet
    intent: Get a regular input set
    question: What values are stored in a particular input set?
  - id: putInputSet
    intent: Update a regular input set
    question: How do I change the values in an existing input set?
  - id: deleteInputSet
    intent: Delete an input set
    question: How do I delete an input set I no longer use?
  - id: getBatchInputSetsMetadata
    intent: List input sets across several pipelines
    question: Can I see the regular input sets for many pipelines in one call?
  - id: getBulkInputSets
    intent: Fetch several input sets by id
    question: Can I fetch a handful of input sets by their identifiers at once?
  phrasing_ops: 14
  slug: harness-pipeline-input-set-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to validation of templates in pipeline yaml
  name: Harness Pipeline Refresh API
  phrasing_intents:
  - id: refreshAllTemplatesInputsInPipeline
    intent: Refresh all template inputs in a pipeline
    question: A template changed; how do I update every template input in a pipeline that uses it?
  - id: validateTemplateInputs
    intent: Validate template inputs in a pipeline
    question: Are the template inputs in my pipeline YAML still valid?
  phrasing_ops: 2
  slug: harness-pipeline-refresh-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Pipeline Security API for STO
  name: Harness Pipeline Security API
  phrasing_intents:
  - id: pipeline-security#ExportPipelineSecurityIssuesCSV
    intent: Export a pipeline run's security issues as CSV
    question: Can I download the security issues found in a pipeline run as a spreadsheet?
  phrasing_ops: 1
  slug: harness-pipeline-security-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Pipeline Plugin Inputs
  name: Harness Pipeline Step API
  phrasing_intents:
  - id: GetV1CustomOperations
    intent: Run a custom operation for a database step
    question: How does a database DevOps step run a custom command against a schema?
  - id: ConsumeFailureInterrupt
    intent: Report a failure interrupt for a DB step
    question: How does a failed database step tell the pipeline which failure strategy to apply?
  - id: GetV1FlywayCustomOperations
    intent: Run a custom Flyway operation for a DB step
    question: Can a Flyway database step run a custom command?
  - id: ConsumeFlywayFailureInterrupt
    intent: Report a failure interrupt for a Flyway step
    question: How does a failed Flyway step report a failure interrupt back to the pipeline?
  - id: ConsumeV1FlywayStepPluginOutputResponse
    intent: Submit Flyway plugin output for a step
    question: How does the Flyway plugin send its step output back in chunks?
  - id: GetV1PluginCapability
    intent: Check DB plugin consolidated-execution support
    question: Does the database DevOps plugin support consolidated execution?
  - id: ConsumeV1StepPluginOutputResponse
    intent: Submit database plugin output for a step
    question: How does a database step plugin page its output back to the pipeline?
  - id: GetV1SchemaInstanceMetadata
    intent: Get metadata and images for a DB schema instance
    question: Which container images and metadata apply to a database schema instance?
  phrasing_ops: 12
  slug: harness-pipeline-step-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Pipeline Store Config API from Harness — 1 operation(s) for pipeline store config.
  name: Harness Pipeline Store Config API
  phrasing_intents:
  - id: savePipelineRemoteConfig
    intent: Save remote Git config for supply chain pipelines
    question: Where do I tell Harness which repo and branch to store supply chain scan pipelines in?
  phrasing_ops: 1
  slug: harness-pipeline-store-config-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The PipelineInfraConfig API from Harness — 2 operation(s) for pipelineinfraconfig.
  name: Harness Pipeline Infra Config API
  phrasing_intents:
  - id: savePipelineInfraConfig
    intent: Save supply chain pipeline infra settings
    question: How do I configure the pipeline infrastructure used for supply chain scans?
  - id: saveIntegrationConfig
    intent: Set how often supply chain scans run
    question: How do I change the scan frequency for supply chain integrations?
  phrasing_ops: 2
  slug: harness-pipelineinfraconfig-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Plugin Information
  name: Harness Plugin Info API
  phrasing_intents:
  - id: get-plugins
    intent: List available developer portal plugins
    question: Which plugins can I enable in my internal developer portal?
  - id: save-custom-plugins-info
    intent: Save info for a custom plugin
    question: How do I register details for a custom plugin I built?
  - id: get-plugins-info-plugin-id
    intent: Get a plugin's details
    question: What does a particular plugin do and how is it configured?
  - id: update-custom-plugins-info
    intent: Update a custom plugin's info
    question: Can I edit the details of a custom plugin I already registered?
  - id: delete-custom-plugin-info
    intent: Delete a custom plugin
    question: How do I remove a custom plugin from the portal?
  - id: get-backstage-plugins
    intent: List available Backstage plugins
    question: Which Backstage plugins are supported in the developer portal?
  - id: post-plugin-request
    intent: Request a new plugin
    question: How do I ask for a plugin that isn't available yet to be added?
  - id: get-plugin-request
    intent: List plugin requests for my account
    question: What plugins has my team asked to have added?
  phrasing_ops: 8
  slug: harness-plugininfo-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Create, edit and delete Governance policies written in rego
  name: Harness Policies API
  phrasing_intents:
  - id: policies#list
    intent: List OPA policies
    question: Which governance policies are defined in my Harness project?
  - id: policies#create
    intent: Create an OPA policy
    question: How do I write a new Rego policy in Harness?
  - id: policies#move_policy
    intent: Move an inline policy to Git
    question: Can I move a policy I wrote inline into a Git repository?
  - id: policies#delete
    intent: Delete a policy
    question: Why can't I delete a policy that policy sets still reference?
  - id: policies#find
    intent: Get one policy by identifier
    question: What Rego does a specific policy contain?
  - id: policies#update
    intent: Update a policy's name or Rego
    question: How do I change the Rego of an existing policy?
  - id: policies#list_policy_sets
    intent: List policy sets that use a policy
    question: Which policy sets reference a given policy?
  phrasing_ops: 7
  slug: harness-policies-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The principals API from Harness — 2 operation(s) for principals.
  name: Harness Principals API
  phrasing_intents:
  - id: listPrincipals
    intent: Search users and service principals
    question: Which users or service accounts in my Harness account match a name?
  - id: listPrincipalsScoped
    intent: List principals scoped to a repo or project
    question: Who has access within a specific code repository?
  phrasing_ops: 2
  slug: harness-principals-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Principals With Access API from Harness — 1 operation(s) for principals with access.
  name: Harness Principals With Access API
  phrasing_intents:
  - id: get-v1-listPrincipalsWithAccess
    intent: List principals with access to a module
    question: Which users and groups have access to a given Harness module?
  - id: post-v1-listPrincipalsWithAccess
    intent: Filter principals with access to a module
    question: Can I apply a filter when listing who has access to a module?
  phrasing_ops: 2
  slug: harness-principals-with-access-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Probe Templates API from Harness — 3 operation(s) for probe templates.
  name: Harness Probe Templates API
  phrasing_intents:
  - id: listProbeTemplate
    intent: List probe templates in a chaos hub
    question: Which chaos probe templates are available in a ChaosHub?
  - id: createProbeTemplate
    intent: Create a chaos probe template
    question: How do I save a reusable resilience probe as a template in a hub?
  - id: getProbeTemplate
    intent: Get a chaos probe template
    question: What does a specific probe template in my hub look like?
  - id: updateProbeTemplate
    intent: Update a chaos probe template
    question: How do I change the configuration of an existing probe template?
  - id: deleteProbeTemplate
    intent: Delete a chaos probe template
    question: How do I remove a probe template from a ChaosHub?
  - id: listVariablesInProbeTemplate
    intent: List inputs of a probe template revision
    question: Which inputs do I need to supply when using a probe template?
  phrasing_ops: 6
  slug: harness-probe-templates-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Probes API from Harness — 8 operation(s) for probes.
  name: Harness Probes API
  phrasing_intents:
  - id: listProbes
    intent: List chaos resilience probes
    question: What resilience probes are defined in my chaos engineering project?
  - id: createProbe
    intent: Create a chaos probe
    question: How do I create a new resilience probe for chaos experiments?
  - id: getProbesInExperiment
    intent: Get probes used in experiment runs
    question: Which probes ran as part of a chaos experiment run?
  - id: importProbe
    intent: Import a probe from a ChaosHub
    question: How do I import an existing probe template into my project?
  - id: getProbeManifest
    intent: Get a probe's manifest
    question: Where can I see the raw manifest YAML behind a probe?
  - id: getProbe
    intent: Get a probe's details
    question: What is configured on a specific chaos probe?
  - id: updateProbe
    intent: Update a probe's configuration
    question: How do I change the properties of an existing probe?
  - id: deleteProbe
    intent: Delete a probe
    question: How do I delete a chaos probe I no longer need?
  phrasing_ops: 11
  slug: harness-probes-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Access Scan Tool information
  name: Harness Products API
  phrasing_intents:
  - id: Products#ListProducts
    intent: List supported security scan tools
    question: Which security scan tools can I use with security testing orchestration?
  - id: Products#FindProductById
    intent: Get a scan tool by ID
    question: What details are recorded for one scan tool?
  phrasing_ops: 2
  slug: harness-products-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Project as defined in Harness
  name: Harness Project API
  phrasing_intents:
  - id: getProjectList
    intent: List projects I'm a member of
    question: Which Harness projects do I belong to in an org?
  - id: postProject
    intent: Create a project
    question: How do I create a new project in an organization?
  - id: getProject
    intent: Get a project's details
    question: What are the details of a specific project?
  - id: putProject
    intent: Update a project
    question: How do I change a project's name or description?
  - id: deleteProject
    intent: Delete a project
    question: How do I delete a project?
  - id: getProjectListWithMultiOrgFilter
    intent: List my projects across several orgs
    question: Can I list my projects from multiple organizations at once?
  phrasing_ops: 6
  slug: harness-project-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for project-scoped Certificates
  name: Harness Project Certificate API
  phrasing_intents:
  - id: get-project-scoped-certificate
    intent: Get a project certificate
    question: What are the details of a certificate stored in my project?
  - id: update-project-scoped-certificate
    intent: Update a project certificate
    question: How do I replace the certificate value stored in a project?
  - id: delete-project-scoped-certificate
    intent: Delete a project certificate
    question: How do I remove a certificate from a project?
  - id: validate-project-scoped-certificate-identifier
    intent: Check a project certificate ID is available
    question: Is a certificate identifier still free to use in my project?
  - id: get-project-scoped-certificates
    intent: List a project's certificates
    question: Which certificates are stored in my project?
  - id: create-project-scoped-certificates
    intent: Add a certificate to a project
    question: How do I upload a new certificate at project scope?
  phrasing_ops: 6
  slug: harness-project-certificate-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Project-scoped Connectors.
  name: Harness Project Connector API
  phrasing_intents:
  - id: create-project-scoped-connector
    intent: Create a connector in a project
    question: How do I add a Git or Artifactory connector to a project?
  - id: get-project-scoped-connectors
    intent: List a project's connectors
    question: Which connectors are configured in my project?
  - id: get-project-scoped-connector
    intent: Get a project connector
    question: What settings does a particular project connector have?
  - id: update-project-scoped-connector
    intent: Update a project connector
    question: Can I change the credentials or URL on a project connector?
  - id: delete-project-scoped-connector
    intent: Delete a project connector
    question: How do I remove a connector from a project?
  - id: test-project-scoped-connector
    intent: Test a project connector's connection
    question: Is my project connector actually able to connect?
  phrasing_ops: 6
  slug: harness-project-connector-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for project-scoped environments.
  name: Harness Project Environments API
  phrasing_intents:
  - id: create-environment
    intent: Create an environment in a project
    question: How do I create a new production or pre-production environment?
  - id: get-environments
    intent: List environments in a project
    question: Which deployment environments exist in my Harness project?
  - id: get-environment
    intent: Get an environment
    question: How do I look up one environment's type and settings?
  - id: update-environment
    intent: Update an environment
    question: Can I rename an environment or switch it between production and pre-production?
  - id: delete-environment
    intent: Delete an environment
    question: How do I delete an environment from a project?
  phrasing_ops: 5
  slug: harness-project-environments-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for project-scoped Favorites.
  name: Harness Project Favorites API
  phrasing_intents:
  - id: create-project-favorite
    intent: Mark a resource as a favorite in a project
    question: How do I star a pipeline or resource as a favorite in a project?
  - id: get-project-favorites
    intent: List a user's favorites in a project
    question: What has a user marked as a favorite in a project?
  - id: delete-project-favorite
    intent: Remove a favorite in a project
    question: How do I unstar a resource I favorited in a project?
  phrasing_ops: 3
  slug: harness-project-favorites-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Project Gitx Webhooks API from Harness — 2 operation(s) for project gitx webhooks.
  name: Harness Project Gitx Webhooks API
  phrasing_intents:
  - id: list-project-gitx-webhook
    intent: List GitX webhooks in a project
    question: Which GitX webhooks are configured for this project?
  - id: create-project-gitx-webhook
    intent: Create a project GitX webhook
    question: How do I set up a GitX webhook so Harness syncs changes from my repo?
  - id: get-project-gitx-webhook
    intent: Get a project GitX webhook
    question: What repo and folders does a specific GitX webhook track?
  - id: update-project-gitx-webhook
    intent: Update a project GitX webhook
    question: How do I disable a GitX webhook without deleting it?
  - id: delete-project-gitx-webhook
    intent: Delete a project GitX webhook
    question: How do I remove a GitX webhook from a project?
  phrasing_ops: 5
  slug: harness-project-gitx-webhooks-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Project Gitx Webhooks Events.
  name: Harness Project Gitx Webhooks Events API
  phrasing_intents:
  - id: list-project-gitx-webhook-events
    intent: List GitX webhook events for a project
    question: What GitX webhook events has my project received?
  phrasing_ops: 1
  slug: harness-project-gitx-webhooks-events-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Project Infrastructures API from Harness — 2 operation(s) for project infrastructures.
  name: Harness Project Infrastructures API
  phrasing_intents:
  - id: create-infrastructure
    intent: Create an infrastructure in a project environment
    question: How do I define a new infrastructure for a project environment?
  - id: get-infrastructures
    intent: List infrastructures in a project environment
    question: Which infrastructures are defined in an environment of my project?
  - id: get-infrastructure
    intent: Get a project infrastructure definition
    question: Can I view one infrastructure definition in a project environment?
  - id: update-infrastructure
    intent: Update a project infrastructure definition
    question: How do I edit an infrastructure definition in my project?
  - id: delete-infrastructure
    intent: Delete a project infrastructure
    question: Can I delete an infrastructure from a project environment?
  phrasing_ops: 5
  slug: harness-project-infrastructures-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Project mappings API from Harness — 7 operation(s) for project mappings.
  name: Harness Project mappings API
  phrasing_intents:
  - id: AppProjectMappingService_GetAppProjectMappingListByAgent
    intent: List an agent's Argo project mappings (v1)
    question: Which Argo projects are mapped to Harness projects on a given GitOps agent?
  - id: AppProjectMappingService_Create
    intent: Create Argo project mappings on an agent (v1)
    question: Is there a v1 way to add new Argo project mappings for an agent?
  - id: AppProjectMappingService_Update
    intent: Update an agent's Argo project mappings (v1)
    question: How do I change which Harness project an Argo project maps to on an agent, using v1?
  - id: AppProjectMappingService_Delete
    intent: Delete an Argo project mapping by name (v1)
    question: How do I remove an Argo project mapping by its name on an agent?
  - id: AppProjectMappingService_GetAppProjectMappingList
    intent: List Argo project mappings across agents (v1)
    question: Can I list all Harness-Argo project mappings in my project regardless of agent?
  - id: AppProjectMappingService_CreateV2
    intent: Create an Argo project mapping (v2)
    question: Can a v2 mapping auto-create services and environments for me?
  - id: AppProjectMappingService_GetAppProjectMappingV2
    intent: Get one Argo project mapping by id (v2)
    question: Can I look up a single v2 project mapping by its identifier?
  - id: AppProjectMappingService_DeleteV2
    intent: Delete an Argo project mapping by id (v2)
    question: How do I delete a v2 project mapping using its identifier?
  phrasing_ops: 11
  slug: harness-project-mappings-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Rancher infra entities for project level.
  name: Harness Project Rancher Infrastructure API
  phrasing_intents:
  - id: list-project-scoped-rancher-clusters-using-connector
    intent: List Rancher clusters through a project connector
    question: Which Rancher clusters can my project-level Rancher connector reach?
  - id: list-project-scoped-rancher-clusters-using-env-and-infra
    intent: List Rancher clusters for an environment's infra definition
    question: Which Rancher clusters does an infrastructure definition in my environment target?
  phrasing_ops: 2
  slug: harness-project-rancher-infrastructure-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Project-scoped Resource Groups.
  name: Harness Project Resource Groups API
  phrasing_intents:
  - id: list-resource-groups-project
    intent: List resource groups in a project
    question: Which resource groups are defined inside a specific Harness project?
  - id: create-resource-group-project
    intent: Create a resource group in a project
    question: How do I create a custom resource group scoped to one project?
  - id: get-resource-group-project
    intent: Get a resource group in a project
    question: What resources does a project-level resource group include?
  - id: update-resource-group-project
    intent: Update a resource group in a project
    question: How do I change which resources a project resource group covers?
  - id: delete-resource-group-project
    intent: Delete a resource group from a project
    question: How do I delete a custom resource group in a project?
  phrasing_ops: 5
  slug: harness-project-resource-groups-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Project-scoped Role Assignments.
  name: Harness Project Role Assignments API
  phrasing_intents:
  - id: get-project-scoped-role-assignments
    intent: List a project's role assignments
    question: Who has which roles in my project?
  - id: create-project-scoped-role-assignments
    intent: Assign a role in a project
    question: How do I give a user or group a role on a project?
  - id: get-project-scoped-role-assignment
    intent: Get a project role assignment
    question: What role and resource group does a specific project role assignment grant?
  - id: delete-project-scoped-role-assignment
    intent: Remove a project role assignment
    question: How do I revoke someone's role on a project?
  phrasing_ops: 4
  slug: harness-project-role-assignments-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Project-scoped Roles.
  name: Harness Project Roles API
  phrasing_intents:
  - id: list-roles-project
    intent: List the roles in a project
    question: What roles are available in a Harness project?
  - id: create-role-project
    intent: Create a custom role in a project
    question: How do I create a custom role with specific permissions in a project?
  - id: get-role-project
    intent: Get a project role
    question: Which permissions does a given project role include?
  - id: update-role-project
    intent: Update a project role
    question: Can I add permissions to an existing project role?
  - id: delete-role-project
    intent: Delete a custom project role
    question: Can I delete a custom role from a project?
  phrasing_ops: 5
  slug: harness-project-roles-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for project-scoped secrets.
  name: Harness Project Secret API
  phrasing_intents:
  - id: create-project-scoped-secret
    intent: Create a secret in a project
    question: How do I add a new secret to a project?
  - id: get-project-scoped-secrets
    intent: List secrets in a project
    question: Which secrets are stored in my Harness project?
  - id: validate-project-secret-ref
    intent: Check a secret manager path can be referenced
    question: Can I verify a secret manager path is referenceable before I create a secret for it?
  - id: get-project-scoped-secret
    intent: Get one project secret's details
    question: What secret manager and type does a specific project secret use?
  - id: delete-project-scoped-secret
    intent: Delete a project secret
    question: How do I remove a secret from a project?
  - id: update-project-scoped-secret
    intent: Update a project secret
    question: How do I rotate the value of an existing project secret?
  phrasing_ops: 6
  slug: harness-project-secret-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for project-scoped services.
  name: Harness Project Services API
  phrasing_intents:
  - id: get-service
    intent: Retrieve a project-scoped service
    question: How do I get the definition of a deployment service in a project?
  - id: update-service
    intent: Update a project-scoped service
    question: How do I change a service's name, description or YAML?
  - id: delete-service
    intent: Delete a project-scoped service
    question: How do I delete a service from a project?
  - id: get-services
    intent: List services in a project
    question: Which services can I see in a project?
  - id: create-service
    intent: Create a service in a project
    question: How do I create a new deployment service in a project?
  - id: get-primary-manifests
    intent: List eligible primary manifests for a service
    question: Which manifests in a service can be chosen as the primary manifest?
  - id: post-primary-manifests
    intent: List primary manifests for a Git-stored service
    question: How do I list primary manifests for a service whose YAML lives in a Git branch?
  phrasing_ops: 7
  slug: harness-project-services-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Project-scoped Templates.
  name: Harness Project Template API
  phrasing_intents:
  - id: update-git-metadata-details-project
    intent: Update Git details of a project template
    question: Can I update the Git details stored for every version of a project template?
  - id: create-templates-project
    intent: Create a project template
    question: Can I create a new pipeline template scoped to one project?
  - id: get-templates-list-project
    intent: List templates in a project
    question: Which templates exist in my project?
  - id: get-template-stable-project
    intent: Get the stable version of a project template
    question: Which version of a project template is currently marked stable?
  - id: get-template-project
    intent: Get a specific project template version
    question: Can I fetch one particular version of a project template?
  - id: update-template-project
    intent: Update a project template version
    question: Can I edit the YAML of an existing template version in a project?
  - id: delete-template-project
    intent: Delete a project template version
    question: Can I delete one version of a template in my project?
  - id: update-template-stable-project
    intent: Mark a project template version stable
    question: How do I promote a template version to stable in my project?
  phrasing_ops: 10
  slug: harness-project-template-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Project Webhooks.
  name: Harness Project Webhooks API
  phrasing_intents:
  - id: list-project-webhooks
    intent: List project-level webhooks
    question: Which webhooks are configured inside a project?
  - id: create-project-webhooks
    intent: Create a project-level webhook
    question: How do I add a webhook scoped to just one project?
  - id: get-project-webhook
    intent: Get a project-level webhook
    question: How is a particular project webhook set up?
  - id: update-project-webhook
    intent: Update a project-level webhook
    question: Can I turn off a project webhook but keep its configuration?
  - id: delete-project-webhook
    intent: Delete a project-level webhook
    question: How do I delete a webhook from a project?
  phrasing_ops: 5
  slug: harness-project-webhooks-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Prometheus Data Retrieval API from Harness — 1 operation(s) for prometheus data retrieval.
  name: Harness Prometheus Data Retrieval API
  phrasing_intents:
  - id: get-sync-data-collection-result
    intent: Run a Prometheus query and return the data
    question: Can I run a PromQL query through Harness and get the results back right away?
  phrasing_ops: 1
  slug: harness-prometheus-data-retrieval-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Provider
  name: Harness Provider API
  phrasing_intents:
  - id: getProviderList
    intent: List providers in the account
    question: Which providers are configured in my account?
  - id: createProvider
    intent: Create a provider
    question: How do I add a new provider configuration to my account?
  - id: getProvider
    intent: Get a provider by identifier
    question: How do I look up one provider's configuration by its identifier?
  - id: updateProvider
    intent: Update a provider
    question: Can I change the spec of a provider that's already configured?
  - id: deleteProvider
    intent: Delete a provider
    question: How do I remove a provider I no longer use?
  phrasing_ops: 5
  slug: harness-provider-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The provider-registry service implements HashiCorp's Provider Registry Protocol for private Terraform providers
  name: Harness Provider Registry API
  phrasing_intents:
  - id: provider-registry#list-providers
    intent: List Terraform providers in the registry
    question: Which Terraform providers have we published to the Harness IaCM provider registry?
  - id: provider-registry#delete-provider
    intent: Delete a provider from the registry
    question: How do I remove a whole Terraform provider from our private registry?
  - id: provider-registry#get-provider
    intent: Get a registry provider by ID
    question: What details does the registry hold for a single Terraform provider I own?
  - id: provider-registry#delete-provider-lifecycle
    intent: Remove a provider's lifecycle rule
    question: How do I clear the lifecycle rule on a provider so every version counts as supported again?
  - id: provider-registry#get-provider-lifecycle
    intent: Get a provider's lifecycle rule
    question: What lifecycle rule is set on a provider — how many versions stay supported before warnings?
  - id: provider-registry#put-provider-lifecycle
    intent: Set a provider's version lifecycle rule
    question: How do I define how many provider versions stay supported before they are flagged as warning?
  - id: provider-registry#get-provider-lifecycle-version-status
    intent: Check the lifecycle tier of a provider version
    question: Is a specific provider version still supported, in warning, or deprecated?
  - id: provider-registry#create-provider-version
    intent: Create a new provider version
    question: How do I register a new version of a Terraform provider in the Harness registry?
  phrasing_ops: 24
  slug: harness-provider-registry-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Provision
  name: Harness Provision API
  phrasing_intents:
  - id: provision-idp
    intent: Provision the Internal Developer Portal
    question: What does it take to provision the Harness Internal Developer Portal for my account?
  phrasing_ops: 1
  slug: harness-provision-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Provisioner Activities Service handles the API for managing provisioner activity lifecycle. This API provides explicit start and complete endpoints for provisioner operations (CDK, Terraform).
  name: Harness Provisioner Activities API
  phrasing_intents:
  - id: provisioner_activities#complete-activity
    intent: Finish a provisioner activity with its result
    question: How does a pipeline report that a provisioning activity succeeded or failed?
  - id: provisioner_activities#start-activity
    intent: Start a provisioner activity on a workspace
    question: How do I register the start of a provisioning run on an infrastructure workspace?
  phrasing_ops: 2
  slug: harness-provisioner-activities-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: APIs used by the ff-proxy
  name: Harness Proxy API
  phrasing_intents:
  - id: GetProxyKeys
    intent: List Relay Proxy keys
    question: What feature flag Relay Proxy keys exist in my account?
  - id: CreateProxyKey
    intent: Create a Relay Proxy key
    question: How do I create a key for the feature flags Relay Proxy?
  - id: DeleteProxyKey
    intent: Delete a Relay Proxy key
    question: How do I revoke a Relay Proxy key?
  - id: GetProxyKey
    intent: Get a Relay Proxy key
    question: What environments does a specific proxy key have access to?
  - id: PatchProxyKey
    intent: Change which environments a proxy key can access
    question: Can I give a proxy key access to more environments?
  phrasing_ops: 5
  slug: harness-proxy-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Public Access API from Harness — 4 operation(s) for public access.
  name: Harness Public Access API
  phrasing_intents:
  - id: enable-public-access
    intent: Make a resource publicly accessible
    question: Can I share a Harness resource, such as a pipeline, publicly without requiring login?
  - id: is-resource-public
    intent: Check whether one resource is public
    question: Is this particular resource currently exposed to the public?
  - id: check-public
    intent: Check public status for many resources
    question: Which of these resources are publicly accessible?
  - id: disable-public-access
    intent: Turn off public access on a resource
    question: What's the way to stop a resource from being publicly visible?
  phrasing_ops: 4
  slug: harness-public-access-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Access and Modify Pull Requests
  name: Harness Pull Requests API
  phrasing_intents:
  - id: PullRequests#ListPullRequests
    intent: List pull requests for a repository
    question: Which pull requests are open on a repository scanned by Security Testing Orchestration?
  - id: PullRequests#FindPullRequestByID
    intent: Find a pull request by number
    question: What are the details of a specific pull request number in my repository?
  - id: PullRequests#CreatePullRequest
    intent: Open a new PR with an AI remediation
    question: Can STO open a new pull request that fixes a vulnerability it found?
  - id: PullRequests#UpdatePullRequest
    intent: Add an AI remediation fix to an existing PR
    question: Can I push an AI-suggested remediation for a security issue onto a pull request I already have open?
  - id: PullRequests#GetPullRequestAction
    intent: Decide which PR action to offer for an issue
    question: Should the UI offer to create a PR, suggest a fix, or show an existing PR for this occurrence?
  - id: PullRequests#GetPullRequestCorrelation
    intent: Check if a code path is touched by a PR
    question: Is this file path part of a particular pull request?
  phrasing_ops: 6
  slug: harness-pull-requests-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The pullreq API from Harness — 40 operation(s) for pullreq.
  name: Harness Pullreq API
  phrasing_intents:
  - id: listPullReqSpace
    intent: List pull requests across an account, org or project
    question: Can I see every open pull request across all repos in my Harness project at once?
  - id: countPullReqSpace
    intent: Count pull requests across an account, org or project
    question: How many pull requests are open across all repositories in my project?
  - id: listPullReq
    intent: List pull requests in a repository
    question: What pull requests are open in one specific Harness Code repository?
  - id: createPullReq
    intent: Open a pull request
    question: How do I open a pull request from a feature branch into main?
  - id: getPullReq
    intent: Get a pull request
    question: Where can I look up the title, branches and state of one pull request by its number?
  - id: updatePullReq
    intent: Edit a pull request's title or description
    question: Can I rename a pull request after it's been opened?
  - id: listPullReqActivities
    intent: List a pull request's activity timeline
    question: What has happened on a pull request so far, comments, reviews and state changes included?
  - id: prAutoMergeDisable
    intent: Turn off auto-merge for a pull request
    question: How do I stop a pull request from merging automatically?
  phrasing_ops: 52
  slug: harness-pullreq-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The quarantine API from Harness — 1 operation(s) for quarantine.
  name: Harness Quarantine API
  phrasing_intents:
  - id: deleteQuarantineFilePath
    intent: Release an artifact from quarantine
    question: What does it take to lift quarantine on a package so it can be downloaded again?
  - id: quarantineFilePath
    intent: Quarantine an artifact in a registry
    question: How do I block a vulnerable package version from being pulled from my registry?
  phrasing_ops: 2
  slug: harness-quarantine-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: APIs for observing queued pipeline executions at account level
  name: Harness Queued Pipeline Executions API
  phrasing_intents:
  - id: bulkAbortQueuedPipelines
    intent: Abort several queued pipeline executions
    question: Can I cancel a bunch of queued pipeline runs in one go?
  - id: listQueuedPipelines
    intent: List queued and running pipeline executions
    question: Which pipeline executions are waiting in the queue right now?
  phrasing_ops: 2
  slug: harness-queued-pipeline-executions-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Qwiet/ShiftLeft integration endpoints
  name: Harness Qwiet API
  phrasing_intents:
  - id: Qwiet#GetToken
    intent: Get the account's Qwiet scanner token
    question: Where do I get the Qwiet token and organization ID for my account's security scans?
  - id: Qwiet#GetUserToken
    intent: Get a Qwiet access token for the current user
    question: How do I get a personal Qwiet access token for the signed-in user?
  phrasing_ops: 2
  slug: harness-qwiet-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Get/set cost type preferences for recommendations
  name: Harness Recommendation cost settings API
  phrasing_intents:
  - id: getRecommendationCostSettings
    intent: Get recommendation cost settings
    question: Which cost settings are used to calculate savings in my recommendations?
  - id: updateRecommendationCostSettings
    intent: Update recommendation cost settings
    question: Can I change the pricing preferences used for AWS and Azure recommendations?
  phrasing_ops: 2
  slug: harness-recommendation-cost-settings-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Recommendation CRUD apis for recommendations ignore list.
  name: Harness Recommendation Ignore List API
  phrasing_intents:
  - id: addRecommendationsIgnoreList
    intent: Ignore resources in cost recommendations
    question: Can I stop getting cost recommendations for specific workloads or EC2 instances?
  - id: getRecommendationsIgnoreList
    intent: List resources ignored in recommendations
    question: Which resources am I currently ignoring in cost recommendations?
  - id: removeRecommendationsIgnoreList
    intent: Stop ignoring resources in recommendations
    question: How do I start getting recommendations again for a resource I ignored?
  phrasing_ops: 3
  slug: harness-recommendation-ignore-list-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Recommendation CRUD apis for jira.
  name: Harness Recommendation Jira API
  phrasing_intents:
  - id: createRecommendationJira
    intent: Open a Jira ticket for a cost recommendation
    question: How do I create a Jira issue from a cloud cost recommendation?
  - id: getJiraFieldMappings
    intent: List Jira field mappings for recommendations
    question: Which Jira fields are mapped to savings and variance values on my account?
  - id: upsertJiraFieldMapping
    intent: Replace Jira field mappings for a field type
    question: How do I set which Jira field receives the savings amount?
  - id: deleteJiraFieldMapping
    intent: Delete a Jira field mapping for a project
    question: How do I remove the Jira field mapping for one Jira project?
  - id: deleteJiraFromRecommendations
    intent: Unlink Jira tickets from recommendations
    question: How do I clear the Jira ticket details attached to recommendations?
  - id: getJiraStatuses
    intent: List Jira statuses
    question: What Jira statuses can a recommendation ticket be in?
  - id: getCommonJiraFields
    intent: Find Jira fields shared across projects
    question: Which Jira fields exist in all of the projects and issue types I selected?
  - id: getCommonJiraIssueTypes
    intent: Find Jira issue types shared across projects
    question: Which issue types are available in every one of my selected Jira projects?
  phrasing_ops: 10
  slug: harness-recommendation-jira-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Recommendation apis for recommendations preferences.
  name: Harness Recommendation Preferences API
  phrasing_intents:
  - id: updateCloudAccountOverride
    intent: Update a cloud account preset override
    question: How do I change which cloud accounts an existing recommendation override applies to?
  - id: deleteCloudAccountOverride
    intent: Delete a cloud account preset override
    question: How do I remove a cloud account level recommendation override?
  - id: getRecommendationPreferences
    intent: Get recommendation preferences
    question: What look-back period and presets are applied to my cost recommendations?
  - id: updatePreset
    intent: Update recommendation preferences
    question: How do I change the look-back period used for cost recommendations?
  - id: getCloudAccountOverrideOverview
    intent: Get an overview of cloud account overrides
    question: How many cloud account overrides exist per resource type?
  - id: listCloudAccountOverridesByResourceType
    intent: List cloud account overrides for a resource type
    question: Which cloud account overrides apply to a given resource type?
  - id: createCloudAccountOverride
    intent: Create a cloud account preset override
    question: How do I apply a different recommendation preset to specific cloud accounts?
  phrasing_ops: 7
  slug: harness-recommendation-preferences-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Recommendation apis for recommendations presets.
  name: Harness Recommendation Presets API
  phrasing_intents:
  - id: updatePreset_1
    intent: Update a cost recommendation preset
    question: Can I rename or re-describe an existing recommendation preset?
  - id: deletePreset
    intent: Delete a cost recommendation preset
    question: Can I remove a recommendation preset I no longer use?
  - id: getRecommendationPresets
    intent: List cost recommendation presets
    question: Which recommendation presets exist in my Harness cloud cost account?
  - id: createPreset
    intent: Create a cost recommendation preset
    question: How do I save my preferences for cost recommendations as a preset?
  phrasing_ops: 4
  slug: harness-recommendation-presets-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Recommendation CRUD apis for servicenow.
  name: Harness Recommendation Servicenow API
  phrasing_intents:
  - id: createRecommendationServicenowTicket
    intent: Open a ServiceNow ticket for a cost recommendation
    question: How do I send a cloud cost recommendation to ServiceNow so an owner acts on it?
  - id: getServiceNowServiceRequestFields
    intent: List ServiceNow service request fields
    question: Which ServiceNow fields can I fill in when raising a ticket from a recommendation?
  phrasing_ops: 2
  slug: harness-recommendation-servicenow-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Recommendation apis for recommendations tags.
  name: Harness Recommendation Tags API
  phrasing_intents:
  - id: getRecommendationTags
    intent: Get tags on a cost recommendation
    question: What tags are attached to a specific cost recommendation?
  - id: getTagsForFilterPanel
    intent: List tag keys and values for recommendation filters
    question: Which tag keys can I filter cost recommendations by?
  phrasing_ops: 2
  slug: harness-recommendation-tags-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Recommendations for workloads and node pools.
  name: Harness Recommendations API
  phrasing_intents:
  - id: appliedRecommendationResourceStats
    intent: Get savings from applied recommendations by resource
    question: How much have we saved from cost recommendations we already applied, per resource type?
  - id: changeInferenceState
    intent: Verify or reject an inferred recommendation
    question: Can I mark an inferred cost recommendation as verified or rejected?
  - id: changeRecommendationState
    intent: Mark a recommendation as applied or open
    question: How do I mark a cost recommendation as applied?
  - id: recommendationsCount
    intent: Count cost recommendations
    question: How many cost recommendations do we have right now?
  - id: recommendationFilterValues
    intent: List values for recommendation filters
    question: What values can I pick for each recommendation filter column?
  - id: getSupportedRecommendationFilters
    intent: List supported recommendation filter fields
    question: Which fields am I allowed to filter recommendations on?
  - id: iacmResourceRecommendations
    intent: Get recommendations for IaCM-managed resources
    question: Can I get cost recommendations for resources managed by Terraform in IaCM?
  - id: listRecommendations
    intent: List cost recommendations
    question: What cost-saving recommendations are open for my cloud resources?
  phrasing_ops: 12
  slug: harness-recommendations-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Recommendations details for workloads and node pools.
  name: Harness Recommendations Details API
  phrasing_intents:
  - id: azureVmRecommendationDetail
    intent: Get an Azure VM rightsizing recommendation
    question: What does a cost recommendation suggest for one of my Azure VMs?
  - id: ec2RecommendationDetail
    intent: Get an EC2 instance recommendation
    question: What instance change is recommended for an EC2 machine?
  - id: ecsRecommendationDetail
    intent: Get an ECS service recommendation
    question: What CPU and memory does a recommendation suggest for my ECS service?
  - id: nodeRecommendationDetail
    intent: Get a Kubernetes node pool recommendation
    question: What node pool sizing is recommended for my cluster?
  - id: workloadRecommendationDetail
    intent: Get a Kubernetes workload recommendation
    question: What resource requests are recommended for a Kubernetes workload?
  phrasing_ops: 5
  slug: harness-recommendations-details-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Reconciler API from Harness — 3 operation(s) for reconciler.
  name: Harness Reconciler API
  phrasing_intents:
  - id: ReconcilerService_ListAutoCreateLogs
    intent: List logs of resources the GitOps import auto-created
    question: Which services, environments and cluster links were auto-created during a GitOps import?
  - id: ReconcilerService_CollectCounts
    intent: Count GitOps entities on a cluster before import
    question: How many Argo entities exist on the cluster behind a GitOps agent?
  - id: ReconcilerService_ImportData
    intent: Import cluster data into Harness via a GitOps agent
    question: How do I import existing Argo apps and clusters into Harness through an agent?
  phrasing_ops: 3
  slug: harness-reconciler-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Reference Identifiers Lookup
  name: Harness Reference Identifiers API
  phrasing_intents:
  - id: ReferenceIdentifiers#getByReferenceId
    intent: Look up a security reference identifier
    question: What does a vulnerability reference ID found in a security scan refer to?
  phrasing_ops: 1
  slug: harness-reference-identifiers-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: APIs to create, update, list registries
  name: Harness Registries API
  phrasing_intents:
  - id: CreateRegistry
    intent: Create an artifact registry
    question: How do I create a new Docker or Helm registry in Harness Artifact Registry?
  - id: DeleteRegistry
    intent: Delete an artifact registry
    question: How do I delete an entire artifact registry?
  - id: GetRegistry
    intent: Get an artifact registry's details
    question: What package type, visibility and cleanup policy does a registry have?
  - id: ModifyRegistry
    intent: Update an artifact registry
    question: How do I add a cleanup policy or blocked pattern to an existing registry?
  - id: GetAllArtifactsByRegistry
    intent: List artifacts in a registry
    question: Which artifacts are stored in a particular registry?
  - id: GetClientSetupDetails
    intent: Get CLI setup steps for a registry
    question: How do I configure docker or helm on my machine to push to this registry?
  phrasing_ops: 6
  slug: harness-registries-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: registry V2 endpoints
  name: Harness Registry V2 API
  phrasing_intents:
  - id: ListVersions
    intent: List artifact versions in the registry
    question: Which versions of a package are stored in my artifact registry?
  - id: Copy
    intent: Copy an artifact between registries
    question: How do I promote an artifact from one registry to another?
  - id: GetFile
    intent: Download a registry file by its path
    question: How do I download a single file from my artifact registry by its path?
  - id: CreateBulkDownloadRequest
    intent: Start a bulk download of registry packages
    question: Can I download several packages or versions from a registry in one archive?
  - id: GetBulkDownloadRequestStatus
    intent: Check the status of a bulk download request
    question: Is my registry bulk download finished yet?
  - id: SearchFiles
    intent: Search files in a registry
    question: How do I find files in a registry by a search query?
  - id: DeleteMetadata
    intent: Delete metadata keys from a registry entity
    question: How do I remove specific metadata keys from a package in my registry?
  - id: GetMetadata
    intent: Get metadata for a package, version or registry
    question: What metadata key-value pairs are attached to a package version in my registry?
  phrasing_ops: 15
  slug: harness-registry-v2-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Registry V3 - Bulk Deletion API from Harness — 1 operation(s) for registry v3 - bulk deletion.
  name: Harness Registry V3 - Bulk Deletion API
  phrasing_intents:
  - id: BulkDeleteV3
    intent: Bulk delete packages and versions from a registry
    question: Can I delete many packages or versions from an artifact registry at once?
  phrasing_ops: 1
  slug: harness-registry-v3-bulk-deletion-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: V3 files endpoints
  name: Harness Registry V3 - Files API
  phrasing_intents:
  - id: ListFilesV3
    intent: List files across artifact registries
    question: Which files belong to a given package version in my artifact registry?
  - id: GetFileV3
    intent: Download a registry file by id
    question: How do I download the bytes of a registry file when I know its id?
  - id: GetFileMetadataV3
    intent: Get metadata for a registry file
    question: What metadata is attached to a single file in my registry?
  - id: UpsertFileMetadataV3
    intent: Add or overwrite metadata keys on a registry file
    question: Can I add a metadata key to a file without erasing its other metadata?
  - id: SaveFileMetadataV3
    intent: Replace all metadata on a registry file
    question: How do I overwrite every metadata entry on a file so only new ones remain?
  - id: GetFilePreviewV3
    intent: Get an inline preview URL for a registry file
    question: How do I get a browser-viewable link to preview a registry file?
  - id: SearchRegistryFilesV3
    intent: Search registry files by path regex
    question: Can I find files in a registry using a regular expression on their path?
  - id: ListRegistryFilesV3
    intent: List files in a named registry
    question: What files are stored in one registry I can name?
  phrasing_ops: 8
  slug: harness-registry-v3-files-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Registry V3 - Filters API from Harness — 2 operation(s) for registry v3 - filters.
  name: Harness Registry V3 - Filters API
  phrasing_intents:
  - id: ListFiltersV3
    intent: List registry filter definitions
    question: Which filters can I apply when browsing registries, packages or versions?
  - id: ListFilterOptionsV3
    intent: List selectable values for one registry filter
    question: What values can I pick for a specific registry filter?
  phrasing_ops: 2
  slug: harness-registry-v3-filters-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: V3 firewall endpoints
  name: Harness Registry V3 - Firewall API
  phrasing_intents:
  - id: AddBuildInfoV3
    intent: Record build info from a package install
    question: How does the CLI report package installation build info to the registry?
  - id: ListPipelineBuildInfoDetailsV3
    intent: List pipeline build info details
    question: Which pipelines installed a given package version?
  - id: GetArtifactScansV3
    intent: List artifact firewall scan results
    question: Which artifacts in my registries were flagged by firewall scans?
  - id: GetArtifactScanDetailsV3
    intent: Get the details of one artifact scan
    question: Why was a specific artifact blocked by the firewall scan?
  - id: InitiateBulkScanEvaluationV3
    intent: Start an asynchronous bulk firewall evaluation
    question: Can I trigger firewall policy evaluation for many artifacts in the background?
  - id: BulkEvaluateArtifactsV3
    intent: Evaluate up to 50 artifacts synchronously
    question: Can I get firewall results immediately for a batch of artifacts without saving anything?
  - id: GetBulkScanEvaluationStatusV3
    intent: Check a bulk scan evaluation's status
    question: Is my bulk firewall evaluation finished?
  - id: EvaluateArtifactScanV3
    intent: Re-evaluate an artifact scan
    question: Can I rerun the firewall evaluation for an artifact after a policy change?
  phrasing_ops: 14
  slug: harness-registry-v3-firewall-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: V3 internal admin endpoints for search backfill
  name: Harness Registry V3 - Internal API
  phrasing_intents:
  - id: TriggerBackfillV3
    intent: Start a registry search index backfill
    question: How do I rebuild the artifact registry search index for an account?
  - id: GetBackfillStateV3
    intent: Get registry search backfill state
    question: What state is the registry search backfill in for my account?
  - id: GetBackfillTaskStatusV3
    intent: Get the status of a backfill job
    question: Has a specific search backfill job finished yet?
  phrasing_ops: 3
  slug: harness-registry-v3-internal-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: V3 lifecycle rule endpoints
  name: Harness Registry V3 - Lifecycle API
  phrasing_intents:
  - id: ListLifecycleExecutionsV3
    intent: List artifact lifecycle rule runs
    question: Which artifact registry lifecycle executions have run recently?
  - id: CreateLifecycleExecutionV3
    intent: Dry-run a registry lifecycle rule
    question: Can I preview what a lifecycle rule would clean up before it actually runs?
  - id: GetLifecycleExecutionV3
    intent: Get one lifecycle execution
    question: What was the outcome of a specific lifecycle rule execution?
  - id: ListLifecycleExecutionItemsV3
    intent: List artifacts evaluated in a lifecycle run
    question: Which artifacts did a lifecycle execution evaluate, and what happened to each?
  - id: ListLifecycleRulesV3
    intent: List artifact lifecycle rules
    question: What artifact retention and cleanup rules are configured in my registry?
  - id: CreateLifecycleRuleV3
    intent: Create an artifact lifecycle rule
    question: How do I set up a rule that cleans up old artifacts in my registry?
  - id: DeleteLifecycleRuleV3
    intent: Delete a lifecycle rule
    question: How do I delete an artifact lifecycle rule?
  - id: GetLifecycleRuleV3
    intent: Get one lifecycle rule
    question: What criteria and schedule does a specific lifecycle rule use?
  phrasing_ops: 11
  slug: harness-registry-v3-lifecycle-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: V3 metadata endpoints
  name: Harness Registry V3 - Metadata API
  phrasing_intents:
  - id: DeleteMetadataV3
    intent: Delete a registry metadata entry
    question: How do I remove a metadata key-value pair from the artifact registry?
  - id: GetMetadataKeysV3
    intent: List metadata keys used in the registry
    question: What metadata keys are in use across my artifact registry?
  - id: GetMetadataValuesV3
    intent: List values recorded for a metadata key
    question: Which values have been set for a particular metadata key in the registry?
  phrasing_ops: 3
  slug: harness-registry-v3-metadata-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: V3 packages endpoints
  name: Harness Registry V3 - Packages API
  phrasing_intents:
  - id: ListPackagesV3
    intent: List packages in the artifact registry
    question: Which packages and images are stored across my Harness artifact registries?
  - id: DeletePackageV3
    intent: Delete a package or image
    question: How do I delete a package or container image from the registry?
  - id: GetPackageMetadataV3
    intent: Get a package's metadata
    question: What custom metadata key-value pairs are attached to a package?
  - id: UpsertPackageMetadataV3
    intent: Add or update metadata keys on a package
    question: Can I add one metadata key to a package without touching the others?
  - id: SavePackageMetadataV3
    intent: Replace all metadata on a package
    question: How do I wipe a package's metadata and replace it with a new set in one call?
  - id: RestorePackageV3
    intent: Restore a soft-deleted package
    question: I deleted a package by mistake — can I get it back?
  - id: GetPackagesStatsV3
    intent: Get size and download stats for packages
    question: How many downloads and how much storage do a set of packages account for?
  phrasing_ops: 7
  slug: harness-registry-v3-packages-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Registry V3 - Principals API from Harness — 1 operation(s) for registry v3 - principals.
  name: Harness Registry V3 - Principals API
  phrasing_intents:
  - id: ListPrincipalsV3
    intent: List artifact registry principals
    question: Which users and service accounts can be granted access in the artifact registry?
  phrasing_ops: 1
  slug: harness-registry-v3-principals-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: V3 registries endpoints
  name: Harness Registry V3 - Registries API
  phrasing_intents:
  - id: ListRegistriesV3
    intent: List artifact registries
    question: Which artifact registries exist in my Harness account?
  - id: DeleteRegistryV3
    intent: Delete an artifact registry
    question: How do I delete a registry, and is it soft-deleted by default?
  - id: GetRegistryMetadataV3
    intent: Get a registry's metadata
    question: What metadata key-values are attached to a registry?
  - id: UpsertRegistryMetadataV3
    intent: Add or overwrite metadata keys on a registry
    question: Can I add a few metadata keys to a registry without replacing the rest?
  - id: SaveRegistryMetadataV3
    intent: Replace all metadata on a registry
    question: How do I overwrite a registry's metadata so only my new set remains?
  - id: MigrateRegistryV3
    intent: Convert a generic registry to a raw registry
    question: How do I migrate a GENERIC registry to the RAW type?
  - id: RebuildRegistryIndexV3
    intent: Rebuild a registry's package index
    question: My registry index looks out of date; can I rebuild it?
  - id: RestoreRegistryV3
    intent: Restore a soft-deleted registry
    question: Can I bring back a registry I deleted by mistake?
  phrasing_ops: 9
  slug: harness-registry-v3-registries-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: V3 system-level endpoints for registry configuration and discovery
  name: Harness Registry V3 - System API
  phrasing_intents:
  - id: GetSystemInfoV3
    intent: Get the artifact registry hostname for an account
    question: What registry hostname should I push and pull artifacts to in Harness Artifact Registry?
  phrasing_ops: 1
  slug: harness-registry-v3-system-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: V3 transfer endpoints
  name: Harness Registry V3 - Transfer API
  phrasing_intents:
  - id: CreateBulkDownloadRequestV3
    intent: Start a bulk download of registry packages
    question: Can I download many artifact registry packages as one archive?
  - id: GetBulkDownloadRequestStatusV3
    intent: Check a bulk download request's status
    question: Is my bulk package download ready yet?
  - id: CopyResourcesV3
    intent: Copy artifacts between registries
    question: Can I copy packages from one artifact registry to another?
  phrasing_ops: 3
  slug: harness-registry-v3-transfer-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: V3 versions endpoints
  name: Harness Registry V3 - Versions API
  phrasing_intents:
  - id: ListVersionsV3
    intent: List package versions in the artifact registry
    question: Which package versions are stored in my Harness Artifact Registry?
  - id: DeleteVersionV3
    intent: Delete a package version
    question: How do I delete one version of a package from the registry?
  - id: ListConanRecipeRevisionsV3
    intent: List Conan recipe revisions for a version
    question: What Conan recipe revisions (RREVs) exist for this package version?
  - id: GetConanRecipeRevisionDetailV3
    intent: Get details of a Conan recipe revision
    question: What's recorded about a specific Conan recipe revision?
  - id: ListConanPackagesV3
    intent: List Conan packages under a recipe revision
    question: Which binary packages (PKGIDs) were built for a Conan recipe revision?
  - id: GetConanPackageDetailV3
    intent: Get a Conan package and its revisions
    question: What details and package revisions are attached to a specific Conan PKGID?
  - id: ListConanPackageRevisionsV3
    intent: List revisions of a Conan package
    question: What package revisions (PREVs) exist for a Conan binary package?
  - id: GetConanPackageRevisionDetailV3
    intent: Get details of a Conan package revision
    question: What's recorded for one specific Conan package revision (PREV)?
  phrasing_ops: 16
  slug: harness-registry-v3-versions-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Release Groups API from Harness — 5 operation(s) for release groups.
  name: Harness Release Groups API
  phrasing_intents:
  - id: post-releaseGroup
    intent: Create a release group from YAML
    question: How do I create a new release group?
  - id: delete-releaseGroup
    intent: Delete a release group
    question: How do I delete a release group?
  - id: put-releaseGroup
    intent: Replace a release group's definition
    question: How do I update a release group with new YAML?
  - id: get-releaseGroup
    intent: Get a release group
    question: What's in a specific release group?
  - id: patch-releaseGroup
    intent: Toggle scheduled auto-execution for a release group
    question: Can releases run automatically when their scheduled time arrives?
  - id: get-releaseGroup-summary
    intent: List release groups
    question: What release groups exist in my project?
  - id: get-releaseGroup-releaseGroupId-components
    intent: Get the components of a release group
    question: Which components are included in a release group?
  - id: getReleaseConflicts
    intent: List conflicts in a release group
    question: Are there any release conflicts in this release group?
  phrasing_ops: 8
  slug: harness-release-groups-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Releases API from Harness — 11 operation(s) for releases.
  name: Harness Releases API
  phrasing_intents:
  - id: postReleaseAdhoc
    intent: Create an ad hoc release
    question: Can I schedule a one-off release outside the normal release group cadence?
  - id: postReleaseSummary
    intent: Summarize releases over time ranges
    question: Which releases are scheduled in the next few weeks?
  - id: get-release
    intent: Get a release's details
    question: What are the details of a specific release?
  - id: put-release-releaseId
    intent: Update a release's schedule and definition
    question: How do I reschedule a release to a new start time and duration?
  - id: getReleaseActivities
    intent: List a release's activities in a time window
    question: What activities are part of a release between two dates?
  - id: getReleaseDayActivities
    intent: Get a release's activities for a calendar day view
    question: What does a release's calendar look like day by day?
  - id: get-release-releaseId-approvals
    intent: List approval activity for a release
    question: Which approvals are still pending on a release?
  - id: get-release-releaseId-environmentDashboard
    intent: View the environment dashboard for a release
    question: What is deployed to each environment in a release?
  phrasing_ops: 12
  slug: harness-releases-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Project-level remediation agent configuration
  name: Harness Remediation Agent API
  phrasing_intents:
  - id: remediation-agent#disable-project-remediation
    intent: Turn off AI remediation for a project
    question: How do I stop AI remediation from running on a project's workspaces?
  - id: remediation-agent#get-project-remediation-config
    intent: Check whether AI remediation is on for a project
    question: Is AI remediation enabled for my infrastructure-as-code project?
  - id: remediation-agent#enable-project-remediation
    intent: Turn on AI remediation for a project
    question: How do I enable AI remediation for every workspace in a project?
  - id: RemediationAgent#DiffOccurrences
    intent: Compare a validation scan against the original
    question: Did the remediation agent's validation run actually remove the vulnerabilities from the original scan?
  - id: RemediationAgent#ListOccurrencesInScope
    intent: List occurrences in scope for remediation
    question: Which issue occurrences in a scan will the remediation agent try to fix?
  - id: RemediationAgent#BatchPersistResults
    intent: Save a remediation agent run's results
    question: How are per-occurrence results from a remediation agent run recorded?
  phrasing_ops: 6
  slug: harness-remediation-agent-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Remediation API from Harness — 17 operation(s) for remediation.
  name: Harness Remediation API
  phrasing_intents:
  - id: createRemediationTracker
    intent: Open a vulnerability remediation tracker
    question: How do I start tracking remediation of a vulnerable component across my Harness project?
  - id: listRemediations
    intent: List remediation trackers in a project
    question: Which remediation trackers are open in my project right now?
  - id: updateRemediationTracker
    intent: Update a remediation tracker's details
    question: Can I change the severity or target date on a remediation tracker that already exists?
  - id: getOverallSummary
    intent: Summarize all remediation trackers
    question: What does the overall remediation picture look like for my project?
  - id: closeRemediationTracker
    intent: Close a remediation tracker
    question: How do I mark a remediation tracker as closed once the fix has shipped?
  - id: excludeArtifact
    intent: Exclude an artifact from a remediation tracker
    question: Can I remove an artifact that isn't affected from a remediation tracker's scope?
  - id: getRemediationDetails
    intent: Get a remediation tracker's details
    question: What's the current state and scope of one specific remediation tracker?
  - id: getArtifactListForRemediation
    intent: List artifacts tracked by a remediation
    question: Which artifacts are affected by a given remediation tracker?
  phrasing_ops: 21
  slug: harness-remediation-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Replication API from Harness — 6 operation(s) for replication.
  name: Harness Replication API
  phrasing_intents:
  - id: listReplicationRules
    intent: List registry replication rules
    question: Which replication rules are copying artifacts between my registries?
  - id: createReplicationRule
    intent: Create a registry replication rule
    question: How do I set up replication from an external registry into Harness Artifact Registry?
  - id: deleteReplicationRule
    intent: Delete a replication rule
    question: How do I stop and remove a replication rule entirely?
  - id: getReplicationRule
    intent: Get a replication rule
    question: What source, destination and patterns does a replication rule use?
  - id: updateReplicationRule
    intent: Update a replication rule
    question: How do I change the allowed patterns on an existing replication rule?
  - id: listMigrationImages
    intent: List images in a replication migration
    question: Which images are being migrated under a replication rule?
  - id: getMigrationLogsForImage
    intent: Get migration logs for an image
    question: Why did one image fail to migrate?
  - id: startMigration
    intent: Start a replication migration
    question: How do I kick off the migration for a replication rule?
  phrasing_ops: 9
  slug: harness-replication-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Reports API from Harness — 4 operation(s) for reports.
  name: Harness Reports API
  phrasing_intents:
  - id: postReleaseReportGenerate
    intent: Generate a CSV report for a release
    question: Can I produce a CSV report for one release over a date range?
  - id: postReleaseGroupReportGenerate
    intent: Generate a CSV report for a release group
    question: How do I get one CSV report covering every release in a release group?
  - id: getReportStatus
    intent: Check a release report job's status
    question: Is my release report finished generating yet?
  - id: getReportDownload
    intent: Download a completed release report
    question: Where do I download the CSV once a release report is ready?
  phrasing_ops: 4
  slug: harness-reports-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Read APIs backing the STO Target Code Repositories page.
  name: Harness Repositories API
  phrasing_intents:
  - id: AgentRepositoryService_ListRepositories
    intent: List repositories configured on a GitOps agent
    question: Which Git repositories are connected to my Harness GitOps agent?
  - id: AgentRepositoryService_CreateRepository
    intent: Add a repository to a GitOps agent
    question: How do I register a new Git or Helm repository with a GitOps agent?
  - id: AgentRepositoryService_CheckExternalSecretsOperator
    intent: Check if External Secrets Operator is installed
    question: Is External Secrets Operator installed where my GitOps agent runs?
  - id: AgentRepositoryService_ListESOGenerators
    intent: List ESO generators in an agent namespace
    question: Which External Secrets generators are installed in my GitOps agent's namespace?
  - id: AgentRepositoryService_CheckOCIRepoType
    intent: Detect the repository type of an OCI repo
    question: What kind of repository is behind this OCI URL?
  - id: AgentRepositoryService_ValidateAccess
    intent: Validate connection access to a repository
    question: Can my GitOps agent actually connect to this repo with these credentials?
  - id: AgentRepositoryService_Get
    intent: Get a GitOps repository or its credentials
    question: What is configured for a specific repository on my GitOps agent?
  - id: AgentRepositoryService_DeleteRepository
    intent: Remove a repository from a GitOps agent
    question: How do I remove a repository from my GitOps agent's configuration?
  phrasing_ops: 24
  slug: harness-repositories-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The repository API from Harness — 38 operation(s) for repository.
  name: Harness Repository API
  phrasing_intents:
  - id: listRepos
    intent: List code repositories
    question: Which Git repositories exist in my Harness Code project?
  - id: createRepository
    intent: Create a new code repository
    question: How do I create a new Git repository in Harness Code?
  - id: deleteRepository
    intent: Soft delete a repository
    question: How do I delete a repository in Harness Code?
  - id: getRepository
    intent: Get a repository's details
    question: Where can I see the details of a single code repository?
  - id: updateRepository
    intent: Update a repository's description or tags
    question: Can I change a repository's description after it's created?
  - id: listRepoActivities
    intent: List activity on a repository
    question: What recent activity has happened in a repository?
  - id: archive
    intent: Download a repository as an archive
    question: Can I download a snapshot of a repo at a specific branch or tag as a zip or tarball?
  - id: getBlame
    intent: Show git blame for a file
    question: Who last changed each line of a file in my repo?
  phrasing_ops: 49
  slug: harness-repository-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Repository Certificates API from Harness — 1 operation(s) for repository certificates.
  name: Harness Repository Certificates API
  phrasing_intents:
  - id: AgentCertificateService_List
    intent: List repository certificates on a GitOps agent
    question: Which repository TLS and SSH certificates are installed on my GitOps agent?
  - id: AgentCertificateService_Delete
    intent: Remove repository certificates from a GitOps agent
    question: How do I delete repository certificates from a GitOps agent?
  - id: AgentCertificateService_Create
    intent: Add repository certificates to a GitOps agent
    question: How do I add a TLS or SSH known-host certificate so a GitOps agent trusts my repo server?
  phrasing_ops: 3
  slug: harness-repository-certificates-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Repository credentials API from Harness — 4 operation(s) for repository credentials.
  name: Harness Repository credentials API
  phrasing_intents:
  - id: AgentRepositoryCredentialsService_CreateRepositoryCredentials
    intent: Create a GitOps repository credential template
    question: How do I add a credential template so a GitOps agent can access many repos?
  - id: AgentRepositoryCredentialsService_GetCredentialsForRepositoryUrl
    intent: Find the credential that matches a repo URL
    question: Which credential template would a GitOps agent use for a given repository URL?
  - id: AgentRepositoryCredentialsService_GetRepositoryCredentials
    intent: Get a GitOps repository credential
    question: Where can I see one repository credential template by its identifier?
  - id: AgentRepositoryCredentialsService_DeleteRepositoryCredentials
    intent: Delete a GitOps repository credential
    question: How do I remove a repository credential template from a GitOps agent?
  - id: AgentRepositoryCredentialsService_UpdateRepositoryCredentials
    intent: Update a GitOps repository credential
    question: How do I rotate the password or key in a repository credential template?
  - id: AgentRepositoryCredentialsService_ListRepositoryCredentials
    intent: List GitOps repository credentials
    question: Which repository credential templates are configured for GitOps?
  phrasing_ops: 6
  slug: harness-repository-credentials-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The resource API from Harness — 2 operation(s) for resource.
  name: Harness Resource API
  phrasing_intents:
  - id: listGitignore
    intent: List available .gitignore templates
    question: Which .gitignore templates can I pick when creating a Harness Code repository?
  - id: listLicenses
    intent: List available license templates
    question: Which open source licenses can I add when creating a Harness Code repository?
  phrasing_ops: 2
  slug: harness-resource-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The RI Inventory APIs API from Harness — 3 operation(s) for ri inventory apis.
  name: Harness RI Inventory APIs API
  phrasing_intents:
  - id: ListReservedInstances
    intent: List Reserved Instances
    question: Which Reserved Instances do I own across my cloud accounts?
  - id: GetReservedInstanceDetails
    intent: Get details of a Reserved Instance
    question: What are the term, payment option and utilization of a specific Reserved Instance?
  - id: GetRIFilterOptions
    intent: Get filter options for Reserved Instances
    question: What instance types, platforms and accounts can I filter Reserved Instances by?
  phrasing_ops: 3
  slug: harness-ri-inventory-apis-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The RI Inventory Overview API from Harness — 1 operation(s) for ri inventory overview.
  name: Harness RI Inventory Overview API
  phrasing_intents:
  - id: GetRIInventoryOverview
    intent: Get an overview of Reserved Instance inventory
    question: How many Reserved Instances do I have, and how are they distributed by status?
  phrasing_ops: 1
  slug: harness-ri-inventory-overview-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Risks API from Harness — 8 operation(s) for risks.
  name: Harness Risks API
  phrasing_intents:
  - id: getExperimentationActivityReport
    intent: Generate a chaos experimentation activity report
    question: How much chaos experimentation did my account run last quarter?
  - id: getOverallServiceUsageStats
    intent: Get overall chaos service usage stats by type
    question: What's the overall chaos service usage broken down by type for my account?
  - id: getServiceUsageReport
    intent: Generate a chaos service usage report
    question: Can I produce a service usage report for chaos engineering over a timeframe?
  - id: getAccountServiceUsageStats
    intent: Get chaos service usage grouped by day or month
    question: How does my chaos service usage trend day by day?
  - id: getAccountServiceDetails
    intent: List per-service chaos usage details
    question: Which individual services used chaos engineering in a given time frame?
  - id: listRisks
    intent: List chaos resilience risks
    question: What resilience risks have been defined for my chaos project?
  - id: createRisk
    intent: Create a resilience risk
    question: How do I register a new resilience risk to track with chaos probes?
  - id: getRisk
    intent: Get a resilience risk
    question: Can I look up one risk and see its category and tags?
  phrasing_ops: 11
  slug: harness-risks-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for CRUD on role assignments
  name: Harness Role Assignments API
  phrasing_intents:
  - id: bulkDeleteRoleAssignment
    intent: Delete several role assignments at once
    question: Can I revoke a batch of role assignments in one request?
  - id: postRoleAssignments
    intent: Create multiple role assignments in a scope
    question: How do I grant roles to many users or groups in one call?
  - id: getRoleAssignmentList
    intent: List role assignments in a scope
    question: Who has which roles in my account?
  - id: postRoleAssignment
    intent: Assign a role to a principal
    question: How do I give a user a role on a resource group?
  - id: getRoleAssignment
    intent: Get one role assignment
    question: What role and resource group does a particular role assignment grant?
  - id: deleteRoleAssignment
    intent: Delete a role assignment
    question: How do I revoke a single role assignment from a user?
  - id: getFilteredRoleAssignmentList
    intent: Filter role assignments by role, principal or group
    question: Which users hold a specific role in this scope?
  - id: getRoleAssignmentAggregateList
    intent: List role assignments with role and group metadata
    question: Can I get role assignments together with the role and resource group details in one response?
  phrasing_ops: 10
  slug: harness-role-assignments-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for CRUD on roles
  name: Harness Roles API
  phrasing_intents:
  - id: getRoleList
    intent: List roles in a scope
    question: What roles exist in my Harness project?
  - id: postRole
    intent: Create a custom role
    question: How do I create a custom role with specific permissions?
  - id: getRole
    intent: Get a role and its permissions
    question: Which permissions does a particular role grant?
  - id: putRole
    intent: Update a custom role
    question: How do I add or remove permissions on a custom role?
  - id: deleteRole
    intent: Delete a custom role
    question: How do I delete a custom role?
  phrasing_ops: 5
  slug: harness-roles-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Post Prod Rollback of specific service
  name: Harness Rollback API
  phrasing_intents:
  - id: checkIfInstanceCanBeRolledBack
    intent: Check whether a service instance can be rolled back
    question: Before I roll back, can Harness tell me if this service instance is eligible?
  - id: triggerRollback
    intent: Roll back a service instance
    question: How do I trigger a rollback for a specific deployed instance?
  - id: triggerRollbackV2
    intent: Roll back a service in an environment
    question: Can I roll back a service in a given environment without knowing the instance key?
  - id: triggerRollbackV3
    intent: Roll back several service targets at once
    question: Can I trigger rollbacks for multiple services and environments in one request?
  phrasing_ops: 4
  slug: harness-rollback-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Rollouts API from Harness — 1 operation(s) for rollouts.
  name: Harness Rollouts API
  phrasing_intents:
  - id: RolloutsService_GetRolloutStatus
    intent: Get the status of an Argo Rollout
    question: Is my progressive rollout healthy, paused or degraded right now?
  phrasing_ops: 1
  slug: harness-rollouts-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Governance Rule Management
  name: Harness Rule API
  phrasing_intents:
  - id: CloneRule
    intent: Clone a cloud governance rule
    question: Can I copy an existing governance rule to start a new one from it?
  - id: updateRule
    intent: Update a cloud governance rule
    question: How do I change the policy of an existing governance rule?
  - id: CreateNewRule
    intent: Create a cloud governance rule
    question: Can I add a new custom rule to Cloud Asset Governance?
  - id: getGovernanceRule
    intent: Get a governance rule by ID
    question: What policy does a particular governance rule enforce?
  - id: deleteRule
    intent: Delete a governance rule
    question: How do I remove a governance rule I no longer need?
  - id: enqueueGovernanceJob
    intent: Queue governance evaluation jobs
    question: How do I queue a governance rule enforcement to be evaluated against a cloud account?
  - id: simpleEnqueueAdhocGovernanceRule
    intent: Run a governance rule ad hoc
    question: Can I run one governance rule right now against a few cloud accounts?
  - id: costCoRelationSupportedResources
    intent: List resources that support cost correlation
    question: Which cloud resource types can governance correlate with cost?
  phrasing_ops: 15
  slug: harness-rule-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Rule Executions
  name: Harness Rule Executions API
  phrasing_intents:
  - id: exportEvaluations
    intent: Export governance rule evaluation data
    question: Can I export my cloud governance rule evaluations for offline analysis?
  - id: getRuleExecutions
    intent: List governance rule executions
    question: Which cloud governance rules have run in my Harness account recently?
  - id: getRuleExecutionsFilterValues
    intent: Get filter options for rule executions
    question: What values can I filter governance rule executions by?
  - id: getRuleExecution
    intent: Get one governance rule execution
    question: What was the outcome of a specific governance rule execution?
  - id: getRuleExecutionActionedResources
    intent: List resources a rule execution acted on
    question: Which cloud resources did a governance rule actually take action on?
  - id: getRuleExecutionDetails
    intent: Get resource files or logs for a rule execution
    question: Can I pull the resource file for one resource in a governance run?
  - id: getRuleExecutionGranularStatus
    intent: Get per-resource status for a rule execution
    question: What is the granular status of each resource in a governance rule run?
  - id: getRuleExecutionLogs
    intent: Get logs for a rule execution
    question: Where can I read the logs from a governance rule execution?
  phrasing_ops: 13
  slug: harness-rule-executions-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Rule Enforcement
  name: Harness Rule Enforcement API
  phrasing_intents:
  - id: updateEnforcement
    intent: Update a cloud governance rule enforcement
    question: How do I change the schedule or targets of an existing cloud governance enforcement?
  - id: addRuleEnforcement
    intent: Create a cloud governance rule enforcement
    question: How do I schedule a cloud asset governance rule to run automatically against my accounts?
  - id: deleteRuleEnforcement
    intent: Delete a rule enforcement
    question: How do I permanently remove a governance enforcement?
  - id: getRuleEnforcementCount
    intent: Find enforcements that use given rules or rule sets
    question: Which enforcements use a given governance rule before I edit or delete it?
  - id: enforcementDetails
    intent: Get details of a rule enforcement
    question: What rules, schedule and target accounts does a particular enforcement have?
  - id: enforcementSavings
    intent: Get savings produced by a rule enforcement
    question: How much money has a specific governance enforcement saved us?
  - id: getRuleEnforcement
    intent: List rule enforcements by keyword
    question: What governance enforcements exist in my account?
  - id: listRuleEnforcements
    intent: Filter rule enforcements by rule, region or status
    question: Which enforcements are enabled and running in dry-run mode?
  phrasing_ops: 9
  slug: harness-ruleenforcement-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The rules API from Harness — 4 operation(s) for rules.
  name: Harness Rules API
  phrasing_intents:
  - id: repoRuleList
    intent: List a repository's protection rules
    question: What branch protection rules apply to one Harness Code repository?
  - id: repoRuleAdd
    intent: Add a protection rule to a repository
    question: How do I protect the main branch of a single repo from direct pushes?
  - id: repoRuleDelete
    intent: Delete a repository protection rule
    question: Can I remove a branch protection rule from just one repository?
  - id: repoRuleGet
    intent: Get a repository protection rule
    question: What exactly does a given protection rule on my repo enforce?
  - id: repoRuleUpdate
    intent: Update a repository protection rule
    question: Can I temporarily disable a protection rule on a repo without deleting it?
  - id: spaceRuleList
    intent: List protection rules for an account, org or project
    question: Which protection rules are defined at the org or project level rather than per repo?
  - id: spaceRuleAdd
    intent: Add a protection rule for an account, org or project
    question: How do I enforce one branch protection rule across every repo in a project?
  - id: spaceRuleDelete
    intent: Delete an account, org or project protection rule
    question: Can I remove a protection rule that applies across a whole project?
  phrasing_ops: 10
  slug: harness-rules-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Savings Detail API from Harness — 1 operation(s) for savings detail.
  name: Harness Savings Detail API
  phrasing_intents:
  - id: postGatewayLwApiAccountsByAccountIdV2SavingsDetail
    intent: Break down cloud cost savings by dimension
    question: How much have my auto-stopping rules saved over a given date range?
  phrasing_ops: 1
  slug: harness-savings-detail-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Savings Overview API from Harness — 1 operation(s) for savings overview.
  name: Harness Savings Overview API
  phrasing_intents:
  - id: GetSavingsOverview
    intent: Get cloud cost savings overview
    question: How much have we saved overall, and how much of it is managed vs unmanaged?
  phrasing_ops: 1
  slug: harness-savings-overview-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Savings Rate API from Harness — 1 operation(s) for savings rate.
  name: Harness Savings Rate API
  phrasing_intents:
  - id: GetSavingsRate
    intent: Get the effective savings rate
    question: What's my effective savings rate on cloud commitments for a date range?
  phrasing_ops: 1
  slug: harness-savings-rate-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The SBOM API from Harness — 2 operation(s) for sbom.
  name: Harness SBOM API
  phrasing_intents:
  - id: downloadSbomForArtifact
    intent: Download the SBOM for an artifact
    question: How do I download the software bill of materials for a build artifact?
  - id: getSbomScoreForArtifact
    intent: Get the SBOM quality score for an artifact
    question: How complete and high-quality is an artifact's SBOM?
  phrasing_ops: 2
  slug: harness-sbom-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The sbomDrift API from Harness — 3 operation(s) for sbomdrift.
  name: Harness Sbom Drift API
  phrasing_intents:
  - id: calculateDriftForArtifact
    intent: Calculate SBOM drift between two artifact versions
    question: What changed in the SBOM between two tags of the same image?
  - id: getComponentDrift
    intent: List component changes in an SBOM drift
    question: Which components were added, removed or modified between the two versions?
  - id: getLicenseDrift
    intent: List license changes in an SBOM drift
    question: Did any open source licenses change between two builds of the artifact?
  phrasing_ops: 3
  slug: harness-sbomdrift-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The sbomProcessor API from Harness — 2 operation(s) for sbomprocessor.
  name: Harness Sbom Processor API
  phrasing_intents:
  - id: process-sbom
    intent: Normalize and ingest a raw SBOM
    question: How do I turn a raw SBOM into the normalized form used for policy checks?
  - id: enforce-sbom
    intent: Enforce policies on a normalized SBOM
    question: How do I check an artifact's SBOM against our allow and deny policies?
  phrasing_ops: 2
  slug: harness-sbomprocessor-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Access and modify Security Test Scans
  name: Harness Scans API
  phrasing_intents:
  - id: Scans#ListScans
    intent: List security test scans
    question: What security scans have run in my Harness STO account?
  - id: Scans#CreateScan
    intent: Record a new security test scan
    question: How do I register a new security scan record for a pipeline step?
  - id: Scans#DeleteScan
    intent: Delete a security test scan
    question: How do I remove a security scan record I no longer need?
  - id: Scans#FindScanById
    intent: Get a security test scan by ID
    question: What are the details and status of a particular security scan?
  - id: Scans#UpdateScan
    intent: Update an existing security test scan
    question: How do I mark a running security scan as succeeded or failed?
  - id: Scans#ScanIssue
    intent: Get one issue found by a scan
    question: What are the details of one vulnerability a security scan reported?
  - id: Scans#ScanIssueOccurrences
    intent: List occurrences of a scan issue
    question: Where in the code or image does a scan issue occur, and how many times?
  - id: Scans#ScanIssues
    intent: List the issues found by a scan
    question: What vulnerabilities did a particular security scan find?
  phrasing_ops: 10
  slug: harness-scans-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Schemas.
  name: Harness Schemas API
  phrasing_intents:
  - id: get-individual-static-schema
    intent: Get the JSON schema for a pipeline step or stage
    question: Where can I get the JSON schema for one pipeline step or stage type?
  - id: get-inputs-schema
    intent: Get the runtime inputs schema of a pipeline
    question: What runtime inputs does my pipeline YAML expect, as a schema?
  - id: get-template-schema
    intent: Get the JSON schema for a template node
    question: Where do I get the schema for a step or stage template type?
  - id: get-inputs-schema1
    intent: Get the inputs schema of a template
    question: What inputs does a template YAML expect when someone uses it?
  phrasing_ops: 4
  slug: harness-schemas-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The ScmDataPoints API from Harness — 1 operation(s) for scmdatapoints.
  name: Harness Scm Data Points API
  phrasing_intents:
  - id: get-scm-data-point-values
    intent: Get SCM data point values for scorecards
    question: What values do the source control data points return for my catalog entities?
  phrasing_ops: 1
  slug: harness-scmdatapoints-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Scorecard API from Harness — 1 operation(s) for scorecard.
  name: Harness Scorecard API
  phrasing_intents:
  - id: saveSbomScorecard
    intent: Save an SBOM scorecard
    question: How do I store a computed scorecard for an SBOM?
  - id: getSbomScorecard
    intent: Get the SBOM scorecard for an orchestration
    question: How good is the quality score of the SBOM from my orchestration run?
  phrasing_ops: 2
  slug: harness-scorecard-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Scorecards API from Harness — 4 operation(s) for scorecards.
  name: Harness Scorecards API
  phrasing_intents:
  - id: get-scorecards
    intent: List scorecards
    question: Which scorecards are set up in my internal developer portal?
  - id: create-scorecard
    intent: Create a scorecard with checks
    question: How do I create a scorecard to grade catalog components?
  - id: get-scorecard
    intent: Get a scorecard's details
    question: What checks make up a particular scorecard?
  - id: update-scorecard
    intent: Update a scorecard and its checks
    question: Can I add or remove checks from an existing scorecard?
  - id: delete-scorecard
    intent: Delete a scorecard
    question: How do I delete a scorecard we no longer use?
  - id: get-scorecard-stats
    intent: Get a scorecard's stats
    question: How are components scoring against a given scorecard?
  - id: get-entity-facets
    intent: Get entity facets for a catalog kind
    question: What filter facets are available for a given catalog entity kind?
  phrasing_ops: 7
  slug: harness-scorecards-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Scores Information
  name: Harness Scores API
  phrasing_intents:
  - id: get-all-scorecard-summary
    intent: Summarize scorecard scores for an entity
    question: How is a catalog component doing across all its scorecards?
  - id: get-scorecards-scores-overview
    intent: Get per-scorecard scores for an entity
    question: What score does each scorecard give a particular catalog entity?
  - id: get-aggregated-scores
    intent: Aggregate scores across catalog entities
    question: What's the average scorecard score across all our components of a given kind?
  - id: get-scorecards-graphs-score-summary
    intent: Get check status data for score graphs
    question: How have an entity's scorecard checks trended over time?
  - id: scorecard-recalibrate
    intent: Recalculate scorecard scores
    question: I fixed a failing check — can I force the scorecard to recompute now?
  - id: get-scores-recalibrate-status
    intent: Check a score recalibration's progress
    question: Has the scorecard recalculation I kicked off finished yet?
  phrasing_ops: 6
  slug: harness-scores-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Scores Information V2
  name: Harness Scores V2 API
  phrasing_intents:
  - id: scorecard-recalibrate-v2
    intent: Recalibrate scorecard scores
    question: Can I force a scorecard to recompute its scores right away?
  phrasing_ops: 1
  slug: harness-scoresv2-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to SecretManagers as defined in Harness
  name: Harness Secret Managers API
  phrasing_intents:
  - id: getMetadata
    intent: Get a secret manager's metadata
    question: What metadata does a secret manager connection report back?
  phrasing_ops: 1
  slug: harness-secret-managers-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Secrets as defined in Harness
  name: Harness Secrets API
  phrasing_intents:
  - id: countSecretsForScope
    intent: Count the secrets in a scope
    question: How many secrets exist under a given org or project?
  - id: listSecretsV2
    intent: List secrets with query-string filters
    question: What secrets are stored in my Harness project?
  - id: postSecret
    intent: Create a secret
    question: How do I store a new text secret at the project level?
  - id: postSecretFileV2
    intent: Upload a file as a secret
    question: Can I upload a certificate or key file as a secret?
  - id: postSecretViaYaml
    intent: Create a secret from YAML
    question: Can I define a new secret using a YAML document?
  - id: getSecretV2
    intent: Get a secret by its identifier
    question: Can I look up the details of one secret by its ID?
  - id: putSecret
    intent: Update a secret
    question: How do I rotate the value of an existing text secret?
  - id: deleteSecretV2
    intent: Delete a secret
    question: Can I force-delete a secret that is still referenced somewhere?
  phrasing_ops: 14
  slug: harness-secrets-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This has all the APIs specific to the Service Accounts in Harness.
  name: Harness Service Account API
  phrasing_intents:
  - id: listServiceAccount
    intent: List service accounts
    question: Which service accounts exist in my account, org or project?
  - id: createServiceAccount
    intent: Create a service account
    question: How do I create a service account for automation?
  - id: updateServiceAccount
    intent: Update a service account
    question: Can I rename a service account or change its email?
  - id: deleteServiceAccount
    intent: Delete a service account
    question: How do I remove a service account that's no longer used?
  - id: getAggregatedServiceAccount
    intent: Get a service account with its roles
    question: What roles and details does a single service account have in this scope?
  - id: getInheritingChildScopeListForServiceAccount
    intent: List child scopes inheriting a service account
    question: Which orgs and projects inherit a given service account?
  - id: listAggregatedServiceAccounts
    intent: List service accounts with role details
    question: Can I list service accounts together with their role bindings?
  - id: listManageableServiceAccounts
    intent: List service accounts I can manage keys for
    question: Which service accounts am I allowed to manage API keys on?
  phrasing_ops: 8
  slug: harness-service-account-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Service Dashboard
  name: Harness Service Dashboard API
  phrasing_intents:
  - id: pipelineExecutionCount
    intent: Count pipeline executions for a service
    question: How many pipeline executions deployed a given service over a period?
  phrasing_ops: 1
  slug: harness-service-dashboard-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The ServiceLevelObjective API from Harness — 2 operation(s) for servicelevelobjective.
  name: Harness Service Level Objective API
  phrasing_intents:
  - id: getMetricGraphForSLO
    intent: Get the metric graph behind an SLO
    question: What metrics are driving a particular SLO?
  - id: listSlo
    intent: List SLOs with filters
    question: Which SLOs belong to a composite SLO?
  phrasing_ops: 2
  slug: harness-servicelevelobjective-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Service Overrides V2
  name: Harness Service Overrides API
  phrasing_intents:
  - id: updateServiceOverride
    intent: Update an existing service override
    question: How do I change the values of a service override I already created?
  - id: createServiceOverride
    intent: Create a service override for an environment
    question: How do I override a service's variables or manifests for one environment?
  - id: getServiceOverrides
    intent: Get a service override by identifier
    question: What values does a particular service override apply?
  - id: deleteServiceOverride_1
    intent: Delete a service override
    question: How do I remove a service override so the defaults apply again?
  - id: serviceOverrideMoveConfigs
    intent: Move a service override between inline and git
    question: Can I move a service override's YAML out of Harness and into a git repo?
  - id: updateServiceOverrideGitDetails
    intent: Update the git metadata of a remote service override
    question: I renamed the repo holding my service override - how do I relink it?
  phrasing_ops: 6
  slug: harness-serviceoverrides-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Services
  name: Harness Services API
  phrasing_intents:
  - id: checkAllowedValuesInServices
    intent: Check services for allowed-values usage
    question: Do any of my Harness services use allowed-values in their inputs?
  - id: getServiceList
    intent: List deployment services
    question: What deployment services are defined in my project?
  - id: updateServiceV2
    intent: Update an existing service
    question: How do I change the YAML or description of an existing service?
  - id: createServiceV2
    intent: Create a single service
    question: How do I create a new deployment service in a Harness project?
  - id: createServicesV2
    intent: Create several services in one batch
    question: Can I create many services in a single request?
  - id: createServicesPartialBatch
    intent: Batch-create services allowing partial success
    question: What happens if some services in a batch fail to create?
  - id: getServiceV2
    intent: Get a service by identifier
    question: What is the definition of one specific service?
  - id: deleteServiceV2
    intent: Delete a service
    question: How do I delete a service I no longer deploy?
  phrasing_ops: 17
  slug: harness-services-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Settings as defined in Harness
  name: Harness Setting API
  phrasing_intents:
  - id: getSettingValue
    intent: Get a setting's value
    question: What value is a specific Harness setting set to?
  - id: getSettingsList
    intent: List settings in a category
    question: Which settings exist under a given category?
  - id: updateSettingValue
    intent: Update setting values
    question: How do I change one or more settings at once?
  phrasing_ops: 3
  slug: harness-setting-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Settings service handles all API endpoints related to configuration settings
  name: Harness Settings API
  phrasing_intents:
  - id: findSpaceGeneralSettings
    intent: Get general Code repository settings for a scope
    question: What default branch is configured for new Harness Code repositories in my project?
  - id: updateSpaceGeneralSettings
    intent: Change the default branch for a scope
    question: How do I change the default branch name used for new repositories?
  - id: settings#delete-default-pipeline
    intent: Remove a default pipeline association
    question: How do I stop a pipeline from being the default for a provisioner operation?
  - id: settings#list-default-pipelines
    intent: List default pipelines for IaC operations
    question: Which pipelines run by default for plan and apply operations in my IaCM project?
  - id: settings#upsert-default-pipeline
    intent: Set the default pipeline for a provisioner operation
    question: How do I make a specific pipeline the default for Terraform plan runs in a project?
  - id: settings#check-push-data
    intent: Check if plan and state upload is disabled
    question: Is my IaCM project set to send Terraform plans and state back to the server?
  - id: settings#disable-project-drift
    intent: Turn off drift detection for a whole project
    question: How do I switch off drift detection for every workspace in a project?
  - id: settings#get-project-drift
    intent: Get project drift detection settings
    question: Is drift detection turned on for all workspaces in my project, and on what schedule?
  phrasing_ops: 12
  slug: harness-settings-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Slack Utils API from Harness — 1 operation(s) for slack utils.
  name: Harness Slack Utils API
  phrasing_intents:
  - id: slackOauthTokenGenerate
    intent: Exchange a Slack authorization code for a token
    question: How does Harness turn a Slack OAuth code into a token?
  phrasing_ops: 1
  slug: harness-slack-utils-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to SLOs dashboard
  name: Harness SLOs dashboard API
  phrasing_intents:
  - id: getSLOAssociatedEnvironmentIdentifiers
    intent: List environments that have SLOs
    question: Which environments have service level objectives attached?
  - id: getSLOAssociatedMonitoredServices
    intent: List monitored services that have SLOs
    question: Which monitored services have SLOs defined on them?
  - id: getSecondaryEventDetails
    intent: Get details of SLO secondary events
    question: What happened in a specific annotation or downtime event on my SLO chart?
  - id: getSecondaryEvents
    intent: List secondary events for an SLO in a time range
    question: What secondary events like downtime affected an SLO during a time window?
  - id: getServiceLevelObjectivesRiskCount
    intent: Count SLOs by error budget risk
    question: How many of our SLOs are at risk of exhausting their error budget?
  - id: getSloConsumptionBreakdownView
    intent: Get an SLO's error budget consumption breakdown
    question: What consumed the error budget of an SLO over a period?
  - id: getSLODetails
    intent: Get dashboard details for one SLO
    question: What is the current health and error budget of a specific SLO?
  - id: getSLOHealthListView
    intent: List SLO health using query filters
    question: What is the health of all SLOs in my project?
  phrasing_ops: 9
  slug: harness-slos-dashboard-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Slsa API from Harness — 3 operation(s) for slsa.
  name: Harness Slsa API
  phrasing_intents:
  - id: saveProvenance
    intent: Store SLSA provenance for a pipeline build
    question: Where do I store the SLSA provenance a pipeline step generated?
  - id: getProvenance
    intent: Get SLSA provenance for an artifact
    question: What SLSA build provenance was recorded for an artifact?
  - id: saveSlsaVerification
    intent: Record the SLSA verification result
    question: Can I record whether an artifact passed SLSA provenance verification?
  - id: saveSlsaPolicyViolations
    intent: Record SLSA policy violations
    question: How do I save the policy violations found when verifying SLSA provenance?
  phrasing_ops: 4
  slug: harness-slsa-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The slsaV2 API from Harness — 2 operation(s) for slsav2.
  name: Harness Slsa V2 API
  phrasing_intents:
  - id: saveProvenanceV2
    intent: Save SLSA provenance for an artifact
    question: How do I record build provenance for an artifact in my project?
  - id: saveSlsaVerificationV2
    intent: Save an SLSA verification result
    question: How do I store whether an artifact passed SLSA verification?
  phrasing_ops: 2
  slug: harness-slsav2-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to SmtpConfig as defined in Harness
  name: Harness SMTP API
  phrasing_intents:
  - id: deleteSmtpConfig
    intent: Delete the SMTP configuration
    question: How do I remove the SMTP server configuration from my account?
  - id: getSmtpConfig
    intent: Get the account's SMTP configuration
    question: Which SMTP server does Harness use to send email for my account?
  - id: updateSmtp
    intent: Update the SMTP configuration
    question: How do I change the SMTP host or credentials Harness sends mail through?
  - id: createSmtpConfig
    intent: Create an SMTP configuration
    question: How do I set up an SMTP server so Harness can send notification emails?
  - id: validateConnectivity
    intent: Send a test email through the SMTP config
    question: How can I check my SMTP settings work by sending a test email?
  - id: validateName
    intent: Check an SMTP config name is available
    question: Is the name I want for an SMTP config already used by another connector?
  phrasing_ops: 6
  slug: harness-smtp-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Contains APIs related to Source Code Manager
  name: Harness Source Code Manager API
  phrasing_intents:
  - id: updateSourceCodeManager
    intent: Update a source code manager
    question: How do I change the credentials of a source code manager I've linked?
  - id: deleteSourceCodeManager
    intent: Delete a source code manager
    question: Can I remove a source code manager I no longer use?
  - id: getSourceCodeManagers
    intent: List source code managers
    question: Which source code managers are set up in my account?
  - id: createSourceCodeManager
    intent: Add a source code manager
    question: How do I connect a Git provider as a source code manager?
  phrasing_ops: 4
  slug: harness-source-code-manager-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The SP Inventory APIs API from Harness — 3 operation(s) for sp inventory apis.
  name: Harness SP Inventory APIs API
  phrasing_intents:
  - id: ListSavingsPlans
    intent: List Savings Plans in inventory
    question: Which Savings Plans does my cloud account hold?
  - id: GetSavingsPlanDetails
    intent: Get one Savings Plan's details
    question: What are the details of a specific Savings Plan?
  - id: GetSPFilterOptions
    intent: Get Savings Plan filter options
    question: What filter values exist for Savings Plans, like instance families or payment options?
  phrasing_ops: 3
  slug: harness-sp-inventory-apis-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The SP Inventory Overview API from Harness — 1 operation(s) for sp inventory overview.
  name: Harness SP Inventory Overview API
  phrasing_intents:
  - id: GetSPInventoryOverview
    intent: Get a Savings Plans inventory overview
    question: How many Savings Plans do I have, and what state are they in?
  phrasing_ops: 1
  slug: harness-sp-inventory-overview-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Spaces API from Harness — 8 operation(s) for spaces.
  name: Harness Spaces API
  phrasing_intents:
  - id: GetArtifactStatsForSpace
    intent: Get artifact stats for a space
    question: How many artifacts and downloads does a registry space have?
  - id: GetAllArtifacts
    intent: List artifacts across a space's registries
    question: What artifacts are stored in the registries of this space?
  - id: GetStorageDetails
    intent: Get storage usage for a space
    question: How much registry storage is a space using?
  - id: RegistrylistSpaceLabels
    intent: List labels defined in a space
    question: What labels are defined in this space?
  - id: RegistrydefineSpaceLabel
    intent: Define a new label in a space
    question: How do I define a new label key for a space?
  - id: RegistrysaveSpaceLabel
    intent: Save a label and its values in a space
    question: Can I create or overwrite a label together with its values in one call?
  - id: RegistrydeleteSpaceLabel
    intent: Delete a label from a space
    question: How do I delete a label key from a space?
  - id: findSpaceLabel
    intent: Get one label in a space
    question: What does a particular label in my space look like?
  phrasing_ops: 14
  slug: harness-spaces-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Spend Details API from Harness — 1 operation(s) for spend details.
  name: Harness Spend Details API
  phrasing_intents:
  - id: SpendDetails
    intent: Break down spend across RIs, Savings Plans and on-demand
    question: How much of our compute spend is covered by reserved instances or savings plans versus on-demand?
  phrasing_ops: 1
  slug: harness-spend-details-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Spend Overview API from Harness — 1 operation(s) for spend overview.
  name: Harness Spend Overview API
  phrasing_intents:
  - id: SpendOverview
    intent: Break down cloud spend by RI, Savings Plans and on-demand
    question: How much of my compute spend went to reserved instances versus Savings Plans versus on-demand?
  phrasing_ops: 1
  slug: harness-spend-overview-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to CRUD operations of srm notifications
  name: Harness Srm Notification API
  phrasing_intents:
  - id: getNotificationRuleData
    intent: Get a service reliability notification rule
    question: What conditions and channel does a specific SRM notification rule use?
  - id: updateNotificationRuleData
    intent: Update a service reliability notification rule
    question: Can I change the conditions that trigger an existing SRM notification rule?
  - id: deleteNotificationRuleData
    intent: Delete a service reliability notification rule
    question: Can I remove an SRM notification rule that's too noisy?
  - id: getNotificationRuleData_1
    intent: List service reliability notification rules
    question: Which notification rules are set up for monitored services and SLOs in my project?
  - id: saveNotificationRuleData
    intent: Create a service reliability notification rule
    question: How do I set up a new SRM notification rule?
  phrasing_ops: 5
  slug: harness-srm-notification-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The sscaPipelineView API from Harness — 2 operation(s) for sscapipelineview.
  name: Harness Ssca Pipeline View API
  phrasing_intents:
  - id: getSSCASummary
    intent: Get the supply chain summary for a run
    question: What does the supply chain security tab show for a pipeline execution?
  - id: getPipelineArtifactList
    intent: List artifacts produced by a pipeline run
    question: Which artifacts did a pipeline execution produce?
  phrasing_ops: 2
  slug: harness-sscapipelineview-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The status_checks API from Harness — 3 operation(s) for status_checks.
  name: Harness Status Checks API
  phrasing_intents:
  - id: listStatusCheckRecentSpace
    intent: List recent status checks across an account or project
    question: Which status checks have run recently across all repos in my project?
  - id: listStatusCheckResults
    intent: List status check results for a commit
    question: Did all the status checks pass on a specific commit?
  - id: reportStatusCheckResults
    intent: Report a status check result on a commit
    question: How do I post a CI check result back to a commit?
  - id: listStatusCheckRecent
    intent: List recent status checks in a repository
    question: What status checks have run lately in one repository?
  phrasing_ops: 4
  slug: harness-status-checks-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Status Information
  name: Harness Status Info API
  phrasing_intents:
  - id: get-status-info-by-type
    intent: Get status info of a given type
    question: What's the current status recorded for a given status type in my account?
  - id: save-status-info-by-type
    intent: Save status info of a given type
    question: How do I record a new status for a given status type?
  phrasing_ops: 2
  slug: harness-statusinfo-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The StatusInfoV2 API from Harness — 1 operation(s) for statusinfov2.
  name: Harness Status Info V2 API
  phrasing_intents:
  - id: get-status-info-type-v2
    intent: Get status info by type
    question: What's the current status information for a given type?
  phrasing_ops: 1
  slug: harness-statusinfov2-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Steps.
  name: Harness Steps API
  phrasing_intents:
  - id: get-steps
    intent: Get steps for the pipeline step palette
    question: Which steps can I add to a pipeline stage from the step palette?
  phrasing_ops: 1
  slug: harness-steps-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Endpoints that power the other modules micro-frontend with STO data
  name: Harness STO Data Frontend API
  phrasing_intents:
  - id: STODataFrontend#AllIssuesFilters
    intent: Get available issue filter values for scan targets
    question: Which severities, scanners and issue types can I filter on for a set of scan targets?
  - id: STODataFrontend#AllIssuesList
    intent: List security issues for scan targets
    question: What security vulnerabilities were found for my scanned targets?
  - id: STODataFrontend#ExecutionArtifactScanSummary
    intent: Count active security issues per scanner
    question: How many active security issues did each scanner find for my pipeline executions' artifacts?
  - id: STODataFrontend#ExecutionArtifactSummary
    intent: Summarize active security issues for artifacts
    question: What's the overall count of active security issues across the artifacts from my pipeline runs?
  - id: STODataFrontend#ExecutionSummary
    intent: Summarize security issues for one pipeline execution
    question: How many active security issues did a single pipeline execution produce?
  - id: STODataFrontend#ExecutionIssueCounts
    intent: Count security issues across pipeline executions
    question: How many active security issues exist across several pipeline executions' targets?
  phrasing_ops: 6
  slug: harness-sto-data-frontend-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for Streaming Destinations.
  name: Harness Streaming Destinations API
  phrasing_intents:
  - id: create-streaming-destinations
    intent: Create an audit streaming destination
    question: How do I start streaming Harness audit events to my own storage?
  - id: get-streaming-destinations
    intent: List audit streaming destinations
    question: Where are my audit logs being streamed to?
  - id: getStreamingDestinationsAggregate
    intent: List streaming destinations with aggregates
    question: Is there an aggregated view of my streaming destinations and their streaming state?
  - id: update-streaming-destination
    intent: Update a streaming destination
    question: How do I disable a streaming destination before deleting it?
  - id: delete-disabled-streaming-destination
    intent: Delete a disabled streaming destination
    question: Can I delete a streaming destination that's still active?
  - id: get-streaming-destination
    intent: Get a streaming destination
    question: What connector and spec does one streaming destination use?
  - id: validateUniqueIdentifier
    intent: Check a streaming destination id is unique
    question: Is a streaming destination identifier already in use?
  - id: get-streaming-destinations-cards
    intent: Get streaming destination summary cards
    question: What summary counts appear on the streaming destinations page?
  phrasing_ops: 8
  slug: harness-streaming-destinations-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Unauthenticated support endpoints
  name: Harness System API
  phrasing_intents:
  - id: System#health
    intent: Check the STO service health
    question: Is the Security Testing Orchestration service up right now?
  - id: System#version
    intent: Get the STO service version
    question: Which version of the Security Testing Orchestration service is running?
  - id: system#health
    intent: Check the policy management service health
    question: Is the policy management service responding?
  - id: system#version
    intent: Get the policy management service version
    question: What version of the policy management service is deployed?
  - id: IaCMsystem#health
    intent: Check the IaCM server health
    question: Is the Infrastructure as Code Management server healthy?
  - id: system#latest-plugin-version
    intent: Look up the latest IaCM plugin version
    question: Is the IaCM plugin I'm running the newest release?
  - id: system#get-provisioner-config
    intent: Get an IaC provisioner's configuration
    question: What configuration settings does a given IaC provisioner expose?
  - id: system#list-supported-provisioner-versions
    intent: List supported versions of a provisioner
    question: Which versions of a provisioner can my IaCM workspaces use?
  phrasing_ops: 9
  slug: harness-system-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: APIs to create and manage Feature Flag Tags
  name: Harness Tags API
  phrasing_intents:
  - id: GetAllTags
    intent: List feature flag tags
    question: What tags are used on feature flags in my project?
  - id: CreateTag
    intent: Create a feature flag tag
    question: Can I create a new tag to organize feature flags?
  - id: DeleteTag
    intent: Delete a feature flag tag
    question: Can I delete a tag that's no longer needed?
  - id: GetTag
    intent: Get a feature flag tag
    question: Which feature flags are associated with a specific tag?
  phrasing_ops: 4
  slug: harness-tags-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: APIs to create and manage Feature Flag Target Groups
  name: Harness Target Groups API
  phrasing_intents:
  - id: GetAllSegments
    intent: List feature flag target groups
    question: Which target groups exist in my feature flag environment?
  - id: CreateSegment
    intent: Create a target group
    question: Can I create a group of targets to roll a feature flag out to?
  - id: DeleteSegment
    intent: Delete a target group
    question: Can I delete a target group I no longer use?
  - id: GetSegment
    intent: Get a target group
    question: What rules and members does a specific target group have?
  - id: PatchSegment
    intent: Update a target group
    question: Can I add or remove targets in an existing target group?
  - id: GetAvailableFlagsForSegment
    intent: List flags a target group can be added to
    question: Which feature flags could I still add this target group to?
  - id: GetSegmentFlags
    intent: List feature flags that use a target group
    question: Which feature flags currently include a given target group?
  phrasing_ops: 7
  slug: harness-target-groups-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Access and modify Scan Target Variants
  name: Harness Target Variants API
  phrasing_intents:
  - id: TargetVariants#ListTargetVariants
    intent: List variants of a scan target
    question: Which variants, like branches or tags, exist for a security scan target?
  - id: TargetVariants#CreateTargetVariant
    intent: Create a scan target variant
    question: How do I add a new variant to a security scan target?
  - id: TargetVariants#DeleteTargetVariant
    intent: Delete a scan target variant
    question: How do I remove a variant from a scan target?
  - id: TargetVariants#FindTargetVariantById
    intent: Get one scan target variant
    question: What parameters does a specific scan target variant have?
  - id: TargetVariants#UpdateTargetVariant
    intent: Update a scan target variant
    question: How do I change the parameters of an existing target variant?
  phrasing_ops: 5
  slug: harness-target-variants-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: APIs to create and manage Feature Flag Targets
  name: Harness Targets API
  phrasing_intents:
  - id: GetAllTargets
    intent: List feature flag targets in an environment
    question: Which feature flag targets exist in one of my environments?
  - id: CreateTarget
    intent: Create a feature flag target
    question: How do I register a new user or device as a feature flag target?
  - id: UploadTargets
    intent: Bulk add targets from a CSV file
    question: Can I import a batch of feature flag targets from a CSV?
  - id: DeleteTarget
    intent: Delete a feature flag target
    question: How do I remove a target from an environment?
  - id: GetTarget
    intent: Get a feature flag target's details
    question: How do I look up one feature flag target and its attributes?
  - id: PatchTarget
    intent: Apply patch instructions to a target
    question: Can I change a target with patch instructions, like adding it to a target group?
  - id: ModifyTarget
    intent: Replace a target's name and attributes
    question: How do I overwrite a target's full definition, including attributes?
  - id: GetTargetSegments
    intent: List the target groups a target belongs to
    question: Which target groups is a particular target a member of?
  phrasing_ops: 8
  slug: harness-targets-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to tas
  name: Harness Tas API
  phrasing_intents:
  - id: getTasOrganizations
    intent: List Tanzu Application Service organizations
    question: Which Tanzu Application Service organizations can my TAS connector see?
  - id: getTasSpaces
    intent: List TAS spaces via a connector
    question: Which spaces exist in a Tanzu organization when I query through a connector?
  - id: getTasSpacesV2
    intent: List TAS spaces for an infrastructure definition
    question: Which TAS spaces are available for a given environment and infrastructure definition?
  phrasing_ops: 3
  slug: harness-tas-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Teams
  name: Harness Teams API
  phrasing_intents:
  - id: get-team-hierarchy
    intent: Get the team hierarchy
    question: What does our team and sub-team hierarchy look like?
  - id: get-team-owned-entities
    intent: List catalog entities a team owns
    question: Which services and components does a particular team own?
  phrasing_ops: 2
  slug: harness-teams-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains a list of APIs specific to the Templates Validations and Refresh
  name: Harness Templates API
  phrasing_intents:
  - id: getRefreshedYaml
    intent: Refresh template inputs inside a YAML
    question: My pipeline YAML has stale template inputs — can Harness give me a version with them refreshed?
  - id: TemplatevalidateTemplateInputs
    intent: Validate the inputs of a template version
    question: Are the template inputs in my pipeline still valid for this template version?
  - id: getYamlWithTemplateRefsResolvedV2
    intent: Resolve all template references in a YAML
    question: How can I see a pipeline's full YAML with every template reference expanded?
  - id: createTemplate
    intent: Create a pipeline template
    question: How do I create a new reusable template in Harness?
  - id: deleteTemplateVersion
    intent: Delete a version of a template
    question: Can I delete one version of a template while keeping the others?
  - id: getTemplate
    intent: Get a template
    question: Where can I view the YAML of a template and its current stable version?
  - id: getTemplateInputSetYaml
    intent: Get the runtime inputs YAML of a template
    question: Which runtime inputs does a template expect when I use it?
  - id: getTemplateLabelsMap
    intent: List custom labels on template versions
    question: What custom labels are attached to each version of a template?
  phrasing_ops: 16
  slug: harness-templates-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Access and modify Scan Targets
  name: Harness Test Targets API
  phrasing_intents:
  - id: Targets#ListTargets
    intent: List security test targets
    question: Which test targets are defined for security scanning in my project?
  - id: Targets#CreateTarget
    intent: Create a security test target
    question: How do I create a new test target for security scans?
  - id: Targets#DeleteTarget
    intent: Delete a test target
    question: How do I delete a test target I no longer scan?
  - id: Targets#FindTargetById
    intent: Get a test target by ID
    question: How do I look up one test target and its settings?
  - id: Targets#PatchTarget
    intent: Change selected fields on a test target
    question: Can I change just the baseline of a test target without resending everything?
  - id: Targets#UpdateTarget
    intent: Replace a test target's definition
    question: How do I fully replace a test target's name, type and baseline?
  - id: Targets#ListTargetExecutions
    intent: List a test target's scan history
    question: What is the scan history for a test target, newest first?
  - id: Targets#GetTargetExecution
    intent: Get metadata for one target execution
    question: Which pipeline and build produced a given target scan execution?
  phrasing_ops: 13
  slug: harness-test-targets-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: HTTP standard backend for Terraform
  name: Harness Tf Standard Backend API
  phrasing_intents:
  - id: tf-standard-backend#pull-terraform-state
    intent: Read a workspace's Terraform state
    question: How do I read the current Terraform state stored for an IaCM workspace?
  - id: tf-standard-backend#push-terraform-state
    intent: Save new Terraform state for a workspace
    question: How does Terraform push updated state to a Harness workspace backend?
  - id: tf-standard-backend#unlock-workspace
    intent: Release a Terraform workspace lock
    question: How do I release the state lock on a stuck Terraform workspace?
  - id: tf-standard-backend#lock-workspace
    intent: Lock a Terraform workspace's state
    question: How do I lock a workspace so two Terraform runs don't change state at once?
  phrasing_ops: 4
  slug: harness-tf-standard-backend-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Token as defined in Harness
  name: Harness Token API
  phrasing_intents:
  - id: createToken
    intent: Create an API key token
    question: How do I create a new token under an API key in Harness?
  - id: updateToken
    intent: Update an existing token
    question: How do I rename or change the description of an existing token?
  - id: deleteToken
    intent: Delete a token
    question: How do I delete a token so it can no longer be used?
  - id: listAggregatedTokens
    intent: List tokens across API keys
    question: Which tokens exist for my service account API keys?
  - id: rotateToken
    intent: Rotate a token
    question: How do I rotate a token without creating a new one from scratch?
  - id: validateToken
    intent: Validate a token
    question: Is this Harness token still valid for my account?
  - id: Token#IssueToken
    intent: Issue a cross-service token for STO
    question: How do I exchange my Harness token for a Security Testing Orchestration cross-service token?
  - id: Token#IssueToken1
    intent: Issue a cross-service token (v1)
    question: Is there a v1 endpoint for issuing a cross-service token?
  phrasing_ops: 8
  slug: harness-token-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Total users count API from Harness — 1 operation(s) for total users count.
  name: Harness Total users count API
  phrasing_intents:
  - id: get-v1-devSubscriptions
    intent: Get monthly developer user counts for a year
    question: How many users did my account have each month this year?
  phrasing_ops: 1
  slug: harness-total-users-count-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs for performing CRUD operations on Triggers.
  name: Harness Triggers API
  phrasing_intents:
  - id: create-trigger
    intent: Create a pipeline trigger (v1 API)
    question: How do I add a trigger to a pipeline using the v1 org/project API?
  - id: get-trigger
    intent: Retrieve a pipeline trigger (v1 API)
    question: How do I read a trigger's definition through the v1 org/project path?
  - id: update-trigger
    intent: Update a pipeline trigger (v1 API)
    question: How do I edit a trigger through the v1 org/project API?
  - id: delete-trigger
    intent: Delete a pipeline trigger (v1 API)
    question: How do I remove a trigger using the v1 org/project path?
  - id: getListForTarget
    intent: List triggers for a target pipeline
    question: What triggers are set up on a pipeline, with paging and search?
  - id: createTrigger
    intent: Create a trigger with the pipeline service endpoint
    question: How do I create a trigger for a target pipeline with the classic pipeline service API?
  - id: createTriggerV2
    intent: Create a trigger with an executor identity (v2)
    question: Can I create a trigger that runs as a specific executor identity?
  - id: getTrigger
    intent: Get a trigger via the pipeline service
    question: How do I fetch a trigger by identifier from the classic pipeline service API?
  phrasing_ops: 14
  slug: harness-triggers-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Trigger Event History.
  name: Harness Triggers Events API
  phrasing_intents:
  - id: polledResponseTriggerIdentifier
    intent: Get polled responses for a trigger
    question: What did a polling trigger see the last times it checked for new artifacts or manifests?
  - id: triggerEventHistoryNew
    intent: Get event history for a trigger
    question: Why didn't my pipeline trigger fire, and what events did it receive?
  - id: triggerEventHistoryUsingFilters
    intent: Filter trigger events by status and type
    question: Which trigger events for a pipeline failed, filtered by status?
  - id: triggerHistoryEventCorrelation
    intent: Get trigger events by correlation ID
    question: Which trigger events share one event correlation ID?
  - id: triggerHistoryEventCorrelationV2
    intent: Get trigger events by correlation ID (v2)
    question: Is there a v2 endpoint for looking up trigger history by correlation ID?
  - id: triggerEventHistoryBuildSourceType
    intent: Get artifact and manifest trigger history
    question: What events did my artifact and manifest triggers receive, by build source type?
  phrasing_ops: 6
  slug: harness-triggersevents-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Unified Executions Service handles the API for unified workflow executions.
  name: Harness Unified Executions API
  phrasing_intents:
  - id: unified-executions#create-unified-execution
    intent: Record a unified infrastructure execution
    question: How do I register an infrastructure-as-code run against a pipeline execution?
  phrasing_ops: 1
  slug: harness-unified-executions-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Unit Metric resource.
  name: Harness Unit Metric API
  phrasing_intents:
  - id: getUnitMetric
    intent: Get a unit metric's records over time
    question: What were the values of a unit cost metric, like cost per customer, over the last month?
  - id: updateUnitMetric
    intent: Update a unit metric definition
    question: How do I change the name or default aggregation of an existing unit metric?
  - id: createUnitMetric
    intent: Create a unit metric
    question: How do I define a new business unit metric, such as cost per transaction?
  - id: deleteUnitMetric
    intent: Delete unit metric records or the whole metric
    question: How do I delete a unit metric's records for a certain time range?
  - id: getColumnUnitMetricForPerspective
    intent: Query a derived unit metric within a perspective
    question: What does a derived unit metric look like when scoped to one cost perspective?
  - id: listAllUnitMetrics
    intent: List all unit metrics in an account
    question: Which unit metrics have been defined in my cloud cost account?
  phrasing_ops: 6
  slug: harness-unit-metric-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Update Module Access API from Harness — 1 operation(s) for update module access.
  name: Harness Update Module Access API
  phrasing_intents:
  - id: put-v1-updateModuleAccess
    intent: Update module access entries
    question: Where do I record updated module access for my Harness account?
  phrasing_ops: 1
  slug: harness-update-module-access-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The upload API from Harness — 2 operation(s) for upload.
  name: Harness Upload API
  phrasing_intents:
  - id: repoArtifactUpload
    intent: Upload a file to a code repository
    question: How do I upload an attachment or artifact to a Harness Code repo?
  - id: repoArtifactDownload
    intent: Download an uploaded file from a repo
    question: Can I download a file that was previously uploaded to a repo?
  phrasing_ops: 2
  slug: harness-upload-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Uploads API from Harness — 2 operation(s) for uploads.
  name: Harness Uploads API
  phrasing_intents:
  - id: presignUpload
    intent: Get a presigned URL to upload release media
    question: How do I get a signed URL to upload an image or video for a release?
  - id: serveUpload
    intent: Retrieve an uploaded release file
    question: How do I retrieve an image or video that was uploaded to a release?
  phrasing_ops: 2
  slug: harness-uploads-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs specific to CD license usage
  name: Harness Usage API
  phrasing_intents:
  - id: downloadCDUsageCSVReport
    intent: Download the CD license usage CSV report
    question: How do I export my Continuous Delivery license usage as a CSV?
  - id: downloadActiveServiceCSVReport
    intent: Download active CD services CSV (platform)
    question: Where can I get a CSV of the CD services that counted as active for licensing?
  - id: getCDLicenseUsageForServiceInstances
    intent: Get CD service-instance license usage (platform)
    question: How many CD service instances am I consuming against my license?
  - id: getCDLicenseUsageForServices
    intent: Get CD services license usage (platform)
    question: How many licensed CD services is my account using right now?
  - id: getLicenseUsage
    intent: Get license usage for a module (platform)
    question: How much of my license is a given Harness module consuming?
  - id: CcmdownloadActiveServiceCSVReport
    intent: Download active CD services CSV via CCM
    question: Can I get the active services CSV from the Cloud Cost Management service path?
  - id: CcmgetCDLicenseUsageForServiceInstances
    intent: Get CD service-instance license usage via CCM
    question: Does the CCM service report CD service-instance license usage too?
  - id: CcmgetCDLicenseUsageForServices
    intent: Get CD services license usage via CCM
    question: Can the Cloud Cost Management service tell me my CD services license usage?
  phrasing_ops: 18
  slug: harness-usage-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to User as defined in Harness
  name: Harness User API
  phrasing_intents:
  - id: addUserToUserGroups
    intent: Set which user groups a user belongs to
    question: How do I put an existing Harness user into a set of user groups?
  - id: addUsers
    intent: Invite users by email to a scope
    question: Can I invite several people by email to a Harness project at once?
  - id: changeUserPassword
    intent: Change my password
    question: How do I change my own login password?
  - id: checkIfLastAdmin
    intent: Check whether a user is the last admin
    question: Is this user the only admin left in the account?
  - id: disableTTwoFactorAuth
    intent: Turn off two-factor authentication for me
    question: How do I switch off two-factor authentication on my Harness login?
  - id: endImpersonation
    intent: End an impersonation session
    question: How do I stop impersonating another user?
  - id: getAggregatedUser
    intent: Get a user's details and role assignments
    question: What roles has a specific user been assigned in a project?
  - id: getAggregatedUsers
    intent: List users with their role assignments
    question: Who has access to this project, and with which roles?
  phrasing_ops: 20
  slug: harness-user-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to User Group as defined in Harness
  name: Harness User Group API
  phrasing_intents:
  - id: getMember
    intent: Check if a user belongs to a user group
    question: Is a specific user a member of this user group?
  - id: putMember
    intent: Add a user to a user group
    question: How do I add one person to a user group?
  - id: deleteMember
    intent: Remove a user from a user group
    question: How do I take someone out of a user group?
  - id: copyUserGroup
    intent: Copy a user group
    question: Can I copy an existing user group?
  - id: getUserGroupList
    intent: List user groups in a scope
    question: What user groups exist in my account, org or project?
  - id: putUserGroup
    intent: Update a user group by user IDs
    question: How do I rename a user group or change its member user IDs?
  - id: postUserGroup
    intent: Create a user group from user IDs
    question: How do I create a new user group with members given by user ID?
  - id: getUserGroup
    intent: Get a user group
    question: What members and settings does a particular user group have?
  phrasing_ops: 20
  slug: harness-user-group-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to User Settings as defined in Harness
  name: Harness User Setting API
  phrasing_intents:
  - id: getUserSettingValue
    intent: Get one user setting's value
    question: What is my current value for a specific user setting?
  - id: getUserSettingsList
    intent: List user settings in a category
    question: Which user settings exist under a given category?
  - id: updateUserSettingValue
    intent: Update my user settings
    question: How do I change one of my Harness user settings?
  - id: getUserPreferencesList
    intent: List my user preferences
    question: What user preferences are saved for me?
  phrasing_ops: 4
  slug: harness-usersetting-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Utilization Overview API from Harness — 1 operation(s) for utilization overview.
  name: Harness Utilization Overview API
  phrasing_intents:
  - id: postGatewayLwApiAccountsByAccountIdV2UtilisationOverview
    intent: Get a utilization overview for cloud resources
    question: What does resource utilization look like across my account for last month?
  phrasing_ops: 1
  slug: harness-utilization-overview-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to SSH or WinRm host validation
  name: Harness Validate Host API
  phrasing_intents:
  - id: validateHosts
    intent: Test connectivity to hosts with a credential
    question: Can Harness reach my target hosts using the credentials stored in a given secret?
  phrasing_ops: 1
  slug: harness-validatehost-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Variable Sets Service handles the API for managing variable sets assigned to workspaces.
  name: Harness Variable Sets API
  phrasing_intents:
  - id: variable_sets#delete-variable-set-by-query-proj-level
    intent: Delete a project variable set by query identifier
    question: Can I delete a project variable set whose identifier contains a slash?
  - id: variable_sets#create-variable-set-proj-level
    intent: Create a project-level variable set
    question: How do I create an IaCM variable set scoped to a single project?
  - id: variable_sets#delete-variable-set-proj-level
    intent: Delete a project variable set by identifier
    question: How do I delete a variable set from one of my projects?
  - id: variable_sets#get-variable-set-proj-level
    intent: Get a project variable set
    question: Where can I see the Terraform variables and connectors inside one project variable set?
  - id: variable_sets#update-variable-set-proj-level
    intent: Update a project variable set
    question: How do I change the Terraform variables in an existing project variable set?
  - id: variable_sets#list-variable-set-references-proj-level
    intent: List where a project variable set is referenced
    question: Which workspaces reference a given project variable set?
  - id: variable_sets#list-variable-sets-proj-level
    intent: List variable sets in a project
    question: What variable sets exist in my IaCM project?
  - id: variable_sets#delete-variable-set-by-query-org-level
    intent: Delete an org variable set by query identifier
    question: Can I delete an organization variable set whose id has characters unsafe in a URL path?
  phrasing_ops: 21
  slug: harness-variable-sets-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Variables as defined in Harness.
  name: Harness Variables API
  phrasing_intents:
  - id: getVariableList
    intent: List platform variables in a scope
    question: What account, org or project variables have we defined in Harness?
  - id: updateVariable
    intent: Update a platform variable
    question: How do I change the value of an existing platform variable?
  - id: createVariable
    intent: Create a platform variable
    question: Can I define a reusable variable at the account or project level?
  - id: getVariable
    intent: Get a platform variable by identifier
    question: Where can I look up one platform variable's value and type?
  - id: deleteVariable
    intent: Delete a platform variable
    question: Is it possible to delete a platform variable we no longer use?
  - id: listVariable
    intent: Fetch several platform variables by identifier
    question: Can I look up a specific set of platform variables in one call by their identifiers?
  - id: variables#list-variables
    intent: List variables on an IaC workspace
    question: What Terraform and environment variables are set on an infrastructure workspace?
  - id: variables#create-variable
    intent: Add a variable to an IaC workspace
    question: How do I add a Terraform variable to an infrastructure workspace?
  phrasing_ops: 12
  slug: harness-variables-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The version API from Harness — 1 operation(s) for version.
  name: Harness Version API
  phrasing_intents:
  - id: getVersion
    intent: Get the supply chain manager version
    question: Which version of the supply chain security manager is running?
  phrasing_ops: 1
  slug: harness-version-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The webhook API from Harness — 10 operation(s) for webhook.
  name: Harness Webhook API
  phrasing_intents:
  - id: listRepoWebhooks
    intent: List webhooks on a code repository
    question: Which webhooks are configured on one of my Harness Code repositories?
  - id: createRepoWebhook
    intent: Add a webhook to a code repository
    question: How do I send push and pull request events from a single repository to my endpoint?
  - id: deleteRepoWebhook
    intent: Delete a repository webhook
    question: How do I stop a repository from calling a webhook endpoint permanently?
  - id: getRepoWebhook
    intent: Get a repository webhook
    question: What URL and triggers is a particular repository webhook set up with?
  - id: updateRepoWebhook
    intent: Update a repository webhook
    question: Can I change the target URL or triggers of an existing repository webhook?
  - id: listRepoWebhookExecutions
    intent: List deliveries of a repository webhook
    question: What deliveries has a repository webhook made recently?
  - id: getRepoWebhookExecution
    intent: Get one delivery of a repository webhook
    question: What request and response did one repository webhook delivery record?
  - id: retriggerRepoWebhookExecution
    intent: Redeliver a repository webhook event
    question: Can I resend a repository webhook delivery that failed?
  phrasing_ops: 16
  slug: harness-webhook-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Contains APIs corresponding to Webhook Triggers.
  name: Harness Webhook Event Handler API
  phrasing_intents:
  - id: processWebhookEvent
    intent: Process a webhook event for triggers
    question: How do I send an incoming webhook payload so it fires my pipeline triggers?
  phrasing_ops: 1
  slug: harness-webhook-event-handler-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Webhook Triggers.
  name: Harness Webhook Triggers API
  phrasing_intents:
  - id: fetchWebhookDetails
    intent: Check how a webhook trigger event was processed
    question: Did Harness receive and process the webhook event I sent to a pipeline trigger?
  - id: fetchWebhookExecutionDetails
    intent: Get the pipeline execution a webhook event started
    question: Which pipeline execution did a given webhook event kick off?
  - id: fetchWebhookExecutionDetailsV2
    intent: Check a queued webhook trigger event
    question: Is my webhook event still queued before it has triggered the pipeline?
  - id: PipelineprocessWebhookEvent
    intent: Send a Git webhook payload to pipeline triggers
    question: Where do I post a Git provider webhook payload so Harness pipeline triggers can react?
  - id: processCustomWebhookEvent
    intent: Fire a custom webhook trigger (original endpoint)
    question: How do I fire a custom webhook trigger with my own payload using the original endpoint?
  - id: processCustomWebhookEventV2
    intent: Fire a custom webhook trigger (v2 endpoint)
    question: What is the v2 custom webhook endpoint for firing a custom trigger?
  - id: processCustomWebhookEventV3
    intent: Fire a custom webhook trigger with a webhook token
    question: How do I fire a custom trigger using a webhook token in the URL?
  phrasing_ops: 7
  slug: harness-webhook-triggers-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: APIs to create, update, list webhooks
  name: Harness Webhooks API
  phrasing_intents:
  - id: ListWebhooks
    intent: List webhooks on an artifact registry
    question: Which webhooks are configured on my artifact registry?
  - id: CreateWebhook
    intent: Create a webhook on an artifact registry
    question: How do I get notified at my own URL when artifacts are pushed to a registry?
  - id: DeleteWebhook
    intent: Delete a registry webhook
    question: How do I stop a registry from calling a webhook for good?
  - id: GetWebhook
    intent: Get a registry webhook
    question: What URL and triggers does a particular registry webhook use?
  - id: UpdateWebhook
    intent: Update a registry webhook
    question: How do I change the target URL of an existing registry webhook?
  - id: ListWebhookExecutions
    intent: List delivery attempts of a registry webhook
    question: Did my registry webhook actually fire, and what did the endpoint respond?
  - id: GetWebhookExecution
    intent: Get one webhook delivery attempt
    question: What request and response were recorded for one webhook delivery?
  - id: ReTriggerWebhookExecution
    intent: Retry a registry webhook delivery
    question: Can I resend a webhook delivery that failed while my endpoint was down?
  phrasing_ops: 8
  slug: harness-webhooks-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Workspace Templates Service handles the API for managing template associations with workspaces.
  name: Harness Workspace Templates API
  phrasing_intents:
  - id: workspace_templates#get-workspace-template-reconciliation-diff
    intent: Preview a workspace's template reconciliation diff
    question: What would change in my workspace YAML if I reconcile it with its template?
  - id: workspace_templates#add-workspace-template
    intent: Link a workspace to a template version
    question: How do I associate a workspace with a workspace template?
  - id: workspace_templates#get-workspaces-by-template-id
    intent: List a project's workspaces that use a template
    question: Which workspaces in this project are linked to a given template?
  - id: workspace_templates#remove-workspace-template
    intent: Unlink a workspace from its template
    question: How do I detach a workspace from a template?
  - id: workspace_templates#update-workspace-template
    intent: Change the template version a workspace uses
    question: How do I move a workspace to a newer version of its template?
  phrasing_ops: 5
  slug: harness-workspace-templates-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Workspaces Service handles the API for managing workspaces and triggering workflows against them.
  name: Harness Workspaces API
  phrasing_intents:
  - id: workspaces#list-all-workspace-tags
    intent: List tags used across workspaces in a project
    question: Which tags are applied to the infrastructure workspaces in my project?
  - id: workspaces#show-workspace-metrics
    intent: Show workspace metrics for a project
    question: What metrics does Harness IaCM report for the workspaces in a project?
  - id: workspaces#list-workspaces
    intent: List infrastructure workspaces in a project
    question: How do I list all the IaCM workspaces in a project?
  - id: workspaces#create-workspace
    intent: Create an infrastructure workspace
    question: How do I create a new Terraform or OpenTofu workspace in Harness IaCM?
  - id: workspaces#destroy-workspace
    intent: Delete a workspace
    question: How do I delete an IaCM workspace I no longer need?
  - id: workspaces#show-workspace
    intent: Show one workspace's details
    question: How do I look up the configuration of a single IaCM workspace?
  - id: workspaces#update-workspace
    intent: Update an existing workspace's settings
    question: How do I change the repository branch or provisioner version on an existing workspace?
  - id: workspaces#force-unlock-workspace
    intent: Force-unlock a locked workspace
    question: How do I clear a stuck lock on a workspace, even one set automatically?
  phrasing_ops: 41
  slug: harness-workspaces-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs specific to the creation of zendesk ticket
  name: Harness Zendesk API
  phrasing_intents:
  - id: createZendeskTicket
    intent: Open a Zendesk support ticket
    question: How do I file a support ticket with Harness from inside the product?
  - id: getCoveoToken
    intent: Get a short-lived Coveo search token
    question: What gives me a temporary token for Coveo support search?
  phrasing_ops: 2
  slug: harness-zendesk-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Zoom Utils API from Harness — 1 operation(s) for zoom utils.
  name: Harness Zoom Utils API
  phrasing_intents:
  - id: zoomOauthTokenGenerate
    intent: Exchange a Zoom authorization code for a token
    question: How does Harness turn a Zoom authorization code into an OAuth token?
  phrasing_ops: 1
  slug: harness-zoom-utils-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to CRUD operations of SLOs
  name: Harness SL Os API
  phrasing_intents:
  - id: getErrorBudgetResetHistory
    intent: Get an SLO's error budget reset history
    question: When was an SLO's error budget last reset, and why?
  - id: getNotificationRulesForSLO
    intent: List notification rules for an SLO
    question: Which alerts fire when an SLO is at risk?
  - id: getServiceLevelObjectiveLogs
    intent: Get an SLO's logs for a time range
    question: Can I see the execution or API call logs behind an SLO?
  - id: resetErrorBudget
    intent: Reset an SLO's error budget
    question: Can I top up an SLO's error budget after an incident was excused?
  - id: getMetricGraphForSLO
    intent: Get the metric graph behind an SLO
    question: What underlying metrics drive a particular SLO?
  - id: listSlo
    intent: List SLOs in a project
    question: Which service level objectives are defined in my project?
  phrasing_ops: 6
  slug: harness-slos-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Account Information
  name: Harness Account Info API
  phrasing_intents:
  - id: get-account-for-namespace
    intent: Look up the account behind a namespace
    question: Which Harness account owns a given namespace?
  phrasing_ops: 1
  slug: harness-account-info-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Account Settings as defined in Harness
  name: Harness Account Setting API
  phrasing_intents:
  - id: getAccountSetting
    intent: Get one type of account setting
    question: What is our account configured to for a particular setting type?
  - id: updateAccountSetting
    intent: Update an account setting
    question: How do I change an account-level configuration setting?
  - id: listAccountSetting
    intent: List all account settings
    question: What account settings are configured overall?
  phrasing_ops: 3
  slug: harness-account-setting-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This contains APIs related to Generative AI Support for Governance
  name: Harness AI Engine API
  phrasing_intents:
  - id: getPromptResources
    intent: List resources supported by AI governance prompts
    question: Which cloud resource types can I write AI governance rules for?
  - id: getPromptRules
    intent: Get sample AI governance rules
    question: Can I see example governance rule prompts for a resource type?
  phrasing_ops: 2
  slug: harness-ai-engine-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: This fetches API keys defined in Harness
  name: Harness API Key API
  phrasing_intents:
  - id: listApiKeys_1
    intent: List API keys for a user or service account
    question: What API keys does a given service account have?
  - id: createApiKey
    intent: Create an API key
    question: How do I create an API key for a service account?
  - id: updateApiKey
    intent: Update an API key
    question: How do I rename or re-describe an existing API key?
  - id: deleteApiKey
    intent: Delete an API key
    question: How do I delete an API key that should no longer be used?
  - id: getAggregatedApiKey
    intent: Get an API key's aggregated details
    question: How many tokens does a particular API key have?
  - id: listApiKeys
    intent: List API keys with aggregated token details
    question: Can I page through API keys with their token counts?
  phrasing_ops: 6
  slug: harness-api-key-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: IDP App Configurations
  name: Harness App Config API
  phrasing_intents:
  - id: toggle-plugin-for-account
    intent: Enable or disable a Backstage plugin
    question: How do I turn on a Backstage plugin in my Harness developer portal?
  - id: save-or-update-plugin-app-config
    intent: Save a Backstage plugin's app config
    question: Where do I put the app-config YAML a Backstage plugin needs?
  phrasing_ops: 2
  slug: harness-app-config-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The Compliance Standards API from Harness — 3 operation(s) for compliance standards.
  name: Harness Compliance Standards API
  phrasing_intents:
  - id: createComplianceStandards
    intent: Create compliance standards for a project
    question: How do I set up compliance standards in a supply chain project?
  - id: getComplianceStandards
    intent: Search a project's compliance standards
    question: Which compliance checks apply to my project, and at what severity?
  - id: getCompliaceStandardById
    intent: Get one compliance standard by id
    question: What does a specific compliance rule check for?
  phrasing_ops: 3
  slug: harness-compliance-standards-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: DataSource Information
  name: Harness Data Source API
  phrasing_intents:
  - id: get-all-datasources-for-account
    intent: List the data sources in an account
    question: Which data sources are present in my Harness account?
  - id: get-data-points-for-data-source
    intent: List the data points of one data source
    question: What data points does a particular data source expose?
  - id: get-data-sources-data-points-map
    intent: Map every data source to its data points
    question: Can I get every data source and all of its data points in one response?
  phrasing_ops: 3
  slug: harness-data-source-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Create, edit and delete Governance policy sets
  name: Harness Policy Sets API
  phrasing_intents:
  - id: policysets#list
    intent: List policy sets at one scope
    question: Which policy sets are defined in this project or org?
  - id: policysets#create
    intent: Create a policy set
    question: How do I group policies into a set that runs on a pipeline event?
  - id: policysets#listall
    intent: List policy sets across all scope levels
    question: What policy sets apply to a project once account and org sets are included?
  - id: policysets#delete
    intent: Delete a policy set
    question: How do I delete a policy set I no longer enforce?
  - id: policysets#find
    intent: Get a policy set
    question: What policies are in a specific policy set?
  - id: policysets#update
    intent: Update a policy set
    question: Can I add policies or resource groups to an existing policy set?
  phrasing_ops: 6
  slug: harness-policy-sets-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: Rule sets serve as logical bindings on top of individual rules that help you organize and manage rules.
  name: Harness Rulesets API
  phrasing_intents:
  - id: updateRuleSet
    intent: Update a cloud governance rule set
    question: How do I change which rules are in a cloud cost governance rule set?
  - id: addRuleSet
    intent: Create a cloud governance rule set
    question: How do I group cloud cost governance rules into a new rule set?
  - id: deleteRuleSet
    intent: Delete a cloud governance rule set
    question: How do I delete a governance rule set?
  - id: listRuleSets
    intent: List cloud governance rule sets
    question: Which governance rule sets exist in my account?
  phrasing_ops: 4
  slug: harness-rulesets-api
- baseURL: https://app.harness.io
  baseurl_source: declared
  description: The User Groups API from Harness — 2 operation(s) for user groups.
  name: Harness User Groups API
  phrasing_intents:
  - id: listUsergroups
    intent: List user groups at account, org or project level
    question: Which user groups exist at my account, org or project level for code access?
  - id: listUsergroupsScoped
    intent: List user groups visible within a space
    question: Which user groups are in scope for a space, including ones inherited from parents?
  phrasing_ops: 2
  slug: harness-user-groups-api
artifact_total: 801
asyncapis:
- description: ''
  name: Harness Events
  slug: harness-events
collections:
- collection_type: postman
  name: Harness Platform Organizations API
  slug: postman-harness-organizations-api
- collection_type: postman
  name: Harness Platform Organizations Pipeline Execution API
  slug: postman-harness-pipeline-execution-api
- collection_type: postman
  name: Harness Platform Organizations Pipelines API
  slug: postman-harness-pipelines-api
- collection_type: postman
  name: Harness Platform Organizations Projects API
  slug: postman-harness-projects-api
- collection_type: open
  name: Harness Platform Organizations API
  slug: open-harness-organizations-api
- collection_type: open
  name: Harness Platform Organizations Pipeline Execution API
  slug: open-harness-pipeline-execution-api
- collection_type: open
  name: Harness Platform Organizations Pipelines API
  slug: open-harness-pipelines-api
- collection_type: open
  name: Harness Platform Organizations Projects API
  slug: open-harness-projects-api
common:
- group: design
  href: https://artifacts.apis.io/harness/rules/harness-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/harness-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/harness/rules/harness-rules.yml
  title: ''
  type: Spectral
  url: rules/harness-rules.yml
- group: design
  href: https://artifacts.apis.io/harness/json-ld/harness-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/harness-context.jsonld
- group: design
  href: https://artifacts.apis.io/harness/vocabulary/harness-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/harness-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/harness/errors/harness-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/harness-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/harness/llms/harness-apidocs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/harness-apidocs-llms.txt
- group: other
  href: https://artifacts.apis.io/harness/hosts/harness-hosts.yml
  title: ''
  type: Hosts
  url: hosts/harness-hosts.yml
- group: other
  href: https://artifacts.apis.io/harness/vendors/harness-vendors.yml
  title: ''
  type: Vendors
  url: vendors/harness-vendors.yml
- group: auth
  href: https://artifacts.apis.io/harness/security/harness-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/harness-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.harness.io/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/harness/overview
- group: agent
  href: https://artifacts.apis.io/harness/agentic-access/harness-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/harness-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/harness/security/harness-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/harness-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/harness/security/harness-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/harness-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/harness/authentication/harness-authentication.yml
  title: ''
  type: Authentication
  url: authentication/harness-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/harnessinc
- group: start
  title: ''
  type: Portal
  url: https://developer.harness.io/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.harness.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.harness.io/docs/platform/automation/api/api-quickstart/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.harness.io/docs/platform/automation/api/add-and-manage-api-keys/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.harness.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.harness.io/auth/
- group: company
  title: ''
  type: Blog
  url: https://www.harness.io/blog
- group: operate
  title: ''
  type: Support
  url: https://www.harness.io/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.harness.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.harness.io/release-notes/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.harness.io/legal/website-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.harness.io/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/harness
- group: learn
  title: ''
  type: Training
  url: https://developer.harness.io/university/
- group: auth
  title: ''
  type: Security
  url: https://www.harness.io/security
- group: agent
  href: https://artifacts.apis.io/harness/mcp/harness-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/harness-mcp.yml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/harness/mcp-server
- group: build
  href: https://artifacts.apis.io/harness/mcp/harness-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/harness-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/harness/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/harness/harness-skills
- group: agent
  href: https://artifacts.apis.io/harness/llms/harness-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/harness-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.harness.io/llms.txt
- group: docs
  href: https://artifacts.apis.io/harness/openapi/_original/harness-apis-openapi.yaml
  title: ''
  type: OpenAPI
  url: openapi/_original/harness-apis-openapi.yaml
- group: other
  href: https://artifacts.apis.io/harness/overlays/harness-apis-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/harness-apis-overlay.yaml
- group: build
  href: https://artifacts.apis.io/harness/packages/harness-packages.yml
  title: ''
  type: Packages
  url: packages/harness-packages.yml
- group: build
  href: https://artifacts.apis.io/harness/packages/harness-packages.yml
  title: ''
  type: SDKs
  url: packages/harness-packages.yml
- group: build
  href: https://artifacts.apis.io/harness/cli/harness-cli.yml
  title: ''
  type: CLI
  url: cli/harness-cli.yml
- group: agent
  href: https://artifacts.apis.io/harness/well-known/harness-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/harness-well-known.yml
- group: design
  href: https://artifacts.apis.io/harness/conventions/harness-conventions.yml
  title: ''
  type: Conventions
  url: conventions/harness-conventions.yml
- group: design
  href: https://artifacts.apis.io/harness/conventions/harness-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/harness-conventions.yml
- group: design
  href: https://artifacts.apis.io/harness/errors/harness-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/harness-error-codes.yml
- group: design
  href: https://artifacts.apis.io/harness/lifecycle/harness-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/harness-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/harness/lifecycle/harness-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/harness-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/harness/changelog/harness-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/harness-changelog.yml
- group: design
  href: https://artifacts.apis.io/harness/conformance/harness-conformance.yml
  title: ''
  type: Conformance
  url: conformance/harness-conformance.yml
- group: auth
  href: https://artifacts.apis.io/harness/conformance/harness-conformance.yml
  title: ''
  type: Compliance
  url: conformance/harness-conformance.yml
- group: auth
  href: https://artifacts.apis.io/harness/scopes/harness-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/harness-scopes.yml
- group: design
  href: https://artifacts.apis.io/harness/data-model/harness-data-model.yml
  title: ''
  type: DataModel
  url: data-model/harness-data-model.yml
- group: design
  href: https://artifacts.apis.io/harness/asyncapi/harness-events.yml
  title: ''
  type: Webhooks
  url: asyncapi/harness-events.yml
- group: build
  href: https://artifacts.apis.io/harness/examples/harness-examples.yml
  title: ''
  type: Examples
  url: examples/harness-examples.yml
- group: docs
  href: https://artifacts.apis.io/harness/json-schema/harness-json-schema-index.yml
  title: ''
  type: JSONSchema
  url: json-schema/harness-json-schema-index.yml
- group: commercial
  href: https://artifacts.apis.io/harness/plans/harness-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/harness-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/harness/rate-limits/harness-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/harness-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/harness/finops/harness-finops.yml
  title: ''
  type: FinOps
  url: finops/harness-finops.yml
- group: design
  href: https://artifacts.apis.io/harness/rules/harness-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/harness-spectral-rules.yml
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.harness.io
- group: operate
  title: ''
  type: Roadmap
  url: https://developer.harness.io/roadmap
created: '2026-01-02'
description: Harness is an AI-powered software delivery platform that automates and accelerates the entire software development lifecycle from code to production. The platform provides intelligent automation across DevOps, testing and resilience, security and compliance, and cost optimization, helping engineering teams ship code faster, safer, and smarter as they scale.
features:
- description: Intelligent automation with Harness AI for test intelligence, deployment verification, and cost optimization.
  name: AI-Powered Automation
- description: Visual pipeline builder with conditional logic, parallel execution, and approval gates.
  name: Pipeline Orchestration
- description: Declarative GitOps deployments with Argo CD integration for Kubernetes workloads.
  name: GitOps Deployments
- description: Progressive feature rollouts with targeting, experimentation, and A/B testing capabilities.
  name: Feature Flag Management
- description: FinOps capabilities including AutoStopping, commitment orchestration, and cost anomaly detection.
  name: Cloud Cost Optimization
- description: Resilience testing with chaos experiments, load testing, and disaster recovery validation.
  name: Chaos Engineering
- description: Automated security scanning with 40+ scanner integrations and policy enforcement.
  name: Security Testing Orchestration
- description: Backstage-powered developer portal for software catalog, self-service workflows, and scorecards.
  name: Internal Developer Portal
finops:
- has_sources: true
  method: derived
  name: Harness Finops
  primary_unit: ''
  service_category: ''
  slug: harness-finops
  template: true
image: /assets/icons/harness.png
integrations:
- description: Source code management, GitHub Actions, and GitHub App integration for CI/CD workflows.
  name: GitHub
- description: Native Kubernetes deployment support with Helm, Kustomize, and GitOps.
  name: Kubernetes
- description: Multi-service AWS integration including ECS, EKS, Lambda, S3, and CloudFormation.
  name: AWS
- description: Azure DevOps, AKS, Azure Functions, and Azure Resource Manager integration.
  name: Azure
- description: Google Cloud integration with GKE, Cloud Run, Cloud Functions, and Cloud Build.
  name: GCP
- description: Infrastructure as Code management with Terraform plan, apply, and state management.
  name: Terraform
- description: Issue tracking integration for deployment approvals, change management, and traceability.
  name: Jira
- description: Notifications and approval workflows within Slack channels.
  name: Slack
json_schemas:
- name: AcceptRequestBody
  property_count: 2
  slug: harness-accept-request-body
- name: AccessCheckRequest
  property_count: 2
  slug: harness-access-check-request
- name: AccessPointActivityResponse
  property_count: 1
  slug: harness-access-point-activity-response
- name: AccessPoint
  property_count: 15
  slug: harness-access-point
- name: Account
  property_count: 27
  slug: harness-account
- name: actions.ActionResponse
  property_count: 27
  slug: harness-actions-action-response
- name: actions.ImportActionTemplateRequest
  property_count: 9
  slug: harness-actions-import-action-template-request
- name: actions.ListActionTemplateResponse
  property_count: 2
  slug: harness-actions-list-action-template-response
- name: ActivityResourceCollection
  property_count: 0
  slug: harness-activity-resource-collection
- name: AgentMtlsEndpointDetails
  property_count: 5
  slug: harness-agent-mtls-endpoint-details
- name: AgentMtlsEndpointRequest
  property_count: 3
  slug: harness-agent-mtls-endpoint-request
- name: AggregationRuleDetailsRequest
  property_count: 1
  slug: harness-aggregation-rule-details-request
- name: AggregationSelectionReviewRequest
  property_count: 2
  slug: harness-aggregation-selection-review-request
- name: AlertCreateResponse
  property_count: 1
  slug: harness-alert-create-response
- name: AlertListResponse
  property_count: 1
  slug: harness-alert-list-response
- name: AlertMessageResponse
  property_count: 1
  slug: harness-alert-message-response
- name: AlertRequest
  property_count: 7
  slug: harness-alert-request
- name: AlertSearchRequest
  property_count: 9
  slug: harness-alert-search-request
- name: AlertThreshold
  property_count: 7
  slug: harness-alert-threshold
- name: AlertUpdateRequest
  property_count: 7
  slug: harness-alert-update-request
- name: AllowListRequest
  property_count: 1
  slug: harness-allow-list-request
- name: AnalyzeRequestBody
  property_count: 2
  slug: harness-analyze-request-body
- name: AnalyzeResponse
  property_count: 2
  slug: harness-analyze-response
- name: AnomaliesWhitelistRule
  property_count: 11
  slug: harness-anomalies-whitelist-rule
- name: AnomalyComment
  property_count: 6
  slug: harness-anomaly-comment
- name: AnomalyFeedback
  property_count: 1
  slug: harness-anomaly-feedback
- name: AnomalyFilterProperties
  property_count: 37
  slug: harness-anomaly-filter-properties
- name: AnomalyRequestDTO
  property_count: 3
  slug: harness-anomaly-request-dto
- name: AnsibleActivityResourceCollection
  property_count: 0
  slug: harness-ansible-activity-resource-collection
- name: ApplicationSetGenerateRequest  is a query for applicationset generate resources
  property_count: 2
  slug: harness-applications-application-set-generate-request
- name: ApplicationSetGenerateResponse is a response for applicationset generate request
  property_count: 1
  slug: harness-applications-application-set-generate-response
- name: 'ApplicationSetTree holds nodes which belongs to the application

    Used to build a tree of an ApplicationSet and its children'
  property_count: 1
  slug: harness-applications-application-set-tree
- name: applicationsApplicationSpec
  property_count: 9
  slug: harness-applications-application-spec
- name: ApplicationSyncRequest is a request to apply the config state to live state
  property_count: 14
  slug: harness-applications-application-sync-request
- name: ApplicationTree represents the hierarchical structure of resources associated with an Argo CD application
  property_count: 4
  slug: harness-applications-application-tree
- name: applicationsEventList
  property_count: 2
  slug: harness-applications-event-list
- name: 'AppProjectList is list of AppProject resources

    +k8s:deepcopy-gen:interfaces=k8s.io/apimachinery/pkg/runtime.Object'
  property_count: 2
  slug: harness-appprojects-app-project-list
- name: 'AppProject provides a logical grouping of applications, providing controls for:

    * where the apps may deploy to (cluster whitelist)

    * what may be deployed (repository whitelist, resource whitelist/blacklist)

    * who can access these applications (roles, OIDC group claims bindings)

    * and what they can do (RBAC policies)

    * automation access to these roles (JWT tokens)

    +genclient

    +genclient:noStatus

    +k8s:deepcopy-gen:interfaces=k8s.io/apimachinery/pkg/runtime.Object

    +kubebuilder:resource:path=appprojects,shortName=appproj;appprojs'
  property_count: 3
  slug: harness-appprojects-app-project
- name: ApprovalEventsSuccessResponse
  property_count: 4
  slug: harness-approval-events-success-response
- name: ApprovalOverviewSuccessResponse
  property_count: 4
  slug: harness-approval-overview-success-response
- name: ApprovalResourceCollection
  property_count: 0
  slug: harness-approval-resource-collection
- name: ApprovalsCreateApprovalResponseBodyCreation
  property_count: 1
  slug: harness-approvals-create-approval-response-body-creation
- name: ApprovalsListRequestV2
  property_count: 6
  slug: harness-approvals-list-request-v2
- name: ApprovalsListResponseV2
  property_count: 4
  slug: harness-approvals-list-response-v2
- name: ApprovalsOverviewRequestFilters
  property_count: 3
  slug: harness-approvals-overview-request-filters
- name: ApprovalsShowApprovalResponseBodyStatusInfo
  property_count: 5
  slug: harness-approvals-show-approval-response-body-status-info
- name: ArtifactChainOfCustody
  property_count: 10
  slug: harness-artifact-chain-of-custody
- name: ArtifactChainOfCustodyV2
  property_count: 4
  slug: harness-artifact-chain-of-custody-v2
- name: ArtifactComponentViewRequestBody
  property_count: 5
  slug: harness-artifact-component-view-request-body
- name: ArtifactDeploymentViewRequestBody
  property_count: 3
  slug: harness-artifact-deployment-view-request-body
- name: ArtifactModelPipeline
  property_count: 9
  slug: harness-artifact-model-pipeline
- name: ArtifactV2Overview
  property_count: 16
  slug: harness-artifact-v2-overview
- name: AuditFilterProperties
  property_count: 12
  slug: harness-audit-filter-properties
- name: AuditFilterPropertiesV1DTO
  property_count: 11
  slug: harness-audit-filter-properties-v1-dto
- name: AutoCUDConfig
  property_count: 6
  slug: harness-auto-cudconfig
- name: BackstageEnvVariableBatchRequest
  property_count: 1
  slug: harness-backstage-env-variable-batch-request
- name: BudgetFilterPropertiesDTO
  property_count: 16
  slug: harness-budget-filter-properties-dto
- name: BudgetGroup
  property_count: 21
  slug: harness-budget-group
- name: Budget
  property_count: 29
  slug: harness-budget
- name: BusinessMapping
  property_count: 12
  slug: harness-business-mapping
- name: CategoryResponse
  property_count: 5
  slug: harness-category-response
- name: CCMBudgetFilterProperties
  property_count: 18
  slug: harness-ccmbudget-filter-properties
- name: Harness Cdevents Build_Started
  property_count: 0
  slug: harness-cdevents-build_started
- name: Harness Cdevents Pipelinerun_Finished_Failure
  property_count: 0
  slug: harness-cdevents-pipelinerun_finished_failure
- name: Harness Cdevents Pipelinerun_Finished_Success
  property_count: 0
  slug: harness-cdevents-pipelinerun_finished_success
- name: Harness Cdevents Pipelinerun_Started
  property_count: 0
  slug: harness-cdevents-pipelinerun_started
- name: chaoscomponents.GetChaosComponentVariableResponse
  property_count: 1
  slug: harness-chaoscomponents-get-chaos-component-variable-response
- name: chaoscomponents.RunChaosComponentRequest
  property_count: 6
  slug: harness-chaoscomponents-run-chaos-component-request
- name: chaoscomponents.RunChaosComponentResponse
  property_count: 2
  slug: harness-chaoscomponents-run-chaos-component-response
- name: chaosfaulttemplate.ActionTemplate
  property_count: 13
  slug: harness-chaosfaulttemplate-action-template
- name: chaosfaulttemplate.ActionTemplateVariables
  property_count: 4
  slug: harness-chaosfaulttemplate-action-template-variables
- name: chaosfaulttemplate.GetActionTemplateResponse
  property_count: 2
  slug: harness-chaosfaulttemplate-get-action-template-response
- name: chaosfaulttemplate.ListActionTemplateResponse
  property_count: 4
  slug: harness-chaosfaulttemplate-list-action-template-response
- name: chaosguardconditions.CreateConditionRequest
  property_count: 8
  slug: harness-chaosguardconditions-create-condition-request
- name: chaosguardconditions.CreateConditionResponse
  property_count: 9
  slug: harness-chaosguardconditions-create-condition-response
- name: chaosguardconditions.GetConditionResponse
  property_count: 14
  slug: harness-chaosguardconditions-get-condition-response
- name: chaosguardconditions.ListConditionResponse
  property_count: 3
  slug: harness-chaosguardconditions-list-condition-response
- name: chaosguardconditions.UpdateConditionResponse
  property_count: 9
  slug: harness-chaosguardconditions-update-condition-response
- name: chaosguardrules.CreateRuleRequest
  property_count: 8
  slug: harness-chaosguardrules-create-rule-request
- name: chaosguardrules.CreateRuleResponse
  property_count: 9
  slug: harness-chaosguardrules-create-rule-response
- name: chaosguardrules.GetRuleResponse
  property_count: 14
  slug: harness-chaosguardrules-get-rule-response
- name: chaosguardrules.ListRuleResponse
  property_count: 3
  slug: harness-chaosguardrules-list-rule-response
- name: chaosguardrules.UpdateRuleResponse
  property_count: 9
  slug: harness-chaosguardrules-update-rule-response
- name: chaoshubv2.CreateHubRequest
  property_count: 7
  slug: harness-chaoshubv2-create-hub-request
- name: chaoshubv2.GetHubResponse
  property_count: 25
  slug: harness-chaoshubv2-get-hub-response
- name: chaoshubv2.ListHubResponse
  property_count: 2
  slug: harness-chaoshubv2-list-hub-response
- name: chaoshubv2.UpdateHubRequest
  property_count: 3
  slug: harness-chaoshubv2-update-hub-request
- name: CheckDetailsRequest
  property_count: 1
  slug: harness-check-details-request
- name: CICDWorkflowListingRequest
  property_count: 2
  slug: harness-cicdworkflow-listing-request
- name: CICDWorkflowListingResponse
  property_count: 5
  slug: harness-cicdworkflow-listing-response
- name: CICDWorkflowSummary
  property_count: 2
  slug: harness-cicdworkflow-summary
- name: CloneBudgetRequest
  property_count: 5
  slug: harness-clone-budget-request
- name: ClusterCostDetailsQueryParams
  property_count: 9
  slug: harness-cluster-cost-details-query-params
- name: ClusterLinkRequest
  property_count: 7
  slug: harness-cluster-link-request
- name: ClusterRequest
  property_count: 6
  slug: harness-cluster-request
- name: ClusterUnlinkRequest
  property_count: 5
  slug: harness-cluster-unlink-request
- name: clustersClusterUpdateRequest
  property_count: 6
  slug: harness-clusters-cluster-update-request
- name: CodeRepoRulesEvaluation
  property_count: 3
  slug: harness-code-repo-rules-evaluation
- name: CommitmentUtilizationDetailResponse
  property_count: 4
  slug: harness-commitment-utilization-detail-response
- name: ComplianceStandardsFilterEntity
  property_count: 2
  slug: harness-compliance-standards-filter-entity
- name: ComputeCoverageResponse
  property_count: 4
  slug: harness-compute-coverage-response
- name: ComputeCoveragesDetailResponse
  property_count: 4
  slug: harness-compute-coverages-detail-response
- name: ConnectedKubernetesClustersGetResponse
  property_count: 4
  slug: harness-connected-kubernetes-clusters-get-response
- name: ConnectedKubernetesClustersListResponse
  property_count: 4
  slug: harness-connected-kubernetes-clusters-list-response
- name: ConnectorFilterProperties
  property_count: 10
  slug: harness-connector-filter-properties
- name: Connector2
  property_count: 1
  slug: harness-connector2
- name: CoolDownMetaSuccessResponse
  property_count: 3
  slug: harness-cool-down-meta-success-response
- name: CoolDownOption
  property_count: 2
  slug: harness-cool-down-option
- name: CopmputeCoverageFilter
  property_count: 6
  slug: harness-copmpute-coverage-filter
- name: CostCategoryJiraMapping
  property_count: 9
  slug: harness-cost-category-jira-mapping
- name: CostDetailsQueryParams
  property_count: 8
  slug: harness-cost-details-query-params
- name: CostResourceCollection
  property_count: 0
  slug: harness-cost-resource-collection
- name: CostSettings
  property_count: 12
  slug: harness-cost-settings
- name: CreateAccessPointResponse
  property_count: 3
  slug: harness-create-access-point-response
- name: CreateApprovalRequest
  property_count: 4
  slug: harness-create-approval-request
- name: CreateComplianceResultV2
  property_count: 14
  slug: harness-create-compliance-result-v2
- name: CreateCostBucketBudgetsRequest
  property_count: 12
  slug: harness-create-cost-bucket-budgets-request
- name: CreateInventoryResponse
  property_count: 11
  slug: harness-create-inventory-response
- name: CreatePlaybookResponse
  property_count: 19
  slug: harness-create-playbook-response
- name: CreditOverUsage
  property_count: 2
  slug: harness-credit-over-usage
- name: CustomDeploymentYamlDTO
  property_count: 1
  slug: harness-custom-deployment-yaml-dto
- name: CustomDeploymentYamlRequestDTO
  property_count: 1
  slug: harness-custom-deployment-yaml-request-dto
- name: CustomPropertyByEntityDeleteRequest
  property_count: 3
  slug: harness-custom-property-by-entity-delete-request
- name: CustomPropertyByEntityRequest
  property_count: 5
  slug: harness-custom-property-by-entity-request
- name: CustomPropertyByFieldDeleteRequest
  property_count: 3
  slug: harness-custom-property-by-field-delete-request
- name: CustomPropertyByFieldRequest
  property_count: 5
  slug: harness-custom-property-by-field-request
- name: CustomPropertyFilterDeleteRequest
  property_count: 3
  slug: harness-custom-property-filter-delete-request
- name: CustomPropertyFilterRequest
  property_count: 5
  slug: harness-custom-property-filter-request
- name: DailyModuleAccountAccessDTO
  property_count: 5
  slug: harness-daily-module-account-access-dto
- name: DashboardMetrics
  property_count: 2
  slug: harness-dashboard-metrics
- name: DeleteAccessPointPayload
  property_count: 2
  slug: harness-delete-access-point-payload
- name: DownloadSignatureResponseBody
  property_count: 3
  slug: harness-download-signature-response-body
- name: EventLogsRequest
  property_count: 3
  slug: harness-event-logs-request
- name: EventLogsSuccessResponse
  property_count: 4
  slug: harness-event-logs-success-response
- name: EventsChartsSuccessResponse
  property_count: 4
  slug: harness-events-charts-success-response
- name: EventsFilter
  property_count: 3
  slug: harness-events-filter
- name: ExecutionDetail
  property_count: 3
  slug: harness-execution-detail
- name: Filter
  property_count: 6
  slug: harness-filter
- name: FixedSchedule
  property_count: 6
  slug: harness-fixed-schedule
- name: FixedSchedulesListResponse
  property_count: 1
  slug: harness-fixed-schedules-list-response
- name: FormDataContentDisposition
  property_count: 8
  slug: harness-form-data-content-disposition
- name: GenerateRequestBody
  property_count: 2
  slug: harness-generate-request-body
- name: GenericSuccessResponse
  property_count: 3
  slug: harness-generic-success-response
- name: github_com_harness_hce-saas_graphql_server_graph_model.RegisterInfraRequest
  property_count: 20
  slug: harness-github-com-harness-hce-saas-graphql-server-graph-model-register-infra-request
- name: github_com_harness_hce-saas_graphql_server_pkg_actions.Action
  property_count: 12
  slug: harness-github-com-harness-hce-saas-graphql-server-pkg-actions-action
- name: github_com_harness_hce-saas_graphql_server_pkg_database_mongodb_actions.Action
  property_count: 21
  slug: harness-github-com-harness-hce-saas-graphql-server-pkg-database-mongodb-actions-action
- name: github_com_harness_hce-saas_graphql_server_pkg_database_mongodb_recommendation.Recommendation
  property_count: 21
  slug: harness-github-com-harness-hce-saas-graphql-server-pkg-database-mongodb-recommendation-recommendation
- name: github_com_harness_hce-saas_graphql_server_pkg_database_mongodb_security_governance.Rule
  property_count: 8
  slug: harness-github-com-harness-hce-saas-graphql-server-pkg-database-mongodb-security-governance-rule
- name: github_com_harness_hce-saas_hce-sdk_types_api_machine_infra.Infra
  property_count: 21
  slug: harness-github-com-harness-hce-saas-hce-sdk-types-api-machine-infra-infra
- name: gitopsservicev1NamespaceList
  property_count: 7
  slug: harness-gitopsservicev1-namespace-list
- name: GovernanceCostSettings
  property_count: 7
  slug: harness-governance-cost-settings
- name: HarnessApprovalActivityRequest
  property_count: 4
  slug: harness-harness-approval-activity-request
- name: HostActivityResourceCollection
  property_count: 0
  slug: harness-host-activity-resource-collection
- name: IacmResourceCostRequest
  property_count: 1
  slug: harness-iacm-resource-cost-request
- name: infra_v2.KubernetesInfrastructureV2Details
  property_count: 46
  slug: harness-infra-v2-kubernetes-infrastructure-v2-details
- name: infra_v2.RegisterInfrastructureV2Request
  property_count: 30
  slug: harness-infra-v2-register-infrastructure-v2-request
- name: infra_v2.UpdateKubernetesInfrastructureV2Request
  property_count: 24
  slug: harness-infra-v2-update-kubernetes-infrastructure-v2-request
- name: InstanceTypesPayload
  property_count: 4
  slug: harness-instance-types-payload
- name: LandingPageResponse
  property_count: 4
  slug: harness-landing-page-response
- name: LDAPSettings
  property_count: 9
  slug: harness-ldapsettings
- name: LicenseTypeResponse
  property_count: 1
  slug: harness-license-type-response
- name: LicensedModules
  property_count: 1
  slug: harness-licensed-modules
- name: ListAccessPointResponse
  property_count: 1
  slug: harness-list-access-point-response
- name: ListActivityResourceChangesResponse
  property_count: 11
  slug: harness-list-activity-resource-changes-response
- name: ListChildAccountsSuccessResponse
  property_count: 4
  slug: harness-list-child-accounts-success-response
- name: ListCostsResponse
  property_count: 4
  slug: harness-list-costs-response
- name: ListMasterSuccessResponse
  property_count: 4
  slug: harness-list-master-success-response
- name: ManageBudgetAlertsRequest
  property_count: 5
  slug: harness-manage-budget-alerts-request
- name: model.KubernetesInfra
  property_count: 34
  slug: harness-model-kubernetes-infra
- name: OAuthSettings
  property_count: 3
  slug: harness-oauth-settings
- name: OnboardToClusterOrchestratorRequest
  property_count: 3
  slug: harness-onboard-to-cluster-orchestrator-request
- name: OrganizationList
  property_count: 2
  slug: harness-organization-list
- name: PerspectiveQueryDTO
  property_count: 2
  slug: harness-perspective-query-dto
- name: PipelineExecutionRequest
  property_count: 1
  slug: harness-pipeline-execution-request
- name: PipelineExecution
  property_count: 2
  slug: harness-pipeline-execution
- name: PipelineList
  property_count: 2
  slug: harness-pipeline-list
- name: PluginResponseBody
  property_count: 3
  slug: harness-plugin-response-body
- name: PolicySample
  property_count: 2
  slug: harness-policy-sample
- name: ProjectList
  property_count: 2
  slug: harness-project-list
- name: projectsEmptyResponse
  property_count: 0
  slug: harness-projects-empty-response
- name: recommendations.CreateActionResponse
  property_count: 2
  slug: harness-recommendations-create-action-response
- name: recommendations.ListRecommendationsRequest
  property_count: 1
  slug: harness-recommendations-list-recommendations-request
- name: recommendations.ListRecommendationsResponse
  property_count: 2
  slug: harness-recommendations-list-recommendations-response
- name: recommendations.PipelineAddExperimentResponse
  property_count: 3
  slug: harness-recommendations-pipeline-add-experiment-response
- name: recommendations.RunActionResponse
  property_count: 2
  slug: harness-recommendations-run-action-response
- name: ReleaseType
  property_count: 0
  slug: harness-release-type
- name: RenewalEventsRequest
  property_count: 5
  slug: harness-renewal-events-request
- name: RenewalEventsSuccessResponse
  property_count: 4
  slug: harness-renewal-events-success-response
- name: repositoriesRevisionMetadata
  property_count: 6
  slug: harness-repositories-revision-metadata
- name: RepositoriesSummary
  property_count: 3
  slug: harness-repositories-summary
- name: RICoverageDetailsResponse
  property_count: 4
  slug: harness-ricoverage-details-response
- name: RIRecommendationScheduleSuccessResponse
  property_count: 4
  slug: harness-rirecommendation-schedule-success-response
- name: RuleExecutionFilter
  property_count: 22
  slug: harness-rule-execution-filter
- name: SaveIntegrityVerificationRequestBody
  property_count: 5
  slug: harness-save-integrity-verification-request-body
- name: SaveServiceRequestV2
  property_count: 3
  slug: harness-save-service-request-v2
- name: SaveServiceRequestV2WithoutDisabled
  property_count: 3
  slug: harness-save-service-request-v2-without-disabled
- name: SaveServiceRequestWithoutDisabled
  property_count: 3
  slug: harness-save-service-request-without-disabled
- name: SaveSignatureRequestBody
  property_count: 3
  slug: harness-save-signature-request-body
- name: SaveStaticSchedulesRequest
  property_count: 2
  slug: harness-save-static-schedules-request
- name: ScheduleReportRequestBody
  property_count: 6
  slug: harness-schedule-report-request-body
- name: security_governance.Condition
  property_count: 8
  slug: harness-security-governance-condition
- name: ServiceHealthResponse
  property_count: 1
  slug: harness-service-health-response
- name: ServicesResponse
  property_count: 1
  slug: harness-services-response
- name: servicev1Application
  property_count: 15
  slug: harness-servicev1-application
- name: servicev1ApplicationSetList
  property_count: 7
  slug: harness-servicev1-application-set-list
- name: servicev1ApplicationSet
  property_count: 9
  slug: harness-servicev1-application-set
- name: servicev1Applicationlist
  property_count: 7
  slug: harness-servicev1-applicationlist
- name: servicev1ClusterQuery
  property_count: 12
  slug: harness-servicev1-cluster-query
- name: servicev1Cluster
  property_count: 11
  slug: harness-servicev1-cluster
- name: SessionTimeoutSettings
  property_count: 2
  slug: harness-session-timeout-settings
- name: SetupInstanceTypesSuccessResponse
  property_count: 4
  slug: harness-setup-instance-types-success-response
- name: SetupValidateSuccessResponse
  property_count: 4
  slug: harness-setup-validate-success-response
- name: shared.ListMetadataResponse
  property_count: 3
  slug: harness-shared-list-metadata-response
- name: ShowCcmCostsResponse
  property_count: 6
  slug: harness-show-ccm-costs-response
- name: SPCoverageDetailsResponse
  property_count: 4
  slug: harness-spcoverage-details-response
- name: StoStatus
  property_count: 1
  slug: harness-sto-status
- name: TwoFactorAdminOverrideSettings
  property_count: 1
  slug: harness-two-factor-admin-override-settings
- name: types.ListMetadataRequest
  property_count: 1
  slug: harness-types-list-metadata-request
- name: UpdateApprovalRequest
  property_count: 3
  slug: harness-update-approval-request
- name: UpdateDashboardFilterRequest
  property_count: 5
  slug: harness-update-dashboard-filter-request
- name: UpdateInventoryResponse
  property_count: 1
  slug: harness-update-inventory-response
- name: UpdatePlaybookResponse
  property_count: 1
  slug: harness-update-playbook-response
- name: UsageResponse1
  property_count: 3
  slug: harness-usage-response1
- name: trigger
  property_count: 1
  slug: harness-v0-trigger
- name: v1AgentQuery
  property_count: 22
  slug: harness-v1-agent-query
- name: A gitops-agent
  property_count: 21
  slug: harness-v1-agent
- name: v1AgentSetPrimaryNodeRequest
  property_count: 6
  slug: harness-v1-agent-set-primary-node-request
- name: v1AgentSyncAllowedUpdateRequest
  property_count: 6
  slug: harness-v1-agent-sync-allowed-update-request
- name: v1ApplicationSetQuery
  property_count: 12
  slug: harness-v1-application-set-query
- name: v1ArgoProjectList
  property_count: 7
  slug: harness-v1-argo-project-list
- name: v1ArgoProject
  property_count: 9
  slug: harness-v1-argo-project
- name: v1Certificatelist
  property_count: 7
  slug: harness-v1-certificatelist
- name: v1DashboardOverview
  property_count: 8
  slug: harness-v1-dashboard-overview
- name: inputSet
  property_count: 3
  slug: harness-v1-inputSet
- name: overlayInputSet
  property_count: 3
  slug: harness-v1-overlayInputSet
- name: pipeline
  property_count: 2
  slug: harness-v1-pipeline
- name: RecentDeploymentQuery
  property_count: 11
  slug: harness-v1-recent-deployment-query
- name: v1RecentDeploymentsDetailsList
  property_count: 3
  slug: harness-v1-recent-deployments-details-list
- name: v1RecentlyCreatedOverview
  property_count: 4
  slug: harness-v1-recently-created-overview
- name: template
  property_count: 2
  slug: harness-v1-template
- name: v1TopApplicationPhaseStatsList
  property_count: 2
  slug: harness-v1-top-application-phase-stats-list
- name: v1VersionUpgradeResponse
  property_count: 7
  slug: harness-v1-version-upgrade-response
- name: WarmUpOption
  property_count: 3
  slug: harness-warm-up-option
- name: WarmUpResponse
  property_count: 4
  slug: harness-warm-up-response
- name: YamlDiffRequest
  property_count: 1
  slug: harness-yaml-diff-request
jsonld:
- class_count: 4
  name: Harness Context
  property_count: 7
  slug: harness-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.harness.io requiring OAuth; 11 tools listed.
  name: Harness MCP Server 2.0
  slug: harness-mcp-v2
modified: '2026-09-12'
name: Harness
nav: Providers
network: true
overview: 'Harness publishes 488 API contracts indexed on the [APIs.io](https://apis.io/) network, including Organizations API, Pipeline Execution API, Pipelines API, and 485 more. Tagged areas include DevOps, GitOps, Internal Developer Portal, Lifecycle, and Software Delivery.


  The Harness catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Harness'' developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, signup flow, engineering blog, and 56 more developer resources.'
plans:
- name: Harness Plans Pricing
  plan_count: 3
  slug: harness-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 7
  name: Harness Rate Limits
  slug: harness-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Harness API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 1
  slug: harness-rules
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Harness API Rules
  rule_count: 16
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 10
  slug: harness-spectral-rules
scopes:
- name: Harness Scopes
  scope_count: 0
  slug: harness-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 89.2
  coverage:
    artifact_dirs: 37
    catalog_earned: 80.8
    catalog_earned_first_party: 24.0
    catalog_gap: 34.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 35.6
    contract_quality: 70.6
    developer_ergonomics: 74.4
    discoverability: 75.0
    operational_transparency: 97.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 89.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 0.4
      total: 477
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 100.0
screenshot: https://apis.io/screenshots/harness/harness-2026-06-20T182519.png
security:
- kind: authentication
  name: Harness Authentication
  slug: harness-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Harness Domain Security
  slug: harness-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Harness Vulnerability Disclosure
  slug: harness-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Harness Trust Center
  slug: harness-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, GDPR, CSA STAR
skill_count: 88
skills:
- name: ai-operations
  slug: ai-operations-2
- name: ai-operations
  slug: ai-operations
- name: analyze-costs
  slug: analyze-costs-2
- name: analyze-costs
  slug: analyze-costs
- name: audit-report
  slug: audit-report-2
- name: audit-report
  slug: audit-report
- name: chaos-experiment
  slug: chaos-experiment-2
- name: chaos-experiment
  slug: chaos-experiment
- name: configure-container-scan
  slug: configure-container-scan-2
- name: configure-container-scan
  slug: configure-container-scan
- name: configure-repo-scan
  slug: configure-repo-scan-2
- name: configure-repo-scan
  slug: configure-repo-scan
- name: configure-secret-scan
  slug: configure-secret-scan-2
- name: configure-secret-scan
  slug: configure-secret-scan
- name: create-agent
  slug: create-agent-2
- name: create-agent-template
  slug: create-agent-template-2
- name: create-agent-template
  slug: create-agent-template
- name: create-agent
  slug: create-agent
- name: create-connector
  slug: create-connector-2
- name: create-connector
  slug: create-connector
- name: create-environment
  slug: create-environment-2
- name: create-environment
  slug: create-environment
- name: create-infrastructure
  slug: create-infrastructure-2
- name: create-infrastructure
  slug: create-infrastructure
slug: harness
tags:
- DevOps
- GitOps
- Internal Developer Portal
- Lifecycle
- Software Delivery
- CI/CD
- Continuous Delivery
- Continuous Integration
use_cases:
- description: Automate build, test, and deploy workflows across multi-cloud and hybrid environments.
  name: CI/CD Pipeline Automation
- description: Roll out features progressively with feature flags, canary deployments, and blue-green strategies.
  name: Progressive Feature Delivery
- description: Optimize cloud spend with automated cost recommendations, idle resource detection, and budget alerts.
  name: Cloud Cost Management
- description: Enforce security policies with automated scanning, SBOM generation, and supply chain verification.
  name: Security Compliance
- description: Build internal developer platforms with self-service workflows, templates, and software catalogs.
  name: Platform Engineering
- description: Manage SLOs, monitor service health, and validate resilience with chaos engineering.
  name: SRE and Reliability
website: https://www.harness.io/
---
