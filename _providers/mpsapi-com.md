---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Provides access to mobile and residential proxy endpoints via REST. Supports reseller and direct developer usage with API key authentication.
  name: MPS Proxy API
  slug: mps-proxy-api
- description: 'mpsapi-com API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: mpsapi-com API
  slug: mpsapi-com-api
artifact_total: 11
common:
- group: operate
  href: https://artifacts.apis.io/mpsapi-com/rate-limits/mpsapi-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mpsapi-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/mpsapi-com/plans/mpsapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mpsapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mpsapi-com/rules/mpsapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/mpsapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/mpsapi-com/json-ld/mpsapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mpsapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/mpsapi-com/vocabulary/mpsapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mpsapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/mpsapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/mpsapi-com/data-model/mpsapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mpsapi-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/mpsapi-com/authentication/mpsapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mpsapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/mpsapi-com/conformance/mpsapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mpsapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mpsapi-com/llms/mpsapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mpsapi-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/mpsapi-com/mcp/mpsapi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mpsapi-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/mpsapi-com/well-known/mpsapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mpsapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/mpsapi-com/hosts/mpsapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mpsapi-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/mpsapi-com/security/mpsapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mpsapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mpsapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://mpsapi.com/en/docs.html
- group: docs
  title: ''
  type: APIReference
  url: https://mpsapi.com/en/docs.html
- group: start
  title: ''
  type: GettingStarted
  url: https://mpsapi.com/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mpsapi.com/en/terms-of-service.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mpsapi.com/en/privacypolicy.html
- group: operate
  title: ''
  type: Support
  url: https://mpsapi.com/en/
coverage:
  checked: '2026-10-31'
  detail: OpenAPI spec is mentioned in llms.txt but requires API key authentication, preventing public access.
  evidence:
  - status: 200
    url: https://mpsapi.com/en/reseller-api.html
  reason: auth-required
  state: gated
created: '2026-10-30'
description: MPS API provides mobile and residential proxy services via a RESTful API for developers and resellers. It offers proxy endpoints in 47 countries for mobile connections and in 178 countries for residential IPs, with a 16% reseller discount and flexible pricing. Users obtain an API key after sign‑up and can integrate the service into data collection, automation, and testing workflows. The platform emphasizes high‑availability, global coverage, and easy integration through standard HTTP requests.
image: https://mpsapi.com/build/images/logo/favico_api.svg?1790585629
json_schemas:
- name: GetApiHtmlResponse
  property_count: 7
  slug: mpsapi-com-get-api-html-response
jsonld:
- class_count: 1
  name: Mpsapi Com Context
  property_count: 7
  slug: mpsapi-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.mpsapi.com.
  name: mpsapi-com MCP Server
  slug: mpsapi-com-mcp-yml
modified: '2026-10-30'
name: mpsapi-com
nav: Providers
network: true
overview: 'mpsapi-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Proxy, Mobile, Residential, and Reseller.


  The mpsapi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  mpsapi-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, and 16 more developer resources.'
plans:
- name: Mpsapi Com Plans Pricing
  plan_count: 3
  slug: mpsapi-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Mpsapi Com Rate Limits
  slug: mpsapi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: mpsapi-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: mpsapi-com-rules
scopes:
- name: Mpsapi Com Scopes
  scope_count: 0
  slug: mpsapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 81.1
    catalog_earned_first_party: 0.0
    catalog_gap: 33.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 49.5
    contract_governance: 79.1
    contract_quality: 45.0
    developer_ergonomics: 51.7
    discoverability: 56.7
    operational_transparency: 18.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Mpsapi Com Authentication
  slug: mpsapi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mpsapi Com Domain Security
  slug: mpsapi-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mpsapi-com
tags:
- Company
- Proxy
- Mobile
- Residential
- Reseller
website: https://mpsapi.com/
---
