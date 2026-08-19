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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 27
  human_in_the_loop: 1
  name: Tanium Agentic Access
  operation_count: 70
  slug: tanium-agentic-access
  summary_line: 70 operations · 27 acting · 1 human-in-the-loop
api_count: 22
apis:
- description: The Tanium API Gateway is a GraphQL interface for querying data and taking action in Tanium. It is the preferred method for integrating with Tanium, supporting asset queries, endpoint actions, and dat
  name: Tanium API Gateway
  slug: api-gateway
- description: Deploy and manage actions on endpoints
  name: Tanium Actions API
  slug: tanium-actions-api
- description: Manage threat alerts
  name: Tanium Alerts API
  slug: tanium-alerts-api
- description: Session and token management
  name: Tanium Authentication API
  slug: tanium-authentication-api
- description: Manage data delivery connections
  name: Tanium Connections API
  slug: tanium-connections-api
- description: Manage connection destinations
  name: Tanium Destinations API
  slug: tanium-destinations-api
- description: Retrieve Recorder events from endpoints
  name: Tanium Events API
  slug: tanium-events-api
- description: Collect and manage investigation evidence
  name: Tanium Evidence API
  slug: tanium-evidence-api
- description: Download and manage files from endpoints
  name: Tanium File Downloads API
  slug: tanium-file-downloads-api
- description: Browse and manage files on connected endpoints
  name: Tanium File Operations API
  slug: tanium-file-operations-api
- description: Manage computer and action groups
  name: Tanium Groups API
  slug: tanium-groups-api
- description: Manage threat intelligence documents
  name: Tanium Intel Documents API
  slug: tanium-intel-documents-api
- description: Manage classification labels for intel documents
  name: Tanium Labels API
  slug: tanium-labels-api
- description: Manage deployment packages
  name: Tanium Packages API
  slug: tanium-packages-api
- description: Inspect endpoint processes and process trees
  name: Tanium Processes API
  slug: tanium-processes-api
- description: Ask and retrieve questions from endpoints
  name: Tanium Questions API
  slug: tanium-questions-api
- description: Manage saved questions
  name: Tanium Saved Questions API
  slug: tanium-saved-questions-api
- description: Manage connection schedules
  name: Tanium Schedules API
  slug: tanium-schedules-api
- description: Manage endpoint sensors
  name: Tanium Sensors API
  slug: tanium-sensors-api
- description: Capture and manage endpoint memory snapshots
  name: Tanium Snapshots API
  slug: tanium-snapshots-api
- description: Manage connection data sources
  name: Tanium Sources API
  slug: tanium-sources-api
- description: Connect service status and logs
  name: Tanium Status API
  slug: tanium-status-api
arazzos:
- description: Parse question text, ask it across endpoints, poll until answered, then read the result data.
  name: Tanium Ask A Question And Get Results
  slug: tanium-ask-question-get-results-workflow
- description: Confirm a Connect connection by id, then trigger an immediate on-demand execution.
  name: Tanium Connect Run A Connection On Demand
  slug: tanium-connect-run-on-demand-workflow
- description: Resolve a package, action group, and target computer group by name, then create and execute the action.
  name: Tanium Deploy A Package As An Action
  slug: tanium-deploy-package-action-workflow
- description: Open a live connection to an endpoint, poll until connected, then capture a snapshot for offline analysis.
  name: Tanium Threat Response Live Connection And Snapshot
  slug: tanium-live-connection-snapshot-workflow
- description: Resolve a saved question by name, then read its latest endpoint result data.
  name: Tanium Run A Saved Question By Name
  slug: tanium-run-saved-question-workflow
- description: Resolve a sensor by name, ask a question that selects it, poll until answered, then read the result data.
  name: Tanium Ask A Sensor Question And Get Results
  slug: tanium-sensor-question-results-workflow
- description: Resolve a computer group by name, ask a question scoped to it, then read the result data.
  name: Tanium Ask A Question Scoped To A Computer Group
  slug: tanium-target-group-question-workflow
