---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 36
  human_in_the_loop: 1
  name: Dataiku Agentic Access
  operation_count: 88
  slug: dataiku-agentic-access
  summary_line: 88 operations · 36 acting · 1 human-in-the-loop
api_count: 34
apis:
- description: Python client library for interacting with Dataiku DSS.
  name: Dataiku Python API
  slug: dataiku-python-api
- description: Internal API for use within recipes, notebooks, and plugins in Dataiku DSS.
  name: Dataiku Internal API
  slug: dataiku-internal-api
- description: R client library for interacting with Dataiku DSS.
  name: Dataiku R API
  slug: dataiku-r-api
- description: JavaScript API for building custom web applications that read from Dataiku datasets within DSS.
  name: Dataiku JavaScript API
  slug: dataiku-javascript-api
- description: Scala API for reading and writing DSS datasets from the Spark and Scala environment within Dataiku DSS.
  name: Dataiku Scala API
  slug: dataiku-scala-api
- description: API for developing custom plugins that extend Dataiku DSS with custom datasets, recipes, processors, and web applications.
  name: Dataiku Plugin API
  slug: dataiku-plugin-api
- description: Manage sign-off workflows on artifacts
  name: Dataiku Artifact Sign-Offs API
  slug: dataiku-artifact-sign-offs-api
- description: Manage governed artifacts (models, projects, etc.)
  name: Dataiku Artifacts API
  slug: dataiku-artifacts-api
- description: Manage API keys for service access
  name: Dataiku Authentication API
  slug: dataiku-authentication-api
- description: Manage blueprint version definitions
  name: Dataiku Blueprint Versions API
  slug: dataiku-blueprint-versions-api
- description: Manage governance blueprints that define artifact types
  name: Dataiku Blueprints API
  slug: dataiku-blueprints-api
- description: Import and export project bundles
  name: Dataiku Bundles API
  slug: dataiku-bundles-api
- description: Manage code environments for Python and R
  name: Dataiku Code Envs API
  slug: dataiku-code-envs-api
- description: Manage data connections
  name: Dataiku Connections API
  slug: dataiku-connections-api
- description: Manage custom fields on artifacts
  name: Dataiku Custom Fields API
  slug: dataiku-custom-fields-api
- description: Manage datasets within projects
  name: Dataiku Datasets API
  slug: dataiku-datasets-api
- description: Manage instance-level settings
  name: Dataiku General Settings API
  slug: dataiku-general-settings-api
- description: Manage service generations (versions)
  name: Dataiku Generations API
  slug: dataiku-generations-api
- description: Manage global API keys
  name: Dataiku Global API Keys API
  slug: dataiku-global-api-keys-api
- description: Manage DSS groups
  name: Dataiku Groups API
  slug: dataiku-groups-api
- description: Run and monitor build jobs
  name: Dataiku Jobs API
  slug: dataiku-jobs-api
- description: Manage folders for unstructured data
  name: Dataiku Managed Folders API
  slug: dataiku-managed-folders-api
- description: Manage user-defined meanings
  name: Dataiku Meanings API
  slug: dataiku-meanings-api
- description: Retrieve metrics and health information
  name: Dataiku Metrics API
  slug: dataiku-metrics-api
- description: Manage model evaluation stores
  name: Dataiku Model Evaluation Stores API
  slug: dataiku-model-evaluation-stores-api
- description: Manage DSS plugins
  name: Dataiku Plugins API
  slug: dataiku-plugins-api
- description: Manage DSS projects
  name: Dataiku Projects API
  slug: dataiku-projects-api
- description: Manage recipes and data transformations
  name: Dataiku Recipes API
  slug: dataiku-recipes-api
- description: Manage governance roles and assignments
  name: Dataiku Roles API
  slug: dataiku-roles-api
- description: Manage trained machine learning models
  name: Dataiku Saved Models API
  slug: dataiku-saved-models-api
- description: Manage and trigger automation scenarios
  name: Dataiku Scenarios API
  slug: dataiku-scenarios-api
- description: The Services API from Dataiku — 4 operation(s) for services.
  name: Dataiku Services API
  slug: dataiku-services-api
- description: Execute SQL queries on connections
  name: Dataiku SQL Queries API
  slug: dataiku-sql-queries-api
- description: Manage Govern users
  name: Dataiku Users API
  slug: dataiku-users-api
arazzos:
- description: List a project's recipes, read one recipe's inputs and outputs, and list the project's jobs.
  name: Dataiku Audit Recipe and Project Jobs
  slug: dataiku-audit-recipe-and-jobs-workflow
- description: Create a DSS project, add a managed dataset to it, and confirm the dataset definition.
  name: Dataiku Bootstrap Project with First Dataset
  slug: dataiku-bootstrap-project-workflow
