---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Cloudbees Agentic Access
  operation_count: 79
  slug: cloudbees-agentic-access
  summary_line: 79 operations · 32 acting
api_count: 2
apis:
- description: CloudBees CI is a hardened, enterprise distribution of Jenkins. The REST API is the Jenkins remote access API exposed at /api on every controller and on individual jobs, runs, queues and nodes. Caller
  name: CloudBees CI REST API
  slug: ci
- description: 'The CloudBees CD/RO (Continuous Delivery / Release Orchestration) REST API exposes resources for pipelines, releases, environments, applications, deployments, projects and resources. Operations cover '
  name: CloudBees CD/RO REST API
  slug: cd-ro
- description: The CloudBees Feature Management REST API (formerly Rollout) provides programmatic access to applications, environments, feature flags, experiments, target groups, audit logs, and users. Authenticatio
  name: CloudBees Feature Management REST API
  slug: feature-management
- description: The CloudBees CD plugin for Jenkins exposes Jenkins pipeline steps that call CloudBees CD/RO REST endpoints — triggering pipelines, running releases, deploying applications, and pulling artifacts from
  name: CloudBees CD/RO Jenkins Plugin Steps
  slug: jenkins-plugin
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: The Computer API from CloudBees — 1 operation(s) for computer.
  name: CloudBees Computer API
  phrasing_intents:
  - id: getComputerApiJson
    intent: List the build nodes and agents on a controller
    question: Which build agents are connected to my CloudBees CI controller?
  phrasing_ops: 1
  slug: cloudbees-computer-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: The CreateItem API from CloudBees — 1 operation(s) for createitem.
  name: CloudBees CreateItem API
  phrasing_intents:
  - id: postCreateItem
    intent: Create a new job on the controller
    question: How do I create a new Jenkins job through the CloudBees CI API?
  phrasing_ops: 1
  slug: cloudbees-createitem-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: The Job API from CloudBees — 7 operation(s) for job.
  name: CloudBees Job API
  phrasing_intents:
  - id: getJobByNameApiJson
    intent: Get a job's metadata and build history
    question: How do I see a job's status and recent builds in CloudBees CI?
  - id: postJobByNameBuild
    intent: Start a build of a job with no parameters
    question: How do I kick off a job that takes no build parameters?
  - id: postJobByNameBuildWithParameters
    intent: Start a parameterized build of a job
    question: How do I run a job and pass it build parameters?
  - id: getJobByNameByNumberApiJson
    intent: Get a specific build of a job by number
    question: What was the result of a particular numbered build of my job?
  - id: getJobByNameLastSuccessfulBuildApiJson
    intent: Get the last successful build of a job
    question: When did my job last pass, and which build was it?
  - id: getJobByNameConfigXml
    intent: Download a job's configuration XML
    question: How do I export a job's config.xml so I can back it up?
  - id: postJobByNameConfigXml
    intent: Replace a job's configuration XML
    question: How do I change an existing job's settings by uploading new config XML?
  - id: postJobByNameDoDelete
    intent: Delete a job
    question: How do I permanently remove a job from the controller?
  phrasing_ops: 8
  slug: cloudbees-job-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: The Json API from CloudBees — 1 operation(s) for json.
  name: CloudBees Json API
  phrasing_intents:
  - id: getApiJson
    intent: Get top-level controller metadata as JSON
    question: How do I get an overview of my CloudBees CI controller and its jobs as JSON?
  phrasing_ops: 1
  slug: cloudbees-json-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: The Python API from CloudBees — 1 operation(s) for python.
  name: CloudBees Python API
  phrasing_intents:
  - id: getApiPython
    intent: Get controller metadata as a Python literal
    question: Can I get my controller's metadata in a form Python can eval directly?
  phrasing_ops: 1
  slug: cloudbees-python-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: The Queue API from CloudBees — 1 operation(s) for queue.
  name: CloudBees Queue API
  phrasing_intents:
  - id: getQueueApiJson
    intent: Show the pending build queue
    question: Which builds are waiting in the queue on my CloudBees CI controller?
  phrasing_ops: 1
  slug: cloudbees-queue-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: The Xml API from CloudBees — 1 operation(s) for xml.
  name: CloudBees Xml API
  phrasing_intents:
  - id: getApiXml
    intent: Get controller metadata as XML
    question: Can I pull my CloudBees CI controller's metadata as XML instead of JSON?
  phrasing_ops: 1
  slug: cloudbees-xml-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: Create and manage the components in an organization. A component represents a source code repository that CloudBees Unify tracks. Components can be onboarded with or without an SCM integration, and an
  name: CloudBees Components API
  phrasing_intents:
  - id: ServiceEndpoint_ListServices2
    intent: List applications and components together
    question: Where can I see both the applications and the components in my organization in one list?
  phrasing_ops: 1
  slug: cloudbees-components-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: Discover and manage environments within your organization. Use environments to maintain an up-to-date inventory for feature flag targeting, deployment scripts, and monitoring workflows.
  name: CloudBees Environments API
  phrasing_intents:
  - id: ReportServiceHandler_GetEnvironmentsv2
    intent: List environments in an organization
    question: Which environments exist in my CloudBees organization?
  phrasing_ops: 1
  slug: cloudbees-environments-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: Set flag state (enabled or disabled) and targeting rules for a specific environment to determine which users or segments receive each variation.
  name: CloudBees Flag configurations API
  phrasing_intents:
  - id: FlagConfigurationApi_ListFlagConfigurations
    intent: List all flag configurations in an environment
    question: How can I see how every feature flag is configured in one environment?
  - id: FlagConfigurationApi_GetFlagConfiguration
    intent: Get one flag's configuration in an environment
    question: How do I see the targeting conditions and default value of one flag in production?
  - id: FlagConfigurationApi_UpdateFlagConfiguration
    intent: Replace a flag's full configuration in an environment
    question: How do I overwrite the entire configuration of a flag in one environment?
  - id: FlagConfigurationApi_PatchFlagConfiguration
    intent: Change selected fields of a flag's configuration
    question: Can I change just the default value of a flag in one environment without resending everything?
  - id: FlagConfigurationApi_UpdateFlagConfigurationConfigState
    intent: Turn a flag on or off in an environment
    question: How do I switch a feature flag on in production?
  - id: FlagConfigurationApi_CloneFlagConfiguration
    intent: Copy a flag's configuration to other environments
    question: Can I copy a flag's setup from staging to other environments?
  phrasing_ops: 6
  slug: cloudbees-flag-configurations-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: Create, read, update, and delete custom properties used in targeting conditions and target groups.
  name: CloudBees Flag custom properties API
  phrasing_intents:
  - id: CustomPropertyApi_ListCustomProperties
    intent: List custom properties in an application
    question: Which custom properties can I use in flag targeting for my application?
  - id: CustomPropertyApi_AddCustomProperty
    intent: Create a custom property for targeting
    question: How do I add a new custom property to target flags on, like a user's plan?
  - id: CustomPropertyApi_GetCustomPropertyByName
    intent: Look up a custom property by name
    question: Can I fetch a custom property if I only know its name?
  - id: CustomPropertyApi_GetCustomProperty
    intent: Get a custom property by ID
    question: How do I retrieve a custom property when I have its ID?
  - id: CustomPropertyApi_UpdateCustomProperty
    intent: Replace a custom property's settings
    question: How do I change the type or description of an existing custom property?
  - id: CustomPropertyApi_DeleteCustomProperty
    intent: Delete a custom property
    question: How do I permanently remove a custom property I no longer use?
  - id: CustomPropertyApi_GetCustomPropertyFlagUsagePerEnvironment
    intent: See which flags use a custom property
    question: Which feature flags reference a custom property, per environment?
  - id: CustomPropertyApi_GetCustomPropertyTargetGroupUsage
    intent: See which target groups use a custom property
    question: Which target groups rely on a particular custom property?
  phrasing_ops: 8
  slug: cloudbees-flag-custom-properties-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: Track how often each feature flag variation is served within an environment. Use impression data to monitor flag adoption, validate rollout progress, and analyze which variations are being evaluated b
  name: CloudBees Flag lifecycle API
  phrasing_intents:
  - id: FmImpressionsApi_GetFlagsStatus2
    intent: Get the status of all flags in an environment
    question: What is the current status of every feature flag in an environment?
  - id: FmImpressionsApi_GetImpressions2
    intent: Get impression counts for feature flags
    question: How many times has a feature flag been evaluated over the last day?
  phrasing_ops: 2
  slug: cloudbees-flag-lifecycle-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: Control runtime feature visibility and behavior to enable gradual rollouts, A/B testing, progressive delivery, and safe deployments without redeployment.
  name: CloudBees Flags API
  phrasing_intents:
  - id: FlagApi_ListFlags
    intent: List feature flags in an application
    question: Which feature flags exist in my application?
  - id: FlagApi_AddFlag
    intent: Create a feature flag
    question: How do I create a new feature flag in CloudBees?
  - id: FlagApi_GetFlagByName
    intent: Look up a feature flag by name
    question: Can I fetch a feature flag if I only know its name?
  - id: FlagApi_ListLabels
    intent: List labels used on feature flags
    question: What labels are used across the flags in my application?
  - id: FlagApi_GetFlag
    intent: Get a feature flag by ID
    question: How do I retrieve a feature flag when I have its ID?
  - id: FlagApi_UpdateFlag
    intent: Update a feature flag's definition
    question: How do I change a flag's description or labels?
  - id: FlagApi_DeleteFlag
    intent: Delete a feature flag
    question: How do I permanently delete a feature flag and its configurations?
  - id: FlagApi_GetFlagConfigurationState
    intent: Check where a flag is enabled
    question: In which environments is a particular flag switched on?
  phrasing_ops: 9
  slug: cloudbees-flags-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: Define the structural and governance boundaries within a CloudBees Unify tenant. Organizations model business units or departments, support parent-child hierarchies, and inherit configuration—properti
  name: CloudBees Organizations API
  phrasing_intents:
  - id: listOrganizations
    intent: List organizations I can access
    question: Which CloudBees organizations do I have access to?
  - id: getOrganizationByName
    intent: Get an organization by exact name
    question: How do I look up an organization by its exact domain name?
  phrasing_ops: 2
  slug: cloudbees-organizations-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: Create, update, and retrieve CI/CD runs for a component. Attach and list test results, artifacts, security results, evidences, and deployments.
  name: CloudBees Runs API
  phrasing_intents:
  - id: createRun
    intent: Record a CI/CD run for a component
    question: How do I report a pipeline run from an external CI tool?
  - id: updateRun
    intent: Update a run's status
    question: How do I mark a run as finished or failed after it started?
  - id: getRun
    intent: Get a run
    question: How can I look up a single run and its status?
  - id: listArtifacts
    intent: List build artifacts on a run
    question: What build artifacts were produced by a run?
  - id: createArtifacts
    intent: Attach build artifacts to a run
    question: How do I attach build artifacts, like container images, to a run?
  - id: listDeployments
    intent: List deployments recorded on a run
    question: Which deployments are associated with a run?
  - id: createDeploymentArtifacts
    intent: Record a deployment on a run
    question: How do I record that a run deployed artifacts to production?
  - id: listEvidences
    intent: List evidence attached to a run
    question: What compliance evidence has been attached to a run?
  phrasing_ops: 13
  slug: cloudbees-runs-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: Define reusable sets of targeting conditions for feature flags. Specify rules once (such as matching users by role, region, or custom property) and apply them across multiple flags. Changes to a targe
  name: CloudBees Target groups API
  phrasing_intents:
  - id: TargetGroupApi_ListTargetGroups
    intent: List target groups in an application
    question: Which target groups are defined in my application?
  - id: TargetGroupApi_AddTargetGroup
    intent: Create a target group
    question: How do I create a target group of beta users to target flags at?
  - id: TargetGroupApi_GetTargetGroupByName
    intent: Look up a target group by name
    question: Can I fetch a target group if I only know its name?
  - id: TargetGroupApi_ListTargetGroupsWithFlagsUsage
    intent: List target groups with the flags using them
    question: Which flags use each of my target groups?
  - id: TargetGroupApi_GetTargetGroup
    intent: Get a target group by ID
    question: How do I retrieve a target group when I have its ID?
  - id: TargetGroupApi_UpdateTargetGroup
    intent: Update a target group
    question: How do I change the conditions of an existing target group?
  - id: TargetGroupApi_DeleteTargetGroup
    intent: Delete a target group
    question: How do I permanently delete a target group?
  - id: TargetGroupApi_GetTargetGroupFlagUsagePerEnvironment
    intent: See which flags use a target group, by environment
    question: Which feature flags reference one target group in each environment?
  phrasing_ops: 8
  slug: cloudbees-target-groups-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: List teams, and get a specific team with optional user expansion.
  name: CloudBees Teams API
  phrasing_intents:
  - id: TeamsService_GetTeams
    intent: List teams in an organization
    question: Which teams belong to a specific organization?
  phrasing_ops: 1
  slug: cloudbees-teams-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: List users in a tenant.
  name: CloudBees Users API
  phrasing_intents:
  - id: InvitesService_CreateInviteV3
    intent: Invite users to an organization
    question: How do I invite new people to my organization by email?
  - id: MembershipsService_RemoveUsersFromTeamV3
    intent: Remove a user from an organization
    question: How do I revoke someone's access to my whole organization?
  phrasing_ops: 2
  slug: cloudbees-users-api
