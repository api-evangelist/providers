---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Crimescore Io Agentic Access
  operation_count: 4
  slug: crimescore-io-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://api.crimescore.io/v1
  baseurl_source: declared
  description: The Geocode API from crimescore-io — 1 operation(s) for geocode.
  name: crimescore-io Geocode API
  slug: crimescore-io-geocode-api
- baseURL: https://api.crimescore.io/v1
  baseurl_source: declared
  description: The Incidents API from crimescore-io — 1 operation(s) for incidents.
  name: crimescore-io Incidents API
  slug: crimescore-io-incidents-api
- baseURL: https://api.crimescore.io/v1
  baseurl_source: declared
  description: The Score API from crimescore-io — 2 operation(s) for score.
  name: crimescore-io Score API
  slug: crimescore-io-score-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/crimescore-io/agentic-access/crimescore-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/crimescore-io-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/crimescore-io/rate-limits/crimescore-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/crimescore-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/crimescore-io/plans/crimescore-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crimescore-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/crimescore-io/rules/crimescore-io-rules.yml
  title: ''
  type: Spectral
  url: rules/crimescore-io-rules.yml
- group: design
  href: https://artifacts.apis.io/crimescore-io/json-ld/crimescore-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/crimescore-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/crimescore-io/vocabulary/crimescore-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/crimescore-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/crimescore-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/crimescore-io/data-model/crimescore-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/crimescore-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/crimescore-io/components/crimescore-io-components.yml
  title: ''
  type: Components
  url: components/crimescore-io-components.yml
- group: auth
  href: https://artifacts.apis.io/crimescore-io/authentication/crimescore-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crimescore-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/crimescore-io/errors/crimescore-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/crimescore-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/crimescore-io/conformance/crimescore-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crimescore-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/crimescore-io/llms/crimescore-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crimescore-io-llms.txt
- group: other
  href: https://artifacts.apis.io/crimescore-io/hosts/crimescore-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crimescore-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/crimescore-io/vendors/crimescore-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crimescore-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/crimescore-io/packages/crimescore-io-packages.yml
  title: ''
  type: SDKs
  url: packages/crimescore-io-packages.yml
- group: build
  href: https://artifacts.apis.io/crimescore-io/packages/crimescore-io-packages.yml
  title: ''
  type: Packages
  url: packages/crimescore-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crimescore.io/terms-of-service/
- group: start
  title: ''
  type: Sandbox
  url: https://crimescore.io/playground/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crimescore.io/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/crimescore-io/security/crimescore-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crimescore-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crimescore.io/
- group: docs
  title: ''
  type: Documentation
  url: https://crimescore.io/crime-data-api/
- group: docs
  title: ''
  type: APIReference
  url: https://crimescore.io/crime-data-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://crimescore.io/crime-data-api/
- group: operate
  title: ''
  type: Support
  url: https://crimescore.io/contact/
- group: company
  title: ''
  type: Blog
  url: https://crimescore.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://crimescore.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://crimescore.io/dashboard/register
created: '2026-10-30'
description: CrimeScore provides U.S. neighborhood safety data through modeled Safety Scores, component scores, recent activity context, and embeddable maps. Users can search by address, ZIP code, or city to view safety reports, download sample reports, and integrate the CrimeScore API into real‑estate, prop‑tech, and location‑aware applications. The platform offers a public map, free ZIP profile lookups, and paid API plans with higher request limits and custom contracts. Backed by OopsLab LLC, CrimeScore emphasizes transparent data sources and licensing options.
image: https://crimescore.io/logo-512.png
json_schemas:
- name: NearbyIncidentsResponse
  property_count: 8
  slug: crimescore-io-nearby-incidents-response
- name: ScoreDetailsResponse
  property_count: 0
  slug: crimescore-io-score-details-response
- name: ScoreResponse
  property_count: 0
  slug: crimescore-io-score-response
jsonld:
- class_count: 10
  name: Crimescore Io Context
  property_count: 37
  slug: crimescore-io-context
layout: provider
modified: '2026-10-30'
name: crimescore-io
nav: Providers
network: true
overview: 'crimescore-io publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Geocode API, Incidents API, and Score API. Tagged areas include Company, Safety, RealEstate, Data, and Mapping.


  The crimescore-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  crimescore-io''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, support, engineering blog, and 22 more developer resources.'
plans:
- name: Crimescore Io Plans Pricing
  plan_count: 3
  slug: crimescore-io-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Crimescore Io Rate Limits
  slug: crimescore-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: crimescore-io API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: crimescore-io-rules
scopes:
- name: Crimescore Io Scopes
  scope_count: 0
  slug: crimescore-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 66.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 95.7
    catalog_earned_first_party: 0.0
    catalog_gap: 19.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 65.0
    developer_ergonomics: 68.3
    discoverability: 66.1
    operational_transparency: 18.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Crimescore Io Authentication
  slug: crimescore-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Crimescore Io Domain Security
  slug: crimescore-io-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: crimescore-io-main
  slug: crimescore-io-main
slug: crimescore-io
tags:
- Company
- Safety
- RealEstate
- Data
- Mapping
- API
website: https://crimescore.io/
---
