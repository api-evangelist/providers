---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Provides static outbound IP addresses via WireGuard tunnels for cloud workloads.
  name: AnchoredIP API
  slug: anchoredip-api
- baseURL: https://api.anchoredip.com/api
  baseurl_source: declared
  description: 'AnchoredIP API as documented publicly: 16 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AnchoredIP API
  slug: anchoredip-com-api
artifact_total: 15
common:
- group: commercial
  href: https://artifacts.apis.io/anchoredip-com/plans/anchoredip-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/anchoredip-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/anchoredip-com/rules/anchoredip-com-rules.yml
  title: ''
  type: Spectral
  url: rules/anchoredip-com-rules.yml
- group: design
  href: https://artifacts.apis.io/anchoredip-com/json-ld/anchoredip-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/anchoredip-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/anchoredip-com/vocabulary/anchoredip-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/anchoredip-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/anchoredip-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/anchoredip-com/data-model/anchoredip-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anchoredip-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/anchoredip-com/errors/anchoredip-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/anchoredip-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/anchoredip-com/conformance/anchoredip-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anchoredip-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/anchoredip-com/llms/anchoredip-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anchoredip-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/anchoredip-com/mcp/anchoredip-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/anchoredip-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/anchoredip-com/hosts/anchoredip-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anchoredip-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anchoredip.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.anchoredip.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anchoredip.com/privacy
- group: auth
  href: https://artifacts.apis.io/anchoredip-com/security/anchoredip-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anchoredip-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anchoredip.com/
- group: docs
  title: ''
  type: Documentation
  url: https://anchoredip.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://anchoredip.com/docs/mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://anchoredip.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://anchoredip.com/order
- group: start
  title: ''
  type: Login
  url: https://anchoredip.com/leases
- group: start
  title: ''
  type: GettingStarted
  url: https://anchoredip.com/order
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec was found on the provider's API host.
  evidence:
  - status: 404
    url: https://api.anchoredip.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AnchoredIP provides static outbound IP addresses (IPv4 and IPv6) via WireGuard tunnels for cloud workloads, enabling reliable allowlisting for APIs and services.
image: https://anchoredip.com/og-image.png
json_schemas:
- name: GetApiPlansResponseResponse
  property_count: 11
  slug: anchoredip-com-get-api-plans-response-response
- name: GetApiPlansResponse
  property_count: 11
  slug: anchoredip-com-get-api-plans-response
- name: PostApiLeasesAccesstokenTunnelsRequest
  property_count: 4
  slug: anchoredip-com-post-api-leases-accesstoken-tunnels-request
- name: PostApiLeasesAccesstokenTunnelsResponse
  property_count: 5
  slug: anchoredip-com-post-api-leases-accesstoken-tunnels-response
- name: PostApiLeasesRequest
  property_count: 4
  slug: anchoredip-com-post-api-leases-request
- name: PostApiLeasesResponse
  property_count: 5
  slug: anchoredip-com-post-api-leases-response
jsonld:
- class_count: 13
  name: Anchoredip Com Context
  property_count: 39
  slug: anchoredip-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.anchoredip.com.
  name: AnchoredIP MCP Server
  slug: anchoredip-com-mcp-yml
modified: '2026-11-01'
name: AnchoredIP
nav: Providers
network: true
overview: 'AnchoredIP is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include StaticIP, Networking, Cloud, WireGuard, and Outbound.


  The AnchoredIP catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AnchoredIP''s developer surface includes documentation, API reference, pricing, signup flow, getting-started guide, and 17 more developer resources.'
plans:
- name: Anchoredip Com Plans Pricing
  plan_count: 4
  slug: anchoredip-com-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: AnchoredIP API Rules
  rule_count: 9
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 0
  slug: anchoredip-com-rules
scopes:
- name: Anchoredip Com Scopes
  scope_count: 0
  slug: anchoredip-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 28
    catalog_earned: 69.0
    catalog_earned_first_party: 12.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 53.9
    contract_governance: 19.7
    contract_quality: 24.8
    developer_ergonomics: 20.7
    discoverability: 56.7
    operational_transparency: 7.9
  previous_composite: 40.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anchoredip Com Authentication
  slug: anchoredip-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Anchoredip Com Domain Security
  slug: anchoredip-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: anchoredip-com
tags:
- StaticIP
- Networking
- Cloud
- WireGuard
- Outbound
website: https://anchoredip.com/
---
