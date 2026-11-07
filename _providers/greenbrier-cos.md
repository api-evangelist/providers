---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.0
  scored_at: '2026-11-06'
api_count: 1
apis:
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
  description: The railcar reporting marks for which Greenbrier holds gauge tables.
  name: Greenbrier Companies Reporting Marks API
  slug: greenbrier-cos-reporting-marks-api
- description: 'The public WordPress REST API (wp-json) of the Greenbrier Companies website at www.gbrx.com: the route index of the site''s content management system, catalogued as one site surface rather than as sepa'
  name: Greenbrier Companies Website (WordPress REST)
  slug: gbrx-com-website-wordpress-rest
artifact_total: 14
common:
- group: other
  href: https://artifacts.apis.io/greenbrier-cos/overlays/greenbrier-cos-gauge-table-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/greenbrier-cos-gauge-table-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/greenbrier-cos/overlays/greenbrier-cos-railcar-catalog-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/greenbrier-cos-railcar-catalog-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/greenbrier-cos/overlays/greenbrier-cos-parts-store-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/greenbrier-cos-parts-store-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/greenbrier-cos/overlays/greenbrier-cos-press-room-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/greenbrier-cos-press-room-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/greenbrier-cos/overlays/greenbrier-cos-site-content-api-overlay.yaml
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
  href: https://artifacts.apis.io/greenbrier-cos/conformance/greenbrier-cos-conformance.yml
  title: ''
  type: Conformance
  url: conformance/greenbrier-cos-conformance.yml
- group: build
  href: https://artifacts.apis.io/greenbrier-cos/packages/greenbrier-cos-packages.yml
  title: ''
  type: Packages
  url: packages/greenbrier-cos-packages.yml
- group: agent
  href: https://artifacts.apis.io/greenbrier-cos/well-known/greenbrier-cos-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/greenbrier-cos-well-known.yml
- group: agent
  href: https://artifacts.apis.io/greenbrier-cos/llms/greenbrier-cos-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/greenbrier-cos-llms.txt
- group: agent
  href: https://artifacts.apis.io/greenbrier-cos/mcp/greenbrier-cos-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/greenbrier-cos-mcp.yml
- group: agent
  href: https://artifacts.apis.io/greenbrier-cos/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/greenbrier-cos/plans/greenbrier-cos-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/greenbrier-cos-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/greenbrier-cos/rate-limits/greenbrier-cos-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/greenbrier-cos-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/greenbrier-cos/security/greenbrier-cos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/greenbrier-cos-domain-security.yml
created: '2026-03-24'
description: 'The Greenbrier Companies is a leading international supplier of equipment and services to global freight transportation markets, designing, building and marketing freight railcars in North America, Europe and South America from its headquarters in Lake Oswego, Oregon. Greenbrier also operates railcar leasing and fleet management, wheel services, maintenance and repair, marine barge manufacturing in Portland, and participates in the RailPulse railcar-telematics joint venture. Greenbrier publishes no developer program, no API portal and no SDKs, and sells no API product. It does, however, operate several real, anonymously callable HTTP surfaces on its own hosts: a bespoke JSON API serving certified tank-car gauge tables at tankcar.gbrx.com, and the WordPress and WooCommerce Store REST APIs behind www.gbrx.com, which expose the railcar product catalog, the aftermarket parts catalog, the press room and site search. Those are catalogued here for discovery; they are not a product
  Greenbrier markets.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/greenbrier-cos.png
layout: provider
mcp_servers:
- description: MCP server; 14 tools listed. A candidate, not confirmed as published by the provider.
  name: Greenbrier Companies MCP Server
  slug: greenbrier-cos-mcp-yml
modified: '2026-09-12'
name: Greenbrier Companies
nav: Providers
network: true
overview: 'Greenbrier Companies publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Export API, Gauge Tables API, Reporting Marks API, and 1 more. Tagged areas include Rail, Railcars, Freight, Transportation, and Manufacturing.


  The Greenbrier Companies catalog on APIs.io includes 1 Spectral governance ruleset.


  Greenbrier Companies'' developer surface includes engineering blog, support, and 19 more developer resources.'
plans:
- name: Greenbrier Cos Plans Pricing
  plan_count: 0
  slug: greenbrier-cos-plans-pricing
press:
- date: ''
  title: The Greenbrier Cos. Inc. Upgraded To 'B+' On Impr
  url: https://www.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/1044886
- date: ''
  title: Stock Analysis, Ratings & Investment Research
  url: https://financhill.com/compare/industry/na/aiq-vs-gbx
- date: ''
  title: Rail supplier news from Hitachi Rail and Greenbrier
  url: https://www.progressiverailroading.com/supplier_spotlight/news/Rail-supplier-news-from-Hitachi-Rail-and-Greenbrier--75682
- date: ''
  title: Greenbrier Cos. Inc <GBX.N> Q4 results
  url: https://www.reuters.com/article/legal/government/greenbrier-cos-inc-gbxn-q4-results-idUSWNAS0537/
- date: ''
  title: Greenbrier Cos. (GBX,N) reports earnings for Qtr to Aug 31
  url: https://www.nytimes.com/1994/11/11/business/greenbrier-cos-gbxn-reports-earnings-for-qtr-to-aug-31.html
random_paper: 15
rate_limits:
- limit_count: 0
  name: Greenbrier Cos Rate Limits
  slug: greenbrier-cos-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Greenbrier Companies API Rules
  rule_count: 60
  severity_counts:
    error: 48
    hint: 0
    info: 2
    warn: 10
  slug: greenbrier-cos-rules
score:
  band: thin
  composite: 26.4
  coverage:
    artifact_dirs: 24
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 28.9
    contract_governance: 31.8
    contract_quality: 12.4
    developer_ergonomics: 25.6
    discoverability: 64.3
    operational_transparency: 0.0
  previous_composite: 27.4
  provenance:
    conformance: first-party
    contracts:
      callable: 72.7
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/greenbrier-cos/greenbrier-cos-2026-06-20T182356.png
security:
- kind: authentication
  name: Greenbrier Cos Authentication
  slug: greenbrier-cos-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Greenbrier Cos Domain Security
  slug: greenbrier-cos-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: greenbrier-aftermarket-parts-lookup
  slug: greenbrier-cos-aftermarket-parts-lookup
- name: greenbrier-press-room-monitor
  slug: greenbrier-cos-press-room-monitor
- name: greenbrier-railcar-catalog-search
  slug: greenbrier-cos-railcar-catalog-search
- name: greenbrier-tank-car-gauge-table-lookup
  slug: greenbrier-cos-tank-car-gauge-table-lookup
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
