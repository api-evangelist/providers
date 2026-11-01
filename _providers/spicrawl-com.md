---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 59.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Spicrawl Com Agentic Access
  operation_count: 27
  slug: spicrawl-com-agentic-access
  summary_line: 27 operations · 10 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.spicrawl.com
  baseurl_source: declared
  description: Scrape many URLs as one asynchronous job.
  name: spicrawl-com Batch API
  slug: spicrawl-com-batch-api
- baseURL: https://api.spicrawl.com
  baseurl_source: declared
  description: Drive a hosted browser over a DevTools Protocol (CDP) WebSocket.
  name: spicrawl-com Browser API
  slug: spicrawl-com-browser-api
- baseURL: https://api.spicrawl.com
  baseurl_source: declared
  description: Deployment capacity and readiness.
  name: spicrawl-com Fleet API
  slug: spicrawl-com-fleet-api
- baseURL: https://api.spicrawl.com
  baseurl_source: declared
  description: Liveness and readiness probes.
  name: spicrawl-com Health API
  slug: spicrawl-com-health-api
- baseURL: https://api.spicrawl.com
  baseurl_source: declared
  description: Inspect the history of requests made in this key's project, or with the `read` scope in every project of its organization.
  name: spicrawl-com Requests API
  slug: spicrawl-com-requests-api
- baseURL: https://api.spicrawl.com
  baseurl_source: declared
  description: Fetch, render and extract one URL synchronously.
  name: spicrawl-com Scrape API
  slug: spicrawl-com-scrape-api
- baseURL: https://api.spicrawl.com
  baseurl_source: declared
  description: Reuse cookies, storage and an exit IP across requests.
  name: spicrawl-com Sessions API
  slug: spicrawl-com-sessions-api
- baseURL: https://api.spicrawl.com
  baseurl_source: declared
  description: Credits and volume over time. Requires the `read` scope.
  name: spicrawl-com Usage API
  slug: spicrawl-com-usage-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/spicrawl-com/agentic-access/spicrawl-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/spicrawl-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/spicrawl-com/rate-limits/spicrawl-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/spicrawl-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/spicrawl-com/plans/spicrawl-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/spicrawl-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/spicrawl-com/rules/spicrawl-com-rules.yml
  title: ''
  type: Spectral
  url: rules/spicrawl-com-rules.yml
- group: design
  href: https://artifacts.apis.io/spicrawl-com/json-ld/spicrawl-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/spicrawl-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/spicrawl-com/vocabulary/spicrawl-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/spicrawl-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/spicrawl-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/spicrawl-com/data-model/spicrawl-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/spicrawl-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/spicrawl-com/cli/spicrawl-com-cli.yml
  title: ''
  type: CLI
  url: cli/spicrawl-com-cli.yml
- group: design
  href: https://artifacts.apis.io/spicrawl-com/conventions/spicrawl-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/spicrawl-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/spicrawl-com/authentication/spicrawl-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/spicrawl-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/spicrawl-com/scopes/spicrawl-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/spicrawl-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/spicrawl-com/errors/spicrawl-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/spicrawl-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/spicrawl-com/conformance/spicrawl-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/spicrawl-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/spicrawl-com/llms/spicrawl-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/spicrawl-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/spicrawl-com/well-known/spicrawl-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/spicrawl-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/spicrawl-com/hosts/spicrawl-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/spicrawl-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/spicrawl-com/vendors/spicrawl-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/spicrawl-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/spicrawl-com/packages/spicrawl-com-packages.yml
  title: ''
  type: Packages
  url: packages/spicrawl-com-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@spicrawl/sdk
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.spicrawl.com`
- group: auth
  href: https://artifacts.apis.io/spicrawl-com/security/spicrawl-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/spicrawl-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spicrawl.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spicrawl.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.spicrawl.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.spicrawl.com/api-reference/introduction
- group: operate
  title: ''
  type: Support
  url: https://spicrawl.com/support
- group: company
  title: ''
  type: Blog
  url: https://spicrawl.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OfficialSpicrawl
- group: commercial
  title: ''
  type: Pricing
  url: https://spicrawl.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://spicrawl.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://spicrawl.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spicrawl.com/privacy
created: '2026-10-31'
description: Spicrawl provides a web data API that fetches, renders, and extracts any URL into clean markdown, HTML, JSON, or PDF. It supports JavaScript rendering, batch processing, login session reuse, and offers flexible output formats for AI agents and developers. The platform includes a REST endpoint at /v1/scrape, detailed documentation, SDKs, and a CLI tool, enabling developers to integrate web content extraction into applications with simple GET/POST calls. Spicrawl aims to simplify web data acquisition while handling anti-bot challenges and providing transparent credit usage.
image: https://spicrawl.com/spicrawl-logo.png
json_schemas:
- name: BatchCreateRequest
  property_count: 10
  slug: spicrawl-com-batch-create-request
- name: BatchJob
  property_count: 24
  slug: spicrawl-com-batch-job
- name: BatchResultLine
  property_count: 16
  slug: spicrawl-com-batch-result-line
- name: ScrapeRequest
  property_count: 41
  slug: spicrawl-com-scrape-request
- name: SessionCreateRequest
  property_count: 10
  slug: spicrawl-com-session-create-request
- name: Session
  property_count: 18
  slug: spicrawl-com-session
jsonld:
- class_count: 65
  name: Spicrawl Com Context
  property_count: 281
  slug: spicrawl-com-context
layout: provider
modified: '2026-10-31'
name: spicrawl-com
nav: Providers
network: true
overview: 'spicrawl-com publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Batch API, Browser API, Fleet API, and 5 more. Tagged areas include Company, Web Scraping, Data Extraction, API, and Automation.


  The spicrawl-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  spicrawl-com''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 26 more developer resources.'
plans:
- name: Spicrawl Com Plans Pricing
  plan_count: 1
  slug: spicrawl-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Spicrawl Com Rate Limits
  slug: spicrawl-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: spicrawl-com API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 3
  slug: spicrawl-com-rules
scopes:
- name: Spicrawl Com Scopes
  scope_count: 5
  slug: spicrawl-com-scopes
  summary_line: 5 scopes
score:
  band: exemplar
  composite: 66.5
  coverage:
    artifact_dirs: 29
    catalog_earned: 95.7
    catalog_earned_first_party: 0.0
    catalog_gap: 19.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.7
    contract_governance: 79.1
    contract_quality: 60.8
    developer_ergonomics: 77.9
    discoverability: 66.1
    operational_transparency: 33.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Spicrawl Com Authentication
  slug: spicrawl-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Spicrawl Com Domain Security
  slug: spicrawl-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 4
skills:
- name: batch
  slug: spicrawl-com-batch
- name: browser
  slug: spicrawl-com-browser
- name: scrape
  slug: spicrawl-com-scrape
- name: sessions
  slug: spicrawl-com-sessions
slug: spicrawl-com
tags:
- Company
- Web Scraping
- Data Extraction
- API
- Automation
- AI
website: https://spicrawl.com/
---
