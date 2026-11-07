---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://www.pathwren.workers.dev
  baseurl_source: spec
  description: The whole dataset in several shapes.
  name: AI Crawler Index Bulk API
  slug: pathwren-bulk-api
- baseURL: https://www.pathwren.workers.dev
  baseurl_source: spec
  description: One record per crawler.
  name: AI Crawler Index Crawlers API
  slug: pathwren-crawlers-api
- baseURL: https://www.pathwren.workers.dev
  baseurl_source: spec
  description: Operator-published prefixes, normalised.
  name: AI Crawler Index Ip Ranges API
  slug: pathwren-ip-ranges-api
- baseURL: https://www.pathwren.workers.dev
  baseurl_source: spec
  description: Ready-made robots.txt policy files.
  name: AI Crawler Index Robots API
  slug: pathwren-robots-api
- baseURL: https://www.pathwren.workers.dev
  baseurl_source: spec
  description: Freshness of the upstream sources.
  name: AI Crawler Index Status API
  slug: pathwren-status-api
artifact_total: 18
common:
- group: operate
  href: https://artifacts.apis.io/pathwren/rate-limits/pathwren-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pathwren-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pathwren.workers.dev/.well-known/x402
- group: other
  href: https://artifacts.apis.io/pathwren/overlays/pathwren-ai-crawler-index-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pathwren-ai-crawler-index-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://pathwren.workers.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.pathwren.workers.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pathwren.workers.dev/api.html
- group: operate
  title: ''
  type: Support
  url: https://www.pathwren.workers.dev/about.html
- group: commercial
  title: ''
  type: License
  url: https://creativecommons.org/publicdomain/zero/1.0/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.pathwren.workers.dev/status.html
- group: operate
  href: https://artifacts.apis.io/pathwren/changelog/pathwren-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pathwren-changelog.yml
- group: agent
  href: https://artifacts.apis.io/pathwren/well-known/pathwren-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pathwren-well-known.yml
- group: auth
  href: https://artifacts.apis.io/pathwren/well-known/pathwren-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pathwren-security.txt
- group: auth
  href: https://artifacts.apis.io/pathwren/security/pathwren-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/pathwren-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/pathwren/security/pathwren-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pathwren-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/pathwren/security/pathwren-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pathwren-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/pathwren/llms/pathwren-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pathwren-llms.txt
- group: agent
  href: https://artifacts.apis.io/pathwren/mcp/pathwren-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pathwren-mcp.yml
- group: other
  href: https://artifacts.apis.io/pathwren/a2a/pathwren-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/pathwren-a2a.yml
- group: agent
  href: https://artifacts.apis.io/pathwren/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/pathwren/packages/pathwren-packages.yml
  title: ''
  type: Packages
  url: packages/pathwren-packages.yml
- group: design
  href: https://artifacts.apis.io/pathwren/conformance/pathwren-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pathwren-conformance.yml
- group: design
  href: https://artifacts.apis.io/pathwren/lifecycle/pathwren-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pathwren-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/pathwren/plans/pathwren-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pathwren-plans-pricing.yml
created: '2026-08-31'
description: 'Every AI crawler on the web, what it is for, what blocking it costs you, and the IP ranges its operator publishes — as JSON, CSV, robots.txt and regex. 56 crawlers from 30 operators, 1887 IPv4 and 1056 IPv6 prefixes mirrored from 12 operator-published endpoints and refreshed every six hours. Read-only static files: no key, no signup, no rate limit, CORS open, CC0.'
finops:
- has_sources: true
  method: derived
  name: Pathwren Finops
  primary_unit: ''
  service_category: ''
  slug: pathwren-finops
  template: true
image: https://www.pathwren.workers.dev/icon.png
json_schemas:
- name: Crawler
  property_count: 17
  slug: pathwren-crawler.schema
layout: provider
mcp_servers:
- description: Remote MCP server at www.pathwren.workers.dev over streamable HTTP; 9 tools listed.
  name: AI Crawler Index MCP Server
  slug: pathwren-mcp-yml
modified: '2026-09-16'
name: AI Crawler Index
nav: Providers
network: true
overview: 'AI Crawler Index publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bulk API, Crawlers API, Ip Ranges API, and 2 more. Tagged areas include AI crawlers, web crawlers, Robots.txt, User Agents, and Bot Detection.


  The AI Crawler Index catalog on APIs.io includes 1 Spectral governance ruleset.


  AI Crawler Index''s developer surface includes pricing, documentation, support, changelog, and 19 more developer resources.'
plans:
- name: Pathwren Plans Pricing
  plan_count: 1
  slug: pathwren-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Pathwren Rate Limits
  slug: pathwren-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: AI Crawler Index API Rules
  rule_count: 54
  severity_counts:
    error: 43
    hint: 0
    info: 5
    warn: 6
  slug: pathwren-rules
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 49.9
    catalog_earned_first_party: 8.0
    catalog_gap: 65.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 26.3
    contract_governance: 31.8
    contract_quality: 45.6
    developer_ergonomics: 56.5
    discoverability: 73.3
    operational_transparency: 42.1
  previous_composite: 47.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/pathwren/pathwren-2026-09-02T150912.png
security:
- kind: authentication
  name: Pathwren Authentication
  slug: pathwren-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Pathwren Domain Security
  slug: pathwren-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pathwren Vulnerability Disclosure
  slug: pathwren-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: build-robots-policy
  slug: pathwren-build-robots-policy
- name: identify-crawler
  slug: pathwren-identify-crawler
- name: monitor-index-freshness
  slug: pathwren-monitor-index-freshness
- name: verify-crawler-ip
  slug: pathwren-verify-crawler-ip
slug: pathwren
tags:
- AI crawlers
- web crawlers
- Robots.txt
- User Agents
- Bot Detection
- GPTBot
- ClaudeBot
- crawler IP ranges
- Llms.txt
- Open Data
- A2A
website: https://pathwren.workers.dev
---