- description: List a project's managed folders and read the file contents of one folder.
  name: Dataiku Browse Managed Folder Contents
  slug: dataiku-browse-managed-folder-workflow
- description: Start a build job for a dataset output and poll the job until it reaches a terminal state.
  name: Dataiku Build Dataset and Poll Job
  slug: dataiku-build-dataset-job-workflow
- description: Create a dataset, apply an explicit schema to it, and kick off a build job.
  name: Dataiku Create Dataset, Set Schema, and Build
  slug: dataiku-create-dataset-set-schema-build-workflow
- description: Create a governed artifact under a blueprint, set its custom field values, and read them back.
  name: Dataiku Create Govern Artifact with Custom Fields
  slug: dataiku-create-govern-artifact-workflow
- description: Create a governance blueprint, add a first version to it, and read the version back.
  name: Dataiku Create Govern Blueprint and Version
  slug: dataiku-create-govern-blueprint-version-workflow
- description: Verify a project, create an export bundle for it, and list bundles to confirm the export.
  name: Dataiku Export Project Bundle
  slug: dataiku-export-project-bundle-workflow
- description: Import a generation bundle for a service, preload it into memory, then switch the service to it.
  name: Dataiku Import and Preload API Node Generation
  slug: dataiku-import-and-preload-generation-workflow
- description: List a project's datasets, fetch a dataset definition, and read a sample of its rows.
  name: Dataiku Inspect and Read a Dataset
  slug: dataiku-inspect-and-read-dataset-workflow
- description: List a project's saved models and fetch the details of one model including its active version.
  name: Dataiku Inspect Saved Model
  slug: dataiku-inspect-saved-model-workflow
- description: Verify a deployed service, list its generations, switch the active generation, and enable the service.
  name: Dataiku Promote API Node Generation
  slug: dataiku-promote-apinode-generation-workflow
- description: Create a DSS user, confirm it by reading the user back, and assign groups via update.
  name: Dataiku Provision DSS User
  slug: dataiku-provision-user-workflow
- description: List an artifact's sign-off steps, read one step, and add an approve or reject review to it.
  name: Dataiku Review Artifact Sign-Off
  slug: dataiku-review-artifact-signoff-workflow
- description: Trigger a scenario run and poll its lightweight status until it is no longer running.
  name: Dataiku Run Scenario and Poll to Completion
  slug: dataiku-run-scenario-and-poll-workflow
- description: Verify a DSS connection exists, then execute a SQL query against it and return the rows.
  name: Dataiku Resolve Connection and Run SQL Query
  slug: dataiku-run-sql-query-workflow
- description: Read a project's current metadata, then write an updated label, description, and tags.
  name: Dataiku Tag Project Metadata
  slug: dataiku-tag-project-metadata-workflow
- description: Verify a project, delete a dataset within it, then delete the project itself.
  name: Dataiku Teardown Project
  slug: dataiku-teardown-project-workflow
artifact_total: 141
collections:
- collection_type: postman
  name: Dataiku API Node Administration API
  slug: postman-dataiku-api-node-admin
- collection_type: postman
  name: Dataiku Govern API
  slug: postman-dataiku-govern-api
- collection_type: postman
  name: Dataiku DSS Public API
  slug: postman-dataiku-public-api
- collection_type: open
  name: Dataiku API Node Administration API
  slug: open-dataiku-api-node-admin
- collection_type: open
  name: Dataiku Govern API
  slug: open-dataiku-govern-api
- collection_type: open
  name: Dataiku DSS Public API
  slug: open-dataiku-public-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dataiku-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dataiku-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dataiku-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dataiku-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/dataiku/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dataiku-audit-recipe-and-jobs-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dataiku-bootstrap-project-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dataiku-browse-managed-folder-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dataiku-build-dataset-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dataiku-create-dataset-set-schema-build-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dataiku-create-govern-artifact-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dataiku-create-govern-blueprint-version-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dataiku-export-project-bundle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dataiku-import-and-preload-generation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dataiku-inspect-and-read-dataset-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dataiku-inspect-saved-model-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dataiku-promote-apinode-generation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dataiku-provision-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dataiku-review-artifact-signoff-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dataiku-run-scenario-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dataiku-run-sql-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dataiku-tag-project-metadata-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dataiku-teardown-project-workflow.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dataiku.com/product/get-started/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.dataiku.com/
- group: operate
  title: ''
  type: Community
  url: https://community.dataiku.com/
- group: learn
  title: ''
  type: Academy
  url: https://academy.dataiku.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dataiku.com/product/pricing/
