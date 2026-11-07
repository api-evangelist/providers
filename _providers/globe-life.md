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
  href: https://artifacts.apis.io/globe-life/finops/globe-life-finops.yml
  title: ''
  type: FinOps
  url: finops/globe-life-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://home.globelifeinsurance.com/articles
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Globe_Life
- group: other
  title: ''
  type: StockExchange
  url: https://www.nyse.com/quote/XNYS:GL
- group: company
  title: ''
  type: Website
  url: https://www.globelifeinsurance.com
- group: company
  title: ''
  type: About
  url: https://home.globelifeinsurance.com/about
- group: operate
  title: ''
  type: Support
  url: https://home.globelifeinsurance.com/customer-service
- group: operate
  title: ''
  type: FAQ
  url: https://home.globelifeinsurance.com/faq
- group: company
  title: ''
  type: Newsroom
  url: https://home.globelifeinsurance.com/press-releases
- group: company
  title: ''
  type: Careers
  url: https://careers.globelifeinsurance.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.globelifeinsurance.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://home.globelifeinsurance.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://home.globelifeinsurance.com/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Globe-Life
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/globelife
- group: auth
  href: https://artifacts.apis.io/globe-life/security/globe-life-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/globe-life-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/globe-life/plans/globe-life-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/globe-life-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/globe-life/rate-limits/globe-life-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/globe-life-rate-limits.yml
coverage:
  checked: '2026-09-14'
  detail: Globe Life runs consumer and agent web products (home.globelifeinsurance.com, the myaccount Vite SPA, the ln./agency.ailife.com agent locators, the eProvider remittance portal) but ships no developer program at all — /developers, /api, /pricing, /status and /changelog are hard 404s on the live host, every RFC 8615 well-known path missed on all eleven hosts probed, and the api. and developer. subdomains this profile previously recorded as its API base and portal are wildcard DNS with no service behind them, answering a generic 466-byte HTTP 500 on every path including /docs and /openapi.json.
  evidence:
  - status: 200
    url: https://home.globelifeinsurance.com/
  - status: 404
    url: https://home.globelifeinsurance.com/developers
  - status: 404
    url: https://home.globelifeinsurance.com/api
  - status: 404
    url: https://home.globelifeinsurance.com/openapi.json
  - status: 404
    url: https://home.globelifeinsurance.com/swagger.json
  - status: 404
    url: https://home.globelifeinsurance.com/llms.txt
  - status: 404
    url: https://home.globelifeinsurance.com/.well-known/agent-card.json
  - status: 404
    url: https://home.globelifeinsurance.com/.well-known/agent.json
  - status: 404
    url: https://home.globelifeinsurance.com/.well-known/api-catalog
  - status: 404
    url: https://home.globelifeinsurance.com/.well-known/security.txt
  - status: 404
    url: https://home.globelifeinsurance.com/zz-api-evangelist-control-9f3a
  - status: 500
    url: https://developer.globelifeinsurance.com/docs
  - status: 500
    url: https://api.globelifeinsurance.com/openapi.json
  - status: 200
    url: https://myaccount.globelifeinsurance.com/zz-api-evangelist-control-9f3a
  - status: 404
    url: https://www.ailife.com/openapi.json
  - status: 404
    url: https://eprovider.globelifeinc.com/.well-known/api-catalog
  reason: no-developer-program
  state: none
created: '2026-04-19'
description: 'Globe Life Inc. (NYSE: GL) is a McKinney, Texas insurance holding company and Fortune 1000 constituent. Its wholly owned subsidiaries — Globe Life And Accident Insurance Company, American Income Life, Globe Life Liberty National Division, United American and Family Heritage — sell individual life, accident, supplemental health and Medicare Supplement policies direct to consumers and through captive and independent agents. Globe Life''s public digital surface is entirely consumer- and agent-facing: quote tools, the myaccount policyholder portal, an agent locator, the eProvider remittance portal and a mobile app. As of the 2026-09-14 probe Globe Life publishes no developer portal, no API reference and no machine-readable contract of any kind; partner and distributor integrations are governed by bilateral carrier agreements rather than by a public developer program.'
finops:
- has_sources: true
  method: generated
  name: Globe Life Finops
  primary_unit: ''
  service_category: Insurance
  slug: globe-life-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/globe-life.png
layout: provider
modified: '2026-10-06'
name: Globe Life
nav: Providers
network: true
overview: 'Globe Life is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Life Insurance, Financial Services, Supplemental Health, and Medicare Supplement.


  Globe Life''s developer surface includes engineering blog, support, FAQ, and 15 more developer resources.'
plans:
- name: Globe Life Plans Pricing
  plan_count: 0
  slug: globe-life-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Globe Life Rate Limits
  slug: globe-life-rate-limits
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 9
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
    developer_ergonomics: 7.1
    discoverability: 49.1
    operational_transparency: 2.6
  previous_composite: 10.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/globe-life/globe-life-2026-06-20T181929.png
security:
- kind: domain-security
  name: Globe Life Domain Security
  slug: globe-life-domain-security
  summary_line: TLSv1.3
slug: globe-life
tags:
- Insurance
- Life Insurance
- Financial Services
- Supplemental Health
- Medicare Supplement
- Insurance Carrier
- Fortune 1000
website: https://www.globelifeinsurance.com
---