- baseURL: https://example.cloudbees.com
  baseurl_source: declared
  description: Edge runners execute jobs on your own infrastructure rather than CloudBees-hosted systems, running builds and other work closer to private resources such as source control, artifact stores, and intern
  name: CloudBees Edge runners API
  slug: cloudbees-edge-runners-api
artifact_total: 101
asyncapis:
- description: ''
  name: Cloudbees Webhooks
  slug: cloudbees-webhooks
collections:
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible) Computer API
  slug: open-cloudbees-computer-api
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible) Computer CreateItem API
  slug: open-cloudbees-createitem-api
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible) Computer Job API
  slug: open-cloudbees-job-api
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible) Computer Json API
  slug: open-cloudbees-json-api
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible) Computer Python API
  slug: open-cloudbees-python-api
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible) Computer Queue API
  slug: open-cloudbees-queue-api
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible) Computer Xml API
  slug: open-cloudbees-xml-api
- collection_type: open
  name: CloudBees CI REST API (Jenkins-compatible)
  slug: open-cloudbees
common:
- group: design
  href: https://artifacts.apis.io/cloudbees/vocabulary/cloudbees-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cloudbees-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/cloudbees/hosts/cloudbees-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudbees-hosts.yml
- group: other
  href: https://artifacts.apis.io/cloudbees/vendors/cloudbees-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudbees-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.cloudbees.com/media
