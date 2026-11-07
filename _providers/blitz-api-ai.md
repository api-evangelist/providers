---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Blitz Api Ai Agentic Access
  operation_count: 40
  slug: blitz-api-ai-agentic-access
  summary_line: 40 operations · 27 acting
api_count: 2
apis:
- baseURL: https://agents.blitz-api.ai
  baseurl_source: declared
  description: The Account API from blitz-api-ai — 1 operation(s) for account.
  name: blitz-api-ai Account API
  slug: blitz-api-ai-account-api
- baseURL: https://agents.blitz-api.ai
  baseurl_source: declared
  description: The Changelog API from blitz-api-ai — 1 operation(s) for changelog.
  name: blitz-api-ai Changelog API
  slug: blitz-api-ai-changelog-api
- baseURL: https://agents.blitz-api.ai
  baseurl_source: declared
  description: The Company API from blitz-api-ai — 2 operation(s) for company.
  name: blitz-api-ai Company API
  slug: blitz-api-ai-company-api
- baseURL: https://agents.blitz-api.ai
  baseurl_source: declared
  description: The Company Enrichment API from blitz-api-ai — 5 operation(s) for company enrichment.
  name: blitz-api-ai Company Enrichment API
  slug: blitz-api-ai-company-enrichment-api
- baseURL: https://agents.blitz-api.ai
  baseurl_source: declared
  description: The Company Search API from blitz-api-ai — 3 operation(s) for company search.
  name: blitz-api-ai Company Search API
  slug: blitz-api-ai-company-search-api
- baseURL: https://agents.blitz-api.ai
  baseurl_source: declared
  description: The Enrichment API from blitz-api-ai — 10 operation(s) for enrichment.
  name: blitz-api-ai Enrichment API
  slug: blitz-api-ai-enrichment-api
- baseURL: https://agents.blitz-api.ai
  baseurl_source: declared
  description: The Job Search API from blitz-api-ai — 2 operation(s) for job search.
  name: blitz-api-ai Job Search API
  slug: blitz-api-ai-job-search-api
- baseURL: https://agents.blitz-api.ai
  baseurl_source: declared
  description: The Jobs API from blitz-api-ai — 2 operation(s) for jobs.
  name: blitz-api-ai Jobs API
  slug: blitz-api-ai-jobs-api
- baseURL: https://agents.blitz-api.ai
  baseurl_source: declared
  description: The People Enrichment API from blitz-api-ai — 5 operation(s) for people enrichment.
  name: blitz-api-ai People Enrichment API
  slug: blitz-api-ai-people-enrichment-api
- baseURL: https://agents.blitz-api.ai
  baseurl_source: declared
  description: The People Search API from blitz-api-ai — 3 operation(s) for people search.
  name: blitz-api-ai People Search API
  slug: blitz-api-ai-people-search-api
- baseURL: https://agents.blitz-api.ai
  baseurl_source: declared
  description: The Search API from blitz-api-ai — 4 operation(s) for search.
  name: blitz-api-ai Search API
  slug: blitz-api-ai-search-api
- baseURL: https://agents.blitz-api.ai
  baseurl_source: declared
  description: The Utilities API from blitz-api-ai — 1 operation(s) for utilities.
  name: blitz-api-ai Utilities API
  slug: blitz-api-ai-utilities-api
