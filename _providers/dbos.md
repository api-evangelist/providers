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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: DBOS Transact is a durable execution library that decorates application functions with workflow, step, transaction, scheduled, and Kafka consumer semantics, persisting all state to Postgres so workflo
  name: DBOS Transact
  slug: dbos
- description: DBOS Cloud is the managed, serverless hosting platform for DBOS workflows, queues, and scheduled jobs. The CLI deploys and manages DBOS applications and provides a graphical observability UI.
  name: DBOS Cloud
  slug: dbos-cloud
artifact_total: 11
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/dbos-inc/dbos-transact-py/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/dbos-inc/dbos-transact-py/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/dbos-inc/dbos-transact-py/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/dbos-inc/dbos-transact-py/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dbos-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dbos-inc
- group: company
  title: ''
  type: Website
  url: https://www.dbos.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dbos.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dbos-inc
- group: start
  title: ''
  type: Console
  url: https://console.dbos.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dbos.dev/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.dbos.dev/blog
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/dbos
- group: design
  title: ''
  type: JSONLD
  url: json-ld/dbos-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/dbos-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/dbos-rules.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/dbos-inc/dbos-mcp
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.dbos.dev/llms.txt
created: '2026-03-27'
description: DBOS is a durable execution platform built on Postgres for running resilient workflows, scheduled jobs, durable queues, and Kafka consumers. The core library (DBOS Transact) is available for Python, TypeScript, Go, and Java, with a managed serverless runtime offered as DBOS Cloud.
finops:
- name: Dbos Finops
  service_category: API
  slug: dbos-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dbos.png
json_schemas:
- name: DBOS Workflow
  property_count: 4
  slug: workflow
jsonld:
- class_count: 0
  name: Dbos Context
  property_count: 6
  slug: dbos-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: DBOS
nav: Providers
network: true
overview: 'DBOS publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Composition, Durable Execution, Postgres, Queues, and Scheduled Jobs.


  The DBOS catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  DBOS''s developer surface includes documentation, developer console, pricing, engineering blog, and 14 more developer resources.'
plans:
- name: Dbos Plans Pricing
  plan_count: 3
  slug: dbos-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Dbos Rate Limits
  slug: dbos-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: DBOS API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: dbos-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: DBOS API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: dbos-rules
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 28.8
    contract_quality: 14.7
    developer_ergonomics: 28.6
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 50.0
  previous_composite: 30.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dbos/refs/heads/main/screenshots/dbos-2026-06-20T175736.png
security:
- kind: domain-security
  name: Dbos Domain Security
  slug: dbos-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dbos
tags:
- API Composition
- Durable Execution
- Postgres
- Queues
- Scheduled Jobs
- Workflows
website: https://www.dbos.dev/
---