- group: other
  href: https://artifacts.apis.io/cloudbees/overlays/cloudbees-unify-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudbees-unify-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cloudbees/overlays/cloudbees-unify-beta-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cloudbees-unify-beta-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/cloudbees/agentic-access/cloudbees-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudbees-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cloudbees/security/cloudbees-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cloudbees-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cloudbees/security/cloudbees-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudbees-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cloudbees/security/cloudbees-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudbees-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cloudbees/authentication/cloudbees-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cloudbees-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudbees
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudbees
- group: company
  title: ''
  type: Website
  url: https://www.cloudbees.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloudbees.com/
- group: operate
  title: ''
  type: Support
  url: https://support.cloudbees.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloudbees.com/legal/privacy-policy
- group: build
  title: ''
  type: Plugins
  url: https://docs.cloudbees.com/plugins/ci
- group: design
  href: https://artifacts.apis.io/cloudbees/json-ld/cloudbees-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudbees-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloudbees/rules/cloudbees-rules.yml
  title: ''
  type: Spectral
  url: rules/cloudbees-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://www.cloudbees.com/blog/rss.xml
- group: agent
  href: https://artifacts.apis.io/cloudbees/mcp/cloudbees-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cloudbees-mcp.yml
- group: build
  href: https://artifacts.apis.io/cloudbees/mcp/cloudbees-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cloudbees-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/cloudbees/llms/cloudbees-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudbees-llms.txt