artifact_total: 79
collections:
- collection_type: postman
  name: Tanium Connect API
  slug: postman-tanium-connect-api
- collection_type: postman
  name: Tanium Platform REST API
  slug: postman-tanium-platform-rest-api
- collection_type: postman
  name: Tanium Threat Response API
  slug: postman-tanium-threat-response-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tanium Connect Actions API
  slug: open-tanium-actions-api
- collection_type: open
  name: Tanium Connect Actions Alerts API
  slug: open-tanium-alerts-api
- collection_type: open
  name: Tanium Connect Actions Authentication API
  slug: open-tanium-authentication-api
- collection_type: open
  name: Tanium Connect API
  slug: open-tanium-connect-api
- collection_type: open
  name: Tanium Connect Actions Connections API
  slug: open-tanium-connections-api
- collection_type: open
  name: Tanium Connect Actions Destinations API
  slug: open-tanium-destinations-api
- collection_type: open
  name: Tanium Connect Actions Events API
  slug: open-tanium-events-api
- collection_type: open
  name: Tanium Connect Actions Evidence API
  slug: open-tanium-evidence-api
- collection_type: open
  name: Tanium Connect Actions File Downloads API
  slug: open-tanium-file-downloads-api
- collection_type: open
  name: Tanium Connect Actions File Operations API
  slug: open-tanium-file-operations-api
- collection_type: open
  name: Tanium Connect Actions Groups API
  slug: open-tanium-groups-api
- collection_type: open
  name: Tanium Connect Actions Intel Documents API
  slug: open-tanium-intel-documents-api
- collection_type: open
  name: Tanium Connect Actions Labels API
  slug: open-tanium-labels-api
- collection_type: open
  name: Tanium Connect Actions Packages API
  slug: open-tanium-packages-api
- collection_type: open
  name: Tanium Platform REST API
  slug: open-tanium-platform-rest-api
- collection_type: open
  name: Tanium Connect Actions Processes API
  slug: open-tanium-processes-api
- collection_type: open
  name: Tanium Connect Actions Questions API
  slug: open-tanium-questions-api
- collection_type: open
  name: Tanium Connect Actions Saved Questions API
  slug: open-tanium-saved-questions-api
- collection_type: open
  name: Tanium Connect Actions Schedules API
  slug: open-tanium-schedules-api
- collection_type: open
  name: Tanium Connect Actions Sensors API
  slug: open-tanium-sensors-api
- collection_type: open
  name: Tanium Connect Actions Snapshots API
  slug: open-tanium-snapshots-api
- collection_type: open
  name: Tanium Connect Actions Sources API
  slug: open-tanium-sources-api
- collection_type: open
  name: Tanium Connect Actions Status API
  slug: open-tanium-status-api
- collection_type: open
  name: Tanium Threat Response API
  slug: open-tanium-threat-response-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tanium-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tanium-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tanium-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/tanium/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tanium-ask-question-get-results-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tanium-connect-run-on-demand-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tanium-deploy-package-action-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tanium-live-connection-snapshot-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tanium-run-saved-question-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tanium-sensor-question-results-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tanium-target-group-question-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tanium
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tanium-endpoint-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tanium-question-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tanium-alert-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tanium-sensor-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tanium-package-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tanium-action-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tanium-connection-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/tanium-endpoint-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/tanium-action-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tanium-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/tanium-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tanium-vocabulary.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.tanium.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.tanium.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.tanium.com/apis/api_intro
- group: auth
  title: ''
  type: Authentication
  url: https://docs.tanium.com/platform_user/platform_user/console_api_tokens.html
- group: company
  title: ''
  type: Blog
  url: https://www.tanium.com/p/tanium-blog/
- group: operate
  title: ''
  type: Support
  url: https://community.tanium.com/s/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tanium.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tanium.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tanium
- group: operate
  title: ''
  type: Community
  url: https://community.tanium.com/s/
