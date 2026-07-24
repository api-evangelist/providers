---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 22
  human_in_the_loop: 1
  name: Robocorp Agentic Access
  operation_count: 44
  slug: robocorp-agentic-access
  summary_line: 44 operations · 22 acting · 1 human-in-the-loop
api_count: 13
apis:
- description: The RPA Framework is an open-source collection of Python libraries for robotic process automation designed for use with Robot Framework and Python. It includes libraries for browser automation, deskto
  name: RPA Framework
  slug: rpa-framework
- description: Asset storage management
  name: Robocorp Assets API
  slug: robocorp-assets-api
- description: AI assistant management
  name: Robocorp Assistants API
  slug: robocorp-assistants-api
- description: Process execution and monitoring
  name: Robocorp Process Runs API
  slug: robocorp-process-runs-api
- description: Process definition and management
  name: Robocorp Processes API
  slug: robocorp-processes-api
- description: Individual step execution details
  name: Robocorp Step Runs API
  slug: robocorp-step-runs-api
- description: Task package deployment
  name: Robocorp Task Packages API
  slug: robocorp-task-packages-api
- description: Secret management
  name: Robocorp Vault API
  slug: robocorp-vault-api
- description: Webhook configuration
  name: Robocorp Webhooks API
  slug: robocorp-webhooks-api
- description: Work item queue management
  name: Robocorp Work Items API
  slug: robocorp-work-items-api
- description: Worker group organization
  name: Robocorp Worker Groups API
  slug: robocorp-worker-groups-api
- description: Worker agent management
  name: Robocorp Workers API
  slug: robocorp-workers-api
- description: Workspace information
  name: Robocorp Workspace API
  slug: robocorp-workspace-api
artifact_total: 28
collections:
- collection_type: open
  name: Robocorp Control Room API
  slug: open-robocorp-control-room
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/robocorp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/robocorp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/robocorp-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/robocorp
- group: company
  title: ''
  type: Website
  url: https://robocorp.com
- group: docs
  title: ''
  type: Documentation
  url: https://robocorp.com/docs
- group: build
  title: ''
  type: GitHub
  url: https://github.com/robocorp
- group: other
  title: ''
  type: PyPI
  url: https://pypi.org/project/robocorp/
- group: company
  title: ''
  type: Blog
  url: https://robocorp.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://robocorp.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://robocorp.com/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.robocorp.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://robocorp.com/docs/changelog
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/robocorp/refs/heads/main/json-ld/robocorp-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/robocorp/refs/heads/main/vocabulary/robocorp-vocabulary.yml
created: '2026-03-27'
description: Robocorp is an open source RPA and workflow automation platform for building Python-based automation bots. The platform provides the Control Room API for managing workspaces, workers, processes, work items, assets, vaults, webhooks, and task packages. Robocorp also provides the RPA Framework, an open-source collection of Python libraries for robotic process automation including browser, desktop, email, Excel, PDF, and cloud service automation. The platform has evolved toward Sema4 AI for AI-powered automation actions.
examples:
- key_count: 2
  name: Robocorp Create Work Item Example
  slug: robocorp-create-work-item-example
- key_count: 2
  name: Robocorp Start Process Run Example
  slug: robocorp-start-process-run-example
finops:
- name: Robocorp Finops
  service_category: API
  slug: robocorp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/robocorp.png
json_schemas:
- name: Robocorp Process
  property_count: 7
  slug: robocorp-process
- name: Robocorp Work Item
  property_count: 7
  slug: robocorp-work-item
json_structures:
- name: Robocorp Process Structure
  property_count: 0
  slug: robocorp-process-structure
jsonld:
- class_count: 34
  name: Robocorp Context
  property_count: 0
  slug: robocorp-context
layout: provider
modified: '2026-05-19'
name: Robocorp
nav: Providers
network: true
overview: 'Robocorp publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Assistants API, Process Runs API, and 9 more. Tagged areas include RPA, Workflow Automation, Python, Open Source, and Automation.


  The Robocorp catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Robocorp''s developer surface includes authentication, documentation, GitHub presence, engineering blog, changelog, and 10 more developer resources.'
plans:
- name: Robocorp Plans Pricing
  plan_count: 3
  slug: robocorp-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Robocorp Rate Limits
  slug: robocorp-rate-limits
rules:
- name: Robocorp API Rules
  rule_count: 13
  severity_counts:
    error: 2
    hint: 0
    info: 4
    warn: 7
  slug: robocorp-control-room-rules
- name: Robocorp API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: robocorp-jsonschema-spectral-rules
score:
  band: developing
  composite: 57.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 65.5
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 68.4
  previous_composite: 57.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/robocorp/refs/heads/main/screenshots/robocorp-2026-06-20T193143.png
security:
- kind: authentication
  name: Robocorp Authentication
  slug: robocorp-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Robocorp Domain Security
  slug: robocorp-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: robocorp
tags:
- RPA
- Workflow Automation
- Python
- Open Source
- Automation
website: https://robocorp.com
---
