---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Anahana Com Agentic Access
  operation_count: 20
  slug: anahana-com-agentic-access
  summary_line: 20 operations · 3 acting
api_count: 1
apis:
- baseURL: https://www.anahana.com
  baseurl_source: declared
  description: Static agent-discovery documents.
  name: Anahana Discovery API
  slug: anahana-com-discovery-api
- baseURL: https://www.anahana.com
  baseurl_source: declared
  description: Model Context Protocol server (Streamable HTTP, JSON-RPC 2.0).
  name: Anahana MCP API
  slug: anahana-com-mcp-api
- baseURL: https://www.anahana.com
  baseurl_source: declared
  description: OAuth 2.1 registered tier. Optional — anonymous access to /mcp is fully supported.
  name: Anahana OAuth API
  slug: anahana-com-oauth-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/anahana-com/agentic-access/anahana-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/anahana-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/anahana-com/rate-limits/anahana-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/anahana-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/anahana-com/rules/anahana-com-rules.yml
  title: ''
  type: Spectral
  url: rules/anahana-com-rules.yml
- group: design
  href: https://artifacts.apis.io/anahana-com/json-ld/anahana-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/anahana-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/anahana-com/vocabulary/anahana-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/anahana-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/anahana-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/anahana-com/data-model/anahana-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anahana-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/anahana-com/security/anahana-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/anahana-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/anahana-com/authentication/anahana-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/anahana-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/anahana-com/errors/anahana-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/anahana-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/anahana-com/conformance/anahana-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anahana-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/anahana-com/llms/anahana-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anahana-com-llms.txt
- group: build
  href: https://artifacts.apis.io/anahana-com/mcp/anahana-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/anahana-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/anahana-com/mcp/anahana-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/anahana-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/anahana-com/well-known/anahana-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/anahana-com-security.txt
- group: auth
  href: https://artifacts.apis.io/anahana-com/well-known/anahana-com-anahana-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/anahana-com-anahana-security.txt
- group: agent
  href: https://artifacts.apis.io/anahana-com/well-known/anahana-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anahana-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/anahana-com/hosts/anahana-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anahana-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/anahana-com/vendors/anahana-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anahana-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/anahana-com/security/anahana-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/anahana-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/anahana-com/security/anahana-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anahana-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anahana.com/
- group: company
  title: ''
  type: Blog
  url: https://www.anahana.com/en/nema-blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anahana.com/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anahana.com/en/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.anahana.com/en/support/
created: '2026-11-01'
description: Anahana — Spiritual Wellness & Personal Growth. Explore angel numbers, astrology, tarot, zodiac, crystals, yoga, meditation, and more. Trusted resources for spiritual growth and holistic wellness. A place for wellbeing, movement, and meaning.
image: https://www.anahana.com/images/discovery/river-still.fd59b390aa50f393007f4e9a2de7214820710813a116cb5bdab54f749a3df5e5.webp
json_schemas:
- name: ClientMetadata
  property_count: 6
  slug: anahana-com-client-metadata
- name: JsonRpcRequest
  property_count: 4
  slug: anahana-com-json-rpc-request
- name: JsonRpcResponse
  property_count: 4
  slug: anahana-com-json-rpc-response
jsonld:
- class_count: 4
  name: Anahana Com Context
  property_count: 14
  slug: anahana-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.anahana.com.
  name: Anahana MCP Server
  slug: anahana-com-mcp-yml
modified: '2026-11-01'
name: Anahana
nav: Providers
network: true
overview: 'Anahana publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Discovery API, MCP API, and OAuth API. Tagged areas include SpiritualWellness, Personal Growth, Astrology, Meditation, and Yoga.


  The Anahana catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Anahana''s developer surface includes authentication, engineering blog, support, and 23 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 2
  name: Anahana Com Rate Limits
  slug: anahana-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Anahana API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: anahana-com-rules
scopes:
- name: Anahana Com Scopes
  scope_count: 0
  slug: anahana-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 67.0
    catalog_earned_first_party: 8.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 10.5
    contract_governance: 33.3
    contract_quality: 57.9
    developer_ergonomics: 21.9
    discoverability: 65.0
    operational_transparency: 31.6
  previous_composite: 42.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anahana Com Authentication
  slug: anahana-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Anahana Com Domain Security
  slug: anahana-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Anahana Com Vulnerability Disclosure
  slug: anahana-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: mcp-tools
  slug: anahana-com-mcp-tools
slug: anahana-com
tags:
- SpiritualWellness
- Personal Growth
- Astrology
- Meditation
- Yoga
website: https://anahana.com/
---
