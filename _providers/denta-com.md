---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Denta platform (not publicly documented)
  name: Denta API
  slug: denta-api
- description: 'Denta API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Denta API
  slug: denta-com-api
artifact_total: 12
asyncapis:
- description: ''
  name: Denta Com Webhooks
  slug: denta-com-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/denta-com/well-known/denta-com-vercel-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/denta-com-vercel-security.txt
- group: commercial
  href: https://artifacts.apis.io/denta-com/plans/denta-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/denta-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/denta-com/rules/denta-com-rules.yml
  title: ''
  type: Spectral
  url: rules/denta-com-rules.yml
- group: design
  href: https://artifacts.apis.io/denta-com/json-ld/denta-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/denta-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/denta-com/vocabulary/denta-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/denta-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/denta-com/asyncapi/denta-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/denta-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/denta-com/data-model/denta-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/denta-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/denta-com/authentication/denta-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/denta-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/denta-com/conformance/denta-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/denta-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/denta-com/well-known/denta-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/denta-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/denta-com/hosts/denta-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/denta-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/denta-com/vendors/denta-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/denta-com-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://vercel.com/docs/getting-started-with-vercel.md?from=llms-txt
- group: docs
  title: ''
  type: Documentation
  url: https://dev.denta.com/
- group: docs
  title: ''
  type: APIReference
  url: https://vercel.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/denta-com/security/denta-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/denta-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://denta.com
- group: company
  title: ''
  type: Blog
  url: https://www.denta.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.denta.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.denta.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.denta.com/legal/privacy
coverage:
  checked: '2026-10-29'
  detail: Docs are rendered via JavaScript and no machine‑readable OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://www.denta.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Denta, Inc. administers self-funded dental benefit plans for US employers. It offers a SaaS platform that lets companies set up dental coverage for their teams in minutes, with claims processed in seconds. Based in San Francisco, Denta serves the US market with easy enrollment, claim management, and comprehensive dental benefits.
json_schemas:
- name: PostV1BillingBuyRequest
  property_count: 3
  slug: denta-com-post-v1-billing-buy-request
- name: PostV1BillingBuyResponse
  property_count: 3
  slug: denta-com-post-v1-billing-buy-response
- name: PostV1RegistrarDomainsPriceRequest
  property_count: 1
  slug: denta-com-post-v1-registrar-domains-price-request
- name: PostV1RegistrarDomainsSearchRequest
  property_count: 1
  slug: denta-com-post-v1-registrar-domains-search-request
jsonld:
- class_count: 4
  name: Denta Com Context
  property_count: 7
  slug: denta-com-context
layout: provider
modified: '2026-10-29'
name: Denta
nav: Providers
network: true
overview: 'Denta is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Dental, Benefits, Software-as-a-Service, Healthcare, and Employer.


  The Denta catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Denta''s developer surface includes authentication, getting-started guide, documentation, API reference, engineering blog, signup flow, and 15 more developer resources.'
plans:
- name: Denta Com Plans Pricing
  plan_count: 1
  slug: denta-com-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Denta API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: denta-com-rules
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 57.8
    catalog_earned_first_party: 8.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 38.2
    contract_governance: 22.0
    contract_quality: 27.9
    developer_ergonomics: 27.4
    discoverability: 53.6
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 37.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/denta-com/denta-com-2026-11-03T130526.png
security:
- kind: authentication
  name: Denta Com Authentication
  slug: denta-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Denta Com Domain Security
  slug: denta-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: denta-com
tags:
- Dental
- Benefits
- Software-as-a-Service
- Healthcare
- Employer
website: https://denta.com
---
