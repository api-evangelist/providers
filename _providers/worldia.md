---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Worldia production REST API. An API Platform (Symfony) deployment that content-negotiates application/vnd.worldia+json, application/ld+json (Hydra) and application/problem+json. A subset of collection
  name: Worldia API
  slug: worldia-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/worldia/llms/worldia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/worldia-llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://help.worldia.com/
- group: operate
  href: https://artifacts.apis.io/worldia/lifecycle/worldia-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/worldia-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/worldia/well-known/worldia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/worldia-well-known.yml
- group: other
  href: https://artifacts.apis.io/worldia/hosts/worldia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/worldia-hosts.yml
- group: other
  href: https://artifacts.apis.io/worldia/vendors/worldia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/worldia-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://corp.worldia.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/worldia
- group: operate
  title: ''
  type: Support
  url: https://corp.worldia.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://share.hsforms.com/1MISGoMI5Spmh025GTEiHog4nazr
- group: commercial
  title: ''
  type: TermsOfService
  url: https://corp.worldia.com/hubfs/website%20-%20v3/legal/terms-of-use-EN.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://static.worldia.com/documents/privacy-policy/GB.pdf
- group: design
  href: https://artifacts.apis.io/worldia/json-ld/worldia-json-ld.yml
  title: ''
  type: JSONLD
  url: json-ld/worldia-json-ld.yml
- group: design
  href: https://artifacts.apis.io/worldia/vocabulary/worldia-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/worldia-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/worldia/data-model/worldia-data-model.yml
  title: ''
  type: DataModel
  url: data-model/worldia-data-model.yml
- group: design
  href: https://artifacts.apis.io/worldia/conventions/worldia-conventions.yml
  title: ''
  type: Conventions
  url: conventions/worldia-conventions.yml
- group: design
  href: https://artifacts.apis.io/worldia/errors/worldia-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/worldia-problem-types.yml
- group: design
  href: https://artifacts.apis.io/worldia/conformance/worldia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/worldia-conformance.yml
- group: design
  href: https://artifacts.apis.io/worldia/lifecycle/worldia-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/worldia-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/worldia/plans/worldia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/worldia-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/worldia/security/worldia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/worldia-domain-security.yml
coverage:
  checked: '2026-10-20'
  detail: api.worldia.com is a live API Platform deployment but serves no OpenAPI or Hydra documentation (/docs.json and /docs.jsonld return 404 problem+json) and Worldia publishes no developer docs, only a French/English traveler help center.
  evidence:
  - status: 404
    url: https://api.worldia.com/docs.json
  - status: 404
    url: https://api.worldia.com/docs.jsonld
  - status: 404
    url: https://api.worldia.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-04'
description: Worldia is a Paris-based B2B2C travel technology company, founded in 2012 and headquartered in Montreuil, France, that lets travel distributors, retailers and agents build, price and book personalized tailor-made trips across more than 80 destinations from a single connected platform. Its product is a white-label trip-building and booking stack — a curated multi-supplier catalogue of accommodations, activities, transfers, car hire, rail and flights, combined with itinerary templates, channel-specific branding and 24/7 traveler support — delivered to each partner as a branded storefront. The platform is driven by a production REST API at api.worldia.com built on API Platform (Symfony) that content-negotiates JSON-LD and Hydra and is multi-tenanted through a required X-Channel header; Worldia publishes no developer portal, OpenAPI or public API reference, so the API is reached through commercial partnership rather than self-service signup.
image: https://f.hubspotusercontent20.net/hubfs/9239422/WORLDIA/GENERAL/mainlogo.png
jsonld:
- class_count: 64
  name: Worldia Accommodation Context
  property_count: 1
  slug: worldia-context-accommodation
- class_count: 39
  name: Worldia Agent Context
  property_count: 0
  slug: worldia-context-agent
- class_count: 31
  name: Worldia Airport Context
  property_count: 0
  slug: worldia-context-airport
- class_count: 13
  name: Worldia Car Context
  property_count: 0
  slug: worldia-context-car
- class_count: 84
  name: Worldia Channel Context
  property_count: 13
  slug: worldia-context-channel
- class_count: 23
  name: Worldia Customer Context
  property_count: 1
  slug: worldia-context-customer
- class_count: 13
  name: Worldia Document Context
  property_count: 0
  slug: worldia-context-document
- class_count: 69
  name: Worldia Location Context
  property_count: 1
  slug: worldia-context-location
- class_count: 30
  name: Worldia Payment Context
  property_count: 1
  slug: worldia-context-payment
- class_count: 8
  name: Worldia Place Context
  property_count: 0
  slug: worldia-context-place
- class_count: 29
  name: Worldia Route Context
  property_count: 2
  slug: worldia-context-route
- class_count: 34
  name: Worldia Template Context
  property_count: 4
  slug: worldia-context-template
- class_count: 24
  name: Worldia Theme Context
  property_count: 1
  slug: worldia-context-theme
- class_count: 42
  name: Worldia Train Context
  property_count: 2
  slug: worldia-context-train
- class_count: 45
  name: Worldia Transfer Context
  property_count: 4
  slug: worldia-context-transfer
- class_count: 104
  name: Worldia Trip Context
  property_count: 9
  slug: worldia-context-trip
layout: provider
modified: '2026-09-04'
name: Worldia
nav: Providers
network: true
overview: 'Worldia is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Tourism, Booking, Trip Planning, and Travel Technology.


  The Worldia catalog on APIs.io includes 16 JSON-LD contexts.


  Worldia''s developer surface includes documentation, support, signup flow, and 18 more developer resources.'
plans:
- name: Worldia Plans Pricing
  plan_count: 0
  slug: worldia-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Worldia Rate Limits
  slug: worldia-rate-limits
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.3
    catalog_earned_first_party: 0.0
    catalog_gap: 65.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 14.7
    developer_ergonomics: 14.3
    discoverability: 66.1
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 24.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/worldia/worldia-2026-10-11T195751.png
security:
- kind: authentication
  name: Worldia Authentication
  slug: worldia-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Worldia Domain Security
  slug: worldia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: worldia
tags:
- Travel
- Tourism
- Booking
- Trip Planning
- Travel Technology
- Hospitality
- B2B2C
- White Label
- Itinerary
- Distribution
website: https://corp.worldia.com/
---
