---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Voltcast Com Agentic Access
  operation_count: 3
  slug: voltcast-com-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://voltcast.com/api
  baseurl_source: declared
  description: The Prices API from voltcast-com — 1 operation(s) for prices.
  name: voltcast-com Prices API
  slug: voltcast-com-prices-api
- baseURL: https://voltcast.com/api
  baseurl_source: declared
  description: The Public API from voltcast-com — 1 operation(s) for public.
  name: voltcast-com Public API
  slug: voltcast-com-public-api
- baseURL: https://voltcast.com/api
  baseurl_source: declared
  description: The Zones API from voltcast-com — 1 operation(s) for zones.
  name: voltcast-com Zones API
  slug: voltcast-com-zones-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/voltcast-com/agentic-access/voltcast-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/voltcast-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/voltcast-com/plans/voltcast-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/voltcast-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/voltcast-com/rules/voltcast-com-rules.yml
  title: ''
  type: Spectral
  url: rules/voltcast-com-rules.yml
- group: design
  href: https://artifacts.apis.io/voltcast-com/json-ld/voltcast-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/voltcast-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/voltcast-com/vocabulary/voltcast-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/voltcast-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/voltcast-com/data-model/voltcast-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/voltcast-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/voltcast-com/errors/voltcast-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/voltcast-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/voltcast-com/conformance/voltcast-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/voltcast-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/voltcast-com/llms/voltcast-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/voltcast-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/voltcast-com/mcp/voltcast-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/voltcast-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/voltcast-com/well-known/voltcast-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/voltcast-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/voltcast-com/hosts/voltcast-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/voltcast-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/voltcast-com/vendors/voltcast-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/voltcast-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/voltcast-com/packages/voltcast-com-packages.yml
  title: ''
  type: Packages
  url: packages/voltcast-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://voltcast.com/legal/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://voltcast.com/status
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Voltcast-com/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://voltcast.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://voltcast.com/pricing
- group: start
  title: ''
  type: Login
  url: https://voltcast.com/login
- group: docs
  title: ''
  type: APIReference
  url: https://voltcast.com/docs
- group: auth
  href: https://artifacts.apis.io/voltcast-com/authentication/voltcast-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/voltcast-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/voltcast-com/security/voltcast-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/voltcast-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://voltcast.com/
created: '2026-10-31'
description: Voltcast is a technology company providing a platform for streaming and casting video content to various devices. The service enables developers and enterprises to integrate live and on‑demand video distribution into their applications, offering APIs for content ingestion, transcoding, playback, and analytics. Voltcast focuses on low‑latency delivery, adaptive bitrate streaming, and robust security features, catering to media companies, broadcasters, and corporate communication solutions. The platform supports multi‑region deployment and offers comprehensive documentation for developers to build custom workflows and monetize video streams.
image: https://voltcast.com/og-image.png
json_schemas:
- name: PriceRow
  property_count: 5
  slug: voltcast-com-price-row
jsonld:
- class_count: 3
  name: Voltcast Com Context
  property_count: 10
  slug: voltcast-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at voltcast.com.
  name: voltcast-com MCP Server
  slug: voltcast-com-mcp-yml
modified: '2026-10-31'
name: voltcast-com
nav: Providers
network: true
overview: 'voltcast-com publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Prices API, Public API, and Zones API. Tagged areas include Video, Streaming, Media, and Platform.


  The voltcast-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  voltcast-com''s developer surface includes pricing, API reference, authentication, and 21 more developer resources.'
plans:
- name: Voltcast Com Plans Pricing
  plan_count: 5
  slug: voltcast-com-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: voltcast-com API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: voltcast-com-rules
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 63.2
    catalog_earned_first_party: 12.0
    catalog_gap: 51.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 56.1
    developer_ergonomics: 22.6
    discoverability: 56.7
    operational_transparency: 7.9
  previous_composite: 47.1
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Voltcast Com Authentication
  slug: voltcast-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Voltcast Com Domain Security
  slug: voltcast-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: voltcast-com
tags:
- Video
- Streaming
- Media
- Platform
website: https://voltcast.com/
---
