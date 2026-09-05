---
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://southendonsea.city/
  baseurl_source: declared
  description: Current and archived source-linked city observations
  name: SouthendOnSea.city Southend Now API
  slug: southendonsea-southend-now-api
artifact_total: 7
common:
- group: agent
  title: ''
  type: WellKnown
  url: well-known/southendonsea-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/southendonsea-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/southendonsea-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/southendonsea-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/southendonsea-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/southendonsea-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/southendonsea-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: https://southendonsea.city/contact
- group: auth
  title: ''
  type: DomainSecurity
  url: security/southendonsea-domain-security.yml
- group: other
  title: ''
  type: APIsJSON
  url: https://southendonsea.city/.well-known/apis.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/southendonsea-llms.txt
- group: company
  title: ''
  type: Website
  url: https://southendonsea.city
- group: docs
  title: ''
  type: Documentation
  url: https://southendonsea.city/data/reuse
- group: commercial
  title: ''
  type: TermsOfService
  url: https://southendonsea.city/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://southendonsea.city/privacy
created: '2026-08-23'
description: 'SouthendOnSea.city is an independent local information and community-participation platform for Southend-on-Sea, Essex, covering local news, community propositions and public voting, city information and the Southend Science Exhibition. Its public data API — Southend Now — serves unauthenticated, source-linked current and historical observations for the area: weather, designated bathing waters, marine conditions, modelled air quality and flood alerts. Three operations return the current snapshot, a JSON history and a CSV history, refreshed on a 1,800-second interval, with source licensing and attribution preserved in the payload. The platform is independent and unofficial and states plainly that it is not operated by Southend-on-Sea City Council, Essex Police or any election authority.'
examples:
- key_count: 9
  name: Southendonsea Now Example
  slug: southendonsea-now-example
image: https://southendonsea.city/southend-city-email-brand.png
layout: provider
mcp_servers:
- description: ''
  name: SouthendOnSea.city MCP Server
  slug: southendonseacity-mcp-server
modified: '2026-09-03'
name: SouthendOnSea.city
nav: Providers
network: true
overview: 'SouthendOnSea.city publishes 1 API on the [APIs.io](https://apis.io/) network: Southend Now API. Tagged areas include Open Data, Southend-on-Sea, Weather, Environment, and local data.


  SouthendOnSea.city''s developer surface includes authentication, support, documentation, and 13 more developer resources.'
plans:
- name: Southendonsea Plans Pricing
  plan_count: 0
  slug: southendonsea-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Southendonsea Rate Limits
  slug: southendonsea-rate-limits
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 47.6
    developer_ergonomics: 35.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 37.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/southendonsea/refs/heads/main/screenshots/southendonsea-2026-09-02T160255.png
security:
- kind: authentication
  name: Southendonsea Authentication
  slug: southendonsea-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Southendonsea Domain Security
  slug: southendonsea-domain-security
  summary_line: TLSv1.3 · HSTS
slug: southendonsea
tags:
- Open Data
- Southend-on-Sea
- Weather
- Environment
- local data
website: https://southendonsea.city
---
