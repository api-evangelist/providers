---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The public REST API for AXL, providing JSON over HTTPS with authentication via API keys.
  name: AXL REST API
  slug: axl-rest-api
- baseURL: https://app.axl.tech
  baseurl_source: declared
  description: 'AXL API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: AXL API
  slug: axl-tech-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/axl-tech/plans/axl-tech-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/axl-tech-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/axl-tech/rules/axl-tech-rules.yml
  title: ''
  type: Spectral
  url: rules/axl-tech-rules.yml
- group: design
  href: https://artifacts.apis.io/axl-tech/json-ld/axl-tech-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/axl-tech-context.jsonld
- group: design
  href: https://artifacts.apis.io/axl-tech/vocabulary/axl-tech-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/axl-tech-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/axl-tech/data-model/axl-tech-data-model.yml
  title: ''
  type: DataModel
  url: data-model/axl-tech-data-model.yml
- group: auth
  href: https://artifacts.apis.io/axl-tech/authentication/axl-tech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/axl-tech-authentication.yml
- group: design
  href: https://artifacts.apis.io/axl-tech/conformance/axl-tech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/axl-tech-conformance.yml
- group: agent
  href: https://artifacts.apis.io/axl-tech/llms/axl-tech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/axl-tech-llms.txt
- group: agent
  href: https://artifacts.apis.io/axl-tech/mcp/axl-tech-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/axl-tech-mcp.yml
- group: agent
  href: https://artifacts.apis.io/axl-tech/well-known/axl-tech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/axl-tech-well-known.yml
- group: other
  href: https://artifacts.apis.io/axl-tech/hosts/axl-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/axl-tech-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://axl.tech/security
- group: start
  title: ''
  type: GettingStarted
  url: https://axl.tech/developers/mcp/chatgpt
- group: auth
  href: https://artifacts.apis.io/axl-tech/security/axl-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axl-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://axl.tech/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://axl.tech/developers
- group: docs
  title: ''
  type: Documentation
  url: https://axl.tech/developers
- group: docs
  title: ''
  type: APIReference
  url: https://axl.tech/developers/api
- group: operate
  title: ''
  type: Support
  url: https://axl.tech/support
- group: company
  title: ''
  type: Blog
  url: https://axl.tech/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://axl.tech/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://axl.tech/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://axl.tech/legal/privacy
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI or other machine-readable spec is published for the API.
  evidence:
  - status: 404
    url: https://app.axl.tech/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: AXL is an AI-native sales and marketing platform that enables founder-led businesses to build websites, manage leads, automate follow-up, book clients, and process payments through chat. It combines CRM, automation, booking, payments, calls, courses, and customer history into a single solution, offering a unified experience for sales teams, call centers, and online course creators.
image: https://cdn.app.axl.tech/2b1aHbg3dU60m7o2bL753w/images/ryT6bPQamkainNTTvqI00A.png
json_schemas:
- name: GetApiV1CrmLeadResponse
  property_count: 3
  slug: axl-tech-get-api-v1-crm-lead-response
- name: PostApiV1ScenarioRunRequest
  property_count: 3
  slug: axl-tech-post-api-v1-scenario-run-request
- name: PostLeadsRequest
  property_count: 3
  slug: axl-tech-post-leads-request
jsonld:
- class_count: 3
  name: Axl Tech Context
  property_count: 9
  slug: axl-tech-context
layout: provider
mcp_servers:
- description: Remote MCP server at app.axl.tech.
  name: AXL MCP Server
  slug: axl-tech-mcp-yml
modified: '2026-11-02'
name: AXL
nav: Providers
network: true
overview: 'AXL is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Sales, Marketing, CRM, and Automation.


  The AXL catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AXL''s developer surface includes authentication, getting-started guide, documentation, API reference, support, engineering blog, pricing, and 16 more developer resources.'
plans:
- name: Axl Tech Plans Pricing
  plan_count: 5
  slug: axl-tech-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Axl Tech Rate Limits
  slug: axl-tech-rate-limits
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: AXL API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: axl-tech-rules
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 68.8
    catalog_earned_first_party: 12.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 34.5
    discoverability: 65.0
    operational_transparency: 5.3
  previous_composite: 41.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
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
  name: Axl Tech Authentication
  slug: axl-tech-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Axl Tech Domain Security
  slug: axl-tech-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: axl-tech
tags:
- Artificial Intelligence
- Sales
- Marketing
- CRM
- Automation
website: https://axl.tech/
---
