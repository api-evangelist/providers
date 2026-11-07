---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Use MotaWord API to post and track your translation projects.
  name: MotaWord API
  slug: motaword-api
- baseURL: https://api.motaword.com
  baseurl_source: declared
  description: Use MotaWord API to post and track your translation projects.
  name: MotaWord API API
  slug: motaword-api-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/motaword/rules/motaword-rules.yml
  title: ''
  type: Spectral
  url: rules/motaword-rules.yml
- group: design
  href: https://artifacts.apis.io/motaword/json-ld/motaword-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/motaword-context.jsonld
- group: design
  href: https://artifacts.apis.io/motaword/vocabulary/motaword-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/motaword-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/motaword/conformance/motaword-conformance.yml
  title: ''
  type: Conformance
  url: conformance/motaword-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/motaword/plans/motaword-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/motaword-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/motaword/data-model/motaword-data-model.yml
  title: ''
  type: DataModel
  url: data-model/motaword-data-model.yml
- group: design
  href: https://artifacts.apis.io/motaword/errors/motaword-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/motaword-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/motaword/llms/motaword-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/motaword-llms.txt
- group: agent
  href: https://artifacts.apis.io/motaword/well-known/motaword-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/motaword-well-known.yml
- group: other
  href: https://artifacts.apis.io/motaword/hosts/motaword-hosts.yml
  title: ''
  type: Hosts
  url: hosts/motaword-hosts.yml
- group: other
  href: https://artifacts.apis.io/motaword/vendors/motaword-vendors.yml
  title: ''
  type: Vendors
  url: vendors/motaword-vendors.yml
- group: build
  href: https://artifacts.apis.io/motaword/packages/motaword-packages.yml
  title: ''
  type: SDKs
  url: packages/motaword-packages.yml
- group: build
  href: https://artifacts.apis.io/motaword/packages/motaword-packages.yml
  title: ''
  type: Packages
  url: packages/motaword-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.motaword.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.motaword.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.motaword.com:443/pricing
- group: start
  title: ''
  type: Login
  url: https://www.motaword.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.motaword.com:443/developer
- group: company
  title: ''
  type: Blog
  url: https://www.motaword.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MotaWord
- group: auth
  href: https://artifacts.apis.io/motaword/security/motaword-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/motaword-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://motaword.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.motaword.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.motaword.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.motaword.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.motaword.com/contact
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.motaword.com/openapi.yaml
  - status: 401
    url: https://docs.motaword.com/mcp
  - status: 403
    url: https://api.motaword.com/v1/graphql
  - status: 401
    url: https://api.motaword.com/mcp
  - status: 200
    url: https://motaword.com/
  reason: partner-login
  state: gated
created: '2026-10-28'
description: MotaWord provides professional document translation, AI‑powered machine translation, localization, and interpretation services for businesses and individuals. Their platform supports human translation, post‑editing, academic evaluation, certified legal translation, and a suite of AI tools for continuous localization in CI/CD pipelines. MotaWord also offers integrations with popular legal and practice management software, enabling seamless workflow automation.
image: https://d1qrzs23hpns6w.cloudfront.net/f/84976/2400x1350/3a6c6e19c2/motaword-home-page-og.png
json_schemas:
- name: ActiveWidget
  property_count: 38
  slug: motaword-active-widget
- name: FilterVendorRequest
  property_count: 64
  slug: motaword-filter-vendor-request
- name: InterpretSession
  property_count: 15
  slug: motaword-interpret-session
- name: Project
  property_count: 49
  slug: motaword-project
- name: User
  property_count: 26
  slug: motaword-user
- name: UserUpdateContent
  property_count: 24
  slug: motaword-user-update-content
jsonld:
- class_count: 120
  name: Motaword Context
  property_count: 431
  slug: motaword-context
layout: provider
modified: '2026-10-28'
name: MotaWord
nav: Providers
network: true
overview: 'MotaWord publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Translation, Localization, Artificial Intelligence, Software-as-a-Service, and Enterprise.


  The MotaWord catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MotaWord''s developer surface includes pricing, engineering blog, documentation, API reference, getting-started guide, support, and 20 more developer resources.'
plans:
- name: Motaword Plans Pricing
  plan_count: 2
  slug: motaword-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: MotaWord API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: motaword-rules
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.9
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 45.5
    developer_ergonomics: 29.8
    discoverability: 73.2
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 50.4
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/motaword/motaword-2026-11-03T135849.png
security:
- kind: domain-security
  name: Motaword Domain Security
  slug: motaword-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: motaword
tags:
- Translation
- Localization
- Artificial Intelligence
- Software-as-a-Service
- Enterprise
website: https://motaword.com/
---
