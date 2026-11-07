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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 59
  human_in_the_loop: 1
  name: Soda Data Agentic Access
  operation_count: 103
  slug: soda-data-agentic-access
  summary_line: 103 operations · 59 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://cloud.soda.io
  baseurl_source: declared
  description: The Attributes surface of the Soda Cloud v4 API — 4 operation(s) across 2 path(s).
  name: Soda Attributes API
  phrasing_intents:
  - id: GET/api/v1/attributes
    intent: List custom attributes
    question: Which custom attributes are defined in my Soda Cloud organization?
  - id: POST/api/v1/attributes
    intent: Create a custom attribute
    question: How do I add a new custom attribute like 'data domain' for datasets?
  - id: POST/api/v1/attributes/{attributeId}
    intent: Update an existing attribute
    question: Can I rename the label of an attribute that already exists?
  - id: DELETE/api/v1/attributes/{attributeId}
    intent: Delete an attribute
    question: How do I remove a custom attribute I no longer use?
  phrasing_ops: 4
  slug: soda-data-attributes-api
- baseURL: https://cloud.soda.io
  baseurl_source: declared
  description: The Checks surface of the Soda Cloud v4 API — 2 operation(s) across 2 path(s).
  name: Soda Checks API
  phrasing_intents:
  - id: GET/api/v1/checks
    intent: List data quality checks
    question: Which data quality checks exist on a given dataset?
  - id: DELETE/api/v1/checks/{checkId}
    intent: Delete a check
    question: How do I remove a data quality check from Soda Cloud?
  phrasing_ops: 2
  slug: soda-data-checks-api
- baseURL: https://cloud.soda.io
  baseurl_source: declared
  description: The Contracts surface of the Soda Cloud v4 API — 10 operation(s) across 8 path(s).
  name: Soda Contracts API
  phrasing_intents:
  - id: GET/api/v1/contracts
    intent: List data contracts
    question: Which datasets in my organization already have data contracts?
  - id: POST/api/v1/contracts
    intent: Create a contract on a dataset
    question: How do I start a new data contract for a dataset that has none?
  - id: POST/api/v1/contracts/actions/createSkeleton
    intent: Generate a skeleton contract from schema
    question: Can Soda draft a basic contract from a dataset's schema for me?
  - id: GET/api/v1/contracts/actions/createSkeleton/{operationId}
    intent: Check skeleton contract generation status
    question: Is my skeleton contract generation finished yet?
  - id: POST/api/v1/contracts/actions/generate
    intent: Generate contracts with AI
    question: Can Soda use AI to write contracts for several datasets at once?
  - id: GET/api/v1/contracts/actions/generate/{operationId}
    intent: Check AI contract generation status
    question: Has the AI finished generating contracts for my datasets?
  - id: GET/api/v1/contracts/{contractId}
    intent: Get a contract and its YAML
    question: How do I read the current YAML of a specific data contract?
  - id: POST/api/v1/contracts/{contractId}
    intent: Publish new YAML for a contract
    question: How do I publish an updated version of an existing contract's YAML?
  phrasing_ops: 10
  slug: soda-data-contracts-api
- baseURL: https://cloud.soda.io
  baseurl_source: declared
  description: The Data Standards surface of the Soda Cloud v4 API — 13 operation(s) across 10 path(s).
  name: Soda Data Standards API
  phrasing_intents:
  - id: GET/api/v1/dataStandards
    intent: List data standards
    question: Which data standards are defined in my organization?
  - id: POST/api/v1/dataStandards
    intent: Create a data standard
    question: How do I define a new data standard that applies checks across many datasets?
  - id: POST/api/v1/dataStandards/actions/execute
    intent: Run a dataset's active data standards
    question: Can I trigger a scan of all active data standards linked to one dataset?
  - id: POST/api/v1/dataStandards/actions/previewScope
    intent: Preview datasets matching a scope
    question: Which datasets would a draft data standard scope match before I save it?
  - id: POST/api/v1/dataStandards/actions/test
    intent: Test an unsaved data standard on a dataset
    question: Can I dry-run a draft data standard against one dataset's live data?
  - id: GET/api/v1/dataStandards/activity
    intent: Get organization data standards activity
    question: How many data standards are active and how many datasets do they cover?
  - id: GET/api/v1/dataStandards/{dataStandardId}
    intent: Get a data standard
    question: What YAML and scope does a specific data standard use?
  - id: POST/api/v1/dataStandards/{dataStandardId}
    intent: Replace a data standard's definition
    question: How do I change the YAML or owners of an existing data standard?
  phrasing_ops: 13
  slug: soda-data-data-standards-api
