---
access_model:
  confidence: low
  gated_conflict: 'x-api-posture: private but 2 published API entries'
  label: Unknown
  onboarding: unknown
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 11.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: A first-party application backend on api.wowmomo.com behind an AWS Application Load Balancer, running an Express service scaffolded with DhiWise (its root serves a "welcome to node.js" page carrying t
  name: WOW! Momo App Backend
  slug: wow-momo-app-backend
- description: 'The public WordPress REST API (wp-json) of the WOW! Momo website at www.wowmomo.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate API'
  name: WOW! Momo Website (WordPress REST)
  slug: wowmomo-com-website-wordpress-rest
artifact_total: 10
common:
- group: auth
  href: https://artifacts.apis.io/wow-momo/security/wow-momo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wow-momo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wowmomo.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wowmomo.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wowmomo.com/privacy/
- group: other
  title: ''
  type: Franchise
  url: https://www.wowmomo.com/franchise-form/
- group: other
  title: ''
  type: StoreLocator
  url: https://restaurants.wowmomo.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.wowmomo.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://in.linkedin.com/company/wow-momo
- group: docs
  href: https://artifacts.apis.io/wow-momo/openapi/_ae-authored/wow-momo-content-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_ae-authored/wow-momo-content-api-openapi.yml
- group: other
  href: https://artifacts.apis.io/wow-momo/overlays/wow-momo-content-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/wow-momo-content-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/wow-momo/llms/wow-momo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wow-momo-llms.txt
- group: agent
  href: https://artifacts.apis.io/wow-momo/mcp/wow-momo-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/wow-momo-mcp.yml
- group: agent
  href: https://artifacts.apis.io/wow-momo/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/wow-momo/authentication/wow-momo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wow-momo-authentication.yml
- group: design
  href: https://artifacts.apis.io/wow-momo/conventions/wow-momo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wow-momo-conventions.yml
- group: design
  href: https://artifacts.apis.io/wow-momo/errors/wow-momo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wow-momo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/wow-momo/data-model/wow-momo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wow-momo-data-model.yml
- group: design
  href: https://artifacts.apis.io/wow-momo/lifecycle/wow-momo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/wow-momo-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/wow-momo/conformance/wow-momo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wow-momo-conformance.yml
- group: build
  href: https://artifacts.apis.io/wow-momo/packages/wow-momo-packages.yml
  title: ''
  type: Packages
  url: packages/wow-momo-packages.yml
- group: commercial
  href: https://artifacts.apis.io/wow-momo/plans/wow-momo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wow-momo-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/wow-momo/rate-limits/wow-momo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/wow-momo-rate-limits.yml
created: '2026-09-04'
description: 'WOW! Momo Foods Private Limited is the Kolkata, India quick-service restaurant company founded in August 2008 by St. Xavier''s College alumni Sagar J. Daryani and Binod K. Homagai, which built a national chain around the momo and now operates three brands — WOW! Momo, WOW! China and WOW! Chicken (launched December 2021) — across roughly 650 outlets in more than 30 Indian cities, backed by Lighthouse Funds, Tiger Global, Khazanah Nasional and Oaks Capital. WOW! Momo runs no developer programme: it publishes no API documentation, developer portal, SDK, API pricing or support channel, and no company-authored OpenAPI, AsyncAPI or GraphQL contract exists anywhere public. It is catalogued here because www.wowmomo.com serves a live, anonymously readable WordPress REST API — advertised in the head of every page as <link rel="https://api.w.org/"> — exposing the site''s pages, media library, taxonomies, search index, oEmbed 1.0 provider endpoint and Yoast SEO head document, alongside
  a separate first-party application backend on api.wowmomo.com that answers every anonymous request, including a control path that cannot exist, with an identical NO_AUTH body.'
image: https://www.wowmomo.com/wp-content/uploads/2022/03/Wow-Momo-Logo.png
layout: provider
modified: '2026-09-04'
name: WOW! Momo
nav: Providers
network: true
overview: 'WOW! Momo is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant, Food and Beverage, Quick Service Restaurant, and Retail.


  The WOW! Momo catalog on APIs.io includes 1 Spectral governance ruleset.


  WOW! Momo''s developer surface includes authentication and 21 more developer resources.'
plans:
- name: Wow Momo Plans Pricing
  plan_count: 0
  slug: wow-momo-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Wow Momo Rate Limits
  slug: wow-momo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: WOW! Momo API Rules
  rule_count: 57
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 6
  slug: wow-momo-rules
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 21.1
    contract_governance: 31.8
    contract_quality: 1.7
    developer_ergonomics: 18.5
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 20.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/wow-momo/wow-momo-2026-10-11T195212.png
security:
- kind: authentication
  name: Wow Momo Authentication
  slug: wow-momo-authentication
  summary_line: http/apiKey/opaque-application-credential · 3 schemes
- kind: domain-security
  name: Wow Momo Domain Security
  slug: wow-momo-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Embed a WOW! Momo page and read its SEO graph
  slug: wow-momo-embed-and-describe
- name: Pull WOW! Momo brand and campaign imagery
  slug: wow-momo-pull-brand-assets
- name: Read the WOW! Momo site through its API
  slug: wow-momo-read-the-site
slug: wow-momo
tags:
- Company
- Restaurant
- Food and Beverage
- Quick Service Restaurant
- Retail
- Hospitality
- Consumer
- Franchising
- Content
- WordPress
- oEmbed
- India
- Kolkata
website: https://www.wowmomo.com/
---
