---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: derived
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'star365-site API as documented publicly: 50 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: star365-site API
  slug: star365-site-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/star365-site/plans/star365-site-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/star365-site-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/star365-site/rules/star365-site-rules.yml
  title: ''
  type: Spectral
  url: rules/star365-site-rules.yml
- group: design
  href: https://artifacts.apis.io/star365-site/json-ld/star365-site-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/star365-site-context.jsonld
- group: design
  href: https://artifacts.apis.io/star365-site/vocabulary/star365-site-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/star365-site-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/star365-site/data-model/star365-site-data-model.yml
  title: ''
  type: DataModel
  url: data-model/star365-site-data-model.yml
- group: operate
  href: https://artifacts.apis.io/star365-site/changelog/star365-site-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/star365-site-changelog.yml
- group: design
  href: https://artifacts.apis.io/star365-site/conventions/star365-site-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/star365-site-conventions.yml
- group: design
  href: https://artifacts.apis.io/star365-site/conventions/star365-site-conventions.yml
  title: ''
  type: Conventions
  url: conventions/star365-site-conventions.yml
- group: auth
  href: https://artifacts.apis.io/star365-site/authentication/star365-site-authentication.yml
  title: ''
  type: Authentication
  url: authentication/star365-site-authentication.yml
- group: design
  href: https://artifacts.apis.io/star365-site/conformance/star365-site-conformance.yml
  title: ''
  type: Conformance
  url: conformance/star365-site-conformance.yml
- group: agent
  href: https://artifacts.apis.io/star365-site/llms/star365-site-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/star365-site-llms.txt
- group: auth
  href: https://artifacts.apis.io/star365-site/well-known/star365-site-audit-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/star365-site-audit-security.txt
- group: agent
  href: https://artifacts.apis.io/star365-site/well-known/star365-site-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/star365-site-well-known.yml
- group: other
  href: https://artifacts.apis.io/star365-site/hosts/star365-site-hosts.yml
  title: ''
  type: Hosts
  url: hosts/star365-site-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://help.star365.site/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://star365.site/privacy
- group: start
  title: ''
  type: Login
  url: https://members.star365.site/login
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.star365.site/paperclip/cli/setup-commands
- group: auth
  href: https://artifacts.apis.io/star365-site/security/star365-site-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/star365-site-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://star365.site/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.star365.site/
- group: docs
  title: ''
  type: APIReference
  url: https://api.star365.site/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.star365.site/
- group: company
  title: ''
  type: Blog
  url: https://blog.star365.site/
coverage:
  checked: '2026-10-30'
  detail: Documentation pages are rendered with JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.star365.site/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Star365 is a Korean platform offering a unified account to access a wide range of services across public data, healthcare, commerce, finance, and AI tools. Users can log in once to access 53 services spanning data analytics, stock strategy verification, government grant tracking, AI media creation, document scanning, and more. The ecosystem includes specialized subdomains for each service, providing APIs for data retrieval, AI-driven content generation, and integrated payment via USDT credits.
image: https://star365.site/logo.png
json_schemas:
- name: GetApiCompaniesCompanyidActivityResponse
  property_count: 6
  slug: star365-site-get-api-companies-companyid-activity-response
- name: GetApiIssuesIssueidResponse
  property_count: 3
  slug: star365-site-get-api-issues-issueid-response
- name: PatchApiRoutinesRoutineidRequest
  property_count: 10
  slug: star365-site-patch-api-routines-routineid-request
- name: PostApiCompaniesCompanyidRoutinesRequest
  property_count: 10
  slug: star365-site-post-api-companies-companyid-routines-request
- name: PostApiRoutinesRoutineidRunRequest
  property_count: 4
  slug: star365-site-post-api-routines-routineid-run-request
- name: PostApiRoutinesRoutineidTriggersRequest
  property_count: 5
  slug: star365-site-post-api-routines-routineid-triggers-request
jsonld:
- class_count: 25
  name: Star365 Site Context
  property_count: 58
  slug: star365-site-context
layout: provider
modified: '2026-10-29'
name: star365-site
nav: Providers
network: true
overview: 'star365-site is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Artificial Intelligence, Finance, and Healthcare.


  The star365-site catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  star365-site''s developer surface includes changelog, authentication, support, getting-started guide, documentation, API reference, engineering blog, and 17 more developer resources.'
plans:
- name: Star365 Site Plans Pricing
  plan_count: 12
  slug: star365-site-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: star365-site API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: star365-site-rules
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 69.0
    catalog_earned_first_party: 12.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 43.4
    contract_governance: 19.7
    contract_quality: 25.2
    developer_ergonomics: 29.8
    discoverability: 64.3
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 43.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/star365-site/star365-site-2026-11-03T143731.png
security:
- kind: authentication
  name: Star365 Site Authentication
  slug: star365-site-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Star365 Site Domain Security
  slug: star365-site-domain-security
  summary_line: TLSv1.3 · HSTS
slug: star365-site
tags:
- Company
- Data
- Artificial Intelligence
- Finance
- Healthcare
website: https://star365.site/
---
