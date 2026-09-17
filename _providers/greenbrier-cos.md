---
access_model:
  confidence: high
  label: Public read-only APIs, no key and no signup
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: true
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
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.0
  scored_at: '2026-09-16'
api_count: 1
apis:
- baseURL: https://tankcar.gbrx.com
  baseurl_source: declared
  description: Product categories, tags, brands and attribute vocabularies.
  name: Greenbrier Companies Catalog API
  slug: greenbrier-cos-catalog-api
- baseURL: https://tankcar.gbrx.com
  baseurl_source: declared
  description: oEmbed discovery for gbrx.com URLs.
  name: Greenbrier Companies Discovery API
  slug: greenbrier-cos-discovery-api
- baseURL: https://tankcar.gbrx.com
  baseurl_source: declared
  description: Downloadable Pdf, Csv and Txt renderings of a gauge table.
  name: Greenbrier Companies Export API
  slug: greenbrier-cos-export-api
- baseURL: https://tankcar.gbrx.com
  baseurl_source: declared
  description: Innage/outage capacity curves for a specific tank car.
  name: Greenbrier Companies Gauge Tables API
  slug: greenbrier-cos-gauge-tables-api
- baseURL: https://tankcar.gbrx.com
  baseurl_source: declared
  description: Static site pages — services, manufacturing, leasing, investors, careers, policies.
  name: Greenbrier Companies Pages API
  slug: greenbrier-cos-pages-api
- baseURL: https://tankcar.gbrx.com
  baseurl_source: declared
  description: Greenbrier press releases, announcements and Perspectives & Updates articles.
  name: Greenbrier Companies Posts API
  slug: greenbrier-cos-posts-api
- baseURL: https://tankcar.gbrx.com
  baseurl_source: declared
  description: Aftermarket railcar replacement parts.
  name: Greenbrier Companies Products API
  slug: greenbrier-cos-products-api
- baseURL: https://tankcar.gbrx.com
  baseurl_source: declared
  description: Greenbrier railcar models — covered hoppers, tank cars, gondolas, boxcars, intermodal and automotive equipment.
  name: Greenbrier Companies Railcars API
  slug: greenbrier-cos-railcars-api
- baseURL: https://tankcar.gbrx.com
  baseurl_source: declared
  description: The railcar reporting marks for which Greenbrier holds gauge tables.
  name: Greenbrier Companies Reporting Marks API
  slug: greenbrier-cos-reporting-marks-api
- baseURL: https://tankcar.gbrx.com
  baseurl_source: declared
  description: Cross-content search over posts, pages and railcars.
  name: Greenbrier Companies Search API
  slug: greenbrier-cos-search-api
- baseURL: https://tankcar.gbrx.com
  baseurl_source: declared
  description: Post categories and tags.
  name: Greenbrier Companies Taxonomies API
  slug: greenbrier-cos-taxonomies-api
artifact_total: 16
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/greenbrier-cos/refs/heads/main/overlays/greenbrier-cos-gauge-table-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/greenbrier-cos-gauge-table-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/greenbrier-cos/refs/heads/main/overlays/greenbrier-cos-railcar-catalog-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/greenbrier-cos-railcar-catalog-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/greenbrier-cos/refs/heads/main/overlays/greenbrier-cos-parts-store-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/greenbrier-cos-parts-store-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/greenbrier-cos/refs/heads/main/overlays/greenbrier-cos-press-room-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/greenbrier-cos-press-room-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/greenbrier-cos/refs/heads/main/overlays/greenbrier-cos-site-content-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/greenbrier-cos-site-content-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.gbrx.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-greenbrier-companies
- group: company
  title: ''
  type: Blog
  url: https://www.gbrx.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.gbrx.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gbrx.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gbrx.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.gbrx.com/certifications/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/greenbrier-cos/refs/heads/main/conformance/greenbrier-cos-conformance.yml
  title: ''
  type: Conformance
  url: conformance/greenbrier-cos-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/greenbrier-cos/refs/heads/main/packages/greenbrier-cos-packages.yml
  title: ''
  type: Packages
  url: packages/greenbrier-cos-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/greenbrier-cos/refs/heads/main/well-known/greenbrier-cos-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/greenbrier-cos-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/greenbrier-cos/refs/heads/main/llms/greenbrier-cos-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/greenbrier-cos-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/greenbrier-cos/refs/heads/main/mcp/greenbrier-cos-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/greenbrier-cos-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/greenbrier-cos/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/greenbrier-cos/refs/heads/main/plans/greenbrier-cos-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/greenbrier-cos-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/greenbrier-cos/refs/heads/main/rate-limits/greenbrier-cos-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/greenbrier-cos-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/greenbrier-cos/refs/heads/main/security/greenbrier-cos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/greenbrier-cos-domain-security.yml
