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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Workday Extend Agentic Access
  operation_count: 44
  slug: workday-extend-agentic-access
  summary_line: 44 operations · 23 acting
api_count: 16
apis:
- description: API for accessing orchestration execution data and monitoring information. Provides insights into orchestration performance, run history, and operational metrics for troubleshooting and optimization.
  name: Workday Orchestrate Insights API
  slug: workday-orchestrate-insights-api
- description: AI-powered APIs within Workday Illuminate that provide skills and sentiment analysis, document intelligence, natural language WQL queries, and machine learning forecasting capabilities. Enables develo
  name: Workday Illuminate AI API
  slug: workday-illuminate-ai-api
- description: Operations for managing application configuration settings and environment-specific parameters.
  name: Workday Extend App Configurations API
  slug: workday-extend-app-configurations-api
- description: Operations for deploying and managing Extend application instances within a tenant.
  name: Workday Extend App Deployments API
  slug: workday-extend-app-deployments-api
- description: Operations for managing application versions and release lifecycle.
  name: Workday Extend App Versions API
  slug: workday-extend-app-versions-api
- description: Operations for managing Extend applications including registration, deployment, and configuration.
  name: Workday Extend Apps API
  slug: workday-extend-apps-api
- description: Operations for defining and managing custom object types including their schemas, attributes, and relationships to standard Workday objects.
  name: Workday Extend Custom Object Definitions API
  slug: workday-extend-custom-object-definitions-api
- description: Operations for managing the fields and attributes defined within custom object schemas.
  name: Workday Extend Custom Object Fields API
  slug: workday-extend-custom-object-fields-api
- description: Operations for creating, reading, updating, and deleting custom object data instances attached to Workday business objects.
  name: Workday Extend Custom Object Instances API
  slug: workday-extend-custom-object-instances-api
- description: Operations for querying Workday business objects using the Graph API. Supports flexible field selection and relationship traversal.
  name: Workday Extend Graph Query API
  slug: workday-extend-graph-query-api
- description: Operations for triggering orchestration runs, monitoring execution status, and retrieving execution results.
  name: Workday Extend Orchestration Executions API
  slug: workday-extend-orchestration-executions-api
- description: Operations for managing individual steps within an orchestration flow, including connectors, transformations, and conditions.
  name: Workday Extend Orchestration Steps API
  slug: workday-extend-orchestration-steps-api
- description: Operations for configuring orchestration triggers including event-based, scheduled, and API-triggered orchestrations.
  name: Workday Extend Orchestration Triggers API
  slug: workday-extend-orchestration-triggers-api
- description: Operations for managing orchestration definitions including creation, configuration, versioning, and lifecycle management.
  name: Workday Extend Orchestrations API
  slug: workday-extend-orchestrations-api
- description: Operations for discovering available business objects, their fields, relationships, and query capabilities through the Graph API.
  name: Workday Extend Schema Introspection API
  slug: workday-extend-schema-introspection-api
- description: Operations for executing Workday Query Language (WQL) queries against the Workday data model. WQL provides SQL-like syntax for complex data retrieval across business objects.
  name: Workday Extend WQL Query API
  slug: workday-extend-wql-query-api
arazzos:
- description: Confirm an Extend app exists, read its current configuration, then replace the configuration values.
  name: Workday Extend Update Application Configuration
  slug: workday-extend-app-configuration-update-workflow
- description: Find the most recent running execution of an orchestration, cancel it, and confirm cancellation.
  name: Workday Extend Cancel a Running Orchestration Execution
  slug: workday-extend-cancel-running-execution-workflow
- description: Create an orchestration, attach a trigger, and activate it for execution.
  name: Workday Extend Create and Activate Orchestration
  slug: workday-extend-create-and-activate-orchestration-workflow
- description: Create a custom object definition, add a field to it, and list the resulting field schema.
  name: Workday Extend Define a Custom Object With Fields
  slug: workday-extend-define-custom-object-with-fields-workflow