- group: company
  title: ''
  type: Blog
  url: https://blog.dataiku.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/dataiku
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dataiku.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dataiku.com/privacy/
- group: start
  title: ''
  type: Portal
  url: https://developer.dataiku.com/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.dataiku.com/latest/api-reference/index.html
- group: operate
  title: ''
  type: Support
  url: https://support.dataiku.com/
- group: other
  title: ''
  type: Knowledge Base
  url: https://knowledge.dataiku.com/latest/
- group: operate
  title: ''
  type: ChangeLog
  url: https://doc.dataiku.com/dss/latest/release_notes/index.html
- group: auth
  title: ''
  type: Trust Center
  url: https://www.dataiku.com/legal/trust/
- group: build
  title: ''
  type: Plugins
  url: https://www.dataiku.com/product/plugins/
- group: learn
  title: ''
  type: Webinars
  url: https://www.dataiku.com/stories/webinars/
- group: start
  title: ''
  type: Signup
  url: https://www.dataiku.com/product/get-started/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dataiku
- group: other
  title: ''
  type: X
  url: https://twitter.com/dataiku
- group: design
  title: ''
  type: JSONLD
  url: json-ld/dataiku-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/dataiku-project-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/dataiku-dataset-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/dataiku-vocabulary.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/dataiku-capabilities.yml
- group: design
  title: ''
  type: Rules
  url: rules/dataiku-rules.yml
created: '2024-01-01'
description: Dataiku is an advanced data science and machine learning platform that enables teams to build and deploy AI applications at scale.
finops:
- name: Dataiku Finops
  service_category: AI Platform
  slug: dataiku-finops
image: https://www.dataiku.com/static/img/logo.png
json_schemas:
- name: Artifact
  property_count: 10
  slug: dataiku-artifact
- name: ArtifactSummary
  property_count: 6
  slug: dataiku-artifactsummary
- name: AuthKey
  property_count: 5
  slug: dataiku-authkey
- name: Blueprint
  property_count: 8
  slug: dataiku-blueprint
- name: BlueprintSummary
  property_count: 5
  slug: dataiku-blueprintsummary
- name: BlueprintVersion
  property_count: 7
  slug: dataiku-blueprintversion
- name: BlueprintVersionSummary
  property_count: 4
  slug: dataiku-blueprintversionsummary
- name: BundleSummary
  property_count: 4
  slug: dataiku-bundlesummary
- name: CodeEnv
  property_count: 5
  slug: dataiku-codeenv
- name: CodeEnvSummary
  property_count: 2
  slug: dataiku-codeenvsummary
- name: Connection
  property_count: 5
  slug: dataiku-connection
- name: ConnectionSummary
  property_count: 2
  slug: dataiku-connectionsummary
- name: CreateArtifactRequest
  property_count: 4
  slug: dataiku-createartifactrequest
- name: CreateAuthKeyRequest
  property_count: 2
  slug: dataiku-createauthkeyrequest
- name: CreateBlueprintRequest
  property_count: 3
  slug: dataiku-createblueprintrequest
- name: CreateBlueprintVersionRequest
  property_count: 1
  slug: dataiku-createblueprintversionrequest
- name: CreateBundleRequest
  property_count: 1
  slug: dataiku-createbundlerequest
- name: CreateDatasetRequest
  property_count: 5
  slug: dataiku-createdatasetrequest
- name: CreateProjectRequest
  property_count: 3
  slug: dataiku-createprojectrequest
- name: CreateUserRequest
  property_count: 6
  slug: dataiku-createuserrequest
- name: Dataiku DSS Dataset
  property_count: 14
  slug: dataiku-dataset
- name: DatasetData
  property_count: 3
  slug: dataiku-datasetdata
- name: DatasetSchema
  property_count: 2
  slug: dataiku-datasetschema
- name: DelegateSignOffRequest
  property_count: 2
  slug: dataiku-delegatesignoffrequest
- name: Endpoint
  property_count: 3
  slug: dataiku-endpoint
- name: FieldSetting
  property_count: 6
  slug: dataiku-fieldsetting
- name: GeneralSettings
  property_count: 4
  slug: dataiku-generalsettings
- name: Generation
  property_count: 5
  slug: dataiku-generation
- name: GenerationSummary
  property_count: 3
  slug: dataiku-generationsummary
- name: GlobalAPIKey
  property_count: 6
  slug: dataiku-globalapikey
- name: GovernUser
  property_count: 4
  slug: dataiku-governuser
- name: Group
  property_count: 4
  slug: dataiku-group
- name: HealthStatus
  property_count: 2
  slug: dataiku-healthstatus
- name: Job
  property_count: 7
  slug: dataiku-job
- name: JobActivity
  property_count: 3
  slug: dataiku-jobactivity
- name: JobSummary
  property_count: 5
  slug: dataiku-jobsummary
