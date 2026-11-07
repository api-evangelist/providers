---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - rate-limits
  - security
  - '{''url'': ''https://www.hilltop-holdings.com'', ''status'': 302, ''note'': ''declared website redirects to https://www.hilltop.com/ — a different registrable domain (hilltop-holdings.com -> hilltop.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/hilltop-holdings/finops/hilltop-holdings-finops.yml
  title: ''
  type: FinOps
  url: finops/hilltop-holdings-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hilltop.com/
- group: auth
  href: https://artifacts.apis.io/hilltop-holdings/security/hilltop-holdings-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hilltop-holdings-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hilltop-holdings
- group: company
  title: ''
  type: Website
  url: https://www.hilltop.com/
- group: company
  title: ''
  type: Blog
  url: https://www.hilltop.com/news-media/hilltop-news/
- group: agent
  href: https://artifacts.apis.io/hilltop-holdings/llms/hilltop-holdings-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hilltop-holdings-llms.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hilltop.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hilltop.com/terms-and-conditions/
- group: commercial
  href: https://artifacts.apis.io/hilltop-holdings/plans/hilltop-holdings-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hilltop-holdings-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/hilltop-holdings/rate-limits/hilltop-holdings-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hilltop-holdings-rate-limits.yml
coverage:
  checked: '2026-09-14'
  detail: 'Hilltop Holdings is a bank/broker-dealer/mortgage holding company with no developer program at any level of the family: the two hosts this profile previously claimed, api.hilltop-holdings.com and developer.hilltop-holdings.com, do not exist in DNS at all (NXDOMAIN), the corporate site www.hilltop.com serves only a Yoast-generated llms.txt and answers every other discovery path with an Imperva catch-all, the HilltopSecurities API host serves a default IIS start page, and the hilltopsecurities / hilltopholdings / primelending GitHub organizations each hold zero public repositories.'
  evidence:
  - status: 0
    url: https://api.hilltop-holdings.com/
  - status: 0
    url: https://developer.hilltop-holdings.com/docs
  - status: 200
    url: https://www.hilltop.com/llms.txt
  - status: 200
    url: https://www.hilltop.com/.well-known/api-catalog
  - status: 404
    url: https://www.hilltop.com/.well-known/security.txt
  - status: 404
    url: https://api.hilltopsecurities.com/openapi.json
  - status: 200
    url: https://api.github.com/orgs/hilltopsecurities/repos
  reason: no-developer-program
  state: none
created: '2026-04-19'
description: 'Hilltop Holdings Inc. (NYSE: HTH, dual-listed on NYSE Texas) is a Dallas-based financial services holding company that operates through three wholly owned subsidiaries: PlainsCapital Bank, a Texas commercial bank; HilltopSecurities, a full-service investment bank covering public finance, wealth management, fixed income capital markets and structured finance; and PrimeLending, a national residential mortgage originator. Hilltop Holdings itself is a holding company, not a software vendor — it publishes no developer portal, no API reference and no machine-readable specification at the holding-company level, and the subsidiaries surface their technology as end-user platforms (MOmentum Advisor, HilltopBancSystems, loan servicing portals) rather than as public APIs. This profile records that public surface as it actually is: a corporate site that serves an llms.txt and nothing else a machine can consume.'
finops:
- has_sources: true
  method: generated
  name: Hilltop Holdings Finops
  primary_unit: varies
  service_category: Banking / Insurance / Financial Services
  slug: hilltop-holdings-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hilltop-holdings.png
layout: provider
modified: '2026-09-14'
name: Hilltop Holdings
nav: Providers
network: true
overview: 'Hilltop Holdings is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Insurance, Financial Services, Mortgage, and Broker-Dealer.


  Hilltop Holdings'' developer surface includes pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Hilltop Holdings Plans Pricing
  plan_count: 1
  slug: hilltop-holdings-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Hilltop Holdings Rate Limits
  slug: hilltop-holdings-rate-limits
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 46.0
    catalog_earned_first_party: 16.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 14.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 5.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/hilltop-holdings/hilltop-holdings-2026-10-11T105310.png
security:
- kind: domain-security
  name: Hilltop Holdings Domain Security
  slug: hilltop-holdings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hilltop-holdings
tags:
- Banking
- Insurance
- Financial Services
- Mortgage
- Broker-Dealer
- Wealth Management
- Holding Company
website: https://www.hilltop.com/
---
