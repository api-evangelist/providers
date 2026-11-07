---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 32
  human_in_the_loop: 2
  name: Boardwalkai Com Agentic Access
  operation_count: 110
  slug: boardwalkai-com-agentic-access
  summary_line: 110 operations · 32 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.boardwalkai.com/api/v1
  baseurl_source: declared
  description: Plan, credit balance, and rate-limit info for the authenticated key.
  name: Boardwalk Account API
  slug: boardwalkai-com-account-api
- baseURL: https://api.boardwalkai.com/api/v1
  baseurl_source: declared
  description: Standing searches that run on a cadence and deliver into your account. Configuration and runs are free. Find Contact Info on delivered records is billed separately when email or phone is found.
  name: Boardwalk Alerts API
  slug: boardwalkai-com-alerts-api
- baseURL: https://api.boardwalkai.com/api/v1
  baseurl_source: declared
  description: Free counts, distributions and rankings. Returns aggregates and never record identity, so an analytical question costs nothing.
  name: Boardwalk Analytics API
  slug: boardwalkai-com-analytics-api
- baseURL: https://api.boardwalkai.com/api/v1
  baseurl_source: declared
  description: Fetch the source meeting documents projects were extracted from.
  name: Boardwalk Documents API
  slug: boardwalkai-com-documents-api
- baseURL: https://api.boardwalkai.com/api/v1
  baseurl_source: declared
  description: 'Find contact info. County, State, and National: 1 credit per project the first time this account receives email or phone. Standalone API Only: included on records already purchased. Empty lookups cost'
  name: Boardwalk Enrichment API
  slug: boardwalkai-com-enrichment-api
- baseURL: https://api.boardwalkai.com/api/v1
  baseurl_source: declared
  description: CSV export jobs queued from the product, from POST /exports, or from search format=csv.
  name: Boardwalk Exports API
  slug: boardwalkai-com-exports-api
- baseURL: https://api.boardwalkai.com/api/v1
  baseurl_source: declared
  description: 'Saved lists of projects, shared with you or with your team. Reading a list''s configuration is free. Pulling its records uses the same record meter as search: free on County, State, and National; 1 cre'
  name: Boardwalk Lists API
  slug: boardwalkai-com-lists-api
- baseURL: https://api.boardwalkai.com/api/v1
  baseurl_source: declared
  description: States, counties, and cities. IDs from here are used as filter values in project search.
  name: Boardwalk Locations API
  slug: boardwalkai-com-locations-api
- baseURL: https://api.boardwalkai.com/api/v1
  baseurl_source: declared
  description: Building Type tree (type, subtype, class) and application types.
  name: Boardwalk Project types API
  slug: boardwalkai-com-project-types-api
- baseURL: https://api.boardwalkai.com/api/v1
  baseurl_source: declared
  description: Search and retrieve land use development projects.
  name: Boardwalk Projects API
  slug: boardwalkai-com-projects-api
- baseURL: https://api.boardwalkai.com/api/v1
  baseurl_source: declared
  description: Value catalogues. `statuses` and `decision-bodies` are filter vocabularies used by search; `owner-types` is a labelling vocabulary only; its filter was withdrawn.
  name: Boardwalk Reference API
  slug: boardwalkai-com-reference-api
artifact_total: 24
common:
- group: docs
  title: ''
  type: APIReference
  url: https://boardwalkai.com/docs/api/reference/
- group: agent
  href: https://artifacts.apis.io/boardwalkai-com/agentic-access/boardwalkai-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/boardwalkai-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/boardwalkai-com/plans/boardwalkai-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boardwalkai-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/boardwalkai-com/rules/boardwalkai-com-rules.yml
  title: ''
  type: Spectral
  url: rules/boardwalkai-com-rules.yml
- group: design
  href: https://artifacts.apis.io/boardwalkai-com/json-ld/boardwalkai-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/boardwalkai-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/boardwalkai-com/vocabulary/boardwalkai-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/boardwalkai-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/boardwalkai-com/data-model/boardwalkai-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/boardwalkai-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/boardwalkai-com/changelog/boardwalkai-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/boardwalkai-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/boardwalkai-com/conventions/boardwalkai-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/boardwalkai-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/boardwalkai-com/conventions/boardwalkai-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/boardwalkai-com-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://boardwalkai.com/privacy/
