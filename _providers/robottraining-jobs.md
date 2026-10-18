---
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Robottraining Jobs Agentic Access
  operation_count: 3
  slug: robottraining-jobs-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://robottraining.jobs
  baseurl_source: spec
  description: The Pay.csv API from RobotTraining.jobs — 1 operation(s) for pay.csv.
  name: RobotTraining.jobs Pay.csv API
  slug: robottraining-jobs-pay-csv-api
- baseURL: https://robottraining.jobs
  baseurl_source: spec
  description: The Pay.json API from RobotTraining.jobs — 1 operation(s) for pay.json.
  name: RobotTraining.jobs Pay.json API
  slug: robottraining-jobs-pay-json-api
- baseURL: https://robottraining.jobs
  baseurl_source: spec
  description: The Roles.json API from RobotTraining.jobs — 1 operation(s) for roles.json.
  name: RobotTraining.jobs Roles.json API
  slug: robottraining-jobs-roles-json-api
artifact_total: 10
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/robottraining-jobs/refs/heads/main/agentic-access/robottraining-jobs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/robottraining-jobs-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/robottraining-jobs/refs/heads/main/rules/robottraining-jobs-rules.yml
  title: ''
  type: Spectral
  url: rules/robottraining-jobs-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/robottraining-jobs/refs/heads/main/json-ld/robottraining-jobs-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/robottraining-jobs-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/robottraining-jobs/refs/heads/main/vocabulary/robottraining-jobs-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/robottraining-jobs-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/robottraining-jobs/refs/heads/main/data-model/robottraining-jobs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/robottraining-jobs-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/robottraining-jobs/refs/heads/main/conformance/robottraining-jobs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/robottraining-jobs-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/robottraining-jobs/refs/heads/main/overlays/robottraining-jobs-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/robottraining-jobs-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/robottraining-jobs/refs/heads/main/llms/robottraining-jobs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/robottraining-jobs-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/robottraining-jobs/refs/heads/main/mcp/robottraining-jobs-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/robottraining-jobs-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/robottraining-jobs/refs/heads/main/hosts/robottraining-jobs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/robottraining-jobs-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/robottraining-jobs/refs/heads/main/vendors/robottraining-jobs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/robottraining-jobs-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/robottraining-jobs/refs/heads/main/security/robottraining-jobs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/robottraining-jobs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://robottraining.jobs
- group: docs
  title: ''
  type: Documentation
  url: https://robottraining.jobs/data
- group: docs
  title: ''
  type: APIReference
  url: https://robottraining.jobs/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://robottraining.jobs/learn
- group: operate
  title: ''
  type: Support
  url: https://robottraining.jobs/about
- group: company
  title: ''
  type: Blog
  url: https://robottraining.jobs/learn
- group: start
  title: ''
  type: SignUp
  url: https://robottraining.jobs/app
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://robottraining.jobs/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://robottraining.jobs/legal/terms
created: '2026-10-15'
description: RobotTraining.jobs is a job board focused on robot‑training and robot‑operator positions. It aggregates listings from robotics companies, providing details on pay, job type, and employer. Users can browse, compare, and apply to roles across various platforms, with tools to estimate earnings and match opportunities to their skills.
image: https://robottraining.jobs/opengraph-image
json_schemas:
- name: PayDocument
  property_count: 0
  slug: robottraining-jobs-pay-document
- name: RolesDocument
  property_count: 0
  slug: robottraining-jobs-roles-document
jsonld:
- class_count: 2
  name: Robottraining Jobs Context
  property_count: 14
  slug: robottraining-jobs-context
layout: provider
mcp_servers:
- description: Remote MCP server at robottraining.jobs.
  name: RobotTraining.jobs MCP Server
  slug: robottraining-jobs-mcp-yml
modified: '2026-10-15'
name: RobotTraining.jobs
nav: Providers
network: true
overview: 'RobotTraining.jobs publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Pay.csv API, Pay.json API, and Roles.json API. Tagged areas include Company, JobBoard, Robotics, Employment, and Artificial Intelligence.


  The RobotTraining.jobs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RobotTraining.jobs'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 15 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: RobotTraining.jobs API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: robottraining-jobs-rules
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 56.3
    developer_ergonomics: 35.7
    discoverability: 66.7
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 17.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Robottraining Jobs Domain Security
  slug: robottraining-jobs-domain-security
  summary_line: TLSv1.3 · HSTS
slug: robottraining-jobs
tags:
- Company
- JobBoard
- Robotics
- Employment
- Artificial Intelligence
website: https://robottraining.jobs
---
