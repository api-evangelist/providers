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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Shuffle Agentic Access
  operation_count: 47
  slug: shuffle-agentic-access
  summary_line: 47 operations · 27 acting
api_count: 1
apis:
- baseURL: https://shuffler.io/api/v1
  baseurl_source: declared
  description: The Administration API from Shuffle — 1 operation(s) for administration.
  name: Shuffle Administration API
  slug: shuffle-administration-api
- baseURL: https://shuffler.io/api/v1
  baseurl_source: declared
  description: The Apps API from Shuffle — 8 operation(s) for apps.
  name: Shuffle Apps API
  slug: shuffle-apps-api
- baseURL: https://shuffler.io/api/v1
  baseurl_source: declared
  description: The Datastore API from Shuffle — 4 operation(s) for datastore.
  name: Shuffle Datastore API
  slug: shuffle-datastore-api
- baseURL: https://shuffler.io/api/v1
  baseurl_source: declared
  description: The Files API from Shuffle — 5 operation(s) for files.
  name: Shuffle Files API
  slug: shuffle-files-api
- baseURL: https://shuffler.io/api/v1
  baseurl_source: declared
  description: The Notifications API from Shuffle — 3 operation(s) for notifications.
  name: Shuffle Notifications API
  slug: shuffle-notifications-api
- baseURL: https://shuffler.io/api/v1
  baseurl_source: declared
  description: The Organizations API from Shuffle — 3 operation(s) for organizations.
  name: Shuffle Organizations API
  slug: shuffle-organizations-api
- baseURL: https://shuffler.io/api/v1
  baseurl_source: declared
  description: The Triggers API from Shuffle — 2 operation(s) for triggers.
  name: Shuffle Triggers API
  slug: shuffle-triggers-api
- baseURL: https://shuffler.io/api/v1
  baseurl_source: declared
  description: The Users API from Shuffle — 5 operation(s) for users.
  name: Shuffle Users API
  slug: shuffle-users-api
- baseURL: https://shuffler.io/api/v1
  baseurl_source: declared
  description: The Workflows API from Shuffle — 9 operation(s) for workflows.
  name: Shuffle Workflows API
  slug: shuffle-workflows-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shuffle Administration API
  slug: open-shuffle-administration-api
- collection_type: open
  name: Shuffle Administration Apps API
  slug: open-shuffle-apps-api
- collection_type: open
  name: Shuffle Administration Datastore API
  slug: open-shuffle-datastore-api
- collection_type: open
  name: Shuffle Administration Files API
  slug: open-shuffle-files-api
- collection_type: open
  name: Shuffle Administration Notifications API
  slug: open-shuffle-notifications-api
- collection_type: open
  name: Shuffle Administration Organizations API
  slug: open-shuffle-organizations-api
- collection_type: open
  name: Shuffle Administration Triggers API
  slug: open-shuffle-triggers-api
- collection_type: open
  name: Shuffle Administration Users API
  slug: open-shuffle-users-api
- collection_type: open
  name: Shuffle Administration Workflows API
  slug: open-shuffle-workflows-api
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
random_paper: 14
rate_limits:
- limit_count: 5
  name: Shuffle Rate Limits
  slug: shuffle-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Shuffle API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: shuffle-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Shuffle API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 4
  slug: shuffle-rules
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 38.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 28.8
    contract_quality: 70.1
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- Open-Source
---
