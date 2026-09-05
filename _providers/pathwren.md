---
access_model:
  confidence: high
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Which crawler a User-Agent header belongs to, who operates it, whether it documents obeying robots.txt, how to verify it is genuine against the operator's own published IP ranges, and what blocking it
  name: AI Crawler Index
  slug: ai-crawler-index
artifact_total: 9
common:
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
  title: ''
  type: ChangeLog
  url: changelog/pathwren-changelog.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pathwren-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/pathwren-security.txt
- group: auth
  title: ''
  type: Security
  url: security/pathwren-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pathwren-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pathwren-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pathwren-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pathwren-mcp.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/pathwren-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/pathwren-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pathwren-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pathwren-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pathwren-plans-pricing.yml
created: '2026-08-31'
description: 'Every AI crawler on the web, what it is for, what blocking it costs you, and the IP ranges its operator publishes — as JSON, CSV, robots.txt and regex. 56 crawlers from 30 operators, 1887 IPv4 and 1056 IPv6 prefixes mirrored from 12 operator-published endpoints and refreshed every six hours. Read-only static files: no key, no signup, no rate limit, CORS open, CC0.'
image: https://www.pathwren.workers.dev/icon.png
json_schemas:
- name: Crawler
  property_count: 17
  slug: pathwren-crawler.schema
layout: provider
mcp_servers:
- description: Mirrored from the provider's own x-mcp-server property so the canonical reader sees it. Verified 2026-09-01.
  name: AI Crawler Index MCP Server
  slug: ai-crawler-index-mcp-server
- description: ''
  name: AI Crawler Index MCP Server
  slug: ai-crawler-index-mcp-server-2
modified: '2026-09-01'
name: AI Crawler Index
nav: Providers
network: true
overview: 'AI Crawler Index publishes 1 API on the [APIs.io](https://apis.io/) network: AI Crawler Index. Tagged areas include AI crawlers, web crawlers, robots.txt, user agents, and bot detection.


  AI Crawler Index''s developer surface includes documentation, support, changelog, and 16 more developer resources.'
plans:
- name: Pathwren Plans Pricing
  plan_count: 1
  slug: pathwren-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Pathwren Rate Limits
  slug: pathwren-rate-limits
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 51.0
    catalog_earned_first_party: 8.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 41.3
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 44.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 42.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pathwren/refs/heads/main/screenshots/pathwren-2026-09-02T150912.png
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
slug: pathwren
tags:
- AI crawlers
- web crawlers
- robots.txt
- user agents
- bot detection
- GPTBot
- ClaudeBot
- crawler IP ranges
- llms.txt
- open data
website: https://www.pathwren.workers.dev/
---