- group: auth
  href: https://artifacts.apis.io/boardwalkai-com/authentication/boardwalkai-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/boardwalkai-com-authentication.yml
- group: operate
  href: https://artifacts.apis.io/boardwalkai-com/lifecycle/boardwalkai-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/boardwalkai-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/boardwalkai-com/lifecycle/boardwalkai-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/boardwalkai-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/boardwalkai-com/errors/boardwalkai-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/boardwalkai-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/boardwalkai-com/conformance/boardwalkai-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boardwalkai-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/boardwalkai-com/llms/boardwalkai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boardwalkai-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/boardwalkai-com/well-known/boardwalkai-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/boardwalkai-com-security.txt
- group: agent
  href: https://artifacts.apis.io/boardwalkai-com/well-known/boardwalkai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boardwalkai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/boardwalkai-com/hosts/boardwalkai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boardwalkai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/boardwalkai-com/vendors/boardwalkai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boardwalkai-com-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://boardwalkai.com/industries/developers/
- group: operate
  title: ''
  type: ChangeLog
  url: https://boardwalkai.com/docs/api/changelog/
- group: start
  title: ''
  type: SignUp
  url: https://boardwalkai.com/auth/signup/
- group: auth
  href: https://artifacts.apis.io/boardwalkai-com/security/boardwalkai-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/boardwalkai-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/boardwalkai-com/security/boardwalkai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boardwalkai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boardwalkai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://boardwalkai.com/our-data/
- group: start
  title: ''
  type: GettingStarted
  url: https://boardwalkai.com/coverage/
- group: operate
  title: ''
  type: Support
  url: https://boardwalkai.com/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://boardwalkai.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boardwalkai.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boardwalkai.com/privacy/
created: '2026-11-02'
description: Boardwalk helps contractors, developers, and lenders find planned residential, commercial, and industrial projects across thousands of U.S. cities and counties. It provides early‑stage project data to inform financing, construction, and investment decisions, offering a searchable map of upcoming real‑estate developments.
image: https://boardwalkai.com/og/boardwalk-share-2026-10.jpg
json_schemas:
- name: AiSearchJobCancel
  property_count: 7
  slug: boardwalkai-com-ai-search-job-cancel
- name: AiSearchJobStatus
  property_count: 14
  slug: boardwalkai-com-ai-search-job-status
- name: AiSearchRequest
  property_count: 25
  slug: boardwalkai-com-ai-search-request
- name: CreditBalanceResponse
  property_count: 2
  slug: boardwalkai-com-credit-balance-response
- name: CsvExportJobAccepted
  property_count: 8
  slug: boardwalkai-com-csv-export-job-accepted
- name: ProjectCountResponse
  property_count: 3
  slug: boardwalkai-com-project-count-response
jsonld:
- class_count: 55
  name: Boardwalkai Com Context
  property_count: 286
  slug: boardwalkai-com-context
layout: provider
modified: '2026-11-02'
name: Boardwalk
nav: Providers
network: true
overview: 'Boardwalk publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Alerts API, Analytics API, and 8 more. Tagged areas include Real Estate, Construction, Data Platform, Mapping, and Analytics.


  The Boardwalk catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Boardwalk''s developer surface includes API reference, changelog, authentication, signup flow, documentation, getting-started guide, support, and 26 more developer resources.'
plans:
- name: Boardwalkai Com Plans Pricing
  plan_count: 3
  slug: boardwalkai-com-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Boardwalk API Rules
  rule_count: 58
  severity_counts:
    error: 43
    hint: 0
    info: 4
    warn: 11
  slug: boardwalkai-com-rules
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 62.0
    developer_ergonomics: 33.3
    discoverability: 66.1
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Boardwalkai Com Authentication
  slug: boardwalkai-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Boardwalkai Com Domain Security
  slug: boardwalkai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Boardwalkai Com Vulnerability Disclosure
  slug: boardwalkai-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: boardwalkai-com
tags:
- Real Estate
- Construction
- Data Platform
- Mapping
- Analytics
website: https://boardwalkai.com/
---
