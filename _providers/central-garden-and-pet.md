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
  href: https://artifacts.apis.io/central-garden-and-pet/plans/central-garden-and-pet-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/central-garden-and-pet-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/central-garden-and-pet/rate-limits/central-garden-and-pet-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/central-garden-and-pet-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/central-garden-and-pet/finops/central-garden-and-pet-finops.yml
  title: ''
  type: FinOps
  url: finops/central-garden-and-pet-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.central.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/central-garden-and-pet
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/centralgardenandpet/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.central.com/central-privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.central.com/terms-of-use
- group: company
  title: ''
  type: Newsroom
  url: https://ir.central.com/news-events/press-releases
- group: other
  title: ''
  type: Leadership
  url: https://www.central.com/about-us/leadership-team
- group: company
  title: ''
  type: Investors
  url: https://ir.central.com/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.central.com/contact-us
- group: company
  title: ''
  type: Careers
  url: https://centralgardenandpet.ttcportals.com/search/jobs
- group: auth
  href: https://artifacts.apis.io/central-garden-and-pet/security/central-garden-and-pet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/central-garden-and-pet-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/central-garden-and-pet/regulatory/central-garden-and-pet-regulatory-posture.yml
  title: ''
  type: GlobalPrivacyControl
  url: regulatory/central-garden-and-pet-regulatory-posture.yml
- group: other
  href: https://artifacts.apis.io/central-garden-and-pet/regulatory/central-garden-and-pet-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/central-garden-and-pet-regulatory-posture.yml
coverage:
  checked: '2026-09-19'
  detail: Central Garden & Pet is a pet-supplies and lawn & garden manufacturer/distributor whose retailer connectivity is private EDI via E2open; the developer.central.com host this profile once recorded is NXDOMAIN, api.central.com serves a 39-byte IIS "Hello" placeholder last modified 2015-02-27 with every other path a stock 404, and the 101-URL sitemap of www.central.com contains no developer, API, docs or pricing page.
  evidence:
  - status: 200
    url: https://api.central.com/
  - status: 404
    url: https://api.central.com/openapi.json
  - status: 0
    url: https://developer.central.com/
  - status: 302
    url: https://www.central.com/.well-known/security.txt
  - status: 200
    url: https://www.central.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-04-19'
description: 'Central Garden & Pet Company (Nasdaq: CENT, CENTA) is a Walnut Creek, California manufacturer and distributor of branded pet supplies and lawn & garden products — Nylabone, Kaytee, Aqueon, Four Paws, Farnam, Pennington, Amdro, Sevin and Ferry-Morse among roughly seventy brands — with its own nationwide pet and garden distribution network. It is a consumer-products company, not a software company: it publishes no developer portal, public API, SDK, package, OpenAPI, AsyncAPI, GraphQL, MCP server, A2A agent card or llms.txt, and retailer and distributor connectivity is EDI through E2open under private contract. The host developer.central.com once recorded here does not resolve, and api.central.com, on Central''s own network block, serves only a 2015-era IIS placeholder page, so no API entry is carried. On the horizontal regulatory layer its privacy notice states the Global Privacy Control signal is honored and links a OneTrust portal for CCPA and GDPR data subject requests.'
finops:
- has_sources: true
  method: generated
  name: Central Garden And Pet Finops
  primary_unit: ''
  service_category: Consumer Goods (Pet + Garden)
  slug: central-garden-and-pet-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/central-garden-and-pet.png
layout: provider
modified: '2026-09-19'
name: Central Garden and Pet
nav: Providers
network: true
overview: Central Garden and Pet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Pet Products, Garden, Consumer, Consumer Goods, and Lawn and Garden.
plans:
- name: Central Garden And Pet Plans Pricing
  plan_count: 0
  slug: central-garden-and-pet-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Central Garden And Pet Rate Limits
  slug: central-garden-and-pet-rate-limits
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  previous_composite: 10.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/central-garden-and-pet/central-garden-and-pet-2026-06-20T174129.png
security:
- kind: domain-security
  name: Central Garden And Pet Domain Security
  slug: central-garden-and-pet-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: central-garden-and-pet
tags:
- Pet Products
- Garden
- Consumer
- Consumer Goods
- Lawn and Garden
- Pet Supplies
- Distribution
- Manufacturing
website: https://www.central.com
---