- baseURL: https://cloud.soda.io
  baseurl_source: declared
  description: The Datasets surface of the Soda Cloud v4 API — 24 operation(s) across 17 path(s).
  name: Soda Datasets API
  phrasing_intents:
  - id: GET/api/v1/datasets
    intent: List datasets
    question: Which datasets does my Soda Cloud account monitor, and what is their health?
  - id: GET/api/v1/datasets/byDatasetQualifiedName/{datasetQualifiedName}
    intent: Get a dataset by qualified name
    question: Can I look up a dataset by its fully qualified name rather than its ID?
  - id: GET/api/v1/datasets/roles
    intent: List dataset roles
    question: What dataset-level roles are available for granting access?
  - id: POST/api/v1/datasets/roles
    intent: Create a custom dataset role
    question: How do I create a dataset role that can manage checks but not delete datasets?
  - id: POST/api/v1/datasets/roles/{roleId}
    intent: Update a dataset role
    question: Can I change the permissions of an existing dataset role?
  - id: DELETE/api/v1/datasets/roles/{roleId}
    intent: Delete a dataset role
    question: How do I remove a custom dataset role?
  - id: GET/api/v1/datasets/{datasetId}
    intent: Get a dataset by ID
    question: What are the details of one dataset in Soda Cloud?
  - id: POST/api/v1/datasets/{datasetId}
    intent: Update dataset properties
    question: How do I change a dataset's owners, label or tags?
  phrasing_ops: 24
  slug: soda-data-datasets-api
- baseURL: https://cloud.soda.io
  baseurl_source: declared
  description: The Discovered Datasets surface of the Soda Cloud v4 API — 1 operation(s) across 1 path(s).
  name: Soda Discovered Datasets API
  phrasing_intents:
  - id: GET/api/v1/discoveredDatasets
    intent: List discovered datasets
    question: Which tables has Soda discovered that are not onboarded yet?
  phrasing_ops: 1
  slug: soda-data-discovered-datasets-api
- baseURL: https://cloud.soda.io
  baseurl_source: declared
  description: The Incidents surface of the Soda Cloud v4 API — 5 operation(s) across 3 path(s).
  name: Soda Incidents API
  phrasing_intents:
  - id: GET/api/v1/incidents
    intent: List data quality incidents
    question: Which data quality incidents are open right now?
  - id: POST/api/v1/incidents
    intent: Open an incident
    question: How do I raise an incident from failing monitor results?
  - id: POST/api/v1/incidents/{incidentId}
    intent: Update an incident
    question: How do I mark an existing incident as resolved with notes?
  - id: GET/api/v1/incidents/{incidentId}/rcaReport
    intent: Get an incident's root cause analysis
    question: What was the root cause of this data incident?
  - id: POST/api/v1/incidents/{incidentId}/rcaReport
    intent: Publish a root cause analysis report
    question: Can an agent attach a root cause analysis to an incident?
  phrasing_ops: 5
  slug: soda-data-incidents-api
- baseURL: https://cloud.soda.io
  baseurl_source: declared
  description: The Licensing surface of the Soda Cloud v4 API — 1 operation(s) across 1 path(s).
  name: Soda Licensing API
  phrasing_intents:
  - id: GET/api/v1/licensing/spuConsumption
    intent: Get SPU consumption
    question: How many SPUs has my organization used this month?
  phrasing_ops: 1
  slug: soda-data-licensing-api
- baseURL: https://cloud.soda.io
  baseurl_source: declared
  description: The Notification Rules surface of the Soda Cloud v4 API — 4 operation(s) across 2 path(s).
  name: Soda Notification Rules API
  phrasing_intents:
  - id: GET/api/v1/notificationRules
    intent: List notification rules
    question: Which notification rules decide who gets alerted about failing checks?
  - id: POST/api/v1/notificationRules
    intent: Create a notification rule
    question: How do I alert a user group when checks with a certain attribute fail?
  - id: POST/api/v1/notificationRules/{notificationRuleId}
    intent: Replace a notification rule
    question: Can I change who an existing notification rule alerts?
  - id: DELETE/api/v1/notificationRules/{notificationRuleId}
    intent: Delete a notification rule
    question: How do I stop an alert rule from sending notifications permanently?
  phrasing_ops: 4
  slug: soda-data-notification-rules-api
