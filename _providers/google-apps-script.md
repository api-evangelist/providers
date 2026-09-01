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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Google Apps Script Agentic Access
  operation_count: 16
  slug: google-apps-script-agentic-access
  summary_line: 16 operations · 7 acting
api_count: 1
apis:
- description: The Processes API from Google Apps Script — 1 operation(s) for processes.
  name: Google Apps Script Processes API
  slug: google-apps-script-processes-api
- description: The processes:listScriptProcesses API from Google Apps Script — 1 operation(s) for processes:listscriptprocesses.
  name: Google Apps Script processes:listScriptProcesses API
  slug: google-apps-script-processes-listscriptprocesses-api
- description: The Projects API from Google Apps Script — 8 operation(s) for projects.
  name: Google Apps Script Projects API
  slug: google-apps-script-projects-api
- description: The Scripts API from Google Apps Script — 1 operation(s) for scripts.
  name: Google Apps Script Scripts API
  slug: google-apps-script-scripts-api
artifact_total: 80
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Apps Script Processes API
  slug: open-google-apps-script-processes-api
- collection_type: open
  name: Google Apps Script Processes processes:listScriptProcesses API
  slug: open-google-apps-script-processes-listscriptprocesses-api
- collection_type: open
  name: Google Apps Script Processes Projects API
  slug: open-google-apps-script-projects-api
- collection_type: open
  name: Google Apps Script Processes Scripts API
  slug: open-google-apps-script-scripts-api
- collection_type: open
  name: Google Apps Script API
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-apps-script-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-apps-script-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-apps-script-domain-security.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/apps-script/api/concepts
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.google.com/apps-script/guides/services/quotas
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.jsonld
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleworkspace
- group: build
  title: ''
  type: SDKs
  url: https://developers.google.com/apps-script/api/quickstart/nodejs
- group: build
  title: ''
  type: CLI
  url: https://developers.google.com/apps-script/guides/clasp
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/apps-script/reference
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/apps-script/support
- group: company
  title: ''
  type: Blog
  url: https://developers.google.com/apps-script/updates
- group: design
  title: ''
  type: Rules
  url: rules/google-apps-script-spectral-rules.yml
created: '2026-03-13'
description: The Apps Script API provides programmatic access to manage Google Apps Script projects, deployments, and executions. It enables creating and updating script projects, managing project versions and deployments, monitoring script processes, and remotely executing Apps Script functions. The API is essential for automating Apps Script project management and integrating script execution into external applications.
examples:
- key_count: 2
  name: Openapi Content Example
  slug: openapi-content-example
- key_count: 2
  name: Openapi Create Project Request Example
  slug: openapi-create-project-request-example
- key_count: 4
  name: Openapi Deployment Config Example
  slug: openapi-deployment-config-example
- key_count: 2
  name: Openapi Deployment Example
  slug: openapi-deployment-example
- key_count: 4
  name: Openapi Execution Request Example
  slug: openapi-execution-request-example
- key_count: 5
  name: Openapi File Example
  slug: openapi-file-example
- key_count: 2
  name: Openapi List Deployments Response Example
  slug: openapi-list-deployments-response-example
- key_count: 2
  name: Openapi List Processes Response Example
  slug: openapi-list-processes-response-example
- key_count: 2
  name: Openapi List Versions Response Example
  slug: openapi-list-versions-response-example
- key_count: 3
  name: Openapi Metrics Example
  slug: openapi-metrics-example
- key_count: 3
  name: Openapi Operation Example
  slug: openapi-operation-example
- key_count: 6
  name: Openapi Process Example
  slug: openapi-process-example
- key_count: 6
  name: Openapi Project Example
  slug: openapi-project-example
- key_count: 0
  name: Openapi Update Deployment Request Example
  slug: openapi-update-deployment-request-example
- key_count: 4
  name: Openapi Version Example
  slug: openapi-version-example
features:
- Create and manage Apps Script projects programmatically
- Deploy script projects as web apps, add-ons, and API executables
- Remotely execute Apps Script functions from external applications
- Monitor script execution processes and metrics
- Version management with immutable snapshots of script code
finops:
- name: Google Apps Script Finops
  service_category: API
  slug: google-apps-script-finops
image: /assets/icons/google-apps-script.png
integrations:
- Google Workspace apps including Sheets, Docs, Slides, Gmail, and Calendar
- Google Cloud Platform services for extended functionality
- External REST APIs via Apps Script UrlFetchApp service
- Google Drive for document and file management automation
- clasp CLI for local development and version control workflows
json_schemas:
- name: Content
  property_count: 2
  slug: openapi-content
