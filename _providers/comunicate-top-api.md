---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 57.0
  scored_at: '2026-09-12'
api_count: 1
apis:
- description: 'REST API for press-release/advertorial distribution: free keyless public routes (niches, stats, market statistics) plus authenticated partner routes for articles, media, publications, editorial orders'
  name: Comunicate.top API
  slug: comunicatetop-api
artifact_total: 8
asyncapis:
- description: ''
  name: Comunicate Top Api Webhooks
  slug: comunicate-top-api-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://comunicate.top
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/comunicate-top-api-tool-crosswalk.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/comunicate-top-api-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/comunicate-top-api-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/comunicate-top-api-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/comunicate-top-api-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/comunicate-top-api-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/comunicate-top-api-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/comunicate-top-api-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/comunicate-top-api-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/comunicate-top-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/comunicate-top-api-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/comunicate-top-api-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/comunicate-top-api-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/comunicate-top-api-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/comunicate-top-api-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/comunicate-top-api-packages.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://comunicate.top/ro/preturi
- group: start
  title: ''
  type: SignUp
  url: https://app.comunicate.top/ro/inregistrare
- group: start
  title: ''
  type: Login
  url: https://app.comunicate.top/ro/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://comunicate.top/ro/legal/termeni
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://comunicate.top/ro/legal/confidentialitate
- group: operate
  title: ''
  type: Support
  url: https://comunicate.top/ro/contact
- group: company
  title: ''
  type: Blog
  url: https://comunicate.top/ro/blog
created: '2026-09-08'
description: Romanian press-release and advertorial distribution platform exposing a REST API (with free keyless public read routes and authenticated partner routes), an OpenAPI 3.1 contract, an llms.txt, and a hosted MCP server for agent-native access to catalogue search, drafting, editorial planning, and publication ordering.
image: https://comunicate.top/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: Comunicate.top API MCP Server
  slug: comunicatetop-api-mcp-server
modified: '2026-09-09'
name: Comunicate.top API
nav: Providers
network: true
overview: 'Comunicate.top API publishes 1 API on the [APIs.io](https://apis.io/) network: Comunicate.top API. Tagged areas include Press Releases, Advertorials, PR, Publishing, and Media.


  The Comunicate.top API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Comunicate.top API''s developer surface includes authentication, pricing, signup flow, support, engineering blog, and 20 more developer resources.'
plans:
- name: Comunicate Top Api Plans Pricing
  plan_count: 0
  slug: comunicate-top-api-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Comunicate Top Api Rate Limits
  slug: comunicate-top-api-rate-limits
scopes:
- name: Comunicate Top Api Scopes
  scope_count: 10
  slug: comunicate-top-api-scopes
  summary_line: 10 scopes · authorizationCode
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 22.4
    contract_governance: 4.5
    contract_quality: 47.2
    developer_ergonomics: 33.9
    discoverability: 75.9
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 39.6
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Comunicate Top Api Authentication
  slug: comunicate-top-api-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Comunicate Top Api Domain Security
  slug: comunicate-top-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: comunicate-top-api
tags:
- Press Releases
- Advertorials
- PR
- Publishing
- Media
- SEO
- Link Building
- Content Marketing
- Romania
- MCP
- Open Data
- Webhooks
- OAuth
website: https://comunicate.top
---
