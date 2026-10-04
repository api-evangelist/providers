---
access_model:
  confidence: high
  label: No public API program
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Machine-readable filing data for Apogee Enterprises is available from the U.S. Securities and Exchange Commission, not from the company. The SEC EDGAR submissions API returns the full filing history f
  name: SEC EDGAR Filings (Apogee Enterprises, CIK 6845)
  slug: sec-edgar-filings
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://www.apog.com
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.apog.com/investor-relations
- group: operate
  title: ''
  type: PressReleases
  url: https://www.apog.com/news-releases
- group: other
  title: ''
  type: Sustainability
  url: https://www.apog.com/sustainability
- group: other
  title: ''
  type: Suppliers
  url: https://www.apog.com/supplier-portal
- group: company
  title: ''
  type: Careers
  url: https://apog.wd1.myworkdayjobs.com/Apogee
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apog.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apog.com/terms-use
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apogee-enterprises
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/apogeeglass
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/ApogeeEnterprisesInc
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/apog-enterprises/refs/heads/main/plans/apog-enterprises-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apog-enterprises-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apog-enterprises/refs/heads/main/rate-limits/apog-enterprises-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apog-enterprises-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apog-enterprises/refs/heads/main/security/apog-enterprises-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apog-enterprises-domain-security.yml
coverage:
  checked: '2026-09-18'
  detail: Apogee is an architectural glass and framing manufacturer whose only web surface is an Akamai-fronted investor-relations site; the api.apog.com and developer.apog.com hosts the April 2026 stub listed do not resolve in DNS, and the only "API" mention on its site is a Coupa Supplier Portal user role.
  evidence:
  - status: 0
    url: https://api.apog.com/openapi.json
  - status: 0
    url: https://developer.apog.com/docs
  - status: 403
    url: https://www.apog.com/.well-known/api-catalog
  - status: 403
    url: https://www.apog.com/supplier-portal
  - status: 200
    url: https://data.sec.gov/submissions/CIK0000006845.json
  reason: not-a-software-company
  state: none
created: '2026-04-19'
description: 'Apogee Enterprises (Nasdaq: APOG), founded in 1949 as the Harmon Glass Company and headquartered in Minneapolis, Minnesota, is an architectural products and services company. Its operating brands make high-performance architectural glass (Viracon), aluminum framing, storefront, curtainwall and entrance systems (Apogee Architectural Metals — the former EFCO and Tubelite — and Alumicor, with Linetec finishing), install glass and metal facades on large commercial buildings (Harmon) and produce large-scale optical glass and acrylic for framing and displays (Tru Vue, UW Solutions). Apogee does not publish a public developer API, SDK, webhook or developer portal. Its external digital surface is an Akamai-fronted investor-relations website at apog.com serving HTML and PDF, plus supplier onboarding on Coupa''s Supplier Portal; the "EDI/API/Integration contact" named there is a Coupa user role, not an Apogee API. The hosts api.apog.com and developer.apog.com listed by an earlier stub
  do not exist in DNS. Machine-readable company data is available only through third-party channels, namely the SEC''s EDGAR APIs.'
features:
- description: High-performance insulating, laminated and coated architectural glass for commercial buildings.
  name: Architectural Glass (Viracon)
- description: Aluminum window, storefront, curtainwall and entrance systems from Apogee Architectural Metals (formerly EFCO and Tubelite) and Alumicor, with Linetec architectural finishing.
  name: Architectural Framing Systems
- description: Design, engineering, fabrication and installation of glass and metal building facades.
  name: Architectural Services (Harmon)
- description: Glass and acrylic for custom picture framing, museums, displays and industrial applications.
  name: Large-Scale Optical (Tru Vue, UW Solutions)
- description: Quarterly earnings, annual reports and SEC filings published as HTML and PDF through the investor relations site and EDGAR.
  name: SEC Filings and Investor Reporting
finops:
- name: Apog Enterprises Finops
  service_category: Architectural Products
  slug: apog-enterprises-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apog-enterprises.png
integrations:
- description: All filings for CIK 0000006845 are available through EDGAR and the SEC's public JSON APIs at data.sec.gov.
  name: SEC EDGAR
- description: Supplier registration, purchase orders and invoicing run on Coupa; support at coupasupport@apog.com.
  name: Coupa Supplier Portal
- description: Careers and job applications are hosted on Workday (apog.wd1.myworkdayjobs.com).
  name: Workday
- description: Shares trade on Nasdaq under the ticker APOG.
  name: Nasdaq
layout: provider
modified: '2026-09-18'
name: Apogee Enterprises
nav: Providers
network: true
overview: 'Apogee Enterprises publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Glass, Architectural Glass, Architectural Framing, Storefront Systems, and Curtain Wall.


  Apogee Enterprises'' developer surface includes YouTube channel and 13 more developer resources.'
plans:
- name: Apog Enterprises Plans Pricing
  plan_count: 0
  slug: apog-enterprises-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Apog Enterprises Rate Limits
  slug: apog-enterprises-rate-limits
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 67.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 12.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apog Enterprises Domain Security
  slug: apog-enterprises-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apog-enterprises
tags:
- Glass
- Architectural Glass
- Architectural Framing
- Storefront Systems
- Curtain Wall
- Building Products
- Construction
- Investor Relations
- Fortune 1000
use_cases:
- description: Analyze Apogee Enterprises (Nasdaq:APOG) financial performance and segment reporting through EDGAR filings and investor materials.
  name: Investment Research
- description: Suppliers onboard and transact through Apogee's Coupa Supplier Portal and reference its supplier terms, conditions and policies.
  name: Supply Chain and Procurement
- description: Access sustainability disclosures on people, products, operations and community published through the corporate site.
  name: ESG Reporting
website: https://www.apog.com
---
