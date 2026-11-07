---
access_model:
  confidence: high
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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Hosted/remote MCP server 'LOA Healthcare Pricing' v1.0.0 over Streamable HTTP with 12 tools for CPT search, procedure suggestions, provider/hospital search, pricing estimates, market pricing, entity p
  name: Loa Healthcare Pricing MCP Server
  slug: loa-healthcare-pricing-mcp-server
- baseURL: https://www.loacare.com/api/v1
  baseurl_source: declared
  description: The Entities API from Loa Healthcare Pricing API — 3 operation(s) for entities.
  name: Loa Healthcare Pricing API Entities API
  slug: loa-healthcare-pricing-api-entities-api
- baseURL: https://www.loacare.com/api/v1
  baseurl_source: declared
  description: The Entity Analytics API from Loa Healthcare Pricing API — 1 operation(s) for entity analytics.
  name: Loa Healthcare Pricing API Entity Analytics API
  slug: loa-healthcare-pricing-api-entity-analytics-api
- baseURL: https://www.loacare.com/api/v1
  baseurl_source: declared
  description: The Entity Updates API from Loa Healthcare Pricing API — 1 operation(s) for entity updates.
  name: Loa Healthcare Pricing API Entity Updates API
  slug: loa-healthcare-pricing-api-entity-updates-api
- baseURL: https://www.loacare.com/api/v1
  baseurl_source: declared
  description: The Prices API from Loa Healthcare Pricing API — 1 operation(s) for prices.
  name: Loa Healthcare Pricing API Prices API
  slug: loa-healthcare-pricing-api-prices-api
artifact_total: 21
collections:
- collection_type: open
  name: Loa Healthcare Pricing Entities API
  slug: open-loa-healthcare-pricing-api-entities-api
- collection_type: open
  name: Loa Healthcare Pricing Entity Analytics API
  slug: open-loa-healthcare-pricing-api-entity-analytics-api
- collection_type: open
  name: Loa Healthcare Pricing Entity Updates API
  slug: open-loa-healthcare-pricing-api-entity-updates-api
- collection_type: open
  name: Loa Healthcare Pricing Prices API
  slug: open-loa-healthcare-pricing-api-prices-api
common:
- group: other
  href: https://artifacts.apis.io/loa-healthcare-pricing-api/capabilities/loa-healthcare-pricing-api-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/loa-healthcare-pricing-api-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.loacare.com
- group: auth
  href: https://artifacts.apis.io/loa-healthcare-pricing-api/security/loa-healthcare-pricing-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/loa-healthcare-pricing-api-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/loa-healthcare-pricing-api/authentication/loa-healthcare-pricing-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/loa-healthcare-pricing-api-authentication.yml
- group: agent
  href: https://artifacts.apis.io/loa-healthcare-pricing-api/well-known/loa-healthcare-pricing-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/loa-healthcare-pricing-api-well-known.yml
- group: agent
  href: https://artifacts.apis.io/loa-healthcare-pricing-api/llms/loa-healthcare-pricing-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/loa-healthcare-pricing-api-llms.txt
- group: design
  href: https://artifacts.apis.io/loa-healthcare-pricing-api/conformance/loa-healthcare-pricing-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/loa-healthcare-pricing-api-conformance.yml
- group: design
  href: https://artifacts.apis.io/loa-healthcare-pricing-api/errors/loa-healthcare-pricing-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/loa-healthcare-pricing-api-problem-types.yml
- group: design
  href: https://artifacts.apis.io/loa-healthcare-pricing-api/lifecycle/loa-healthcare-pricing-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/loa-healthcare-pricing-api-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/loa-healthcare-pricing-api/scopes/loa-healthcare-pricing-api-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/loa-healthcare-pricing-api-scopes.yml
- group: design
  href: https://artifacts.apis.io/loa-healthcare-pricing-api/conventions/loa-healthcare-pricing-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/loa-healthcare-pricing-api-conventions.yml
- group: design
  href: https://artifacts.apis.io/loa-healthcare-pricing-api/conventions/loa-healthcare-pricing-api-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/loa-healthcare-pricing-api-conventions.yml
