---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.6
  scored_at: '2026-09-03'
api_count: 14
apis:
- baseURL: https://www.habiteo.com/wp-json
  baseurl_source: declared
  description: News and blog posts published on habiteo.com, plus their revisions. DERIVED by API Evangelist from the WordPress REST route index at https://www.habiteo.com/wp-json/ — this is the CMS content API behi
  name: Habiteo Site Content API — Posts API
  slug: posts-api
- baseURL: https://www.habiteo.com/wp-json
  baseurl_source: declared
  description: Marketing and product pages of habiteo.com, plus their revisions. DERIVED by API Evangelist from the WordPress REST route index at https://www.habiteo.com/wp-json/ — this is the CMS content API behind
  name: Habiteo Site Content API — Pages API
  slug: pages-api
- baseURL: https://www.habiteo.com/wp-json
  baseurl_source: declared
  description: The WordPress media library behind habiteo.com — images and documents. DERIVED by API Evangelist from the WordPress REST route index at https://www.habiteo.com/wp-json/ — this is the CMS content API b
  name: Habiteo Site Content API — Media API
  slug: media-api
- baseURL: https://www.habiteo.com/wp-json
  baseurl_source: declared
  description: The `portfolio` custom post type used for Habiteo client and project showcases. DERIVED by API Evangelist from the WordPress REST route index at https://www.habiteo.com/wp-json/ — this is the CMS cont
  name: Habiteo Site Content API — Portfolio API
  slug: portfolio-api
- baseURL: https://www.habiteo.com/wp-json
  baseurl_source: declared
  description: The `uncodeblock` custom post type from the Uncode theme — reusable page blocks. DERIVED by API Evangelist from the WordPress REST route index at https://www.habiteo.com/wp-json/ — this is the CMS con
  name: Habiteo Site Content API — Blocks API
  slug: blocks-api
- baseURL: https://www.habiteo.com/wp-json
  baseurl_source: declared
  description: Categories, tags, portfolio categories and the taxonomy registry. DERIVED by API Evangelist from the WordPress REST route index at https://www.habiteo.com/wp-json/ — this is the CMS content API behind
  name: Habiteo Site Content API — Taxonomy API
  slug: taxonomy-api
- baseURL: https://www.habiteo.com/wp-json
  baseurl_source: declared
  description: The wp-json route index and the registered post types and statuses — the route-discovery surface this profile was derived from. DERIVED by API Evangelist from the WordPress REST route index at https:/
  name: Habiteo Site Content API — Discovery API
  slug: discovery-api
- baseURL: https://www.habiteo.com/wp-json
  baseurl_source: declared
  description: 'Post authors exposed by the WordPress users route. Read-only for anonymous callers. DERIVED by API Evangelist from the WordPress REST route index at https://www.habiteo.com/wp-json/ — this is the CMS '
  name: Habiteo Site Content API — Users API
  slug: users-api
- baseURL: https://www.habiteo.com/wp-json
  baseurl_source: declared
  description: Site comments. The comment collection is anonymously readable. DERIVED by API Evangelist from the WordPress REST route index at https://www.habiteo.com/wp-json/ — this is the CMS content API behind th
  name: Habiteo Site Content API — Comments API
  slug: comments-api
- baseURL: https://www.habiteo.com/wp-json
  baseurl_source: declared
  description: Site settings. Anonymous calls return HTTP 403 rest_forbidden — recorded as a gated route, not a readable one. DERIVED by API Evangelist from the WordPress REST route index at https://www.habiteo.com/
  name: Habiteo Site Content API — Settings API
  slug: settings-api
- baseURL: https://www.habiteo.com/wp-json
  baseurl_source: declared
  description: 'The WordPress oEmbed provider endpoint for habiteo.com URLs. DERIVED by API Evangelist from the WordPress REST route index at https://www.habiteo.com/wp-json/ — this is the CMS content API behind the '
  name: Habiteo Site Content API — oEmbed API
  slug: oembed-api