- group: agent
  href: https://artifacts.apis.io/cloudbees/well-known/cloudbees-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudbees-well-known.yml
- group: auth
  href: https://artifacts.apis.io/cloudbees/well-known/cloudbees-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cloudbees-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.cloudbees.com/legal/security-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.cloudbees.com/company/trust-center
- group: design
  href: https://artifacts.apis.io/cloudbees/conformance/cloudbees-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudbees-conformance.yml
- group: design
  href: https://artifacts.apis.io/cloudbees/errors/cloudbees-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cloudbees-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cloudbees/lifecycle/cloudbees-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cloudbees-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloudbees.io/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.cloudbees.com/docs/cloudbees-common/latest/maintenance-lifecycle
- group: design
  href: https://artifacts.apis.io/cloudbees/conventions/cloudbees-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cloudbees-conventions.yml
- group: operate
  href: https://artifacts.apis.io/cloudbees/changelog/cloudbees-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cloudbees-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.cloudbees.com/docs/cloudbees-unify-changelog/latest/
- group: build
  href: https://artifacts.apis.io/cloudbees/cli/cloudbees-cli.yml
  title: ''
  type: CLI
  url: cli/cloudbees-cli.yml
- group: design
  href: https://artifacts.apis.io/cloudbees/asyncapi/cloudbees-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cloudbees-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/cloudbees/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cloudbees/data-model/cloudbees-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloudbees-data-model.yml
