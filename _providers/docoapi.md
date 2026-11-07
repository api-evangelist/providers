---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: quarter
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Platform offering API documentation that stays in sync with OpenAPI specifications.
  name: DocoAPI
  slug: docoapi
- description: The admin API from Saga Labs — 2 operation(s) for admin.
  name: Saga Labs Admin API
  slug: docoapi-admin-api
- description: The auth API from Saga Labs — 21 operation(s) for auth.
  name: Saga Labs Auth API
  slug: docoapi-auth-api
- description: The billing API from Saga Labs — 3 operation(s) for billing.
  name: Saga Labs Billing API
  slug: docoapi-billing-api
- description: The github API from Saga Labs — 4 operation(s) for github.
  name: Saga Labs GitHub API
  slug: docoapi-github-api
- description: The Health API from Saga Labs — 1 operation(s) for health.
  name: Saga Labs Health API
  slug: docoapi-health-api
- description: The mcp API from Saga Labs — 1 operation(s) for mcp.
  name: Saga Labs MCP API
  slug: docoapi-mcp-api
- description: The portal API from Saga Labs — 6 operation(s) for portal.
  name: Saga Labs Portal API
  slug: docoapi-portal-api
- description: The portal-search API from Saga Labs — 1 operation(s) for portal-search.
  name: Saga Labs Portal Search API
  slug: docoapi-portal-search-api
- description: The projects API from Saga Labs — 11 operation(s) for projects.
  name: Saga Labs Projects API
  slug: docoapi-projects-api
- description: The proxy API from Saga Labs — 1 operation(s) for proxy.
  name: Saga Labs Proxy API
  slug: docoapi-proxy-api
- description: The users API from Saga Labs — 1 operation(s) for users.
  name: Saga Labs Users API
  slug: docoapi-users-api
- description: The webhooks API from Saga Labs — 1 operation(s) for webhooks.
  name: Saga Labs Webhooks API
  slug: docoapi-webhooks-api
- description: The workspaces API from Saga Labs — 1 operation(s) for workspaces.
  name: Saga Labs Workspaces API
  slug: docoapi-workspaces-api
artifact_total: 19
common:
- group: other
  href: https://artifacts.apis.io/docoapi/capabilities/docoapi-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/docoapi-capability-edges.yml
- group: design
  href: https://artifacts.apis.io/docoapi/rules/docoapi-rules.yml
  title: ''
  type: Spectral
  url: rules/docoapi-rules.yml
- group: design
  href: https://artifacts.apis.io/docoapi/json-ld/docoapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/docoapi-context.jsonld
- group: design
  href: https://artifacts.apis.io/docoapi/vocabulary/docoapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/docoapi-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/docoapi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/docoapi/data-model/docoapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/docoapi-data-model.yml
- group: design
  href: https://artifacts.apis.io/docoapi/errors/docoapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/docoapi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/docoapi/conformance/docoapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/docoapi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/docoapi/llms/docoapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/docoapi-llms.txt
- group: agent
  href: https://artifacts.apis.io/docoapi/mcp/docoapi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/docoapi-mcp.yml
- group: other
  href: https://artifacts.apis.io/docoapi/hosts/docoapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docoapi-hosts.yml
- group: other
  href: https://artifacts.apis.io/docoapi/vendors/docoapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docoapi-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docoapi.com/vs/swagger
- group: auth
  href: https://artifacts.apis.io/docoapi/security/docoapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docoapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docoapi.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://docoapi.com/
- group: start
  title: ''
  type: SignUp
  url: https://docoapi.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docoapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docoapi.com/privacy
coverage:
  checked: '2026-10-16'
  detail: Docs at https://docoapi.com/docs are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://docoapi.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-16'
description: Saga Labs provides DocoAPI, a platform offering API documentation that stays in sync with your OpenAPI specifications. It targets developers seeking automated, up‑to‑date docs, featuring a beta service with a 14‑day free trial, pricing at $99/month, and integrations for FastAPI apps. The service includes live demos, AI coding assistance, and reliable uptime monitoring, aiming to replace costly, manual documentation processes with a seamless, always‑current developer portal.
jsonld:
- class_count: 38
  name: Docoapi Context
  property_count: 88
  slug: docoapi-context
layout: provider
mcp_servers:
- description: Remote MCP server at petstore.docoapi.com.
  name: Saga Labs MCP Server
  slug: docoapi-mcp-yml
modified: '2026-10-16'
name: Saga Labs
nav: Providers
network: true
overview: 'Saga Labs publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Auth API, Billing API, and 11 more. Tagged areas include Company, API Documentation, Developer Tools, Software-as-a-Service, and FastAPI.


  The Saga Labs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Saga Labs'' developer surface includes API reference, pricing, signup flow, and 16 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Saga Labs API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: docoapi-rules
score:
  band: thin
  composite: 26.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 46.8
    catalog_earned_first_party: 0.0
    catalog_gap: 68.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 50.5
    developer_ergonomics: 5.4
    discoverability: 63.3
    operational_transparency: 0.0
  previous_composite: 32.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/docoapi/docoapi-2026-11-03T130839.png
security:
- kind: domain-security
  name: Docoapi Domain Security
  slug: docoapi-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: create-project
  slug: docoapi-create-project
slug: docoapi
tags:
- Company
- API Documentation
- Developer Tools
- Software-as-a-Service
- FastAPI
website: https://docoapi.com/
---
