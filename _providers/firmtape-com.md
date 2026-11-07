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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 62.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Firmtape Com Agentic Access
  operation_count: 1
  slug: firmtape-com-agentic-access
  summary_line: 1 operation
api_count: 2
apis:
- baseURL: https://firmtape.com
  baseurl_source: declared
  description: The Levels API from firmtape-com — 1 operation(s) for levels.
  name: firmtape-com Levels API
  slug: firmtape-com-levels-api
- baseURL: https://firmtape.com
  baseurl_source: declared
  description: The Days API from FirmTape — 1 operation(s) for days.
  name: FirmTape Days API
  slug: firmtape-com-days-api
- baseURL: https://firmtape.com
  baseurl_source: declared
  description: The Session API from FirmTape — 1 operation(s) for session.
  name: FirmTape Session API
  slug: firmtape-com-session-api
artifact_total: 14
asyncapis:
- description: ''
  name: Firmtape Com Webhooks
  slug: firmtape-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/firmtape-com/asyncapi/firmtape-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/firmtape-com-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/firmtape-com/changelog/firmtape-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/firmtape-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/firmtape-com/security/firmtape-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/firmtape-com-vulnerability-disclosure.yml
- group: operate
  href: https://artifacts.apis.io/firmtape-com/lifecycle/firmtape-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/firmtape-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/firmtape-com/lifecycle/firmtape-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/firmtape-com-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/firmtape-com/well-known/firmtape-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/firmtape-com-security.txt
- group: auth
  href: https://artifacts.apis.io/firmtape-com/security/firmtape-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/firmtape-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/firmtape-com/vocabulary/firmtape-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/firmtape-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/firmtape-com/data-model/firmtape-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/firmtape-com-data-model.yml
- group: agent
  href: https://artifacts.apis.io/firmtape-com/agentic-access/firmtape-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/firmtape-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/firmtape-com/rate-limits/firmtape-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/firmtape-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/firmtape-com/plans/firmtape-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/firmtape-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/firmtape-com/rules/firmtape-com-rules.yml
  title: ''
  type: Spectral
  url: rules/firmtape-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/firmtape-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/firmtape-com/authentication/firmtape-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/firmtape-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/firmtape-com/errors/firmtape-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/firmtape-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/firmtape-com/conformance/firmtape-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/firmtape-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/firmtape-com/llms/firmtape-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/firmtape-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/firmtape-com/mcp/firmtape-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/firmtape-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/firmtape-com/well-known/firmtape-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/firmtape-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/firmtape-com/hosts/firmtape-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/firmtape-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/firmtape-com/vendors/firmtape-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/firmtape-com-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://firmtape.com/features/live/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://firmtape.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://firmtape.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://firmtape.com/privacy
- group: start
  title: ''
  type: Login
  url: https://firmtape.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://firmtape.com/account/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://firmtape.com/docs/developers/quickstart
- group: auth
  href: https://artifacts.apis.io/firmtape-com/security/firmtape-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/firmtape-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://firmtape.com/
- group: docs
  title: ''
  type: Documentation
  url: https://firmtape.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://firmtape.com/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://firmtape.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://firmtape.com/docs
created: '2026-10-30'
description: Dealer gamma, vanna, charm and the flip, rebuilt from the options tape every second, plus gamma levels for 100+ indexes, ETFs and stocks. LIVE stream paid, REPLAY of 1,000+ finished sessions free, LAB backtests with honest verdicts, MCP for AI assistants. FirmTape provides live dealer gamma (GEX) data for the S&P 500 and over 100 other ETFs, indexes and stocks, delivering second‑by‑second gamma, vanna, charm and wall information. Users can stream live data, replay historic sessions, and back‑test strategies using the Lab. The service offers free delayed data, paid live subscriptions, and a credit‑based Lab for AI assistants.
image: https://firmtape.com/og.png
json_schemas:
- name: LiveLevel
  property_count: 0
  slug: firmtape-com-live-level
layout: provider
mcp_servers:
- description: Remote MCP server at geo.firmtape.com.
  name: FirmTape MCP Server
  slug: firmtape-com-mcp-yml
modified: '2026-10-30'
name: FirmTape
nav: Providers
network: true
overview: 'FirmTape publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: firmtape-com Levels API, Days API, and Session API. Tagged areas include Finance, Data, Analytics, Options, and Gamma.


  The FirmTape catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  FirmTape''s developer surface includes changelog, authentication, API reference, documentation, pricing, getting-started guide, and 29 more developer resources.'
plans:
- name: Firmtape Com Plans Pricing
  plan_count: 19
  slug: firmtape-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 9
  name: Firmtape Com Rate Limits
  slug: firmtape-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: FirmTape API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: firmtape-com-rules
score:
  band: developing
  composite: 47.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 39.9
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 28.6
    contract_governance: 22.0
    contract_quality: 56.6
    developer_ergonomics: 37.4
    discoverability: 65.0
    operational_transparency: 69.7
  previous_composite: 53.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/firmtape-com/firmtape-com-2026-11-03T132051.png
security:
- kind: authentication
  name: Firmtape Com Authentication
  slug: firmtape-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Firmtape Com Domain Security
  slug: firmtape-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Firmtape Com Vulnerability Disclosure
  slug: firmtape-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: get-levels
  slug: firmtape-com-get-levels
slug: firmtape-com
tags:
- Finance
- Data
- Analytics
- Options
- Gamma
website: https://firmtape.com/
---
