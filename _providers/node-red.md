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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 11
  human_in_the_loop: 3
  name: Node Red Agentic Access
  operation_count: 20
  slug: node-red-agentic-access
  summary_line: 20 operations · 11 acting · 3 human-in-the-loop
api_count: 6
apis:
- description: The Auth API from Node-RED — 3 operation(s) for auth.
  name: Node-RED Auth API
  slug: node-red-auth-api
- description: The Diagnostics API from Node-RED — 1 operation(s) for diagnostics.
  name: Node-RED Diagnostics API
  slug: node-red-diagnostics-api
- description: The Flow API from Node-RED — 2 operation(s) for flow.
  name: Node-RED Flow API
  slug: node-red-flow-api
- description: The Flows API from Node-RED — 2 operation(s) for flows.
  name: Node-RED Flows API
  slug: node-red-flows-api
- description: The Nodes API from Node-RED — 3 operation(s) for nodes.
  name: Node-RED Nodes API
  slug: node-red-nodes-api
- description: The Settings API from Node-RED — 1 operation(s) for settings.
  name: Node-RED Settings API
  slug: node-red-settings-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Node-RED Admin API
  slug: open-node-red-admin
- collection_type: open
  name: Node-RED Admin Auth API
  slug: open-node-red-auth-api
- collection_type: open
  name: Node-RED Admin Auth Diagnostics API
  slug: open-node-red-diagnostics-api
- collection_type: open
  name: Node-RED Admin Auth Flow API
  slug: open-node-red-flow-api
- collection_type: open
  name: Node-RED Admin Auth Flows API
  slug: open-node-red-flows-api
- collection_type: open
  name: Node-RED Admin Auth Nodes API
  slug: open-node-red-nodes-api
- collection_type: open
  name: Node-RED Admin Auth Settings API
  slug: open-node-red-settings-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/node-red/node-red/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/node-red/node-red/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/node-red/node-red/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/node-red/node-red/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/node-red/node-red/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/node-red/node-red/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/node-red-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/node-red-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/node-red-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://nodered.org
- group: docs
  title: ''
  type: Documentation
  url: https://nodered.org/docs/
- group: docs
  title: ''
  type: API Documentation
  url: https://nodered.org/docs/api/admin/methods/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/node-red/refs/heads/main/openapi/node-red-admin-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/node-red/refs/heads/main/json-schema/node-red-flow-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/node-red/refs/heads/main/json-ld/node-red-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://nodered.org/feed.xml
created: '2026-03-27'
description: Node-RED is an open source flow-based programming tool for wiring together hardware devices, APIs, and online services. The runtime exposes an Admin HTTP API used by the Node-RED Editor and the command-line admin tool to manage flows, nodes, settings, diagnostics, and authentication.
finops:
- name: Node Red Finops
  service_category: API
  slug: node-red-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/node-red.png
json_schemas:
- name: Node-RED Flow
  property_count: 11
  slug: node-red-flow
jsonld:
- class_count: 9
  name: Node Red Context
  property_count: 0
  slug: node-red-context
layout: provider
modified: '2026-05-19'
name: Node-RED
nav: Providers
network: true
overview: 'Node-RED publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Diagnostics API, Flow API, and 3 more. Tagged areas include Self-Hosted, Workflow Automation, Flow-Based Programming, and IoT.


  The Node-RED catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Node-RED''s developer surface includes authentication, documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Node Red Plans Pricing
  plan_count: 3
  slug: node-red-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 5
  name: Node Red Rate Limits
  slug: node-red-rate-limits
rules:
- name: Node-RED API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: node-red-jsonschema-spectral-rules
score:
  band: thin
  composite: 41.3
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 61.9
    developer_ergonomics: 28.3
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 34.2
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/node-red/refs/heads/main/screenshots/node-red-2026-06-20T190350.png
security:
- kind: authentication
  name: Node Red Authentication
  slug: node-red-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Node Red Domain Security
  slug: node-red-domain-security
  summary_line: TLSv1.3 · DMARC
slug: node-red
tags:
- Self-Hosted
- Workflow Automation
- Flow-Based Programming
- IoT
website: https://nodered.org
---