- group: design
  href: https://artifacts.apis.io/loa-healthcare-pricing-api/data-model/loa-healthcare-pricing-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/loa-healthcare-pricing-api-data-model.yml
- group: agent
  href: https://artifacts.apis.io/loa-healthcare-pricing-api/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/loa-healthcare-pricing-api/plans/loa-healthcare-pricing-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/loa-healthcare-pricing-api-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/loa-healthcare-pricing-api/rate-limits/loa-healthcare-pricing-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/loa-healthcare-pricing-api-rate-limits.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.loacare.com/api-partnership
- group: start
  title: ''
  type: GettingStarted
  url: https://www.loacare.com/provider/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.loacare.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.loacare.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.loacare.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://www.loacare.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://www.loacare.com/sign-in
created: '2026-07-28'
description: Source-labeled U.S. healthcare price transparency API and MCP server. Provides hospital and provider entity search, source-labeled price rows, cross-entity price comparison by CPT/HCPCS, and a reviewed update-submission workflow. Data comes from 6,000+ hospital Machine Readable Files under the federal Hospital Price Transparency Rule plus CMS NPI Registry and Loa-reviewed provider submissions.
finops:
- has_sources: true
  method: derived
  name: Loa Healthcare Pricing Api Finops
  primary_unit: ''
  service_category: ''
  slug: loa-healthcare-pricing-api-finops
  template: true
image: https://www.loacare.com/logos/Loa_logo.png
layout: provider
mcp_servers:
- description: ''
  name: Loa Healthcare Pricing API MCP Server
  slug: mcp
modified: '2026-09-03'
name: Loa Healthcare Pricing API
nav: Providers
network: true
overview: 'Loa Healthcare Pricing API publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Entities API, Entity Analytics API, Entity Updates API, and 2 more. Tagged areas include Healthcare, Price Transparency, medical pricing, Hospitals, and Providers.


  The Loa Healthcare Pricing API catalog on APIs.io includes 1 Spectral governance ruleset.


  Loa Healthcare Pricing API''s developer surface includes authentication, getting-started guide, pricing, signup flow, and 19 more developer resources.'
plans:
- name: Loa Healthcare Pricing Api Plans Pricing
  plan_count: 2
  slug: loa-healthcare-pricing-api-plans-pricing
- name: Loa Healthcare Pricing Api Price Estimates
  plan_count: 0
  slug: loa-healthcare-pricing-api-price-estimates
random_paper: 10
rate_limits:
- limit_count: 0
  name: Loa Healthcare Pricing Api Rate Limits
  slug: loa-healthcare-pricing-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Loa Healthcare Pricing API API Rules
  rule_count: 63
  severity_counts:
    error: 57
    hint: 0
    info: 3
    warn: 3
  slug: loa-healthcare-pricing-api-rules
scopes:
- name: Loa Healthcare Pricing Api Scopes
  scope_count: 3
  slug: loa-healthcare-pricing-api-scopes
  summary_line: 3 scopes
score:
  band: developing
  composite: 50.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 52.2
    developer_ergonomics: 44.6
    discoverability: 75.0
    operational_transparency: 0.0
  previous_composite: 48.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/loa-healthcare-pricing-api/loa-healthcare-pricing-api-2026-08-07T171743.png
security:
- kind: authentication
  name: Loa Healthcare Pricing Api Authentication
  slug: loa-healthcare-pricing-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Loa Healthcare Pricing Api Domain Security
  slug: loa-healthcare-pricing-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: compare-procedure-prices
  slug: loa-healthcare-pricing-api-compare-procedure-prices
- name: find-entity-prices
  slug: loa-healthcare-pricing-api-find-entity-prices
- name: submit-price-correction
  slug: loa-healthcare-pricing-api-submit-price-correction
slug: loa-healthcare-pricing-api
tags:
- Healthcare
- Price Transparency
- medical pricing
- Hospitals
- Providers
- Provider Directory
- hospital prices
- CPT
- HCPCS
- MCP
- Agent-Native
- OpenAPI
- Llms.txt
website: https://www.loacare.com
---