- group: auth
  href: https://artifacts.apis.io/cloudbees/scopes/cloudbees-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cloudbees-scopes.yml
- group: commercial
  href: https://artifacts.apis.io/cloudbees/plans/cloudbees-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cloudbees-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cloudbees/rate-limits/cloudbees-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cloudbees-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cloudbees/finops/cloudbees-finops.yml
  title: ''
  type: FinOps
  url: finops/cloudbees-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cloudbees.com/docs/cloudbees-unify/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.cloudbees.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cloudbees.com/docs/cloudbees-unify/latest/getting-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cloudbees.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloudbees.com/company/terms-of-service
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/cloudbees/cloudbees-feature-management
- group: other
  href: https://artifacts.apis.io/cloudbees/capabilities/cloudbees-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cloudbees-capability-edges.yml
- group: build
  href: https://artifacts.apis.io/cloudbees/packages/cloudbees-packages.yml
  title: ''
  type: Packages
  url: packages/cloudbees-packages.yml
- group: build
  href: https://artifacts.apis.io/cloudbees/packages/cloudbees-packages.yml
  title: ''
  type: SDKs
  url: packages/cloudbees-packages.yml
created: '2025-01-08'
description: CloudBees provides software delivery automation across continuous integration, continuous deployment, release orchestration, and feature management. Their developer surface includes the CloudBees CI REST API (an extension of the Jenkins REST API), the CloudBees CD/RO REST API for release orchestration, the CloudBees Feature Management REST API (formerly Rollout) for feature flags and environments, and the CloudBees Unify Platform API for the modern unified delivery platform. APIs are generally JSON, token-authenticated, and follow REST conventions.
finops:
- has_sources: true
  method: derived
  name: Cloudbees Finops
  primary_unit: ''
  service_category: ''
  slug: cloudbees-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudbees.png
json_schemas:
- name: api.auth.CreateInvitesRequestV3
  property_count: 6
  slug: cloudbees-api-auth-create-invites-request-v3
- name: api.auth.CreateInvitesV3Response
  property_count: 1
  slug: cloudbees-api-auth-create-invites-v3-response
- name: api.auth.GetOrganizationByNameResponse
  property_count: 1
  slug: cloudbees-api-auth-get-organization-by-name-response
- name: api.auth.GetOrganizationsResponse
  property_count: 2
  slug: cloudbees-api-auth-get-organizations-response
- name: api.auth.GetTeamsResponse
  property_count: 2
  slug: cloudbees-api-auth-get-teams-response
- name: api.CustomProperty.AddCustomPropertyResponse
  property_count: 1
  slug: cloudbees-api-custom-property-add-custom-property-response
- name: api.CustomProperty.CustomProperty
  property_count: 6
  slug: cloudbees-api-custom-property-custom-property
- name: api.CustomProperty.GetCustomPropertyFlagsUsagePerEnvironmentResponse
  property_count: 1
  slug: cloudbees-api-custom-property-get-custom-property-flags-usage-per-environment-response
