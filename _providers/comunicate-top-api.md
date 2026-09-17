---
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
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 62.0
  scored_at: '2026-09-16'
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
artifact_total: 18
asyncapis:
- description: ''
  name: Comunicate Top Api Webhooks
  slug: comunicate-top-api-webhooks
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://app.comunicate.top/mcp
- group: company
  title: ''
  type: Website
  url: https://comunicate.top
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/comunicate-top-api/refs/heads/main/mcp/comunicate-top-api-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/comunicate-top-api-tool-crosswalk.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/comunicate-top-api/refs/heads/main/security/comunicate-top-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/comunicate-top-api-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/comunicate-top-api/refs/heads/main/scopes/comunicate-top-api-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/comunicate-top-api-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/comunicate-top-api/refs/heads/main/authentication/comunicate-top-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/comunicate-top-api-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/comunicate-top-api/refs/heads/main/well-known/comunicate-top-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/comunicate-top-api-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/comunicate-top-api/refs/heads/main/asyncapi/comunicate-top-api-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/comunicate-top-api-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/comunicate-top-api/refs/heads/main/errors/comunicate-top-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/comunicate-top-api-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/comunicate-top-api/refs/heads/main/conventions/comunicate-top-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/comunicate-top-api-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/comunicate-top-api/refs/heads/main/conventions/comunicate-top-api-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/comunicate-top-api-conventions.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/comunicate-top-api/refs/heads/main/plans/comunicate-top-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/comunicate-top-api-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/comunicate-top-api/refs/heads/main/rate-limits/comunicate-top-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/comunicate-top-api-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/comunicate-top-api/refs/heads/main/lifecycle/comunicate-top-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/comunicate-top-api-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/comunicate-top-api/refs/heads/main/conformance/comunicate-top-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/comunicate-top-api-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/comunicate-top-api/refs/heads/main/overlays/comunicate-top-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/comunicate-top-api-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/comunicate-top-api/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/comunicate-top-api/refs/heads/main/data-model/comunicate-top-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/comunicate-top-api-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/comunicate-top-api/refs/heads/main/packages/comunicate-top-api-packages.yml
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
overview: 'Comunicate.top API publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Articles API, Balance and reports API, Campaigns API, and 8 more. Tagged areas include Press Releases, Advertorials, PR, Publishing, and Media.


  The Comunicate.top API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Comunicate.top API''s developer surface includes authentication, pricing, signup flow, support, engineering blog, and 21 more developer resources.'
plans:
- name: Comunicate Top Api Plans Pricing
  plan_count: 0
  slug: comunicate-top-api-plans-pricing
random_paper: 3
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
  composite: 44.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.0
  facets:
    access_clarity: 22.4
    contract_governance: 4.5
    contract_quality: 67.2
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
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: rising
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
- Webhook
- Authentication
website: https://comunicate.top
---
