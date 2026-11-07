---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Provides access to Jev AI models and tools.
  name: Jev API
  slug: jev-api
- description: 'Jev Model Guide API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Jev Model Guide API
  slug: jevmodel-org-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/jevmodel-org/plans/jevmodel-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jevmodel-org-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/jevmodel-org/rules/jevmodel-org-rules.yml
  title: ''
  type: Spectral
  url: rules/jevmodel-org-rules.yml
- group: design
  href: https://artifacts.apis.io/jevmodel-org/json-ld/jevmodel-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/jevmodel-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/jevmodel-org/vocabulary/jevmodel-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/jevmodel-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/jevmodel-org/data-model/jevmodel-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/jevmodel-org-data-model.yml
- group: design
  href: https://artifacts.apis.io/jevmodel-org/conventions/jevmodel-org-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/jevmodel-org-conventions.yml
- group: design
  href: https://artifacts.apis.io/jevmodel-org/conventions/jevmodel-org-conventions.yml
  title: ''
  type: Conventions
  url: conventions/jevmodel-org-conventions.yml
- group: auth
  href: https://artifacts.apis.io/jevmodel-org/authentication/jevmodel-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jevmodel-org-authentication.yml
- group: design
  href: https://artifacts.apis.io/jevmodel-org/conformance/jevmodel-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jevmodel-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/jevmodel-org/llms/jevmodel-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jevmodel-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/jevmodel-org/mcp/jevmodel-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/jevmodel-org-mcp.yml
- group: other
  href: https://artifacts.apis.io/jevmodel-org/hosts/jevmodel-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jevmodel-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/jevmodel-org/vendors/jevmodel-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jevmodel-org-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jevmodel.org/terms/
- group: commercial
  title: ''
  type: Pricing
  url: https://jevmodel.org/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://jevmodel.org/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://jevmodel.org/how-to-use-jev/
- group: auth
  href: https://artifacts.apis.io/jevmodel-org/security/jevmodel-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jevmodel-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jevmodel.org
created: '2026-10-28'
description: Jev Model Guide provides the Jev AI decision model API, a hosted service by TypeSafe that returns choices, scores, or yes/no probabilities for application state queries. It offers a free Playground with 10,000 tokens, paid usage at $0.042 per million tokens, and detailed documentation, pricing, and support pages. The service is closed-source, focused on routing and gating use cases, and integrates via REST endpoints.
image: https://jevmodel.org/og.png
json_schemas:
- name: GetMcpResponse
  property_count: 1
  slug: jevmodel-org-get-mcp-response
jsonld:
- class_count: 1
  name: Jevmodel Org Context
  property_count: 1
  slug: jevmodel-org-context
layout: provider
mcp_servers:
- description: Remote MCP server at jevmodel.org requiring an API key.
  name: Jev Model Guide MCP Server
  slug: jevmodel-org-mcp-yml
modified: '2026-10-28'
name: Jev Model Guide
nav: Providers
network: true
overview: 'Jev Model Guide is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, DecisionModel, and Type Safe.


  The Jev Model Guide catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Jev Model Guide''s developer surface includes authentication, pricing, documentation, getting-started guide, and 15 more developer resources.'
plans:
- name: Jevmodel Org Plans Pricing
  plan_count: 9
  slug: jevmodel-org-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Jev Model Guide API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: jevmodel-org-rules
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 55.2
    catalog_earned_first_party: 12.0
    catalog_gap: 59.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 17.6
    developer_ergonomics: 22.6
    discoverability: 58.3
    operational_transparency: 0.0
  previous_composite: 30.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/jevmodel-org/jevmodel-org-2026-11-03T134141.png
security:
- kind: authentication
  name: Jevmodel Org Authentication
  slug: jevmodel-org-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Jevmodel Org Domain Security
  slug: jevmodel-org-domain-security
  summary_line: TLSv1.3
slug: jevmodel-org
tags:
- Company
- Artificial Intelligence
- DecisionModel
- Type Safe
website: https://jevmodel.org
---
