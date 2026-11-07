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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 57.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 87
  human_in_the_loop: 6
  name: Bisibility Com Agentic Access
  operation_count: 161
  slug: bisibility-com-agentic-access
  summary_line: 161 operations · 87 acting · 6 human-in-the-loop
api_count: 1
apis:
- description: Public API for Bisibility platform
  name: Bisibility Public API
  slug: bisibility-public-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Manage the authenticated account and personal access tokens.
  name: Bisibility Account Access API
  slug: bisibility-com-account-access-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Manage alert rules, triggered alerts, and notification preferences.
  name: Bisibility Alerts API
  slug: bisibility-com-alerts-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Read project analytics, traffic snapshots, and search-performance data.
  name: Bisibility Analytics API
  slug: bisibility-com-analytics-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Create, list, and revoke API keys.
  name: Bisibility API Keys API
  slug: bisibility-com-api-keys-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Analyze backlinks and page through backlink snapshots.
  name: Bisibility Backlinks API
  slug: bisibility-com-backlinks-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Manage project competitors.
  name: Bisibility Competitors API
  slug: bisibility-com-competitors-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Discover the API contract, capabilities, health, and public provider pricing.
  name: Bisibility Discovery API
  slug: bisibility-com-discovery-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Analyze domain visibility and load its history, keywords, and pages.
  name: Bisibility Domain Overview API
  slug: bisibility-com-domain-overview-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Research keywords, metrics, locations, and ranked keyword suggestions.
  name: Bisibility Keyword Research API
  slug: bisibility-com-keyword-research-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Manage tracked keywords and exact keyword matching.
  name: Bisibility Keywords API
  slug: bisibility-com-keywords-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Manage migration tokens and instance import sessions.
  name: Bisibility Migration API
  slug: bisibility-com-migration-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Create projects and manage their core settings.
  name: Bisibility Projects API
  slug: bisibility-com-projects-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Find questions to track. Today this is model-generated suggestions to review; accepted suggestions become Prompt Tracker prompts.
  name: Bisibility Prompt Research API
  slug: bisibility-com-prompt-research-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Configure AI observations and inspect project-scoped answers, citations and comparable history.
  name: Bisibility Prompt Tracker API
  slug: bisibility-com-prompt-tracker-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Connect and configure external providers.
  name: Bisibility Providers API
  slug: bisibility-com-providers-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Run rank checks and retrieve rank-check history.
  name: Bisibility Rank Checks API
  slug: bisibility-com-rank-checks-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Read stored research reports with their freshness state.
  name: Bisibility Research Reports API
  slug: bisibility-com-research-reports-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Save keywords for later without putting them under rank tracking.
  name: Bisibility Saved Keywords API
  slug: bisibility-com-saved-keywords-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Create, list, and delete saved views.
  name: Bisibility Saved Views API
  slug: bisibility-com-saved-views-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Ingest and list project signals.
  name: Bisibility Signals API
  slug: bisibility-com-signals-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Inspect and configure project sitemap monitoring.
  name: Bisibility Sitemap Monitoring API
  slug: bisibility-com-sitemap-monitoring-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Manage team members and invitations.
  name: Bisibility Team API
  slug: bisibility-com-team-api
- baseURL: https://eu.bisibility.com/api/v1
  baseurl_source: declared
  description: Create and manage webhook endpoints.
  name: Bisibility Webhooks API
  slug: bisibility-com-webhooks-api
artifact_total: 33
common:
- group: agent
  href: https://artifacts.apis.io/bisibility-com/agentic-access/bisibility-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bisibility-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/bisibility-com/plans/bisibility-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bisibility-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bisibility-com/rules/bisibility-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bisibility-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bisibility-com/json-ld/bisibility-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bisibility-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bisibility-com/vocabulary/bisibility-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bisibility-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bisibility-com/data-model/bisibility-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bisibility-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/bisibility-com/cli/bisibility-com-cli.yml
  title: ''
  type: CLI
  url: cli/bisibility-com-cli.yml
- group: design
  href: https://artifacts.apis.io/bisibility-com/conventions/bisibility-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bisibility-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/bisibility-com/conventions/bisibility-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bisibility-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/bisibility-com/authentication/bisibility-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bisibility-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/bisibility-com/errors/bisibility-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bisibility-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bisibility-com/conformance/bisibility-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bisibility-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bisibility-com/llms/bisibility-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bisibility-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/bisibility-com/well-known/bisibility-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bisibility-com-security.txt
- group: auth
  href: https://artifacts.apis.io/bisibility-com/well-known/bisibility-com-eu-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bisibility-com-eu-security.txt
- group: auth
  href: https://artifacts.apis.io/bisibility-com/well-known/bisibility-com-demo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bisibility-com-demo-security.txt
- group: agent
  href: https://artifacts.apis.io/bisibility-com/well-known/bisibility-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bisibility-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bisibility-com/hosts/bisibility-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bisibility-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bisibility-com/vendors/bisibility-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bisibility-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bisibility.com/terms
- group: auth
  title: ''
  type: Security
  url: https://bisibility.com/security
- group: operate
  title: ''
  type: Roadmap
  url: https://bisibility.com/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bisibility.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://bisibility.com/pricing
- group: start
  title: ''
  type: Login
  url: https://bisibility.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://bisibility.com/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://bisibility.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://bisibility.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://bisibility.com/#quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://bisibility.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/bisibility-com/scopes/bisibility-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/bisibility-com-scopes.yml
- group: auth
  href: https://artifacts.apis.io/bisibility-com/security/bisibility-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bisibility-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bisibility-com/security/bisibility-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bisibility-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bisibility.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://bisibility.com/api/mcp
  - status: 401
    url: https://demo.bisibility.com/api/mcp
  - status: 200
    url: https://bisibility.com/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Bisibility provides an open-source SEO platform that can be self‑hosted or used as a cloud service. It offers keyword rank tracking, backlink monitoring, and search console data integration, supporting multiple SERP providers. Users can start with a 7‑day free trial and choose monthly cloud plans or run the software on their own infrastructure.
image: https://bisibility.com/opengraph-image?v=2
jsonld:
- class_count: 120
  name: Bisibility Com Context
  property_count: 349
  slug: bisibility-com-context
layout: provider
modified: '2026-11-02'
name: Bisibility
nav: Providers
network: true
overview: 'Bisibility publishes 24 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Access API, Alerts API, Analytics API, and 21 more. Tagged areas include SEO, Open Source, KeywordTracking, BacklinkMonitoring, and Cloud.


  The Bisibility catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bisibility''s developer surface includes CLI, authentication, pricing, documentation, changelog, engineering blog, getting-started guide, and 27 more developer resources.'
plans:
- name: Bisibility Com Plans Pricing
  plan_count: 1
  slug: bisibility-com-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Bisibility API Rules
  rule_count: 60
  severity_counts:
    error: 43
    hint: 0
    info: 3
    warn: 14
  slug: bisibility-com-rules
scopes:
- name: Bisibility Com Scopes
  scope_count: 2
  slug: bisibility-com-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 61.8
    catalog_earned_first_party: 8.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 52.1
    developer_ergonomics: 34.5
    discoverability: 73.2
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bisibility Com Authentication
  slug: bisibility-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bisibility Com Domain Security
  slug: bisibility-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bisibility Com Vulnerability Disclosure
  slug: bisibility-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: bisibility
  slug: bisibility-com-bisibility
slug: bisibility-com
tags:
- SEO
- Open Source
- KeywordTracking
- BacklinkMonitoring
- Cloud
website: https://bisibility.com/
---