- baseURL: https://cloud.soda.io
  baseurl_source: declared
  description: The Runners surface of the Soda Cloud v4 API — 4 operation(s) across 2 path(s).
  name: Soda Runners API
  phrasing_intents:
  - id: GET/api/v1/runners
    intent: List runners
    question: Which Soda runners are registered in my organization?
  - id: POST/api/v1/runners
    intent: Create a self-hosted runner
    question: How do I get API credentials to deploy a new self-hosted runner?
  - id: GET/api/v1/runners/{runnerId}
    intent: Get a runner
    question: What is the status and configuration of a specific runner?
  - id: DELETE/api/v1/runners/{runnerId}
    intent: Delete a self-hosted runner
    question: How do I decommission a self-hosted runner?
  phrasing_ops: 4
  slug: soda-data-runners-api
- baseURL: https://cloud.soda.io
  baseurl_source: declared
  description: The Scans surface of the Soda Cloud v4 API — 3 operation(s) across 2 path(s).
  name: Soda Scans API
  phrasing_intents:
  - id: GET/api/v1/scans/{scanId}
    intent: Get scan status
    question: Is my data quality scan still running or has it finished?
  - id: DELETE/api/v1/scans/{scanId}
    intent: Cancel a scan
    question: Can I cancel a scan that is pending or already submitted?
  - id: GET/api/v1/scans/{scanId}/logs
    intent: Get scan logs
    question: Where can I read the logs of a finished scan to debug a failure?
  phrasing_ops: 3
  slug: soda-data-scans-api
- baseURL: https://cloud.soda.io
  baseurl_source: declared
  description: The Secrets surface of the Soda Cloud v4 API — 5 operation(s) across 3 path(s).
  name: Soda Secrets API
  phrasing_intents:
  - id: GET/api/v1/secrets
    intent: List secrets
    question: Which stored secrets can my data source configurations reference?
  - id: POST/api/v1/secrets
    intent: Create a secret
    question: How do I store a database password so it stays out of plain-text data source config?
  - id: POST/api/v1/secrets/{secretId}
    intent: Rotate a secret's value
    question: Can I rotate the value of an existing secret without renaming it?
  - id: DELETE/api/v1/secrets/{secretId}
    intent: Delete a secret
    question: How do I delete a stored secret?
  - id: GET/api/v1/secretsPublicKey
    intent: Get the public key for encrypting secrets
    question: Which public key should I use to encrypt a secret client-side?
  phrasing_ops: 5
  slug: soda-data-secrets-api
- baseURL: https://cloud.soda.io
  baseurl_source: declared
  description: The Users surface of the Soda Cloud v4 API — 8 operation(s) across 4 path(s).
  name: Soda Users API
  phrasing_intents:
  - id: GET/api/v1/userGroups
    intent: List user groups
    question: Which user groups exist and who belongs to each?
  - id: POST/api/v1/userGroups
    intent: Create a user group
    question: How do I create a team group and add members to it?
  - id: GET/api/v1/userGroups/{userGroupId}
    intent: Get a user group
    question: Who are the members of a specific user group?
  - id: POST/api/v1/userGroups/{userGroupId}
    intent: Update user group members
    question: How do I change the membership of an existing user group?
  - id: DELETE/api/v1/userGroups/{userGroupId}
    intent: Delete a user group
    question: How do I remove a user group I no longer need?
  - id: GET/api/v1/users
    intent: List users
    question: Who has access to my organization's Soda Cloud account?
  - id: POST/api/v1/users
    intent: Invite users by email
    question: How do I invite teammates to join my organization?
  - id: POST/api/v1/users/{userId}/disable
    intent: Disable a user
    question: Can I deactivate someone's membership without deleting their account?
  phrasing_ops: 8
  slug: soda-data-users-api
