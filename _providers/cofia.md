---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 0
artifact_total: 2
common:
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cofia-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cofia-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cofia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cofia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cofia.ai
- group: auth
  title: ''
  type: Security
  url: https://cofia.ai/security
created: '2026-07-17'
description: Cofia is an AI automation platform that learns how a team actually works and automatically builds custom workflow automations without manual setup. By monitoring system events and recognizing repetitive patterns, Cofia proposes and assembles custom agents for tasks like prospect list building, outreach and follow-ups, recruiting pipeline management, and data report creation. The company markets itself as "AI automations that implement themselves." Cofia is a Y Combinator (Winter 2026) company based in New York City, founded by Moses Wayne (formerly Engineering Director at Duolingo) and Paola Martinez (formerly Senior Product Manager at Brilliant.org). It was added to the API Evangelist network as a portfolio-lead stub and enriched with what the company publishes publicly. As of this pass Cofia exposes no public developer API, OpenAPI specification, or documentation surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cofia.png
layout: provider
modified: '2026-07-18'
name: Cofia
nav: Providers
network: true
overview: Cofia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automation, Workflow Automation, and Agents.
random_paper: 4
score:
  band: minimal
  composite: 8.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 8.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Cofia Domain Security
  slug: cofia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cofia Vulnerability Disclosure
  slug: cofia-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cofia
tags:
- Company
- Artificial Intelligence
- Automation
- Workflow Automation
- Agents
- Productivity
- Y Combinator
website: https://cofia.ai
---
