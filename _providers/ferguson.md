---
access_model:
  confidence: medium
  label: Partner approval required
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://developer.ferguson.com/faq
  - https://developer.ferguson.com/get-started
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 5.0
  scored_at: '2026-09-10'
api_count: 1
apis:
- description: A curated set of REST/JSON Enterprise APIs that let approved partners and software providers transact with Ferguson — product availability and vendor cost data, and electronic purchase-order submissio
  name: Ferguson Enterprise APIs
  slug: enterprise-apis
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ferguson-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ferguson-official
- group: company
  title: ''
  type: Website
  url: https://www.ferguson.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ferguson.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.ferguson.com/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ferguson.com/get-started
- group: company
  title: ''
  type: Blog
  url: https://developer.ferguson.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.ferguson.com/content/customer-support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ferguson.com/content/customer-support/website-information/terms-of-site-use/
- group: start
  title: ''
  type: SignUp
  url: https://www.ferguson.com/s/sign-up
- group: auth
  title: ''
  type: Authentication
  url: authentication/ferguson-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ferguson-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/ferguson-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ferguson-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ferguson-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ferguson-llms.txt
coverage:
  checked: '2026-09-09'
  detail: Ferguson's API catalog and its Swagger documentation live inside a Backstage developer portal whose backend answers HTTP 401 "Missing credentials" to every anonymous request (/api/catalog/entities, /api/search/query), and Ferguson grants portal access only to organizations that complete its partner review and approval process via api.team@ferguson.com.
  evidence:
  - status: 401
    url: https://developer.ferguson.com/api/catalog/entities?filter=kind=api
  - status: 401
    url: https://developer.ferguson.com/api/search/query?term=api
  - status: 404
    url: https://www.ferguson.com/.well-known/api-catalog
  reason: partner-login
  state: gated
created: '2026-03-21'
description: Ferguson is a Fortune 500 distributor of plumbing supplies, HVAC products, pipe, valves and fittings, waterworks, and building supplies serving professional contractors, residential homeowners, and commercial customers across the United States. Ferguson runs an Enterprise API program on Google Apigee, published through the Ferguson Developer Portal, that lets approved partners and software providers pull product availability and cost data and submit purchase orders electronically. Access is granted only to organizations that complete Ferguson's partner review and approval process, and the API catalog and its Swagger documentation are not readable without credentials.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ferguson.png
layout: provider
modified: '2026-09-09'
name: Ferguson
nav: Providers
network: true
overview: 'Ferguson publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Distribution, Plumbing, HVAC, Building Supplies, and Waterworks.


  Ferguson''s developer surface includes API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 10 more developer resources.'
plans:
- name: Ferguson Plans Pricing
  plan_count: 0
  slug: ferguson-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Ferguson Rate Limits
  slug: ferguson-rate-limits
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 11.2
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 5.0
  provenance:
    conformance: first-party
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ferguson Authentication
  slug: ferguson-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Ferguson Domain Security
  slug: ferguson-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ferguson
tags:
- Distribution
- Plumbing
- HVAC
- Building Supplies
- Waterworks
- Pipe Valves Fittings
- Wholesale Distribution
- B2B
- Fortune 500
website: https://www.ferguson.com
---
