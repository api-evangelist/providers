---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: three_quarters
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://agent.yuens.me
  baseurl_source: declared
  description: The Availability API from Sunny Yuen — 1 operation(s) for availability.
  name: Sunny Yuen Availability API
  slug: yuens-me-availability-api
- baseURL: https://agent.yuens.me
  baseurl_source: declared
  description: The Info API from Sunny Yuen — 1 operation(s) for info.
  name: Sunny Yuen Info API
  slug: yuens-me-info-api
- baseURL: https://agent.yuens.me
  baseurl_source: declared
  description: The Match API from Sunny Yuen — 1 operation(s) for match.
  name: Sunny Yuen Match API
  slug: yuens-me-match-api
- baseURL: https://agent.yuens.me
  baseurl_source: declared
  description: The Observations API from Sunny Yuen — 1 operation(s) for observations.
  name: Sunny Yuen Observations API
  slug: yuens-me-observations-api
- baseURL: https://agent.yuens.me
  baseurl_source: declared
  description: The Projects API from Sunny Yuen — 1 operation(s) for projects.
  name: Sunny Yuen Projects API
  slug: yuens-me-projects-api
- baseURL: https://agent.yuens.me
  baseurl_source: declared
  description: The Query API from Sunny Yuen — 1 operation(s) for query.
  name: Sunny Yuen Query API
  slug: yuens-me-query-api
artifact_total: 15
common:
- group: operate
  href: https://artifacts.apis.io/yuens-me/rate-limits/yuens-me-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/yuens-me-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://www.yuens.me/blog/
- group: other
  href: https://artifacts.apis.io/yuens-me/capabilities/yuens-me-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/yuens-me-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/yuens-me/mcp/yuens-me-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/yuens-me-mcp.yml
- group: other
  href: https://artifacts.apis.io/yuens-me/overlays/yuens-me-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/yuens-me-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/yuens-me/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/yuens-me/security/yuens-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yuens-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://yuens.me/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/yuens1002
- group: operate
  title: ''
  type: Support
  url: https://github.com/yuens1002/resume-agent/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/yuens1002/resume-agent/blob/main/LICENSE
- group: other
  title: ''
  type: Sitemap
  url: https://www.yuens.me/sitemap.xml
- group: agent
  href: https://artifacts.apis.io/yuens-me/llms/yuens-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/yuens-me-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.yuens.me/llms.txt
- group: other
  href: https://artifacts.apis.io/yuens-me/a2a/yuens-me-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/yuens-me-a2a.yml
- group: agent
  href: https://artifacts.apis.io/yuens-me/well-known/yuens-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yuens-me-well-known.yml
- group: build
  href: https://artifacts.apis.io/yuens-me/packages/yuens-me-packages.yml
  title: ''
  type: Packages
  url: packages/yuens-me-packages.yml
- group: commercial
  href: https://artifacts.apis.io/yuens-me/plans/yuens-me-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/yuens-me-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/yuens-me/changelog/yuens-me-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/yuens-me-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/yuens1002/resume-agent/blob/main/CHANGELOG.md
- group: other
  href: https://artifacts.apis.io/yuens-me/regulatory/yuens-me-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/yuens-me-regulatory-posture.yml
created: '2026-09-19'
description: 'Sunny Yuen is an independent full-stack engineer who operates a self-sovereign "Resume Agent": a machine-queryable professional profile served from agent.yuens.me for employer AI systems, ATS tools and personal assistants. The surface is an anonymous six-operation REST API described by a published OpenAPI 3.1 document, a public remote MCP server exposing an ask_candidate tool, and an A2A 1.0 agent card, with the agent''s identity tied to the yuens.me domain through an Ed25519 fingerprint published in DNS (Open Employment Protocol Phase 1). The software is MIT-licensed and published as a fork-ready reference implementation.'
image: https://www.yuens.me/og-default.jpg
layout: provider
mcp_servers:
- description: Sunny Yuen operates a public, anonymous, remote MCP server at https://agent.yuens.me/public-mcp (Streamable HTTP, stateless, MCP protocol revision 2025-03-26) exposing ONE tool, ask_candidate, which a
  name: Sunny Yuen MCP Server
  slug: yuens-me-mcp-yml
modified: '2026-10-06'
name: Sunny Yuen
nav: Providers
network: true
overview: 'Sunny Yuen publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Availability API, Info API, Match API, and 3 more. Tagged areas include Company, AI Agents, A2A, MCP, and Resume.


  The Sunny Yuen catalog on APIs.io includes 1 Spectral governance ruleset.


  Sunny Yuen''s developer surface includes engineering blog, GitHub presence, support, changelog, and 17 more developer resources.'
plans:
- name: Yuens Me Plans Pricing
  plan_count: 0
  slug: yuens-me-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Yuens Me Rate Limits
  slug: yuens-me-rate-limits
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Sunny Yuen API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: yuens-me-rules
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 0.0
    contract_governance: 31.8
    contract_quality: 46.9
    developer_ergonomics: 32.7
    discoverability: 75.0
    operational_transparency: 42.1
  previous_composite: 36.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/yuens-me/yuens-me-2026-10-11T194006.png
security:
- kind: authentication
  name: Yuens Me Authentication
  slug: yuens-me-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Yuens Me Domain Security
  slug: yuens-me-domain-security
  summary_line: TLSv1.3
skill_count: 3
skills:
- name: yuens-me-ask-candidate
  slug: yuens-me-ask-candidate
- name: yuens-me-browse-evidence
  slug: yuens-me-browse-evidence
- name: yuens-me-score-job-fit
  slug: yuens-me-score-job-fit
slug: yuens-me
tags:
- Company
- AI Agents
- A2A
- MCP
- Resume
- Hiring
- Recruiting
- Professional Profile
- Job Matching
- Open Source
website: https://yuens.me/
---
