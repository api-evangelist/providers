---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: The stock WordPress REST API exposed by PlusMargin's marketing site. The root discovery document at /wp-json self-identifies as "Plus Margin" (url https://plusmargin.com) and registers 237 routes acro
  name: PlusMargin WordPress REST API
  slug: wordpress-rest-api
- description: RSS 2.0 syndication feed for PlusMargin's editorial content — Thai-language articles across Marketing, Business, Advertising, Technology, Learning, Insurance, Science and Lifestyle. Served as applicat
  name: PlusMargin RSS Feed
  slug: rss-feed
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://plusmargin.com
- group: company
  title: ''
  type: About
  url: https://plusmargin.com/about/
- group: operate
  title: ''
  type: Contact
  url: https://plusmargin.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://plusmargin.com/privacy-policy/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plusmargin-domain-security.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://plusmargin.com/feed/
- group: other
  title: ''
  type: Sitemap
  url: https://plusmargin.com/sitemap.xml
- group: auth
  title: ''
  type: Authentication
  url: authentication/plusmargin-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/plusmargin-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/plusmargin-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/plusmargin-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/plusmargin-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/plusmargin-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plusmargin-llms.txt
coverage:
  checked: '2026-08-12'
  detail: PlusMargin runs a four-page WordPress consulting site — its own page sitemap lists only /, /about/, /contact/ and /privacy-policy/ — with no developer, API, docs or pricing page, no api/developer/docs subdomain (all NXDOMAIN), and no package on any registry; the only machine-readable surface is the CMS's own /wp-json route index.
  evidence:
  - status: 200
    url: https://plusmargin.com/page-sitemap.xml
  - status: 404
    url: https://plusmargin.com/openapi.json
  - status: 404
    url: https://plusmargin.com/.well-known/agent-card.json
  - status: 404
    url: https://plusmargin.com/llms.txt
  - status: 200
    url: https://plusmargin.com/wp-json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: PlusMargin (Plus Margin) is a Bangkok, Thailand based digital marketing and business consulting practice operating under the tagline "Connect | Engage | Convert." The firm focuses on inbound marketing strategy, personalized and AI-assisted marketing, buyer-persona development, and customer-journey mapping for its clients, and publishes Thai-language editorial content across marketing, business, advertising, technology, learning, insurance, and lifestyle topics. It was surfaced as a portfolio company of 500 Global — where secondary sources describe an earlier Singapore-founded "predictive persuasion" e-commerce personalization product — but the domain today serves a four-page consulting and content site with no trace of that platform. Enrichment on 2026-08-12 confirmed no product API, no developer portal, no SDKs on any package registry, no /.well-known/ discovery surface, no llms.txt and no agent card. The one callable, machine-readable surface is the stock WordPress REST API
  the marketing site exposes at /wp-json — 237 routes across 11 namespaces, anonymously readable for content — which is WordPress core's API rather than a product PlusMargin designed, documents, or supports.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plusmargin.png
layout: provider
modified: '2026-08-12'
name: PlusMargin
nav: Providers
network: true
overview: 'PlusMargin publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Digital Marketing, Consulting, and Advertising.


  PlusMargin''s developer surface includes authentication and 13 more developer resources.'
plans:
- name: Plusmargin Plans Pricing
  plan_count: 0
  slug: plusmargin-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Plusmargin Rate Limits
  slug: plusmargin-rate-limits
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 14.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plusmargin/refs/heads/main/screenshots/plusmargin-2026-09-02T151555.png
security:
- kind: authentication
  name: Plusmargin Authentication
  slug: plusmargin-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Plusmargin Domain Security
  slug: plusmargin-domain-security
  summary_line: TLSv1.3
slug: plusmargin
tags:
- Company
- Marketing
- Digital Marketing
- Consulting
- Advertising
- Customer Engagement
- Thailand
website: https://plusmargin.com
---
