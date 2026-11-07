---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: REST API providing Vietnamese economic data such as exchange rates, commodities, and market prices.
  name: DuLieu API
  slug: dulieu-api
- description: 'dulieu-dev API as documented publicly: 79 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: dulieu-dev API
  slug: dulieu-dev-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/dulieu-dev/rules/dulieu-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/dulieu-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/dulieu-dev/json-ld/dulieu-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dulieu-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/dulieu-dev/vocabulary/dulieu-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dulieu-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dulieu-dev/data-model/dulieu-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dulieu-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/dulieu-dev/conformance/dulieu-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dulieu-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dulieu-dev/llms/dulieu-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dulieu-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/dulieu-dev/hosts/dulieu-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dulieu-dev-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dulieu.dev/page/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://dulieu.dev/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dulieu.dev/page/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://dulieu.dev/blog
- group: auth
  href: https://artifacts.apis.io/dulieu-dev/security/dulieu-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dulieu-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dulieu.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://dulieu.dev/api/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dulieu.dev/api/docs
coverage:
  checked: '2026-10-29'
  detail: API documentation page renders a large HTML shell requiring JavaScript to view specifications.
  evidence:
  - status: 200
    url: https://dulieu.dev/api/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: DuLieu.dev provides a Vietnamese economic data dashboard offering exchange rates, gold, silver, weather, fuel, coffee, pepper, groceries, drugs, electronics and more. It aggregates public economic indicators and market prices, presenting them via a web interface and API for developers to integrate Vietnamese market data into applications.
image: https://dulieu.dev/public/og-image.svg
json_schemas:
- name: GetApiCosmeticsCompareResponse
  property_count: 10
  slug: dulieu-dev-get-api-cosmetics-compare-response
- name: GetApiCosmeticsSummaryResponse
  property_count: 7
  slug: dulieu-dev-get-api-cosmetics-summary-response
- name: GetApiElectronicsSummaryResponse
  property_count: 7
  slug: dulieu-dev-get-api-electronics-summary-response
- name: GetApiRealestateByIdSourceidResponse
  property_count: 11
  slug: dulieu-dev-get-api-realestate-by-id-sourceid-response
- name: GetApiRealestateFacetsResponse
  property_count: 6
  slug: dulieu-dev-get-api-realestate-facets-response
- name: GetApiRealestateSuggestResponse
  property_count: 7
  slug: dulieu-dev-get-api-realestate-suggest-response
jsonld:
- class_count: 77
  name: Dulieu Dev Context
  property_count: 96
  slug: dulieu-dev-context
layout: provider
modified: '2026-10-29'
name: dulieu-dev
nav: Providers
network: true
overview: 'dulieu-dev is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Vietnam, and Economics.


  The dulieu-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  dulieu-dev''s developer surface includes engineering blog, documentation, API reference, and 12 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: dulieu-dev API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: dulieu-dev-rules
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 9.5
    discoverability: 55.4
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - vietnam
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 25.3
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/dulieu-dev/dulieu-dev-2026-11-03T131119.png
security:
- kind: domain-security
  name: Dulieu Dev Domain Security
  slug: dulieu-dev-domain-security
  summary_line: TLSv1.3
slug: dulieu-dev
tags:
- Company
- Data
- Vietnam
- Economics
website: https://dulieu.dev/
---
