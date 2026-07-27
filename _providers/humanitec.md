---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 119
  human_in_the_loop: 1
  name: Humanitec Agentic Access
  operation_count: 221
  slug: humanitec-agentic-access
  summary_line: 221 operations · 119 acting · 1 human-in-the-loop
api_count: 45
apis:
- description: Resource Account Types define cloud providers or protocols to which a resource account can belong. <SchemaDefinition schemaRef="#/components/schemas/AccountTypeRequest" />
  name: Humanitec AccountType API
  slug: humanitec-accounttype-api
- description: Active Resources represent the concrete resources provisioned for an Environment. They are provisioned on the first deployment after a dependency on a particular resource type is introduced into an En
  name: Humanitec ActiveResource API
  slug: humanitec-activeresource-api
- description: An object containing the details of an Agent. <SchemaDefinition schemaRef="#/components/schemas/Agent" />
  name: Humanitec Agents API
  slug: humanitec-agents-api
- description: An Application is a collection of Workloads that work together. When deployed, all Workloads in an Application are deployed to the same namespace. Apps are the root of the configuration tree holding E
  name: Humanitec Application API
  slug: humanitec-application-api
- description: Artefacts can be registered with Humanitec. Continuous Integration (CI) pipelines notify Humanitec when a new version of an Artefact becomes available. Humanitec tracks the Artefact along with metadat
  name: Humanitec Artefact API
  slug: humanitec-artefact-api
- description: Details of a Container Artefact Version <SchemaDefinition schemaRef="#/components/schemas/ContainerArtefactVersion" />
  name: Humanitec ArtefactVersion API
  slug: humanitec-artefactversion-api
- description: An entry in the audit log <SchemaDefinition schemaRef="#/components/schemas/AuditLogEntry" />
  name: Humanitec AuditLogs API
  slug: humanitec-auditlogs-api
- description: An Automation Rule defining how and when artefacts in an environment should be updated. <SchemaDefinition schemaRef="#/components/schemas/AutomationRuleRequest" />
  name: Humanitec AutomationRule API
  slug: humanitec-automationrule-api
- description: A Deployment Delta (or just "Delta") describes the changes that must be applied to one Deployment Set to generate another Deployment Set. Deployment Deltas are the only way to create new Deployment Se
  name: Humanitec Delta API
  slug: humanitec-delta-api
- description: Deployments represent updates to the running state of an Environment. Deployments are made by applying _Deltas_ to a state defined by an existing Deployment. The Environment’s from_deploy property def
  name: Humanitec Deployment API
  slug: humanitec-deployment-api
- description: DriverDefinition describes the resource driver. Resource Drivers are code that fulfils the Humanitec Resource Driver Interface. This interface allows for certain actions to be performed on resources s
  name: Humanitec DriverDefinition API
  slug: humanitec-driverdefinition-api
- description: Environments are independent spaces where Applications can run. An Application is always deployed into an Environment. <SchemaDefinition schemaRef="#/components/schemas/EnvironmentResponse" />
  name: Humanitec Environment API
  slug: humanitec-environment-api
- description: The EnvironmentPausedInfo API from Humanitec — 1 operation(s) for environmentpausedinfo.
  name: Humanitec EnvironmentPausedInfo API
  slug: humanitec-environmentpausedinfo-api
- description: Environment Types are a way of grouping and managing Environments. Every Environment has exactly 1 Environment Type. Environment Types can be used with External Resources to manage where resources suc
  name: Humanitec EnvironmentType API
  slug: humanitec-environmenttype-api
- description: Webhook is a special type of a Job. It performs an HTTPS request to a specified URL with specified headers. <SchemaDefinition schemaRef="#/components/schemas/WebhookRequest" />
  name: Humanitec Event API
  slug: humanitec-event-api
- description: GroupRequest holds the definition of a new group. <SchemaDefinition schemaRef="#/components/schemas/GroupRequest" />
  name: Humanitec Group API
  slug: humanitec-group-api
- description: The HumanitecPublicKeys API from Humanitec — 1 operation(s) for humanitecpublickeys.
  name: Humanitec HumanitecPublicKeys API
  slug: humanitec-humanitecpublickeys-api
