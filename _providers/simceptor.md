---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Simceptor provides a mock API platform with REST, SOAP, WSDL, and AI‑native features.
  name: Simceptor Mock API
  slug: simceptor-mock-api
- description: 'Simceptor API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: Simceptor API
  slug: simceptor-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/simceptor/rules/simceptor-rules.yml
  title: ''
  type: Spectral
  url: rules/simceptor-rules.yml
- group: design
  href: https://artifacts.apis.io/simceptor/json-ld/simceptor-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/simceptor-context.jsonld
- group: design
  href: https://artifacts.apis.io/simceptor/vocabulary/simceptor-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/simceptor-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/simceptor/data-model/simceptor-data-model.yml
  title: ''
  type: DataModel
  url: data-model/simceptor-data-model.yml
- group: start
  href: https://artifacts.apis.io/simceptor/sandbox/simceptor-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/simceptor-sandbox.yml
- group: design
  href: https://artifacts.apis.io/simceptor/conformance/simceptor-conformance.yml
  title: ''
  type: Conformance
  url: conformance/simceptor-conformance.yml
- group: agent
  href: https://artifacts.apis.io/simceptor/mcp/simceptor-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/simceptor-mcp.yml
- group: agent
  href: https://artifacts.apis.io/simceptor/well-known/simceptor-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/simceptor-well-known.yml
- group: other
  href: https://artifacts.apis.io/simceptor/hosts/simceptor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/simceptor-hosts.yml
- group: other
  href: https://artifacts.apis.io/simceptor/vendors/simceptor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/simceptor-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://simceptor.com/privacy
- group: auth
  href: https://artifacts.apis.io/simceptor/security/simceptor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/simceptor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://simceptor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://simceptor.com/docs
- group: company
  title: ''
  type: Blog
  url: https://simceptor.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://simceptor.com/register
- group: start
  title: ''
  type: Login
  url: https://simceptor.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://simceptor.com/terms
coverage:
  checked: '2026-10-19'
  detail: Documentation pages are rendered via JavaScript (Next.js), preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://simceptor.com/docs/openapi
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: Simceptor provides a free no‑code mock API server that supports REST, SOAP, and WSDL, with conditional rules, AI‑native mocking via Model Context Protocol (MCP), and a playground for developers. It enables rapid creation, testing, and updating of mock endpoints, offering features like latency simulation, dynamic faker data, webhook forwarding, multi‑environment support, and integration with AI assistants such as Claude and Cursor.
image: https://simceptor.com/og-image.jpg
json_schemas:
- name: GetInquiryIdResponse
  property_count: 3
  slug: simceptor-get-inquiry-id-response
- name: GetOrdersIdResponse
  property_count: 3
  slug: simceptor-get-orders-id-response
jsonld:
- class_count: 2
  name: Simceptor Context
  property_count: 4
  slug: simceptor-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.simceptor.com.
  name: Simceptor MCP Server
  slug: simceptor-mcp-yml
modified: '2026-10-18'
name: Simceptor
nav: Providers
network: true
overview: 'Simceptor is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mock API, No-Code, AI Integration, and Developer Tools.


  The Simceptor catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Simceptor''s developer surface includes sandbox, documentation, engineering blog, signup flow, and 14 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Simceptor API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: simceptor-rules
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 51.0
    catalog_earned_first_party: 0.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 17.1
    contract_governance: 19.7
    contract_quality: 18.9
    developer_ergonomics: 13.1
    discoverability: 60.0
    operational_transparency: 0.0
  previous_composite: 24.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/simceptor/simceptor-2026-11-03T143218.png
security:
- kind: domain-security
  name: Simceptor Domain Security
  slug: simceptor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: simceptor
tags:
- Company
- Mock API
- No-Code
- AI Integration
- Developer Tools
website: https://simceptor.com/
---
