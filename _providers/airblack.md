---
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airblack/refs/heads/main/security/airblack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airblack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.airblack.com/
- group: company
  title: ''
  type: About
  url: https://www.airblack.com/about
- group: operate
  title: ''
  type: Support
  url: https://www.airblack.com/contact
- group: company
  title: ''
  type: Blog
  url: https://blog.airblack.com/
- group: company
  title: ''
  type: BlogFeeds
  url: https://blog.airblack.com/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.airblack.com/terms/termsofservice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airblack.com/terms/privacypolicy
- group: other
  title: ''
  type: RefundPolicy
  url: https://www.airblack.com/terms/refundpolicy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.airblack.com/terms/cookiepolicy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airblack
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/airblack.club/
- group: other
  title: ''
  type: GooglePlay
  url: https://play.google.com/store/apps/details?id=com.airblack
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Airblack-Tech
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/airblack/refs/heads/main/packages/airblack-packages.yml
  title: ''
  type: Packages
  url: packages/airblack-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/airblack/refs/heads/main/llms/airblack-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airblack-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/airblack/refs/heads/main/regulatory/airblack-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/airblack-regulatory-posture.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/airblack
coverage:
  checked: '2026-09-19'
  detail: 'Airblack sells live makeup, beauty and culinary courses to consumers and ships no developer surface at all: api./developer./docs./app./mcp.airblack.com are all NXDOMAIN, every contract path 404s at the site''s Next.js catch-all, and the only backend it operates — service.ablck.com/new/api/, found by reading the site''s own JS chunks — is a private application service that answers every probed path with a JSON 404.'
  evidence:
  - status: 200
    url: https://www.airblack.com/
  - status: 404
    url: https://www.airblack.com/openapi.json
  - status: 404
    url: https://www.airblack.com/developers
  - status: 404
    url: https://www.airblack.com/.well-known/api-catalog
  - status: 404
    url: https://service.ablck.com/new/api/openapi.json
  - status: 200
    url: https://blog.airblack.com/feed/
  reason: no-developer-program
  state: none
created: '2026-09-19'
description: 'Airblack (Airblack Technologies Private Limited) is a Gurugram, India-based edtech company that runs an outcome-focused skilling academy for creators and micro-entrepreneurs, delivering live online makeup, beauty and culinary courses with professional certification through its website and Android/iOS app, plus a sister app, Zudo. Founded by Videt Jaiswal and backed by Info Edge Ventures and Elevation Capital (USD 5.2M Series A, 2021), it reports a community of 45,000+ students. Airblack is a consumer learning product, not a platform: it publishes no developer program, no public API documentation and no machine-readable API contract, and the backend its web app calls (service.ablck.com) is a private application service that answers every probed path with a JSON 404.'
image: https://d2i464mmj9hzgy.cloudfront.net/cloudinary/dtks0l86r/website-static-assets/Project_Website/Homepage/middleHQ_kwjdxb.webp
layout: provider
modified: '2026-09-19'
name: Airblack
nav: Providers
network: true
overview: 'Airblack is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, EdTech, Online Learning, Skilling, and Beauty.


  Airblack''s developer surface includes support, engineering blog, and 16 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 55.4
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 11.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Airblack Domain Security
  slug: airblack-domain-security
  summary_line: TLSv1.2
slug: airblack
tags:
- Education
- EdTech
- Online Learning
- Skilling
- Beauty
- Makeup
- Culinary
- Creator Economy
- India
- Company
website: https://www.airblack.com/
---
