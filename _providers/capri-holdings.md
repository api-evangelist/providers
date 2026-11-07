---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - probe
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/capri-holdings/plans/capri-holdings-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/capri-holdings-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/capri-holdings/rate-limits/capri-holdings-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/capri-holdings-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/capri-holdings/finops/capri-holdings-finops.yml
  title: ''
  type: FinOps
  url: finops/capri-holdings-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.capriholdings.com
- group: company
  title: ''
  type: About
  url: https://www.capriholdings.com/overview/default.aspx
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.capriholdings.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.capriholdings.com/news/default.aspx
- group: other
  title: ''
  type: X-SECFilings
  url: https://www.capriholdings.com/financials/sec-filings/default.aspx
- group: other
  title: ''
  type: X-AnnualReports
  url: https://www.capriholdings.com/financials/annual-reports/default.aspx
- group: other
  title: ''
  type: Sustainability
  url: https://www.capriholdings.com/impact/esg-resources/default.aspx
- group: company
  title: ''
  type: Careers
  url: https://www.capriholdings.com/people/Join-Us/default.aspx
- group: operate
  title: ''
  type: Contact
  url: https://www.capriholdings.com/resources/investor-contacts/default.aspx
- group: other
  title: ''
  type: X-Sitemap
  url: https://www.capriholdings.com/site-map/default.aspx
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/capri-holdings-limited
- group: auth
  href: https://artifacts.apis.io/capri-holdings/security/capri-holdings-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capri-holdings-domain-security.yml
coverage:
  checked: '2026-09-19'
  detail: Capri Holdings is a luxury goods holding company (Michael Kors, Jimmy Choo) whose only web property, capriholdings.com, is a Q4-hosted investor-relations site with no developer, API or partner pages; the scaffolded api.capriholdings.com and developer.capriholdings.com hosts return NXDOMAIN, /openapi.json and /llms.txt 404, and every /.well-known/* path returns the platform's 11-byte 'Invalid key' catch-all (HTML pages answer 403 to curl behind a Cloudflare challenge but render in a browser fetch, which confirmed the site map lists no developer page).
  evidence:
  - status: 0
    url: https://api.capriholdings.com/
  - status: 0
    url: https://developer.capriholdings.com/
  - status: 404
    url: https://www.capriholdings.com/openapi.json
  - status: 404
    url: https://www.capriholdings.com/llms.txt
  - status: 200
    url: https://www.capriholdings.com/.well-known/security.txt
  - status: 200
    url: https://www.capriholdings.com/.well-known/agent-card.json
  - status: 403
    url: https://www.capriholdings.com/site-map/default.aspx
  reason: not-a-software-company
  state: none
created: '2026-04-19'
description: 'Capri Holdings Limited (NYSE: CPRI) is a global luxury fashion group whose portfolio is the Michael Kors and Jimmy Choo brands (Versace was sold to Prada in 2025 and no longer appears on the company''s overview). It designs, markets and sells apparel, footwear, handbags and accessories through its own stores, wholesale partners, licensees and brand e-commerce sites. Capri Holdings publishes no developer program: the corporate site at capriholdings.com is a Q4-hosted investor-relations property (news, SEC filings, governance, ESG resources, careers) with no API, documentation, SDK, package, OpenAPI, GraphQL, MCP or A2A surface, and the api.capriholdings.com and developer.capriholdings.com hosts an earlier scaffold named do not resolve in DNS. Every /.well-known/* path answers with the IR platform''s ''Invalid key'' catch-all rather than a document. This profile records that absence honestly; nothing has been authored on the company''s behalf.'
finops:
- has_sources: true
  method: generated
  name: Capri Holdings Finops
  primary_unit: ''
  service_category: Retail / Luxury Brand Integration
  slug: capri-holdings-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/capri-holdings.png
layout: provider
modified: '2026-09-19'
name: Capri Holdings
nav: Providers
network: true
overview: Capri Holdings is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Retail, Luxury, Fashion, Apparel, and Footwear.
plans:
- name: Capri Holdings Plans Pricing
  plan_count: 1
  slug: capri-holdings-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Capri Holdings Rate Limits
  slug: capri-holdings-rate-limits
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 31.0
    catalog_earned_first_party: 0.0
    catalog_gap: 84.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 5.3
  previous_composite: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/capri-holdings/capri-holdings-2026-07-25T204429.png
security:
- kind: domain-security
  name: Capri Holdings Domain Security
  slug: capri-holdings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: capri-holdings
tags:
- Retail
- Luxury
- Fashion
- Apparel
- Footwear
- Accessories
- Holding Company
- No Developer Program
website: https://www.capriholdings.com
---
