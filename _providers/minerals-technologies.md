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
  href: https://artifacts.apis.io/minerals-technologies/plans/minerals-technologies-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/minerals-technologies-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/minerals-technologies/rate-limits/minerals-technologies-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/minerals-technologies-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/minerals-technologies/finops/minerals-technologies-finops.yml
  title: ''
  type: FinOps
  url: finops/minerals-technologies-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.mineralstech.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mineralstech.com/docs/default-source/default-document-library/privacy-notice.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mineralstech.com/docs/default-source/default-document-library/terms-of-use.pdf
- group: operate
  title: ''
  type: Support
  url: https://www.mineralstech.com/contact
- group: company
  title: ''
  type: Careers
  url: https://www.mineralstech.com/careers
- group: company
  title: ''
  type: Newsroom
  url: https://www.mineralstech.com/investors/news
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/minerals-technologies
- group: auth
  href: https://artifacts.apis.io/minerals-technologies/security/minerals-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/minerals-technologies-domain-security.yml
coverage:
  checked: '2026-09-17'
  detail: Minerals Technologies is an industrial specialty-minerals manufacturer whose 1,954-URL sitemap holds product, CAD and investor pages but no developer, API or portal page; the api.mineralstech.com and developer.mineralstech.com hosts the prior record carried do not resolve in DNS, and every contract, llms.txt, security.txt and agent-card path on www.mineralstech.com returns the site's own 404 while the remaining /.well-known/* paths answer only an Imperva bot-challenge frame.
  evidence:
  - status: 0
    url: https://api.mineralstech.com/
  - status: 0
    url: https://developer.mineralstech.com/docs
  - status: 404
    url: https://www.mineralstech.com/openapi.json
  - status: 404
    url: https://www.mineralstech.com/llms.txt
  - status: 404
    url: https://www.mineralstech.com/.well-known/security.txt
  - status: 404
    url: https://www.mineralstech.com/.well-known/agent-card.json
  - status: 200
    url: https://www.mineralstech.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-04-19'
description: 'Minerals Technologies Inc. (NYSE: MTX) is a New York-headquartered, Fortune 1000 resource- and technology-based company that develops, produces and markets specialty minerals, mineral-based and synthetic mineral products and related systems and services across two segments, Consumer & Specialties (household and personal care, specialty additives) and Engineered Solutions (high-temperature technologies, environmental and infrastructure), through brands including Specialty Minerals, Minteq, CETCO and AMCOL, with more than 110 locations worldwide. It sells physical products through direct sales and distributors and publishes no developer portal, public API, SDK or machine-readable contract.'
finops:
- has_sources: true
  method: generated
  name: Minerals Technologies Finops
  primary_unit: ''
  service_category: Industrial Materials
  slug: minerals-technologies-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/minerals-technologies.png
layout: provider
modified: '2026-09-17'
name: Minerals Technologies
nav: Providers
network: true
overview: 'Minerals Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Specialty Minerals, Chemicals, Industrial, Manufacturing, and Materials.


  Minerals Technologies'' developer surface includes support and 10 more developer resources.'
plans:
- name: Minerals Technologies Plans Pricing
  plan_count: 0
  slug: minerals-technologies-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Minerals Technologies Rate Limits
  slug: minerals-technologies-rate-limits
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 49.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 8.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/minerals-technologies/minerals-technologies-2026-06-20T185602.png
security:
- kind: domain-security
  name: Minerals Technologies Domain Security
  slug: minerals-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: minerals-technologies
tags:
- Specialty Minerals
- Chemicals
- Industrial
- Manufacturing
- Materials
- Mining
- B2B
website: https://www.mineralstech.com
---
