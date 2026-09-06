---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: AO Smith's iCOMM connected technology platform enables remote monitoring and control of compatible AO Smith water heaters through the A. O. Smith and iCOMM Connectivity mobile apps — tracking water an
  name: AO Smith iCOMM Connected Technology
  slug: ao-smith-icomm-connected-technology
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.aosmith.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ao-smith-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/ao-smith-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ao-smith-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/a-o-smith-corporation
- group: start
  title: ''
  type: Portal
  url: https://www.aosmith.com
- group: operate
  title: ''
  type: Support
  url: https://www.aosmith.com/about-us/contact.html
- group: company
  title: ''
  type: Blog
  url: https://www.aosmith.com/news.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aosmith.com/terms-and-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aosmith.com/privacy-policy
coverage:
  checked: '2026-09-02'
  detail: A. O. Smith ships connected water heaters but no developer program — the iCOMM platform is an end-user mobile app whose only backend is an undocumented Apollo GraphQL endpoint with introspection disabled, and the Red Hat 3scale portal on A. O. Smith's own OpenShift cluster is a stock unconfigured install advertising nothing but 3scale's built-in "Echo API" demo.
  evidence:
  - status: 200
    url: https://r2.wh8.co/graphql
  - status: 200
    url: https://3scale.apps.aosmith-prod.hd1m.p1.openshiftapps.com/
  - status: 0
    url: https://api.aosmith.com/
  - status: 404
    url: https://www.aosmith.com/.well-known/api-catalog
  - status: 404
    url: https://www.hotwater.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-03-23'
description: 'A. O. Smith Corporation (NYSE: AOS) is a global manufacturer of residential and commercial water heaters, boilers, water treatment and air purification products, headquartered in Milwaukee, Wisconsin. Its connected-product line runs on the iCOMM platform, which lets homeowners and plumbing professionals monitor and control compatible water heaters — temperature, vacation mode, leak and maintenance alerts, energy-use history — from a mobile app. A. O. Smith operates no public developer program: there is no developer portal, API reference, OpenAPI, SDK or MCP server, and the iCOMM backend is an undocumented GraphQL endpoint reachable only by the mobile apps and by community clients that reverse-engineered it.'
finops:
- name: Ao Smith Finops
  service_category: API
  slug: ao-smith-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ao-smith.png
layout: provider
modified: '2026-09-02'
name: AO Smith
nav: Providers
network: true
overview: 'AO Smith publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include IoT, Manufacturing, Smart Home, Water Heaters, and Connected Products.


  AO Smith''s developer surface includes developer portal, support, engineering blog, and 7 more developer resources.'
plans:
- name: Ao Smith Plans Pricing
  plan_count: 0
  slug: ao-smith-plans-pricing
press:
- date: '2026-05-25'
  title: Artificial Intelligence will redefine the marketing space
  url: https://www.exchange4media.com/digital-news/artificial-intelligence-will-redefine-the-marketing-space-143435.html
- date: '2026-05-25'
  title: A. O. Smith hires Chris Howe as new chief digital ...
  url: https://www.pmmag.com/articles/106872-a-o-smith-hires-chris-howe-as-new-chief-digital-information-officer
- date: '2026-05-25'
  title: A. O. Smith and The Water Council announce ... - Investor Relations
  url: https://investor.aosmith.com/node/17986/pdf
- date: '2026-05-25'
  title: 'A.O. Smith India on Instagram: "Innovation That Preserves ...'
  url: https://www.instagram.com/reel/DXZPysADbjW/
- date: '2026-05-25'
  title: The Water Council and A. O. Smith Kick Off 2018 Competition ...
  url: https://investor.aosmith.com/news-releases/news-release-details/water-council-and-o-smith-kick-2018-competition-supporting
random_paper: 4
rate_limits:
- limit_count: 0
  name: Ao Smith Rate Limits
  slug: ao-smith-rate-limits
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.1
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 11.8
  provenance:
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/ao-smith/refs/heads/main/screenshots/ao-smith-2026-06-20T172035.png
security:
- kind: domain-security
  name: Ao Smith Domain Security
  slug: ao-smith-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: ao-smith
tags:
- IoT
- Manufacturing
- Smart Home
- Water Heaters
- Connected Products
- Water Treatment
- Boilers
- Consumer Hardware
website: https://www.aosmith.com/
---
