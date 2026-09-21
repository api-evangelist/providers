---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.8
  scored_at: '2026-09-20'
api_count: 1
apis:
- baseURL: https://agent.yuens.me
  baseurl_source: declared
  description: 'Anonymous JSON API over one candidate''s published professional profile: ask a natural-language question (queryProfile), score the candidate against a job description (matchJob), and read the structure'
  name: Resume Agent API
  slug: resume-agent-api
artifact_total: 6
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/yuens-me/refs/heads/main/security/yuens-me-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/yuens-me/refs/heads/main/llms/yuens-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/yuens-me-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.yuens.me/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/yuens-me/refs/heads/main/a2a/yuens-me-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/yuens-me-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/yuens-me/refs/heads/main/well-known/yuens-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yuens-me-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/yuens-me/refs/heads/main/packages/yuens-me-packages.yml
  title: ''
  type: Packages
  url: packages/yuens-me-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/yuens-me/refs/heads/main/plans/yuens-me-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/yuens-me-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/yuens-me/refs/heads/main/changelog/yuens-me-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/yuens-me-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/yuens1002/resume-agent/blob/main/CHANGELOG.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/yuens-me/refs/heads/main/regulatory/yuens-me-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/yuens-me-regulatory-posture.yml
created: '2026-09-19'
description: 'Sunny Yuen is an independent full-stack engineer who operates a self-sovereign "Resume Agent": a machine-queryable professional profile served from agent.yuens.me for employer AI systems, ATS tools and personal assistants. The surface is an anonymous six-operation REST API described by a published OpenAPI 3.1 document, a public remote MCP server exposing an ask_candidate tool, and an A2A 1.0 agent card, with the agent''s identity tied to the yuens.me domain through an Ed25519 fingerprint published in DNS (Open Employment Protocol Phase 1). The software is MIT-licensed and published as a fork-ready reference implementation.'
image: https://www.yuens.me/og-default.jpg
layout: provider
mcp_servers:
- description: ''
  name: Sunny Yuen MCP Server
  slug: sunny-yuen-mcp-server
modified: '2026-09-19'
name: Sunny Yuen
nav: Providers
network: true
overview: 'Sunny Yuen publishes 1 API on the [APIs.io](https://apis.io/) network: Resume Agent API. Tagged areas include Company, AI Agents, A2A, MCP, and Resume.


  Sunny Yuen''s developer surface includes GitHub presence, support, changelog, and 12 more developer resources.'
plans:
- name: Yuens Me Plans Pricing
  plan_count: 0
  slug: yuens-me-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Yuens Me Rate Limits
  slug: yuens-me-rate-limits
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 32.2
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 44.2
    developer_ergonomics: 47.0
    discoverability: 75.9
    operational_transparency: 42.1
  previous_composite: 2.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Yuens Me Authentication
  slug: yuens-me-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Yuens Me Domain Security
  slug: yuens-me-domain-security
  summary_line: TLSv1.3
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
- Open-Source
website: https://yuens.me/
---
