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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Divine Services valet and chauffeur platform, documented at the services page.
  name: Divine Services API
  slug: divine-services-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/divine-services/hosts/divine-services-hosts.yml
  title: ''
  type: Hosts
  url: hosts/divine-services-hosts.yml
- group: other
  href: https://artifacts.apis.io/divine-services/vendors/divine-services-vendors.yml
  title: ''
  type: Vendors
  url: vendors/divine-services-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.divinevalet.com/team
- group: auth
  href: https://artifacts.apis.io/divine-services/security/divine-services-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/divine-services-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.divinevalet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.divinevalet.com/services
- group: start
  title: ''
  type: GettingStarted
  url: https://www.divinevalet.com/become-a-valet
- group: operate
  title: ''
  type: Support
  url: https://www.divinevalet.com/contact2
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.divinevalet.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.divinevalet.com/terms-of-use
- group: operate
  title: ''
  type: FAQ
  url: https://www.divinevalet.com/faq
coverage:
  checked: '2026-10-23'
  detail: Documentation pages exist but no machine‑readable OpenAPI, GraphQL, or AsyncAPI spec is published.
  evidence:
  - status: 200
    url: https://www.divinevalet.com/services
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-23'
description: Divine Services Corporation provides valet parking, chauffeur, and on‑demand parking services across Ohio and beyond. Founded in 2009, the company offers event valet, restaurant parking, and technology‑enabled solutions for property managers and businesses, emphasizing professionalism, integrity, and customer satisfaction. Their services include dedicated parking staff, mobile scheduling, and integrated payment platforms to streamline the valet experience for clients.
image: http://static1.squarespace.com/static/5d531d6dcab07100012c58c2/t/66c0f2bcbc76747967fdaaf6/1723921084851/34455.jpg?format=1500w
layout: provider
modified: '2026-10-23'
name: Divine Services
nav: Providers
network: true
overview: 'Divine Services is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Valet, Parking, Chauffeur, Ohio, and Services.


  Divine Services'' developer surface includes documentation, getting-started guide, support, FAQ, and 7 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Divine Services Domain Security
  slug: divine-services-domain-security
  summary_line: TLSv1.3 · HSTS
slug: divine-services
tags:
- Valet
- Parking
- Chauffeur
- Ohio
- Services
website: https://www.divinevalet.com/
---
