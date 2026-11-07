---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.sgpdirectory.com/v1
  baseurl_source: declared
  description: Public API for accessing Singapore Business Directory data. Date fields use YYYY-MM-DD. Datetime fields use ISO-8601 date-time. Rate-limit reset timestamps use Unix epoch milliseconds with field/heade
  name: SGP Directory API API
  slug: sgp-directory-api-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/sgpdirectory-com/llms/sgpdirectory-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sgpdirectory-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/sgpdirectory-com/well-known/sgpdirectory-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sgpdirectory-com-security.txt
- group: agent
  href: https://artifacts.apis.io/sgpdirectory-com/well-known/sgpdirectory-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sgpdirectory-com-well-known.yml
- group: design
  href: https://artifacts.apis.io/sgpdirectory-com/rules/sgpdirectory-com-rules.yml
  title: ''
  type: Spectral
  url: rules/sgpdirectory-com-rules.yml
- group: design
  href: https://artifacts.apis.io/sgpdirectory-com/json-ld/sgpdirectory-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sgpdirectory-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/sgpdirectory-com/vocabulary/sgpdirectory-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sgpdirectory-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/sgpdirectory-com/data-model/sgpdirectory-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sgpdirectory-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/sgpdirectory-com/conventions/sgpdirectory-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sgpdirectory-com-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://sgpdirectory.com/security
- group: auth
  href: https://artifacts.apis.io/sgpdirectory-com/authentication/sgpdirectory-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sgpdirectory-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/sgpdirectory-com/errors/sgpdirectory-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sgpdirectory-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sgpdirectory-com/conformance/sgpdirectory-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sgpdirectory-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/sgpdirectory-com/hosts/sgpdirectory-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sgpdirectory-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/sgpdirectory-com/vendors/sgpdirectory-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sgpdirectory-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sgpdirectory.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sgpdirectory.com/privacy
- group: start
  title: ''
  type: Login
  url: https://console.sgpdirectory.com/sign-in
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sgpdirectory.com/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sgpdirectory.com/
- group: company
  title: ''
  type: Website
  url: https://sgpdirectory.com/
- group: auth
  href: https://artifacts.apis.io/sgpdirectory-com/security/sgpdirectory-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sgpdirectory-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sgpdirectory-com/security/sgpdirectory-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sgpdirectory-com-domain-security.yml
created: '2026-10-30'
description: 'sgpdirectory-com provides a public API for Singapore Business Directory data. apis: - name: SGP Directory API description: Public API for accessing Singapore Business Directory data. humanURL: https://sgpdirectory.com/docs baseURL: https://api.sgpdirectory.com/v1 openapi: url: openapi/sgpdirectory-com-openapi.json type: OpenAPI (provider-hosted) in the API Evangelist catalog, representing a company that provides a directory of Singapore-based businesses and services. The entry currently lacks publicly accessible documentation or a verified website, and further investigation is needed to confirm its online presence and API offerings. This placeholder description will be expanded as more information becomes available.'
json_schemas:
- name: EntityCompliance
  property_count: 8
  slug: sgpdirectory-com-entity-compliance
- name: EntityFinancials
  property_count: 2
  slug: sgpdirectory-com-entity-financials
- name: Entity
  property_count: 21
  slug: sgpdirectory-com-entity
- name: EntityShareholder
  property_count: 10
  slug: sgpdirectory-com-entity-shareholder
- name: NameCheckResponse
  property_count: 4
  slug: sgpdirectory-com-name-check-response
- name: SearchEntitiesResponse
  property_count: 2
  slug: sgpdirectory-com-search-entities-response
jsonld:
- class_count: 14
  name: Sgpdirectory Com Context
  property_count: 61
  slug: sgpdirectory-com-context
layout: provider
modified: '2026-10-30'
name: sgpdirectory-com
nav: Providers
network: true
overview: 'sgpdirectory-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: SGP Directory API API. Tagged areas include Company, Directory, Singapore, and Business.


  The sgpdirectory-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  sgpdirectory-com''s developer surface includes authentication, getting-started guide, documentation, and 19 more developer resources.'
plans:
- name: Sgpdirectory Com Plans Pricing
  plan_count: 0
  slug: sgpdirectory-com-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Sgpdirectory Com Rate Limits
  slug: sgpdirectory-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: sgpdirectory-com API Rules
  rule_count: 14
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 0
  slug: sgpdirectory-com-rules
scopes:
- name: Sgpdirectory Com Scopes
  scope_count: 0
  slug: sgpdirectory-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 63.0
    catalog_earned_first_party: 8.0
    catalog_gap: 52.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 17.1
    contract_governance: 19.7
    contract_quality: 56.7
    developer_ergonomics: 22.6
    discoverability: 60.7
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - singapore
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 44.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/sgpdirectory-com/sgpdirectory-com-2026-11-03T143103.png
security:
- kind: authentication
  name: Sgpdirectory Com Authentication
  slug: sgpdirectory-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sgpdirectory Com Domain Security
  slug: sgpdirectory-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sgpdirectory Com Vulnerability Disclosure
  slug: sgpdirectory-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sgpdirectory-com
tags:
- Company
- Directory
- Singapore
- Business
website: https://sgpdirectory.com/
---