- baseURL: https://cloud.soda.io
  baseurl_source: declared
  description: The Utility surface of the Soda Cloud v4 API — 1 operation(s) across 1 path(s).
  name: Soda Utility API
  phrasing_intents:
  - id: GET/api/v1/test-login
    intent: Test API credentials
    question: Are my Soda Cloud API keys working?
  phrasing_ops: 1
  slug: soda-data-utility-api
- baseURL: https://cloud.soda.io
  baseurl_source: declared
  description: Soda Cloud API Datasource Endpoints
  name: Soda Data Sources API
  phrasing_intents:
  - id: GET/api/v1/datasources
    intent: List data sources
    question: Which data sources are connected to my organization?
  - id: POST/api/v1/datasources
    intent: Create a data source
    question: How do I connect a new data source from a YAML configuration?
  - id: POST/api/v1/datasources/actions/testConnection
    intent: Test a data source connection
    question: Can I check that a data source configuration connects before saving it?
  - id: GET/api/v1/datasources/actions/testConnection/{operationId}
    intent: Check connection test result
    question: Did my data source connection test succeed?
  - id: GET/api/v1/datasources/roles
    intent: List data source roles
    question: What data source-level roles can I assign?
  - id: POST/api/v1/datasources/roles
    intent: Create a custom data source role
    question: Can I create a data source role that lets people create datasets?
  - id: POST/api/v1/datasources/roles/{roleId}
    intent: Update a data source role
    question: Can I change what an existing data source role is allowed to do?
  - id: DELETE/api/v1/datasources/roles/{roleId}
    intent: Delete a data source role
    question: How do I remove a custom data source role?
  phrasing_ops: 18
  slug: soda-data-data-sources-api
artifact_total: 35
asyncapis:
- description: ''
  name: Soda Data Webhooks
  slug: soda-data-webhooks
collections:
- collection_type: open
  name: Soda Cloud REST Attributes API
  slug: open-soda-data-attributes-api
- collection_type: open
  name: Soda Cloud REST Attributes Authentication API
  slug: open-soda-data-authentication-api
- collection_type: open
  name: Soda Cloud REST Attributes Checks API
  slug: open-soda-data-checks-api
- collection_type: open
  name: Soda Cloud REST Attributes Contracts API
  slug: open-soda-data-contracts-api
- collection_type: open
  name: Soda Cloud REST Attributes Datasets API
  slug: open-soda-data-datasets-api
- collection_type: open
  name: Soda Cloud REST API
  slug: open-soda-data
common:
- group: commercial
  href: https://artifacts.apis.io/soda-data/finops/soda-data-finops.yml
  title: ''
  type: FinOps
  url: finops/soda-data-finops.yml
- group: other
  href: https://artifacts.apis.io/soda-data/capabilities/soda-data-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/soda-data-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/soda-data/overlays/soda-data-datasources-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/soda-data-datasources-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.soda.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.soda.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.soda.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.soda.io/reference/soda-apis/rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.soda.io/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.soda.io/soda-documentation/soda-v3/learning-resources/support
- group: company
  title: ''
  type: Blog
  url: https://www.soda.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sodadata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sodadata
- group: commercial
  title: ''
  type: Pricing
  url: https://www.soda.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.soda.io/request-free
- group: start
  title: ''
  type: Login
  url: https://cloud.soda.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.soda.io/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.soda.io/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.soda.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.soda.io/release-notes
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.soda.io/llms.txt
- group: agent
  href: https://artifacts.apis.io/soda-data/agentic-access/soda-data-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/soda-data-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/soda-data/authentication/soda-data-authentication.yml
  title: ''
  type: Authentication
  url: authentication/soda-data-authentication.yml
- group: design
  href: https://artifacts.apis.io/soda-data/conventions/soda-data-conventions.yml
  title: ''
  type: Conventions
  url: conventions/soda-data-conventions.yml
- group: design
  href: https://artifacts.apis.io/soda-data/errors/soda-data-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/soda-data-problem-types.yml
- group: design
  href: https://artifacts.apis.io/soda-data/lifecycle/soda-data-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/soda-data-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/soda-data/conformance/soda-data-conformance.yml
  title: ''
  type: Conformance
  url: conformance/soda-data-conformance.yml
- group: auth
  href: https://artifacts.apis.io/soda-data/security/soda-data-trust-center.yml
  title: ''
  type: Compliance
  url: security/soda-data-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/soda-data/security/soda-data-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/soda-data-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/soda-data/security/soda-data-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/soda-data-domain-security.yml
