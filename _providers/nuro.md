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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/nuro/hosts/nuro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nuro-hosts.yml
- group: other
  href: https://artifacts.apis.io/nuro/vendors/nuro-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nuro-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.nuro.ai/release-notes
- group: start
  title: ''
  type: GettingStarted
  url: https://www.nuro.ai/blog/onboarding-ai-employees-at-nuro
- group: auth
  href: https://artifacts.apis.io/nuro/security/nuro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nuro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nuro.ai
- group: company
  title: ''
  type: Newsroom
  url: https://nuro.ai/press
- group: company
  title: ''
  type: Blog
  url: https://medium.com/nuro
- group: other
  title: ''
  type: NuroDriver
  url: https://nuro.ai/nuro-driver
- group: build
  title: ''
  type: NuroToolkit
  url: https://nuro.ai/nuro-toolkit
- group: other
  title: ''
  type: Technology
  url: https://nuro.ai/technology
- group: other
  title: ''
  type: Safety
  url: https://nuro.ai/safety
- group: company
  title: ''
  type: Careers
  url: https://nuro.ai/careers
- group: operate
  title: ''
  type: Contact
  url: https://nuro.ai/contact
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/nuro
- group: company
  title: ''
  type: Website
  url: https://www.nuro.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.nuro.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nuro-ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nuro.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nuro.ai/terms
coverage:
  checked: '2026-10-20'
  detail: Nuro licenses the Nuro Driver and Toolkit through B2B deals; nuro.ai/developers is a 404, api.nuro.ai returns a 502, and no OpenAPI/AsyncAPI/GraphQL/MCP was found on nuro.ai, www.nuro.ai or api.nuro.ai.
  evidence:
  - status: 200
    url: https://nuro.ai
  - status: 404
    url: https://nuro.ai/developers
  - status: 502
    url: https://api.nuro.ai/
  reason: no-developer-program
  state: none
created: '2026-05-23'
description: Nuro is a Mountain View-based autonomy company that has pivoted from its original autonomous-goods-delivery vehicle program (R1, R2, R3) to a licensable, vehicle-agnostic autonomous driving stack. The Nuro Driver is an AI-first Level 4 self-driving system, validated through 5+ years of driverless deployments and more than 1.7 million autonomous miles with zero at-fault incidents, paired with the Nuro Toolkit suite of supporting technology. Partners and customers include Uber and Lucid (premium robotaxi program with production-intent vehicles announced for CES 2026), Mercedes- Benz, Toyota, Kroger, Domino's, and Walmart, with NVIDIA participation in recent funding rounds. Nuro has offices in Mountain View, San Francisco, Santa Clara, Las Vegas, Houston, Toronto, Washington DC, Shenzhen, Tokyo, and an upcoming Munich expansion. Nuro does not publish a public developer API; the Driver and Toolkit are commercialized through B2B licensing rather than a self-serve developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nuro.png
layout: provider
modified: '2026-10-20'
name: Nuro
nav: Providers
network: true
overview: 'Nuro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Autonomous Vehicles, Self-Driving, Robotaxi, Goods Delivery, and Licensing.


  Nuro''s developer surface includes changelog, getting-started guide, engineering blog, and 17 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 14.6
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
    developer_ergonomics: 14.3
    discoverability: 50.0
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 14.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/nuro/nuro-2026-06-20T190524.png
security:
- kind: domain-security
  name: Nuro Domain Security
  slug: nuro-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: nuro
tags:
- Autonomous Vehicles
- Self-Driving
- Robotaxi
- Goods Delivery
- Licensing
- Nuro Driver
- Nuro Toolkit
website: https://nuro.ai
---
