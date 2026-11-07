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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 60.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://app.comunicate.top/api/v1
  baseurl_source: declared
  description: 'An article enters the platform four ways: written by you as HTML, imported from a document, taken from a Drive folder, or written by the platform from a brief. All produce the same thing — a draft tha'
  name: Comunicate.top API Articles API
  slug: comunicate-top-api-articles-api
- baseURL: https://app.comunicate.top/api/v1
  baseurl_source: declared
  description: The Balance and reports API from Comunicate.top API — 3 operation(s) for balance and reports.
  name: Comunicate.top API Balance and reports API
  slug: comunicate-top-api-balance-and-reports-api
- baseURL: https://app.comunicate.top/api/v1
  baseurl_source: declared
  description: Grouping articles and publications by client or project. The equivalent of "projects" on other platforms.
  name: Comunicate.top API Campaigns API
  slug: comunicate-top-api-campaigns-api
- baseURL: https://app.comunicate.top/api/v1
  baseurl_source: declared
  description: Which publications exist, what each campaign type costs, and whether your packages cover them.
  name: Comunicate.top API Catalogue API
  slug: comunicate-top-api-catalogue-api
- baseURL: https://app.comunicate.top/api/v1
  baseurl_source: declared
  description: 'What can be said about an article without calling any model: the SEO analysis and the campaign-type fit. Both are rule-based, so they cost nothing, are not rate-limited, and give the same answer every'
  name: Comunicate.top API Checks API
  slug: comunicate-top-api-checks-api
- baseURL: https://app.comunicate.top/api/v1
  baseurl_source: declared
  description: 'A full check of a domain: PageSpeed on mobile and desktop with every category, real Chrome field data, Safe Browsing, and — when we have access to the property — Search Console.'
  name: Comunicate.top API Domain audit API
  slug: comunicate-top-api-domain-audit-api
- baseURL: https://app.comunicate.top/api/v1
  baseurl_source: declared
  description: 'The first call of any integration: who the key is and what it may do. This is also where you see whether the organisation enabled "AI assistants may order and publish" — the switch that decides what a'
  name: Comunicate.top API Key and permissions API
  slug: comunicate-top-api-key-and-permissions-api
- baseURL: https://app.comunicate.top/api/v1
  baseurl_source: declared
  description: The Media API from Comunicate.top API — 1 operation(s) for media.
  name: Comunicate.top API Media API
  slug: comunicate-top-api-media-api
- baseURL: https://app.comunicate.top/api/v1
  baseurl_source: declared
  description: 'Four routes that work with no key at all: the network’s niches, one niche with sample publications, the catalogue figures and the market statistics. This is the same data the public site shows, served'
  name: Comunicate.top API Public catalogue API
  slug: comunicate-top-api-public-catalogue-api
- baseURL: https://app.comunicate.top/api/v1
  baseurl_source: declared
  description: A publication ties an article to a publisher site. It is the only place in the API that spends credits or money.
  name: Comunicate.top API Publications API
  slug: comunicate-top-api-publications-api
- baseURL: https://app.comunicate.top/api/v1
  baseurl_source: declared
  description: 'The API starts no generation. You place an order, we see it, we write it or decline it with a reason, and you learn the outcome the same way. The reason is simple: a key runs inside a script and can a'
  name: Comunicate.top API Writing orders API
  slug: comunicate-top-api-writing-orders-api
artifact_total: 23
asyncapis:
- description: ''
  name: Comunicate Top Api Webhooks
  slug: comunicate-top-api-webhooks
common:
- group: other
  href: https://artifacts.apis.io/comunicate-top-api/capabilities/comunicate-top-api-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/comunicate-top-api-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://app.comunicate.top/mcp
- group: company
  title: ''
  type: Website
  url: https://comunicate.top