- name: CreateProjectRequest
  property_count: 2
  slug: openapi-create-project-request
- name: DeploymentConfig
  property_count: 4
  slug: openapi-deployment-config
- name: Deployment
  property_count: 2
  slug: openapi-deployment
- name: ExecutionRequest
  property_count: 4
  slug: openapi-execution-request
- name: File
  property_count: 5
  slug: openapi-file
- name: ListDeploymentsResponse
  property_count: 2
  slug: openapi-list-deployments-response
- name: ListProcessesResponse
  property_count: 2
  slug: openapi-list-processes-response
- name: ListVersionsResponse
  property_count: 2
  slug: openapi-list-versions-response
- name: Metrics
  property_count: 3
  slug: openapi-metrics
- name: Operation
  property_count: 3
  slug: openapi-operation
- name: Process
  property_count: 6
  slug: openapi-process
- name: Project
  property_count: 6
  slug: openapi-project
- name: UpdateDeploymentRequest
  property_count: 0
  slug: openapi-update-deployment-request
- name: Version
  property_count: 4
  slug: openapi-version
json_structures:
- name: Openapi Content Structure
  property_count: 2
  slug: openapi-content-structure
- name: Openapi Create Project Request Structure
  property_count: 2
  slug: openapi-create-project-request-structure
- name: Openapi Deployment Config Structure
  property_count: 4
  slug: openapi-deployment-config-structure
- name: Openapi Deployment Structure
  property_count: 2
  slug: openapi-deployment-structure
- name: Openapi Execution Request Structure
  property_count: 4
  slug: openapi-execution-request-structure
- name: Openapi File Structure
  property_count: 5
  slug: openapi-file-structure
- name: Openapi List Deployments Response Structure
  property_count: 2
  slug: openapi-list-deployments-response-structure
- name: Openapi List Processes Response Structure
  property_count: 2
  slug: openapi-list-processes-response-structure
- name: Openapi List Versions Response Structure
  property_count: 2
  slug: openapi-list-versions-response-structure
- name: Openapi Metrics Structure
  property_count: 3
  slug: openapi-metrics-structure
- name: Openapi Operation Structure
  property_count: 3
  slug: openapi-operation-structure
- name: Openapi Process Structure
  property_count: 6
  slug: openapi-process-structure
- name: Openapi Project Structure
  property_count: 6
  slug: openapi-project-structure
- name: Openapi Update Deployment Request Structure
  property_count: 0
  slug: openapi-update-deployment-request-structure
- name: Openapi Version Structure
  property_count: 4
  slug: openapi-version-structure
jsonld:
- class_count: 4
  name: Json Ld Context
  property_count: 5
  slug: json-ld
- class_count: 0
  name: Openapi Context
  property_count: 0
  slug: openapi-context
layout: provider
modified: '2026-05-19'
name: Google Apps Script
nav: Providers
network: true
overview: 'Google Apps Script publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Processes API, processes:listScriptProcesses API, Projects API, and 1 more. Tagged areas include Apps Script, Automation, Deployment, Google, and Google Workspace.


  The Google Apps Script catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Google Apps Script''s developer surface includes getting-started guide, pricing, CLI, documentation, support, engineering blog, and 7 more developer resources.'
plans:
- name: Google Apps Script Plans Pricing
  plan_count: 3
  slug: google-apps-script-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Google Apps Script Rate Limits
  slug: google-apps-script-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Google Apps Script API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-apps-script-jsonschema-spectral-rules
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: Google Apps Script API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 5
  slug: google-apps-script-spectral-rules
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 60.4
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-apps-script/refs/heads/main/screenshots/google-apps-script-2026-06-20T182017.png
security:
- kind: domain-security
  name: Google Apps Script Domain Security
  slug: google-apps-script-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Apps Script Vulnerability Disclosure
  slug: google-apps-script-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-apps-script
tags:
- Apps Script
- Automation
- Deployment
- Google
- Google Workspace
- Scripting
use_cases:
- Automating Google Workspace workflows across Sheets, Docs, and Gmail
- Building custom add-ons and integrations for Google Workspace
- Managing script deployments across development and production environments
- Monitoring script execution health and performance metrics
- Integrating Apps Script automation into CI/CD pipelines
---
