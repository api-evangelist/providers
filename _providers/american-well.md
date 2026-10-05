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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/american-well/refs/heads/main/security/american-well-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/american-well-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://business.amwell.com/
- group: company
  title: ''
  type: Blog
  url: https://business.amwell.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://business.amwell.com/about-us
- group: docs
  title: ''
  type: APIReference
  url: https://business.amwell.com/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://business.amwell.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://business.amwell.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://business.amwell.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://business.amwell.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://business.amwell.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://community.amwell.com/p/support
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/organization/american-well
created: '2026-09-24'
description: American Well, operating as Amwell, provides a comprehensive telehealth platform connecting patients, providers, and payers. Their services include virtual primary care, digital behavioral health, specialty consults, and integrated care solutions, enabling scalable, on-demand healthcare delivery across the United States.
layout: provider
modified: '2026-09-24'
name: American Well
nav: Providers
network: true
overview: 'American Well is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  American Well''s developer surface includes engineering blog, documentation, API reference, pricing, signup flow, support, and 6 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 2
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 35.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: American Well Domain Security
  slug: american-well-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: american-well
tags:
- Company
website: https://business.amwell.com/
---
