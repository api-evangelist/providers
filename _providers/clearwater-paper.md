---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/clearwater-paper/finops/clearwater-paper-finops.yml
  title: ''
  type: FinOps
  url: finops/clearwater-paper-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.clearwaterpaper.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clearwaterpaper.com/privacy-notice/default.aspx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clearwaterpaper.com/terms-and-conditions-of-use/default.aspx
- group: operate
  title: ''
  type: Support
  url: https://www.clearwaterpaper.com/contact-us/default.aspx
- group: company
  title: ''
  type: Newsroom
  url: https://www.clearwaterpaper.com/investors/press-releases/default.aspx
- group: other
  title: ''
  type: Leadership
  url: https://www.clearwaterpaper.com/about-us/leadership/default.aspx
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clearwaterpaper
- group: auth
  href: https://artifacts.apis.io/clearwater-paper/security/clearwater-paper-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clearwater-paper-domain-security.yml
- group: other
  href: https://artifacts.apis.io/clearwater-paper/regulatory/clearwater-paper-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/clearwater-paper-regulatory-posture.yml
- group: other
  href: https://artifacts.apis.io/clearwater-paper/regulatory/clearwater-paper-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/clearwater-paper-regulatory-posture.yml
- group: commercial
  href: https://artifacts.apis.io/clearwater-paper/plans/clearwater-paper-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clearwater-paper-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/clearwater-paper/rate-limits/clearwater-paper-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/clearwater-paper-rate-limits.yml
coverage:
  checked: '2026-09-19'
  detail: Clearwater Paper is a paperboard and tissue manufacturer whose corporate site is a Q4 Inc. investor-relations platform with no developer, API or documentation section; the developer.clearwaterpaper.com and api.clearwaterpaper.com hosts the previous record named as humanURL and baseURL return NXDOMAIN, every /.well-known/ path on www answers the platform's 11-byte "Invalid key" body, /llms.txt 404s, the customer-login page describes a customer portal without naming or linking it, and the only EDI trace (X12 850/810/856/997) is a Cleo trading-partner marketing page rather than any Clearwater Paper publication.
  evidence:
  - status: 0
    url: https://developer.clearwaterpaper.com/docs
  - status: 0
    url: https://api.clearwaterpaper.com/openapi.json
  - status: 200
    url: https://www.clearwaterpaper.com/customer-login/default.aspx
  - status: 200
    url: https://www.clearwaterpaper.com/.well-known/api-catalog
  - status: 404
    url: https://www.clearwaterpaper.com/llms.txt
  - status: 404
    url: https://www.clearwaterpaper.com/accessibility/default.aspx
  reason: not-a-software-company
  state: none
created: '2026-04-19'
description: 'Clearwater Paper Corporation (NYSE: CLW) is a Spokane, Washington-based manufacturer of bleached paperboard for North American packaging converters and, historically, private-label tissue for retailers. It is a Fortune 1000 company with mills in Idaho, Arkansas and Georgia. Clearwater Paper publishes no public API, developer program, SDK, or machine-readable contract: its corporate site is an investor-relations platform with a customer-login landing page that describes, but does not name or link, a secure customer web portal, and the api./developer. hostnames an earlier version of this record pointed at do not exist in DNS. Trading-partner EDI (X12 850/810/856/997) is offered only through third-party VAN and integration vendors, not from a Clearwater Paper developer surface.'
finops:
- has_sources: true
  method: generated
  name: Clearwater Paper Finops
  primary_unit: ''
  service_category: Consumer Goods Manufacturing
  slug: clearwater-paper-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clearwater-paper.png
layout: provider
modified: '2026-09-19'
name: Clearwater Paper
nav: Providers
network: true
overview: 'Clearwater Paper is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Paperboard, Tissue, Packaging, Manufacturing, and Consumer Goods.


  Clearwater Paper''s developer surface includes support and 12 more developer resources.'
plans:
- name: Clearwater Paper Plans Pricing
  plan_count: 0
  slug: clearwater-paper-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Clearwater Paper Rate Limits
  slug: clearwater-paper-rate-limits
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 10.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/clearwater-paper/clearwater-paper-2026-06-20T174513.png
security:
- kind: domain-security
  name: Clearwater Paper Domain Security
  slug: clearwater-paper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clearwater-paper
tags:
- Paperboard
- Tissue
- Packaging
- Manufacturing
- Consumer Goods
- Forest Products
- Fortune 1000
website: https://www.clearwaterpaper.com
---
