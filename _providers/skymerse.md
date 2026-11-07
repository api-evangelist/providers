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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.notamify.com/api/v2
  baseurl_source: declared
  description: The Notams API from Skymerse — 9 operation(s) for notams.
  name: Skymerse Notams API
  slug: skymerse-notams-api
artifact_total: 14
asyncapis:
- description: ''
  name: Skymerse Watcher Webhooks
  slug: skymerse-watcher-webhooks
collections:
- collection_type: open
  name: Notamify API V2 Notams API
  slug: open-skymerse-notams-api
common:
- group: commercial
  href: https://artifacts.apis.io/skymerse/plans/skymerse-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/skymerse-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/skymerse/security/skymerse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skymerse-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/skymerse/authentication/skymerse-authentication.yml
  title: ''
  type: Authentication
  url: authentication/skymerse-authentication.yml
- group: build
  href: https://artifacts.apis.io/skymerse/packages/skymerse-packages.yml
  title: ''
  type: Packages
  url: packages/skymerse-packages.yml
- group: build
  href: https://artifacts.apis.io/skymerse/packages/skymerse-packages.yml
  title: ''
  type: SDKs
  url: packages/skymerse-packages.yml
- group: agent
  href: https://artifacts.apis.io/skymerse/mcp/skymerse-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/skymerse-mcp.yml
- group: agent
  href: https://artifacts.apis.io/skymerse/llms/skymerse-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/skymerse-llms.txt
- group: agent
  href: https://artifacts.apis.io/skymerse/well-known/skymerse-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/skymerse-well-known.yml
- group: design
  href: https://artifacts.apis.io/skymerse/conventions/skymerse-conventions.yml
  title: ''
  type: Conventions
  url: conventions/skymerse-conventions.yml
- group: design
  href: https://artifacts.apis.io/skymerse/errors/skymerse-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/skymerse-problem-types.yml
- group: design
  href: https://artifacts.apis.io/skymerse/lifecycle/skymerse-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/skymerse-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/skymerse/changelog/skymerse-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/skymerse-changelog.yml
- group: operate
  href: https://artifacts.apis.io/skymerse/rate-limits/skymerse-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/skymerse-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/skymerse/conformance/skymerse-conformance.yml
  title: ''
  type: Conformance
  url: conformance/skymerse-conformance.yml
- group: design
  href: https://artifacts.apis.io/skymerse/asyncapi/skymerse-watcher-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/skymerse-watcher-webhooks.yml
- group: start
  href: https://artifacts.apis.io/skymerse/sandbox/skymerse-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/skymerse-sandbox.yml
- group: design
  href: https://artifacts.apis.io/skymerse/data-model/skymerse-data-model.yml
  title: ''
  type: DataModel
  url: data-model/skymerse-data-model.yml
- group: other
  href: https://artifacts.apis.io/skymerse/overlays/skymerse-notamify-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/skymerse-notamify-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/skymerse/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://skymerse.gitbook.io/notamify-api
- group: docs
  title: ''
  type: Documentation
  url: https://skymerse.gitbook.io/notamify-api
- group: docs
  title: ''
  type: APIReference
  url: https://skymerse.gitbook.io/notamify-api/active-notams-endpoint
- group: start
  title: ''
  type: GettingStarted
  url: https://skymerse.gitbook.io/notamify-api/basics/quick-start
- group: company
  title: ''
  type: Blog
  url: https://notamify.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/skymerse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.skymerse.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://skymerse.gitbook.io/notamify-api/basics/notamify-api-credits-and-costs
- group: start
  title: ''
  type: SignUp
  url: https://notamify.com/api-manager
- group: operate
  title: ''
  type: Support
  url: https://www.skymerse.com/contact
created: '2026-07-17'
description: 'Skymerse is a Y Combinator-backed aviation company building one AI system for airline flight operations — from planning and monitoring in the operations center to real-time support in the cockpit. Its first product, Notamify, interprets NOTAMs (Notices to Airmen) with specialized aeronautical models and ships the Notamify API V2: a REST API over global NOTAM data with AI-enhanced interpretation, active/nearby/raw/archive NOTAM endpoints, AI NOTAM prioritisation, synchronous and asynchronous flight briefings, and a Watcher API that pushes matching interpreted NOTAMs to signed webhooks. Notamify already serves airline customers and thousands of pilots and aviation professionals, with an official Python SDK and an MCP server for agents.'
finops:
- has_sources: true
  method: derived
  name: Skymerse Finops
  primary_unit: package
  service_category: ''
  slug: skymerse-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/skymerse.png
layout: provider
mcp_servers:
- description: Local (stdio) MCP server; 2 tools listed.
  name: Skymerse MCP Server
  slug: notamify
modified: '2026-07-21'
name: Skymerse
nav: Providers
network: true
overview: 'Skymerse publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Notams API. Tagged areas include Company, Aviation, NOTAM, Flight Operations, and Aeronautical.


  The Skymerse catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Skymerse''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, engineering blog, and 22 more developer resources.'
plans:
- name: Skymerse Plans Pricing
  plan_count: 3
  slug: skymerse-plans-pricing
- name: Skymerse Price Estimates
  plan_count: 0
  slug: skymerse-price-estimates
random_paper: 19
rate_limits:
- limit_count: 2
  name: Skymerse Rate Limits
  slug: skymerse-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Skymerse API Rules
  rule_count: 62
  severity_counts:
    error: 57
    hint: 0
    info: 2
    warn: 3
  slug: skymerse-rules
score:
  band: strong
  composite: 58.4
  coverage:
    artifact_dirs: 27
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 54.6
    developer_ergonomics: 73.2
    discoverability: 71.7
    operational_transparency: 47.4
  previous_composite: 58.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/skymerse/skymerse-2026-08-17T081918.png
security:
- kind: authentication
  name: Skymerse Authentication
  slug: skymerse-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Skymerse Domain Security
  slug: skymerse-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Generate an AI flight briefing
  slug: skymerse-generate-flight-briefing
- name: Get active NOTAMs for airports
  slug: skymerse-get-airport-notams
- name: Subscribe to NOTAM changes via the Watcher API
  slug: skymerse-watcher-webhooks
slug: skymerse
tags:
- Company
- Aviation
- NOTAM
- Flight Operations
- Aeronautical
- Weather
- Artificial Intelligence
- Webhook
website: https://skymerse.gitbook.io/notamify-api
---