- baseURL: https://agents.blitz-api.ai
  baseurl_source: declared
  description: The Zeroclick API from blitz-api-ai — 1 operation(s) for zeroclick.
  name: blitz-api-ai Zeroclick API
  slug: blitz-api-ai-zeroclick-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/blitz-api-ai/agentic-access/blitz-api-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blitz-api-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/blitz-api-ai/rate-limits/blitz-api-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/blitz-api-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/blitz-api-ai/plans/blitz-api-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blitz-api-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/blitz-api-ai/rules/blitz-api-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/blitz-api-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/blitz-api-ai/json-ld/blitz-api-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blitz-api-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/blitz-api-ai/vocabulary/blitz-api-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blitz-api-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/blitz-api-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/blitz-api-ai/data-model/blitz-api-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blitz-api-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/blitz-api-ai/changelog/blitz-api-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/blitz-api-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/blitz-api-ai/conventions/blitz-api-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/blitz-api-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/blitz-api-ai/authentication/blitz-api-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blitz-api-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/blitz-api-ai/errors/blitz-api-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blitz-api-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blitz-api-ai/conformance/blitz-api-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blitz-api-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blitz-api-ai/llms/blitz-api-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blitz-api-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/blitz-api-ai/a2a/blitz-api-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/blitz-api-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/blitz-api-ai/well-known/blitz-api-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blitz-api-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/blitz-api-ai/hosts/blitz-api-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blitz-api-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/blitz-api-ai/vendors/blitz-api-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blitz-api-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/blitz-api-ai/packages/blitz-api-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/blitz-api-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/blitz-api-ai/packages/blitz-api-ai-packages.yml
  title: ''
  type: Packages
  url: packages/blitz-api-ai-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blitz-api.ai/legal/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.blitz-api.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blitz-api.ai/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://app.blitz-api.ai/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://app.blitz-api.ai/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.blitz-api.ai`
- group: auth
  href: https://artifacts.apis.io/blitz-api-ai/security/blitz-api-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blitz-api-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blitz-api.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blitz-api.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.blitz-api.ai/api-reference/account/get-api-key-details
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.blitz-api.ai/guide/getting-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.blitz-api.ai/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.blitz-api.ai/pricing
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://agents.blitz-api.ai/openapi.json
  - status: null
    url: https://api.blitz-api.ai/openapi
  - status: null
    url: https://docs.blitz-api.ai/mcp
  - status: 401
    url: https://agents.blitz-api.ai/mcp
  - status: 401
    url: https://api.blitz-api.ai/mcp
  - status: 200
    url: https://blitz-api.ai/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: BlitzAPI provides B2B data APIs enabling GTM builders to access company, people, employee, and job intelligence. Their platform offers searchable enrichment, reverse lookups, and integration via MCP server tools, with pricing starting at $99/month and a free tier of 1,000 records. The service targets developers, sales, and marketing teams seeking accurate data for decision‑making and workflow automation.
image: https://www.blitz-api.ai/og/og-default.jpg
jsonld:
- class_count: 1
  name: Blitz Api Ai Context
  property_count: 3
  slug: blitz-api-ai-context
layout: provider
modified: '2026-10-30'
name: blitz-api-ai
nav: Providers
network: true
overview: 'blitz-api-ai publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Changelog API, Company API, and 10 more. Tagged areas include B2B, Data, Data Enrichment, and Go-To-Market.


  The blitz-api-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  blitz-api-ai''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, pricing, and 26 more developer resources.'
plans:
- name: Blitz Api Ai Plans Pricing
  plan_count: 4
  slug: blitz-api-ai-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Blitz Api Ai Rate Limits
  slug: blitz-api-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: blitz-api-ai API Rules
  rule_count: 58
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 8
  slug: blitz-api-ai-rules
score:
  band: developing
  composite: 47.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 66.8
    catalog_earned_first_party: 24.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.3
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 51.5
    developer_ergonomics: 42.3
    discoverability: 57.1
    operational_transparency: 47.4
  previous_composite: 59.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 38.5
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/blitz-api-ai/blitz-api-ai-2026-11-03T121949.png
security:
- kind: authentication
  name: Blitz Api Ai Authentication
  slug: blitz-api-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Blitz Api Ai Domain Security
  slug: blitz-api-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: blitz-api-ai-company-enrichment
  slug: blitz-api-ai-company-enrichment
- name: blitz-api-ai-company-search
  slug: blitz-api-ai-company-search
- name: blitz-api-ai-people-enrichment
  slug: blitz-api-ai-people-enrichment
slug: blitz-api-ai
tags:
- B2B
- Data
- Data Enrichment
- Go-To-Market
website: https://blitz-api.ai/
---
