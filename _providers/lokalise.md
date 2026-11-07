---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Lokalise Agentic Access
  operation_count: 10
  slug: lokalise-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 1
apis:
- description: Full-coverage REST API for the Lokalise TMS. Resources include projects, keys, translations, contributors, files, comments, screenshots, snapshots, teams, team users, team user groups, branches, langu
  name: Lokalise API v2
  slug: api-v2
- baseURL: https://api.lokalise.com/api2
  baseurl_source: declared
  description: The Files API from Lokalise — 1 operation(s) for files.
  name: Lokalise Files API
  slug: lokalise-files-api
- baseURL: https://api.lokalise.com/api2
  baseurl_source: declared
  description: The Keys API from Lokalise — 2 operation(s) for keys.
  name: Lokalise Keys API
  slug: lokalise-keys-api
- baseURL: https://api.lokalise.com/api2
  baseurl_source: declared
  description: The Projects API from Lokalise — 2 operation(s) for projects.
  name: Lokalise Projects API
  slug: lokalise-projects-api
- baseURL: https://api.lokalise.com/api2
  baseurl_source: declared
  description: The Branches API from Lokalise — 3 operation(s) for branches.
  name: Lokalise Branches API
  slug: lokalise-branches-api
- baseURL: https://api.lokalise.com/api2
  baseurl_source: declared
  description: The Comments API from Lokalise — 3 operation(s) for comments.
  name: Lokalise Comments API
  slug: lokalise-comments-api
- baseURL: https://api.lokalise.com/api2
  baseurl_source: declared
  description: The Languages API from Lokalise — 2 operation(s) for languages.
  name: Lokalise Languages API
  slug: lokalise-languages-api
- baseURL: https://api.lokalise.com/api2
  baseurl_source: declared
  description: The Queued Processes API from Lokalise — 2 operation(s) for queued processes.
  name: Lokalise Queued Processes API
  slug: lokalise-queued-processes-api
- baseURL: https://api.lokalise.com/api2
  baseurl_source: declared
  description: The Screenshots API from Lokalise — 1 operation(s) for screenshots.
  name: Lokalise Screenshots API
  slug: lokalise-screenshots-api
- baseURL: https://api.lokalise.com/api2
  baseurl_source: declared
  description: The Tasks API from Lokalise — 3 operation(s) for tasks.
  name: Lokalise Tasks API
  slug: lokalise-tasks-api
- baseURL: https://api.lokalise.com/api2
  baseurl_source: declared
  description: The Translations API from Lokalise — 2 operation(s) for translations.
  name: Lokalise Translations API
  slug: lokalise-translations-api
artifact_total: 23
collections:
- collection_type: open
  name: Lokalise API v2 Files API
  slug: open-lokalise-files-api
- collection_type: open
  name: Lokalise API v2 Files Keys API
  slug: open-lokalise-keys-api
- collection_type: open
  name: Lokalise API v2 Files Projects API
  slug: open-lokalise-projects-api
- collection_type: open
  name: Lokalise API v2
  slug: open-lokalise
common:
- group: agent
  href: https://artifacts.apis.io/lokalise/agentic-access/lokalise-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lokalise-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/lokalise/security/lokalise-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lokalise-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/lokalise/authentication/lokalise-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lokalise-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://lokalise.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.lokalise.com/
- group: company
  title: ''
  type: Blog
  url: https://lokalise.com/blog/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/lokalise
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lokalise
- group: commercial
  href: https://artifacts.apis.io/lokalise/plans/lokalise-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lokalise-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/lokalise/rate-limits/lokalise-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lokalise-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/lokalise/finops/lokalise-finops.yml
  title: ''
  type: FinOps
  url: finops/lokalise-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.lokalise.com/llms.txt
created: '2026-05-23'
description: Lokalise is a translation management system (TMS) for software, mobile, web, games, and documentation. It pairs collaborative localization workflows with AI machine translation and a full-coverage REST API (APIv2) that exposes projects, keys, translations, files, contributors, screenshots, snapshots, tasks, branches, glossaries, webhooks, and payments. Official SDKs are maintained for Node.js, Python, Ruby, PHP, Go, Java, .NET, and Elixir.
finops:
- has_sources: false
  method: generated
  name: Lokalise Finops
  primary_unit: ''
  service_category: API
  slug: lokalise-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lokalise.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.lokalise.com over HTTP.
  name: Lokalise MCP Server
  slug: lokalise
modified: '2026-05-23'
name: Lokalise
nav: Providers
network: true
overview: 'Lokalise publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Files API, Keys API, Projects API, and 8 more. Tagged areas include Localization, Translation, TMS, AI Machine Translation, and REST.


  The Lokalise catalog on APIs.io includes 1 Spectral governance ruleset.


  Lokalise''s developer surface includes authentication, documentation, engineering blog, GitHub presence, and 8 more developer resources.'
plans:
- name: Lokalise Plans Pricing
  plan_count: 1
  slug: lokalise-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Lokalise Rate Limits
  slug: lokalise-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Lokalise API Rules
  rule_count: 57
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 9
  slug: lokalise-rules
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 45.5
    catalog_earned_first_party: 0.0
    catalog_gap: 69.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.0
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 54.8
    developer_ergonomics: 40.5
    discoverability: 75.0
    operational_transparency: 10.5
  previous_composite: 30.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 71.4
      total: 14
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/lokalise/lokalise-2026-06-20T184709.png
security:
- kind: authentication
  name: Lokalise Authentication
  slug: lokalise-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lokalise Domain Security
  slug: lokalise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lokalise
tags:
- Localization
- Translation
- TMS
- AI Machine Translation
- REST
- Developer Tools
website: https://lokalise.com/
---