- name: ManagedFolder
  property_count: 4
  slug: dataiku-managedfolder
- name: ManagedFolderContents
  property_count: 1
  slug: dataiku-managedfoldercontents
- name: Meaning
  property_count: 4
  slug: dataiku-meaning
- name: Metrics
  property_count: 5
  slug: dataiku-metrics
- name: ModelEvaluationStoreSummary
  property_count: 3
  slug: dataiku-modelevaluationstoresummary
- name: ModelVersion
  property_count: 3
  slug: dataiku-modelversion
- name: Plugin
  property_count: 6
  slug: dataiku-plugin
- name: PluginSummary
  property_count: 4
  slug: dataiku-pluginsummary
- name: Dataiku DSS Project
  property_count: 12
  slug: dataiku-project
- name: ProjectMetadata
  property_count: 5
  slug: dataiku-projectmetadata
- name: ProjectSummary
  property_count: 4
  slug: dataiku-projectsummary
- name: Recipe
  property_count: 8
  slug: dataiku-recipe
- name: RecipeSummary
  property_count: 3
  slug: dataiku-recipesummary
- name: Role
  property_count: 4
  slug: dataiku-role
- name: SavedModel
  property_count: 6
  slug: dataiku-savedmodel
- name: SavedModelSummary
  property_count: 4
  slug: dataiku-savedmodelsummary
- name: Scenario
  property_count: 7
  slug: dataiku-scenario
- name: ScenarioLight
  property_count: 3
  slug: dataiku-scenariolight
- name: ScenarioRun
  property_count: 4
  slug: dataiku-scenariorun
- name: ScenarioSummary
  property_count: 5
  slug: dataiku-scenariosummary
- name: SchemaColumn
  property_count: 4
  slug: dataiku-schemacolumn
- name: Service
  property_count: 5
  slug: dataiku-service
- name: ServiceSummary
  property_count: 4
  slug: dataiku-servicesummary
- name: SignOff
  property_count: 5
  slug: dataiku-signoff
- name: SignOffConfiguration
  property_count: 1
  slug: dataiku-signoffconfiguration
- name: SignOffReview
  property_count: 4
  slug: dataiku-signoffreview
- name: SignOffReviewRequest
  property_count: 2
  slug: dataiku-signoffreviewrequest
- name: SignOffStep
  property_count: 5
  slug: dataiku-signoffstep
- name: SqlQueryRequest
  property_count: 4
  slug: dataiku-sqlqueryrequest
- name: SqlQueryResult
  property_count: 2
  slug: dataiku-sqlqueryresult
- name: StartJobRequest
  property_count: 1
  slug: dataiku-startjobrequest
- name: Tag
  property_count: 3
  slug: dataiku-tag
- name: User
  property_count: 6
  slug: dataiku-user
- name: WorkflowConfiguration
  property_count: 2
  slug: dataiku-workflowconfiguration
- name: WorkflowStatus
  property_count: 3
  slug: dataiku-workflowstatus
- name: WorkflowTransition
  property_count: 2
  slug: dataiku-workflowtransition
json_structures:
- name: Dataiku Structure
  property_count: 0
  slug: dataiku-structure
jsonld:
- class_count: 0
  name: Dataiku Context
  property_count: 14
  slug: dataiku-context
layout: provider
modified: '2026-05-19'
name: Dataiku
nav: Providers
network: true
overview: 'Dataiku publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Artifact Sign-Offs API, Artifacts API, Authentication API, and 25 more. Tagged areas include Analytics, Artificial Intelligence, Data Platform, Data Science, and Machine Learning.


  The Dataiku catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Dataiku''s developer surface includes authentication, getting-started guide, documentation, academy / training, pricing, engineering blog, GitHub presence, and 42 more developer resources.'
plans:
- name: Dataiku Plans Pricing
  plan_count: 3
  slug: dataiku-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Dataiku Rate Limits
  slug: dataiku-rate-limits
rules:
- name: Dataiku API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: dataiku-jsonschema-spectral-rules
- name: Dataiku API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: dataiku-rules
score:
  band: strong
  composite: 61.7
  delta: -4.6
  facets:
    commercial_clarity: 71.1
    contract_quality: 64.4
    developer_ergonomics: 56.5
    discoverability: 50.0
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 66.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 28
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dataiku/refs/heads/main/screenshots/dataiku-2026-06-20T175643.png
security:
- kind: authentication
  name: Dataiku Authentication
  slug: dataiku-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dataiku Domain Security
  slug: dataiku-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dataiku Vulnerability Disclosure
  slug: dataiku-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dataiku
tags:
- Analytics
- Artificial Intelligence
- Data Platform
- Data Science
- Machine Learning
website: https://developer.dataiku.com/latest/
---