- description: Find a queryable business object type, inspect its schema, then run a graph query against it.
  name: Workday Extend Discover Schema and Run a Graph Query
  slug: workday-extend-discover-schema-and-query-workflow
- description: Resolve an orchestration by search, then list its steps and triggers to build a full picture.
  name: Workday Extend Inspect an Orchestration
  slug: workday-extend-inspect-orchestration-workflow
- description: Confirm an orchestration, launch an execution with inputs, and poll until it completes.
  name: Workday Extend Launch Orchestration and Poll Execution
  slug: workday-extend-launch-orchestration-and-poll-workflow
- description: Confirm an app, create a new version, and verify the version was recorded.
  name: Workday Extend Publish a New Application Version
  slug: workday-extend-publish-app-version-workflow
- description: Register an Extend app, publish a version, deploy it, and poll until the deployment settles.
  name: Workday Extend Register and Deploy Application
  slug: workday-extend-register-and-deploy-app-workflow
- description: Deactivate an active orchestration, apply changes, and reactivate it.
  name: Workday Extend Safely Update an Orchestration
  slug: workday-extend-safe-update-orchestration-workflow
- description: Confirm a custom object definition, check whether a worker already has data, then create or update it.
  name: Workday Extend Upsert Worker Custom Object Data
  slug: workday-extend-upsert-worker-custom-object-workflow
- description: Run a WQL query to retrieve worker data, then write the result into a worker's custom object.
  name: Workday Extend WQL Query Into a Worker Custom Object
  slug: workday-extend-wql-query-to-worker-custom-object-workflow
artifact_total: 88
collections:
- collection_type: postman
  name: Workday Extend Workday Custom Objects API
  slug: postman-workday-extend-custom-objects
- collection_type: postman
  name: Workday Extend Workday Graph API
  slug: postman-workday-extend-graph-api
- collection_type: postman
  name: Workday Extend Workday Orchestration API
  slug: postman-workday-extend-orchestration
- collection_type: postman
  name: Workday Extend REST API
  slug: postman-workday-extend-rest-api
- collection_type: open
  name: Workday Extend Workday Custom Objects API
  slug: open-workday-extend-custom-objects
- collection_type: open
  name: Workday Extend Workday Graph API
  slug: open-workday-extend-graph-api
- collection_type: open
  name: Workday Extend Workday Orchestration API
  slug: open-workday-extend-orchestration
- collection_type: open
  name: Workday Extend REST API
  slug: open-workday-extend-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workday-extend-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/workday-extend-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workday-extend-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workday-extend-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/workday-extend-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/workday-extend/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-extend-app-configuration-update-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-extend-cancel-running-execution-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-extend-create-and-activate-orchestration-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-extend-define-custom-object-with-fields-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-extend-discover-schema-and-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-extend-inspect-orchestration-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-extend-launch-orchestration-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-extend-publish-app-version-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-extend-register-and-deploy-app-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-extend-safe-update-orchestration-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-extend-upsert-worker-custom-object-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/workday-extend-wql-query-to-worker-custom-object-workflow.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.workday.com/extend/getting-started/
- group: start
  title: ''
  type: Portal
  url: https://developer.workday.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.workday.com/documentation
- group: docs
  title: ''
  type: Reference
  url: https://developer.workday.com/documentation/GUID-04def314-83a7-4edf-b84c-c0a5f005b23c-enHYPHENus
- group: docs
  title: ''
  type: APIReference
  url: https://doc.workday.com/extend/reference/
- group: build
  title: ''
  type: SDKs
  url: https://doc.workday.com/extend/sdk/
- group: build
  title: ''
  type: Code Samples
  url: https://github.com/Workday/extend-js-example
- group: operate
  title: ''
  type: Community
  url: https://forum.developer.workday.com
- group: operate
  title: ''
  type: Support
  url: https://support.developer.workday.com/s/
