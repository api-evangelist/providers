---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Housesigma Agentic Access
  operation_count: 22
  slug: housesigma-agentic-access
  summary_line: 22 operations
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the HouseSigma website at housesigma.com/blog-en: the route index of the site''s content management system, catalogued as one site surface rather than as sepa'
  name: HouseSigma Website (WordPress REST)
  slug: housesigma-com-blog-en-website-wordpress-rest
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/housesigma/mcp/housesigma-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/housesigma-mcp.yml
- group: agent
  href: https://artifacts.apis.io/housesigma/agentic-access/housesigma-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/housesigma-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/housesigma/security/housesigma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/housesigma-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/housesigma/authentication/housesigma-authentication.yml
  title: ''
  type: Authentication
  url: authentication/housesigma-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://housesigma.com/
- group: company
  title: ''
  type: Blog
  url: https://housesigma.com/blog-en/
- group: company
  title: ''
  type: BlogRSS
  url: https://housesigma.com/blog-en/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/housesigma
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/housesigma
- group: agent
  href: https://artifacts.apis.io/housesigma/llms/housesigma-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/housesigma-llms.txt
- group: agent
  href: https://artifacts.apis.io/housesigma/well-known/housesigma-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/housesigma-well-known.yml
- group: design
  href: https://artifacts.apis.io/housesigma/conventions/housesigma-conventions.yml
  title: ''
  type: Conventions
  url: conventions/housesigma-conventions.yml
- group: design
  href: https://artifacts.apis.io/housesigma/errors/housesigma-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/housesigma-problem-types.yml
- group: design
  href: https://artifacts.apis.io/housesigma/lifecycle/housesigma-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/housesigma-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/housesigma/conformance/housesigma-conformance.yml
  title: ''
  type: Conformance
  url: conformance/housesigma-conformance.yml
- group: design
  href: https://artifacts.apis.io/housesigma/data-model/housesigma-data-model.yml
  title: ''
  type: DataModel
  url: data-model/housesigma-data-model.yml
- group: design
  href: https://artifacts.apis.io/housesigma/components/housesigma-components.yml
  title: ''
  type: Components
  url: components/housesigma-components.yml
- group: agent
  href: https://artifacts.apis.io/housesigma/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/housesigma/examples/
  title: ''
  type: Examples
  url: examples/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://housesigma.com/blog-en/2018/04/25/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://housesigma.com/blog-en/2018/04/25/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://housesigma.com/blog-en/contact-us/
- group: operate
  title: ''
  type: FAQ
  url: https://housesigma.com/blog-en/faq/
- group: company
  title: ''
  type: About
  url: https://housesigma.com/blog-en/about-us/
- group: company
  title: ''
  type: Careers
  url: https://team.housesigma.com/
- group: other
  title: ''
  type: iOSApp
  url: https://itunes.apple.com/ca/app/toronto-real-estate-housesigma/id1255490256?mt=8
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=com.housesigma.android&hl=en_CA
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/housesigma/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/housesigma/
created: '2026-07-26'
description: 'HouseSigma, Inc. Brokerage is a Toronto-based Canadian residential real estate portal and licensed brokerage that pairs map-based MLS listing search with sold-price history and machine-learning home valuations (SigmaEstimate) across Ontario, British Columbia, and Alberta. It sits in the challenger layer of the Canadian value chain, below CREA, which operates REALTOR.ca and the national Data Distribution Facility (DDF) that syndicates member boards'' listings, and alongside Wahi, Zolo, and Properly, competing on visibility into data the boards control, a position it won in part through the Competition Bureau litigation that forced TRREB to release sold data in 2018. Its API posture is closed. There is no developer portal, no published API program, and no partner or data-licensing page; developer., developers., and docs.housesigma.com do not resolve in DNS, and /developers, /api, /api-docs, /openapi.json and /swagger.json all return the single-page-application shell rather than
  any contract. The listing, sold-history and valuation backend at housesigma.com/bkv2/api/ is private, keyless, undocumented, and explicitly disallowed to all crawlers in robots.txt. The one genuinely public, anonymously callable, machine-readable HTTP surface the company operates is the WordPress REST API behind housesigma.com/blog-en, which serves its Canadian housing-market analysis blog as JSON across 157 advertised routes; API Evangelist derived an OpenAPI for the 22 operations verified to answer anonymously. HouseSigma also publishes a real llms.txt and mobile deep-link association documents. RESO is absent: HouseSigma is not among the Canadian organizations RESO lists as members, and no Web API or Data Dictionary certification, OData $metadata document, or Universal Property Identifier usage was found. No open, unlicensed dataset is published. The underlying listing and sold data is board-licensed and reaches HouseSigma through its own brokerage membership, not through anything a
  third-party developer can sign up for.'
examples:
- key_count: 3
  name: Housesigma Blog Content Error 400 Rest_Invalid_Param
  slug: housesigma-blog-content-error-400-rest_invalid_param
- key_count: 3
  name: Housesigma Blog Content Error 401 Rest_Forbidden
  slug: housesigma-blog-content-error-401-rest_forbidden
- key_count: 3
  name: Housesigma Blog Content Error 404 Rest_Post_Invalid_Id
  slug: housesigma-blog-content-error-404-rest_post_invalid_id
- key_count: 12
  name: Housesigma Blog Content Getoembed 200
  slug: housesigma-blog-content-getOembed-200
- key_count: 4
  name: Housesigma Blog Content Listtaxonomies 200
  slug: housesigma-blog-content-listTaxonomies-200
image: https://housesigma.com/apple-touch-icon.png?v=2
layout: provider
modified: '2026-07-26'
name: HouseSigma
nav: Providers
network: true
overview: 'HouseSigma publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Canada, Property Listings, MLS, and Valuation.


  HouseSigma''s developer surface includes authentication, engineering blog, code examples, support, FAQ, and 24 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 6.5
    developer_ergonomics: 25.6
    discoverability: 64.3
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 20.6
  provenance:
    agentic_access: derived
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
screenshot: https://apis.io/screenshots/housesigma/housesigma-2026-08-07T170335.png
security:
- kind: authentication
  name: Housesigma Authentication
  slug: housesigma-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Housesigma Domain Security
  slug: housesigma-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Embed a HouseSigma market-analysis post
  slug: housesigma-embed-market-analysis
- name: Mirror the HouseSigma content catalog
  slug: housesigma-mirror-content-catalog
- name: Track HouseSigma Canadian housing-market commentary
  slug: housesigma-track-market-commentary
slug: housesigma
tags:
- Real Estate
- Canada
- Property Listings
- MLS
- Valuation
- AVM
- PropTech
- Rentals
- Blog
- Content
- WordPress
- oEmbed
- Ontario
- British Columbia
- Toronto
website: https://housesigma.com/
---
