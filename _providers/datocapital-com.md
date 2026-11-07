---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Datocapital Com Agentic Access
  operation_count: 12
  slug: datocapital-com-agentic-access
  summary_line: 12 operations
api_count: 1
apis:
- baseURL: https://api.datocapital.com
  baseurl_source: declared
  description: Caller identity, plan, entitlements.
  name: Dato Capital Account API
  slug: datocapital-com-account-api
- baseURL: https://api.datocapital.com
  baseurl_source: declared
  description: Look up and search company records.
  name: Dato Capital Companies API
  slug: datocapital-com-companies-api
- baseURL: https://api.datocapital.com
  baseurl_source: declared
  description: Per-company filing history.
  name: Dato Capital Filings API
  slug: datocapital-com-filings-api
- baseURL: https://api.datocapital.com
  baseurl_source: declared
  description: Operational endpoints (no auth required).
  name: Dato Capital Health API
  slug: datocapital-com-health-api
- baseURL: https://api.datocapital.com
  baseurl_source: declared
  description: Officers, directors, shareholders.
  name: Dato Capital Individuals API
  slug: datocapital-com-individuals-api
- baseURL: https://api.datocapital.com
  baseurl_source: declared
  description: Static catalogs (countries, types).
  name: Dato Capital Reference API
  slug: datocapital-com-reference-api
- baseURL: https://api.datocapital.com
  baseurl_source: declared
  description: Typeahead.
  name: Dato Capital Suggest API
  slug: datocapital-com-suggest-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/datocapital-com/agentic-access/datocapital-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/datocapital-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/datocapital-com/plans/datocapital-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datocapital-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/datocapital-com/rules/datocapital-com-rules.yml
  title: ''
  type: Spectral
  url: rules/datocapital-com-rules.yml
- group: design
  href: https://artifacts.apis.io/datocapital-com/json-ld/datocapital-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/datocapital-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/datocapital-com/vocabulary/datocapital-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datocapital-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/datocapital-com/data-model/datocapital-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/datocapital-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/datocapital-com/authentication/datocapital-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/datocapital-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/datocapital-com/errors/datocapital-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/datocapital-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/datocapital-com/conformance/datocapital-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datocapital-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/datocapital-com/hosts/datocapital-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datocapital-com-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://en.datocapital.com/isn/Login
- group: company
  title: ''
  type: Blog
  url: https://en.datocapital.com/blog/uk-removed-urls-right-to-be-forgotten.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DatoCapital
- group: auth
  href: https://artifacts.apis.io/datocapital-com/security/datocapital-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datocapital-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datocapital.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://en.datocapital.com/
- group: docs
  title: ''
  type: Documentation
  url: https://en.datocapital.com/help.html
- group: docs
  title: ''
  type: APIReference
  url: https://api.datocapital.com
- group: commercial
  title: ''
  type: Pricing
  url: https://en.datocapital.com/pricing.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://en.datocapital.com/terms-of-service.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://en.datocapital.com/privacy-policy.html
created: '2026-11-05'
description: Dato Capital provides international company and director search services, offering access to global corporate records, director information, and related data. The platform enables users to search for companies worldwide, retrieve detailed corporate structures, and obtain director profiles, supporting compliance, due diligence, and market research needs.
json_schemas:
- name: CompanyList
  property_count: 4
  slug: datocapital-com-company-list
- name: Company
  property_count: 25
  slug: datocapital-com-company
- name: IndividualList
  property_count: 4
  slug: datocapital-com-individual-list
- name: Individual
  property_count: 19
  slug: datocapital-com-individual
- name: RepresentativeList
  property_count: 3
  slug: datocapital-com-representative-list
- name: WhoAmI
  property_count: 4
  slug: datocapital-com-who-am-i
jsonld:
- class_count: 19
  name: Datocapital Com Context
  property_count: 79
  slug: datocapital-com-context
layout: provider
modified: '2026-11-05'
name: Dato Capital
nav: Providers
network: true
overview: 'Dato Capital publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Companies API, Filings API, and 4 more. Tagged areas include Company, Data, Search, Compliance, and Due Diligence.


  The Dato Capital catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dato Capital''s developer surface includes authentication, engineering blog, documentation, API reference, pricing, and 16 more developer resources.'
plans:
- name: Datocapital Com Plans Pricing
  plan_count: 3
  slug: datocapital-com-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Dato Capital API Rules
  rule_count: 51
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 1
  slug: datocapital-com-rules
score:
  band: developing
  composite: 49.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 60.7
    developer_ergonomics: 40.5
    discoverability: 62.5
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Datocapital Com Authentication
  slug: datocapital-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Datocapital Com Domain Security
  slug: datocapital-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: datocapital-com
tags:
- Company
- Data
- Search
- Compliance
- Due Diligence
website: https://datocapital.com/
---