- group: design
  href: https://artifacts.apis.io/soda-data/data-model/soda-data-data-model.yml
  title: ''
  type: DataModel
  url: data-model/soda-data-data-model.yml
- group: build
  href: https://artifacts.apis.io/soda-data/packages/soda-data-packages.yml
  title: ''
  type: Packages
  url: packages/soda-data-packages.yml
- group: build
  href: https://artifacts.apis.io/soda-data/packages/soda-data-packages.yml
  title: ''
  type: SDKs
  url: packages/soda-data-packages.yml
- group: build
  href: https://artifacts.apis.io/soda-data/cli/soda-data-cli.yml
  title: ''
  type: CLI
  url: cli/soda-data-cli.yml
- group: agent
  href: https://artifacts.apis.io/soda-data/mcp/soda-data-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/soda-data-mcp.yml
- group: build
  href: https://artifacts.apis.io/soda-data/mcp/soda-data-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/soda-data-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/soda-data/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/soda-data/asyncapi/soda-data-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/soda-data-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/soda-data/rate-limits/soda-data-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/soda-data-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/soda-data/plans/soda-data-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/soda-data-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/soda-data/changelog/soda-data-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/soda-data-changelog.yml
- group: agent
  href: https://artifacts.apis.io/soda-data/llms/soda-data-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/soda-data-llms.txt
created: '2026-03-27'
description: Soda is a data quality and data observability platform for the modern data stack. Its core abstraction is the data contract — a declarative YAML source of truth that defines the checks a dataset must pass — extended by organization-wide data standards, ML-based metric monitors for anomaly detection, record-level diagnostics, lineage and impact analysis, and AI-assisted contract generation (Contract Autopilot and Copilot). Soda ships an open-source engine (Soda Core), a Go CLI for the whole platform (sodacli), a 103-operation Soda Cloud v4 REST API, a webhook event surface, and a first-party MCP server that exposes 78 tools so agents can manage data quality directly. Soda Data Inc. is headquartered in Belgium.
finops:
- has_sources: true
  method: derived
  name: Soda Data Finops
  primary_unit: subscription
  service_category: ''
  slug: soda-data-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/soda-data.png
layout: provider
mcp_servers:
- description: soda-mcp is Soda's first-party Model Context Protocol server for Soda Cloud. It runs as a LOCAL stdio process started by the MCP client (Claude Code, Cursor, Codex, GitHub Copilot), authenticates to S
  name: Soda MCP Server
  slug: soda-mcp
modified: '2026-08-29'
name: Soda
nav: Providers
network: true
overview: 'Soda publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Attributes API, Checks API, Contracts API, and 12 more. Tagged areas include AIOps, Data Quality, Data Observability, Data Contracts, and Data Governance.


  The Soda catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Soda''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 34 more developer resources.'
plans:
- name: Soda Data Plans Pricing
  plan_count: 3
  slug: soda-data-plans-pricing
- name: Soda Data Price Estimates
  plan_count: 0
  slug: soda-data-price-estimates
random_paper: 14
rate_limits:
- limit_count: 6
  name: Soda Data Rate Limits
  slug: soda-data-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Soda API Rules
  rule_count: 60
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 7
  slug: soda-data-rules
score:
  band: exemplar
  composite: 73.6
  coverage:
    artifact_dirs: 31
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 63.4
    developer_ergonomics: 73.2
    discoverability: 71.7
    operational_transparency: 73.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - belgium
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 73.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/soda-data/soda-data-2026-06-20T194129.png
security:
- kind: authentication
  name: Soda Data Authentication
  slug: soda-data-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Soda Data Domain Security
  slug: soda-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Soda Data Trust Center
  slug: soda-data-trust-center
  summary_line: SOC 2, GDPR
skill_count: 3
skills:
- name: soda-contract-lifecycle
  slug: soda-data-contract-lifecycle
- name: soda-onboard-datasource
  slug: soda-data-onboard-datasource
- name: soda-triage-failing-checks
  slug: soda-data-triage-failing-checks
slug: soda-data
tags:
- AIOps
- Data Quality
- Data Observability
- Data Contracts
- Data Governance
- Anomaly Detection
- Data Monitoring
- Data Testing
website: https://www.soda.io
---
