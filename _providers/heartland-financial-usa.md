---
access_model:
  confidence: medium
  gated: private
  gated_source:
  - x-api-posture
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/heartland-financial-usa/finops/heartland-financial-usa-finops.yml
  title: ''
  type: FinOps
  url: finops/heartland-financial-usa-finops.yml
- group: auth
  href: https://artifacts.apis.io/heartland-financial-usa/security/heartland-financial-usa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/heartland-financial-usa-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/poweredbyhtlf
- group: company
  title: ''
  type: Website
  url: https://www.umb.com
- group: commercial
  href: https://artifacts.apis.io/heartland-financial-usa/plans/heartland-financial-usa-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/heartland-financial-usa-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/heartland-financial-usa/rate-limits/heartland-financial-usa-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/heartland-financial-usa-rate-limits.yml
coverage:
  checked: '2026-09-14'
  detail: Heartland Financial USA ceased to exist when UMB Financial completed its acquisition on 2025-01-31 and finished converting every former HTLF divisional bank to the UMB brand and platforms in October 2025; htlf.com now answers HTTP 400 to every path behind a decommissioned Akamai configuration serving a certificate for a248.e.akamai.net, while api.htlf.com and developer.htlf.com — the two hosts a 2026-04 bulk sweep had written into this record — return NXDOMAIN and never existed.
  evidence:
  - status: 400
    url: https://www.htlf.com/
  - status: 400
    url: https://htlf.com/.well-known/security.txt
  - status: 0
    url: https://api.htlf.com/
  - status: 0
    url: https://developer.htlf.com/docs
  - status: 404
    url: https://github.com/htlfusa
  - status: 200
    url: https://www.umb.com/
  reason: defunct
  state: none
created: '2026-04-19'
description: Heartland Financial USA, Inc. (HTLF) was a Denver, Colorado bank holding company — formerly headquartered in Dubuque, Iowa — that operated a multi-charter family of community banks across twelve states, including Dubuque Bank and Trust, Illinois Bank & Trust, Wisconsin Bank & Trust, New Mexico Bank & Trust, Arizona Bank & Trust, Rocky Mountain Bank, Citywide Banks, Minnesota Bank & Trust, Premier Valley Bank, First Bank & Trust, Bank of Blue Valley and Signature Bank of Arkansas. Its business was commercial and retail banking, treasury management, and wealth services delivered through branches and third-party core banking platforms rather than through a developer program. HTLF never published a developer portal, API reference, SDK, or machine-readable contract of any kind. UMB Financial Corporation completed its all-stock acquisition of HTLF on January 31, 2025 — the largest in UMB's history — and completed the systems and brand conversion of every former HTLF divisional bank
  in October 2025, at which point the HTLF brand ceased to exist. The htlf.com edge configuration has since been decommissioned. This profile is retained as a historical record; any banking API surface for these institutions now lives with UMB and is tracked separately under the UMB Bank profile.
finops:
- has_sources: true
  method: generated
  name: Heartland Financial Usa Finops
  primary_unit: varies
  service_category: Banking / Financial Services
  slug: heartland-financial-usa-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/heartland-financial-usa.png
layout: provider
modified: '2026-09-14'
name: Heartland Financial USA
nav: Providers
network: true
overview: Heartland Financial USA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Financial Services, Commercial Banking, Treasury Management, and Acquired.
plans:
- name: Heartland Financial Usa Plans Pricing
  plan_count: 0
  slug: heartland-financial-usa-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Heartland Financial Usa Rate Limits
  slug: heartland-financial-usa-rate-limits
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  lifecycle: defunct
  previous_composite: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 4.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/heartland-financial-usa/heartland-financial-usa-2026-10-11T105155.png
security:
- kind: domain-security
  name: Heartland Financial Usa Domain Security
  slug: heartland-financial-usa-domain-security
  summary_line: DMARC
slug: heartland-financial-usa
tags:
- Banking
- Financial Services
- Commercial Banking
- Treasury Management
- Acquired
- Defunct
- Bank-Holding-Company
- United States
website: https://www.umb.com
---