- group: operate
  title: ''
  type: ChangeLog
  url: https://doc.workday.com/extend/release-notes/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.workday.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workday.com/en-us/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workday.com/en-us/privacy.html
- group: auth
  title: ''
  type: Authentication
  url: https://doc.workday.com/extend/authentication/
- group: operate
  title: ''
  type: RateLimits
  url: https://doc.workday.com/extend/rate-limits/
- group: company
  title: ''
  type: Blog
  url: https://blog.workday.com/en-us/introducing-workday-build-developer-platform-build-future-work-ai.html
- group: company
  title: ''
  type: Website
  url: https://www.workday.com/en-us/products/platform-product-extensions/app-development.html
- group: start
  title: ''
  type: Login
  url: https://developer.workday.com/login
- group: start
  title: ''
  type: Console
  url: https://developer.workday.com/about
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Workday
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.workday.com/en-US/home
- group: build
  title: ''
  type: Developer Tools
  url: https://api.developer.workday.com/devtools
- group: company
  title: ''
  type: Partners
  url: https://www.workday.com/en-us/company/partners/software-partners.html
- group: design
  title: ''
  type: SpectralRules
  url: rules/workday-extend-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/workday-extend-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workday-extend-app-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workday-extend-orchestration-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/workday-extend-custom-object-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/workday-extend-vocabulary.yml
created: 2025-03-14 00:00:00+00:00
description: Workday Extend is a platform that enables developers to build custom applications that integrate seamlessly with Workday. It provides APIs, development tools, and a runtime environment for creating tailored solutions that extend Workday's core functionality.
examples:
- key_count: 2
  name: Workday Extend Deploy App Example
  slug: workday-extend-deploy-app-example
- key_count: 2
  name: Workday Extend Execute Orchestration Example
  slug: workday-extend-execute-orchestration-example
- key_count: 2
  name: Workday Extend List Apps Example
  slug: workday-extend-list-apps-example
finops:
- name: Workday Extend Finops
  service_category: Low-Code Platform
  slug: workday-extend-finops
image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
json_schemas:
- name: Workday Extend Application
  property_count: 11
  slug: workday-extend-app
- name: AppConfiguration
  property_count: 6
  slug: workday-extend-appconfiguration
- name: AppConfigurationUpdate
  property_count: 1
  slug: workday-extend-appconfigurationupdate
- name: AppCreate
  property_count: 3
  slug: workday-extend-appcreate
- name: AppDeployment
  property_count: 8
  slug: workday-extend-appdeployment
- name: AppDeploymentCreate
  property_count: 2
  slug: workday-extend-appdeploymentcreate
- name: AppUpdate
  property_count: 3
  slug: workday-extend-appupdate
- name: AppVersion
  property_count: 7
  slug: workday-extend-appversion
- name: AppVersionCreate
  property_count: 2
  slug: workday-extend-appversioncreate
- name: Workday Custom Object Definition
  property_count: 9
  slug: workday-extend-custom-object
- name: CustomObjectData
  property_count: 0
  slug: workday-extend-customobjectdata
- name: CustomObjectDefinition
  property_count: 11
  slug: workday-extend-customobjectdefinition
- name: CustomObjectDefinitionCreate
  property_count: 5
  slug: workday-extend-customobjectdefinitioncreate
- name: CustomObjectDefinitionUpdate
  property_count: 2
  slug: workday-extend-customobjectdefinitionupdate
- name: CustomObjectField
  property_count: 10
  slug: workday-extend-customobjectfield
- name: CustomObjectFieldCreate
  property_count: 7
  slug: workday-extend-customobjectfieldcreate
- name: CustomObjectInstance
  property_count: 7
  slug: workday-extend-customobjectinstance
- name: ErrorResponse
  property_count: 2
  slug: workday-extend-errorresponse
- name: GraphQueryRequest
  property_count: 4
  slug: workday-extend-graphqueryrequest
