---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Aviansuite Com Agentic Access
  operation_count: 14
  slug: aviansuite-com-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 1
apis:
- description: 'Start here: what AvianSuite is, how agent writes stay safe, and how to connect your first agent.'
  name: AvianSuite API
  slug: aviansuite-api
- baseURL_template: https://{store}
  baseurl_source: spec_template
  description: The Admin API from AvianSuite — 6 operation(s) for admin.
  name: AvianSuite Admin API
  slug: aviansuite-com-admin-api
- baseURL_template: https://{store}
  baseurl_source: spec_template
  description: The Events API from AvianSuite — 2 operation(s) for events.
  name: AvianSuite Events API
  slug: aviansuite-com-events-api
- baseURL_template: https://{store}
  baseurl_source: spec_template
  description: The Health API from AvianSuite — 2 operation(s) for health.
  name: AvianSuite Health API
  slug: aviansuite-com-health-api
- baseURL_template: https://{store}
  baseurl_source: spec_template
  description: The Refs API from AvianSuite — 1 operation(s) for refs.
  name: AvianSuite Refs API
  slug: aviansuite-com-refs-api
- baseURL_template: https://{store}
  baseurl_source: spec_template
  description: The Root API from AvianSuite — 1 operation(s) for root.
  name: AvianSuite Root API
  slug: aviansuite-com-root-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/aviansuite-com/agentic-access/aviansuite-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aviansuite-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/aviansuite-com/plans/aviansuite-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aviansuite-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aviansuite-com/rules/aviansuite-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aviansuite-com-rules.yml
- group: design
  href: https://artifacts.apis.io/aviansuite-com/json-ld/aviansuite-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aviansuite-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/aviansuite-com/vocabulary/aviansuite-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aviansuite-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aviansuite-com/data-model/aviansuite-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aviansuite-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/aviansuite-com/conventions/aviansuite-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/aviansuite-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/aviansuite-com/conventions/aviansuite-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aviansuite-com-conventions.yml
- group: start
  href: https://artifacts.apis.io/aviansuite-com/sandbox/aviansuite-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/aviansuite-com-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/aviansuite-com/authentication/aviansuite-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aviansuite-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/aviansuite-com/errors/aviansuite-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aviansuite-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aviansuite-com/conformance/aviansuite-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aviansuite-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aviansuite-com/llms/aviansuite-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aviansuite-com-llms.txt
- group: build
  href: https://artifacts.apis.io/aviansuite-com/mcp/aviansuite-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aviansuite-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/aviansuite-com/mcp/aviansuite-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aviansuite-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aviansuite-com/well-known/aviansuite-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aviansuite-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aviansuite-com/hosts/aviansuite-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aviansuite-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aviansuite-com/vendors/aviansuite-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aviansuite-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://aviansuite.com/security/
- group: start
  title: ''
  type: Login
  url: https://app.aviansuite.com/login
- group: company
  title: ''
  type: Blog
  url: https://app.aviansuite.com/blog
- group: auth
  href: https://artifacts.apis.io/aviansuite-com/security/aviansuite-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aviansuite-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aviansuite.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aviansuite.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://aviansuite.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://aviansuite.com/docs/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://aviansuite.com/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://aviansuite.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aviansuite.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aviansuite.com/privacy/
coverage:
  checked: '2026-11-02'
  detail: OpenAPI spec at https://aviansuite.com/openapi.json describes Stellar Jay, not AvianSuite.
  evidence:
  - status: 200
    url: https://aviansuite.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: AvianSuite is an agent-native business data platform. AI agents run business processes like sales follow-up and bookkeeping on your company's data, and every change they make is versioned, attributed to the agent that made it, and reversible. Built on the open-source Stellar Jay data store.
image: https://aviansuite.com/og-image.png?v=2
jsonld:
- class_count: 5
  name: Aviansuite Com Context
  property_count: 16
  slug: aviansuite-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at app.aviansuite.com.
  name: AvianSuite MCP Server
  slug: aviansuite-com-mcp-yml
modified: '2026-11-02'
name: AvianSuite
nav: Providers
network: true
overview: 'AvianSuite publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Events API, Health API, and 3 more. Tagged areas include Artificial Intelligence, Agents, Business Data, Automation, and Platform.


  The AvianSuite catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AvianSuite''s developer surface includes sandbox, authentication, engineering blog, documentation, API reference, getting-started guide, support, and 23 more developer resources.'
plans:
- name: Aviansuite Com Plans Pricing
  plan_count: 6
  slug: aviansuite-com-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: AvianSuite API Rules
  rule_count: 50
  severity_counts:
    error: 46
    hint: 0
    info: 3
    warn: 1
  slug: aviansuite-com-rules
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 60.8
    catalog_earned_first_party: 12.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 51.8
    developer_ergonomics: 36.9
    discoverability: 56.7
    operational_transparency: 5.3
  previous_composite: 50.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aviansuite Com Authentication
  slug: aviansuite-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aviansuite Com Domain Security
  slug: aviansuite-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aviansuite-com
tags:
- Artificial Intelligence
- Agents
- Business Data
- Automation
- Platform
website: https://aviansuite.com/
---