- group: company
  title: ''
  type: Website
  url: https://www.tanium.com/
- group: start
  title: ''
  type: Login
  url: https://community.tanium.com/s/login/
- group: start
  title: ''
  type: Signup
  url: https://community.tanium.com/CommunitiesSelfReg
- group: build
  title: ''
  type: SDKs
  url: https://tanium.github.io/pytan/
- group: docs
  title: ''
  type: IntegrationGuide
  url: https://developer.tanium.com/guides/core-platform/integration_methods
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.tanium.com/bundle/releasenotes/page/releasenotes/index.html
- group: operate
  title: ''
  type: Contact
  url: https://www.tanium.com/contact/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.tanium.com/llms.txt
created: '2025-02-06'
description: Tanium is a unified endpoint management and security platform that provides real-time visibility and control across all endpoints. It offers a suite of APIs including a GraphQL-based API Gateway and platform REST APIs for integrating with endpoint management, security, compliance, and threat response capabilities.
examples:
- key_count: 2
  name: Tanium Ask Question Example
  slug: tanium-ask-question-example
- key_count: 2
  name: Tanium Create Connection Example
  slug: tanium-create-connection-example
- key_count: 2
  name: Tanium Deploy Action Example
  slug: tanium-deploy-action-example
finops:
- name: Tanium Finops
  service_category: Endpoint Management
  slug: tanium-finops
graphqls:
- description: The Tanium API Gateway is a GraphQL interface for querying data and taking action in Tanium. It is the preferred method for integrating with Tanium, supporting asset queries, endpoint actions, and dat
  name: Tanium GraphQL API
  slug: tanium-graphql
image: https://www.tanium.com/images/tanium-logo.png
json_schemas:
- name: Tanium Action
  property_count: 10
  slug: tanium-action
- name: Tanium Threat Alert
  property_count: 13
  slug: tanium-alert
- name: Tanium Connect Connection
  property_count: 12
  slug: tanium-connection
- name: Tanium Endpoint
  property_count: 21
  slug: tanium-endpoint
- name: Tanium Package
  property_count: 11
  slug: tanium-package
- name: Tanium Question
  property_count: 7
  slug: tanium-question
- name: Tanium Sensor
  property_count: 11
  slug: tanium-sensor
json_structures:
- name: Tanium Action Structure
  property_count: 0
  slug: tanium-action-structure
- name: Tanium Endpoint Structure
  property_count: 0
  slug: tanium-endpoint-structure
jsonld:
- class_count: 3
  name: Tanium Context
  property_count: 13
  slug: tanium-context
layout: provider
modified: '2026-05-19'
name: Tanium
nav: Providers
network: true
overview: 'Tanium publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Alerts API, Authentication API, and 18 more. Tagged areas include Compliance, Endpoint Management, Patch Management, Security, and Threat Detection.


  The Tanium catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tanium''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, support, signup flow, and 35 more developer resources.'
plans:
- name: Tanium Plans Pricing
  plan_count: 1
  slug: tanium-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 1
  name: Tanium Rate Limits
  slug: tanium-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tanium API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tanium-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Tanium API Rules
  rule_count: 8
  severity_counts:
    error: 0
    hint: 2
    info: 1
    warn: 5
  slug: tanium-rules
score:
  band: developing
  composite: 47.2
  delta: -8.7
  facets:
    access_clarity: 40.8
    commercial_clarity: 40.8
    contract_governance: 25.0
    contract_quality: 63.1
    developer_ergonomics: 50.0
    discoverability: 72.2
    governance: 25.0
    operational_transparency: 23.7
  previous_composite: 55.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/tanium/refs/heads/main/screenshots/tanium-2026-06-20T194916.png
security:
- kind: authentication
  name: Tanium Authentication
  slug: tanium-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tanium Domain Security
  slug: tanium-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tanium
tags:
- Compliance
- Endpoint Management
- Patch Management
- Security
- Threat Detection
- Unified Endpoint Management
website: https://www.tanium.com/
---
