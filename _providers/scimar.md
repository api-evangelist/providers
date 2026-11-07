---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'Two Model Context Protocol endpoints advertised in the scimar.ca WordPress REST route index under the "mcp" namespace — /wp-json/mcp/mcp-oauth-server and /wp-json/mcp/mcp-adapter-default-server. Both '
  name: Scimar MCP Server (WordPress MCP Adapter)
  slug: mcp
- description: 'The public WordPress REST API (wp-json) of the Scimar website at scimar.ca: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Scimar Website (WordPress REST)
  slug: scimar-ca-website-wordpress-rest
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://scimar.ca/
- group: company
  title: ''
  type: About
  url: https://scimar.ca/about/
- group: company
  title: ''
  type: Blog
  url: https://scimar.ca/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://scimar.ca/feed/
- group: company
  title: ''
  type: News
  url: https://scimar.ca/news/
- group: company
  title: ''
  type: Press
  url: https://scimar.ca/about/media/
- group: operate
  title: ''
  type: Support
  url: https://scimar.ca/about/contact/
- group: other
  title: ''
  type: Team
  url: https://scimar.ca/team/
- group: other
  title: ''
  type: Technology
  url: https://scimar.ca/science-products/the-science/
- group: other
  title: ''
  type: Pipeline
  url: https://scimar.ca/science-products/product-pipeline/
- group: operate
  title: ''
  type: Community
  url: https://scimar.ca/community/
- group: learn
  title: ''
  type: Videos
  url: https://scimar.ca/videos/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scimar.ca/about/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scimar.ca/about/privacy/
- group: other
  title: ''
  type: Accessibility
  url: https://scimar.ca/about/accessibility/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/698875/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/SciMarL
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/scimar-stock
- group: agent
  href: https://artifacts.apis.io/scimar/llms/scimar-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scimar-llms.txt
- group: agent
  href: https://artifacts.apis.io/scimar/well-known/scimar-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scimar-well-known.yml
- group: build
  href: https://artifacts.apis.io/scimar/packages/scimar-packages.yml
  title: ''
  type: Packages
  url: packages/scimar-packages.yml
- group: auth
  href: https://artifacts.apis.io/scimar/authentication/scimar-authentication.yml
  title: ''
  type: Authentication
  url: authentication/scimar-authentication.yml
- group: design
  href: https://artifacts.apis.io/scimar/conventions/scimar-conventions.yml
  title: ''
  type: Conventions
  url: conventions/scimar-conventions.yml
- group: design
  href: https://artifacts.apis.io/scimar/conformance/scimar-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scimar-conformance.yml
- group: design
  href: https://artifacts.apis.io/scimar/errors/scimar-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/scimar-problem-types.yml
- group: design
  href: https://artifacts.apis.io/scimar/data-model/scimar-data-model.yml
  title: ''
  type: DataModel
  url: data-model/scimar-data-model.yml
- group: design
  href: https://artifacts.apis.io/scimar/lifecycle/scimar-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/scimar-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/scimar/security/scimar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scimar-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/scimar/plans/scimar-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/scimar-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/scimar/rate-limits/scimar-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/scimar-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/scimar/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/scimar/overlays/scimar-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/scimar-content-overlay.yaml
created: '2026-08-26'
description: 'Scimar (Scimar Ltd., formerly styled SciMar) is a privately held Canadian life-sciences company founded in 2009 with its head office in Dauphin, Manitoba and research laboratories in Winnipeg. It commercializes the work of co-founder and Chief Scientific Officer Dr. W. Wayne Lautt, who in 1996 identified hepatalin — known in the literature as hepatic insulin-sensitizing substance, or HISS — a liver hormone Scimar describes as the missing link in nutrient partitioning, prediabetes and type 2 diabetes. Its pipeline pairs diagnostics with therapeutics: SciMar NuPa Test, a diagnostic test meal that measures hepatalin production and is in Phase 2 clinical trials in Canada; SciMar NuPa Renew, a pre-meal pharmaceutical preparing for Phase 2B; SciMar NuPa Daily, an antioxidant supplement intended to protect hepatalin production; and Hepatalin-S, a synthetic hepatalin for advanced-stage disease. Alongside the science the company runs the Wellness Transformation Network, a community
  outreach program with nonprofits, Indigenous communities and Manitoba businesses, and produces the Webby-nominated science podcast Inside the Breakthrough hosted by Dan Riskin. Scimar publishes no product or developer API and operates no developer program. The machine-readable surface on scimar.ca is CMS-provided: a served llms.txt generated by All in One SEO, the anonymously readable WordPress REST API (wp/v2) that returns news stories, pages, team profiles, media and site search as JSON, and a WordPress MCP Adapter that advertises two Model Context Protocol endpoints plus RFC 8414 and RFC 9728 OAuth discovery documents — all of which are authentication-gated.'
image: https://scimar.ca/wp-content/uploads/2022/11/scimar-logo.svg
layout: provider
mcp_servers:
- description: 'scimar.ca runs the WordPress MCP Adapter. The "mcp" namespace is registered in the site''s WordPress REST route index alongside wp-abilities/v1 (the adapter''s backing ability registry) and exposes TWO '
  name: Scimar MCP Server
  slug: scimar-mcp-yml
modified: '2026-08-26'
name: Scimar
nav: Providers
network: true
overview: 'Scimar is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Pharmaceuticals, and Diabetes.


  Scimar''s developer surface includes engineering blog, product news, support, authentication, and 28 more developer resources.'
plans:
- name: Scimar Plans Pricing
  plan_count: 0
  slug: scimar-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Scimar Rate Limits
  slug: scimar-rate-limits
scopes:
- name: Scimar Scopes
  scope_count: 1
  slug: scimar-scopes
  summary_line: 1 scope
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 1.7
    developer_ergonomics: 25.6
    discoverability: 68.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 21.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: site-plugin
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/scimar/scimar-2026-09-02T154535.png
security:
- kind: authentication
  name: Scimar Authentication
  slug: scimar-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Scimar Domain Security
  slug: scimar-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 2
skills:
- name: Read the Scimar news archive and science pages
  slug: scimar-read-news-and-science
- name: Search scimar.ca and resolve results
  slug: scimar-search-the-site
slug: scimar
tags:
- Company
- Biotechnology
- Life Sciences
- Pharmaceuticals
- Diabetes
- Diagnostics
- Clinical Trials
- Health
- Nutrition
- Research
- Canada
- Content
website: https://scimar.ca/
---
