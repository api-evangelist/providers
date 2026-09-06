---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.3
  scored_at: '2026-09-05'
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
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: company
  title: ''
  type: Website
  url: https://www.loacare.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loa-healthcare-pricing-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/loa-healthcare-pricing-api-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/loa-healthcare-pricing-api-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/loa-healthcare-pricing-api-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/loa-healthcare-pricing-api-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/loa-healthcare-pricing-api-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/loa-healthcare-pricing-api-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/loa-healthcare-pricing-api-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/loa-healthcare-pricing-api-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/loa-healthcare-pricing-api-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/loa-healthcare-pricing-api-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/loa-healthcare-pricing-api-plans-pricing.yml
- group: operate
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
image: https://www.loacare.com/logos/Loa_logo.png
layout: provider
mcp_servers:
- description: ''
  name: Loa Healthcare Pricing API MCP Server
  slug: loa-healthcare-pricing-api-mcp-server
- description: ''
  name: LOA Healthcare Pricing
  slug: loa-healthcare-pricing
modified: '2026-09-03'
name: Loa Healthcare Pricing API
nav: Providers
network: true
overview: 'Loa Healthcare Pricing API publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Entities API, Entity Analytics API, Entity Updates API, and 1 more. Tagged areas include Healthcare, Price Transparency, medical pricing, Hospitals, and Providers.


  Loa Healthcare Pricing API''s developer surface includes authentication, getting-started guide, pricing, signup flow, and 18 more developer resources.'
plans:
- name: Loa Healthcare Pricing Api Plans Pricing
  plan_count: 2
  slug: loa-healthcare-pricing-api-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Loa Healthcare Pricing Api Rate Limits
  slug: loa-healthcare-pricing-api-rate-limits
scopes:
- name: Loa Healthcare Pricing Api Scopes
  scope_count: 0
  slug: loa-healthcare-pricing-api-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 52.2
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 47.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loa-healthcare-pricing-api/refs/heads/main/screenshots/loa-healthcare-pricing-api-2026-08-07T171743.png
security:
- kind: authentication
  name: Loa Healthcare Pricing Api Authentication
  slug: loa-healthcare-pricing-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Loa Healthcare Pricing Api Domain Security
  slug: loa-healthcare-pricing-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
- agent-native
- OpenAPI
- llms-txt
website: https://www.loacare.com
---
