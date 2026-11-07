---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://unicornscreener.vc
  baseurl_source: spec
  description: The Agent API from Unicorn Screener — 1 operation(s) for agent.
  name: Unicorn Screener Agent API
  slug: unicorn-screener-agent-api
- baseURL: https://unicornscreener.vc
  baseurl_source: spec
  description: The Autocomplete API from Unicorn Screener — 1 operation(s) for autocomplete.
  name: Unicorn Screener Autocomplete API
  slug: unicorn-screener-autocomplete-api
- baseURL: https://unicornscreener.vc
  baseurl_source: spec
  description: The Request Report API from Unicorn Screener — 1 operation(s) for request report.
  name: Unicorn Screener Request Report API
  slug: unicorn-screener-request-report-api
- baseURL: https://unicornscreener.vc
  baseurl_source: spec
  description: The Screen Status API from Unicorn Screener — 1 operation(s) for screen status.
  name: Unicorn Screener Screen Status API
  slug: unicorn-screener-screen-status-api
artifact_total: 13
common:
- group: other
  href: https://artifacts.apis.io/unicorn-screener/capabilities/unicorn-screener-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/unicorn-screener-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/unicorn-screener/plans/unicorn-screener-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/unicorn-screener-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/unicorn-screener/rate-limits/unicorn-screener-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/unicorn-screener-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://unicornscreener.vc/docs/ai-agents
- group: company
  title: ''
  type: BlogRSS
  url: https://unicornscreener.vc/blog/feed.xml
- group: agent
  href: https://artifacts.apis.io/unicorn-screener/mcp/unicorn-screener-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/unicorn-screener-mcp.yml
- group: other
  href: https://artifacts.apis.io/unicorn-screener/overlays/unicorn-screener-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/unicorn-screener-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/unicorn-screener/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/unicorn-screener/security/unicorn-screener-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unicorn-screener-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unicornscreener.vc
- group: start
  title: ''
  type: DeveloperPortal
  url: https://unicornscreener.vc/docs/ai-agents
- group: company
  title: ''
  type: Blog
  url: https://unicornscreener.vc/blog
- group: operate
  title: ''
  type: Support
  url: https://unicornscreener.vc/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unicornscreener.vc/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unicornscreener.vc/privacy-policy
created: '2026-09-10'
description: 'Startup research and screening over an HTTP JSON API: resolve a company name, look up a startup score and summary, request an asynchronous screening, and follow its status to a permanent web memo. For early-stage company research and comparison.'
finops:
- has_sources: true
  method: derived
  name: Unicorn Screener Finops
  primary_unit: ''
  service_category: ''
  slug: unicorn-screener-finops
  template: true
image: https://unicornscreener.vc/opengraph-image?9ac05864e0a0ce88
layout: provider
mcp_servers:
- description: Candidate MCP tool surface derived from the public keyless Unicorn Screener Agent API. Nobody ships an MCP server today; these tools map 1:1 to the OpenAPI operations an agent can already call over pl
  name: Unicorn Screener (candidate MCP)
  slug: unicorn-screener-candidate-mcp
modified: '2026-10-06'
name: Unicorn Screener
nav: Providers
network: true
overview: 'Unicorn Screener publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Autocomplete API, Request Report API, and 1 more. Tagged areas include Venture Capital, Startups, Company Research, Screening, and Investing.


  The Unicorn Screener catalog on APIs.io includes 1 Spectral governance ruleset.


  Unicorn Screener''s developer surface includes pricing, engineering blog, support, and 12 more developer resources.'
plans:
- name: Unicorn Screener Plans Pricing
  plan_count: 3
  slug: unicorn-screener-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Unicorn Screener Rate Limits
  slug: unicorn-screener-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Unicorn Screener API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: unicorn-screener-rules
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 57.5
    catalog_earned_first_party: 24.0
    catalog_gap: 57.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 63.2
    contract_governance: 13.6
    contract_quality: 51.7
    developer_ergonomics: 39.9
    discoverability: 58.9
    operational_transparency: 31.6
  previous_composite: 43.8
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/unicorn-screener/unicorn-screener-2026-10-11T131416.png
security:
- kind: authentication
  name: Unicorn Screener Authentication
  slug: unicorn-screener-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Unicorn Screener Domain Security
  slug: unicorn-screener-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: unicorn-screener-lookup-startup
  slug: unicorn-screener-lookup-startup
- name: unicorn-screener-request-memo
  slug: unicorn-screener-request-memo
slug: unicorn-screener
tags:
- Venture Capital
- Startups
- Company Research
- Screening
- Investing
- AI Agents
website: https://unicornscreener.vc
---