- name: api.CustomProperty.GetCustomPropertyResponse
  property_count: 1
  slug: cloudbees-api-custom-property-get-custom-property-response
- name: api.CustomProperty.GetCustomPropertyTargetGroupUsageResponse
  property_count: 1
  slug: cloudbees-api-custom-property-get-custom-property-target-group-usage-response
- name: api.CustomProperty.ListCustomPropertiesResponse
  property_count: 1
  slug: cloudbees-api-custom-property-list-custom-properties-response
- name: api.flag.AddFlagResponse
  property_count: 1
  slug: cloudbees-api-flag-add-flag-response
- name: api.flag.FlagConfigState
  property_count: 1
  slug: cloudbees-api-flag-flag-config-state
- name: api.flag.FlagConfigurationOptional
  property_count: 5
  slug: cloudbees-api-flag-flag-configuration-optional
- name: api.flag.FlagConfiguration
  property_count: 10
  slug: cloudbees-api-flag-flag-configuration
- name: api.flag.Flag
  property_count: 12
  slug: cloudbees-api-flag-flag
- name: api.flag.GetFlagConfigurationResponse
  property_count: 1
  slug: cloudbees-api-flag-get-flag-configuration-response
- name: api.flag.GetFlagConfigurationStateResponse
  property_count: 1
  slug: cloudbees-api-flag-get-flag-configuration-state-response
- name: api.flag.GetFlagFlagsUsagePerEnvironmentResponse
  property_count: 1
  slug: cloudbees-api-flag-get-flag-flags-usage-per-environment-response
- name: api.flag.GetFlagResponse
  property_count: 1
  slug: cloudbees-api-flag-get-flag-response
- name: api.flag.ListFlagConfigurationsResponse
  property_count: 1
  slug: cloudbees-api-flag-list-flag-configurations-response
- name: api.flag.ListFlagsResponse
  property_count: 1
  slug: cloudbees-api-flag-list-flags-response
- name: api.fmimpressions.GetFlagsStatusResponse
  property_count: 1
  slug: cloudbees-api-fmimpressions-get-flags-status-response
- name: api.fmimpressions.GetImpressionsResponse
  property_count: 1
  slug: cloudbees-api-fmimpressions-get-impressions-response
- name: api.fmimpressions.ImpressionParams
  property_count: 4
  slug: cloudbees-api-fmimpressions-impression-params
- name: api.service.ListServicesResponse
  property_count: 1
  slug: cloudbees-api-service-list-services-response
- name: api.TargetGroup.AddTargetGroupResponse
  property_count: 1
  slug: cloudbees-api-target-group-add-target-group-response
- name: api.TargetGroup.GetTargetGroupFlagsUsagePerEnvironmentResponse
  property_count: 1
  slug: cloudbees-api-target-group-get-target-group-flags-usage-per-environment-response
- name: api.TargetGroup.GetTargetGroupResponse
  property_count: 1
  slug: cloudbees-api-target-group-get-target-group-response
- name: api.TargetGroup.ListTargetGroupsResponse
  property_count: 1
  slug: cloudbees-api-target-group-list-target-groups-response
- name: api.TargetGroup.ListTargetGroupsWithFlagsUsageResponse
  property_count: 1
  slug: cloudbees-api-target-group-list-target-groups-with-flags-usage-response
- name: api.TargetGroup.TargetGroup
  property_count: 6
  slug: cloudbees-api-target-group-target-group
- name: api.v4.Component
  property_count: 11
  slug: cloudbees-api-v4-component
- name: api.v4.CreateDeploymentArtifactsBody
  property_count: 2
  slug: cloudbees-api-v4-create-deployment-artifacts-body
- name: api.v4.CreateDeploymentArtifactsResponse
  property_count: 1
  slug: cloudbees-api-v4-create-deployment-artifacts-response
- name: api.v4.CreateRunResponse
  property_count: 2
  slug: cloudbees-api-v4-create-run-response
- name: api.v4.CreateTeamMembershipRequest
  property_count: 2
  slug: cloudbees-api-v4-create-team-membership-request
- name: api.v4.DeleteComponentResponse
  property_count: 2
  slug: cloudbees-api-v4-delete-component-response
