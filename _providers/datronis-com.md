---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.datronis.com
  baseurl_source: declared
  description: 'Datronis API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Datronis API
  slug: datronis-com-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/datronis-com/plans/datronis-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datronis-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/datronis-com/rules/datronis-com-rules.yml
  title: ''
  type: Spectral
  url: rules/datronis-com-rules.yml
- group: design
  href: https://artifacts.apis.io/datronis-com/json-ld/datronis-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/datronis-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/datronis-com/vocabulary/datronis-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datronis-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/datronis-com/data-model/datronis-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/datronis-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/datronis-com/cli/datronis-com-cli.yml
  title: ''
  type: CLI
  url: cli/datronis-com-cli.yml
- group: design
  href: https://artifacts.apis.io/datronis-com/conformance/datronis-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datronis-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/datronis-com/llms/datronis-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datronis-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/datronis-com/mcp/datronis-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/datronis-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/datronis-com/hosts/datronis-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datronis-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datronis.com/terms-of-service/
- group: start
  title: ''
  type: SignUp
  url: https://datronis.com/signup/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datronis.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://datronis.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://datronis.com/news/
- group: docs
  title: ''
  type: Documentation
  url: https://datronis.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://datronis.com/docs/kanban-quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.datronis.com\
- group: auth
  href: https://artifacts.apis.io/datronis-com/security/datronis-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datronis-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datronis.com/
created: '2026-11-05'
description: Datronis provides free tools, remote job listings, and a global payments platform for remote workers. It offers a suite of productivity utilities, multilingual support in 24 languages, and a no‑credit‑card‑required onboarding. Users can find remote jobs, access free SaaS tools, and receive payments worldwide, all through a simple web interface.
image: https://datronis.com/images/logo_circle.svg
json_schemas:
- name: PostApiMcpRequest
  property_count: 4
  slug: datronis-com-post-api-mcp-request
jsonld:
- class_count: 1
  name: Datronis Com Context
  property_count: 4
  slug: datronis-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.datronis.com.
  name: Datronis MCP Server
  slug: datronis-com-mcp-yml
modified: '2026-11-05'
name: Datronis
nav: Providers
network: true
overview: 'Datronis is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Remote Work, Payments, Tools, Job, and Multilingual.


  The Datronis catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Datronis'' developer surface includes CLI, signup flow, pricing, documentation, getting-started guide, and 15 more developer resources.'
plans:
- name: Datronis Com Plans Pricing
  plan_count: 4
  slug: datronis-com-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 70
  extends:
  - spectral:oas
  name: Datronis API Rules
  rule_count: 29
  severity_counts:
    error: 27
    hint: 0
    info: 1
    warn: 1
  slug: datronis-com-rules
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 65.2
    catalog_earned_first_party: 12.0
    catalog_gap: 49.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 17.8
    developer_ergonomics: 38.1
    discoverability: 66.7
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Datronis Com Domain Security
  slug: datronis-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: datronis-com
tags:
- Remote Work
- Payments
- Tools
- Job
- Multilingual
website: https://datronis.com/
---
