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
- acting_count: 27
  human_in_the_loop: 0
  name: Shuffle Agentic Access
  operation_count: 47
  slug: shuffle-agentic-access
  summary_line: 47 operations · 27 acting
api_count: 9
apis:
- description: The Administration API from Shuffle — 1 operation(s) for administration.
  name: Shuffle Administration API
  slug: shuffle-administration-api
- description: The Apps API from Shuffle — 8 operation(s) for apps.
  name: Shuffle Apps API
  slug: shuffle-apps-api
- description: The Datastore API from Shuffle — 4 operation(s) for datastore.
  name: Shuffle Datastore API
  slug: shuffle-datastore-api
- description: The Files API from Shuffle — 5 operation(s) for files.
  name: Shuffle Files API
  slug: shuffle-files-api
- description: The Notifications API from Shuffle — 3 operation(s) for notifications.
  name: Shuffle Notifications API
  slug: shuffle-notifications-api
- description: The Organizations API from Shuffle — 3 operation(s) for organizations.
  name: Shuffle Organizations API
  slug: shuffle-organizations-api
- description: The Triggers API from Shuffle — 2 operation(s) for triggers.
  name: Shuffle Triggers API
  slug: shuffle-triggers-api
- description: The Users API from Shuffle — 5 operation(s) for users.
  name: Shuffle Users API
  slug: shuffle-users-api
- description: The Workflows API from Shuffle — 9 operation(s) for workflows.
  name: Shuffle Workflows API
  slug: shuffle-workflows-api
artifact_total: 25
collections:
- collection_type: open
  name: Shuffle API
  slug: open-shuffle
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shuffle-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/shuffle-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shuffle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shuffle-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shuffleeditor
- group: agent
  title: ''
  type: LlmsText
  url: https://shuffler.io/llms.txt
created: '2026-05-02'
description: Shuffle is an open source security automation platform (SOAR) built for and by security professionals. The platform enables security teams to orchestrate workflows across their entire security tool stack using a no-code/low-code interface powered by OpenAPI integrations. Shuffle provides workflow automation, app integration, webhook triggers, scheduled executions, file storage, and organization management via a comprehensive REST API. It follows the Unix philosophy of doing one thing well — connecting security tools through REST APIs.
examples:
- key_count: 4
  name: Shuffle Create Workflow Example
  slug: shuffle-create-workflow-example
- key_count: 4
  name: Shuffle Execute Workflow Example
  slug: shuffle-execute-workflow-example
finops:
- name: Shuffle Finops
  service_category: API
  slug: shuffle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shuffle.png
json_schemas:
- name: Shuffle Workflow Execution
  property_count: 9
  slug: shuffle-execution
- name: Shuffle Workflow
  property_count: 12
  slug: shuffle-workflow
json_structures:
- name: Shuffle Workflow Structure
  property_count: 0
  slug: shuffle-workflow-structure
jsonld:
- class_count: 13
  name: Shuffle Context
  property_count: 18
  slug: shuffle-context
layout: provider
modified: '2026-05-19'
name: Shuffle
nav: Providers
network: true
overview: 'Shuffle publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Administration API, Apps API, Datastore API, and 6 more. Tagged areas include Security, Workflows, Automation, SOAR, and Orchestration.


  The Shuffle catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Shuffle''s developer surface includes authentication and 5 more developer resources.'
plans:
- name: Shuffle Plans Pricing
  plan_count: 3
  slug: shuffle-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 5
  name: Shuffle Rate Limits
  slug: shuffle-rate-limits
rules:
- name: Shuffle API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: shuffle-jsonschema-spectral-rules
- name: Shuffle API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 4
  slug: shuffle-rules
score:
  band: developing
  composite: 47.7
  delta: -4.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 76.3
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 51.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shuffle/refs/heads/main/screenshots/shuffle-2026-06-20T193850.png
security:
- kind: authentication
  name: Shuffle Authentication
  slug: shuffle-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Shuffle Domain Security
  slug: shuffle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Shuffle Vulnerability Disclosure
  slug: shuffle-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: shuffle
tags:
- Security
- Workflows
- Automation
- SOAR
- Orchestration
- Open Source
---
