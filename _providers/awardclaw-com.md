---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Awardclaw Com Agentic Access
  operation_count: 10
  slug: awardclaw-com-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 1
apis:
- baseURL: https://www.awardclaw.com/api/v1
  baseurl_source: declared
  description: The Availability API from AwardClaw — 1 operation(s) for availability.
  name: AwardClaw Availability API
  slug: awardclaw-com-availability-api
- baseURL: https://www.awardclaw.com/api/v1
  baseurl_source: declared
  description: The Briefing API from AwardClaw — 1 operation(s) for briefing.
  name: AwardClaw Briefing API
  slug: awardclaw-com-briefing-api
- baseURL: https://www.awardclaw.com/api/v1
  baseurl_source: declared
  description: The Cards API from AwardClaw — 1 operation(s) for cards.
  name: AwardClaw Cards API
  slug: awardclaw-com-cards-api
- baseURL: https://www.awardclaw.com/api/v1
  baseurl_source: declared
  description: The Drops API from AwardClaw — 2 operation(s) for drops.
  name: AwardClaw Drops API
  slug: awardclaw-com-drops-api
- baseURL: https://www.awardclaw.com/api/v1
  baseurl_source: declared
  description: The Me API from AwardClaw — 1 operation(s) for me.
  name: AwardClaw Me API
  slug: awardclaw-com-me-api
- baseURL: https://www.awardclaw.com/api/v1
  baseurl_source: declared
  description: The News API from AwardClaw — 1 operation(s) for news.
  name: AwardClaw News API
  slug: awardclaw-com-news-api
- baseURL: https://www.awardclaw.com/api/v1
  baseurl_source: declared
  description: The Watches API from AwardClaw — 1 operation(s) for watches.
  name: AwardClaw Watches API
  slug: awardclaw-com-watches-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/awardclaw-com/agentic-access/awardclaw-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/awardclaw-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/awardclaw-com/rate-limits/awardclaw-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/awardclaw-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/awardclaw-com/plans/awardclaw-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/awardclaw-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/awardclaw-com/rules/awardclaw-com-rules.yml
  title: ''
  type: Spectral
  url: rules/awardclaw-com-rules.yml
- group: design
  href: https://artifacts.apis.io/awardclaw-com/json-ld/awardclaw-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/awardclaw-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/awardclaw-com/vocabulary/awardclaw-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/awardclaw-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/awardclaw-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/awardclaw-com/data-model/awardclaw-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/awardclaw-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/awardclaw-com/conventions/awardclaw-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/awardclaw-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/awardclaw-com/errors/awardclaw-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/awardclaw-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/awardclaw-com/conformance/awardclaw-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/awardclaw-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/awardclaw-com/llms/awardclaw-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/awardclaw-com-llms.txt
- group: build
  href: https://artifacts.apis.io/awardclaw-com/mcp/awardclaw-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/awardclaw-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/awardclaw-com/mcp/awardclaw-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/awardclaw-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/awardclaw-com/hosts/awardclaw-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/awardclaw-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/awardclaw-com/vendors/awardclaw-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/awardclaw-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/awardclaw-com/authentication/awardclaw-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/awardclaw-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/awardclaw-com/security/awardclaw-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/awardclaw-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.awardclaw.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.awardclaw.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.awardclaw.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.awardclaw.com/developers
- group: operate
  title: ''
  type: Support
  url: https://www.awardclaw.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.awardclaw.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.awardclaw.com/upgrade?from=pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.awardclaw.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.awardclaw.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.awardclaw.com/privacy
created: '2026-11-02'
description: AwardClaw is a 24/7 award travel research service that scans eight airline loyalty programs every three hours for saver‑priced business and first‑class award seats, aggregates news, credit‑card offers, and community insights into a daily briefing, and provides real‑time drop alerts via email and a JSON API for Pro users.
image: https://www.awardclaw.com/icon-512.png
json_schemas:
- name: Drop
  property_count: 15
  slug: awardclaw-com-drop
- name: WatchInput
  property_count: 8
  slug: awardclaw-com-watch-input
jsonld:
- class_count: 4
  name: Awardclaw Com Context
  property_count: 26
  slug: awardclaw-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.awardclaw.com.
  name: AwardClaw MCP Server
  slug: awardclaw-com-mcp-yml
modified: '2026-11-02'
name: AwardClaw
nav: Providers
network: true
overview: 'AwardClaw publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Availability API, Briefing API, Cards API, and 4 more. Tagged areas include Travel, Awards, Airlines, flight-deals, and Automation.


  The AwardClaw catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AwardClaw''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Awardclaw Com Plans Pricing
  plan_count: 3
  slug: awardclaw-com-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Awardclaw Com Rate Limits
  slug: awardclaw-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: AwardClaw API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: awardclaw-com-rules
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 26
    catalog_earned: 79.8
    catalog_earned_first_party: 20.0
    catalog_gap: 35.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 55.5
    developer_ergonomics: 36.2
    discoverability: 65.0
    operational_transparency: 21.1
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: unknown
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
security:
- kind: authentication
  name: Awardclaw Com Authentication
  slug: awardclaw-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Awardclaw Com Domain Security
  slug: awardclaw-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: search-drops
  slug: awardclaw-com-search-drops
slug: awardclaw-com
tags:
- Travel
- Awards
- Airlines
- flight-deals
- Automation
- Newsletters
website: https://www.awardclaw.com/
---