- description: 'DEPRECATED: This type exists for historical compatibility and should not be used. Please use the [Artefact API](https://api-docs.humanitec.com/#tag/Artefact) instead. Container Images (known simply as'
  name: Humanitec Image API
  slug: humanitec-image-api
- description: A container log entry. <SchemaDefinition schemaRef="#/components/schemas/OutputEntryResponse" />
  name: Humanitec Logs API
  slug: humanitec-logs-api
- description: 'Matching Criteria are a set of rules used to choose which Resource Definition to use to provision a particular Resource Type. Matching criteria are made up in order of specificity with least specific '
  name: Humanitec MatchingCriteria API
  slug: humanitec-matchingcriteria-api
- description: An Organization is the top level object in Humanitec. All other objects belong to an Organization. <SchemaDefinition schemaRef="#/components/schemas/OrganizationResponse" />
  name: Humanitec Organization API
  slug: humanitec-organization-api
- description: An approval object <SchemaDefinition schemaRef="#/components/schemas/PipelineApprovalRequest" />
  name: Humanitec PipelineApprovals API
  slug: humanitec-pipelineapprovals-api
- description: Details of a Run within the Pipeline. <SchemaDefinition schemaRef="#/components/schemas/PipelineRun" />
  name: Humanitec PipelineRuns API
  slug: humanitec-pipelineruns-api
- description: An object containing the details of a Pipeline. <SchemaDefinition schemaRef="#/components/schemas/Pipeline" />
  name: Humanitec Pipelines API
  slug: humanitec-pipelines-api
- description: The public API from Humanitec — 141 operation(s) for public.
  name: Humanitec public API
  slug: humanitec-public-api
- description: PublicKey stores a Public Key an organization shares with Humanitec. <SchemaDefinition schemaRef="#/components/schemas/PublicKey" />
  name: Humanitec PublicKeys API
  slug: humanitec-publickeys-api
- description: Humanitec can be used to manage registry credentials. The Registry object represents how to match credentials to a particular registry. Humanitec supports all Docker compatible registries as well as t
  name: Humanitec Registry API
  slug: humanitec-registry-api
- description: null <SchemaDefinition schemaRef="#/components/schemas/ReplicasRequest" />
  name: Humanitec Replicas API
  slug: humanitec-replicas-api
- description: ResourceAccount represents the account being used to access a resource. Resource Accounts hold credentials that are required to provision and manage resources. <SchemaDefinition schemaRef="#/component
  name: Humanitec ResourceAccount API
  slug: humanitec-resourceaccount-api
- description: The ResourceClass API from Humanitec — 3 operation(s) for resourceclass.
  name: Humanitec ResourceClass API
  slug: humanitec-resourceclass-api
- description: A Resource Definitions describes how and when a resource should be provisioned. It links a driver (the how) along with a Matching Criteria (the when) to a Resource Type. This allows Humanitec to invok
  name: Humanitec ResourceDefinition API
  slug: humanitec-resourcedefinition-api
- description: A Resource Definition Version represents a version of a Resource Definition. <SchemaDefinition schemaRef="#/components/schemas/ResourceDefinitionVersion" />
  name: Humanitec ResourceDefinitionVersion API
  slug: humanitec-resourcedefinitionversion-api
- description: ResourceProvisionRequest is the payload passed to the resource provisioner, specifying the resources to be provisioned. <SchemaDefinition schemaRef="#/components/schemas/ResourceProvisionRequestReques
  name: Humanitec ResourceProvision API
  slug: humanitec-resourceprovision-api