- description: A second, older JSON surface on www.habiteo.com, served by the WordPress "JSON API" plugin at /api/. GET https://www.habiteo.com/api/ returns {"status":"ok","json_api_version":"1.1.1","controllers":["
  name: Habiteo Site JSON API (WordPress JSON API plugin)
  slug: json-api-plugin
- baseURL: https://www.habiteo.com/wp-json
  baseurl_source: declared
  description: The ContactForms API from Habiteo — 5 operation(s) for contactforms.
  name: Habiteo Contact Forms API
  slug: habiteo-contactforms-api
- baseURL: https://www.habiteo.com/wp-json
  baseurl_source: declared
  description: The SiteTools API from Habiteo — 7 operation(s) for sitetools.
  name: Habiteo Site Tools API
  slug: habiteo-sitetools-api
artifact_total: 18
common:
- group: company
  title: ''
  type: Website
  url: https://www.habiteo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.habiteo.com/fr/actualite-habiteo/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.habiteo.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.habiteo.com/fr/contact/
- group: start
  title: ''
  type: Login
  url: https://my.habiteo.com/connexion
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.habiteo.com/fr/conditions-generales-de-vente/
- group: commercial
  title: ''
  type: LegalNotice
  url: https://www.habiteo.com/fr/mentions-legales/
- group: company
  title: ''
  type: Press
  url: https://www.habiteo.com/fr/presse/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/habiteo-com
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/HabiteoFR
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCXb9wxCl6kie-XcfLfvMGig
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/habiteofr/
- group: other
  title: ''
  type: Overlay
  url: overlays/habiteo-content-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/habiteo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/habiteo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/habiteo-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/habiteo-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/habiteo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/habiteo-lifecycle.yml
- group: design
  title: ''
  type: Components
  url: components/habiteo-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/habiteo-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/habiteo-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-17'
description: 'Habiteo is a French PropTech company founded in 2014 in Paris that builds full-web 3D sales and marketing technology for new-build real estate. Its products let developers, house builders, commercial-property operators and their agencies model a programme in 3D before it is built: 3D floor plans and perspectives, virtual tours, drone-based site insertions and neighbourhood views (Modelisation and myHabiteo Studio), an interior configurator that lets a buyer choose materials and options in place of a physical showroom (Configurateur), a mobile on-site sales unit (Habiteo Truck), and the MegaWidget, a hosted mini-site that gathers every 3D asset for a programme behind a single link. myHabiteo is the operator platform that binds the 3D layer to commercialisation with a CRM, a reservation module, programme management and sales and marketing dashboards. More than 350 developers, including Nexity, Kaufman & Broad and Immobiliere 3F, have used the technology. Habiteo was acquired
  by the French listings portal Bien''ici in May 2022 and continues to operate under its own brand. Habiteo publishes no public developer programme, no API documentation and no machine-readable API contract for any of these products; the only anonymously readable machine surface on its domain is the WordPress REST API behind its marketing site.'
image: https://www.habiteo.com/wp-content/uploads/2017/02/Logo_Habiteo_Hz_Bg-transparent-1.png
layout: provider
modified: '2026-08-17'
name: Habiteo
nav: Providers
network: true
overview: 'Habiteo publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Site Content API — Posts API, Site Content API — Pages API, Site Content API — Media API, and 10 more. Tagged areas include Company, Real-Estate, PropTech, 3D Visualization, and Property Marketing.


  Habiteo''s developer surface includes engineering blog, support, YouTube channel, authentication, and 19 more developer resources.'
plans:
- name: Habiteo Plans Pricing
  plan_count: 0
  slug: habiteo-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Habiteo Rate Limits
  slug: habiteo-rate-limits
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 19
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 4.5
    contract_quality: 16.6
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 21.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 15
      marker_coverage: 100.0
      total: 15
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/habiteo/refs/heads/main/screenshots/habiteo-2026-09-02T145647.png
security:
- kind: authentication
  name: Habiteo Authentication
  slug: habiteo-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Habiteo Domain Security
  slug: habiteo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: habiteo
tags:
- Company
- Real-Estate
- PropTech
- 3D Visualization
- Property Marketing
- Configurator
- CRM
- France
- Content
- WordPress
website: https://www.habiteo.com/
---
