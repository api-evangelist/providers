---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 2
  name: Asoskill Com Agentic Access
  operation_count: 13
  slug: asoskill-com-agentic-access
  summary_line: 13 operations · 7 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.asoskill.com
  baseurl_source: declared
  description: Browser-assisted agent login and credential lifecycle
  name: asoskill-com Authentication API
  slug: asoskill-com-authentication-api
- baseURL: https://api.asoskill.com
  baseurl_source: declared
  description: Credit-pack discovery and Polar Checkout
  name: asoskill-com Billing API
  slug: asoskill-com-billing-api
- baseURL: https://api.asoskill.com
  baseurl_source: declared
  description: API-key credit balance and usage
  name: asoskill-com Credits API
  slug: asoskill-com-credits-api
- baseURL: https://api.asoskill.com
  baseurl_source: declared
  description: Metered App Store keyword and app data endpoints
  name: asoskill-com Data API
  slug: asoskill-com-data-api
- baseURL: https://api.asoskill.com
  baseurl_source: declared
  description: OAuth-protected Model Context Protocol endpoint for AI clients
  name: asoskill-com MCP API
  slug: asoskill-com-mcp-api
- baseURL: https://api.asoskill.com
  baseurl_source: declared
  description: Unauthenticated service availability
  name: asoskill-com Operations API
  slug: asoskill-com-operations-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/asoskill-com/agentic-access/asoskill-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/asoskill-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/asoskill-com/plans/asoskill-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/asoskill-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/asoskill-com/rules/asoskill-com-rules.yml
  title: ''
  type: Spectral
  url: rules/asoskill-com-rules.yml
- group: design
  href: https://artifacts.apis.io/asoskill-com/json-ld/asoskill-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/asoskill-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/asoskill-com/vocabulary/asoskill-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/asoskill-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/asoskill-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/asoskill-com/data-model/asoskill-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/asoskill-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/asoskill-com/errors/asoskill-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/asoskill-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/asoskill-com/conformance/asoskill-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/asoskill-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/asoskill-com/llms/asoskill-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asoskill-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/asoskill-com/well-known/asoskill-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/asoskill-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/asoskill-com/hosts/asoskill-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asoskill-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/asoskill-com/vendors/asoskill-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asoskill-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.asoskill.com/api/auth/login
- group: auth
  href: https://artifacts.apis.io/asoskill-com/scopes/asoskill-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/asoskill-com-scopes.yml
- group: auth
  href: https://artifacts.apis.io/asoskill-com/authentication/asoskill-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/asoskill-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/asoskill-com/security/asoskill-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asoskill-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asoskill.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.asoskill.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.asoskill.com/openapi.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.asoskill.com/skill
- group: operate
  title: ''
  type: Support
  url: https://www.asoskill.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.asoskill.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.asoskill.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.asoskill.com/privacy
created: '2026-10-30'
description: ASO Skill provides a compact, typed HTTP API for current App Store search results, autocomplete suggestions, keyword difficulty, popularity, and app metadata. Operated by Hesselbom Tech AB in Sweden, the service offers predictable JSON, explicit caching, credit‑based usage, and a public OpenAPI contract for integration with AI agents and scripts.
image: https://www.asoskill.com/og-image-v2.png
json_schemas:
- name: ApiDiscoveryResponse
  property_count: 12
  slug: asoskill-com-api-discovery-response
- name: AutocompleteResponse
  property_count: 8
  slug: asoskill-com-autocomplete-response
- name: DeviceAuthorizationResponse
  property_count: 6
  slug: asoskill-com-device-authorization-response
- name: DeviceTokenResponse
  property_count: 3
  slug: asoskill-com-device-token-response
- name: PopularityResponse
  property_count: 10
  slug: asoskill-com-popularity-response
- name: SearchResponse
  property_count: 9
  slug: asoskill-com-search-response
jsonld:
- class_count: 36
  name: Asoskill Com Context
  property_count: 105
  slug: asoskill-com-context
layout: provider
modified: '2026-10-30'
name: asoskill-com
nav: Providers
network: true
overview: 'asoskill-com publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Billing API, Credits API, and 3 more. Tagged areas include Company, ASO, App Store, and Data.


  The asoskill-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  asoskill-com''s developer surface includes authentication, API reference, getting-started guide, support, pricing, and 20 more developer resources.'
plans:
- name: Asoskill Com Plans Pricing
  plan_count: 4
  slug: asoskill-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Asoskill Com Rate Limits
  slug: asoskill-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: asoskill-com API Rules
  rule_count: 18
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 1
  slug: asoskill-com-rules
scopes:
- name: Asoskill Com Scopes
  scope_count: 2
  slug: asoskill-com-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 47.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 77.8
    catalog_earned_first_party: 20.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 66.6
    developer_ergonomics: 35.0
    discoverability: 57.1
    operational_transparency: 21.1
  previous_composite: 57.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/asoskill-com/asoskill-com-2026-11-03T121208.png
security:
- kind: authentication
  name: Asoskill Com Authentication
  slug: asoskill-com-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Asoskill Com Domain Security
  slug: asoskill-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: discover-skill
  slug: asoskill-com-discover-skill
- name: aso-skill-search
  slug: asoskill-com-search-skill
slug: asoskill-com
tags:
- Company
- ASO
- App Store
- Data
website: https://asoskill.com/
---