- description: Resources Types define the technology that Applications can have dependencies on. Each Resource Type also defines a set of input parameters (`inputs_schema`), and a set of output data (`outputs_schema
  name: Humanitec ResourceType API
  slug: humanitec-resourcetype-api
- description: RuntimeInfo object returned by the runtime endpoint. Represents a list post statuses grouped by modules and controllers (deployments and stateful sets). <SchemaDefinition schemaRef="#/components/schem
  name: Humanitec RuntimeInfo API
  slug: humanitec-runtimeinfo-api
- description: Secret Store represents external secret management system used by an organization to store secrets referenced in Humanitec. <SchemaDefinition schemaRef="#/components/schemas/SecretStoreRequest" />
  name: Humanitec SecretStore API
  slug: humanitec-secretstore-api
- description: A Deployment Set (or just "Set") defines all of the non-Environment specific configuration for Modules and External Resources. Each of these Modules or External Resources has a unique name. Deployment
  name: Humanitec Set API
  slug: humanitec-set-api
- description: Holds metadata about a token. `expires_at` is excluded if token does not expire. <SchemaDefinition schemaRef="#/components/schemas/TokenInfoResponse" />
  name: Humanitec TokenInfo API
  slug: humanitec-tokeninfo-api
- description: The UserInvite API from Humanitec — 1 operation(s) for userinvite.
  name: Humanitec UserInvite API
  slug: humanitec-userinvite-api
- description: UserProfile holds the profile information of a user <SchemaDefinition schemaRef="#/components/schemas/UserProfileResponse" />
  name: Humanitec UserProfile API
  slug: humanitec-userprofile-api
- description: Holds the mapping of role for a subject on a particular object. <SchemaDefinition schemaRef="#/components/schemas/UserRoleRequest" />
  name: Humanitec UserRole API
  slug: humanitec-userrole-api
- description: Shared Values can be used to manage variables and configuration that might vary between environments. They are also the way that secrets can be stored securely. Shared Values are by default shared acr
  name: Humanitec Value API
  slug: humanitec-value-api
- description: A Value Set Version can be used as a track record of Shared Values changes, to restore a previous version of a Shared Value or Value Set, or to purge a Shared Value if it shouldn't be accessible anymo
  name: Humanitec ValueSetVersion API
  slug: humanitec-valuesetversion-api
- description: Workload Profiles provide the baseline configuration for Workloads in Applications in Humanitec. Developers can configure various features of a workload profile to suit their needs. Examples of featur
  name: Humanitec WorkloadProfile API
  slug: humanitec-workloadprofile-api
- description: The WorkloadProfileFeatures API from Humanitec — 1 operation(s) for workloadprofilefeatures.
  name: Humanitec WorkloadProfileFeatures API
  slug: humanitec-workloadprofilefeatures-api
artifact_total: 51
collections:
- collection_type: open
  name: Humanitec API
  slug: open-humanitec
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/humanitec-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/humanitec-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/humanitec
- group: start
  title: ''
  type: Portal
  url: https://developer.humanitec.com/
- group: company
  title: ''
  type: Website
  url: https://humanitec.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.humanitec.com/
- group: start
  title: ''
  type: Signup
  url: https://app.humanitec.io/sign-up
- group: company
  title: ''
  type: Blog
  url: https://humanitec.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/humanitec
- group: commercial
  title: ''
  type: TermsOfService
  url: https://humanitec.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://humanitec.com/privacy-policy
created: '2026-03-16'
description: Humanitec is a platform engineering company that provides an Internal Developer Platform (IDP) for managing applications, deployments, environments, and resources through self-service developer workflows. The Humanitec Platform Orchestrator API enables teams to programmatically manage organizations, applications, environments, deployments, workloads, resources, and integrations.
finops:
- name: Humanitec Finops
  service_category: API
  slug: humanitec-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/humanitec.png
layout: provider
modified: '2026-05-19'
name: Humanitec
nav: Providers
network: true
overview: 'Humanitec publishes 45 APIs on the [APIs.io](https://apis.io/) network, including AccountType API, ActiveResource API, Agents API, and 42 more. Tagged areas include Deployments, DevOps, Internal Developer Platform, Platform Engineering, and Platform Orchestrator.


  Humanitec''s developer surface includes developer portal, documentation, signup flow, engineering blog, and 7 more developer resources.'
plans:
- name: Humanitec Plans Pricing
  plan_count: 3
  slug: humanitec-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Humanitec Rate Limits
  slug: humanitec-rate-limits
score:
  band: thin
  composite: 40.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.0
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/humanitec/refs/heads/main/screenshots/humanitec-2026-06-20T182935.png
security:
- kind: domain-security
  name: Humanitec Domain Security
  slug: humanitec-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: humanitec
tags:
- Deployments
- DevOps
- Internal Developer Platform
- Platform Engineering
- Platform Orchestrator
website: https://humanitec.com/
---
