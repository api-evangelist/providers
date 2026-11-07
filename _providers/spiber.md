---
access_model:
  confidence: low
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
    agent_skills: false
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Spiber website at spiber.xsrv.jp/api: the route index of the site''s content management system, catalogued as one site surface rather than as separate API'
  name: Spiber Website (WordPress REST)
  slug: spiber-xsrv-jp-api-website-wordpress-rest
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://spiber.inc/en
- group: company
  title: ''
  type: About
  url: https://spiber.inc/en/about
- group: company
  title: ''
  type: Blog
  url: https://spiber.inc/en/news
- group: company
  title: ''
  type: BlogRSS
  url: https://spiber.inc/en/news/feed
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spiber.inc/en/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://spiber.inc/en/cookie-policy
- group: company
  title: ''
  type: Careers
  url: https://spiber.inc/en/careers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Spiber
- group: other
  title: ''
  type: Sustainability
  url: https://spiber.inc/en/sustainability
- group: other
  title: ''
  type: Research
  url: https://spiber.inc/en/academic-papers
- group: agent
  href: https://artifacts.apis.io/spiber/llms/spiber-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/spiber-llms.txt
- group: auth
  href: https://artifacts.apis.io/spiber/security/spiber-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/spiber-domain-security.yml
- group: design
  href: https://artifacts.apis.io/spiber/lifecycle/spiber-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/spiber-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/spiber/conformance/spiber-conformance.yml
  title: ''
  type: Conformance
  url: conformance/spiber-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/spiber/plans/spiber-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/spiber-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/spiber/packages/spiber-packages.yml
  title: ''
  type: Packages
  url: packages/spiber-packages.yml
- group: auth
  href: https://artifacts.apis.io/spiber/authentication/spiber-authentication.yml
  title: ''
  type: Authentication
  url: authentication/spiber-authentication.yml
- group: design
  href: https://artifacts.apis.io/spiber/conventions/spiber-conventions.yml
  title: ''
  type: Conventions
  url: conventions/spiber-conventions.yml
- group: design
  href: https://artifacts.apis.io/spiber/errors/spiber-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/spiber-problem-types.yml
- group: design
  href: https://artifacts.apis.io/spiber/data-model/spiber-data-model.yml
  title: ''
  type: DataModel
  url: data-model/spiber-data-model.yml
- group: operate
  href: https://artifacts.apis.io/spiber/rate-limits/spiber-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/spiber-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/spiber/mcp/spiber-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/spiber-mcp.yml
coverage:
  checked: '2026-08-29'
  detail: Spiber manufactures Brewed Protein fiber, resin and film by precision fermentation and sells it to apparel and automotive brands under supply agreements, so it publishes no developer program at all; the only machine-readable HTTP surface on any Spiber host is the unadvertised read-only WordPress REST backend that renders spiber.inc, which serves every response with X-Robots-Tag noindex and has no reference documentation.
  evidence:
  - status: 404
    url: https://spiber.inc/developers
  - status: 404
    url: https://spiber.inc/openapi.json
  - status: 404
    url: https://spiber.inc/.well-known/agent-card.json
  - status: 200
    url: https://spiber.xsrv.jp/api/wp-json/
  - status: 200
    url: https://api.github.com/orgs/Spiber
  reason: not-a-software-company
  state: none
created: '2026-08-28'
description: Spiber Inc. is a Japanese biotechnology and advanced-materials company founded in 2007 and headquartered in Tsuruoka, Yamagata Prefecture, Japan. Spiber develops Brewed Protein materials — structural proteins produced by precision fermentation of plant-derived sugars using engineered microbes, then spun into fibers, resins, and films as animal-free, petroleum-free alternatives to silk, wool, cashmere, leather, and synthetic polymers. The company operates fermentation plants in Japan, Thailand, and the United States and supplies apparel, outdoor, automotive, and consumer brands, alongside a research program in synthetic biology, polymer science, and life-cycle assessment. Spiber is a materials manufacturer rather than a software vendor and publishes no developer program, developer portal, SDKs, or product API; the only machine-readable HTTP surface it serves is the read-only WordPress REST content API behind its corporate website.
image: https://spiber.inc/en/opengraph-image.jpeg
layout: provider
modified: '2026-08-29'
name: Spiber
nav: Providers
network: true
overview: 'Spiber is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Materials Science, Synthetic Biology, and Manufacturing.


  Spiber''s developer surface includes engineering blog, authentication, and 20 more developer resources.'
plans:
- name: Spiber Plans Pricing
  plan_count: 0
  slug: spiber-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Spiber Rate Limits
  slug: spiber-rate-limits
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 64.3
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 16.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/spiber/spiber-2026-09-02T160423.png
security:
- kind: authentication
  name: Spiber Authentication
  slug: spiber-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Spiber Domain Security
  slug: spiber-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spiber
tags:
- Company
- Biotechnology
- Materials Science
- Synthetic Biology
- Manufacturing
- Sustainability
- Textiles
- Precision Fermentation
- Japan
website: https://spiber.inc/en
---