- name: GraphQueryResponse
  property_count: 3
  slug: workday-extend-graphqueryresponse
- name: GraphSchema
  property_count: 2
  slug: workday-extend-graphschema
- name: Workday Orchestration
  property_count: 10
  slug: workday-extend-orchestration
- name: OrchestrationCreate
  property_count: 3
  slug: workday-extend-orchestrationcreate
- name: OrchestrationExecution
  property_count: 13
  slug: workday-extend-orchestrationexecution
- name: OrchestrationLaunch
  property_count: 1
  slug: workday-extend-orchestrationlaunch
- name: OrchestrationStep
  property_count: 6
  slug: workday-extend-orchestrationstep
- name: OrchestrationTrigger
  property_count: 6
  slug: workday-extend-orchestrationtrigger
- name: OrchestrationTriggerCreate
  property_count: 4
  slug: workday-extend-orchestrationtriggercreate
- name: OrchestrationUpdate
  property_count: 2
  slug: workday-extend-orchestrationupdate
- name: ResourceReference
  property_count: 3
  slug: workday-extend-resourcereference
- name: SchemaField
  property_count: 5
  slug: workday-extend-schemafield
- name: SchemaRelationship
  property_count: 4
  slug: workday-extend-schemarelationship
- name: SchemaType
  property_count: 5
  slug: workday-extend-schematype
- name: WqlQueryRequest
  property_count: 1
  slug: workday-extend-wqlqueryrequest
- name: WqlQueryResponse
  property_count: 3
  slug: workday-extend-wqlqueryresponse
json_structures:
- name: Workday Extend App Structure
  property_count: 0
  slug: workday-extend-app-structure
- name: Workday Extend Orchestration Structure
  property_count: 0
  slug: workday-extend-orchestration-structure
- name: Workday Extend Structure
  property_count: 0
  slug: workday-extend-structure
jsonld:
- class_count: 29
  name: Workday Extend Context
  property_count: 2
  slug: workday-extend-context
layout: provider
modified: '2026-05-19'
name: Workday Extend
nav: Providers
network: true
overview: 'Workday Extend publishes 14 APIs on the [APIs.io](https://apis.io/) network, including App Configurations API, App Deployments API, App Versions API, and 11 more. Tagged areas include Automation, Custom Applications, Enterprise, Extensions, and HCM.


  The Workday Extend catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Workday Extend''s developer surface includes authentication, getting-started guide, developer portal, documentation, API reference, support, changelog, and 40 more developer resources.'
plans:
- name: Workday Extend Plans Pricing
  plan_count: 1
  slug: workday-extend-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 1
  name: Workday Extend Rate Limits
  slug: workday-extend-rate-limits
rules:
- name: Workday Extend API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: workday-extend-jsonschema-spectral-rules
- name: Workday Extend API Rules
  rule_count: 15
  severity_counts:
    error: 6
    hint: 1
    info: 0
    warn: 8
  slug: workday-extend-rules
scopes:
- name: Workday Extend Scopes
  scope_count: 9
  slug: workday-extend-scopes
  summary_line: 9 scopes · authorizationCode
score:
  band: exemplar
  composite: 72.9
  delta: 3.2
  facets:
    commercial_clarity: 71.1
    contract_quality: 67.3
    developer_ergonomics: 69.6
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 57.9
  previous_composite: 69.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/workday-extend/refs/heads/main/screenshots/workday-extend-2026-06-20T201559.png
security:
- kind: authentication
  name: Workday Extend Authentication
  slug: workday-extend-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Workday Extend Domain Security
  slug: workday-extend-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Workday Extend Trust Center
  slug: workday-extend-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
slug: workday-extend
tags:
- Automation
- Custom Applications
- Enterprise
- Extensions
- HCM
- Human Capital Management
- Integration
- Orchestration
- PaaS
website: https://www.workday.com/en-us/products/platform-product-extensions/app-development.html
---
