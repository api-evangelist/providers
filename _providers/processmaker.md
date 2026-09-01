---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Processmaker Agentic Access
  operation_count: 64
  slug: processmaker-agentic-access
  summary_line: 64 operations · 38 acting
api_count: 1
apis:
- description: Environment variable management
  name: ProcessMaker Environment Variables API
  slug: processmaker-environment-variables-api
- description: File and media management
  name: ProcessMaker Files API
  slug: processmaker-files-api
- description: Group and membership management
  name: ProcessMaker Groups API
  slug: processmaker-groups-api
- description: Notification management
  name: ProcessMaker Notifications API
  slug: processmaker-notifications-api
- description: BPMN 2.0 process design and management
  name: ProcessMaker Processes API
  slug: processmaker-processes-api
- description: Process request (case) management
  name: ProcessMaker Requests API
  slug: processmaker-requests-api
- description: Form screen design and management
  name: ProcessMaker Screens API
  slug: processmaker-screens-api
- description: System settings management
  name: ProcessMaker Settings API
  slug: processmaker-settings-api
- description: Task and token management
  name: ProcessMaker Tasks API
  slug: processmaker-tasks-api
- description: User account management
  name: ProcessMaker Users API
  slug: processmaker-users-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ProcessMaker Platform RESTful Environment Variables API
  slug: open-processmaker-environment-variables-api
- collection_type: open
  name: ProcessMaker Platform RESTful Environment Variables Files API
  slug: open-processmaker-files-api
- collection_type: open
  name: ProcessMaker Platform RESTful Environment Variables Groups API
  slug: open-processmaker-groups-api
- collection_type: open
  name: ProcessMaker Platform RESTful Environment Variables Notifications API
  slug: open-processmaker-notifications-api
- collection_type: open
  name: ProcessMaker Platform RESTful Environment Variables Processes API
  slug: open-processmaker-processes-api
- collection_type: open
  name: ProcessMaker Platform RESTful Environment Variables Requests API
  slug: open-processmaker-requests-api
- collection_type: open
  name: ProcessMaker Platform RESTful Environment Variables Screens API
  slug: open-processmaker-screens-api
- collection_type: open
  name: ProcessMaker Platform RESTful Environment Variables Settings API
  slug: open-processmaker-settings-api
- collection_type: open
  name: ProcessMaker Platform RESTful Environment Variables Tasks API
  slug: open-processmaker-tasks-api
- collection_type: open
  name: ProcessMaker Platform RESTful Environment Variables Users API
  slug: open-processmaker-users-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/ProcessMaker/processmaker/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/ProcessMaker/processmaker/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/ProcessMaker/processmaker/blob/develop/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/processmaker-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/processmaker-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/processmaker-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.processmaker.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.processmaker.com
- group: docs
  title: ''
  type: Documentation
  url: https://processmaker.gitbook.io/developer-documentation
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ProcessMaker
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/ProcessMaker/processmaker
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/processmaker
- group: other
  title: ''
  type: X
  url: https://twitter.com/processmaker
- group: company
  title: ''
  type: Blog
  url: https://www.processmaker.com/blog/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.processmaker.com/docs/release-notes
- group: operate
  title: ''
  type: Forums
  url: https://forum.processmaker.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.processmaker.com/products/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/processmaker-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/processmaker-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/processmaker-finops.yml
created: '2026-06-13'
description: ProcessMaker is an intelligent BPM and workflow automation platform that provides a REST API for designing processes, managing cases, handling tasks, and integrating with enterprise systems. The platform offers a BPMN 2.0 compliant workflow engine accessible via a RESTful API that is compliant with the OpenAPI specification with documentation auto-generated by Swagger.
examples:
- key_count: 2
  name: Processmaker Complete Task Example
  slug: processmaker-complete-task-example
- key_count: 5
  name: Processmaker Create Process Example
  slug: processmaker-create-process-example
- key_count: 2
  name: Processmaker Start Process Example
  slug: processmaker-start-process-example
finops:
- name: Processmaker Finops
  service_category: ''
  slug: processmaker-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/processmaker.png
json_schemas:
- name: ProcessMaker Process
  property_count: 15
  slug: processmaker-process
- name: ProcessMaker Process Request
  property_count: 11
  slug: processmaker-request
- name: ProcessMaker Task
  property_count: 13
  slug: processmaker-task
jsonld:
- class_count: 14
  name: Processmaker Context
  property_count: 62
  slug: processmaker-context
layout: provider
modified: '2026-06-13'
name: ProcessMaker
nav: Providers
network: true
overview: 'ProcessMaker publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Environment Variables API, Files API, Groups API, and 7 more. Tagged areas include BPM, Business Process Management, Workflow-Automation, BPMN 2.0, and Low-Code.


  The ProcessMaker catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ProcessMaker''s developer surface includes authentication, documentation, engineering blog, release notes, pricing, and 15 more developer resources.'
plans:
- name: Processmaker Plans Pricing
  plan_count: 3
  slug: processmaker-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Processmaker Rate Limits
  slug: processmaker-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: ProcessMaker API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: processmaker-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 48.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 61.5
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 21.1
  open_source:
    applies: true
    score: 25.0
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/processmaker/refs/heads/main/screenshots/processmaker-2026-06-20T192125.png
security:
- kind: authentication
  name: Processmaker Authentication
  slug: processmaker-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Processmaker Domain Security
  slug: processmaker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: processmaker
tags:
- BPM
- Business Process Management
- Workflow-Automation
- BPMN 2.0
- Low-Code
- Intelligent Automation
- Process Design
- Case Management
- Task Management
- Enterprise Integration
website: https://www.processmaker.com
---
