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
  href: https://artifacts.apis.io/crossamerica-partners/finops/crossamerica-partners-finops.yml
  title: ''
  type: FinOps
  url: finops/crossamerica-partners-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.crossamericapartners.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crossamerica-partners-lp
- group: company
  title: ''
  type: Newsroom
  url: https://www.crossamericapartners.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.crossamericapartners.com/about/management
- group: company
  title: ''
  type: Careers
  url: https://www.crossamericapartners.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.crossamericapartners.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crossamericapartners.com/legal-disclaimers-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crossamericapartners.com/privacy-policy
- group: other
  title: ''
  type: Accessibility
  url: https://www.crossamericapartners.com/accessibility-statement
- group: auth
  href: https://artifacts.apis.io/crossamerica-partners/security/crossamerica-partners-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crossamerica-partners-domain-security.yml
- group: other
  href: https://artifacts.apis.io/crossamerica-partners/regulatory/crossamerica-partners-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/crossamerica-partners-regulatory-posture.yml
- group: commercial
  href: https://artifacts.apis.io/crossamerica-partners/plans/crossamerica-partners-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crossamerica-partners-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/crossamerica-partners/rate-limits/crossamerica-partners-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/crossamerica-partners-rate-limits.yml
coverage:
  checked: '2026-09-19'
  detail: CrossAmerica Partners is a wholesale motor-fuel distributor and convenience-store real-estate partnership whose entire public surface is a 26-URL corporate sitemap with no developer, API, docs or pricing page; the api.crossamericapartners.com and developer.crossamericapartners.com hosts a prior scaffold pointed at do not resolve in DNS (NXDOMAIN), every OpenAPI, GraphQL, llms.txt and /.well-known/* path 404s on www.crossamericapartners.com, no GitHub organization or package-registry footprint exists, and the one integration surface it links — the Dealer Portal at www.partnerdatalink.com — is a credential-gated third-party platform behind a Deloitte WAF, not a CrossAmerica-operated API.
  evidence:
  - status: 200
    url: https://www.crossamericapartners.com/
  - status: 200
    url: https://www.crossamericapartners.com/sitemap.xml
  - status: 404
    url: https://www.crossamericapartners.com/openapi.json
  - status: 404
    url: https://www.crossamericapartners.com/developers
  - status: 404
    url: https://www.crossamericapartners.com/llms.txt
  - status: 404
    url: https://www.crossamericapartners.com/.well-known/api-catalog
  - status: 404
    url: https://www.crossamericapartners.com/.well-known/agent-card.json
  - status: 0
    url: https://api.crossamericapartners.com/
  - status: 0
    url: https://developer.crossamericapartners.com/
  - status: 200
    url: https://www.partnerdatalink.com/CrossAmerica/app/login
  - status: 404
    url: https://github.com/crossamericapartners
  reason: not-a-software-company
  state: none
created: '2026-04-19'
description: 'CrossAmerica Partners LP (NYSE: CAPL) is a U.S. wholesale distributor of motor fuels, operator of convenience stores, and owner and lessee of real estate used in the retail distribution of motor fuels. Headquartered in Allentown, Pennsylvania and formed in 2012, it distributes branded (Exxon, Mobil, BP, Shell, Valero, Citgo, Marathon, Phillips 66) and unbranded petroleum to approximately 1,600 locations across 34 states, owns or leases about 900 sites, and runs seven convenience-store brands at 340 locations in 17 states. CrossAmerica publishes no public API, developer portal or machine-readable contract; its only integration surface is a credential-gated Dealer Portal (account balance, pricing notifications, fuel and real-estate invoices, EFTs) hosted on a third-party platform, with logins issued by a Territory Manager under a dealer agreement.'
finops:
- has_sources: true
  method: generated
  name: Crossamerica Partners Finops
  primary_unit: ''
  service_category: Wholesale Fuel Distribution
  slug: crossamerica-partners-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crossamerica-partners.png
layout: provider
modified: '2026-09-19'
name: CrossAmerica Partners
nav: Providers
network: true
overview: CrossAmerica Partners is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fuel Distribution, Convenience Stores, Energy, Wholesale Fuel, and Petroleum.
plans:
- name: Crossamerica Partners Plans Pricing
  plan_count: 0
  slug: crossamerica-partners-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Crossamerica Partners Rate Limits
  slug: crossamerica-partners-rate-limits
score:
  band: minimal
  composite: 9.0
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 9.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/crossamerica-partners/crossamerica-partners-2026-06-20T175242.png
security:
- kind: domain-security
  name: Crossamerica Partners Domain Security
  slug: crossamerica-partners-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: crossamerica-partners
tags:
- Fuel Distribution
- Convenience Stores
- Energy
- Wholesale Fuel
- Petroleum
- Retail Real Estate
- Master Limited Partnership
website: https://www.crossamericapartners.com
---