- group: build
  href: https://artifacts.apis.io/comunicate-top-api/mcp/comunicate-top-api-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/comunicate-top-api-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/comunicate-top-api/security/comunicate-top-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/comunicate-top-api-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/comunicate-top-api/scopes/comunicate-top-api-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/comunicate-top-api-scopes.yml
- group: auth
  href: https://artifacts.apis.io/comunicate-top-api/authentication/comunicate-top-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/comunicate-top-api-authentication.yml
- group: agent
  href: https://artifacts.apis.io/comunicate-top-api/well-known/comunicate-top-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/comunicate-top-api-well-known.yml
- group: design
  href: https://artifacts.apis.io/comunicate-top-api/asyncapi/comunicate-top-api-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/comunicate-top-api-webhooks.yml
- group: design
  href: https://artifacts.apis.io/comunicate-top-api/errors/comunicate-top-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/comunicate-top-api-problem-types.yml
- group: design
  href: https://artifacts.apis.io/comunicate-top-api/conventions/comunicate-top-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/comunicate-top-api-conventions.yml
- group: design
  href: https://artifacts.apis.io/comunicate-top-api/conventions/comunicate-top-api-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/comunicate-top-api-conventions.yml
- group: commercial
  href: https://artifacts.apis.io/comunicate-top-api/plans/comunicate-top-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/comunicate-top-api-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/comunicate-top-api/rate-limits/comunicate-top-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/comunicate-top-api-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/comunicate-top-api/lifecycle/comunicate-top-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/comunicate-top-api-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/comunicate-top-api/conformance/comunicate-top-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/comunicate-top-api-conformance.yml
- group: other
  href: https://artifacts.apis.io/comunicate-top-api/overlays/comunicate-top-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/comunicate-top-api-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/comunicate-top-api/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/comunicate-top-api/data-model/comunicate-top-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/comunicate-top-api-data-model.yml
- group: build
  href: https://artifacts.apis.io/comunicate-top-api/packages/comunicate-top-api-packages.yml
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
finops:
- has_sources: true
  method: derived
  name: Comunicate Top Api Finops
  primary_unit: publicare
  service_category: ''
  slug: comunicate-top-api-finops
  template: false
image: https://comunicate.top/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: Comunicate.top API MCP Server
  slug: mcp
modified: '2026-09-09'
name: Comunicate.top API
nav: Providers
network: true
overview: 'Comunicate.top API publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Articles API, Balance and reports API, Campaigns API, and 8 more. Tagged areas include Press Releases, Advertorials, PR, Publishing, and Media.


  The Comunicate.top API catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Comunicate.top API''s developer surface includes authentication, pricing, signup flow, support, engineering blog, and 22 more developer resources.'
plans:
- name: Comunicate Top Api Plans Pricing
  plan_count: 21
  slug: comunicate-top-api-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Comunicate Top Api Rate Limits
  slug: comunicate-top-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Comunicate.top API API Rules
  rule_count: 62
  severity_counts:
    error: 55
    hint: 0
    info: 4
    warn: 3
  slug: comunicate-top-api-rules
scopes:
- name: Comunicate Top Api Scopes
  scope_count: 10
  slug: comunicate-top-api-scopes
  summary_line: 10 scopes · authorizationCode
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 28
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 61.8
    contract_governance: 18.2
    contract_quality: 67.2
    developer_ergonomics: 33.9
    discoverability: 75.0
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - romania
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 49.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/comunicate-top-api/comunicate-top-api-2026-10-11T103204.png
security:
- kind: authentication
  name: Comunicate Top Api Authentication
  slug: comunicate-top-api-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Comunicate Top Api Domain Security
  slug: comunicate-top-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Create an article and order its publication
  slug: comunicate-top-api-create-article-and-publish
- name: Order a written article and track it to delivery
  slug: comunicate-top-api-order-writing-and-track
- name: Search the Comunicate.top catalogue and price a campaign
  slug: comunicate-top-api-search-catalog-and-price
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
- Webhook
- OAuth
- Authentication
website: https://comunicate.top
---
