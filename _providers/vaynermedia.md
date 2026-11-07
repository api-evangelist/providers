---
access_model:
  confidence: low
  gated_conflict: 'x-api-posture: private but 1 published API entry'
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the VaynerMedia website at vaynermedia.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate A'
  name: VaynerMedia Website (WordPress REST)
  slug: vaynermedia-com-website-wordpress-rest
artifact_total: 8
collections:
- collection_type: open
  name: VaynerMedia WordPress Content API
  slug: open-vaynermedia-wordpress-content
common:
- group: other
  href: https://artifacts.apis.io/vaynermedia/overlays/vaynermedia-wordpress-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/vaynermedia-wordpress-content-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/vaynermedia/authentication/vaynermedia-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vaynermedia-authentication.yml
- group: auth
  href: https://artifacts.apis.io/vaynermedia/security/vaynermedia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vaynermedia-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/vaynermedia/llms/vaynermedia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vaynermedia-llms.txt
- group: agent
  href: https://artifacts.apis.io/vaynermedia/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/vaynermedia/conventions/vaynermedia-conventions.yml
  title: ''
  type: Conventions
  url: conventions/vaynermedia-conventions.yml
- group: design
  href: https://artifacts.apis.io/vaynermedia/errors/vaynermedia-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vaynermedia-problem-types.yml
- group: design
  href: https://artifacts.apis.io/vaynermedia/lifecycle/vaynermedia-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/vaynermedia-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/vaynermedia/rate-limits/vaynermedia-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vaynermedia-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/vaynermedia/plans/vaynermedia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vaynermedia-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/vaynermedia/conformance/vaynermedia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vaynermedia-conformance.yml
- group: design
  href: https://artifacts.apis.io/vaynermedia/data-model/vaynermedia-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vaynermedia-data-model.yml
- group: company
  title: ''
  type: Website
  url: https://vaynermedia.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://vaynermedia.com/llms.txt
- group: other
  title: ''
  type: Services
  url: https://vaynermedia.com/integrated/
- group: other
  title: ''
  type: CaseStudies
  url: https://vaynermedia.com/work/
- group: company
  title: ''
  type: Blog
  url: https://vaynermedia.com/blog/
- group: other
  title: ''
  type: Research
  url: https://vaynermedia.com/reports/
- group: company
  title: ''
  type: Careers
  url: https://vaynermedia.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://vaynermedia.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vaynermedia.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vaynermedia.com/privacy-policy/
- group: other
  title: ''
  type: RSSFeed
  url: https://vaynermedia.com/feed/
- group: other
  title: ''
  type: Sitemap
  url: https://vaynermedia.com/sitemap_index.xml
- group: other
  title: ''
  type: ParentCompany
  url: https://vaynerx.com/
- group: other
  title: ''
  type: SisterCompany
  url: https://gallerymediagroup.com/
- group: other
  title: ''
  type: SisterCompany
  url: https://chukmedia.com/
- group: other
  title: ''
  type: SisterCompany
  url: https://tamaragroup.com/
- group: other
  title: ''
  type: SisterCompany
  url: https://evanosidam.com/
- group: other
  title: ''
  type: SisterCompany
  url: https://vaynerspeakers.com/
- group: other
  title: ''
  type: SisterCompany
  url: https://tingleylane.com/
- group: other
  title: ''
  type: Podcast
  url: https://vaynerx.com/marketing-for-the-now/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vaynermedia
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vaynerx
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vaynermedia
- group: other
  title: ''
  type: X
  url: https://x.com/vaynermedia
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/vaynermedia/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/vaynermedia
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/vaynermedia
created: '2026-05-23'
description: 'VaynerMedia is an integrated strategy, creative, and media agency founded by Gary Vaynerchuk, positioning itself as "The Modern Agency of Record" with social media at the center of its practice. Headquartered in New York with roughly 2,000 employees across offices in Los Angeles, Chattanooga, Chicago, Miami, Toronto, Amsterdam, London, Mexico City, Sydney, Mumbai, Tokyo, Kuala Lumpur, Singapore, and Bangkok, the agency serves clients including Bose, Coach, Diageo, Duracell, Indeed, Jimmy John''s, Meta, Mondelez, NatWest, PepsiCo, Tinder, and Wingstop. VaynerMedia is the flagship brand of holding company VaynerX, whose portfolio also includes Gallery Media Group, ChukMedia, Tamara Group, Eva Nosidam Productions, VaynerSpeakers, Tingley Lane, and the Marketing for the Now podcast. VaynerMedia is a services agency, not an API or platform company — it does not publish a developer API, SDK, or public technology product, and its public GitHub presence (github.com/vaynermedia and
  github.com/vaynerx) consists primarily of forked open source libraries and internal build tooling rather than maintained API products. The one machine-readable surface VaynerMedia does serve is its own website: vaynermedia.com runs on self-hosted WordPress at WP Engine and leaves the WordPress REST API open for anonymous reads at vaynermedia.com/wp-json/, with 365 registered routes covering posts, pages, media, taxonomies and the agency''s own case_study custom post type. The site also serves a Yoast-generated llms.txt. Neither is a developer product — they are the content surface of a marketing site — but both are real, public and callable, and they are what an agent researching the agency can actually read.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vaynermedia.png
layout: provider
modified: '2026-08-12'
name: VaynerMedia
nav: Providers
network: true
overview: 'VaynerMedia publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Agency, Brand Strategy, Content Production, and Creative.


  VaynerMedia''s developer surface includes authentication, engineering blog, YouTube channel, and 36 more developer resources.'
plans:
- name: Vaynermedia Plans Pricing
  plan_count: 0
  slug: vaynermedia-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Vaynermedia Rate Limits
  slug: vaynermedia-rate-limits
score:
  band: emerging
  composite: 17.4
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
    contract_quality: 0.0
    developer_ergonomics: 20.8
    discoverability: 64.3
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 18.4
  provenance:
    conformance: derived
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
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/vaynermedia/vaynermedia-2026-06-20T200840.png
security:
- kind: authentication
  name: Vaynermedia Authentication
  slug: vaynermedia-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vaynermedia Domain Security
  slug: vaynermedia-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: vaynermedia-harvest-case-studies
  slug: vaynermedia-harvest-case-studies
- name: vaynermedia-search-content
  slug: vaynermedia-search-content
slug: vaynermedia
tags:
- Advertising
- Agency
- Brand Strategy
- Content Production
- Creative
- Influencer Marketing
- Marketing
- Media Buying
- Social Media
website: https://vaynermedia.com/
---
