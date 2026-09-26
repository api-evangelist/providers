---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 3
common:
- group: other
  title: ''
  type: Customers
  url: https://calumet.com/products/
- group: other
  title: ''
  type: Resources
  url: https://calumet.com/resources/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/calumet-specialty-products-partners/refs/heads/main/security/calumet-specialty-products-partners-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calumet-specialty-products-partners-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.calumet.com/
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Calumet_Specialty_Products_Partners
- group: company
  title: ''
  type: Investor Relations
  url: https://calumet.investorroom.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/calumet
- group: other
  title: ''
  type: Royal Purple
  url: https://www.royalpurple.com/
- group: other
  title: ''
  type: Bel-Ray
  url: https://www.belray.com/
- group: other
  title: ''
  type: TruFuel
  url: https://www.trufuel50.com/
- group: company
  title: ''
  type: Blog
  url: https://www.calumet.com/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://calumet.com/termsofsale/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calumet.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://calumet.com/contact-us/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/calumet-specialty-products-partners/refs/heads/main/llms/calumet-specialty-products-partners-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/calumet-specialty-products-partners-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/calumet-specialty-products-partners/refs/heads/main/plans/calumet-specialty-products-partners-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/calumet-specialty-products-partners-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/calumet-specialty-products-partners/refs/heads/main/rate-limits/calumet-specialty-products-partners-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/calumet-specialty-products-partners-rate-limits.yml
coverage:
  checked: '2026-09-06'
  detail: 'Calumet manufactures and sells physical specialty hydrocarbons — base oils, solvents, waxes, esters, asphalt and fuels — so there is nothing to expose programmatically: api.calumet.com and developer.calumet.com are NXDOMAIN, the Customer Tools page offers a credit application and tax certificates rather than an integration, and the only machine-readable HTTP surface anywhere on calumet.com is the marketing site''s stock WordPress /wp-json/ CMS namespace.'
  evidence:
  - status: 404
    url: https://calumet.com/openapi.json
  - status: 404
    url: https://calumet.com/.well-known/api-catalog
  - status: 404
    url: https://calumet.com/llms.txt
  - status: 200
    url: https://calumet.com/resources/customer-tools/
  - status: 200
    url: https://calumet.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2024-01-01'
description: 'Calumet, Inc. (NASDAQ: CLMT) is a publicly traded U.S. manufacturing company established in 1919, headquartered in Indianapolis, Indiana. The firm specializes in the manufacture of lubricating oils, solvents, waxes, packaged and synthetic specialty products, fuels, renewable diesel, and fuel-related products. It operates 12 production facilities across North America and serves approximately 2,700 global customers in over 90 countries through brands including Royal Purple, Bel-Ray, Penreco, Orchex, and TruFuel. Calumet does not publish a public developer API program; commercial integrations are handled via B2B portals and EDI.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/calumet-specialty-products-partners.png
layout: provider
modified: '2026-09-06'
name: Calumet Specialty Products Partners
nav: Providers
network: true
overview: 'Calumet Specialty Products Partners is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Asphalt, Fuel, Hydrocarbons, Lubricants, and Manufacturing.


  Calumet Specialty Products Partners'' developer surface includes engineering blog, support, and 15 more developer resources.'
plans:
- name: Calumet Specialty Products Partners Plans Pricing
  plan_count: 0
  slug: calumet-specialty-products-partners-plans-pricing
press:
- date: ''
  title: Calumet To Award Four Stem Scholarships To Area Seniors
  url: https://calumet.com/calumet-to-award-four-stem-scholarships-to-area-seniors/
- date: ''
  title: Calumet Specialty Products Partners Management ...
  url: https://seekingalpha.com/article/1814362-calumet-specialty-products-partners-management-discusses-q3-2013-results-earnings-call
- date: ''
  title: Calumet Announces Sale of Assets Related to Industrial Portion of its Royal Purple® Business
  url: https://calumet.com/calumet-announces-sale-of-assets-related-to-industrial-portion-of-its-royal-purple-business/
- date: ''
  title: Calumet Dickinson Receives Environmental Award for Recycling 28M Pounds of Sustainable Materials
  url: https://calumet.com/calumet-dickinson-receives-environmental-award-for-recycling-28m-pounds-of-sustainable-materials/
- date: ''
  title: Montana Renewables Announces Closing of $1.44 Billion DOE Loan Facility for Renewable Fuels and Biomass Energy Facility
  url: https://calumet.com/montana-renewables-announces-closing-of-1-44-billion-doe-loan-facility-for-renewable-fuels-and-biomass-energy-facility/
- date: ''
  title: TRUFUEL® Announces Record-Breaking Sales as Rapid Growth Continues
  url: https://calumet.com/trufuel-announces-record-breaking-sales-as-rapid-growth-continues/
- date: ''
  title: Calumet Montana and Department of Revenue Finalize Property Tax Assessment
  url: https://calumet.com/calumet-montana-and-department-of-revenue-finalize-property-tax-assessment/
- date: ''
  title: Give Your Valentine a Gift With Meaning
  url: https://calumet.com/give-your-valentine-a-gift-with-meaning/
random_paper: 11
rate_limits:
- limit_count: 0
  name: Calumet Specialty Products Partners Rate Limits
  slug: calumet-specialty-products-partners-rate-limits
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 10.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/calumet-specialty-products-partners/refs/heads/main/screenshots/calumet-specialty-products-partners-2026-06-20T173902.png
security:
- kind: domain-security
  name: Calumet Specialty Products Partners Domain Security
  slug: calumet-specialty-products-partners-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: calumet-specialty-products-partners
tags:
- Asphalt
- Fuel
- Hydrocarbons
- Lubricants
- Manufacturing
- Petroleum
- Renewable Diesel
- Solvents
- Specialty Chemicals
- Waxes
website: https://www.calumet.com/
---