created: '2026-03-24'
description: 'The Greenbrier Companies is a leading international supplier of equipment and services to global freight transportation markets, designing, building and marketing freight railcars in North America, Europe and South America from its headquarters in Lake Oswego, Oregon. Greenbrier also operates railcar leasing and fleet management, wheel services, maintenance and repair, marine barge manufacturing in Portland, and participates in the RailPulse railcar-telematics joint venture. Greenbrier publishes no developer program, no API portal and no SDKs, and sells no API product. It does, however, operate several real, anonymously callable HTTP surfaces on its own hosts: a bespoke JSON API serving certified tank-car gauge tables at tankcar.gbrx.com, and the WordPress and WooCommerce Store REST APIs behind www.gbrx.com, which expose the railcar product catalog, the aftermarket parts catalog, the press room and site search. Those are catalogued here for discovery; they are not a product
  Greenbrier markets.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/greenbrier-cos.png
layout: provider
mcp_servers:
- description: ''
  name: Greenbrier Companies MCP Server
  slug: greenbrier-companies-mcp-server
modified: '2026-09-12'
name: Greenbrier Companies
nav: Providers
network: true
overview: 'Greenbrier Companies publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Discovery API, Export API, and 8 more. Tagged areas include Rail, Railcars, Freight, Transportation, and Manufacturing.


  Greenbrier Companies'' developer surface includes engineering blog, support, and 19 more developer resources.'
plans:
- name: Greenbrier Cos Plans Pricing
  plan_count: 0
  slug: greenbrier-cos-plans-pricing
press:
- date: '2026-05-25'
  title: The Greenbrier Cos. Inc. Upgraded To 'B+' On Impr
  url: https://www.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/1044886
- date: '2026-05-25'
  title: Stock Analysis, Ratings & Investment Research
  url: https://financhill.com/compare/industry/na/aiq-vs-gbx
- date: '2026-05-25'
  title: Rail supplier news from Hitachi Rail and Greenbrier
  url: https://www.progressiverailroading.com/supplier_spotlight/news/Rail-supplier-news-from-Hitachi-Rail-and-Greenbrier--75682
- date: '2026-05-25'
  title: Greenbrier Cos. Inc <GBX.N> Q4 results
  url: https://www.reuters.com/article/legal/government/greenbrier-cos-inc-gbxn-q4-results-idUSWNAS0537/
- date: '2026-05-25'
  title: Greenbrier Cos. (GBX,N) reports earnings for Qtr to Aug 31
  url: https://www.nytimes.com/1994/11/11/business/greenbrier-cos-gbxn-reports-earnings-for-qtr-to-aug-31.html
random_paper: 1
rate_limits:
- limit_count: 0
  name: Greenbrier Cos Rate Limits
  slug: greenbrier-cos-rate-limits
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 13.0
    developer_ergonomics: 20.8
    discoverability: 75.9
    operational_transparency: 0.0
  previous_composite: 23.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/greenbrier-cos/refs/heads/main/screenshots/greenbrier-cos-2026-06-20T182356.png
security:
- kind: authentication
  name: Greenbrier Cos Authentication
  slug: greenbrier-cos-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Greenbrier Cos Domain Security
  slug: greenbrier-cos-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: greenbrier-cos
tags:
- Rail
- Railcars
- Freight
- Transportation
- Manufacturing
- Leasing
- Logistics
- Tank Cars
- Gauge Tables
- Aftermarket Parts
- Content
- Commerce
website: https://www.gbrx.com
---