- name: api.v4.DeleteTeamMembershipResponse
  property_count: 2
  slug: cloudbees-api-v4-delete-team-membership-response
- name: api.v4.ListComponentsResponse
  property_count: 3
  slug: cloudbees-api-v4-list-components-response
- name: api.v4.ListTeamMembershipsResponse
  property_count: 2
  slug: cloudbees-api-v4-list-team-memberships-response
- name: api.v4.ListTeamsResponse
  property_count: 3
  slug: cloudbees-api-v4-list-teams-response
- name: api.v4.ListUsersResponse
  property_count: 3
  slug: cloudbees-api-v4-list-users-response
- name: api.v4.RunForCreate
  property_count: 19
  slug: cloudbees-api-v4-run-for-create
- name: api.v4.RunForUpdate
  property_count: 8
  slug: cloudbees-api-v4-run-for-update
- name: api.v4.Run
  property_count: 21
  slug: cloudbees-api-v4-run
- name: api.v4.TeamMember
  property_count: 2
  slug: cloudbees-api-v4-team-member
- name: api.v4.TeamWithExpansions
  property_count: 8
  slug: cloudbees-api-v4-team-with-expansions
- name: api.vsm.report.EnvironmentResponse
  property_count: 1
  slug: cloudbees-api-vsm-report-environment-response
- name: Build
  property_count: 6
  slug: cloudbees-build
- name: Computer
  property_count: 2
  slug: cloudbees-computer
- name: Jenkins
  property_count: 6
  slug: cloudbees-jenkins
- name: Job
  property_count: 7
  slug: cloudbees-job
- name: Queue
  property_count: 2
  slug: cloudbees-queue
jsonld:
- class_count: 0
  name: Cloudbees Context
  property_count: 11
  slug: cloudbees-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.cloudbees.io over HTTP requiring OAuth; 131 tools listed.
  name: CloudBees Unify MCP Server
  slug: cloudbees-unify-mcp-server
modified: '2026-09-05'
name: CloudBees
nav: Providers
network: true
overview: 'CloudBees publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including Computer API, CreateItem API, Job API, and 20 more. Tagged areas include CI/CD, Continuous Delivery, Continuous Integration, Developer Tools, and DevOps.


  The CloudBees catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  CloudBees'' developer surface includes authentication, documentation, support, engineering blog, changelog, CLI, API reference, and 46 more developer resources.'
plans:
- name: Cloudbees Plans Pricing
  plan_count: 1
  slug: cloudbees-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Cloudbees Rate Limits
  slug: cloudbees-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: CloudBees API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 6
  slug: cloudbees-rules
scopes:
- name: Cloudbees Scopes
  scope_count: 4
  slug: cloudbees-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: exemplar
  composite: 71.2
  coverage:
    artifact_dirs: 36
    catalog_earned: 70.8
    catalog_earned_first_party: 16.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 68.4
    contract_governance: 35.6
    contract_quality: 68.1
    developer_ergonomics: 75.6
    discoverability: 67.5
    operational_transparency: 81.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 70.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 80.0
      derived: 0
      marker_coverage: 34.3
      total: 35
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
    score: 0.0
screenshot: https://apis.io/screenshots/cloudbees/cloudbees-2026-06-20T174542.png
security:
- kind: authentication
  name: Cloudbees Authentication
  slug: cloudbees-authentication
  summary_line: apiKey/http/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Cloudbees Domain Security
  slug: cloudbees-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cloudbees Vulnerability Disclosure
  slug: cloudbees-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Cloudbees Trust Center
  slug: cloudbees-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
skill_count: 3
skills:
- name: Audit CloudBees Unify org and team access
  slug: cloudbees-audit-org-access
- name: Record a CloudBees Unify delivery run
  slug: cloudbees-record-a-delivery-run
- name: Roll out a CloudBees feature flag safely
  slug: cloudbees-roll-out-a-feature-flag
slug: cloudbees
tags:
- CI/CD
- Continuous Delivery
- Continuous Integration
- Developer Tools
- DevOps
- Feature Flags
- Feature Management
- Jenkins
- Release Orchestration
- Software Delivery
website: https://www.cloudbees.com/
---
