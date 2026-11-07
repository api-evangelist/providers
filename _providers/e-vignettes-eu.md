---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: E Vignettes Eu Agentic Access
  operation_count: 3
  slug: e-vignettes-eu-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://e-vignettes.eu/api/v1
  baseurl_source: declared
  description: Which countries are covered and how their toll systems work.
  name: Vignette ID Countries API
  slug: e-vignettes-eu-countries-api
- baseURL: https://e-vignettes.eu/api/v1
  baseurl_source: declared
  description: Live vignette and section-toll catalogue with prices.
  name: Vignette ID Products API
  slug: e-vignettes-eu-products-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/e-vignettes-eu/agentic-access/e-vignettes-eu-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/e-vignettes-eu-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/e-vignettes-eu/plans/e-vignettes-eu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/e-vignettes-eu-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/e-vignettes-eu/rules/e-vignettes-eu-rules.yml
  title: ''
  type: Spectral
  url: rules/e-vignettes-eu-rules.yml
- group: design
  href: https://artifacts.apis.io/e-vignettes-eu/json-ld/e-vignettes-eu-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/e-vignettes-eu-context.jsonld
- group: design
  href: https://artifacts.apis.io/e-vignettes-eu/vocabulary/e-vignettes-eu-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/e-vignettes-eu-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/e-vignettes-eu/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/e-vignettes-eu/data-model/e-vignettes-eu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/e-vignettes-eu-data-model.yml
- group: auth
  href: https://artifacts.apis.io/e-vignettes-eu/authentication/e-vignettes-eu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/e-vignettes-eu-authentication.yml
- group: design
  href: https://artifacts.apis.io/e-vignettes-eu/errors/e-vignettes-eu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/e-vignettes-eu-problem-types.yml
- group: design
  href: https://artifacts.apis.io/e-vignettes-eu/conformance/e-vignettes-eu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/e-vignettes-eu-conformance.yml
- group: agent
  href: https://artifacts.apis.io/e-vignettes-eu/llms/e-vignettes-eu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/e-vignettes-eu-llms.txt
- group: other
  href: https://artifacts.apis.io/e-vignettes-eu/a2a/e-vignettes-eu-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/e-vignettes-eu-a2a.yml
- group: agent
  href: https://artifacts.apis.io/e-vignettes-eu/well-known/e-vignettes-eu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/e-vignettes-eu-well-known.yml
- group: other
  href: https://artifacts.apis.io/e-vignettes-eu/hosts/e-vignettes-eu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/e-vignettes-eu-hosts.yml
- group: other
  href: https://artifacts.apis.io/e-vignettes-eu/vendors/e-vignettes-eu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/e-vignettes-eu-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://e-vignettes.eu/terms
- group: build
  title: ''
  type: SDKs
  url: https://e-vignettes.eu/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://e-vignettes.eu/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://e-vignettes.eu/pricing.md
- group: company
  title: ''
  type: Newsroom
  url: https://e-vignettes.eu/media
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eu-vignette
- group: company
  title: ''
  type: Blog
  url: https://e-vignettes.eu/blog
- group: auth
  href: https://artifacts.apis.io/e-vignettes-eu/security/e-vignettes-eu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/e-vignettes-eu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://e-vignettes.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://e-vignettes.eu/docs
- group: docs
  title: ''
  type: APIReference
  url: https://e-vignettes.eu/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://e-vignettes.eu/auth.md
- group: start
  title: ''
  type: DeveloperPortal
  url: https://e-vignettes.eu/developers
created: '2026-11-06'
description: Vignette ID provides a convenient platform for purchasing official digital road vignettes across nine European countries. Users can buy vignettes for multiple vehicles and countries in a single transaction, simplifying toll payments and compliance. The service aims to streamline cross‑border travel by offering a unified, online solution for road usage fees, backed by secure payment processing and multilingual support.
image: https://e-vignettes.eu/assets/banner-social.png
json_schemas:
- name: CountryDetail
  property_count: 12
  slug: e-vignettes-eu-country-detail
- name: CountryList
  property_count: 3
  slug: e-vignettes-eu-country-list
- name: ProductList
  property_count: 4
  slug: e-vignettes-eu-product-list
jsonld:
- class_count: 7
  name: E Vignettes Eu Context
  property_count: 30
  slug: e-vignettes-eu-context
layout: provider
modified: '2026-11-06'
name: Vignette ID
nav: Providers
network: true
overview: 'Vignette ID publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Countries API and Products API. Tagged areas include Company, Transportation, Payments, Europe, and Digital.


  The Vignette ID catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Vignette ID''s developer surface includes authentication, pricing, engineering blog, documentation, API reference, getting-started guide, and 22 more developer resources.'
plans:
- name: E Vignettes Eu Plans Pricing
  plan_count: 9
  slug: e-vignettes-eu-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Vignette ID API Rules
  rule_count: 58
  severity_counts:
    error: 55
    hint: 0
    info: 2
    warn: 1
  slug: e-vignettes-eu-rules
score:
  band: developing
  composite: 52.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 64.1
    developer_ergonomics: 66.0
    discoverability: 67.9
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: E Vignettes Eu Authentication
  slug: e-vignettes-eu-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: E Vignettes Eu Domain Security
  slug: e-vignettes-eu-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: get-country
  slug: e-vignettes-eu-get-country
slug: e-vignettes-eu
tags:
- Company
- Transportation
- Payments
- Europe
- Digital
website: https://e-vignettes.eu/
---
